# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRRoom.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from Stringf import *
from CRAbs import *

# A Room in real life you put put CRNodes into.
# Example
# ```BASH
# ><.Intake DoeJohn1 Name='John Doe 1'
# ><.ICU.Intake Name='John Doe 2'
# ><.Devices.Ventilators.GHVentilator.GHVA
# ><.Devices.GHVA.GHVA1.Move 0.*.DoeJohn1
# ```
class CRRoom(CRNode):
  
  # Constructs a Duck.
  def __init__(self, Crabs, Type ='Room', Command = None, Cursor = 0):
    CRNode.__init__(self, Crabs, Crabs.RIDNext (), Type, Command, Cursor)
    self.Meta['Directions'] = ''

  def Directions(self):
    return self.Meta['Directions']
  
  def DirectionsSet(self, Directions):
    self.Add('Directions', Directions)
  
  def Command(self, Crabs, Command = None, Cursor = 0):
    Result = CRNode.CommandSuper(self, Crabs, Command, Cursor)
    if Result == None:
      return Result
    return ''
