#!/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRHuman.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020-1 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from Stringf import *
from CRNode import CRNode

# A model of a human.
class CRHuman(CRNode):
  HeightMin = 0.0         #< The minimum Height of a person is 0M.
  HeightMax = 10.0        #< The maximum Height of a person is 10M.
  WeightMin = 0.0         #< The minimum Weight of a person is 0KG.
  WeightMax = 1000000.0   #< The maximum Weight of a person is 1000KG.
  SexMale = 0             #< Sex is male.
  SexFemale = 1           #< Sex if female.
  
  # Creates a Duck.
  def __init__(self, Crabs, TID, Type = "Human"):
    CRNode.__init__(self, Crabs, TID, Type)
    self.Metadata("Sex", "")         #< The Sex of the person.
    self.Metadata("Height", 0.0)     #< The person's Height.
    self.Metadata("Weight", 0.0)     #< The person's Weight.

  def NameSet (self, Name):
    self.Name = Name

  def UIDSet (self, UID):
    self.UID = UID
  
  def SexSet(self, Sex):
    if Sex >= self.SexMale or Sex <= self.SexFemale:
      self.Sex = Sex
  
  def HeightSet (self, Height):
    if Height >= self.HeightMin and Height <= self.HeightMax:
      self.Height = Height
  
  def WeightSet (self, Weight):
    if Weight >= self.WeightMin and Weight <= self.WeightMax:
      self.Weight = Weight
  
  def IsMale (self): return self.Sex == "m"
  
  def IsFemale (self): return self.Sex == "f"
  
  # Returns the idea body weight of a person.
  def WeightIdeal(self):
    # Height calculations using centimeters.
    if self.IsMale():
      return 50.0 + 0.91 * (self.Height - 152.4)
    elif self.IsFemale(): 
      return 45.5 + 0.91 * (self.Height - 152.4)
    else: 
      return self.Weight

  def PrintStats (self, String = "", SelfKey = ""):
    if SelfKey is not None:
      String += SelfKey + "   "
    return String + "Name:" + self.Name () + "   NID:" + str(self.NID) +\
           self.Circulatory.PrintStats (String) +\
           self.Respiratory.PrintStats (String)
    
  # Prints all of the Details about the object except the Help.
  def PrintDetails (self, String = ""):
     String += "Name:" + self.Name () + " NID:" + self.NID + " Sex:" + self.Sex () + \
           " Height:" + self.Height () + " Weight:" + self.Weight () + \
           "\nDescription:\"" + self.Description () + "\n"
     self.Circulatory.PrintDetails (String)
     return self.Respiratory.PrintDetails (String)
