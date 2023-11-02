#!/usr/bin/python3
# @Time    : 2023-10-18
# @Author  : Kevin Kong (kfx2007@163.com)

from rms.comm import Comm


class Sync(Comm):

    def sync_sales_qty(self, salesList):
        """
        Sync sales quantity.

        :param salesList: Sales List Data
        :return Response.
        """
        endpoint = "SyncQty"
        code = "utaakT2fgyPpS23OHOrQKgxpcHovA5Y0qTaezgH9UEKVegNn8O25Dg=="

        data = {
            "salesList": [sale.get_json() for sale in salesList]
        }

        return self.post(endpoint, code, data)

    def sync_imei(self, salesList):
        """
        Sync IMEI 

        :param salesList: SalesList with IMEI
        :return Response
        """

        endpoint = "SyncIMEI"
        code = "TZytiIMnLxEB1r1tTDEFjmE/Gs/aCfo3LiCt4U9IQFJYeWlzZL4gZw=="

        data = {
            "salesList": [sale.get_json() for sale in salesList]
        }

        return self.post(endpoint, code, data)

    def sync_stock_qty(self, stockList):
        """
        Sync Stock

        :param stockList: StockList to Sync
        :return Response
        """

        endpoint = "SyncStock"
        code = "1cyiAblHUYlwWQa7Uywyben1kMmZW5MtYv/MaoBlga7HJ89TPaJJQA=="
        data = {
            "stockList": [stock.get_json() for stock in stockList]
        }

        return self.post(endpoint, code, data)

    def sync_tickets(self, ticketList):
        """
        Sync Tickets

        :param tickets: Tickets to Sync
        :return Respone
        """

        endpoint = "SyncTickets"
        code = "egwIabC/yc31YyngyxdBZdWWa1ODl6gIlN0CblCfxcMp7JZ3D/zuOw=="

        data = {
            "ticketList": [ticket.get_json() for ticket in ticketList]
        }

        return self.post(endpoint, code, data)

    def sync_traffic_flow(self, trafficFlowList):
        """
        Sync TrafficeFlow

        :param trafficeflow: TrafficeFlow to Sync
        :return Response
        """

        endpoint = "SyncCustomerFlow"
        code = "rfjT1NiQJr27JwzLX2huO1m7HQtfm0FpsNIOQnO0RJn7AzFuIXSeow=="

        data = {
            "trafficFlowList": [flow.get_jons() for flow in trafficFlowList]
        }

        return self.post(endpoint, code, data)
