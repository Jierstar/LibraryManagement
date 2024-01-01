from . import user_bp
from models.user import User
from flask import jsonify, request
from app import db


# user模块
@user_bp.route('/')
def index():
    return '/all 全部信息<br>' \
           '/add 增<br>' \
           '/delete/<id> 删<br>' \
           '/query_by_id/<id> 查(id)<br>' \
           '/query_by_name/<name> 查(名字)<br>' \
           '/edit/<id> 改<br>'



@user_bp.route('/all', methods=['GET'])
def getAll():
    return jsonify(User.queryAll())


@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    try:
        data = request.get_json()
        if not data:
            raise Exception('No data received')
        db.session.add(
            User(
                name=data.get('name'),
                id=data.get('id'),
                tel=data.get('tel'),
                password=data.get('password')
            )
        )
        db.session.commit()
        return jsonify({'status_code': 200})
    except Exception as e:
        return jsonify({'error': str(e)})


@user_bp.route('/delete/<uid>', methods=['GET', 'POST', 'DELETE'])
def delete(uid):
    try:
        if request.method == 'DELETE':
            user = User.query.get(uid)
            if not user:
                raise Exception('user not found')
            db.session.delete(user)
            db.session.commit()
            return jsonify({'status_code': 200})
        else:
            raise Exception("method error")

    except Exception as e:
        return jsonify({'error': str(e)})


@user_bp.route('/query_by_id/<uid>', methods=['GET', 'POST'])
def getID(uid):
    try:
        user = db.session.query(User).get(uid)
        return jsonify(user.toDict())
    except Exception as e:
        return jsonify({'error': str(e)})


@user_bp.route('/query_by_name/<uname>', methods=['GET', 'POST'])
def getName(uname):
    try:
        users = db.session.query(User).filter(User.name.like('%' + uname + '%')).all()
        return jsonify([user.toDict() for user in users])
    except Exception as e:
        return jsonify({'error': str(e)})


@user_bp.route('/edit/<uid>', methods=['GET', 'POST'])
def edit(uid):
    try:
        user = User.query.get(uid)

        if not user:
            return jsonify({"error": "User not found"}), 404

        if request.method == 'POST':
            data = request.get_json()
            user.name = data.get('name,', user.name)
            user.id = data.get('id', user.id)
            user.tel = data.get('tel', user.tel)
            user.password = data.get('password', user.password)
            db.session.commit()
            return jsonify({'status_code': 200})
    except Exception as e:
        return jsonify({'error': str(e)})
