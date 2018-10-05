ESXi-Waker - Python utility with crontab-ui support for scheduling server startup & shutdown
==========

Table of contents
-----------------
* [Installation](#installation)
    * [Ansible](#ansible)
* [After Installation](#after-installation)

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
    --ask-become-pass \ # NOTE! IF YOU SPECIFIED ROOT AS SSH USERNAME YOU DONT NEED TO USE THIS ARGUMENT!
    playbooks/waker_deploy.yml
```

After installation
=====

As you deployed script, you have to open your browser with `<your ip>:8001` address and add such actions:

| Step №| Explanation|Action|
| ------------- |:-------------:|-------------|
|1      | Press Add button| # No additional action required | 
|2      |Into `Name` field write following text: |`Wakeup and shutdown server at specified time`|
|3      |Into `Command` field write following text: |`/home/main.py --start && sleep <amount_of_time>h && /home/main.py --stop`|
|4      |Specify when it will be triggered | Use your knowledge of cron syntax or use crontab.guru|
|5      |Check `Enable error logging` in checkbox| # No additional action required |
|6      |Press `Save` button| # No additional action required |

#### Additional explanations of 3th step
Where `sleep <amount_of_time>h` write how many hours it will wait, for example:

```/home/main.py --start && sleep 4h && /home/main.py --stop```


That's it! You've made it!

