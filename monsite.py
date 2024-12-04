from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

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
    app.run(host='172.21.224.1', port=5000)
