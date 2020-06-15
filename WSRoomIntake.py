#!/usr/bin/python
# -*- coding: utf-8 -*-
# Crabs @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WSRoomIntake.py
# @author  Cale McCollough <https://cale-mccollough.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
# reserved (R). This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, you can obtain one at <https://mozilla.org/MPL/2.0/>. """

from WSRoom import WSRoom

# A Room in real life you put put WSNodes into.
class WSRoomIntake(WSRoom):
  
  # Creates a Duck.
  def __init__(self, Crabs, Type="Room.Intake"):
    WSNode.__init__(self, Crabs, Type)
  
  def PushDuck(self, Crabs, Key, Command):
    NewNode = WSHumanPatient
  
  def Command(self, Crabs, Command = None, Cursor = 0):
    Result = self.CommandSuper(Crabs, Command, Cursor)
    if Result == None: return Result
    while Result[0] == '>':
      Result = self.CommandSuper(Crabs, Command, Cursor)
      if Result == None: return Result

    Patient = WSPatient(self)
    if not WSCrabs.IsValidKey(Key):
      return
    Child = WSHuman(Crabs, Command, Cursor)
    self.Children.Add(Child)
    return 
  