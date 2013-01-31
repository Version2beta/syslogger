syslogger
=========

A quick program to write to a specified log facility at a specified log level.

I originally wrote this so I had a way to quickly and easily test my syslog-ng configuration. Of course there were probably already programs that would do this, but for whatever dumb reason, I couldn't find them. (`logger` came to mind much later - http://unixhelp.ed.ac.uk/CGI/man-cgi?logger+1.) On the bright side, it gave me the opportunity to mock the Python logging class for my unit test, using Gary Bernhardt's Dingus library. https://github.com/garybernhardt/dingus. I also used his Expecter library again. Big thanks to Gary. He's been my goto for Python + TDD.

Installation:
-------------

Syslogger is in pypi at http://pypi.python.org/pypi/Syslogger/. To install, simply use pip.

```
pip install syslogger
```

or maybe

```
sudo pip install --upgrade syslogger
```

Use:
----

`syslogger` runs from the command line.

```
syslogger FACILITY LEVEL [--address ADDRESS] MESSAGE
```

where FACILITY is one of:

* AUTH
* AUTHPRIV
* CRON
* DAEMON
* FTP
* KERN
* LPR
* MAIL
* NEWS
* SYSLOG
* USER
* UUCP
* LOCAL0
* LOCAL1
* LOCAL2
* LOCAL3
* LOCAL4
* LOCAL5
* LOCAL6
* LOCAL7

and LEVEL is one of:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

and ADDRESS is the address of the socket that your system logger is listening to (defaults to `/dev/log`),

and MESSAGE is the message you'd like to log.

API:
----

If you think syslogger might make your Python logging easier, feel free to use it in your code too.

```
from syslogger.syslogger import Syslogger
l = Syslogger(level="CRITICAL", facility="AUTH", address="/dev/log")
l.log("Hello world, love syslogger")
```

