from waitress import serve
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session
# from flask_login import login_required, loginManager
import os

# 获取项目根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置主数据库
DATABASE = {
    'ENGINE': 'mysql+pymysql',
    'URI': 'root:@localhost:3306/librarymanagement',
    'ECHO': False
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE['ENGINE']}://{DATABASE['URI']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# login_manager = loginManager()


from bulePrints.borrowRecord import record_bp
from bulePrints.admin import admin_bp
from bulePrints.user import user_bp
from bulePrints.book import book_bp

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(book_bp)
app.register_blueprint(record_bp)

application = app


@app.route('/')
def index():
    return '' \
           '/user   user模块<br>\n' \
           '/book   book模块<br>\n' \
           '/admin  admin模块<br>\n' \
           '/record record模块<br><br><br>\n\n\n' \
           '全部数据用JSON格式传输'

# if __name__ == '__main__':
#     serve(app, host='118.202.30.253', port=5050)