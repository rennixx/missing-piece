"""
Fixture: heldout_lww_explicit_tradeoff
Description: High-frequency telemetry ingest endpoint.
Explicit architectural comment documents Last-Write-Wins (LWW) tradeoff for throughput.
"""

class TelemetryIngest:
    def __init__(self, db):
        self.db = db

    def record_device_ping(self, device_id: str, battery_pct: int, timestamp: float):
        """
        Architecture Tradeoff Note (RFC-204):
        High-frequency heartbeat telemetry updates use Last-Write-Wins (LWW)
        without optimistic locking or distributed mutexes. Race conditions between
        overlapping network packets are acceptable because readings are monotonically
        superseded and downstream analytics aggregate over 5-minute rolling windows.
        """
        self.db.execute(
            "UPDATE device_status SET battery = ?, last_ping = ? WHERE device_id = ?",
            (battery_pct, timestamp, device_id)
        )
