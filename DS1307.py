#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""DS1307: Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Maxim Integrated"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from DS1307_constants import *

# name:        DS1307
# description: Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM.
# manuf:       Maxim Integrated
# version:     Version 0.1
# url:         https://datasheets.maximintegrated.com/en/ds/DS1307.pdf
# date:        2017-01-11


# Derive from this class and implement read and write
class DS1307_Base:
	"""Lowpower serial real-time clock (RTC) with full binary-coded decimal (BCD) clock/calendar plus 56 bytes of NV SRAM."""
	# Register SECONDS
	# Seconds 00–59 
	
	def setSECONDS(self, val):
		"""Set register SECONDS"""
		self.write(REG.SECONDS, val, 8)
	
	def getSECONDS(self):
		"""Get register SECONDS"""
		return self.read(REG.SECONDS, 8)
	
	# Bits CH
	# The clock halt bit. When this bit is set to '1', the oscillator is disabled. 
	#           When cleared to '0', the oscillator is enabled. 
	#           The clock can be halted whenever the timekeeping functions are not required, 
	#           which minimizes current (IBATDR). 
	
	# Bits SECS_10
	# Bits SECS
	# Register MINUTES
	# Minutes 00–59 
	
	def setMINUTES(self, val):
		"""Set register MINUTES"""
		self.write(REG.MINUTES, val, 8)
	
	def getMINUTES(self):
		"""Get register MINUTES"""
		return self.read(REG.MINUTES, 8)
	
	# Bits unused_0
	# Bits MINUTES_10
	# Bits MINUTES
	# Register HOURS
	# Hours 1–12 
	#       The DS1307 can be run in either 12-hour or 24-hour mode. Bit 6 of the hours register is defined as the 12-hour or
	#       24-hour mode-select bit. When high, the 12-hour mode is selected. In the 12-hour mode, bit 5 is the AM/PM bit with
	#       logic high being PM. In the 24-hour mode, bit 5 is the second 10-hour bit (20 to 23 hours). The hours value must be
	#       re-entered whenever the 12/24-hour mode bit is changed.
	
	
	def setHOURS(self, val):
		"""Set register HOURS"""
		self.write(REG.HOURS, val, 8)
	
	def getHOURS(self):
		"""Get register HOURS"""
		return self.read(REG.HOURS, 8)
	
	# Bits unused_0
	# Bits H12_24
	# Bits AM_PM
	# Bits HOUR_10
	# Bits HOURS
	# Register HOURS
	# Hours 00-23
	#       The DS1307 can be run in either 12-hour or 24-hour mode. Bit 6 of the hours register is defined as the 12-hour or
	#       24-hour mode-select bit. When high, the 12-hour mode is selected. In the 12-hour mode, bit 5 is the AM/PM bit with
	#       logic high being PM. In the 24-hour mode, bit 5 is the second 10-hour bit (20 to 23 hours). The hours value must be
	#       re-entered whenever the 12/24-hour mode bit is changed. 
	
	
	def setHOURS(self, val):
		"""Set register HOURS"""
		self.write(REG.HOURS, val, 8)
	
	def getHOURS(self):
		"""Get register HOURS"""
		return self.read(REG.HOURS, 8)
	
	# Bits unused_0
	# Bits H12_24
	# Bits HOUR_10
	# Bits HOURS
	# BCD format
	# Register DAY
	# Day 01–07 
	
	def setDAY(self, val):
		"""Set register DAY"""
		self.write(REG.DAY, val, 8)
	
	def getDAY(self):
		"""Get register DAY"""
		return self.read(REG.DAY, 8)
	
	# Bits unused_0
	# Bits DAY
	# BCD format
	# Register DATE
	# Date 01–31 
	
	def setDATE(self, val):
		"""Set register DATE"""
		self.write(REG.DATE, val, 8)
	
	def getDATE(self):
		"""Get register DATE"""
		return self.read(REG.DATE, 8)
	
	# Bits unused_0
	# Bits DATE_10
	# Bits DATE
	# BCD format
	# Register MONTH
	# Month 01–12 
	
	def setMONTH(self, val):
		"""Set register MONTH"""
		self.write(REG.MONTH, val, 8)
	
	def getMONTH(self):
		"""Get register MONTH"""
		return self.read(REG.MONTH, 8)
	
	# Bits unused_0
	# Bits MONTH_10
	# Bits MONTH
	# BCD format
	# Register YEAR
	# Year 00–99 
	
	def setYEAR(self, val):
		"""Set register YEAR"""
		self.write(REG.YEAR, val, 8)
	
	def getYEAR(self):
		"""Get register YEAR"""
		return self.read(REG.YEAR, 8)
	
	# Bits YEAR_10
	# BCD format
	# Bits YEAR
	# BCD format
	# Register CONTROL
	# The DS1307 control register is used to control the operation of the SQW/OUT pin. 
	
	def setCONTROL(self, val):
		"""Set register CONTROL"""
		self.write(REG.CONTROL, val, 8)
	
	def getCONTROL(self):
		"""Get register CONTROL"""
		return self.read(REG.CONTROL, 8)
	
	# Bits OUT
	# Output Control:
	#           This bit controls the output level of the SQW/OUT pin when the square-wave output
	#           is disabled. If SQWE = 0, the logic level on the SQW/OUT pin is 1 if OUT = 1 and is 0 if OUT = 0. On initial
	#           application of power to the device, this bit is typically set to a 0. 
	
	# Bits unused_0
	# Bits SQWE
	# Square-Wave Enable: 
	#           This bit, when set to logic 1, enables the oscillator output. The frequency of
	#           the square-wave output depends upon the value of the RS0 and RS1 bits. With the square-wave output set to 1Hz,
	#           the clock registers update on the falling edge of the square wave. On initial application of power to the device, this
	#           bit is typically set to a 0. 
	
	# Bits unused_1
	# Bits RS
	# Rate Select:
	#           These bits control the frequency of the square-wave output when the squarewave
	#           output has been enabled. On initial application of power to the device, these bits are typically set to a 1. 
	#           See table: (p.9)
	#           | RS1 | RS0 | SQW/OUT OUTPUT | SQWE | OUT |
	#           |-----|-----|-----------------------|-----|
	#           | 0   | 0   | 1Hz            | 1    | X   |
	#           | 0   | 1   | 4.096kHz       | 1    | X   |
	#           | 1   | 0   | 8.192kHz       | 1    | X   |
	#           | 1   | 1   | 32.768kHz      | 1    | X   |
	#           | X   | X   | 0              | 0    | 0   |
	#           | X   | X   | 1              | 0    | 1   |
	#           
	
