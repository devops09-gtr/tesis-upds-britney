#!/usr/bin/env bash
# ========================================================
# setup_linux.sh - Instalador para Ubuntu/Debian en Laboratorio
# Proyecto de Tesis UPDS - Britney Arratia / Ing. Tarifa
# ========================================================

echo "========================================================"
echo "  CONFIGURACION DE ENTORNO EN LINUX (UBUNTU / DEBIAN)"
echo "  Tesis UPDS - Britney Arratia / Tutor: Ing. Tarifa"
echo "========================================================"

# 1. Instalar paquetes de sistema
sudo apt update && sudo apt install -y \
    python3 python3-pip python3-venv \
    tshark tcpdump wireless-tools aircrack-ng iptables net-tools

# 2. Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "[*] Creando entorno virtual Python..."
    python3 -m venv venv
fi

# 3. Activar e instalar librerías
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "[+] Entorno Linux configurado con éxito."
echo "[*] Para activar manualmente ejecuta: source venv/bin/activate"
