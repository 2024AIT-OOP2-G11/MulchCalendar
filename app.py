from flask import Flask, render_template
from models import initialize_database
from routes import blueprints


app = Flask(__name__)

#　データベースの初期化
initialize_database()

#　各ブループリントをアプリケーションに登録
for bluprint in blueprints:
    app.register_blueprint(bluprint)
    
    
# ホームページのルート
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(port=8080, debug=True)
  
