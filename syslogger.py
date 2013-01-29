from argparse import ArgumentParser
from logging import handlers
import logging

class Logger(object):
  _facilities = {
        "LOG_KERN": 0,
        "LOG_USER": 1,
        "LOG_MAIL": 2,
        "LOG_DAEMON": 3,
        "LOG_AUTH": 4,
        "LOG_SYSLOG": 5,
        "LOG_LPR": 6,
        "LOG_NEWS": 7,
        "LOG_UUCP": 8,
        "LOG_CRON": 9,
        "LOG_AUTHPRIV": 10,
        "LOG_FTP": 11,
        "LOG_LOCAL0": 16,
        "LOG_LOCAL1": 17,
        "LOG_LOCAL2": 18,
        "LOG_LOCAL3": 19,
        "LOG_LOCAL4": 20,
        "LOG_LOCAL5": 21,
        "LOG_LOCAL6": 22,
        "LOG_LOCAL7": 23,
      }
  _levels = {
        "LOG_EMERG": 0,
        "LOG_ALERT": 1,
        "LOG_CRIT": 2,
        "LOG_ERR": 3,
        "LOG_WARNING": 4,
        "LOG_NOTICE": 5,
        "LOG_INFO": 6,
        "LOG_DEBUG": 7,
      }

  def __init__(self, facility = "LOG_USER", level = "LOG_INFO"):
    self._facility = None
    self._level = None
    self.set_facility(facility)
    self.set_level(level)
    pass

  def get_facility(self):
    return self._facility
  def set_facility(self, facility):
    if facility in self._facilities:
      self._facility = self._facilities[facility]
    else:
      self._facility = self._facilities["LOG_USER"]
  def del_facility(self):
    self.facility("LOG_USER")
  facility = property(
        fget = get_facility,
        fset = set_facility,
        fdel = del_facility
      )

  def get_level(self):
    return self._level
  def set_level(self, level):
    if level in self._levels:
      self._level = self._levels[level]
    else:
      self._level = self._levels["LOG_INFO"]
  def del_level(self):
    self.level("LOG_INFO")
  level = property(
        fget = get_level,
        fset = set_level,
        fdel = del_level
      )

  def log(self, message):
    pass

  @classmethod
  def Log(cls, facility, level, message):
    pass

