clustertools
============

check_ssh.py


![](http://f.cl.ly/items/381g0m191N1y1l0V0h3I/Screen%20Shot%202014-05-27%20at%203.15.13%20AM.png)


Must authenticate via SSH. Log into all your servers once and upload your ssh keys.
See setup_parkinson.txt if you have root access and need to create an account with netid.
Also see setup_parkinson.txt if the file ~/.ssh/authorized_keys doesn't exist on the server.

```
cat ~/.ssh/id_rsa.pub | ssh asj936@cs.northwestern.edu 'cat >> .ssh/authorized_keys'
```
