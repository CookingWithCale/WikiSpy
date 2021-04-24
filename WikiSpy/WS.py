# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/WikiSpy/WS.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.
 
from CRAbs import *
from WSWiki import *
from WSSearch import *
  
# The WikiSpy server.
class WS(CRAbs):
  StateLoggedOut    = 0
  StateLoggedIn     = 1
  StateFactChecking = 2
  StateSearching    = 3

  def __init__(self, Command = None, Cursor = 0):
    CRAbs.__init__(self)
    self.State = self.StateLoggedOut
    self.Search = WSSearch(self, Command, Cursor)
    self.Wiki = WSWiki()

    self.Meta['Name'] = 'Crabs'
    self.Meta['Description'] = 'Root Crabs Node with NID 0.'
    N = CRRoomIntakeSubject(self)
    N.Meta['Name'] = 'Subject Intake'
    N.Meta['Description'] = 'The Intake Room where subjects are taken in.'
    self.Add(self, 'Intake', N)
    self.ListDetails(self)
    self.COut('? Added Crabs, adding Intake. <')
    N = CRRoomIntakeSubject(self)
    N.Meta['Name'] = 'Worker Room'
    N.Meta['Description'] = 'Room for the Workers.'
    self.Add(self, 'Workers', N) 
    self.COut('? Added Crabs, adding Intake. <')
    N = CRRoom(self)
    self.COut('? Added Crabs, adding Guest Rooms. <')
    N.Meta['Name'] = 'Guest Rooms'
    N.Meta['Description'] = 'The Room where guests start out in.'
    self.Add(self, 'Guests', N)
    self.COut('? Added Crabs, adding Intake. <')
    N = CRRoom(self)
    N.Meta['Name'] = 'Devices'
    N.Meta['Description'] = 'The Room where all of the unused devices are '\
                            'stored in.'
    self.Add(self, 'Devices', N)
    self.ConsoleMain()

  def FactCheckArticle(self):
    self.State = self.StateFactChecking
  
if __name__ == '__main__':
  WikiSpy = WS()
