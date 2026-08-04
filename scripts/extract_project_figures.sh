#!/usr/bin/env bash
set -euo pipefail

materials_root="${1:-}"
if [[ -z "$materials_root" ]]; then
  echo "Usage: $0 /path/to/my_materials" >&2
  exit 64
fi

repo_root="$(cd "$(dirname "$0")/.." && pwd -P)"
output_dir="$repo_root/images/projects"
mkdir -p "$output_dir"

pair_pdf="$materials_root/job_hunt_kb/Pair counting without binning – a new approach to correlation functions in clustering statistics.pdf"
frdeep_pdf="$materials_root/job_hunt_kb/ApJ_Can_I_trust_you.pdf"
siii_pdf="$materials_root/job_hunt_kb/郭守敬_May23.pdf"

for source in "$pair_pdf" "$frdeep_pdf" "$siii_pdf"; do
  if [[ ! -f "$source" ]]; then
    echo "Missing source PDF: $source" >&2
    exit 66
  fi
done

tmp_dir="$(mktemp -d /tmp/shiyu-project-figures.XXXXXX)"
cleanup() {
  if [[ -n "${tmp_dir:-}" && "$tmp_dir" == /tmp/shiyu-project-figures.* ]]; then
    rm -rf -- "$tmp_dir"
  fi
}
trap cleanup EXIT

render_page() {
  local source="$1"
  local page="$2"
  local prefix="$3"
  pdftoppm -f "$page" -l "$page" -r 200 -png "$source" "$tmp_dir/$prefix" >/dev/null 2>&1
}

render_page "$pair_pdf" 11 pair
render_page "$frdeep_pdf" 12 frdeep_method
render_page "$frdeep_pdf" 19 frdeep_results
render_page "$siii_pdf" 9 siii_method
render_page "$siii_pdf" 12 siii_results

pair_page="$(find "$tmp_dir" -name 'pair-*.png' -print -quit)"
frdeep_method_page="$(find "$tmp_dir" -name 'frdeep_method-*.png' -print -quit)"
frdeep_results_page="$(find "$tmp_dir" -name 'frdeep_results-*.png' -print -quit)"
siii_method_page="$(find "$tmp_dir" -name 'siii_method-*.png' -print -quit)"
siii_results_page="$(find "$tmp_dir" -name 'siii_results-*.png' -print -quit)"

# Crop rectangles are measured on the 200-dpi renders above.
sips -c 285 720 --cropOffset 120 70 "$pair_page" --out "$output_dir/3pcf-method.png" >/dev/null
sips -c 650 1480 --cropOffset 1185 85 "$pair_page" --out "$output_dir/3pcf-validation.png" >/dev/null
sips -c 315 1260 --cropOffset 150 220 "$frdeep_method_page" --out "$output_dir/frdeep-method.png" >/dev/null
sips -c 680 640 --cropOffset 745 930 "$frdeep_results_page" --out "$output_dir/frdeep-results.png" >/dev/null

# Each research slide is already a self-contained figure, so preserve the full slide.
sips -Z 2400 "$siii_method_page" --out "$output_dir/siii-method.png" >/dev/null
sips -Z 2400 "$siii_results_page" --out "$output_dir/siii-results.png" >/dev/null
