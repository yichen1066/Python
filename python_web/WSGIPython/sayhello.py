def application(env, start_response):
    status = '404 not found'
    start_response(status, [])
    return "file not found"