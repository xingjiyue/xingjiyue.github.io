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

**Personal engineering project · Mar 2026 – May 2026**

This project explored how a multi-stage AI workflow could turn unstructured web and API inputs into traceable, reviewable summaries without treating model output as an autonomous final decision.

**Workflow design.** I used n8n and Dify to coordinate ingestion, normalisation, deduplication, retrieval-augmented generation, and LLM-assisted assessment. Explicit structured-output contracts passed state between stages and made downstream routing predictable.

**Reliability and review.** The workflow included schema validation, conditional routing, retries, error logging, state tracking, email notifications, and human-review checkpoints. Intermediate evidence and decisions were retained so that failures could be isolated and outputs could be checked before action.

**Scope.** This was a personal engineering project rather than a production or commercial deployment. Its value lies in modular workflow design, traceability, and controlled use of language models.

**Skills:** n8n, Dify, RAG, structured outputs, workflow orchestration, validation, retry handling, logging, human-in-the-loop review.
