import asyncio
import unittest

from api.consts.user_prefix_const import UserPrefixConst
from api.user_prefix import UserPrefix


class UserPrefixTest(unittest.TestCase):
    """Executes the test case for user_prefix operations.

    These tests contains green and red.
    """
    def setUp(self) -> None:
        self.user_prefix_cls = UserPrefix()
        self.consts_cls = UserPrefixConst()
        self.fixture_user_name_green = 'A'
        self.fixture_user_name_red = 'C'
        self.fixture_prefix = 'arvan3'

    async def test_user_prefix_validation_green(self):
        """Validates allowed prefix for user."""
        assert await asyncio.gather(
            self.user_prefix_cls.user_prefix_validation(
                user_name=self.fixture_user_name_green, prefix=self.fixture_prefix))

    async def test_user_prefix_validation_red(self):
        """Validates allowed prefix for user."""
        assert await asyncio.gather(
            self.user_prefix_cls.user_prefix_validation(
                user_name=self.fixture_user_name_red, prefix=self.fixture_prefix))
