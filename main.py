#!/usr/bin/env python3
from os import path
from sys import exit, argv, stderr
from configparser import ConfigParser
from argparse import ArgumentParser
from subprocess import run
from paramiko import SSHClient, ssh_exception, AutoAddPolicy

argparser = ArgumentParser()
confparser = ConfigParser()
sshcli = SSHClient()
config_path="creds.config"

class MAINW:

    def __init__(self):
        sshcli.set_missing_host_key_policy(AutoAddPolicy())
        argparser.add_argument("-STA", "--start", help="Wokes up server", action="store_true")
        argparser.add_argument("-STP", "--stop", help="Stops server", action="store_true")
        if len(argv) == 1:
            argparser.print_help(stderr)
            exit(1)
        elif argparser.parse_args().start:
            self.door(argumentto=1)
        elif argparser.parse_args().stop:
            self.door(argumentto=2)

    def door(self, argumentto):
        if argumentto == 1:
            print('Woking server...')
            try:
                run(['wol', confparser['DEFAULT']['MAC_ADDR']])
            except FileNotFoundError:
                if path.exists('/usr/bin/etherwake'):
                    print('Link statically /usr/bin/etherwake to /usr/bin/wol that we could continue')
                else:
                    print('Probably your host missing "wol" package. You must install it that we could continue')
                exit(1)
            print('Sent packet!')
        elif argumentto == 2:
            try:
                sshcli.connect(confparser['DEFAULT']['SSH_ADDR'], username=confparser['DEFAULT']['SSH_USER'], password=confparser['DEFAULT']['SSH_PASSWD'])
            except ssh_exception.AuthenticationException:
                print("Can't login due wrong password or login. Change them and try again.")
                exit(1)
            esxi_ver = sshcli.exec_command("vmware -v | awk {'print $3'}")
            if esxi_ver == "6.0.0" or "5.5.0": 
                sshcli.exec_command('powerOffVms')
            elif esxi_ver == "6.5.0" or "6.7.0":
                for vmid in sshcli.exec_command("vim-cmd vmsvc/getallvms | awk {'print $1'} | sed 's/Vmid//g' | sed 1d")
                    sshcli.exec_command("vim-cmd vmsvc/power.shutdown ", vmid)
            sshcli.exec_command('halt')
            print('Executed command to shutdown. Please wait')
            sshcli.close()

if path.exists(config_path):
    confparser.read(config_path)
    classcall = MAINW()
else:
    print('No config found.')
    exit(1) 
