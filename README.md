# Category
# 微服务-个人笔记模块

### 启动方法
    python manager.py runserver

### 创建数据库和迁移数据库

    python manager.py db init
    python manager.py db migrate
    python manager.py db upgrade

## Addandedit(添加主类目或编辑类目名)

#### url
- /category/addandedit

#### method
- POST

#### doc
```
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
```


## Del(删除主类目)

#### url
- /category/del

#### method
- POST

#### doc
```
    
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
```


## List(主类目列表)

#### url
- /category/list

#### method
- POST

#### doc
```
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
```



# Note

## Addoredit(增加或编辑笔记)

#### url
- /note/addoredit

#### method
- POST

#### doc
```
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
```


## Del(删除笔记)

#### url
- /note/del

#### method
- POST

#### doc
```
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
```


## Get(获取单条笔记详细)

#### url
- /note/get

#### method
- POST

#### doc
```
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
```


## List(笔记列表)

#### url
- /note/list

#### method
- POST

#### doc
```
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
```


## Recycler(获取回收站)

#### url
- /note/recycler

#### method
- POST

#### doc
```
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
```


## Renew(恢复回收站内的笔记)

#### url
- /note/renew

#### method
- POST

#### doc
```
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
```



# Subcategory

## Addandedit(添加子类目或编辑子目名)

#### url
- /subcategory/addandedit

#### method
- POST

#### doc
```
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
```


## Del(删除主类目)

#### url
- /subcategory/del

#### method
- POST

#### doc
```
    
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
```


## List(子类目列表)

#### url
- /subcategory/list

#### method
- POST

#### doc
```
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
```


## Options(子类目下拉选项)

#### url
- /subcategory/options

#### method
- POST

#### doc
```
    
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
```



