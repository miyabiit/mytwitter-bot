

### crontab 

```
5,20,35,50 * * * * /bin/sh /home/baker/bin/aktrace_warning.sh 2>&1 | cat > /home/baker/log/aktrace_warning.log
*/10 * * * * /bin/sh /home/baker/bin/magome_mail_check.sh 2>&1 | cat > /home/baker/log/magome_mail_check.log
10 22 * * * /usr/bin/python3.6 /home/baker/bin/yaichi-bot.py 2>&1 | cat > /home/baker/log/yaichi-bot.log
50 22 * * * /usr/bin/python3.6 /home/baker/bin/sherlock-bot.py 2>&1 | cat > /home/baker/log/sherlock-bot.log
```
