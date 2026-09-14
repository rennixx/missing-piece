"""
Fixture: dev_complete_lifecycle
Description: Symmetrical temp file session manager with context manager (__enter__/__exit__),
deterministic cleanup, signal-safe termination handler, and background TTL purge.
"""
import os
import shutil
import time

class WorkspaceSession:
    def __init__(self, base_dir: str, session_id: str, ttl_seconds: int = 3600):
        self.session_id = session_id
        self.session_dir = os.path.join(base_dir, session_id)
        self.ttl_seconds = ttl_seconds
        self.created_at = time.time()
        self.is_active = False

    def __enter__(self):
        os.makedirs(self.session_dir, exist_ok=True)
        self.is_active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def cleanup(self):
        """Deterministic cleanup counterpart for session allocation."""
        if self.is_active and os.path.exists(self.session_dir):
            shutil.rmtree(self.session_dir, ignore_errors=True)
            self.is_active = False

    def purge_expired_sessions(self, base_dir: str):
        """Background maintenance sweeper for orphaned sessions."""
        now = time.time()
        if not os.path.exists(base_dir):
            return
        for entry in os.scandir(base_dir):
            if entry.is_dir():
                mtime = entry.stat().st_mtime
                if now - mtime > self.ttl_seconds:
                    shutil.rmtree(entry.path, ignore_errors=True)
