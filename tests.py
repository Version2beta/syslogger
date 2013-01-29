import unittest
from expecter import expect

from syslogger import Logger

class TestLoggingFacilities(unittest.TestCase):
  def testDefaultFacility(self):
    l = Logger()
    expect(l.facility) == 1
  def testSettingValidFacility(self):
    l = Logger(facility = "LOG_DAEMON")
    expect(l.facility) == 3
  def testSettingInvalidFacility(self):
    l = Logger(facility = "LOG_NOT_REAL")
    expect(l.facility) == 1

class TestLoggingLevels(unittest.TestCase):
  def testDefaultLevel(self):
    l = Logger()
    expect(l.level) == 6
  def testSettingValidLevel(self):
    l = Logger(level = "LOG_DEBUG")
    expect(l.level) == 7
  def testSettingInvalidLevel(self):
    l = Logger(level = "LOG_NOT_REAL")
    expect(l.level) == 6

