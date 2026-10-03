# SOC Ticket — SOC-003

## Incident Information

| Field | Value |
|---|---|
| Ticket | SOC-003 |
| Category | Suspicious PowerShell / Endpoint |
| Priority | P1 — High |
| Status | Escalate |
| Detection | EDR process-chain alert |
| Host | WS-SOC-014 |
| Compromise | Not confirmed |

## Alert Summary

EDR detected a Microsoft Word process spawning PowerShell with -EncodedCommand, followed by rundll32.exe.

## Evidence

- explorer.exe → WINWORD.EXE
- WINWORD.EXE → powershell.exe
- powershell.exe → rundll32.exe
- PowerShell arguments include -EncodedCommand
- Document: Invoice_Q3.docm

## Analysis

The process ancestry and command-line arguments are suspicious in the simulated environment. The evidence supports escalation for deeper endpoint investigation.

The case does not establish malware execution, persistence, credential theft or command-and-control.

## Classification

Suspicious endpoint execution — escalate.

## Recommended Actions

1. Preserve EDR and Windows event evidence.
2. Follow the organization's host-isolation procedure if required.
3. Collect PowerShell logging and process telemetry.
4. Search for the same process chain across endpoints.
5. Investigate document origin and delivery channel.
6. Review network connections associated with the process tree.
7. Escalate confirmed malicious execution or compromise indicators.

## Closure Criteria

The L1 case should remain escalated until the investigation tier determines whether the process chain was benign, malicious or inconclusive based on additional telemetry.
