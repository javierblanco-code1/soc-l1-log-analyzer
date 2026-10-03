# CASE-002 — IOC Inventory

> All indicators are synthetic and use documentation-safe domains.

| Type | Indicator | Confidence | Notes |
|---|---|---|---|
| Email | security-alert@example.com | Medium | Impersonation-style sender |
| Domain | secure-mail.example.com | High | External destination used by phishing lure |
| URL | https://secure-mail.example.com/verify?session=7f2a91c4 | High | Credential-verification lure |
| Message-ID | <soc002-phish-001@example.com> | Medium | Correlates the email artifact |

## Analyst handling

The indicators should be treated as investigation artifacts. In a production environment they would be correlated against:
- secure email gateway telemetry;
- DNS/proxy logs;
- authentication logs;
- endpoint telemetry;
- other messages received by the organization.

No live interaction with the simulated URL is required or recommended.
