# Changelog

All notable changes to the **EDP (Expectation Domain Perception Method)** project
will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] — 2026-07-03

### Added
- **L6 Calibration Layer**: Brier score decomposition, Log score, CRPS,
  calibration curve, and **Hyvärinen score** (normalization-free proper scoring).
- **L7 Conformal Prediction Layer** (2025 frontier): Split Conformal, ACI
  (Adaptive Conformal Inference, distribution-shift robust), AgACI ensemble.
  Provides finite-sample, distribution-free coverage guarantees.
- **Online Bayesian Stacking** (Soft-Bayes) aggregator — arXiv 2505.15638 (2025).
- **Model Diversity (DTVW)** metric — arXiv 2508.07136 (2025).
- **Directed evidence** via `Evidence.outcome_id` field: evidence points to a
  specific outcome, avoiding probability flattening.
- Unified top-level `EDP` class with one-shot `analyze()` (L0→L7).
- `DomainAdapter` abstraction + built-in `GenericDomain` for arbitrary
  "outcomes + signals" problems.
- `EventGraph` supporting chain / fully-connected / custom topologies.
- MCP server exposing 6 tools (`analyze_situation`, `calculate_true_probability`,
  `assess_situation`, `conformal_predict`, `online_aggregate`,
  `evaluate_prediction`).
- `warnings` field mandatory in `analyze()` output.
- Example notebooks: `startup_funding.ipynb` (Series A funding success
  probability), `football_score.ipynb` (match outcome via Glicko-2, no betting
  market signals).
- Top-of-module `⚠️ 风险警示 ⚠️` banners; detailed 5-point warning on
  `AllocationEngine`.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, this `CHANGELOG.md`.

### Changed
- Architecture expanded from 5 layers (V1) to **7 layers**.
- License copyright holder: `SPAF Team` → `EDP Team`.
- `CONTRIBUTING.md` rewritten from SPAF references to EDP V2.0.
- `mcp/README.md` rewritten to match the actual V2.0 tools.
- Repository description and topics aligned with EDP V2.0 scope.

### Fixed
- **P0**: `add_evidence` no longer flattens probabilities for two-outcome
  domains. Directed log-odds update now only boosts the targeted outcome.
- `timedelta.zero` does not exist → `field(default_factory=timedelta)`.
- Concentration constraint no longer re-normalizes single-leg allocation back
  to 1.0 (only normalizes when sum > 1).
- `flow_analyzer.py` `FlowDirection.POSITIVE` bug removed with the module.

### Removed
- `flow_analyzer.py` (merged into `flow_amplification.py`).
- `scheme_designer.py` (merged into `allocation_engine.py`).
- `src/types/protocols.py` (SPAF legacy, unreferenced).
- `skill/` directory (SPAF V1 skill stub, no code, outdated docs).

### Deprecated
- TypeScript/JS implementation under `src/js/` remains at V1 (4.1.0) and is
  marked `LEGACY`. It has not been upgraded to the seven-layer architecture.
  CI runs its jobs with `continue-on-error`. The Python package is the
  authoritative V2.0 implementation.

---

## [4.1.0] — 2026 (legacy)

Initial public version under the SPAF name (Sports Probability Analysis
Framework). Five-layer architecture. Superseded by V2.0; JS port retained as
legacy reference only.

---

[2.0.0]: https://github.com/RewFa-CEO/EDP/releases/tag/v2.0.0
