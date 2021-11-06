# -*- coding: utf-8 -*-
from .ttypes import Message
from .comand import Models, Comand
from .timeline import Timeline
from .server import Server
from .auth import Auth
class LINE(Auth, Models, Timeline, Comand):
    
    def __init__(self, idOrAuthToken=None, passwd=None, **kwargs):
        self.certificate = kwargs.pop('certificate', None)
        self.systemName = kwargs.pop('systemName', None)
        self.appType = kwargs.pop('appType', None)
        self.appName = kwargs.pop('appName', None)
        Auth.__init__(self)
        self.channelId = kwargs.pop('channelId', None)
        self.keepLoggedIn = kwargs.pop('keepLoggedIn', True)
        self.customThrift = kwargs.pop('customThrift', False)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode()
        if idOrAuthToken and passwd:
            self.loginWithCredential(idOrAuthToken, passwd)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(idOrAuthToken)
        self.__initAll()

    def __initAll(self):
        self.profile    = self.talk.getProfile()
        self.groups     = self.talk.getGroupIdsJoined()
        Models.__init__(self)
        Comand.__init__(self)
        Timeline.__init__(self)
