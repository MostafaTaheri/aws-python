import asyncio
import unittest

from api.bucket import Bucket
from api.consts.bucket_const import BucketConst


class BucketTest(unittest.TestCase):
    """Executes the test case for bucket operations.

    These tests contains green and red.
    """
    def setUp(self) -> None:
        self.bucket_cls = Bucket()
        self.consts_cls = BucketConst()
        self.fixture_create_green = {
            'event': self.consts_cls.create,
            'bucket_name': 'arvan1'
        }
        self.fixture_create_red = {
            'event': self.consts_cls.create,
            'bucket_name': 'arvan@1'
        }
        self.fixture_create_by_region_green = {
            'event': self.consts_cls.create,
            'bucket_name': 'arvan1',
            'region': 'us-west-2'
        }
        self.fixture_create_by_region_red = {
            'event': self.consts_cls.create,
            'bucket_name': 'arvan#1',
            'region': 'us-west-2'
        }

    async def test_create_bucket_green(self):
        """Creates an S3 bucket."""
        assert asyncio.gather(
            self.bucket_cls.choose_operation(
                event_name=self.fixture_create_green.get('event'),
                bucket_name=self.fixture_create_green.get('bucket_name')))

    async def test_create_bucket_red(self):
        """Creates a wrong S3 bucket."""
        assert asyncio.gather(
            self.bucket_cls.choose_operation(
                event_name=self.fixture_create_red.get('event'),
                bucket_name=self.fixture_create_red.get('bucket_name')))

    async def test_create_bucket_by_region_green(self):
        """Creates an S3 bucket in a specified region."""
        assert asyncio.gather(
            self.bucket_cls.choose_operation(
                event_name=self.fixture_create_by_region_green.get('event'),
                bucket_name=self.fixture_create_by_region_green.get(
                    'bucket_name'),
                region=self.fixture_create_by_region_green.get('region')))

    async def test_create_bucket_by_region_red(self):
        """Creates a wrong S3 bucket in a specified region."""
        assert asyncio.gather(
            self.bucket_cls.choose_operation(
                event_name=self.fixture_create_by_region_red.get('event'),
                bucket_name=self.fixture_create_by_region_red.get(
                    'bucket_name'),
                region=self.fixture_create_by_region_red.get('region')))
