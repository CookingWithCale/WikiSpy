# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    ~/Tests/TestWS.py
# @license Copyright 2020-1 (C) AStartup <https://astartup.net>.
# This source code form is confidential and is covered under the Kabuki Weak 
# Source-available License. A copy of the license that YOU MUST READ can be 
# found in the readme.md file in this folder.

from CRMission import *
from TestWSLoadTestUsers import *
from TestWSLoadDummyWikipedia import *

# Use case scenario: FactCheckArticle
# @see `~/docs/RAD/SystemModels/Scenarios/UseCase.FactCheckArticle.md`
class TestWSUseCaseFactCheckArticle(CRMission):

  def __init__(self, Crabs, Query, Command = None, Cursor = 0):
    CRMission.__init__(self, Crabs, 'Test.UseCase.FactCheckArticle', 
                       Command, Cursor)
    X = TestWSLoadTestUsers(Crabs)
    X = TestWSLoadDummyWikipedia(Crabs)
    X = TestWSSearchArticle(Crabs)
    String = ''
    Crabs.PrintStats(String, 'Search results')
    print (String)
    assert (Crabs.Top.Key() == Query),'! Article name was not ' + Query + '. <'
    
if __name__ == '__main__':
  App = TestWSUseCaseFactCheckArticle(CRAbs ())
