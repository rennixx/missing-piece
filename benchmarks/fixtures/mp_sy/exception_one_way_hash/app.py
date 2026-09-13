# MP-SY Exception Fixture: One-way hash intentionally has no decrypt counterpart
import hashlib

class TokenService:
    def hash_token(self, raw_token: str) -> str:
        # One-way cryptographic hash intentionally irreversible
        return hashlib.sha256(raw_token.encode()).hexdigest()
