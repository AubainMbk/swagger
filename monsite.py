from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/cursus/remy')
def cursus_remy():
    return render_template('cursus_remy.html')

@app.route('/cursus/elliot')
def cursus_elliot():
    return render_template('cursus_elliot.html')



@app.route('/cv/remy')
def cv_remy():
    return render_template('cv_remy.html')


@app.route('/cv/elliot')
def cv_elliot():
    return render_template('cv_elliot.html')

if __name__ == '__main__':
    app.run(host='192.168.146.91', port=5000, debug=True)
