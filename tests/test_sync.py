#!/usr/bin/python3
# @Time    : 2023-08-22
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from rms.api import RMS
from rms.model.sale_list import SaleList
from rms.model.imei import IMEI
from rms.model.stock import Stock
from rms.model.order import Ticket, TrafficFlow


class TestCommm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rms = RMS("rms_test", "110e9130fdd349ac9475ed18e553ce81", True)

    def test_sync_sale(self):
        salesList = [SaleList("2021-07-09 18:00:00 +08", 1, "E0010000",
                              productId="37174", productCode="6934177764066")]
        res = self.rms.sync.sync_sales_qty(salesList)
        self.assertEqual(res['message'], 'Success', res)

    def test_sync_imei(self):
        salesList = [IMEI("2023-01-01 00:00:00 +08", "37174",
                          storeCode="E0010000", IMEI="X00001", price=100)]
        res = self.rms.sync.sync_imei(salesList)
        self.assertEqual(res['message'], 'Success', res)

    def test_sync_stock(self):
        stockList = [Stock("2023-01-01 00:00:00 +08", 100,
                           storeCode="E0010000", productId="37174")]
        res = self.rms.sync.sync_stock_qty(stockList)
        self.assertEqual(res['message'], 'Success', res)

    def test_sync_order(self):
        ticketsList = [Ticket("2023-01-01 00:00:00 +08", 100, "E0010000")]
        res = self.rms.sync.sync_tickets(ticketsList)
        self.assertEqual(res['message'], 'Success', res)

    def test_sync_trafficeflow(self):
        trafficFlowList = [TrafficFlow(
            "2023-01-01 00:00:00 +08", 100, 150, "E0010000",storeCode="E0010000")]
        res = self.rms.sync.sync_traffic_flow(trafficFlowList)
        self.assertEqual(res['message'], 'Success', res)


if __name__ == "__main__":
    unittest.main()
