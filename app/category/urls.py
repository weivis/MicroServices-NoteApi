from app.category import category, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@category.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''主类目列表

        Param:
            {}
    
        ReturnJson:
            {
                "code": 0,
                "data": [
                    {
                    "create_time": "2020-04-28 23:47:49",
                    "id": 1,
                    "name": "测试编辑"
                    }
                ],
                "msg": "OK"
            }
    '''
    c, m, d = views.category_list(request.json)
    return ReturnRequest(c, m, d)

@category.route('/addandedit', methods=["POST"])
@requestPOST
def AddAndEdit(request):
    '''添加主类目或编辑类目名

        有id时为编辑 无id时为添加

        Param:
            id 需要修改的类目id
            name 类目名

        ReturnCode:
            200 添加成功 or 编辑成功
            201 类目名不能为空
            202 类目名已存在
            301 需要修改的类目不存在
            401 添加失败
            402 修改失败

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "添加成功"
            }

    '''
    c, m, d = views.category_add(request.json)
    return ReturnRequest(c, m, d)

@category.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除主类目
    
        Param:
            id 需要删除的id

        ReturnCode:
            200 删除成功
            201 
            201 类目不存在

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "删除成功"
            }
    
    '''
    c, m, d = views.category_del(request.json)
    return ReturnRequest(c, m, d)