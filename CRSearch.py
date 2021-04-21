# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRSearch.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNode import CRNode
import time

# A Crabs search results that doesn't have a NID.
class CRSearch(CRNode):
  
  def __init__(self, Parent, Type = "Search", TID = 0):
    CRNode.__init__(self, Parent, Type, TID)
    TimeOfSearch = time.time()
    self.Members["Created"] = TimeOfSearch
    Crabs.Push(self)
  