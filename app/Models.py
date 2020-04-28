from app.Extensions import db
from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

# 主类目
class Note_Category(db.Model):
    
    __tablename__ = 'note-category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)
    
# 子类目
class Note_SubCategory(db.Model):
    
    __tablename__ = 'note-subcategory'

    id = db.Column(db.Integer, primary_key=True)
    categoryid = db.Column(db.Integer) # 主类目id
    name = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)
    
# 笔记内容
class Note_Content(db.Model):
    
    __tablename__ = 'note-content'

    id = db.Column(db.Integer, primary_key=True)
    subcategoryid = db.Column(db.Integer) # 子类目id
    note_title = db.Column(db.Text)
    note_content = db.Column(LONGTEXT)
    is_delete = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
