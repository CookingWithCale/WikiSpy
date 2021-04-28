#-------------------------------------------------------------------------------
from flask import Flask, jsonify, request, url_for, redirect, session, g,\
                  render_template
import sqlite3

app = Flask (__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'FooWarriorsOfBar'

def ConnectDB():
  sql = sqlite3.connect('data.db')
  sql.row_factory = sqlite3.Row
  return sql

def GetDB():
  if not hasattr(g, 'sqlite3'):
    g.sqlite_db = ConnectDB()
    return g.sqlite_db

@app.teardown_appcontext
def CloseDB(error):
  if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

@app.route('/')
def Index():
  session.pop('name', None)
  return '<h1>Hello world!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def Home(name):
  session['name'] = name
  db = GetDB()
  cur = db.execute('select id, name, location from users')
  result = cur.fetchall()
  return render_template('home.html', name=name, display=True, results=result)

@app.route('/json')
def Json():
  if 'name' in session:
    name = session['name']
  else:
    name = 'NotInSession'
  return jsonify({'Foo': 'Bar', 'Nasty': [1,2,3], 'name': name})

@app.route('/query', methods=['POST', 'GET'])
def Query():
  name = request.args.get('name')
  location = request.args.get('location')
  return '<h1>Hello {}, you are in {}!</h1>'.format(name, location)

@app.route('/theform')
def Form():
  if request.method == 'GET':
    return  '<h1>Form</h1>'\
            '<form method="POST" action="/formprocess">'\
            '  <input type="text" name="name" />'\
            '  <input type="text" name="location" />'\
            '  <input type="submit" value="Submit" />'\
            '</form>'
  else:
    name = request.form['name']
    location = request.form['location']
    db = GetDB()
    db.execute('insert into users (name, location) values (?, ?)',\
               [name, location])
    db.commit()
#-------------------------------------------------------------------------------
    #return '<h1>Hello {}. You are from {}. You have submitted the form '\
    #       'successfully!</h1>'.format(name, location)
    return redirect(url_for('home', name=name, location=location))

@app.route('/formprocess', methods=['POST'])
def FormProcess():
  name = request.form['name']
  location = request.form['location']

  return 'Hello {}. You are from {}. You have submitted the form successfully'.format(name, location)

@app.route('/<name>')
def EndPoint(name):
  return '<h1>EndPoint {}!</h1>'.format(name)

@app.route('/ProcessJson', methods=['POST'])
def ProcessJSON():
  data = request.get_json()
  name = data['name']
  location = data['location']
  randomlist = data['randomlist']
  return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})

@app.route('/viewresults')
def ViewResults():
  db = GetDB()
  cur = db.execute('select id, name, location from users')
  results = cur.fetchall()
  return '<h1>The ID is {}. The name is {}. The location is {}. </h1>'.\
          format(results[1]['id'], results[1]['name'], results[1]['location'])

if __name__ == '__main__':
  app.run()
