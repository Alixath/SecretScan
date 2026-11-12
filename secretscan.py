import os
import sys

# Carpetas que el escáner nunca debe visitar
CARPETAS_IGNORADAS = {
    ".git", ".vscode", ".idea",
    "node_modules", "venv", ".venv", "__pycache__",
}

# Extensiones de archivos que no son texto 
EXTENSIONES_IGNORADAS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".webp" 
    ".mp3", ".wav", ".mp4", ".avi", ".mkv", ".mov",
    ".zip", ".tar", ".gz", ".7z", ".rar",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx",
    ".exe", ".dll", ".so", ".o", ".class", ".pyc"
}


def es_archivo_de_texto(nombre):
    """Devuelve True si el archivo debe revisarse, False si hay que saltarlo."""
    extension = os.path.splitext(nombre)[1].lower()
    return extension not in EXTENSIONES_IGNORADAS


def listar_archivos(ruta):
    """Devuelve una lista ordenada con la ruta de cada archivo de texto dentro de 'ruta'."""
    encontrados = []
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        # se quitan las carpetas ignoradas para no entrar
        subcarpetas[:] = [s for s in subcarpetas if s not in CARPETAS_IGNORADAS]
        for nombre in archivos:
            if es_archivo_de_texto(nombre):
                encontrados.append(os.path.join(carpeta_actual, nombre))
    encontrados.sort()
    return encontrados


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 secretscan.py <carpeta>")
        sys.exit(1)

    ruta = sys.argv[1]
    if not os.path.isdir(ruta):
        print(f"Error: '{ruta}' no es una carpeta válida.")
        sys.exit(1)

    archivos = listar_archivos(ruta)
    for archivo in archivos:
        print(archivo)
    print(f"Total: {len(archivos)} archivos")


if __name__ == "__main__":
    main()
