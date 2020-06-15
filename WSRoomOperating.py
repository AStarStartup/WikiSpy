# !/usr/bin/python
# -*- coding: utf-8 -*-
# Crabs @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WSRoomOperating.py
# @author  Cale McCollough <https://cale-mccollough.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
# reserved (R). This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, you can obtain one at <https://mozilla.org/MPL/2.0/>.

from WSRoom import *
from WSMission import *

# A Crabs Operating Room to that performs a Bang when popped.
class WSRoomOperating(WSRoom):
  
  def __init__(self, Crabs, RID, Type="Room.Operating"):
    WSRoom.__init__(self, Crabs, RID, Type)
  
  def AddDuck(self, Crabs, Key, Command, Cursor):
    N = WSMission(self, )

  def Pop(self, Crabs, Command = "", Cursor = 0):
    Bang = WSNode.Bang(self,Crabs)
    WSRoom.Pop(self, Crabs, Bang + Command)
