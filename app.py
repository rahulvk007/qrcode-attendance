from http.client import HTTPResponse
import re
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, make_response, session
from datetime import datetime
import pytz
import sqlite3


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '123456790'


@app.route('/', methods=['POST', 'GET'])
def index():
    conn = sqlite3.connect('data.db')
    if 'username' in session:

        query = "select * from users where username = '%s'" % session['username']
        h = conn.execute(query)
        h = [i for i in h]
        if h:
            print('log in')
            return render_template("index.html")
    if request.method == "POST":
        details = request.form
        username = details["username"]
        password = details["password"]
        print(username)
        print(password)
        query = "select * from users where username = '%s'" % username
        lg = conn.execute(query)
        lg = [i for i in lg]
        print(lg)
        if lg:
            if username == lg[0][0] and password == lg[0][1]:
                session['username'] = username
                print('ok')
        if 'username' in session:
            if session['username'] == username:
                return render_template("index.html")
    return render_template('login.html')


@app.route('/participant/<regno>/', methods=['POST', 'GET'])
def attendance(regno):
    if 'username' in session:
        conn2 = sqlite3.connect('data.db')
        if request.method == "GET":
            conn2 = sqlite3.connect('data.db')
            rec = conn2.execute(
                "select * from participants where regno = '%s'" % regno)
            rec = [i for i in rec]
            print(rec)
            return render_template('correct.html', r=rec[0])
        elif request.method == "POST":
            if request.form.get('action1') == 'val1':
                query = "UPDATE participants SET attendance = 'PRESENT' where regno = '%s' " % regno
                conn2.execute(query)
                conn2.commit()
                rec = conn2.execute(
                    "select * from participants where regno = '%s'" % regno)
                rec = [i for i in rec]
                return render_template('correct.html', r=rec[0])
            elif request.form.get('action2') == 'val2':
                query = "UPDATE participants SET food_status = 'PRESENT' where regno = '%s' " % regno
                conn2.execute(query)
                conn2.commit()
                rec = conn2.execute(
                    "select * from participants where regno = '%s'" % regno)
                rec = [i for i in rec]
                return render_template('correct.html', r=rec[0])
            else:
                pass  # unknown
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'supersecret'

if __name__ == '__main__':
    app.run()
