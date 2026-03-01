# bitacora.md — Bitácora de ingeniería (U1A6)

## 2026-02-18  — U1A4 (telemetría base)
- Actividad: Implementar telemetría mínima por Serial y visualizar/registrar en Node-RED.
- Decisión técnica: Payload mínimo **CSV `t_ms,s`** a **115200 bps** con muestreo estable **50 Hz (FS_MS=20 ms)**.
- Resultado/Evidencia: Flujo Node-RED recibe datos, grafica en dashboard y genera CSV (>=300 muestras).
- Siguiente acción: Mejorar trazabilidad de registro (rutas, encabezado, verificación de pérdidas).

## 2026-02-19 — Incidente 1 (reproducibilidad de registro en Node-RED)
- Actividad: Revisar consistencia de archivo CSV generado por Node-RED.
- Decisión técnica: Unificar ruta de “header” y “append” al mismo archivo, para garantizar encabezado y evitar residuos de corridas previas.
- Resultado/Evidencia: En el flow original se detecta inconsistencia de rutas (header y append a paths distintos).
- Siguiente acción: Documentar el flow como histórico v0.1 y migrar pipeline principal a notebook (v0.2).

## 2026-02-24 — U1A5 (dashboard + calibración en notebook)
- Actividad: Implementar dashboard en notebook y registrar CSV con 2 canales.
- Decisión técnica: Usar **2 ADC (GPIO34, GPIO35)**, muestreo **10 Hz (SAMPLE_MS=100 ms)**, payload **`t_ms,s1,s2`**.
- Resultado/Evidencia: CSV generado con **6363 filas** y `dt=100 ms` constante (fs≈10 Hz).
- Siguiente acción: Formalizar parámetros de calibración en archivo separado y checklist reproducible.

## 2026-02-24 — Incidente 2 (calibración y saturación ADC)
- Actividad: Calibrar con captura NEGRO/BLANCO y evaluar normalización.
- Decisión técnica: Umbral por canal `thr = (NEGRO + BLANCO)/2` y normalización robusta para caso invertido.
- Resultado/Evidencia: Se observa saturación frecuente cerca de 4095 en el dataset, y recalibraciones (thr cambia en el CSV).
- Siguiente acción: Controlar altura/condiciones de iluminación del sensor y repetir calibración con múltiples muestras (promedio/mediana).

## 2026-02-28 — Verificación reproducible (script)
- Actividad: Agregar verificación rápida del CSV para reproducibilidad.
- Decisión técnica: Script `verify_csv.py` que verifica filas>=300, monotonicidad de t_ms y fs estimada.
- Resultado/Evidencia: Verificación PASS para el CSV de muestra.
- Siguiente acción: Añadir evidencia (capturas) y diagrama del pipeline en /docs.

## 2026-03-01 — Versionado (tags) y cierre
- Actividad: Congelar versiones y documentar diferencias.
- Decisión técnica: Etiquetar **v0.1** (Node-RED U1A4) y **v0.2** (Notebook U1A5) con CHANGELOG.
- Resultado/Evidencia: Tags creados y CHANGELOG actualizado.
- Siguiente acción: Elaborar PDF final (2–4 páginas) apuntando a este repositorio y evidencias.
