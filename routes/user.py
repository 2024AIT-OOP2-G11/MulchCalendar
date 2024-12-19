from flask import Blueprint, render_template, request, redirect, url_for
from models import User

# Blueprintの作成
user_bp = Blueprint('user',__name__, url_prefix='/users')

# リスト確認用で作成（プログラムから飛ばす予定なし）
@user_bp.route('/')
def list():
    users = User.select()
    return render_template('user_list.html',items=users) 


@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    #POSTのデータを登録
    if request.method == 'POST':
        user = request.form['user']
        color = request.form['color']
        User.create(user=user, color=color)
        return redirect(url_for('index'))
    
    return render_template('user_add.html')