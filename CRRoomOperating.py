# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRRoomOperating.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRRoom import *
from CRMission import *

# A Crabs Operating Room to that performs a Trigger when popped.
class CRRoomOperating(CRRoom):
  
  def __init__(self, Crabs, RID, Type="Room.Operating"):
    CRRoom.__init__(self, Crabs, RID, Type)
  
  def AddDuck(self, Crabs, Key, Command, Cursor):
    N = CRMission(self, )

  def Pop(self, Crabs, Command = "", Cursor = 0):
    Trigger = CRNode.Trigger(self,Crabs)
    CRRoom.Pop(self, Crabs, Trigger + Command)
