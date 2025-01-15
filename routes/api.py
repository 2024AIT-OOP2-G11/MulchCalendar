from flask import Blueprint,jsonify, redirect, url_for, request
from models import Event

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
