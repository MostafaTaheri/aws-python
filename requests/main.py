import json
import logging
from http import HTTPStatus
from typing import Dict

import requests
import uvicorn
from fastapi import FastAPI

from config import LoadConfig

app = FastAPI()

config = None


@app.get("/ping")
def ping():
    """Tests of connection."""
    global config
    response = requests.get(url=config.api_url('ping'))
    return response.json()


@app.post("/bucket/create")
def create_bucket(request: Dict) -> Dict:
    """Sends a request for create bucket.

    Parameters:
        request: Contains username, prefix, bucket name and region.

    Returns:
        A message in dictionary format.
    """
    global config

    body = {
        "user_name": request.get("user_name"),
        "prefix": request.get("bucket_name")[0:5],
        "bucket_name": request.get("bucket_name"),
        "region": request.get("region")
    }

    response = requests.post(url=config.api_url('bucket'),
                             data=json.dumps(body),
                             headers={'content-type': 'application/json'})

    if response.status_code == HTTPStatus.OK:
        return response.json()


def start():
    """Starts server."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


def main():
    """Initializations and configurations."""
    global config
    config = LoadConfig()
    logging.basicConfig(filename=config.logging_info(),
                        filemode=config.logging_mode(),
                        format=config.logging_format(),
                        datefmt=config.logging_date_format())
    logging.info('App Started')


if __name__ == "__main__":
    main()
    start()
