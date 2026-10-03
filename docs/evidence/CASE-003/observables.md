# CASE-003 — Observable Inventory

| Type | Observable | Confidence | Analyst note |
|---|---|---|---|
| File | Invoice_Q3.docm | Medium | Macro-enabled document in simulated scenario |
| Process chain | WINWORD.EXE → powershell.exe | High | Primary suspicious behavior |
| Process chain | powershell.exe → rundll32.exe | High | Secondary suspicious behavior |
| Argument | -EncodedCommand | High | Command content is intentionally redacted |
| Argument | -NoProfile | Medium | Contextual indicator |

## Validation targets

In a production environment, correlate these observables with:
- EDR process telemetry
- PowerShell Script Block Logging
- Windows Security events
- email gateway telemetry
- proxy/DNS logs
- file reputation and sandboxing controls
