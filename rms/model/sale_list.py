#!/usr/bin/python3
# @Time    : 2023-10-18
# @Author  : Kevin Kong (kfx2007@163.com)

class SaleList(object):

    def __init__(self, salesDate, salesQty, storeCode=None, RMSstoreCode=None, productId=None, productSKU=None, productCode=None,  accountNo=None):
        self.salesDate = salesDate
        self.salesQty = salesQty
        self.storeCode = storeCode
        self.RMSstoreCode = RMSstoreCode
        self.productId = productId
        self.productSKU = productSKU
        self.productCode = productCode
        self.accountNo = accountNo

    def get_json(self):
        return {
            "salesDate": self.salesDate,
            "salesQty": self.salesQty,
            "storeCode": self.storeCode,
            "RMSstoreCode": self.RMSstoreCode,
            "productId": self.productId,
            "productSKU": self.productSKU,
            "productCode": self.productCode,
            "accountNo": self.accountNo
        }
