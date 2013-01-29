syslogger
=========

A quick program to write to a specified log facility at a specified log level.

Usage:

```
syslogger.py FACILITY LEVEL MESSAGE
```

where FACILITY is one of:

* LOG_AUTH
* LOG_AUTHPRIV
* LOG_CRON
* LOG_DAEMON
* LOG_FTP
* LOG_KERN
* LOG_LPR
* LOG_MAIL
* LOG_NEWS
* LOG_SYSLOG
* LOG_USER
* LOG_UUCP
* LOG_LOCAL0
* LOG_LOCAL1
* LOG_LOCAL2
* LOG_LOCAL3
* LOG_LOCAL4
* LOG_LOCAL5
* LOG_LOCAL6
* LOG_LOCAL7

and LEVEL is one of:

* LOG_DEBUG
* LOG_INFO
* LOG_NOTICE
* LOG_WARNING
* LOG_ERROR
* LOG_CRITICAL
* LOG_ALERT
* LOG_EMERG

and MESSAGE is the message you'd like to log.

I originally wrote this so I had a way to quickly and easily test my syslog-ng configuration. Of course there were probably already programs that would do this, but I had trouble finding them, so I landed here instead. On the bright side, it gave me the opportunity to mock the Python logging class for my unit test, using Gary Bernhardt's Dingus library. https://github.com/garybernhardt/dingus. I also used his Expecter library again. Big thanks to Gary.
