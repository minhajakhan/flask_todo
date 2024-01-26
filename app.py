from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)
app.app_context().push()

#create models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('dashboard/index.html')

@app.route('/about')
def about():
    return render_template('dashboard/about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)