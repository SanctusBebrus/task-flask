from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    usb_team = ['Никита', 'Стас', 'Гена', 'Турбо', 'Дюша Метёлкин']
    return render_template('template.html', team=usb_team)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
