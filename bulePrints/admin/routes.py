from . import admin_bp
from models.admin import Admin
from flask import jsonify, request
from app import db


# user模块
@admin_bp.route('/')
def index():
    return '/all 全部信息<br>\n' \
           '/add 增<br>\n' \
           '/delete/<id> 删<br>\n' \
           '/query_by_id/<id> 查(id)<br>\n' \
           '/query_by_name/<name> 查(名字)<br>\n' \
           '/edit/<id> 改<br>\n'


@admin_bp.route('/all', methods=['GET'])
def getAll():
    return jsonify(Admin.queryAll())


@admin_bp.route('/add', methods=['GET', 'POST'])
def add():
    try:
        data = request.get_json()
        if not data:
            raise Exception('No data received')
        db.session.add(
            Admin(
                name=data.get('name'),
                password=data.get('password')
            )
        )
        db.session.commit()
        return jsonify({'status_code': 200})
    except Exception as e:
        return jsonify({'error': str(e)})


@admin_bp.route('/delete/<aid>', methods=['GET', 'POST', 'DELETE'])
def delete(aid):
    try:
        if request.method == 'DELETE':
            user = Admin.query.get(aid)
            if not user:
                raise Exception('user not found')
            db.session.delete(user)
            db.session.commit()
            return jsonify({'status_code': 200})
        else:
            raise Exception("method error")

    except Exception as e:
        return jsonify({'error': str(e)})


@admin_bp.route('/query_by_id/<uid>', methods=['GET', 'POST'])
def getID(uid):
    try:
        user = db.session.query(Admin).get(uid)
        return jsonify(user.toDict())
    except Exception as e:
        return jsonify({'error': str(e)})


@admin_bp.route('/query_by_name/<uname>', methods=['GET', 'POST'])
def getName(uname):
    try:
        users = db.session.query(Admin).filter(Admin.name.like('%' + uname + '%')).all()
        return jsonify([user.toDict() for user in users])
    except Exception as e:
        return jsonify({'error': str(e)})


@admin_bp.route('/edit/<uid>', methods=['GET', 'POST'])
def edit(uid):
    try:
        user = Admin.query.get(uid)

        if not user:
            return jsonify({"error": "User not found"}), 404

        if request.method == 'POST':
            data = request.get_json()
            user.name = data.get('name,', user.name)
            user.password = data.get('password', user.password)
            db.session.commit()
            return jsonify({'status_code': 200})
    except Exception as e:
        return jsonify({'error': str(e)})
