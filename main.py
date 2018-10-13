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

class MAINW:
    __config_path="creds.config"

    def __init__(self):
        argparser.add_argument("-STA", "--start", help="Wokes up server", action="store_true")
        argparser.add_argument("-STP", "--stop", help="Stops server", action="store_true")
        if len(argv) == 1:
            argparser.print_help(stderr)
            exit(1)
        sshcli.set_missing_host_key_policy(AutoAddPolicy())
        if path.exists(self.__config_path):
            confparser.read(self.__config_path)
        else:
            print('No config found.')
            exit(1) 
        if argparser.parse_args().start:
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
            sshcli.exec_command('powerOffVms && halt')
            print('Executed command to shutdown. Please wait')
            sshcli.close()


classcall = MAINW()