# AISUS Rules and Controls

## Input Filtering
- Reject clearly malicious requests.
- Flag ambiguous risky requests for additional review.
- Normalize text before scanning (lowercase, trim, punctuation handling).

## Output Filtering
- Prevent disclosure of sensitive personal data.
- Refuse dangerous instructions.
- Replace unsafe content with a policy-safe response.

## Safe Mode
- In safe mode, any high-risk pattern triggers immediate refusal.
- In normal mode, medium-risk may trigger clarification questions.

## Risk Scoring
- LOW: benign queries.
- MEDIUM: borderline or dual-use content.
- HIGH: explicit illegal, harmful, or abusive intent.

## Auditability
- Keep lightweight security logs for blocked high-risk requests.
- Do not store raw personal data in logs.
