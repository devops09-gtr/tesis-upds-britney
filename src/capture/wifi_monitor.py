"""
wifi_monitor.py - Captura y conteo de tramas IEEE 802.11 en modo monitor
Parte de la Fase 2 de Tesis de Grado - Britney Arratia (UPDS Tarija)
"""

import sys
import time
from collections import defaultdict
from scapy.all import sniff, Dot11, Dot11Deauth, Dot11Disas, Dot11Beacon, Dot11ProbeReq

class WifiFrameMonitor:
    def __init__(self, interface="wlan0mon"):
        self.interface = interface
        self.stats = defaultdict(int)
        self.seen_macs = set()
        self.seen_ssids = set()

    def packet_handler(self, pkt):
        if not pkt.haslayer(Dot11):
            return

        # Registrar MACs observadas
        if pkt.addr1: self.seen_macs.add(pkt.addr1)
        if pkt.addr2: self.seen_macs.add(pkt.addr2)

        # 802.11 Type 0: Tramas de Gestión
        if pkt.type == 0:
            if pkt.haslayer(Dot11Deauth):
                self.stats["deauth_count"] += 1
            elif pkt.haslayer(Dot11Disas):
                self.stats["disassoc_count"] += 1
            elif pkt.haslayer(Dot11Beacon):
                self.stats["beacon_count"] += 1
                try:
                    ssid = pkt[Dot11Beacon].info.decode("utf-8", errors="ignore")
                    if ssid:
                        self.seen_ssids.add(ssid)
                except Exception:
                    pass
            elif pkt.haslayer(Dot11ProbeReq):
                self.stats["probe_req_count"] += 1

    def capture_window(self, duration_seconds=60):
        """Captura durante la ventana de observacion y resetea contadores."""
        self.stats.clear()
        self.seen_macs.clear()
        self.seen_ssids.clear()
        
        start_time = time.time()
        sniff(iface=self.interface, prn=self.packet_handler, timeout=duration_seconds, store=False)
        end_time = time.time()

        return {
            "timestamp_start": start_time,
            "timestamp_end": end_time,
            "deauth_count": self.stats["deauth_count"],
            "disassoc_count": self.stats["disassoc_count"],
            "beacon_count": self.stats["beacon_count"],
            "probe_req_count": self.stats["probe_req_count"],
            "unique_macs": len(self.seen_macs),
            "unique_ssids": len(self.seen_ssids)
        }

if __name__ == "__main__":
    iface = sys.argv[1] if len(sys.argv) > 1 else "wlan0mon"
    print(f"[*] Iniciando escucha en {iface} por 10 segundos de prueba...")
    monitor = WifiFrameMonitor(interface=iface)
    try:
        res = monitor.capture_window(duration_seconds=10)
        print("[+] Resultado ventana piloto:", res)
    except Exception as e:
        print(f"[-] Error al capturar: {e}")
        print("[!] Verifica tener permisos de root y la interfaz en modo monitor.")
