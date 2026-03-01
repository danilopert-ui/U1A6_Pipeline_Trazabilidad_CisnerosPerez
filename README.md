# U1A6 — Bitácora técnica y trazabilidad (pipeline sensor→PC→dashboard)

Este repositorio documenta y permite reproducir el pipeline **ESP32 (2 ADC) → Serial USB → Notebook (dashboard + calibración) → CSV**.

> Nota: El historial incluye una versión previa (**v0.1**) basada en Node-RED (U1A4).  
> El **pipeline principal** de esta entrega es **v0.2** (U1A5: 2 sensores + notebook).

## Estructura del repositorio

- `code/firmware/`: firmware ESP32 (Serial CSV).
- `code/pc_tools/`: notebook dashboard/calibración + script de verificación.
- `code/node_red/`: flow Node-RED (histórico v0.1).
- `data/raw/`: CSV de muestra (>=300 filas).
- `data/processed/`: parámetros de calibración.
- `docs/`: evidencias (capturas/diagramas).

## Quickstart (v0.2 — notebook, recomendado)

### 1.- Firmware ESP32
Archivo: `code/firmware/main.cpp`

- Board: ESP32 DevKit / esp32dev
- Baudrate: 115200
- Muestreo: 100 ms (10 Hz)
- Formato de línea (CSV): `t_ms,s1,s2`
- Pines ADC:
  - `s1 -> GPIO34` (ADC1)
  - `s2 -> GPIO35` (ADC1)

**Opción A (PlatformIO):**
- Usa el stub `code/firmware/platformio.ini`
- En la carpeta del proyecto, ejecuta:
  - `pio run -t upload`
  - `pio device monitor -b 115200`

**Opción B (Arduino IDE):**
- Crea un sketch y copia el contenido de `main.cpp`.
- Compila y sube a tu ESP32.
- Abre Serial Monitor a 115200 y verifica que salen líneas `t_ms,s1,s2`.

### 2.- Dependencias Python (dashboard)
Recomendado: Python 3.10+.

Instala:
- `pyserial`
- `pandas`
- `matplotlib`
- `jupyter`
- `ipywidgets`
- `ipympl` (para `%matplotlib widget`)

Por medio de requirements.txt:
- `python -m pip install -r requirements.txt`

### 3.- Ejecutar el notebook
Notebook: `code/pc_tools/U1A5_Cisneros_Daniel.ipynb`

Configura en la celda de CONFIG:
- `PORT`:
  - Windows: `"COM10"` (ejemplo)
  - macOS: `"/dev/tty.usbserial-XXXX"` o `"/dev/tty.SLAB_USBtoUART"`
  - Linux: `"/dev/ttyUSB0"` o `"/dev/ttyACM0"`

Pasos:
1. Ejecuta las celdas en orden.
2. Activa `Start/Stop` para registrar.
3. Calibra:
   - Coloca sensor sobre **NEGRO** y presiona *Capturar NEGRO*.
   - Coloca sensor sobre **BLANCO** y presiona *Capturar BLANCO*.
4. Cierra con *Cerrar (stop + guardar)*.

Salida:
- CSV generado por el notebook (ruta definida en `CSV_PATH`).

## Verificación rápida del CSV de muestra
CSV: `data/raw/U1A6_sample.csv`

Comando:
- `python code/pc_tools/verify_csv.py data/raw/U1A6_sample.csv`

Se espera observar:
- `rows >= 300`
- `t_ms` monótono
- `fs_est ~ 10 Hz` (según `SAMPLE_MS=100`)

## Versiones
- `v0.1`: telemetría 1 canal + Node-RED (U1A4)
- `v0.2`: 2 canales + notebook de calibración + CSV (U1A5)

Ver `CHANGELOG.md` para detalles.
