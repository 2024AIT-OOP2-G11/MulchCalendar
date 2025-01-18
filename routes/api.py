from flask import Blueprint,jsonify, redirect, url_for, request
from models import Event

api_bp = Blueprint("api", __name__, url_prefix='/api')

@api_bp.route('/events', methods=['GET'])
def get_events():
    # DBにデータを追加
    # Event.create(title='イベント1',start='2025-01-10',end='2025-01-10',user=1)
    # Event.create(title='イベント2',start='2025-01-11',end='2025-01-11',user=2)

    events = Event.select()

    return jsonify([{
        'id': event.id,
        'start': event.start.date().isoformat(),
        'end': event.end.date().isoformat(),
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


@api_bp.route('/add', methods=['GET', 'POST'])
def add(user_list):
    print(user_list)
