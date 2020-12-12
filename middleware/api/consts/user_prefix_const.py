class UserPrefixConst:
    exception_users = ['A', 'B']
    Exception_prefix = 'arvan'
    invalid_prefix = 'You can not use this prefix'
    exception_status = 417
    exception_message = 'Occurred some error'
    status_code = {'failed': 101, 'success': 200}
    status_message = {
        'failed': 'The prefix or username is invalid or is not allowed.',
        'success': 'The operation was success'
    }
    collection_name = {
        'users': 'users',
        'prefixes': 'prefixes',
        'user_prefixes': 'user_prefixes'
    }
