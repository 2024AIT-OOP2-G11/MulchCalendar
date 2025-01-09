from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from models import User, Event
import calendar
from datetime import datetime


app = Flask(__name__)

#　データベースの初期化
initialize_database()

#　各ブループリントをアプリケーションに登録
for bluprint in blueprints:
    app.register_blueprint(bluprint)
    
    
# ホームページのルート
@app.route('/')
def index():
    # 現在の年月を取得
    year = datetime.now().year
    month = datetime.now().month
    
    # 月ごとのカレンダーを取得
    cal = calendar.monthcalendar(year, month)

    # ユーザーの一覧を取得
    users = User.select()

    # イベントの一覧を取得
    events = Event.select()

    return render_template('index.html', users=users, events=events, year=year, month=month, calendar=cal)
    
if __name__ == '__main__':
    app.run(port=8080, debug=True)
  
