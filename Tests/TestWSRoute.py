# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/Tests/TestWSRoute.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from flask import Flask
from WS import *
import json
from TestWSRoutes import *

#try:
#  from Foo import Bar
#except Exception as Err:
#  print ('This is how you do conditional compilation in Python.')

def TestWS():
  print ("> WikiSpy Test")
  #self.Do("Intake > ?")
  #wikipedia.search("Foo")
  print ("< ? Done testing WikiSpy Test <")

def TestWSTestRoute():
  print ("> WikiSpy Test")
  #self.Do("Intake > ?")
  #wikipedia.search("Foo")
  App = Flask(__name__)
  ConfigureRoutes(App)
  client = App.test_client()
  url = '/'

  response = client.get(url)
  assert response.get_data() == b'Hello World!'
  assert response.status_code == 200

  print ("< ? Done testing WikiSpy Test <")

def TestPostRouteSuccess():
  App = Flask(__name__)
  ConfigureRoutes(App)
  Client = App.test_client()
  URL = '/post/test'

  MockRequestHeaders = {
    'AuthHash': '123'
  }

  MockRequestData = {
    'RequestId': '123',
    'Payload': {
      'py': 'pi',
      'java': 'script'
    }
  }

  Response = Client.post(URL, data=json.dumps(MockRequestData), headers=MockRequestHeaders)
  assert Response.status_code == 200
