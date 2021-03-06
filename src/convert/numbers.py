#!/usr/bin/env python3
#coding: utf-8
### 1st line allows to execute this script by typing only its name in terminal, with no need to precede it with the python command
### 2nd line declaring source code charset should be not necessary but for exemple pydoc request it



__doc__ = "provide converters for numbers"#information describing the purpose of this module
__status__ = "Development"#should be one of 'Prototype' 'Development' 'Production' 'Deprecated' 'Release'
__version__ = "3.0.0"# version number,date or about last modification made compared to the previous version
__license__ = "public domain"# ref to an official existing License
__date__ = "2017"#started creation date / year month day
__author__ = "N-zo syslog@laposte.net"#the creator origin of this prog,
__maintainer__ = "Nzo"#person who curently makes improvements, replacing the author
__credits__ = []#passed mainteners and any other helpers
__contact__ = "syslog@laposte.net"# current contact adress for more info about this file



def dec2hex(number):
	"""return a decimal number into its hexadecimal form"""
	return hex(number)[2:]


def dec2bin(number):
	"""Convert a decimal number to binary"""
	return bin(number)[2:]


def bin2dec(string):
	"""Convert a binary string to decimal number"""
	return int(string,2)

def hex2dec(string):
	"""Convert a hexadecimal string to decimal number"""
	return int(string,16)
