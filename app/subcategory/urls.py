from app.subcategory import subcategory, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

@subcategory.route('/options', methods=["POST"])
@requestPOST
def options(request):
    '''子类目下拉选项
    
        Param:
            {}

        ReturnCode:
            200 成功

        ReturnJson:
            {
                "code": 200,
                "data": {},
                "msg": "删除成功"
            }
    
    '''
    c, m, d = views.options(request.json)
    return ReturnRequest(c, m, d)

@subcategory.route('/list', methods=["POST"])
@requestPOST
def List(request):
    '''子类目列表

        Param:
            fid 主类目id
    
        ReturnCode:
            200 正常
            201 父级类目id不能为空
            202 父级分类不存在

        ReturnJson:
            {
                "code": 0,
                "data": [
                    {
                    "categoryid": 1,
                    "create_time": "2020-04-29 01:28:41",
                    "id": 1,
                    "name": "测试修改子类目名字"
                    }
                ],
                "msg": "OK"
            }
    '''
    c, m, d = views.category_list(request.json)
    return ReturnRequest(c, m, d)

@subcategory.route('/addandedit', methods=["POST"])
@requestPOST
def AddAndEdit(request):
    '''添加子类目或编辑子目名

        有id时为编辑 无id时为添加

        Param:
            fid 父id
            name 类目名
            id 需要修改的类目id
            
        ReturnCode:
            200 添加成功 or 编辑成功
            201 子类目名不能为空
            202 子类目名已存在
            203 父级类目id不能为空
            204 父级分类不存在
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

@subcategory.route('/del', methods=["POST"])
@requestPOST
def Del(request):
    '''删除主类目
    
        Param:
            id 需要删除的id

        ReturnCode:
            200 删除成功
            201 类目id不能为空
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