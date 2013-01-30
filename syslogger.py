from argparse import ArgumentParser
from logging import handlers
import logging

class Logger(object):
  facilities = {
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
  levels = {
        "LOG_EMERG": 0,
        "LOG_ALERT": 1,
        "LOG_CRIT": 2,
        "LOG_ERR": 3,
        "LOG_WARNING": 4,
        "LOG_NOTICE": 5,
        "LOG_INFO": 6,
        "LOG_DEBUG": 7,
      }

  def __init__(self,
        facility = "LOG_USER",
        level = "LOG_INFO",
        address = "/dev/log",
        logger = logging
      ):
    self._facility = None
    self._level = None
    self.set_facility(facility)
    self.set_level(level)
    self.address = address
    self._logger = logging
    pass

  def get_facility(self):
    return self._facility
  def set_facility(self, facility):
    self._facility = self.facilities[facility]
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
    self._level = self.levels[level]
  def del_level(self):
    self.level("LOG_INFO")
  level = property(
        fget = get_level,
        fset = set_level,
        fdel = del_level
      )

  def log(self, message):
    print __name__, self.address, self.facility, self.level, message
    l = self._logger.getLogger(__name__)
    syslog_handler = handlers.SysLogHandler(
          address = self.address,
          facility = self.facility
        )
    l.addHandler(syslog_handler)
    l.log(self.level, message)

def main():
  parser = ArgumentParser()
  parser.add_argument(
        'facility',
        default = "LOG_USER",
        help = "Log facility that should receive message"
      )
  parser.add_argument(
        'level',
        default = "LOG_INFO",
        help = "Log level for the message"
      )
  parser.add_argument(
        'message',
        help = "Message to log"
      )
  parser.add_argument(
        '--address',
        default = "/dev/log",
        help = "Socket or network address syslog daemon listens to"
      )
  args = parser.parse_args()
  try:
    l = Logger(args.facility, args.level, address = args.address)
  except KeyError:
    print "A valid logging facility and level are required."
    print "Facilities: %s" % ", ".join(Logger.facilities)
    print "Levels: %s" % ", ".join(Logger.levels)
    return
  l.log(args.message)

if __name__ == '__main__':
  main()
