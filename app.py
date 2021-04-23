from flask import Flask, jsonify, request

app = Flask (__name__)

@app.route('/')
def Index():
  return '<h1>Hello world!</h1>'

@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def Home(name):
  return '<h1>Welcome Home {}</h1>'.format(name)

@app.route('/json')
def json():
  return jsonify({'Foo': 'Bar', 'Nasty': [1,2,3]})

@app.route('/query', methods=['POST', 'GET'])
def Query():
  name = request.args.get('name')
  location = request.args.get('location')
  return '<h1>Hello {}, you are in {}!</h1>'.format(name, location)

@app.route('/form')
def Form():
  return '''<h1>Form</h1>
            <form method="POST" action="/FormProcess">
              <input type="text" name="name" />
              <input type="text" name="location" />
              <input type="submit" value="Submit" />
            </form>'''

@app.route('/FormProcess', methods=['POST'])
def FormProcess():
  name = request.form['name']
  location = request.form['location']

  return 'Hello {}. You are from {}. You have submitted the form successfully'.format(name, location)

@app.route('/<name>')
def EndPoint(name):
  return '<h1>Hello {}!</h1>'.format(name)

@app.route('processjson', methods=['POST'])
def ProcessJSON():
  return jsonify({'result': 'Success!'})

if __name__ == '__main__':
  app.run()
  #app.run(debug=True)
