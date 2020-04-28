from app.subcategory import subcategory, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@subcategory.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''子类目列表'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)

@subcategory.route('/add', methods=["POST"])
@requestPOST
def Add(request):
    '''添加子类目'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)

@subcategory.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除子类目'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)