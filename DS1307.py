#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""DS1307: Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Maxim Integrated"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from DS1307_constants import *

# name:        DS1307
# description: Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM.
# manuf:       Maxim Integrated
# version:     0.1
# url:         https://datasheets.maximintegrated.com/en/ds/DS1307.pdf
# date:        2017-01-11


# Derive from this class and implement read and write
class DS1307_Base:
	"""Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM."""
	# Register SECS
	
	
	def setSECS(self, val):
		"""Set register SECS"""
		self.write(REG.SECS, val, 8)
	
	def getSECS(self):
		"""Get register SECS"""
		return self.read(REG.SECS, 8)
	
	# Bits CH
