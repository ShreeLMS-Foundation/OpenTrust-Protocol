# SHREELMS.IN Open Source Revolution Policy (v1.0)

**Status:** Draft for public review  
**Project:** shreelms.in  
**Model Inspiration:** Linux kernel, GNU communities, Mozilla, Apache, Kubernetes

---

## 1) Mission

shreelms.in adopts an **Open Source First** policy to build digital public infrastructure that is:

- transparent by default,
- community governed,
- secure and auditable,
- reusable for everyone.

We believe code should be a commons, not a black box.

---

## 2) Core Commitments

1. **Open by Default**  
   All non-sensitive software developed for shreelms.in should be published in public repositories.

2. **Merit + Inclusion**  
   Decisions are based on quality, ethics, and community impact — while keeping participation open to newcomers.

3. **No Vendor Lock-In**  
   Architecture must use open standards and portable formats.

4. **Public Accountability**  
   Roadmaps, issues, design docs, and major decisions remain publicly visible.

5. **Security Without Secrecy**  
   Security through peer review, responsible disclosure, and independent audits.

---

## 3) Licensing Policy

### 3.1 Software License

- Default license: **Apache License 2.0**.
- Alternative licenses (MIT, GPLv3, AGPLv3) may be used only with documented reason in the repository.

### 3.2 Content & Documentation

- Docs, policies, and media should use **Creative Commons BY 4.0** unless otherwise specified.

### 3.3 Third-Party Dependencies

- Only dependencies with OSI-approved licenses are allowed.
- License compatibility must be checked before merge.
- A machine-readable `NOTICE`/SBOM must be maintained.

---

## 4) Governance Model (Linux-Inspired, Community-Scaled)

### 4.1 Roles

- **Contributors:** anyone submitting issues, code, docs, tests, translations.
- **Maintainers:** trusted reviewers with merge rights for specific modules.
- **Core Council:** small elected/appointed body for cross-project decisions and conflict resolution.
- **Release Steward:** coordinates release quality, changelogs, and versioning discipline.

### 4.2 Decision Flow

- Small technical decisions: maintainers decide after public discussion.
- Architectural changes: require RFC + community comment period.
- Policy/legal/security-critical changes: Core Council approval required.

### 4.3 Elections & Term Limits

- Core Council terms: 12 months.
- Staggered rotation to avoid concentration of power.
- Public nomination and transparent voting summary.

---

## 5) Contribution Policy

### 5.1 Contribution Standards

Each contribution must include where applicable:

- clear problem statement,
- tests,
- docs updates,
- backward compatibility notes,
- security/privacy impact notes.

### 5.2 Developer Certificate of Origin (DCO)

- Contributions require sign-off (`Signed-off-by`) confirming legal right to contribute.
- CLA may be introduced later if required by institutional partnerships.

### 5.3 Review SLA

- First maintainer response target: **within 5 business days**.
- Urgent security reports handled on priority track.

---

## 6) Code of Conduct & Safe Participation

shreelms.in enforces a strict anti-harassment and anti-discrimination standard.

Unacceptable behavior includes:

- hate speech,
- personal attacks,
- intimidation,
- doxxing,
- sustained bad-faith disruption.

Enforcement actions may include warning, temporary suspension, or permanent ban.

---

## 7) Security & Privacy Policy

1. **Responsible Disclosure Program** with dedicated security contact.
2. **Patch Timelines:**
   - critical: target fix within 72 hours,
   - high: within 7 days,
   - medium: within 30 days.
3. **Mandatory security scanning** in CI (SAST, dependency, secret scanning).
4. **Privacy by Design:** collect minimal user data; document purpose and retention.
5. **Cryptographic integrity** for release artifacts (signed tags/releases).

---

## 8) Open Standards & Interoperability

- APIs should be documented and versioned.
- Data export must be possible in open formats (JSON, CSV, Markdown where relevant).
- Protocol choices should prefer community standards over proprietary interfaces.

---

## 9) Transparency Policy

The following must be public by default:

- roadmap,
- issue tracker,
- release notes,
- architecture decisions,
- governance meeting summaries.

Exceptions allowed only for:

- active security vulnerabilities,
- legal constraints,
- personal sensitive information.

---

## 10) Anti-Exploitation Policy

- Community trust data cannot be sold as an extractive product.
- Any monetization must be value-adding, optional, and transparent.
- Sponsor influence cannot override public governance rules.

---

## 11) Localization & Public Good Mandate

- Documentation should support multilingual contributions.
- Regional communities can create local governance chapters aligned with this policy.
- Public-interest deployments (education, civic, NGOs) receive priority collaboration support.

---

## 12) Implementation Roadmap

### Phase 1 (0–60 days)

- Publish governance files (`CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`).
- Create maintainer map and module ownership.
- Enable automated license and security checks.

### Phase 2 (60–120 days)

- Launch RFC process.
- Start monthly community governance calls.
- Publish first transparency report.

### Phase 3 (120–365 days)

- Establish elected Core Council.
- Run third-party security audit.
- Release annual State of OpenTrust/shreelms report.

---

## 13) Policy Change Process

This policy may evolve via open RFC process:

1. Proposal published publicly,
2. minimum 14-day comment window,
3. maintainer + Core Council review,
4. final decision and rationale published.

No silent policy changes are allowed.

---

## 14) Adoption Statement

By contributing to shreelms.in repositories, participants agree to follow this policy and associated governance documents.

**"Built in public. Governed in public. Trusted in public."**
