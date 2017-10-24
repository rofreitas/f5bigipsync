# coding=utf-8
#!C:\Python27\python.exe

from bigip import Bigip

import sys
import os
import time
import atexit
import argparse
import getpass


class Main():
    def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument('--address',
                            required=True,
                            action='store',
                            help='BIG IP Address')

        parser.add_argument('--user',
                            required=True,
                            action='store',
                            help="Username")

        parser.add_argument('--password',
                            required=True,
                            action='store',
                            help='Password')

        args = parser.parse_args()

        return args

    args = get_args()

    bigip = Bigip(args.address,args.user,args.password)
    bigip.openConnection()
    #bigip.setVip("vs_dev_freedom_shopvasco_80")
    bigip.setVip("vs_netshoes_production_80")
    #bigip.getPool()
    bigip.getRule()
    #bigip.getMembers()
    #bigip.getGroups()


