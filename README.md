syslogger
=========

A quick program to write to a specified log facility at a specified log level.

Usage:

```
syslogger.py FACILITY LEVEL [--address ADDR [PORT]] MSG
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

