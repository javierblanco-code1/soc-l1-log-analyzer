# Case Study 002 — Phishing Investigation

> **Environment:** simulated SOC lab  
> **Case ID:** SOC-002  
> **Category:** Phishing / Credential Theft  
> **Analyst level:** SOC L1  
> **Status:** Closed — malicious phishing attempt confirmed

## 1. Scenario

The SOC receives a user report for a suspicious email claiming that the recipient's Microsoft 365 account requires an immediate security verification.

The message uses urgency, requests authentication through an external link, and attempts to resemble a legitimate account-security notification.

All indicators in this case are **synthetic and non-routable / reserved for documentation purposes**.

## 2. Initial Alert

**Alert source:** User-reported suspicious email

**Initial indicators:**
- Sender display name impersonates an account-security function.
- Authentication link points to an external domain.
- Message uses urgency and account-lock language.
- Link contains a session-style query parameter.
- No legitimate Microsoft 365 domain is used for the destination.

**Initial hypothesis:** phishing campaign attempting credential collection.

## 3. Evidence

### Email metadata

| Field | Value |
|---|---|
| From | Microsoft 365 Security <security-alert@example.com> |
| To | analyst@example.org |
| Subject | Urgent: Verify your account within 24 hours |
| Date | 2026-09-30 14:32:11 UTC |
| Message-ID | <soc002-phish-001@example.com> |
| Reply-To | security-alert@example.com |
| Authentication-Results | SPF: neutral; DKIM: none; DMARC: fail |

### Suspicious URL

`https://secure-mail.example.com/verify?session=7f2a91c4`

The destination does not use an official Microsoft domain. The hostname is therefore treated as a phishing IOC in this simulated case.

## 4. Investigation

### Step 1 — Sender analysis

The display name is designed to resemble a security notification, but the sender address uses `example.com` rather than a legitimate Microsoft-owned domain.

**Finding:** sender identity cannot be trusted based on the visible display name.

### Step 2 — Authentication analysis

The simulated authentication results show:
- SPF: neutral
- DKIM: none
- DMARC: fail

These results increase suspicion because the message fails the expected sender-authentication checks represented in the lab evidence.

### Step 3 — URL analysis

The URL uses:
- HTTPS transport;
- a security-themed hostname;
- a `/verify` path;
- a session-like query parameter.

HTTPS alone does **not** establish that a website is legitimate. The relevant indicator is the destination domain and its relationship to the claimed sender.

### Step 4 — User interaction risk

The message attempts to move the user from email directly to an authentication page. If a real user entered credentials, the incident could progress from phishing to account compromise.

## 5. IOC Extraction

| Type | Indicator | Confidence |
|---|---|---|
| Email | security-alert@example.com | Medium |
| Domain | secure-mail.example.com | High |
| URL | https://secure-mail.example.com/verify?session=7f2a91c4 | High |
| Message-ID | <soc002-phish-001@example.com> | Medium |

## 6. Timeline

| UTC | Event |
|---|---|
| 14:32:11 | Suspicious email received |
| 14:34:03 | User reports message to SOC |
| 14:36:20 | SOC L1 begins triage |
| 14:39:12 | Sender/authentication indicators reviewed |
| 14:42:08 | Destination URL identified as suspicious |
| 14:45:17 | IOC set documented |
| 14:48:30 | Phishing classification confirmed |
| 14:52:00 | Recommended containment actions documented |

## 7. MITRE ATT&CK Mapping

### T1566.002 — Phishing: Spearphishing Link

The message attempts to direct the recipient to a malicious or deceptive link.

### T1204.001 — User Execution: Malicious Link

The attack depends on the recipient interacting with the supplied link.

These mappings describe the simulated behavior observed in the case; they do not establish that a real-world compromise occurred.

## 8. Severity Assessment

**Severity: Medium**

Rationale:
- Credential theft is a plausible objective.
- The message contains a direct authentication lure.
- No evidence in the simulated dataset confirms successful credential submission.
- No endpoint compromise or successful account takeover is demonstrated.

## 9. Analyst Decision

**Classification:** Confirmed phishing attempt — no confirmed compromise.

**Recommended SOC L1 actions:**
1. Quarantine/remove matching messages from affected mailboxes.
2. Block the phishing domain and URL at the appropriate email/web security controls.
3. Search for additional recipients using the same indicators.
4. Check authentication logs for successful sign-ins following message delivery.
5. If a user interacted with the link, initiate credential reset and session revocation procedures according to the organization's IR playbook.
6. Escalate if evidence of credential submission, suspicious authentication, or account compromise is identified.

## 10. Analyst Conclusion

The available evidence is consistent with a credential-phishing attempt. The strongest indicators are the failed sender-authentication result, the mismatch between the claimed Microsoft 365 identity and destination domain, and the direct authentication lure.

No successful compromise is claimed because the simulated evidence contains no credential-submission event, successful suspicious login, or endpoint execution.

## 11. Evidence Files

- [Email sample](./evidence/CASE-002/email-sample.eml)
- [Investigation timeline](./evidence/CASE-002/timeline.md)
- [IOC inventory](./evidence/CASE-002/iocs.md)
- [SOC ticket](./evidence/CASE-002/SOC-002-TICKET.md)
- [Triage JSON](./evidence/CASE-002/triage.json)

---
**Portfolio note:** This case is a simulated defensive-security exercise created to demonstrate SOC L1 investigation and documentation skills.
