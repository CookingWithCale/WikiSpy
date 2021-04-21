# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /WSArticle.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNodeWeb import *

# The wiki article
class WSArticle(CRNodeWeb):

  def __init__(self, Crabs, URL, Command = '', Cursor = 0):
    CRNodeWeb.__init__(self, Crabs, URL, 0, 'Article', Command, Cursor)
    self.Title = ''
    self.Body = ''
  
  def PrintStats(self, String = '', SelfKey = ''):
    String += '\nTitle:"' + self.Title
  