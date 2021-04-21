# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRNodeWeb.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNode import *

class CRNodeWeb(CRNode):
  def __init__(self, Crabs, URL, TypeID = 0, Type = 'NodeWeb', Command = '',
               Cursor = 0):
    CRNode.__init__(self, Crabs, TypeID, Type)
    self.Meta['URL'] = URL
