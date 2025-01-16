from flask import Blueprint,jsonify
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