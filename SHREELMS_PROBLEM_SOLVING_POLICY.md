# ShreeLMS Foundation Problem-Solving Policy (v1.0)

**Owner:** ShreeLMS Foundation  
**Applies to:** shreelms.in platform, repositories, maintainers, contributors, partners  
**Effective date:** 2026-03-27

---

## 1. Purpose

This policy defines how ShreeLMS Foundation identifies, prioritizes, solves, and verifies problems across shreelms.in in an open, fair, and repeatable way.

Our objective is to solve the **right problem first**, with measurable outcomes, minimal harm, and full accountability.

---

## 2. Problem-Solving Principles

1. **Human Impact First** — prioritize learner, teacher, and community outcomes over vanity metrics.
2. **Evidence Before Opinion** — decisions must be based on reproducible evidence.
3. **Open by Default** — issue context, analysis, and decisions should be public unless sensitive.
4. **Small Safe Steps** — prefer reversible changes and progressive rollout.
5. **Root Cause Over Patchwork** — permanent fixes are preferred to temporary workarounds.
6. **No-Blame Culture** — focus on systems and process failures, not individuals.
7. **Fast Feedback Loops** — shorten the time from report → diagnosis → fix → verification.

---

## 3. Standard Problem Lifecycle

Every issue must pass through these stages:

1. **Intake**
   - Source: GitHub issue, support channel, security report, monitoring alert, community forum.
   - Required fields: problem statement, affected users, reproduction steps, expected behavior, actual behavior, severity guess.

2. **Triage**
   - Assign severity and ownership within SLA.
   - Confirm if issue is product, process, infra, content, policy, or security.

3. **Diagnosis**
   - Build timeline of failure.
   - Use 5 Whys / Fishbone / incident analysis.
   - Identify root cause and contributing factors.

4. **Decision**
   - Select one of: hotfix, planned fix, experiment, rollback, policy update, or decline with rationale.
   - Record trade-offs and user impact.

5. **Execution**
   - Implement fix with tests, docs, and migration notes.
   - Use feature flags/canary when risk is medium or high.

6. **Verification**
   - Confirm resolution with objective checks (tests, telemetry, user confirmation).
   - Validate no regressions.

7. **Learning & Closure**
   - Publish concise postmortem for major incidents.
   - Add preventive actions to backlog with owner and due date.

---

## 4. Severity Model and SLAs

### Severity Levels

- **SEV-1 Critical:** Data loss, security breach, major service outage, legal/safety risk.
- **SEV-2 High:** Key workflow broken for many users, major performance degradation.
- **SEV-3 Medium:** Partial feature failure, moderate user impact, workaround exists.
- **SEV-4 Low:** Minor bug, UX/content issue, low impact.

### Response Targets

- **SEV-1:** acknowledge ≤ 30 minutes, mitigation start ≤ 1 hour.
- **SEV-2:** acknowledge ≤ 4 hours, work start ≤ 1 business day.
- **SEV-3:** acknowledge ≤ 2 business days.
- **SEV-4:** acknowledge ≤ 5 business days.

---

## 5. Decision Matrix

When multiple solutions exist, teams must score options on:

- user impact,
- implementation risk,
- security/privacy impact,
- time-to-value,
- long-term maintainability,
- interoperability with open standards.

The selected option and rejected alternatives must be documented in issue comments or RFC notes.

---

## 6. Governance and Accountability

- **Incident Commander (for SEV-1/2):** owns coordination and communication.
- **Module Maintainer:** owns technical remediation quality.
- **Policy Steward:** validates compliance impact.
- **Foundation Review Panel:** arbitrates disputed prioritization or unresolved blockers.

No issue may remain unowned after triage.

---

## 7. Communication Rules

1. Use one public source of truth per issue (tracker thread or incident doc).
2. For SEV-1/2, provide periodic status updates until mitigation.
3. Publish closure summary including:
   - what happened,
   - who was impacted,
   - what was fixed,
   - what will prevent recurrence.
4. Never expose personal data or exploit details in public updates.

---

## 8. Security and Privacy Problem Handling

- Security vulnerabilities must follow responsible disclosure process.
- Sensitive details remain private until patch availability.
- Security fixes require regression tests and release notes.
- Privacy incidents require data-impact assessment and legal review where applicable.

---

## 9. Required Artifacts

For each medium-or-higher issue (SEV-1/2/3), maintain:

- issue ticket with owner and severity,
- root-cause analysis notes,
- fix PR(s) linked to issue,
- validation evidence,
- follow-up tasks.

For SEV-1, a postmortem is mandatory within 5 business days.

---

## 10. Metrics (Reviewed Monthly)

ShreeLMS Foundation tracks:

- mean time to acknowledge (MTTA),
- mean time to resolve (MTTR),
- reopen rate,
- regression rate after fix,
- % issues with root-cause analysis,
- % preventive actions completed on time.

Metrics are used to improve systems, not to punish contributors.

---

## 11. Continuous Improvement Cycle

Every month, maintainers and foundation representatives must:

1. review top recurring issue categories,
2. identify one process bottleneck,
3. run one improvement experiment,
4. publish lessons learned.

---

## 12. Policy Exceptions

Exceptions are allowed only when:

- immediate harm reduction is required,
- legal obligations conflict,
- infrastructure emergencies require temporary deviation.

All exceptions must be documented with reason, approver, and expiry date.

---

## 13. Adoption Statement

By contributing to shreelms.in, participants agree to follow this Problem-Solving Policy and uphold transparent, evidence-based, community-first resolution practices.

**ShreeLMS Foundation Principle:** *"Fix fast, learn deeply, and prevent repeat failures."*
