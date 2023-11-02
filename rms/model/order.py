#!/usr/bin/python3
# @Time    : 2023-10-21
# @Author  : Kevin Kong (kfx2007@163.com)

class Ticket(object):

    def __init__(self, countDate, tickets, storeCode=None, RMSstoreCode=None):
        self.countDate = countDate
        self.tickets = tickets
        self.storeCode = storeCode
        self.RMSstoreCode = RMSstoreCode

    def get_json(self):
        return {
            "countDate": self.countDate,
            "tickets": self.tickets,
            "storeCode": self.storeCode,
            "RMSstoreCode": self.RMSstoreCode
        }


class TrafficFlow(object):

    def __init__(self, countDate, inSum, outSum, accountNo=None,  storeCode=None, RMSstoreCode=None):
        self.countDate = countDate
        self.inSum = inSum
        self.outSum = outSum
        self.accountNo = accountNo
        self.storeCode = storeCode
        self.RMSstoreCode = RMSstoreCode

    def get_jons(self):
        return {
            "countDate": self.countDate,
            "inSum": self.inSum,
            "outSum": self.outSum,
            "accountNo": self.accountNo,
            "storeCode": self.storeCode,
            "RMSstoreCode": self.RMSstoreCode
        }
