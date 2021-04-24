# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /TestWS.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from WS import *

#try:
#  from Foo import Bar
#except Exception as Err:
#  print ('This is how you do conditional compilation in Python.')

# Test WikiSpy server.
class TestWS(CRMission):

  def __init__(self, Crabs, Command = None, Cursor = 0):
    CRMission.__init__(self, Crabs, "Mission.Test.WikiSpy", Command, Cursor)
    print ("> MissionTestWikiSpy")
    print ("> Printing stats.")
    StringRep = ''
    self.PrintStats(Crabs, StringRep)
    print ("< ? Done printing stats.<")
    print ("< ? MissionTestWikiSpy complete. <")

if __name__ == '__main__':
  App = TestWS(CRAbs ())
