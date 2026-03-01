# Checklist de reproducibilidad (U1A6)

## 1.- Preparación (Windows)
- [ ] Conectar ESP32 por USB y verificar puerto COM en Administrador de dispositivos.
- [ ] Instalar Python 3.x y dependencias (ver README / requirements).

## 2.- Firmware (ESP32)
- [ ] Cargar firmware `code/firmware/main.cpp` al ESP32.
- [ ] Confirmar Serial a 115200 bps.
- [ ] Confirmar que imprime líneas `t_ms,s1,s2`.

## 3.- Notebook (PC)
- [ ] Abrir `code/pc_tools/U1A5_Cisneros_Daniel.ipynb`.
- [ ] Configurar `PORT = "COMx"` (ej. "COM10") y `BAUD = 115200`.
- [ ] Ejecutar celdas y presionar Start.
- [ ] Verificar que la gráfica actualiza y se muestran lecturas s1/s2.

## 4.- Registro de datos
- [ ] Registrar >=300 muestras.
- [ ] Guardar CSV y copiar muestra como `data/raw/U1A6_sample.csv`.

## 5.- Verificaciones rápidas (pasa/falla)
- [ ] `python code/pc_tools/verify_csv.py data/raw/U1A6_sample.csv` muestra:
  - filas >= 300
  - columnas esperadas presentes
  - fs estimada ~ 10 Hz (tolerancia definida)
  - sin gaps grandes (o gaps contados y documentados)

## 6.- Calibración
- [ ] Capturar NEGRO y BLANCO (ideal: varias muestras por estado).
- [ ] Guardar min/max/umbral por canal en `data/processed/calibration_params.json`.