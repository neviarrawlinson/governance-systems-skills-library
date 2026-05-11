# Claude Code Command Guide

This guide documents the Claude Code command layer for the Governance Systems Skills Library.

## Purpose

Commands provide quick entry points for common Governance Systems Engineering workflows. Claude Code plugins can include simple Markdown command files in a root-level `commands/` folder.

## Included Commands

| Command File | Workflow |
|---|---|
| `commands/review-change.md` | Review a change request for governance completeness and CAB readiness. |
| `commands/prepare-cab-summary.md` | Prepare a CAB-ready summary or agenda note. |
| `commands/review-rca.md` | Review an RCA for governance quality and corrective action readiness. |
| `commands/review-audit-evidence.md` | Review audit evidence before submission. |
| `commands/assess-vendor.md` | Review a vendor or SaaS intake request. |
| `commands/review-ai-intake.md` | Review an AI use case intake request. |
| `commands/summarize-governance-metrics.md` | Convert governance metrics into leadership-ready reporting. |

## Command Design Principles

Each command is designed to trigger the right workflow, reference the related skill, produce structured output, and end with a clear next action.
