from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/list_prof/<order>')
def news(type_printing):
    profession_list = ['Конченый идиот', 'Самый сексуальный мужик в мире', 'Горячая чикса',
                       'Злодей британец', 'Так себе шутник', 'Пубертатная язва',
                       'Какой-то мужик', 'Говнюки', 'Недопонятый гений']
    return render_template('base.html', prof_list=profession_list, print_type=order)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
