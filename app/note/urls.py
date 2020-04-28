from app.note import note, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@note.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''笔记列表

        Param:
            id 子类目id

        ReturnCode:
            201 获取的类目id不能为空
            202 类目不存在

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "添加成功"
            }

    '''
    c, m, d = views.note_list(request.json)
    return ReturnRequest(c, m, d)

@note.route('/get', methods=["POST"])
@requestPOST
def Get(request):
    '''获取单条笔记详细

        Param:
            id 笔记id

        ReturnCode:
            200 正常
            201 笔记id不能为空
            202 笔记不存在

        ReturnJson:
            {
            "code": 200,
            "data": {
                "create_time": "2020-04-29 02:27:04",
                "id": 1,
                "is_delete": false,
                "note_content": "修改后的内容",
                "note_title": "修改后的标题",
                "subcategoryid": 2
            },
            "msg": "OK"
            }
    '''
    c, m, d = views.getanote(request.json)
    return ReturnRequest(c, m, d)

@note.route('/addoredit', methods=["POST"])
@requestPOST
def AddorEdit(request):
    '''增加或编辑笔记

        Param:
            id 笔记id
            cid 类目id
            content 内容
            title 标题

        ReturnCode:
            200 正常
            201 类目id不能为空
            202 类目不存在
            203 笔记内容不能为空
            204 要修改的笔记不存在
            400 添加失败
            401 修改失败

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "修改成功"
            }
    '''
    c, m, d = views.addoredit(request.json)
    return ReturnRequest(c, m, d)

@note.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除笔记

        Param:
            id 笔记id

        ReturnCode:
            200 删除成功
            201 笔记id不能为空
            202 笔记不存在
            400 删除失败

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "删除成功"
            }
    '''
    c, m, d = views.delnote(request.json)
    return ReturnRequest(c, m, d)

@note.route('/recycler', methods=["POST"])
@requestPOST
def recycler(request):
    '''获取回收站

        Param:
            queryPage 获取的页数

        ReturnCode:
            200 成功

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "删除成功"
            }
    '''
    c, m, d = views.recycler(request.json)
    return ReturnRequest(c, m, d)

@note.route('/renew', methods=["POST"])
@requestPOST
def renew(request):
    '''恢复回收站内的笔记

        Param:
            id 被恢复的id
            cid 恢复到的分类

        ReturnCode:
            200 成功
            201 恢复的笔记id不能为空
            202 恢复到的类目id不能为空
            203 类目不存在
            204 笔记不存在
            400 恢复失败

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "恢复成功"
            }
    '''
    c, m, d = views.renew(request.json)
    return ReturnRequest(c, m, d)