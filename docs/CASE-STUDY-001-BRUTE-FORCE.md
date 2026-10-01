# SOC Case Study 001 — SSH Password Guessing / Brute Force Detection

> **Environment:** laboratorio controlado / dataset sintético. No representa un incidente real ni actividad observada en una organización.

## Executive Summary

Se analizaron los logs disponibles en este proyecto. El dataset contiene cuatro fallos consecutivos de autenticación SSH contra el usuario `root`, todos desde `203.0.113.45`, entre las 10:15:11 y las 10:15:17 del 2026-09-08.

El patrón es compatible con **password guessing**, pero la muestra no contiene un login exitoso posterior ni evidencia suficiente para afirmar compromiso.

**Triage:** Medium / confianza media.  
**Disposition:** investigar y correlacionar; no confirmar compromiso.

## Evidence

| Campo | Observación |
|---|---|
| Host | `SOC-SERVER` |
| Servicio | `sshd` |
| Usuario objetivo | `root` (invalid user) |
| IP origen | `203.0.113.45` |
| Fallos | 4 |
| Ventana | 6 segundos |
| Puertos origen | 41123–41126 |
| Primer evento | 2026-09-08 10:15:11 |
| Último evento | 2026-09-08 10:15:17 |
| Login exitoso posterior | No observado en el dataset |

## Timeline

- **10:14:02** — login SSH exitoso de `admin` desde `192.168.1.50`.
- **10:15:11** — fallo para usuario inválido `root` desde `203.0.113.45`.
- **10:15:13** — segundo fallo desde la misma IP.
- **10:15:15** — tercer fallo desde la misma IP.
- **10:15:17** — cuarto fallo desde la misma IP.

Los eventos web posteriores son independientes en la muestra y no se consideran correlacionados sin evidencia adicional.

## Detection / Analyst Reasoning

El análisis agrupa los fallos por **IP de origen + usuario + servicio + ventana temporal**. Cuatro intentos contra el mismo objetivo en seis segundos constituyen una señal que justifica investigación.

El parser actual identifica patrones como `Failed password`; la correlación temporal y la valoración de severidad documentadas aquí representan el **procedimiento de triaje**, no una regla threshold/window que el parser actual implemente por sí solo.

## IOC

- IP: `203.0.113.45`
- Username: `root`
- Service: `sshd`

La IP pertenece al espacio **TEST-NET-3**, reservado para documentación. Debe tratarse como indicador de laboratorio, no como reputación maliciosa real.

## MITRE ATT&CK

**T1110.001 — Brute Force: Password Guessing**

El mapeo se utiliza como hipótesis de técnica porque se observan intentos repetidos de autenticación mediante contraseña.

## Triage Decision

**Classification:** Suspicious Authentication Activity / Password Guessing  
**Severity:** Medium  
**Confidence:** Medium  
**Verdict:** no hay evidencia suficiente de compromiso en la muestra.

### Escalate to L2 if

- aparece un login exitoso desde la misma fuente;
- se observan cambios de privilegios;
- aparece ejecución de comandos posterior;
- se identifica persistencia;
- existen otros indicadores correlacionados.

## Recommended L1 Actions

1. Ampliar la ventana temporal.
2. Buscar autenticaciones exitosas desde la misma IP.
3. Validar si `root` y SSH remoto son esperados.
4. Revisar rate limiting / account lockout.
5. Correlacionar procesos y red.
6. Documentar la decisión final.

## False Positives

Podrían existir pruebas internas autorizadas, automatizaciones mal configuradas o scanners de laboratorio. La muestra por sí sola no permite inferir intención.

## Limitations

- Dataset pequeño.
- No existe una vista completa del host.
- No se observa éxito SSH posterior.
- IP reservada para documentación.
- La correlación threshold/window se presenta como procedimiento de triaje, no como capacidad ya implementada por el parser.

## Reproducibility

- `syslog.log` — dataset.
- `docs/CASE-STUDY-001-BRUTE-FORCE.md` — informe.
- `docs/SOC-001-TICKET.md` — ticket.
- `docs/CASE-001-triage.json` — salida estructurada.

## Recruiter Takeaway

Este caso demuestra, a nivel de laboratorio, **log analysis, alert triage, correlación temporal, IOC extraction, MITRE ATT&CK mapping y documentación de incidentes**, manteniendo una separación clara entre evidencia observada e interpretación del analista.
