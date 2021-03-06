# DEBUG 模式
DEBUG = True

# ----------------------------------------------------------------------

# 跨域密钥
SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# ----------------------------------------------------------------------

# 测试服数据库
SQLALCHEMY_DATABASE_URI = "mysql://root:weivimysql@127.0.0.1:3306/noteapi?charset=utf8mb4"

# SQLALCHEMY_DATABASE_URI = "mysql://root:weivimysql@47.94.153.68:3306/weivi-note?charset=utf8mb4"

# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ----------------------------------------------------------------------

# 服务器地址
# SERVER_GULAOBURL = 'http://127.0.0.1:8080'
SERVER_GULAOBURL = 'http://noteapi.weivird.com/'
SERVER_STATICLOADURL = SERVER_GULAOBURL + '/static'

# ----------------------------------------------------------------------

# CELERY_REDISDB = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL = CELERY_REDISDB

# ----------------------------------------------------------------------

API_DOC_MEMBER = ['category', 'subcategory', 'note']

# 需要排除的 RESTful Api 文档
RESTFUL_API_DOC_EXCLUDE = []