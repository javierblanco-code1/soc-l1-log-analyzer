# CASE-003 — Process Tree

    explorer.exe
    └── WINWORD.EXE "Invoice_Q3.docm"
        └── powershell.exe -NoProfile -EncodedCommand BASE64_REDACTED
            └── rundll32.exe shell32.dll,Control_RunDLL

## Analyst observations

- Office application is the parent of PowerShell.
- PowerShell uses an encoded-command argument.
- PowerShell creates rundll32.exe.
- The complete chain is more informative than any single process event.

The tree is synthetic and does not represent a real endpoint.
