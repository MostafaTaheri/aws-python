# AWS SDK for Python Sample Project

A simple Python application illustrating usage of the AWS SDK for Python (also
referred to as `boto3`).

## Requirements

This sample project depends on `boto3`, the AWS SDK for Python, and requires
Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install `boto3` and another requirements by using pip:

```
   pip install -r requirements.txt

```

## Basic Configuration

You need to set up your AWS security credentials before the sample code is able
to connect to AWS. You must set your parameters in config.yml at middleware dicrectory:

    access_key_id = <your access key id>
    secret_access_key = <your secret key>
    endpoint = <your endpoint>
    service_name = <your service name>

## How to use:

At first, you must run request service and middleware service. After that send a request by post method to middleware just for create a bucket.

The sample body:

```
   {
       "user_name": <your username>,
       "bucket_name": <your bucket name>
   }

```