#!/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRRoomWorker.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRRoom import *

class CRRoomIntakeSubject(CRRoom):
  
  # Creates a Duck.
  def __init__(self, Crabs, Type = "Room.Intake.Subject"):
    CRNode.__init__(self, Crabs, Type)
  
  # Adds a new child Duck.
  def PushDuck(self, Crabs, Key, Command):
    Child = CRHumanSubject(Crabs)
