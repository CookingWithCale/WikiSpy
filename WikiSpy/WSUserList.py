# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/WikiSpy/WSUserList.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from WSUser import *

# A list of users.
class WSUserList(CRNodeWeb):

  def __init__(self, Crabs, Name = '', Command = '', Cursor = 0):
    CRNodeWeb.__init__(self, Crabs, '', 0, 'UserList', Command,
               Cursor)
    self.Name = Name
    self.Users = {}

  def PrintStats(self, String = '', SelfKey = None):
    String += '\nUserList:'
    for Key, Value in self.Children.items() :
      Value.PrintStats(String, Key)
  