# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRAbs.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from ASListActivity import *
from ASListChannel import *
from ASListCost import *
from ASListCustomerRelationship import *
from ASListCustomerSegment import *
from ASListPartner import *
from ASListResource import *
from ASListRevenue import *
from ASListValueProposition import *

"""A business model canvas.
"""
class ASBusinessModel(CRNode):

  def __init__(self, Crabs, Type = 'BusinessModel', Command = None, Cursor = 0):
    CRNode.__init__(self, Crabs, 1, 'BusinessModel')
    self.Activities = ASListActivity(Crabs, Command, Cursor)
    self.Channels = ASListChannel (Crabs, Command, Cursor)
    self.Costs = ASListCost (Crabs, Command, Cursor)
    self.CustomerRelationships = ASListCustomerRelationship (Crabs, Command, Cursor)
    self.CustomerSegments = ASListCustomerSegment (Crabs, Command, Cursor)
    self.Partners = ASListPartner (Crabs, Command, Cursor)
    self.Resources = ASListResource (Crabs, Command, Cursor)
    self.RevenueStreams = ASListRevenue (Crabs, Command, Cursor)
    self.ValuePropositions = ASListValueProposition (Crabs, Command, Cursor)
    self.StateNext = None #< Pointer to the next business model State
  
  # Prints this node's stats to the String.
  # @param SelfKey This object's name is stored in the parent's Meta.
  def PrintStats(self, String = '', SelfKey = None):
    CRNode.PrintStats(self, String, SelfKey)
    self.Activities.PrintStats(String, 'Activities')
    self.Channels.PrintStats(String, 'Channels')
    self.Costs.PrintStats(String, 'Costs')
    self.CustomerRelationships.PrintStats(String, 'CustomerRelationships')
    self.CustomerSegments.PrintStats(String, 'CustomerSegments')
    self.Partners.PrintStats(String, 'Partners')
    self.Resources.PrintStats(String, 'Resources')
    self.RevenueStreams.PrintStats(String, 'RevenueStreams')
    self.ValuePropositions.PrintStats(String, 'ValuePropositions')
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
