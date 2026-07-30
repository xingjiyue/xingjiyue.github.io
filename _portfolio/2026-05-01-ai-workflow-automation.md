---
title: "AI Workflow Automation and Decision Support"
excerpt: "Built a personal n8n and Dify workflow for structured ingestion, evidence retrieval, schema-validated outputs, conditional routing, and human review."
collection: portfolio
permalink: /portfolio/2026-05-01-ai-workflow-automation/
date: 2026-05-01
---

**Personal engineering project · Mar 2026 – May 2026**

This project explored how a multi-stage AI workflow could turn unstructured web and API inputs into traceable, reviewable summaries without treating model output as an autonomous final decision.

**Workflow design.** I used n8n and Dify to coordinate ingestion, normalisation, deduplication, retrieval-augmented generation, and LLM-assisted assessment. Explicit structured-output contracts passed state between stages and made downstream routing predictable.

**Reliability and review.** The workflow included schema validation, conditional routing, retries, error logging, state tracking, email notifications, and human-review checkpoints. Intermediate evidence and decisions were retained so that failures could be isolated and outputs could be checked before action.

**Scope.** This was a personal engineering project rather than a production or commercial deployment. Its value lies in modular workflow design, traceability, and controlled use of language models.

**Skills:** n8n, Dify, RAG, structured outputs, workflow orchestration, validation, retry handling, logging, human-in-the-loop review.
