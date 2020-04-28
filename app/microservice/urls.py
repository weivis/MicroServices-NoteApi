from app.microservice import microservice
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@microservice.route('/', methods=["Get"])
def Home():
    return "微服务模块-笔记 作者:https://github.com/weivis, 在线文档/docs/api/"