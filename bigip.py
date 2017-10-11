import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from f5.bigip import ManagementRoot

class Bigip():

    def __init__(self,address,user,password):
        self.address = address
        self.user = user
        self.password = password
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def openConnection(self):
        self.mgmt = ManagementRoot(self.address,self.user,self.password)

    def setVip(self,vsname):
        self.vip = self.mgmt.tm.ltm.virtuals.virtual.load(name=vsname)

    def getPool(self):
        self.pool = self.mgmt.tm.ltm.pools.pool.load(name=self.vip.pool.split("/")[2],partition='Common')
        print(self.vip.pool.split("/")[1])
        print(self.vip.pool.split("/")[2])

    def getRule(self):
        rules = self.vip.rules
        for rule in rules:
            print(rule.strip('/Common'))

    def getMembers(self):
        members = self.pool.members_s.get_collection()
        for member in members:
            print member.address

