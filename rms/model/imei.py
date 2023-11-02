#!/usr/bin/python3
# @Time    : 2023-10-20
# @Author  : Kevin Kong (kfx2007@163.com)

class IMEI(object):

    def __init__(self, salesDate, salesCode=None, RMSstoreCode=None, accountNo=None, storeCode=None,  IMEI=None, SN=None,  price=None):
        self.salesCode = salesCode
        self.accountNo = accountNo
        self.storeCode = storeCode
        self.RMSstoreCode = RMSstoreCode
        self.IMEI = IMEI
        self.SN = SN
        self.salesDate = salesDate
        self.price = price

    def get_json(self):
        return {
            "salesCode": self.salesCode,
            "accountNo": self.accountNo,
            "storeCode": self.storeCode,
            "RMSstoreCode": self.RMSstoreCode,
            "IMEI": self.IMEI,
            "SN": self.SN,
            "salesDate": self.salesDate,
            # "price": self.price 
        }
