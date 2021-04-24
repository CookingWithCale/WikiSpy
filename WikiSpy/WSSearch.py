# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/WikiSpy/WSSearch.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

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
  