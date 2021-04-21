# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /TestWSRoute.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

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
