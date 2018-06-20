#FLASK_APP=main.py flask run
# https://pypi.org/project/simple-settings/

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
