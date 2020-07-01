# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /CRAbs.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

"""A Org model based on the Org model canvas.
"""
class ASOrgModelPartners(CRNode):

  def __init__(self, Crabs, TypeID = 0, Type = "BussinessModel"):
    CRNode.__init__(self, Crabs, 1, "BussinessModel")d
    self.KeyPartners = {}
    self.KeyActivities = {}
    self.KeyResources = {}
    self.ValuePropositions = {}
    self.CustomerRelationships = {}
    self.Channels = {}
    self.CustomerSegments = {}
    self.CostStructure = {}
    self.RevenueStreams = {}
    self.StateNext = None #< Pointer to the next State
  
  # Handler for the Monitor Process state.
  def StateMonitorHandle(self):
    CRRoom.StateMonitorHandle(self)
  
  def StateShutDownHandle(self):
    CRRoom.StateShutDownHandle(self)
  
  # Function that is called every x seconds to update everything.
  def Update(self):
    CRRoom.Update(self)
  
  def Print(self):
    print('\nKeyPartners:')
    for Key, Value in self.KeyPartners.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nKeyActivities:')
    for Key, Value in self.KeyActivities.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nKeyResources:')
    for Key, Value in self.KeyResources.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nValuePropositions:')
    for Key, Value in self.ValuePropositions.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nCustomerRelationships:')
    for Key, Value in self.CustomerRelationships.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nCustomerSegments:')
    for Key, Value in self.CustomerSegments.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nCostStructure:')
    for Key, Value in self.CostStructure.items():
      print('\nKey:"', Key, ' Value:"', Value)
    print('\nRevenueStreams:')
    for Key, Value in self.RevenueStreams.items():
      print('\nKey:"', Key, ' Value:"', Value)
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
