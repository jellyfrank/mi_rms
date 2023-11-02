#!/usr/bin/python3
# @Time    : 2023-08-22
# @Author  : Kevin Kong (kfx2007@163.com)

from rms.comm import Comm
from rms.sync import Sync

class RMS(object):

    def __init__(self,appid,appkey, sandbox=False):
        """
        init method.

        :param appid: appid.
        :param appkey: appkey for request.
        :param sandbox: using test environment if true.
        """
        self._appid = appid
        self._appkey = appkey
        self._sandbox = sandbox

    comm = Comm()
    sync = Sync()