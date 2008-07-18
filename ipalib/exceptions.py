# Authors:
#   Jason Gerard DeRose <jderose@redhat.com>
#
# Copyright (C) 2008  Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 2 only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""
All custom exceptions raised by `ipalib` package.
"""

class IPAException(Exception):
	"""
	Use this base class for your custom IPA exceptions unless there is a
	specific reason to subclass from AttributeError, KeyError, etc.
	"""
	format = None

	def __init__(self, *args, **kw):
		self.args = args
		self.kw = kw

	def __str__(self):
		"""
		Returns the string representation of this exception.
		"""
		if self.format is None:
			if len(self.args) == 1:
				return unicode(self.args[0])
			return unicode(self.args)
		if len(self.args) > 0:
			return self.format % self.args
		return self.format % self.kw



class CommandOverride(IPAException):
	format = 'Cannot override command %r'
