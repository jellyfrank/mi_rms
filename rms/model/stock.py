#!/usr/bin/python3
# @Time    : 2023-10-21
# @Author  : Kevin Kong (kfx2007@163.com)

class Stock(object):

    def __init__(self, stockDate, inventoryQty, accountNo=None, storeCode=None, RMSstoreCode=None, productId=None, productSKU=None, productCode=None):
        self.accountNo = accountNo
        self.stockDate = stockDate
        self.storeCode = storeCode
        self.RMSstoreCode = RMSstoreCode
        self.productId = productId
        self.productSKU = productSKU
        self.productCode = productCode
        self.inventoryQty = inventoryQty

    def get_json(self):
        return {
            "accountNo": self.accountNo,
            "stockDate": self.stockDate,
            "storeCode": self.storeCode,
            "RMSstoreCode": self.RMSstoreCode,
            "productId": self.productId,
            "productSKU": self.productSKU,
            "productCode": self.productCode,
            "inventoryQty": self.inventoryQty
        }
