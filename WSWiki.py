# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /WSWiki.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNodeWeb import *

class WSWiki(CRNodeWeb):
  def __init__(self, Crabs, URL = 'wikipedia.org'):
    CRNodeWeb.__init__(self, Crabs, URL, 0, 'Wiki')
  
  def PrintStats(self, StringRep = '', SelfName = ''):
    StringRep += 'Wiki:' + self.Meta['URL']
