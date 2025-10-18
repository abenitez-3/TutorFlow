from pathlib import Path

def load_properties(path: str | Path) -> dict:
    """
    Lee un .properties simple (clave=valor, ignora líneas vacías o que comienzan con #).
    """
    cfg = {}
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No se encontró el archivo de configuración: {p}")

    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg