# !/usr/bin/python
# -*- coding: utf-8 -*-
# Crabs @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WikiSpy.py
# @author  Cale McCollough <https://cale-mccollough.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
# reserved (R). This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, you can obtain one at <https://mozilla.org/MPL/2.0/>. Process
 
from WSCrabs import *
  
# The WikiSpy root.
class WikiSpy(WSCrabs):
  
  def __init__(self, Command = None):
    WSCrabs.__init__(self)
    self.Meta["Name"] = "Crabs"
    self.Meta["Description"] ="Crabs Node with NID 0."
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoomIntakePatient(self)
    N.Meta["Name"] = "Patient Intake"
    N.Meta["Description"] = "The Intake Room where you wait get get into " \
                            "the Hospital."
    self.Add(self, "Intake", N)
    self.ListDetails(self)
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoomIntakePatient(self)
    N.Meta["Name"] = "Staff Room"
    N.Meta["Description"] = "The room with Patients who may need critical " \
                            "care."
    self.Add(self, "Staff", N) 
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoom(self)
    N.Meta["Name"] = "Emergency Room"
    N.Meta["Description"] = "The main Hospital Emergency Room."
    self.Add(self, "ER", N)
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoom(self)
    N.Meta["Name"] = "Intensive Care Unit"
    N.Meta["Description"] = "The room for Patients in need of critical care."
    self.Add(self, "ICU", WSRoom(self))
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoom(self)
    N.Meta["Name"] = "Emergency Room"
    N.Meta["Description"] = "The Rooms where the Patients are in who aren\'t " \
                            "in the ER or ICU."
    self.Add(self, "Rooms", N)
    N = WSRoom(self)
    self.COut("? Added Crabs, adding Intake. <")
    N.Meta["Name"] = "Guest Rooms"
    N.Meta["Description"] = "The Room where guests start out in."
    self.Add(self, "Guests", N)
    self.COut("? Added Crabs, adding Intake. <")
    N = WSRoom(self)
    N.Meta["Name"] = "Devices"
    N.Meta["Description"] = "The Room where all of the unused devices are "\
                            "stored in."
    self.Add(self, "Devices", N)
    self.Test()
    self.ConsoleMain()
  
  def Test(self):
    WSCrabs.Test(self)
    self.COut ("> WikiSpy Test")
    #self.Do("Intake > ?")
    self.COut ("< ? Done testing WikiSpy Test")
  
if __name__ == '__main__':
  WikiSpy = WikiSpy()
