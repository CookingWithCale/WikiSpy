# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /TestWSRoutes.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

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