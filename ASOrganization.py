# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRAbs.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from ASBusinessModel import *

"""A Organization with 'business' model canvas.
"""
class ASOrganization(CRNode):

  def __init__(self, Crabs, Type = 'Org', Command = None, Cursor = 0):
    CRNode.__init__(self, Crabs, 1, 'Org')
    self.BusinessModel = ASBusinessModel (Crabs, Command, Cursor)
  
  # Prints this node's stats to the String.
  # @param SelfKey This object's name is stored in the parent's Meta.
  def PrintStats(self, String = '', SelfKey = None):
    CRNode.PrintStats(self, String, SelfKey)
    self.BusinessModel.PrintStats(String, 'Org')
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
