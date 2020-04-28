from datetime import date, datetime

from app.Config import SERVER_GULAOBURL
from app.Extensions import db
from app.Models import Note_SubCategory, Note_Category
from app.ReturnCode import ReturnCode
from app.ModelSerialize import Serialize, SerializeQuerySet

def options(request):
    ret = []
    for i in Note_Category.query.all():
        ret.append(Serialize(i, obj='obj'))
    return 200,'',ret

def category_list(request):
    table = Note_SubCategory
    fid = request.get('fid')
    if not fid:
        return 201, "父级类目id不能为空", {}

    if not Note_Category.query.filter(Note_Category.id == fid).first():
        return 202, "父级分类不存在", {}

    querys = table.query.filter(table.categoryid == fid).all()
    ret = []
    for i in querys:
        ret.append(Serialize(i, obj='obj'))
    return 200,'',ret

def category_add(request):
    fid = request.get('fid')
    name = request.get('name',None)
    id = request.get('id',None)

    if not name:
        return 201, '子类目名不能为空', {}

    if not id:

        if not fid:
            return 203, "父级类目id不能为空", {}

        if not Note_Category.query.filter(Note_Category.id == fid).first():
            return 204, "父级分类不存在", {}

        if Note_SubCategory.query.filter(Note_SubCategory.name == name).first():
            return 202, '子类目名已存在', {}

        add = Note_SubCategory()
        add.categoryid = int(fid)
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
        o = Note_SubCategory.query.filter(Note_SubCategory.id == id).first()
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

    o = Note_SubCategory.query.filter(Note_SubCategory.id == id).first()
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