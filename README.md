# マルチ・カレンダー／MultiCalendar

## マルチユーザに対応したカレンダー・アプリケーション

- 複数のユーザーを選択可能
- 選択されているユーザーに対して予定をまとめて追加
- 選択されているユーザーに関する予定のみを表示

### 仕様
- ユーザーを登録する機能
  - ユーザー名とユーザーカラーを保持
- イベントを登録する機能
  - 件名，開始日（，終了日），対応するユーザー情報を保持
- ICSファイル（カレンダーのデータ）を出力する機能
  - 出力ボタンを押下することで，カレンダーの内容をICSファイルとして出力
    - 他のカレンダー・アプリケーション（Googleカレンダーなど）で再度読み込み可能
- マルチ・ユーザーに対応したカレンダー機能
  - サイドバーのチェックボックスからユーザを複数選択可能
    - 選択されたユーザーに対応するイベントを，ダッシュボード上のカレンダーに表示
  - カレンダーの日付セルやイベントを押下することで，イベントの追加／編集用のポップアップを表示
 
### 実行方法
1. `app.py`を実行
2. `http://127.0.0.1:8080`にアクセス
3. サイドバー上の「ユーザー登録」→「ユーザー追加」から，ユーザーの情報を登録
4. カレンダーの日付セルをクリックすることで，予定の情報を登録

### 
