from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello asdfkajsdkfjdsalkfaslf'

@app.route('/list')
def list():  # put application's code here
    return 'here is list'


if __name__ == '__main__':
    app.run()
