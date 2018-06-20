#FLASK_APP=main.py flask run

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Моя первая строчка"

@app.route('/hello/<user>')
def home(user):
    return 'hello, user:{}'.format(user)

if __name__ == '__main__':
    app.run()
