from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.get('/')
def hello_world():
    return render_template('home.html')


@app.get('/list')
def list():

    return render_template('list.html')


@app.post('/list')
def list_handle():
    data = request.form

    return redirect("https://google.com/list", code=302)


if __name__ == '__main__':
    app.run()
