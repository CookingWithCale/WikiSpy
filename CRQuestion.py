#!/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRQuestion.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRSearch import *

class CRQuestion(CRSearch):
  
  # Creates a Duck CRQuestion.
  def __init__(self, Crabs, Text = '', Command = '', Cursor = 0):
    CRSearch.__init__(self, Crabs, 'Question')
    self.Text = Text
    self.Meta['Answers'] = {}
  
  def Answers(self):
    return self.Meta['Answers']
