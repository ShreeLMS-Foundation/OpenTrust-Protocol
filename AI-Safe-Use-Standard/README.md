# AI Safe Use Standard (AISUS)

A practical open standard to reduce illegal, unethical, and unsafe AI use.

## Purpose

AISUS helps teams design AI systems that are:

- legally compliant,
- privacy-protective,
- harm-aware,
- transparent,
- accountable.

## Core Model

```text
User Input → Input Filter → AI Model → Output Filter → Risk Score → Final Output
```

## Repository Layout

```text
AI-Safe-Use-Standard/
├── README.md
├── POLICY.md
├── RULES.md
├── RULES/
│   ├── RULE-01-LEGAL-COMPLIANCE.md
│   ├── RULE-02-PRIVACY-PROTECTION.md
│   ├── RULE-03-HARM-PREVENTION.md
│   ├── RULE-04-RESPONSIBLE-USE.md
│   └── RULE-05-TRANSPARENCY.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── IMPLEMENTATION/
│   ├── config.py
│   ├── filter.py
│   ├── risk.py
│   ├── logging_policy.py
│   ├── pipeline.py
│   └── validator.py
└── examples/
    ├── README.md
    └── sample_requests.json
```

## Quick Start

```bash
python AI-Safe-Use-Standard/IMPLEMENTATION/validator.py
```

## Rulebook

Use the separated rules in `RULES/` for policy governance and audits.
