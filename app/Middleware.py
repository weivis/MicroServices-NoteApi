from functools import wraps

from flask import request
from flask_login import current_user

from app.Common import ReturnRequest
from app.ReturnCode import SystemCode, ReturnCode

# 通用请求----------------------------------------------------------------------------------------------------

def requestPOST(func=None):
    '''
        [POST]通用Post请求
        条件: POST
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(SystemCode.ErrorRequestMethod,'请求方法不对','')
    return wrapper