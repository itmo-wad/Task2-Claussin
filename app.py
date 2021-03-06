from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/img/<path:path>')
def index2(path):
    return send_from_directory('static/images', path)


@app.route('/static/<path:path>')
def index3(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(threaded=True, port='5000')
