# Case Study 003 — Suspicious PowerShell / Process Discovery

> Environment: simulated SOC lab  
> Case ID: SOC-003  
> Category: Endpoint / PowerShell  
> Analyst level: SOC L1  
> Status: Closed — suspicious execution confirmed; compromise not confirmed

## 1. Scenario

The SOC receives an endpoint alert after a user launches an Office-related process that spawns PowerShell with an encoded command.

The investigation focuses on process ancestry, command-line behavior, PowerShell execution and evidence preservation.

All telemetry and indicators in this case are synthetic and intended only for defensive training.

## 2. Initial Alert

Alert source: Endpoint telemetry

Initial signal: WINWORD.EXE creates powershell.exe with an encoded-command parameter.

Initial hypothesis: suspicious script execution potentially associated with phishing or malicious document activity.

## 3. Evidence

| Time (UTC) | Parent | Child | Command line |
|---|---|---|---|
| 10:15:02 | explorer.exe | WINWORD.EXE | WINWORD.EXE "Invoice_Q3.docm" |
| 10:15:17 | WINWORD.EXE | powershell.exe | powershell.exe -NoProfile -EncodedCommand BASE64_REDACTED |
| 10:15:19 | powershell.exe | rundll32.exe | rundll32.exe shell32.dll,Control_RunDLL |

The encoded payload is intentionally redacted. The objective is to demonstrate analyst workflow without providing an operational payload.

## 4. Investigation

### Step 1 — Process ancestry

explorer.exe → WINWORD.EXE → powershell.exe → rundll32.exe

A Microsoft Word process spawning PowerShell is treated as suspicious in this simulated scenario because it is inconsistent with the expected behavior of opening a normal document.

### Step 2 — PowerShell command line

The PowerShell process uses -NoProfile and -EncodedCommand. Encoded PowerShell commands can obscure command content and therefore require additional investigation.

The actual payload is not decoded or reproduced in this portfolio case.

### Step 3 — Child process behavior

PowerShell creates rundll32.exe. The process chain increases suspicion because execution moves from an Office process into PowerShell and then another Windows execution utility.

### Step 4 — Scope validation

Correlate the endpoint alert with Windows process telemetry, PowerShell logging, Windows Security events, EDR telemetry, email security records, recent document downloads and network connections from the affected host.

The available simulated evidence does not establish successful persistence, credential theft or command-and-control.

## 5. Observable Inventory

| Type | Observable | Confidence |
|---|---|---|
| File | Invoice_Q3.docm | Medium |
| Process | WINWORD.EXE → powershell.exe | High |
| Process | powershell.exe → rundll32.exe | High |
| Argument | -EncodedCommand | High |
| Argument | -NoProfile | Medium |

## 6. Timeline

| UTC | Event |
|---|---|
| 10:15:02 | Word document opened |
| 10:15:17 | Word spawned PowerShell |
| 10:15:17 | Encoded PowerShell command observed |
| 10:15:19 | PowerShell spawned rundll32 |
| 10:18:00 | SOC L1 triage initiated |
| 10:23:00 | Process ancestry documented |
| 10:28:00 | Additional telemetry requested |
| 10:35:00 | Suspicious execution classification recorded |

## 7. MITRE ATT&CK Mapping

### T1059.001 — Command and Scripting Interpreter: PowerShell

PowerShell is used as the command/scripting interpreter in the observed process chain.

### T1218.011 — System Binary Proxy Execution: Rundll32

rundll32.exe appears as a child process in the simulated execution chain.

### T1204.002 — User Execution: Malicious File

This mapping is considered as a hypothesis because a macro-enabled Office document initiated the observed chain. The available evidence does not prove that the document was malicious.

## 8. Severity Assessment

Severity: High

Rationale:
- Office spawning PowerShell is a high-interest endpoint behavior.
- The command line uses -EncodedCommand.
- PowerShell subsequently launches rundll32.exe.
- The dataset does not prove persistence, credential theft or successful C2.

## 9. Analyst Decision

Classification: Suspicious PowerShell execution — escalate for endpoint investigation.

Recommended SOC L1 actions:
1. Preserve endpoint telemetry and process tree.
2. Follow the organization's host-isolation procedure if required.
3. Collect PowerShell and EDR telemetry.
4. Search for the same process chain across other endpoints.
5. Identify the origin of Invoice_Q3.docm.
6. Review recent email/download activity.
7. Check for persistence mechanisms and unusual outbound connections.
8. Escalate if malicious payload execution or compromise indicators are confirmed.

## 10. Analyst Conclusion

The process chain is sufficiently suspicious to warrant escalation in this simulated environment. The strongest evidence is the Office → PowerShell → rundll32 ancestry combined with -EncodedCommand.

The case deliberately does not claim malware execution, persistence or compromise because those conclusions require additional endpoint and network evidence.

## 11. Evidence Files

- [Endpoint telemetry](./evidence/CASE-003/endpoint-telemetry.txt)
- [Process tree](./evidence/CASE-003/process-tree.md)
- [Observable inventory](./evidence/CASE-003/observables.md)
- [Investigation timeline](./evidence/CASE-003/timeline.md)
- [SOC ticket](./evidence/CASE-003/SOC-003-TICKET.md)
- [Triage JSON](./evidence/CASE-003/triage.json)

---
Portfolio note: This is a simulated defensive-security exercise created to demonstrate SOC L1 endpoint triage and documentation skills.
