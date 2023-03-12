from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def get_room(sex, age):
    return render_template('template.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
