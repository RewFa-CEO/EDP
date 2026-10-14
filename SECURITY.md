# Security Policy

## Supported Versions

EDP is an academic-research framework. Security fixes are applied only to the
latest released version.

| Version | Supported          |
|---------|--------------------|
| 2.0.x   | ✅ Latest          |
| < 2.0   | ❌ Not supported   |

## Reporting a Vulnerability

If you discover a security vulnerability in EDP:

1. **Do NOT open a public GitHub issue.**
2. Email the maintainer via a private message through
   [GitHub](https://github.com/RewFa-CEO/EDP), or open a private security
   advisory via GitHub's "Security" → "Advisories" → "Report a vulnerability".
3. Include a clear description of the issue, reproduction steps, and (if
   possible) a minimal proof of concept.

You should receive an acknowledgment within 72 hours. Please allow reasonable
time for investigation and a fix before any public disclosure.

## Scope

EDP is a **probability-analysis research library**, not a production
decision-making system. Within that scope, "security" covers:

- Numerical correctness bugs that could lead to silently wrong probabilities
- Crashes or unhandled exceptions on malformed input
- Path / injection issues in the MCP server

Out of scope:

- **Misuse as financial / betting / gambling advice.** EDP explicitly does NOT
  provide such advice. See the risk warning in the
  [README](README.md). Any decision made on the basis of EDP output is the
  user's sole responsibility.
- Performance issues that do not affect correctness.

## Disclaimer

EDP is for **academic research and educational purposes only**. It is not a
licensed financial product, and its outputs are not professional advice.
