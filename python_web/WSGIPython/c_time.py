import time

def application(env, start_response):
    method = env.get('Method')
    file_path = env.get('Path Info')
    start_response('200 OK', [('Method', method), ('Path Info', file_path)])
    return time.ctime()