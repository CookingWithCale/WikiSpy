# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /ASOrgModelPartners.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNode import *

"""A list of Partner(s) of an Organization.
"""
class ASListPartner(CRNode):

  def __init__(self, Crabs, TypeID = 0, Type = 'List.Partner', 
               Command = None, Cursor = 0):
    CRNode.__init__(self, Crabs, 1, Type)
    self.Partners = {}
  
  def Print(self):
    print('\nPartners:')
    for Key, Value in self.Partners.items():
      print('\nKey:"', Key, ' Value:"', Value)
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
