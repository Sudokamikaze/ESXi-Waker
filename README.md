ESXi-Waker - Python utility with crontab-ui support for scheduling server startup & shutdown
==========

Table of contents
-----------------
* [Installation](#installation)
    * [Ansible](#ansible)

Installation
=====

#### Clone this repo

`git clone https://github.com/Sudokamikaze/ESXi-Waker.git`


Ansible
=====

Run this command and answer some questions before we can start
```
ansible-playbook \
    playbooks/ask_variables.yml
```

After that, execute main playbook by running this command:
```
ansible-playbook \
    --ask-become-pass \
    playbooks/waker_deploy.yml
```

That's it! You've made it!

