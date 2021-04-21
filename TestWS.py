# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /TestWS.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

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
