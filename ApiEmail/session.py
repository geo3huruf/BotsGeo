# -*- coding: utf-8 -*-
from .transport import THttpClient
from thrift.protocol import TCompactProtocol
from .corever import(
        AuthService,
        TalkService,
        ChannelService,
        CallService
)
from .ttypes import *

class Session:

    def __init__(self, url, headers, path='', customThrift=False):
        self.host = url + path
        self.headers = headers
        self.customThrift = customThrift

    def Auth(self, isopen=True):
        self.transport = THttpClient(self.host, customThrift=self.customThrift)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._auth  = AuthService.Client(self.protocol)

        if isopen:
            self.transport.open()

        return self._auth
       
    """def Talk(self, isopen=True):
        try:
            #if "ANDROIDLITE" in self.headers['User-Agent']:
            from .thrift.transport import THttpClientLite as THttpClient
            self.transport = THttpClient.THttpClient(self.host)
        except:
            self.transport = THttpClient(self.host, customThrift=self.customThrift)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)
        if isopen:
            self.transport.open()

        return self._talk"""

    def Talk(self, isopen=True):
        self.transport = THttpClient(self.host, customThrift=self.customThrift)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)
        if isopen:
            self.transport.open()

        return self._talk

    def Channel(self, isopen=True):
        self.transport = THttpClient(self.host, customThrift=self.customThrift)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._channel  = ChannelService.Client(self.protocol)

        if isopen:
            self.transport.open()

        return self._channel

    def Call(self, isopen=True):
        self.transport = THttpClient(self.host, customThrift=self.customThrift)
        self.transport.setCustomHeaders(self.headers)

        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._call  = CallService.Client(self.protocol)

        if isopen:
            self.transport.open()

        return self._call

