import unittest
from dingus import Dingus
from expecter import expect

from syslogger import Logger

class TestLoggingFacilities(unittest.TestCase):
  def testDefaultFacility(self):
    l = Logger()
    expect(l.facility) == 1
  def testSettingValidFacility(self):
    l = Logger(facility = "DAEMON")
    expect(l.facility) == 3
  def testSettingInvalidFacility(self):
    with expect.raises(KeyError):
      l = Logger(facility = "NOT_REAL")

class TestLoggingLevels(unittest.TestCase):
  def testDefaultLevel(self):
    l = Logger()
    expect(l.level) == 20
  def testSettingValidLevel(self):
    l = Logger(level = "DEBUG")
    expect(l.level) == 10
  def testSettingInvalidLevel(self):
    with expect.raises(KeyError):
      l = Logger(level = "NOT_REAL")

class TestLogging(unittest.TestCase):
  logger = Dingus()
  def testLogging(self):
    l = Logger(logger = self.logger)
    l.log('Test message')
    expect(self.logger.calls('log').once());
