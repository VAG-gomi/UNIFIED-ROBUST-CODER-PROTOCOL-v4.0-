```markdown
# Unified Robust Coder Protocol v4.0

**Civilized Coding Posture · Mythophobic · Reality‑Tested · Formally Aware · Continuously Validated · Observed · Operationally Engineered · Release Managed**

The Unified Robust Coder Protocol is a complete software engineering methodology expressed as an AI prompt. It guides an AI coding assistant through the entire lifecycle—from requirements to deployment and maintenance—with built‑in quality gates, formal verification when needed, and a feedback loop that learns from runtime data.

## Why This Exists

Large AI‑generated codebases suffer from hallucinations, silent assumptions, and missing edge cases. Standard “be careful” prompts are not enough. This protocol provides:

- A **structured pipeline** that prevents skipping critical phases
- **Explicit stop conditions** so dangerous code is never produced
- **Mandatory deliverables** at every step (requirements, architecture, audits…)
- **Risk‑based profiles** so you don’t over‑engineer a simple script
- A **closed feedback loop** that brings runtime observability back into design

It is designed to be used as a single, copy‑paste prompt at the beginning of an AI coding session.

## Features

- 🧠 **S‑1 Robust Coder** — a continuous cognitive frame that enforces virtues (Amanah, Ihsan, …), body‑tests code with OSHF postures, and demands five questions per block.
- 🔧 **S‑2 Pipeline Coder** — a 9‑phase build lifecycle with artifact generation, invariant architecture, dependency audits, integration checks, and shadow audits.
- 📊 **S‑3 Quick 20/20 Score** — lightweight, 8‑dimension quality verdict.
- 🧪 **S‑4 Formal Syntax Narrator** — for safety‑critical modules; derives code as a Hoare‑logic proof with surfaced derivations.
- ✅ **S‑5 Continuous Validation** — prescribes automated tests, static analysis, coverage, benchmarks, and regression gates.
- 📡 **S‑6 Observability** — structured logging, metrics, tracing, health checks, and alerting.
- 📋 **S‑7 Operational Engineering** — architecture decision records (ADRs), versioned contracts, threat modeling, and configuration management.
- 🚀 **S‑8 Project & Release Engineering** — semantic versioning, changelogs, CI/CD, code review, deprecation, and rollback.
- 🔁 **Feedback Loop** — runtime incidents and metrics feed back into design, creating a true iterative lifecycle.
- 📂 **Artifact‑driven** — every phase produces a named document (`requirements.md`, `architecture.md`, …).
- 🛑 **Global stop conditions** — the AI halts when requirements are contradictory, dependencies are hallucinated, or safety is at risk.
- 🎭 **Profiles** — Learning, Professional, Production, Critical — so you can scale rigor up or down.

## Protocol Stack

| Protocol | Role | When Active |
|----------|------|-------------|
| **S‑1**  | Cognitive posture & toolkit | Continuously |
| **S‑2**  | Pipeline lifecycle (9 phases) | Multi‑module / non‑trivial tasks |
| **S‑3**  | Quick 20/20 scoring | Standalone or when formal derivation not used |
| **S‑4**  | Formal Hoare‑logic derivation | Safety‑critical modules |
| **S‑5**  | Validation planning | Post‑implementation |
| **S‑6**  | Observability instrumentation | Post‑deployment |
| **S‑7**  | Operational engineering (ADRs, contracts, threat model) | Production/Critical |
| **S‑8**  | Release engineering | Critical / Production (recommended) |

## Execution Profiles

| Profile | Protocols Active | Typical Use |
|---------|------------------|-------------|
| **Learning** | S‑1 + S‑2 (Phases 1‑6) | Personal projects, prototypes |
| **Professional** | Learning + S‑5 | Team libraries, internal tools |
| **Production** | Professional + S‑6 | Customer‑facing services |
| **Critical** | Production + S‑4 + S‑7 + S‑8 | Payments, auth, safety, compliance |

## Quick Start

1. **Set your profile** – decide how much rigor you need.
2. **Copy the full prompt** – the entire `v4.0` specification (available in the repository) and paste it into your AI coding tool (e.g., Replit AI, ChatGPT Code Interpreter).
3. **Start a coding session** – the AI will announce its profile and begin at Phase 1.
4. **Provide requirements** – the AI will clarify, ask ≤2 questions, and output `requirements.md`.
5. **Proceed through the pipeline** – the AI will generate architecture, audit dependencies, implement (with formal proofs if critical), integrate, run a shadow audit, and produce validation, operations, and release plans.
6. **Deploy with confidence** – the AI will hand you a complete set of artifacts, a 20/20 score, and a self‑test checklist proving everything was followed.

## Artifacts Produced

After a full run you will have:

- `requirements.md` – with traceability matrix and performance budgets
- `architecture.md` – module decomposition, invariants, data model, config management
- `dependency_audit.md` – every external call audited with CERTAIN/UNCERTAIN
- `modules/` – verified code, optionally with formal proof sketches
- `integration_report.md` – system‑wide contract checks
- `shadow_audit.md` – adversary‑inspired attack list, all critical/high resolved
- `validation_plan.md` – test specs, coverage targets, benchmarks
- `operations.md` – observability, ADRs, versioned contracts, threat model, error taxonomy
- `change_log.md` – all post‑Phase‑2 changes tracked with approval
- `data_model.md` – entities, schemas, migration strategy (Production/Critical)
- `maintenance.md` – support windows, deprecation policy (for libraries)
- `release_plan.md` – versioning, changelog, CI/CD, rollback
- `self_test.md` – protocol‑compliance checklist, final PASS/FAIL

Every artifact includes a protocol version lock for full traceability.

## Design Philosophy

- **Mythophobia** – no “I think”, no “should work”. Every assumption must be verified or flagged.
- **Civilized Coding** – the AI treats code like a host treats a guest: it leaves it safer than it found it.
- **Generational Evolution** – the protocol expects to be superseded. It includes a meta‑evolution rule: when a missing inference rule is discovered, the AI proposes a new one instead of silently failing.
- **Honesty about limits** – the AI admits it cannot run code, cannot guarantee concurrency safety, and is not a full proof assistant. Formal derivations are human‑auditable, not machine‑checked.

## Example: Adding Two Numbers Safely

```

User: "I need a function that adds two numbers, but it must never crash."
AI (Learning profile):
Phase 1: requirements.md — "Add two integers; handles overflow gracefully."
Phase 2: architecture.md — "Module: safe_add; invariant: result is algebraic sum or error sentinel."
Phase 3: dependency_audit.md — "No external deps (CERTAIN)."
Phase 4: code with surfaced dry run and Hall of Mirrors (overflow, negative, etc.)
…
Phase 6: shadow audit — "No attack surface. Score: 20/20 SHIPPABLE."

```

## Version Compatibility

- **v4.0** is the first unified release. All previous versions (v3.x) are superseded.
- Future patch versions (v4.0.x) will maintain artifact schema compatibility.

## Repository Contents

- `prompt.md` – the full protocol v4.0 (ready to paste into an AI session)
- `README.md` – this file
- `examples/` – example runs for different profiles
- `project-rules-template.md` – a template for project‑specific overrides

## License

MIT — use it, modify it, embed it in your own tools. Attribution appreciated.

---

*Begin every session with: “Protocol: UNIFIED ROBUST CODER v4.0, Profile: [your choice]”. The protocol does the rest.*
```