# SOC Ticket — SOC-002

## Incident Information

| Field | Value |
|---|---|
| Ticket | SOC-002 |
| Category | Phishing |
| Priority | P2 — Medium |
| Status | Closed |
| Detection | User report |
| Scope | Simulated single-recipient scenario |
| Compromise | Not confirmed |

## Alert Summary

User reported an email requesting urgent account verification through an external authentication link.

## Evidence

- Sender: `security-alert@example.com`
- Destination: `secure-mail.example.com`
- URL: `https://secure-mail.example.com/verify?session=7f2a91c4`
- Authentication result: DMARC fail
- DKIM: none
- SPF: neutral

## Analysis

The message uses urgency and an authentication lure. The destination domain does not correspond to the claimed Microsoft 365 identity in the scenario. The simulated authentication evidence further increases the likelihood of sender spoofing or unauthorized use of the sending identity.

## Classification

**Confirmed phishing attempt.**

There is no evidence in the scenario proving that the recipient submitted credentials or that an account was compromised.

## Recommended Actions

1. Remove/quarantine matching messages.
2. Block the identified domain/URL through approved security controls.
3. Search mail telemetry for additional recipients.
4. Review authentication logs for suspicious sign-ins after delivery.
5. If interaction occurred, reset credentials and revoke active sessions according to the organization's incident-response procedure.
6. Escalate confirmed compromise indicators to the appropriate incident-response tier.

## Closure Criteria

Close the L1 case when:
- affected messages are contained;
- indicators are documented;
- additional recipients have been checked;
- no suspicious authentication is found, or any findings have been escalated;
- the investigation record is complete.

## Analyst Conclusion

The evidence supports a phishing classification with a plausible credential-theft objective, but does not demonstrate successful compromise.
