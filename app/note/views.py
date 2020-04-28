from datetime import date, datetime

from app.Config import SERVER_GULAOBURL
from app.Extensions import db
from app.Models import Note_Category, Note_Content, Note_SubCategory
from app.ReturnCode import ReturnCode
from app.ModelSerialize import Serialize, SerializeQuerySet
from app.Kit import PaginatePages

def note_list(request):
    id = request.get('id',None)

    if not id:
        return 201, "获取的类目id不能为空", {}

    if not Note_SubCategory.query.filter(Note_SubCategory.id == id).first():
        return 202, '类目不存在', {}

    querys = Note_Content.query.filter(Note_Content.subcategoryid == id, Note_Content.is_delete == False).all()
    ret = []
    for i in querys:
        ret.append(Serialize(i, obj='obj', dataprocessing='querynotelist'))
    return 200,'',ret

def getanote(request):

    id = request.get('id',None)

    if not id:
        return 201, '笔记id不能为空', {}

    o = Note_Content.query.filter(Note_Content.id == id).first()
    if not o:
        return 202, '笔记不存在', {}

    return 200,'',Serialize(o, obj='obj')

def addoredit(request):

    id = request.get('id',None)
    cid = request.get('cid',None)
    content = request.get('content',None)
    title = request.get('title',None)

    if not content:
        return 203, '笔记内容不能为空', {}

    if not id:
        if not cid:
            return 201, '类目id不能为空', {}

        if not Note_SubCategory.query.filter(Note_SubCategory.id == cid).first():
            return 202, '类目不存在', {}

        add = Note_Content()
        add.note_title = str(title)
        add.note_content = str(content)
        add.subcategoryid = int(cid)
        db.session.add(add)

        try:
            db.session.commit()
            return 200, '添加成功', {}

        except Exception as error:
            print(error)
            db.session.rollback()
            return 400, '添加失败', {}

    else:
        o = Note_Content.query.filter(Note_Content.id == id).first()
        if not o:
            return 204, '要修改的笔记不存在', {}

        o.note_title = str(title)
        o.note_content = str(content)
        
        try:
            db.session.commit()
            return 200, '修改成功', {}

        except Exception as error:
            print(error)
            db.session.rollback()
            return 401, '修改失败', {}

def delnote(request):

    id = request.get('id',None)

    if not id:
        return 201, '笔记id不能为空', {}

    o = Note_Content.query.filter(Note_Content.id == id).first()
    if not o:
        return 202, '笔记不存在', {}

    o.is_delete = True

    try:
        db.session.commit()
        return 200, '删除成功', {}

    except Exception as error:
        print(error)
        db.session.rollback()
        return 400, '删除失败', {}
        
def recycler(request):
    queryPage = PaginatePages(request, None)
    querys = Note_Content.query.filter(Note_Content.is_delete == True).order_by(Note_Content.create_time.desc())
    data_sum, data_item, page_sum = SerializeQuerySet(querys, queryPage)
    ret = Serialize(data_item, obj='list', dataprocessing='querynotelist')
    return 200, '成功', {'result': ret, 'data_sum': data_sum, 'page_sum': page_sum, 'now_page':queryPage}

def renew(request):
    id = request.get('id',None)
    cid = request.get('cid',None)

    if not id:
        return 201, '恢复的笔记id不能为空', {}

    if not cid:
        return 202, '恢复到的类目id不能为空', {}

    if not Note_SubCategory.query.filter(Note_SubCategory.id == cid).first():
        return 203, '类目不存在', {}

    o = Note_Content.query.filter(Note_Content.id == id).first()
    if not o:
        return 204, '笔记不存在', {}

    o.is_delete = False
    o.subcategoryid = int(cid)

    try:
        db.session.commit()
        return 200, '恢复成功', {}

    except Exception as error:
        print(error)
        db.session.rollback()
        return 400, '恢复失败', {}