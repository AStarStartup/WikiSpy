# !/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WikiSpy.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.
 
from CRAbs import *
import wikipedia
  
# The WikiSpy root.
class WikiSpy(CRAbs):
  
  def __init__(self, Command = None):
    CRAbs.__init__(self)
    self.Meta["Name"] = "Crabs"
    self.Meta["Description"] ="Crabs Node with NID 0."
    self.COut("? Added Crabs, adding Intake. <")
    N = CRRoomIntakeSubject(self)
    N.Meta["Name"] = "Subject Intake"
    N.Meta["Description"] = "The Intake Room where subjects are taken in."
    self.Add(self, "Intake", N)
    self.ListDetails(self)
    self.COut("? Added Crabs, adding Intake. <")
    N = CRRoomIntakeSubject(self)
    N.Meta["Name"] = "Worker Room"
    N.Meta["Description"] = "Room for the Workers."
    self.Add(self, "Workers", N) 
    self.COut("? Added Crabs, adding Intake. <")
    N = CRRoom(self)
    self.COut("? Added Crabs, adding Guest Rooms. <")
    N.Meta["Name"] = "Guest Rooms"
    N.Meta["Description"] = "The Room where guests start out in."
    self.Add(self, "Guests", N)
    self.COut("? Added Crabs, adding Intake. <")
    N = CRRoom(self)
    N.Meta["Name"] = "Devices"
    N.Meta["Description"] = "The Room where all of the unused devices are "\
                            "stored in."
    self.Add(self, "Devices", N)
    self.Test()
    self.ConsoleMain()
  
  def Test(self):
    CRAbs.Test(self)
    self.COut ("> WikiSpy Test")
    #self.Do("Intake > ?")
    wikipedia.search("Foo")
    self.COut ("< ? Done testing WikiSpy Test <")
  
if __name__ == '__main__':
  WikiSpy = WikiSpy()
