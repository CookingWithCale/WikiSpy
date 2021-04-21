# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /WSSearch.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNodeWeb import *

# The WikiSpy search widget
class WSSearch(CRNodeWeb):
  self.SearchTargetArticle = 0
  self.SearchTargetContributor = 1

  def __init__(self, Crabs, SearchString, Command = '',
               Cursor = 0):
    CRNodeWeb.__init__(self, Crabs, 'https://wikispy.us/search', 0, 
                       'Search', Command, Cursor)
    self.SearchString = SearchString
    self.SearchTarget = self.SearchTargetArticle
  
  def PrintStats(self, StringRep = '', SelfKey = ''):
    Target = 'Article' if (self.SearchTarget == 0) else 'Contributor'
    return 'Searching for ' + Target + ' ' + self.SearchString
  