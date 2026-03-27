# RULE-03: Harm Prevention

## Requirement
AI systems must not generate content that enables abuse, violence, self-harm facilitation, or dangerous wrongdoing.

## Mandatory Controls
- Run request risk scoring before model output release.
- Reject high-risk prompts and block harmful outputs.
- Enforce safe mode for youth/public deployments.

## Evidence of Compliance
- Risk scoring documentation.
- Blocked output handling in moderation pipeline.
- Safety regression checks.
