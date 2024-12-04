from flask import Flask
from flask.templating import render_template
app = Flask(__name__)
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/update')
def update():
    return render_template('update.html')



@app.route('/read_all')
def read_all():
    return render_template('read_all.html')


@app.route('/read_one')
def read_one():
    return render_template('read_one.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(host='172.21.224.1', port=5000)
