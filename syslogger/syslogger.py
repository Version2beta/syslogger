import argparse
from logging import handlers
import logging

DEFAULT_FACILITY = "USER"
DEFAULT_LEVEL = "INFO"
DEFAULT_ADDRESS = "/dev/log"

class Syslogger(object):
  facilities = {
        "KERN": 0,
        "USER": 1,
        "MAIL": 2,
        "DAEMON": 3,
        "AUTH": 4,
        "SYSLOG": 5,
        "LPR": 6,
        "NEWS": 7,
        "UUCP": 8,
        "CRON": 9,
        "AUTHPRIV": 10,
        "FTP": 11,
        "LOCAL0": 16,
        "LOCAL1": 17,
        "LOCAL2": 18,
        "LOCAL3": 19,
        "LOCAL4": 20,
        "LOCAL5": 21,
        "LOCAL6": 22,
        "LOCAL7": 23,
      }
  levels = {
        "CRITICAL": 50,
        "ERROR": 40,
        "WARNING": 30,
        "INFO": 20,
        "DEBUG": 10,
      }

  def __init__(self,
        facility = DEFAULT_FACILITY,
        level = DEFAULT_LEVEL,
        address = DEFAULT_ADDRESS,
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
    self.facility(DEFAULT_FACILITY)
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
    self.level(DEFAULT_LEVEL)
  level = property(
        fget = get_level,
        fset = set_level,
        fdel = del_level
      )

  def log(self, message):
    l = self._logger.getLogger(__name__)
    syslog_handler = handlers.SysLogHandler(
          address = self.address,
          facility = self.facility
        )
    l.addHandler(syslog_handler)
    l.log(self.level, message)

def main():
  facs_and_levels = ( "A valid logging facility and level are required." +
        "\n\nFacilities:\n%s" % ", ".join(sorted(Syslogger.facilities)) +
        "\n\nLevels:\n%s" % ", ".join(sorted(Syslogger.levels)) + "\n"
      )
  parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog = facs_and_levels
      )
  parser.add_argument(
        'facility',
        default = DEFAULT_FACILITY,
        help = "Log facility that should receive message"
      )
  parser.add_argument(
        'level',
        default = DEFAULT_LEVEL,
        help = "Log level for the message"
      )
  parser.add_argument(
        'message',
        help = "Message to log"
      )
  parser.add_argument(
        '--address',
        default = DEFAULT_ADDRESS,
        help = "Socket or network address syslog daemon listens to"
      )
  args = parser.parse_args()
  try:
    l = Syslogger(args.facility, args.level, address = args.address)
  except KeyError:
    print facs_and_levels
    return
  l.log(args.message)

if __name__ == '__main__':
  main()
