from flask import Flask, render_template, request, redirect, url_for, request_finished
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:eHr9fnsWdoa7lhIgcTd4@containers-us-west-176.railway.app/railway?6587', echo=True, query_cache_size=0,
                       connect_args=dict(host='containers-us-west-176.railway.app', port=6587))

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:eHr9fnsWdoa7lhIgcTd4@containers-us-west-176.railway.app/railway?6587'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        #default é True

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
