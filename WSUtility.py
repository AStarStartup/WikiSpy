#!/usr/bin/python
# -*- coding: utf-8 -*-
# Crabs @version 0.x
# @link    https://github.com/KabukiStarship/WikiSpy.git
# @file    /WSUtility.py
# @author  Cale McCollough <https://cale-mccollough.github.io>
# @license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
# reserved (R). This Source Code Form is subject to the terms of the Mozilla 
# Public License, v. 2.0. If a copy of the MPL was not distributed with this 
# file, you can obtain one at <https://mozilla.org/MPL/2.0/>.

from WSNode import WSNode

# A Node that doesn't have a Node ID or Type ID.
class WSUtility(WSNode):

  # Creates a Utility Duck.
  def __init__(self, Type = "Utility"):
    WSNode.__init__(self, Type)
