from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
def index(title):
    return render_template('template.html', title=f'{title}')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
