#!/usr/bin/env bash
# zeek_runner.sh - Inicia Zeek pasivamente en la interfaz de red interna del laboratorio
# Fase 2 - Tesis Britney Arratia (UPDS Tarija)

IFACE=${1:-"eth1"}
LOG_DIR=${2:-"/tmp/zeek_logs"}

echo "[*] Preparando directorio de logs: $LOG_DIR"
mkdir -p "$LOG_DIR"
cd "$LOG_DIR" || exit 1

echo "[*] Iniciando Zeek en interfaz $IFACE..."
echo "[*] Presione CTRL+C para detener la captura."

# Ejecutar Zeek escuchando en vivo en la interfaz
exec /opt/zeek/bin/zeek -i "$IFACE" local
