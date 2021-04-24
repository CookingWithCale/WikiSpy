# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/Tests/TestWSRoutes.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from flask import request
import json

def ConfigureRoutes(app):

  @app.route('/')
  def HelloWorld():
    return "Hello world!"
  
  @app.route('/post/test', methods=['post'])
  def ReceivePost():
    Headers = request.headers

    AuthToken = Headers.get('AuthHash')
    if not AuthToken:
      return 'Unauthorized', 401
    
    DataString = request.get_data()
    data=json.loads(DataString)

    RequestId = data.get('RequestId')
    Payload = data.get('Payload')

    if RequestId and Payload:
      return 'Ok', 200
    else:
      return 'Bad request', 400