from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from environment import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'max_identifier_length':128}
# See the section 'Max Identifier Lengths' in the SQLAlchemy Oracle dialect documentation

db = SQLAlchemy(app)

# use Oracle Dialog where needed: db.Sequence('id_seq')
# https://docs.sqlalchemy.org/en/13/dialects/oracle.html


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('id', db.Integer, db.Sequence('id_seq'), primary_key=True)
    title = db.Column(db.String(80), unique=False)
    text = db.Column(db.String(120), unique=False)
    done = db.Column(db.Boolean, unique=False)
    pub_date = db.Column(db.DateTime, unique=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()


@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/show_all')
def show_all():
    return render_template('show_all.html',
        todos=Todo.query.order_by(Todo.pub_date.desc()).all()
    )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))


@app.route('/test')
def test_connection():
    sql = text('select sysdate from dual')
    result = db.engine.execute(sql)
    date = [row[0] for row in result]
    return render_template('show_db_datetime.html',
        date=date
    )

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
db.create_all()

