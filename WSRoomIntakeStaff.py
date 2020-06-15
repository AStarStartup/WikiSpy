#!/usr/bin/python
# -*- coding: utf-8 -*-
# Crabs @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WSRoomStaff.py
# @author  Cale McCollough <https://cale-mccollough.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
# reserved (R). This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, you can obtain one at <https://mozilla.org/MPL/2.0/>.

from WSRoom import *

# An HumanStaff factory Room
class WSRoomIntakeStaff(WSRoom):
  
  def __init__(self, Crabs, Type = "Room.Intake.Staff"):
    WSNode.__init__(self, Crabs, Type)
  
  def PushDuck(self, Crabs, Key, Command):
    Children = WSNode.Chidren
    Child = WSHumanStaff(Crabs, Type)
    Children[Key] = Child
    return None
