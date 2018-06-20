from flask import Flask, request

app = Flask(__name__)


@app.route("/sum/<int:first>/<int:second>")
def calc_sum(first, second):
    print(first+second)
    return 'sum = {}'.format(first + second)


@app.route("/")
def home():
    print('200 hi')
    return 'привет медвед'

# http://127.0.0.1:5000/sum/1/2
if __name__ == '__main__':
    app.run()
