from app.category import category
from app.subcategory import subcategory
from app.note import note

DEFAULT_BLUEPRINT = (
    (category, '/category'),
    (subcategory, '/subcategory'),
    (note, '/note'),
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)