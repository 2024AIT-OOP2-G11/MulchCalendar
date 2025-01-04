from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # 現在の年月を取得
    year = datetime.now().year
    month = datetime.now().month
    # 月ごとのカレンダーを取得
    cal = calendar.monthcalendar(year, month)
    # テンプレートに渡して表示
    return render_template("index.html", year=year, month=month, calendar=cal)

if __name__ == "__main__":
    app.run(debug=True)

