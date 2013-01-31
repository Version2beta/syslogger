import unittest
from dingus import Dingus
from expecter import expect

from syslogger import Syslogger

class TestLoggingFacilities(unittest.TestCase):
  def testDefaultFacility(self):
    l = Syslogger()
    expect(l.facility) == 1
  def testSettingValidFacility(self):
    l = Syslogger(facility = "DAEMON")
    expect(l.facility) == 3
  def testSettingInvalidFacility(self):
    with expect.raises(KeyError):
      l = Syslogger(facility = "NOT_REAL")

class TestLoggingLevels(unittest.TestCase):
  def testDefaultLevel(self):
    l = Syslogger()
    expect(l.level) == 20
  def testSettingValidLevel(self):
    l = Syslogger(level = "DEBUG")
    expect(l.level) == 10
  def testSettingInvalidLevel(self):
    with expect.raises(KeyError):
      l = Syslogger(level = "NOT_REAL")

class TestLogging(unittest.TestCase):
  logger = Dingus()
  def testLogging(self):
    l = Syslogger(logger = self.logger)
    l.log('Test message')
    expect(self.logger.calls('log').once());
