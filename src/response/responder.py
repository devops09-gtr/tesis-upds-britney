"""
responder.py - Modulo de respuesta gradual y automatizada en entorno aislado
Fase 2 - Tesis Britney Arratia (UPDS Tarija)
"""

import time
import logging
import subprocess

logging.basicConfig(
    filename="response_events.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class AutomatedResponder:
    def __init__(self, whitelist_macs=None, dry_run=True):
        self.whitelist_macs = set(whitelist_macs or [])
        self.dry_run = dry_run  # dry_run=False ejecuta comandos reales en Linux

    def handle_incident(self, target_mac, target_ip, reason, score):
        """Ejecuta una respuesta gradual basada en la alerta del modelo."""
        now = time.time()

        if target_mac in self.whitelist_macs:
            logging.warning(f"Alerta sobre MAC en lista blanca ({target_mac}). Accion omitida.")
            return False, "En lista blanca"

        logging.info(f"INCIDENTE DETECTADO - MAC: {target_mac}, IP: {target_ip}, Motivo: {reason}, Score: {score}")

        # Mitigacion: Bloqueo temporal por iptables
        cmd = ["iptables", "-I", "FORWARD", "-m", "mac", "--mac-source", target_mac, "-j", "DROP"]

        if self.dry_run:
            logging.info(f"[SIMULACION] Ejecutando: {' '.join(cmd)}")
            return True, f"Simulado: Bloqueo MAC {target_mac}"
        else:
            try:
                subprocess.run(cmd, check=True)
                logging.info(f"[REALIZADO] Regla de bloqueo aplicada para {target_mac}")
                return True, f"Bloqueo aplicado a {target_mac}"
            except Exception as e:
                logging.error(f"Fallo al ejecutar iptables: {e}")
                return False, str(e)
