from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def mission_name():
    return "Миссия Колонизация Марса"


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    import os
    template = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Загрузка фотографии</h1>
<h2 align="center">для участие в миссии</h2>
<div class="container">
    <form class="login_form" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        {}
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Отправить</button>
        </div>
    </form>
</div>
</body>
</html>"""
    if request.method == 'GET':
        """        <div class="text-center">
            <img src="static/img/photo.jpg" class="rounded" alt="Фото">
        </div>"""
        if os.path.exists('static/img/photo.jpg'):
            img = f"""<div class="text-center" style="max-height: 100%; max_width: 100%;">
            <img src="{url_for('static', filename='img/photo.jpg')}" class="rounded" alt="Фото">
        </div>"""
        else:
            img = ""
        page = template.format(url_for("static", filename='css/style.css'), img)
        return page
    elif request.method == 'POST':
        image = request.files['file']
        with open('static/img/photo.jpg', 'wb') as fd:
            fd.write(image.stream.read())
        return redirect('/load_photo')


if __name__ == '__main__':
    app.run(port=8080, host="")
