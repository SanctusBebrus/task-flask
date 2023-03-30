from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/auto_answer")
@app.route("/answer")
def index():
    params = {
        "title": "Досье",
        "surname": "Бонс",
        "name": "Билли",
        "sex": "Мужской",
        "nickname": "Он же 'Капитан'",
        "profession": "Обладатель карты Острова сокровищ",
        "description": "Много пьёт и всегда простужен",
        "character": "Характер скверный",
        "married": "Не женат",
    }
    return render_template("index.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
