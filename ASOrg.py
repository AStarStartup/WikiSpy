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

import CRRoom

class ASBusiness(CRRoom):
  
  def __init__(self):
    CRRoom.__init__(self)
  
  # Handler for the Monitor Process state.
  def StateMonitorHandle(self):
    CRRoom.StateMonitorHandle(self)
  
  def StateShutDownHandle(self):
    CRRoom.StateShutDownHandle(self)
  
  # Function that is called every x seconds to update everything.
  def Update(self):
    CRRoom.Update(self)
  
  # Super-user Do.
  def Do(self, Command, Cursor = 0):
    return None
