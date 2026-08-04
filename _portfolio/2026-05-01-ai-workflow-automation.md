---
title: "AI Workflow Automation and Decision Support"
excerpt: "Built a personal n8n and Dify workflow for structured ingestion, evidence retrieval, schema-validated outputs, conditional routing, and human review."
collection: portfolio
permalink: /portfolio/2026-05-01-ai-workflow-automation/
date: 2026-05-01
category: "Engineering Project"
institution: "Personal engineering project"
role: "Designer and implementer"
period: "Mar–May 2026"
status: "Completed personal project"
research_question: "How can language-model assistance be integrated into a traceable workflow without treating model output as an autonomous final decision?"
built: "Ingestion, normalization, retrieval, schema validation, routing, retry/logging, notification, and review stages."
validation: "Structured schema and state checks plus human-review checkpoints."
result: "A traceable personal workflow prototype; no production or commercial deployment claim."
thumbnail: "/images/projects/ai-workflow.svg"
thumbnail_alt: "AI workflow from web and API ingestion through schema validation, routing, logging, notification, and human review"
thumbnail_caption: "Structured validation and a human checkpoint control whether model-assisted output proceeds to action."
figures:
  - src: "/images/projects/ai-workflow.svg"
    alt: "End-to-end decision-support workflow with validation, retries, state tracking, and human review"
    caption: "The model proposes structured content while schema checks, retry paths, retained evidence, and human review control downstream decisions."
---

## Research question

How can language-model assistance be integrated into a multi-stage workflow while keeping evidence, failure paths, and the final decision reviewable?

## My role

I designed and implemented this personal engineering project from Mar–May 2026, including the data contracts, orchestration logic, retry paths, notifications, and human-review checkpoint.

## At a glance

- **Orchestration:** n8n and Dify
- **Inputs:** web and API content
- **Controls:** structured schemas, conditional routing, retries, logs, and state tracking
- **Scope:** completed personal prototype, not a commercial or production deployment

## What I built

The workflow ingests and normalizes source material, removes duplicates, retrieves supporting evidence, requests schema-constrained model output, validates it, and routes success or failure states to explicit downstream branches.

## Method

Each stage passes structured state rather than prose alone. Validation failures enter controlled retry or review paths; successful outputs retain their supporting evidence. Logging and state records make it possible to identify where an invalid or incomplete result entered the workflow.

{% assign workflow_figure = page.figures[0] %}
{% include academic/figure.html src=workflow_figure.src alt=workflow_figure.alt caption=workflow_figure.caption %}

## Validation

I tested schema enforcement, conditional branches, retry behavior, error logging, email notifications, and human-review handoff. Intermediate evidence and state were retained so individual failures could be inspected without treating the model as an autonomous decision maker.

## Results

The result was a traceable personal workflow prototype with modular ingestion, retrieval, validation, routing, and review stages. No commercial deployment, production ownership, or unsupported performance metric is claimed.

## Outputs

- Reusable workflow architecture and structured-output contracts
- End-to-end validation, logging, notification, and human-review design
