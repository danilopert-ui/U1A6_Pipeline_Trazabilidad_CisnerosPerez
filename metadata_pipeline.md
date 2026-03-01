# Metadata del pipeline (U1A6)

## Hardware
- MCU: ESP32 DevKit (30 pines)
- Sensores: 2× TCRT5000 (reflectivo IR) usando salida **analógica (AO)** hacia ADC
- Canales ADC: s1=GPIO34 (ADC1), s2=GPIO35 (ADC1)
- Rango ADC: 12-bit (0–4095), atenuación ADC_11db
- Alimentación sensor: **TBD (3.3 V recomendado)**. Requisito: AO no debe exceder 3.3 V.

## Muestreo
- Periodo de muestreo (firmware): 100 ms
- Frecuencia nominal: 10 Hz
- Fuente de tiempo: t_ms = millis() en ESP32 (ms)

## Telemetría
- Canal: Serial USB (UART over USB)
- Baudrate: 115200 bps
- Formato de mensaje: CSV por línea: `t_ms,s1,s2\n`

## PC/Dashboard
- SO: Windows
- Herramienta: Jupyter Notebook (.ipynb) con controles (ipywidgets) y gráfica en tiempo casi real
- Dependencias Python: pyserial, pandas, matplotlib, ipywidgets, ipympl

## Datos
- CSV de ejemplo: data/raw/U1A6_sample.csv (>=300 filas)
- Parámetros calibración: data/processed/calibration_params.json (min/max/umbral por canal)