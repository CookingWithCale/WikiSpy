# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/WikiSpy/WSArticle.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from CRNodeWeb import *

# The wiki article
class WSArticle(CRNodeWeb):

  def __init__(self, Crabs, URL, Command = '', Cursor = 0):
    CRNodeWeb.__init__(self, Crabs, URL, 0, 'Article', Command, Cursor)
    self.Title = ''
    self.Body = ''
  
  def PrintStats(self, String = '', SelfKey = ''):
    String += '\nTitle:"' + self.Title
  