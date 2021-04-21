# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /TestWSLoadWikipedia.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from WSWiki import *

#try:
#  from Foo import Bar
#except Exception as Err:
#  print ('This is how you do conditional compilation in Python.')

# Loads WikiSpy test users.
class TestWSLoadDummyWikipedia(CRMission):

  def __init__(self, Crabs, Command = None, Cursor = 0):
    CRMission.__init__(self, Crabs, "Test.LoadDummyWikipedia", 
                       Command, Cursor)
    Crabs.PushPop(Node, WSWiki(Crabs, 'http://wikipedia.org'))

if __name__ == '__main__':
  App = TestWS(CRAbs ())
