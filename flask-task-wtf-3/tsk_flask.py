from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if prof.lower() in ['инженер', 'строитель']:
        prof = 1
    else:
        prof = 2
    image_url = str(url_for("static", filename=f"plan_{prof}.jpg"))
    return render_template('base.html', profession=prof, images_url=image_url)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
