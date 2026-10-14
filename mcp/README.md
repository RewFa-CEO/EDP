# EDP MCP Server

Model Context Protocol (MCP) server for the EDP V2.0 framework.

## ⚠️ Disclaimer

**This server is for ACADEMIC RESEARCH AND EDUCATIONAL PURPOSES ONLY.**

- This framework is for probability analysis and statistical research.
- No system can guarantee results.
- Outputs do **not** constitute any investment advice or decision-making advice.
- Users bear full responsibility for their own decisions.

## Installation

```bash
# 从源码安装（含 MCP 依赖）
pip install -e ".[mcp]"
```

## Configuration

Add to your MCP client configuration (e.g., Claude Desktop):

```json
{
  "mcpServers": {
    "edp": {
      "command": "python",
      "args": ["path/to/EDP/mcp/server.py"]
    }
  }
}
```

## Available Tools (V2.0)

The server exposes the following six tools, mirroring the EDP V2.0 seven-layer architecture.

---

### `analyze_situation`

One-shot analysis running the full L0 → L7 pipeline.

**Parameters:**
- `outcomes` (array): `[{"id": "a", "label": "结果A"}, ...]`
- `evidence` (array, optional): List of evidence dicts
  - `{"id":..., "source_type":..., "probability":..., "outcome_id":..., "confidence":...}`
- `raw_data` (object, optional): `{outcome_id: decimal_quote}` (market quotes)
- `budget` (number, optional): Allocation budget (default: 1000.0)
- `return_multipliers` (object, optional): `{outcome_id: return_multiplier}`

**Returns:** probabilities, summary, prediction_set, coverage_target, allocation, warnings.

---

### `calculate_true_probability`

Shin normalization: extract true probabilities from market quotes.

**Parameters:**
- `quotes` (object): `{outcome_id: decimal_quote}`

**Example:**
```json
{
  "quotes": {"home": 1.50, "draw": 4.20, "away": 6.00}
}
```

**Returns:** `true_probabilities`, `implied_probabilities`, `market_margin`, `method`.

---

### `assess_situation`

Multi-source intelligence fusion (L4 Domain Awareness).

**Parameters:**
- `sources` (array): List of source dicts
  - `{"source_id":..., "evidence_type":..., "probability":..., "reliability_weight":..., "confidence":...}`
- `prior_probability` (number, optional): Prior (default: 0.5)

**Returns:** aggregate_probability, consensus_score, stability, source_count, fusion_method, confidence, anomaly_flags.

---

### `conformal_predict`

Conformal prediction set with finite-sample coverage guarantee (L7).

**Parameters:**
- `predictions` (object): `{outcome_id: probability}`
- `alpha` (number, optional): Miscoverage rate (default: 0.1)
- `method` (string, optional): `"split"` / `"aci"` / `"agaci"` (default: `"aci"`)

**Returns:** `prediction_set`, `coverage_target`, `threshold`, `method`.

---

### `online_aggregate`

Online expert aggregation (Soft-Bayes / EWA / MLPoly / Ridge / OBS).

**Parameters:**
- `predictions` (array): List of `{source_id: probability}` snapshots over time
- `actuals` (array): List of actual values (aligned with predictions)
- `algorithm` (string, optional): Aggregation algorithm (default: `"online_bayesian_stacking"`)

**Returns:** `weights`, `performance`.

---

### `evaluate_prediction`

Prediction calibration evaluation (L6 — Brier, Log, Hyvärinen scores).

**Parameters:**
- `predictions` (object): `{outcome_id: probability}`
- `actual_outcome` (string): The outcome that actually occurred

**Returns:** Brier score, log score, Hyvärinen score, top-1 accuracy, etc.

## Usage with AI Assistants

Once configured, you can use natural language to interact with the EDP framework:

```
User: Calculate the true probability for quotes home 1.5, draw 4.2, away 6.0

AI: I'll calculate the true probabilities via Shin normalization...

[Calls calculate_true_probability tool]

The true probabilities are:
- Home: 63.2%
- Draw: 22.6%
- Away: 15.8%

The market margin is 5.4%.
```

## Development

```bash
# Clone repository
git clone https://github.com/RewFa-CEO/EDP.git
cd EDP/mcp

# Install dependencies
pip install -e ".[dev,mcp]"

# Run server (prints available tools)
python server.py
```

## License

MIT License — See [LICENSE](../LICENSE) file for details.

## Disclaimer

**This server is for ACADEMIC RESEARCH AND EDUCATIONAL PURPOSES ONLY.**

- This server does not constitute any investment advice or decision-making advice.
- Any decisions made using this server are the user's sole responsibility.
- The author is not responsible for any losses incurred through use of this server.
- Please comply with laws and regulations in your jurisdiction.
