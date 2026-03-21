import random
from enum import Enum
from typing import Optional
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


'''

Design a locker system like Amazon Locker where delivery drivers can deposit packages and customers can pick them up using a code.

Requirements:

1. Carrier deposits a package by specifying size (small, medium, large)
   - System assigns an available compartment of matching size
   - Opens compartment and returns access token, or error if no space

2. Upon successful deposit, an access token is generated and returned
   - One access token per package

3. User retrieves package by entering access token
   - System validates code and opens compartment
   - Throws specific error if code is invalid or expired

4. Access tokens expire after 7 days
   - Expired codes are rejected if used for pickup
   - Package remains in compartment until staff removes it

5. Staff can open all expired compartments to manually handle packages
   - System opens all compartments with expired tokens
   - Staff physically removes packages and returns them to sender

6. Invalid access tokens are rejected with clear error messages
   - Wrong code, already used, or expired - user gets specific feedback

Out of scope:
- How the package gets to the locker (delivery logistics)
- How the access token reaches the customer (SMS/email notification)
- Lockout after failed access token attempts
- UI/rendering layer
- Multiple locker stations
- Payment or pricing

'''


class Size(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class Compartment:
    def __init__(self, size: Size):
        self.size = size
        self.occupied = False

    def get_size(self) -> Size:
        return self.size

    def is_occupied(self) -> bool:
        return self.occupied

    def mark_occupied(self) -> None:
        self.occupied = True

    def mark_free(self) -> None:
        self.occupied = False

    def open(self) -> None:
        pass


class AccessToken:
    def __init__(self, code: str, expiration: datetime, compartment: Compartment):
        self.code = code
        self.expiration = expiration
        self.compartment = compartment

    def is_expired(self) -> bool:
        return datetime.now() >= self.expiration

    def get_compartment(self) -> Compartment:
        return self.compartment

    def get_code(self) -> str:
        return self.code


# -------------------------
# SRP: Extract token generation into its own abstraction
# OCP + DIP: Locker depends on abstract TokenGenerator, not a concrete one
# -------------------------
class TokenGenerator(ABC):
    @abstractmethod
    def generate(self, compartment: Compartment) -> AccessToken:
        pass


class RandomTokenGenerator(TokenGenerator):
    def __init__(self, expiry_days: int = 7):
        self.expiry_days = expiry_days
        self._existing_codes: set[str] = set()

    def generate(self, compartment: Compartment) -> AccessToken:
        code = self._unique_code()
        expiration = datetime.now() + timedelta(days=self.expiry_days)
        return AccessToken(code, expiration, compartment)

    def release_code(self, code: str) -> None:
        self._existing_codes.discard(code)

    def _unique_code(self) -> str:
        while True:
            code = f"{random.randint(0, 999999):06d}"
            if code not in self._existing_codes:
                self._existing_codes.add(code)
                return code


# -------------------------
# SRP: Extract compartment lookup into its own class
# -------------------------
class CompartmentManager:
    def __init__(self, compartments: list[Compartment]):
        self.compartments = compartments

    def find_available(self, size: Size) -> Optional[Compartment]:
        for c in self.compartments:
            if c.get_size() == size and not c.is_occupied():
                return c
        return None


class Locker:
    def __init__(self, compartments: list[Compartment], token_generator: TokenGenerator = None):
        self.compartment_manager = CompartmentManager(compartments)
        self.token_generator = token_generator or RandomTokenGenerator()
        self.access_token_mapping: dict[str, AccessToken] = {}

    def deposit_package(self, size: Size) -> str:
        compartment = self.compartment_manager.find_available(size)
        if compartment is None:
            raise Exception(f"No available compartment of size {size}")

        compartment.open()
        compartment.mark_occupied()
        access_token = self.token_generator.generate(compartment)
        self.access_token_mapping[access_token.get_code()] = access_token

        return access_token.get_code()

    def pickup(self, token_code: str) -> None:
        if not token_code:
            raise Exception("Invalid access token code")

        access_token = self.access_token_mapping.get(token_code)
        if access_token is None:
            raise Exception("Invalid access token code")

        if access_token.is_expired():
            raise Exception("Access token has expired")

        compartment = access_token.get_compartment()
        compartment.open()
        self._clear_deposit(access_token)

    def open_expired_compartments(self) -> None:
        expired = [at for at in self.access_token_mapping.values() if at.is_expired()]
        for access_token in expired:
            compartment = access_token.get_compartment()
            compartment.open()
            self._clear_deposit(access_token)

    def _clear_deposit(self, access_token: AccessToken) -> None:
        compartment = access_token.get_compartment()
        compartment.mark_free()
        code = access_token.get_code()
        self.access_token_mapping.pop(code, None)
        if isinstance(self.token_generator, RandomTokenGenerator):
            self.token_generator.release_code(code)