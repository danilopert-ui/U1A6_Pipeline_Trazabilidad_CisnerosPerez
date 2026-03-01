#!/usr/bin/env python3
"""Verificación rápida del CSV de telemetría U1A6.

Uso:
  python code/pc_tools/verify_csv.py data/raw/U1A6_sample.csv
"""

import sys
import pandas as pd
import numpy as np

EXPECTED_COLS_MIN = ["t_ms", "s1", "s2"]

def main():
    if len(sys.argv) < 2:
        print("ERROR: falta ruta CSV. Ej: python code/pc_tools/verify_csv.py data/raw/U1A6_sample.csv")
        sys.exit(2)

    path = sys.argv[1]
    df = pd.read_csv(path)

    # columnas
    missing = [c for c in EXPECTED_COLS_MIN if c not in df.columns]
    if missing:
        print(f"FAIL: faltan columnas mínimas: {missing}")
        sys.exit(1)

    n = len(df)
    print(f"rows: {n}")
    if n < 300:
        print("FAIL: se requieren >=300 filas")
        sys.exit(1)

    # monotonicidad
    t = df["t_ms"].to_numpy()
    mono = np.all(np.diff(t) > 0)
    print(f"t_ms monotonic increasing: {mono}")
    if not mono:
        # reportar primeros puntos problemáticos
        bad = np.where(np.diff(t) <= 0)[0][:5]
        print(f"first non-monotonic indices: {bad.tolist()}")
        sys.exit(1)

    dt = np.diff(t)
    dt_min, dt_med, dt_max = int(dt.min()), float(np.median(dt)), int(dt.max())
    fs_est = 1000.0 / dt_med if dt_med > 0 else float("nan")
    print(f"dt_ms: min={dt_min}  median={dt_med:.1f}  max={dt_max}")
    print(f"fs_est: {fs_est:.3f} Hz")

    # gaps (definición simple)
    gap_thr = 1.5 * dt_med
    gaps = int(np.sum(dt > gap_thr))
    print(f"gaps (dt > {gap_thr:.1f} ms): {gaps}")

    # saturación ADC (señal pegada a 4095)
    for ch in ["s1","s2"]:
        if ch in df.columns:
            sat = float(np.mean(df[ch].to_numpy() >= 4095))
            print(f"{ch} saturation >=4095: {sat*100:.1f}%")

    print("PASS: verificación básica OK")

if __name__ == "__main__":
    main()
