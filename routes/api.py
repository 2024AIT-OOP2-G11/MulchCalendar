from flask import Blueprint,jsonify
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