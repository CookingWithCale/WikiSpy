# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/WikiSpy/WSNewsCard.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from CRNodeWeb import *

class WSNewsCard(CRNodeWeb):

  def __init__(self, Crabs, URL, Command = '',
               Cursor = 0):
    CRNodeWeb.__init__(self, Crabs, URL, 0, 'NewsCard', Command,
               Cursor)
    