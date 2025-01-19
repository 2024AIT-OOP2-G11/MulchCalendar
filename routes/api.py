from flask import Blueprint,jsonify, redirect, url_for, request
from models import Event
from models import User

api_bp = Blueprint("api", __name__, url_prefix='/api')

@api_bp.route('/events', methods=['GET'])
def get_events():

    events = Event.select()

    return jsonify([{
        'id': event.id,
        'start': event.start.date().isoformat(),
        'end': event.end.date().isoformat(),
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
  
@api_bp.route('/delete/<int:event_id>', methods=['POST'])
def delete(event_id):
    # 指定されたIDの予定を取得
    event = Event.get_or_none(Event.id == event_id)
    if event:
        event.delete_instance()  # 予定を削除
    # indexページにリダイレクト
    return redirect(url_for('index'))

@api_bp.route('/edit/<int:event_id>', methods=['POST'])
def edit(event_id):
    # 指定されたIDの予定を取得
    event = Event.get_or_none(Event.id == event_id)
    if event:
        # リクエストのデータを取得
        title = request.form['title']
        # データを更新
        event.title = title
        event.save()
    # indexページにリダイレクト
    return redirect(url_for('index'))
  
