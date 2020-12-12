import asyncio
from typing import Dict

import uvicorn
from fastapi import FastAPI

from api import *
from api.consts import *
from config import LoadConfig
from modules import *

app = FastAPI()

logging = None
load_config = None


@app.get("/ping")
def ping() -> Dict:
    """Tests of connection."""
    return pong()


@app.post("/bucket/create")
async def create_bucket(request: Dict) -> Dict:
    """Validates bucket name and username then create bucket.

    Parameters:
        request: Contains username, prefix, bucket name and region.

    Returns:
        A message in dictionary format.
    """
    try:
        global logging
        bucket_operation = Bucket()
        user_prefix_operation = UserPrefix()

        body = {
            "user_name": request.get("user_name"),
            "prefix": request.get("prefix"),
            "bucket_name": request.get("bucket_name"),
            "region": request.get("region")
        }

        user_validation = await asyncio.gather(
            user_prefix_operation.user_prefix_validation(
                user_name=body.get("user_name"), prefix=body.get("prefix")))

        if user_validation[0] is False:
            return Tools.packer(
                status_code=UserPrefixConst.status_code.get("failed"),
                message=UserPrefixConst.status_message.get("failed"))

        bucket_validation = await asyncio.gather(
            bucket_operation.validation_bucket(
                bucket_name=body.get("bucket_name")))

        if bucket_validation[0] is False:
            return Tools.packer(
                status_code=BucketConst.status_code.get("invalid_bucket_name"),
                message=BucketConst.status_message.get("invalid_bucket_name"))

        if body.get("region"):
            return await asyncio.gather(
                bucket_operation.choose_operation(
                    event_name=BucketConst.create_by_region,
                    bucket_name=body.get("bucket_name"),
                    region=body.get("region")))
        else:
            return await asyncio.gather(
                bucket_operation.choose_operation(
                    event_name=BucketConst.create,
                    bucket_name=body.get("bucket_name")))
    except Exception as EX:
        logging.error(EX)
        errors = CustomException(UserPrefixConst.exception_status,
                                 UserPrefixConst.exception_message)
        return Tools.packer(status_code=errors.fault_code,
                            message=errors.fault_message)


def start():
    """Starts server."""
    uvicorn.run(app, host="127.0.0.1", port=8005)


def main():
    """Initializations and configurations."""
    global logging, load_config
    logging = Logging()
    load_config = LoadConfig()
    logging.info('App started')


if __name__ == "__main__":
    main()
    start()
