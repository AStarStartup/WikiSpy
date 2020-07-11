# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/AStarStartup/WikiSpy.git
# @file    /CRAbs.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>. This Source 
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

"""A Organization with business model canvas.
"""
class ASOrganization(CRNode):

  def __init__(self, Crabs, TypeID = 0, Type = "Org"):
    CRNode.__init__(self, Crabs, 1, "Org")
    self.Activities = ASListActivity()
    self.Channels = ASListChannel ()
    self.Costs = ASListCost ()
    self.CustomerRelationships = ASListCustomerRelationship ()
    self.CustomerSegments = ASListCustomerSegment ()
    self.Partners = ASListPartner ()
    self.Resources = ASListResource ()
    self.RevenueStreams = ASListRevenue ()
    self.ValuePropositions = ASListValueProposition ()
    self.StateNext = None #< Pointer to the next State
  
  def Print(self):
    self.Activities.Print()
    self.Channels.Print()
    self.Costs.Print()
    self.CustomerRelationships.Print()
    self.CustomerSegments.Print()
    self.Partners.Print()
    self.Resources.Print()
    self.RevenueStreams.Print()
    self.ValuePropositions.Print()
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
