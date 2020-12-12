class BucketConst:
    create = 'create_bucket'
    create_by_region = 'create_bucket_by_region'
    exception_status = 417
    exception_message = 'Occurred some error'
    status_code = {'invalid_bucket_name': 101, 'success': 200}
    status_message = {
        'invalid_bucket_name': 'The name of bucket is invalid.',
        'success': 'The operation was success'
    }