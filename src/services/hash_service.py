import hashlib
import os

_SCRYPT_N = 2**14
_SCRYPT_R = 8
_SCRYPT_P = 1
_SCRYPT_DKLEN = 32


class HashService:
    @staticmethod
    def hash(text: str) -> str:
        salt = os.urandom(16)
        dk = hashlib.scrypt(
            text.encode("utf-8"),
            salt=salt,
            n=_SCRYPT_N,
            r=_SCRYPT_R,
            p=_SCRYPT_P,
            dklen=_SCRYPT_DKLEN,
        )
        return salt.hex() + "$" + dk.hex()

    @staticmethod
    def verify(text: str, hashed_text: str) -> bool:
        try:
            salt_hex, dk_hex = hashed_text.split("$", 1)
            salt = bytes.fromhex(salt_hex)
            dk = hashlib.scrypt(
                text.encode("utf-8"),
                salt=salt,
                n=_SCRYPT_N,
                r=_SCRYPT_R,
                p=_SCRYPT_P,
                dklen=_SCRYPT_DKLEN,
            )
            return dk.hex() == dk_hex
        except (ValueError, Exception):
            return False
