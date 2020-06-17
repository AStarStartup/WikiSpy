#!/usr/bin/python
# -*- coding: utf-8 -*-
# WikiSpy @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /CRProcess.py
# @author  Cale McCollough <https://CookingWithCale.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>. This Source 
# Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a 
# copy of the MPL was not distributed with this file, you can obtain one at 
# <https://mozilla.org/MPL/2.0/>.

from CRNode import *

class CRMission(CRNode):
  
  # Creates a Duck.
  def __init__(self, Crabs, Type = "Mission"):
    CRNode.__init__(self, Crabs, Crabs.MIDNext(), Type)
