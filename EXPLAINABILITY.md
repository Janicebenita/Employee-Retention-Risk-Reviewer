# Employee Retention Risk Reviewer Explainability

## Decision and Reasoning Process

The agent's decision support combines authorized indicators such as workload trends, engagement feedback, role changes, and development opportunities. Its reasoning lists the observed signals and suggests supportive responses without making disciplinary conclusions.

## Inputs and Data Sources Used

Input data may include aggregated surveys, authorized HR records, workload summaries, and manager-provided context. Protected attributes, private communications, and undisclosed monitoring are excluded as data sources.

## Outputs and Supporting Evidence

The output presents themes, confidence, contributing evidence, and possible retention actions. It avoids definitive claims about individual intent and preserves traceability to authorized records.

## Limits, Constraints, and Known Issues

A core limitation is that workplace signals cannot reliably predict personal choices. The agent is constrained from recommending termination, demotion, adverse treatment, or automated employment action.

## Uncertainty and Human Review

Uncertainty is always reported because context and individual circumstances may be missing. Human HR review and respectful employee engagement are required before action.

## Implementation in This Repository

This repository implements the worker as an OpenGAP declaration: `agent.yaml` defines the evidence inputs and review-oriented output, `SOUL.md` defines the non-discrimination and human-governance policy, and this file documents uncertainty and limits. `README.md` describes the supported retention-review use case.

No HR-system connector, predictive model, or automated employment action exists in the repository. A compatible host may summarize supplied workplace evidence, but it must surface missing context and leave all decisions to authorized HR staff.
