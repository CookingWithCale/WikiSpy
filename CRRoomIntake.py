#!/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRRoomIntake.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRRoom import CRRoom

# A Room in real life you put put CRNodes into.
class CRRoomIntake(CRRoom):
  
  # Creates a Duck.
  def __init__(self, Crabs, Type="Room.Intake"):
    CRNode.__init__(self, Crabs, Type)
  
  def PushDuck(self, Crabs, Key, Command):
    NewNode = CRHumanSubject
  
  def Command(self, Crabs, Command = None, Cursor = 0):
    Result = self.CommandSuper(Crabs, Command, Cursor)
    if Result == None: return Result
    while Result[0] == '>':
      Result = self.CommandSuper(Crabs, Command, Cursor)
      if Result == None: return Result

    Subject = CRSubject(self)
    if not CRAbs.IsValidKey(Key):
      return
    Child = CRHuman(Crabs, Command, Cursor)
    self.Children.Add(Child)
    return 
  