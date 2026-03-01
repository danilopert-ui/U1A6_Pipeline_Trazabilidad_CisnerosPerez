# bitacora.md — Bitácora de ingeniería (U1A6)

## 2026-02-18 21:10 — U1A4 (telemetría base)
- Actividad: Implementar telemetría mínima por Serial y visualizar/registrar en Node-RED.
- Decisión técnica: Payload mínimo **CSV `t_ms,s`** a **115200 bps** con muestreo estable **50 Hz (FS_MS=20 ms)**.
- Resultado/Evidencia:
  - Flow histórico: `code/node_red/U1A4_node_red.json`.
  - Node-RED recibe datos y grafica en dashboard; se logró generar dataset >=300 muestras (evidencia histórica en docs).
- Siguiente acción: Mejorar trazabilidad del registro (rutas consistentes, encabezado único y verificación de pérdidas).

## 2026-02-19 19:40 — Incidente 1 (reproducibilidad del registro en Node-RED)
- Actividad: Revisar consistencia del CSV generado por Node-RED.
- Decisión técnica: Unificar ruta de “header” y “append” al mismo archivo para garantizar encabezado y evitar residuos de corridas previas.
- Resultado/Evidencia:
  - En el flow original se detectó inconsistencia de rutas (header y append a paths distintos), degradando reproducibilidad.
  - Decisión de mantener U1A4 como histórico: versión etiquetada como `v0.1` (ver tags del repo).
- Siguiente acción: Migrar pipeline principal a notebook (v0.2) para calibración + logging reproducible.

## 2026-02-24 18:25 — U1A5 (dashboard + calibración en notebook)
- Actividad: Implementar dashboard en notebook y registrar CSV con 2 canales.
- Decisión técnica: Usar **2 ADC (GPIO34, GPIO35)**, muestreo **10 Hz (SAMPLE_MS=100 ms)**, payload **`t_ms,s1,s2`**.
- Resultado/Evidencia:
  - Notebook: `code/pc_tools/U1A5_Cisneros_Daniel.ipynb`.
  - Dataset de muestra guardado como: `data/raw/U1A6_sample.csv`.
  - Verificación: `docs/verify_output.txt` reporta **rows=6363**, **fs_est=10.000 Hz**, `dt_ms min/median/max = 100/100/100`.
- Siguiente acción: Formalizar parámetros de calibración en archivo separado y checklist reproducible.

## 2026-02-24 19:05 — Incidente 2 (calibración y saturación ADC)
- Actividad: Calibrar con captura NEGRO/BLANCO y evaluar normalización.
- Decisión técnica: Umbral por canal `thr = (NEGRO + BLANCO)/2` y normalización robusta para caso invertido.
- Resultado/Evidencia:
  - Parámetros persistidos en: `data/processed/calibration_params.json`.
  - Evidencia de saturación en verificación: `docs/verify_output.txt`
    - `s1 saturation >=4095: 64.6%`
    - `s2 saturation >=4095: 49.6%`
- Siguiente acción: Controlar altura/condiciones de iluminación del sensor y repetir calibración con múltiples muestras (promedio/mediana).

## 2026-02-28 20:30 — Verificación reproducible (script)
- Actividad: Agregar verificación rápida del CSV para reproducibilidad.
- Decisión técnica: Script `code/pc_tools/verify_csv.py` para validar: filas>=300, monotonicidad de `t_ms`, fs estimada y gaps.
- Resultado/Evidencia:
  - Salida guardada y versionada: `docs/verify_output.txt`.
  - Resultados clave: `t_ms monotonic=True`, `gaps(dt>150ms)=0`, `PASS`.
- Siguiente acción: Añadir evidencia visual (capturas) y diagrama del pipeline en `/docs`.

## 2026-03-01 13:10 — Versionado (tags) y cierre
- Actividad: Congelar versiones y documentar diferencias.
- Decisión técnica: Etiquetar **v0.1** (Node-RED U1A4) y **v0.2** (Notebook U1A5) con `CHANGELOG.md`.
- Resultado/Evidencia:
  - Tags publicados: `v0.1` y `v0.2` (en GitHub).
  - Evidencia en repo: `CHANGELOG.md` + historial de commits.
- Siguiente acción: Elaborar PDF final (2–4 páginas) apuntando al repositorio y evidencias.
