from flask import Flask, render_template
import random
import json

app = Flask(__name__)


@app.route('/member')
def members():
    with open('templates/crew.json', encoding='utf8') as file:
        f = file.read()
        data = json.loads(f)
        data = data['team'][random.randint(0, 8)]

    return render_template('member_template.html', name=data['name'], prof=data['prof'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
