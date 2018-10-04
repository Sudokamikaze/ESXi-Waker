#!/bin/python3.6
import os, sys
import argparse, configparser
import subprocess
import paramiko

argparser = argparse.ArgumentParser()
confparser = configparser.ConfigParser()
sshcli = paramiko.SSHClient()

class MAINW:
    __config_path="creds.config"

    def __init__(self):
        argparser.add_argument("-STA", "--start", help="Wokes up server", action="store_true")
        argparser.add_argument("-STP", "--stop", help="Stops server", action="store_true")
        sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if os.path.exists(self.__config_path):
            confparser.read(self.__config_path)
        else:
            print('No config found.')
            os.sys.exit(1) 
        if argparser.parse_args().start:
            self.door(argumentto=1)
        elif argparser.parse_args().stop:
            self.door(argumentto=2)

    def door(self, argumentto):
        if argumentto == 1:
            print('Woking server...')
            subprocess.run(['wol', confparser['DEFAULT']['MAC_ADDR']])
            print('Sent packet!')
        elif argumentto == 2:
            sshcli.connect(confparser['DEFAULT']['SSH_ADDR'], username=confparser['DEFAULT']['SSH_USER'], password=confparser['DEFAULT']['SSH_PASSWD'])
            sshcli.exec_command('powerOffVms && halt')
            print('Executed command to shutdown. Please wait')
            sshcli.close()


classcall = MAINW()