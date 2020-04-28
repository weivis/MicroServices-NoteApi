from datetime import date, datetime

from app.Config import SERVER_GULAOBURL
from app.Extensions import db
from app.Models import Note_Category
from app.ReturnCode import ReturnCode
from app.ModelSerialize import Serialize, SerializeQuerySet

def category_list(request):
    querys = Note_Category.query.all()
    ret = []
    for i in querys:
        ret.append(Serialize(i, obj='obj'))
    return 0,0,ret

def category_add(request):
    name = request.get('name',None)
    id = request.get('id',None)

    if not name:
        return 201, '类目名不能为空', {}

    if not id:
        if Note_Category.query.filter(Note_Category.name == name).first():
            return 202, '类目名已存在', {}

        add = Note_Category()
        add.name = name
        add.create_time = datetime.now()
        db.session.add(add)

        try:
            db.session.commit()
            return 200, '添加成功', {}

        except Exception as error:
            print(error)
            db.session.rollback()
            return 401, '添加失败', {}
        
    else:
        o = Note_Category.query.filter(Note_Category.id == id).first()
        if not o:
            return 301, '需要修改的类目不存在', {}

        o.name = name

        try:
            db.session.commit()
            return 200, '编辑成功', {}

        except Exception as error:
            print(error)
            db.session.rollback()
            return 402, '修改失败', {}
        

def category_del(request):
    id = request.get('id',None)
    if not id:
        return 201, '类目id不能为空', {}

    o = Note_Category.query.filter(Note_Category.id == id).first()
    if not o:
        return 202, '类目不存在', {}

    db.session.delete(o)
    try:
        db.session.commit()
        return 200, '删除成功', {}

    except Exception as error:
        print(error)
        db.session.rollback()
        return 400, '删除失败', {}