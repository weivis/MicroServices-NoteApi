from datetime import date, datetime
from app.Extensions import db
from app.ReturnCode import ReturnCode
from app.Config import SERVER_GULAOBURL


from app.Models import Note_Category
def category_list(request):
    all = Note_Category.query.all()
    print(all)
    return 0,0,0

def category_add(request):
    pass

def category_del(request):
    pass