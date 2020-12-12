import asyncio
from typing import List, AnyStr, Dict

import boto3
from botocore.exceptions import ClientError

from config import LoadConfig
from modules import *
from .consts.bucket_const import BucketConst


class Bucket:
    """uses operations of bucket.

    Example:
        bucket = Bucket()
        bucket.choose_operation(event_name='create_bucket',
            bucket_name='s3', region_name='us-west-2')
    """
    def __init__(self):
        """Initialize the variables."""
        self.consts = BucketConst()
        self.config = LoadConfig()
        self.access_key = self.config.bucket_access_key()
        self.secret_key = self.config.bucket_secret_key()
        self.endpoint = self.config.bucket_endpoint()
        self.service_name = self.config.bucket_service_name()
        self.logging = Logging()
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name=self.service_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=self.endpoint)

    async def choose_operation(self, event_name: AnyStr, **kwargs) -> Dict:
        """Chooses events based on event_name for executes async event."""
        try:
            if event_name == self.consts.create_by_region:
                return await asyncio.gather(
                    self._create_by_region(
                        bucket_name=kwargs.get("bucket_name"),
                        region=kwargs.get("region")))
            elif event_name == self.consts.create:
                return await asyncio.gather(
                    self._create(bucket_name=kwargs.get("bucket_name")))
        except Exception as Ex:
            self.logging.error(Ex)
            error = CustomException(self.consts.exception_status,
                                    self.consts.exception_message)
            return Tools.packer(status=error.fault_code,
                                message=error.fault_message)

    async def _create_by_region(self,
                                bucket_name: AnyStr,
                                region: AnyStr = None) -> Dict:
        """Creates an S3 bucket in a specified region.

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        Parameters:
            bucket_name: The name of bucket to create.
            region: String region to create bucket in, e.g., 'us-west-2'.

        Returns:
            A dictionary of information.
        """
        try:
            self.location = {"LocationConstraint": region}
            self.client.create_bucket(Bucket=bucket_name,
                                      CreateBucketConfiguration=self.location)
        except ClientError as ClientException:
            self.logging.error(ClientException)
            error = CustomException(self.consts.exception_status,
                                    self.consts.exception_message)
            return Tools.packer(status=error.fault_code,
                                message=error.fault_message)
        else:
            return Tools.packer(
                status=self.consts.status_code.get("success"),
                message=self.consts.status_message.get("success"))

    async def _create(self, bucket_name: AnyStr) -> Dict:
        """Creates an S3 bucket.

        Parameters:
            bucket_name: The name of bucket to create.

        Returns:
            A dictionary of information.
        """
        try:
            self.client.create_bucket(Bucket=bucket_name)
        except ClientError as ClientException:
            self.logging.error(ClientException)
            error = CustomException(self.consts.exception_status,
                                    self.consts.exception_message)
            return Tools.packer(status=error.fault_code,
                                message=error.fault_message)
        else:
            return Tools.packer(
                status=self.consts.status_code.get("success"),
                message=self.consts.status_message.get("success"))

    def _get_bucket_list(self) -> List:
        """Gets list of buckets."""
        try:
            self.response = self.client.list_buckets()
            self.buckets = [
                bucket["Name"] for bucket in self.response['Buckets']
            ]
        except ClientError as ClientException:
            self.logging.error(ClientException)
            return None
        return self.buckets

    async def validation_bucket(self, bucket_name: AnyStr) -> bool:
        """Checks the conditions of bucket name and it is not exist.

        Parameters:
            bucket_name: The name of bucket

        Returns:
            True if all condition become true, else False.
        """
        try:
            self.bucket_list = self._get_bucket_list()

            if len(bucket_name) < 3:
                return False
            if self.bucket_list and bucket_name in list(
                    filter(lambda x: x, self.bucket_list)):
                return False
            if not Tools.is_english(context=bucket_name):
                return False
            if Tools.is_invalid_character(context=bucket_name):
                return False
        except ClientError as ClientException:
            self.logging.error(ClientException)
            return False
        return True
