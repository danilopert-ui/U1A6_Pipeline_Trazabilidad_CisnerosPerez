# CHANGELOG

## v0.2 — Dashboard/Calibración en notebook (U1A5)
- Firmware ESP32 con 2 canales ADC (`t_ms,s1,s2`) a 10 Hz.
- Notebook con dashboard (RAW + NORM), captura NEGRO/BLANCO y cálculo de umbral por canal.
- Registro CSV con >=300 muestras y columnas de normalización/estado de línea.
- Parámetros de calibración exportados en `data/processed/calibration_params.json`.
- Script `verify_csv.py` para verificación rápida (filas, fs estimada, gaps).

## v0.1 — Telemetría ligera con Node-RED (U1A4)
- Firmware ESP32 1 canal (`t_ms,s`) a 50 Hz (FS_MS=20 ms).
- Flow Node-RED: lectura serial, parseo CSV, gráfica y guardado a CSV.
- Conteo de integridad básico (dup/ooo).
