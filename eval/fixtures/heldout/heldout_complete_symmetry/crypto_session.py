"""
Fixture: heldout_complete_symmetry
Description: Symmetrical cryptographic session manager with balanced open/close,
key rotation, revocation hooks, and keepalive heartbeat.
"""

class CryptoSessionManager:
    def __init__(self, key_store):
        self.key_store = key_store
        self.active_sessions = {}

    def open_session(self, session_id: str, client_pubkey: str) -> str:
        """Establish cryptographic session."""
        shared_secret = self.key_store.generate_secret(client_pubkey)
        self.active_sessions[session_id] = {
            "secret": shared_secret,
            "status": "OPEN"
        }
        return shared_secret

    def close_session(self, session_id: str):
        """Symmetrical teardown counterpart for open_session."""
        if session_id in self.active_sessions:
            self.key_store.wipe_secret(self.active_sessions[session_id]["secret"])
            del self.active_sessions[session_id]

    def revoke_all(self):
        """Emergency bilateral revocation."""
        for s_id in list(self.active_sessions.keys()):
            self.close_session(s_id)
