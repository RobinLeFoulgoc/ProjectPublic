import subprocess
import sys
import importlib.util
def package_installed(package_name):
    spec = importlib.util.find_spec(package_name)
    return spec is not None
def installFunc():
    required_packages = [
        "pynsee",
        "pandas",
        "geopandas",
        "matplotlib",
        "descartes",
        "streamlit",
        "joblib",
        "watchdog",
        "psutil"
    ]

    for package in required_packages:
        if not package_installed(package):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                print(f"Erreur lors de l'installation du package {package}")
                sys.exit(1)
