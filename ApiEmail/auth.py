# -*- coding: utf-8 -*-
from .ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from .server import Server
from .session import Session
import requests, rsa, os
#from .callback import Callback
#var ulass = 'LLA/2.17.0 Redmi 8A Pro 9';
#var buah = 'ANDROIDLITE	2.17.0	Android OS	9';
LINE_HOST_DOMAIN = 'https://legy-jp-addr-long.line.naver.jp'
LINE_LOGIN_QUERY_PATH = '/api/v4p/rs'
LINE_AUTH_QUERY_PATH = '/api/v4/TalkService.do'
LINE_API_QUERY_PATH_FIR = '/F4'
LINE_POLL_QUERY_PATH_FIR = '/P4'
LINE_CALL_QUERY_PATH = '/V4'
LINE_CERTIFICATE_PATH = '/Q'
LINE_CHAN_QUERY_PATH = '/CH4'
LINE_SQUARE_QUERY_PATH = '/SQS1'
LINE_SHOP_QUERY_PATH = '/SHOP4'
#'Line/%s' % APP_VER
LINE_LANGUAGE = 'zh-Hant_TW'
LINE_SERVICE_REGION = 'TW'
deskwin = 'DESKTOPWIN\t6.7.0.2482\tDESKTOP-ALFINONH\t10.0.0-NT-x64'
class Auth(object):
    isLogin     = False
    authToken   = ""
    certificate = ""
    
    
    def __init__(self):
        self.server = Server(self.appType)
        self.server.setHeadersWithDict({
            'User-Agent': "Line/6.7.0.2482", #self.server.USER_AGENT,
            'X-Line-Application': deskwin, #self.server.APP_NAME,
            'X-Line-Carrier': self.server.CARRIER,
            'x-lal': 'zh-Hant_TW'
        })

    def __loadSession(self):
        self.talk = Session(LINE_HOST_DOMAIN, self.server.Headers,LINE_API_QUERY_PATH_FIR, self.customThrift).Talk()
        self.poll = Session(LINE_HOST_DOMAIN, self.server.Headers, LINE_POLL_QUERY_PATH_FIR, self.customThrift).Talk()
        self.call = Session(LINE_HOST_DOMAIN, self.server.Headers, LINE_CALL_QUERY_PATH, self.customThrift).Call()
        self.channel = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, LINE_CHAN_QUERY_PATH, self.customThrift).Channel()
        self.revision = self.poll.getLastOpRevision()
        self.isLogin = True

    def __loginRequest(self, type, data):
        lReq = LoginRequest()
        if type == '0':
            lReq.type = LoginType.ID_CREDENTIAL
            lReq.identityProvider = data['identityProvider']
            lReq.identifier = data['identifier']
            lReq.password = data['password']
            lReq.keepLoggedIn = data['keepLoggedIn']
            lReq.accessLocation = data['accessLocation']
            lReq.systemName = data['systemName']
            lReq.certificate = data['certificate']
            lReq.e2eeVersion = data['e2eeVersion']
        elif type == '1':
            lReq.type = LoginType.QRCODE
            lReq.keepLoggedIn = data['keepLoggedIn']
            if 'identityProvider' in data:
                lReq.identityProvider = data['identityProvider']
            if 'accessLocation' in data:
                lReq.accessLocation = data['accessLocation']
            if 'systemName' in data:
                lReq.systemName = data['systemName']
            lReq.verifier = data['verifier']
            lReq.e2eeVersion = data['e2eeVersion']
        else:
            lReq=False
        return lReq

    def loginWithCredential(self, _id, passwd):
        if self.systemName is None:
            self.systemName=self.server.SYSTEM_NAME
        if self.server.EMAIL_REGEX.match(_id):
            self.provider = IdentityProvider.LINE       # LINE
        else:
            self.provider = IdentityProvider.NAVER_KR   # NAVER
        
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeaders('X-Line-Application', self.appName)
        self.tauth = Session(LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_AUTH_QUERY_PATH).Talk(isopen=False)

        rsaKey = self.tauth.getRSAKeyInfo(self.provider)
        
        message = (chr(len(rsaKey.sessionKey)) + rsaKey.sessionKey +
                   chr(len(_id)) + _id +
                   chr(len(passwd)) + passwd).encode('utf-8')
        pub_key = rsa.PublicKey(int(rsaKey.nvalue, 16), int(rsaKey.evalue, 16))
        crypto = rsa.encrypt(message, pub_key).hex()

        try:
            with open('./db/'+_id + '.crt', 'r') as f:
                self.certificate = f.read()
        except:
            if self.certificate is not None:
                if os.path.exists(self.certificate):
                    with open(self.certificate, 'r') as f:
                        self.certificate = f.read()

        self.auth = Session(
            LINE_HOST_DOMAIN,
            self.server.Headers,
            LINE_LOGIN_QUERY_PATH).Auth(isopen=False
        )

        lReq = self.__loginRequest('0', {
            'identityProvider': self.provider,
            'identifier': rsaKey.keynm,
            'password': crypto,
            'keepLoggedIn': self.keepLoggedIn,
            'accessLocation': '8.8.8.8',
            'systemName': self.systemName,
            'certificate': self.certificate,
            'e2eeVersion': 0
        })

        result = self.auth.loginZ(lReq)
        
        if result.type == LoginResultType.REQUIRE_DEVICE_CONFIRM:
            print((result.pinCode))

            self.server.setHeaders('X-Line-Access', result.verifier)
            getAccessKey = self.server.getJson(self.server.parseUrl(self.server.LINE_CERTIFICATE_PATH), allowHeader=True)

            self.auth = Session(LINE_HOST_DOMAIN, self.server.Headers, LINE_LOGIN_QUERY_PATH).Auth(isopen=False)

            try:
                lReq = self.__loginRequest('1', {
                    'keepLoggedIn': self.keepLoggedIn,
                    'verifier': getAccessKey['result']['verifier'],
                    'e2eeVersion': 0
                })
                result = self.auth.loginZ(lReq)
            except:
                raise Exception('Login failed')
            
            if result.type == LoginResultType.SUCCESS:
                if result.certificate is not None:
                    with open('./db/'+_id + '.crt', 'w') as f:
                        f.write(result.certificate)
                    self.certificate = result.certificate
                if result.authToken is not None:
                    self.loginWithAuthToken(result.authToken)
                else:
                    return False
            else:
                raise Exception('Login failed')

        elif result.type == LoginResultType.REQUIRE_QRCODE:
            self.loginWithQrCode()
            pass

        elif result.type == LoginResultType.SUCCESS:
            self.certificate = result.certificate
            self.loginWithAuthToken(result.authToken)

    def loginWithQrCode(self):
        if self.systemName is None:
            self.systemName=self.server.SYSTEM_NAME
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeaders('X-Line-Application', self.appName)

        self.tauth = Session(LINE_HOST_DOMAIN, self.server.Headers, LINE_AUTH_QUERY_PATH).Talk(isopen=False)
        qrCode = self.tauth.getAuthQrcode(self.keepLoggedIn, self.systemName)

        print(QrUrl('line://au/q/' + qrCode.verifier, self.showQr))
        self.server.setHeaders('X-Line-Access', qrCode.verifier)

        getAccessKey = self.server.getJson(self.server.parseUrl(self.server.LINE_CERTIFICATE_PATH), allowHeader=True)
        
        self.auth = Session(LINE_HOST_DOMAIN, self.server.Headers,LINE_LOGIN_QUERY_PATH).Auth(isopen=False)
        
        try:
            lReq = self.__loginRequest('1', {
                'keepLoggedIn': self.keepLoggedIn,
                'systemName': self.systemName,
                'identityProvider': IdentityProvider.LINE,
                'verifier': getAccessKey['result']['verifier'],
                'accessLocation': self.server.IP_ADDR,
                'e2eeVersion': 0
            })
            result = self.auth.loginZ(lReq)
        except:
            raise Exception('Login failed')

        if result.type == LoginResultType.SUCCESS:
            if result.authToken is not None:
                self.loginWithAuthToken(result.authToken)
            else:
                return False
        else:
            raise Exception('Login failed')

    def loginWithAuthToken(self, authToken=None):
        if authToken is None:
            raise Exception('Please provide Auth Token')
        if self.appName is None:
            self.appName=self.server.APP_NAME
        if "CHROMEOS" in self.appName:
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36"# "requests.get("https://beapi.me/ualine?osname=chromeos").json()["result"]
            print(ua)
            self.server.setHeadersWithDict({
                'User-Agent': ua,
                'X-Line-Application': self.appName,
                'X-Line-Access': authToken
            })
        if "DESKTOPWIN" in self.appName:
            ua = "Line/6.7.0.2482"
            print(ua)
            self.server.setHeadersWithDict({
                'User-Agent': ua,
                'X-Line-Application': self.appName,
                'X-Line-Access': authToken
            })
        if "ANDROIDLITE" in self.appName:
            ua = requests.get("https://beapi.me/ualine?osname=androidlite").json()["result"]
            print (ua)
            self.server.setHeadersWithDict({
                "User-Agent": ua,
                "X-Line-Access": authToken,
                "X-Line-Application": "ANDROIDLITE	2.17.1	Android OS	6.0.1",
                "x-lal": "in_id",
                "content-type": "application/x-thrift",
                "content-length": 54,
                "accept-encoding": "gzip",
                "x-las":"F",
                "x-lam":"w"
            })
        self.authToken = authToken
        self.__loadSession()
        
    """def loginWithAuthToken(self, authToken=None):
        if authToken is None:
            raise Exception('Please provide Auth Token')
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeadersWithDict({
            'X-Line-Application': self.appName,
            'X-Line-Access': authToken
        })
        self.authToken = authToken
        self.__loadSession()"""

    def __defaultCallback(self, str):
        print(str)

    def logout(self):
        self.isLogin = False
        self.auth.logoutZ()
