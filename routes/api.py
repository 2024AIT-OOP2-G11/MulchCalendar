from flask import Blueprint,jsonify
from models import Event
from models import User

api_bp = Blueprint("api", __name__, url_prefix='/api')

@api_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.select()
    return jsonify([{
        'id': event.id,
        'start': event.start,
        'end': event.end,
        'title': event.title,
        'backgroundColor': event.user.color,
        'borderColor': event.user.color,
        
    } for event in events])
    
@api_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # ここでデータベースからユーザー情報を取得
    user = User.get_or_none(User.id == user_id)
    print("ok")
    if user:
        return jsonify({
            'user': user.user,
            'color': user.color
        })
    return