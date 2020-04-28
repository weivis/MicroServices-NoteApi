from app.note import note, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@note.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''笔记列表'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)

@note.route('/get', methods=["POST"])
@requestPOST
def Get(request):
    '''获取单条笔记详细'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)

@note.route('/add', methods=["POST"])
@requestPOST
def Add(request):
    '''添加笔记'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)

@note.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除笔记'''
    c, m, d = 0,0,0
    return ReturnRequest(c, m, d)