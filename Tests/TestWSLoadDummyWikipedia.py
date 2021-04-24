# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/Tests/TestWSLoadWikipedia.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

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
