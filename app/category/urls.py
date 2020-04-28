from app.category import category, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@category.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''主类目列表'''
    c, m, d = views.category_list(request.json)
    return ReturnRequest(c, m, d)

@category.route('/add', methods=["POST"])
@requestPOST
def Add(request):
    '''添加主类目'''
    c, m, d = views.category_add(request.json)
    return ReturnRequest(c, m, d)

@category.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除主类目'''
    c, m, d = views.category_del(request.json)
    return ReturnRequest(c, m, d)