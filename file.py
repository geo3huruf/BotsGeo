## -*- coding: utf-8 -*-
from ApiEmail.client import LINE
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
from SecondaryQrLogin import *
from SecondaryQrLogin.ttypes import *
from oepoll import OEPoll
from ApiEmail.ttypes import(
        ChatRoomAnnouncementContents,
        OpType,
        MediaType,
        ContentType,
        ApplicationType,
        ErrorCode, Message,
        ContactSetting,
        TalkException
)

from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from urllib.parse import urlencode, quote
from pathlib import Path
import youtube_dl
import time, random, sys, json, codecs, re, os, shutil, requests, ast, pytz, atexit, traceback, base64, pafy, livejson, timeago, math, argparse, urllib, urllib.parse, subprocess, asyncio, humanize, threading, string, httpx
#import axolotl_curve25519 as curve
requests.packages.urllib3.disable_warnings()
from ApiEmail.comand import comandText
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def update_non_existing_inplace(original_dict, to_add):
    for key, value in original_dict.items():
        if key not in to_add:
            to_add[key] = value
        if type(value) == dict:
            for k, v in value.items():
                if k not in to_add[key]:
                    to_add[key][k] = v
    original_dict.update(to_add)
    return original_dict

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'
import requests.packages.urllib3.exceptions as urllib3_exceptions
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
_session = requests.session()
dist_http = httpx.Client(http2=True, timeout=240)
#==============================================
programStart = time.time()
#=================[ RUN BOTS COMPACK ]===================
certificate="0e3f7fbfff359e6f44d597cd19fee8672d9beb40d4c2294f90cd0ed1cf8b4e13"
"""tokenya = {
    "email": "geocipto@gmail.com",
    "passwd": "brajA321",
    "certificate": "29293eb2c9b19bf0da1a24f45c29b5ed13a3d2ceb1555af00b63c962e4e20934"
}"""
tokenya = {
    "email": "hakonone6@hotmail.com",
    "passwd": "Braja10123",
    "certificate": "9f3ef6548ac9f0e42a6ea96f52e277d1b5de902c3d0477029edff960b1e92779"
}

deskwin = 'DESKTOPWIN\t6.7.0\tDESKTOP-ALFINONH\t10.0.0-NT-x64'
ios = "IOS\t10.0.0\tiPhone OS\t12.1.4"
adroid = "ANDROIDLITE\t2.16.0\tAndroid OS\t6.0.1"
adroidlite = 'ANDROIDLITE\t2.17.0\tAndroid OS\t9'
TYPE = ["DESKTOPMAC\t6.7.2\tMAC\t10","DESKTOPMAC\t6.7.0\tMAC\t10","DESKTOPMAC\t6.6.0\tMAC\t10"]
chrom = "CHROMEOS\t2.4.7\tChrome OS\t1"
Token = livejson.File('db/token.json', True, False, 4)

line = LINE(tokenya["email"],tokenya["passwd"],certificate=tokenya["certificate"], appName=deskwin)

if line:
    print ('++ AuthToken : %s' % line.authToken)
    print ('++ ProfileMid : %s' % line.profile.mid)
else:
    sys.exit('##----- LOGIN CLIENT (Failed) -----##')
print ('##----- LOGIN CLIENT (Success) -----##')

myMid = line.profile.mid
myOwn = ['uce6d9daa08bce025bd880d7f9fea1746']
oepoll = OEPoll(line)
settings = livejson.File('db/helper.json', True, False, 4)
Bots = livejson.File('db/backup.json', True, False, 4)
myBots = [myMid]

usa = comandText(line)
bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}
#=================================================

def createSecondaryQrCodeLoginService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = SecondaryQrCodeLoginService.Client(protocol)
    return client

def createSecondaryQrCodeLoginPermitNoticeService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = SecondaryQrCodeLoginPermitNoticeService.Client(protocol)
    return client

def loginqr(to, hander):
    if 'desktopwin' in hander:
        handers = 'DESKTOPWIN\t6.7.0\tDESKTOP-GEO\t10.0;SECONDARY'
        agent = 'Line/6.7.0'
        certificate = "\n"
    if "iosipad" in hander:
        handers = "IOSIPAD\t10.3.0\tiOS\t13.3;SECONDARY"
        agent = 'Line/5.21.3'
        certificate = "\n"
    if "chrome" in hander:
        handers = "CHROMEOS\t2.4.7\tChrome OS\t1;SECONDARY"
        agent = 'MozilX-Line-Application/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
        certificate = "\n"
    if 'desktopmac' in hander:
        handers = 'DESKTOPMAC\t6.7.0\tDESKTOP-GEO\t10.0;SECONDARY'
        agent = 'Line/6.7.0'
        certificate = "\n"
    host = 'https://gwz.line.naver.jp'
    qrEndpoint = '/acct/lgn/sq/v1'
    verifierEndpoint = '/acct/lp/lgn/sq/v1'
    url = host+qrEndpoint
    headers = {'User-Agent': agent, 'X-Line-Application': handers, 'x-lal': 'en_id', 'server': random.choice(["pool-1","pool-2"])}
    cl = createSecondaryQrCodeLoginService(url, headers)
    session = cl.createSession(CreateQrSessionRequest())
    session_id = session.authSessionId
    sys.stdout = open('login.txt', 'w')
    qrcode = cl.createQrCode(CreateQrCodeRequest(session_id))
    qrCode = qrcode.callbackUrl
    print ('Qr Code : ', qrCode)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    with open('login.txt', 'r') as f:
        output = f.read()
    line.sendMessage(to, output)
    os.remove('login.txt')
    url = host+verifierEndpoint
    headers = {'User-Agent': agent, 'X-Line-Application': handers, 'X-Line-Access': session_id, 'x-lal': 'en_id','server': random.choice(["pool-1","pool-2"])}
    client_verif = createSecondaryQrCodeLoginPermitNoticeService(url, headers)
    qrverified = client_verif.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session_id))
    if certificate =="oke":
        certificate = input('Input your certificate : ')
    else:
        try:
            certverified = cl.verifyCertificate(VerifyCertificateRequest(session.authSessionId, certificate))
        except SecondaryQrCodeException as error:
            print ('Error Verify Certificate :', error)
            sys.stdout = open('login.txt', 'w')
            pincode = cl.createPinCode(CreatePinCodeRequest(session.authSessionId))
            print ('Pin Code :', pincode.pinCode)
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            with open('login.txt', 'r') as f:
                output = f.read()
                print ('Pin Code :', output)
            line.sendMessage(to, output)
            #os.remove("login.txt")
            sys.stdout = open('login.txt', 'w')
            pincodeverified = client_verif.checkPinCodeVerified(line.CheckPinCodeVerifiedRequest(session.authSessionId))
            print ('LOGIN QR DONE BOSSKU')
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            with open('login.txt', 'r') as f:
                output = f.read()
            line.sendMessage(to, output)
            os.remove("login.txt")
        except Exception:
            traceback.print_exc()
        sys.stdout = open('login.txt', 'w')
        qrcodelogin = cl.qrCodeLogin(QrCodeLoginRequest(session.authSessionId, 'DESKTOP DENMASGEO', True))
        print (f'Qr AuthToken : {qrcodelogin.accessToken}\nCRT : {qrcodelogin.certificate}\nHeanders for login: {handers}')
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        with open('login.txt', 'r') as f:
            output = f.read()
        line.sendMessage(to, output.split(";SECONDARY")[0])
        os.remove("login.txt")

#==================================================
def sendNotifi(message):
    params = {"message": message}
    data = requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": "Bearer lTfVogqLPMeGtW8KjB7CtbO9NQoIXi0vwsbTwNuMGqB"}, params=params)
    return data

def Status_Cek(self):
    try: self.deleteOtherFromChat('c0f9bac8e15c8ade105cda3c9415d9ad0', ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "KICK : [√] MASIH SEGER COK"
    except: has1 = "KICK : [×] LIMIT COK"
    try: self.inviteIntoChat('c0f9bac8e15c8ade105cda3c9415d9ad0', ["u45882d0ead1703855dbc60d40e37bec7"]);has2 = "=•> INVITE : [√] MASIH SEGER COK"
    except: has2 = "KICK : [×] LIMIT COK"
    hasil = has1+"\n"+has2
    return hasil

def BL_Dell():
    for data in settings["blacklist"]["target"]:
        return data
        
def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd
    
def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def removeCmdV2(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split('\n')
    return text_[len(sep[0] + '\n'):]
def executeOp(op):
    try:
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
                if settings['autoAdd']['reply']:
                    if '@!' not in settings['autoAdd']['message']:
                        line.sendMessage(op.param1, settings['autoAdd']['message'])
                    else:
                        line.sendMention(op.param1, settings['autoAdd']['message'], [op.param1])
                        
        if op.type == 13 or op.type == 124:
            if settings['autoJoin']['status'] and myMid in op.param3:
                if op.param2 in myOwn or op.param2 in myBots:
                    line.talk.acceptGroupInvitation(0, op.param1)
                    line.deleteOtherFromChat(op.param1, settings["blacklist"]["target"])
                    #if op.param2 in settings["blacklist"]["target"]:
                  #      line.deleteOtherFromChat(op.param1, settings["blacklist"]["target"])
                   # else: print ("bl bot")
                    print ("invitan Joined")
                    if settings['autoJoin']['reply']:
                        if '@!' not in settings['autoJoin']['message']:
                            line.sendMessage(op.param1, settings['autoJoin']['message'])
                        else:
                            line.sendMention(op.param1, settings['autoJoin']['message'], [op.param2])
            if settings['autoLeave']['status'] and myMid in op.param3:
                line.talk.acceptGroupInvitation(0, op.param1)
                if settings['autoLeave']['reply']:
                    if '@!' not in settings['autoLeave']['message']:
                        line.sendMessage(op.param1, settings['autoLeave']['message'])
                    else:
                        line.sendMention(op.param1, settings['autoLeave']['message'], [op.param2])
                line.talk.leaveGroup(0, op.param1)
            if(op.param3 in settings["blacklist"]["target"]):
                missu = op.param3 #.replace('\x1e',',').split(',')
                print (missu)
                for absi in missu:
                    if absi not in myOwn and absi not in myBots:
                        try: line.cancelChatInvitation(op.param1,[op.param3])
                        except:
                            try: line.cancelChatInvitation(op.param1,[op.param3])
                            except:
                                try:
                                    USA = line
                                    chat = USA.getChats([op.param1]).chats[0]
                                    for target in settings["blacklist"]["target"]:
                                        if target in list(chat.extra.groupExtra.inviteeMids) or target in list(chat.extra.groupExtra.memberMids):
                                            USA.cancelChatInvitation(op.param1,[target])
                                        USA.deleteOtherFromChat(op.param1,[target])
                                except: pass
#==========================================
        if op.type == 17 or op.type == 130:
                if op.param1:
                    if op.param2 in settings["blacklist"]["target"]:
                        if(op.param2 not in myOwn or op.param2 not in myBots):
                            try:
                                jmlh = 1
                                try:
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            line1.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                    else: pass
                                except: pass
                                try:
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            line.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                    else: pass
                                except: pass
                                try:
                                    data = line
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            data.deleteOtherFromChat(op.param1, [op.param2])
                                    else: pass
                                except: pass
                            except TalkException as talk_error:
                                TalkException.code(109)
                    else: pass
                    
#        if op.type == 18 or op.type == 132:
#                if op.param2 not in myOwn or op.param2 not in myBots:
#                    settings["blacklist"]["target"][op.param2] = True
#                else: pass
                        
        if op.type == 19 or op.type == 133:
                if(op.param3 in myMid):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = line
                             JSSI = {}
                             chat = line.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else:
                                         JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                 data.inviteIntoChat(op.param1, JSSI)
                        except:
                             try:
                                 data = line
                                 JSSI = {}
                                 chat = data.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in data.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         data.deleteOtherFromChat(op.param1,[op.param2])
                                         data.inviteIntoChat(op.param1, JSSI)
                             except: pass
                if(op.param3 in myBots):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                            jmlh = 1
                            try:
                                if jmlh <= 10:
                                    for x in range(jmlh):
                                        try: line.talk.inviteIntoGroup(0, op.param1, [op.param3])
                                        except: line.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                else: pass
                            except: pass
                        except: pass
                        try:
                             data = line
                             JSSI = {}
                             chat = data.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else:
                                         JSSI[targets] = True
                                 data.inviteIntoChat(op.param1, JSSI)
                             data.deleteOtherFromChat(op.param1,[op.param2])
                        except: pass
                if(op.param3 in myOwn):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                            jmlh = 1
                            try:
                                if jmlh <= 10:
                                    for x in range(jmlh):
                                        try:
                                            line.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                        except:
                                            line.talk.inviteIntoGroup(0, op.param1, [op.param3])
                                else: pass
                            except: pass
                        except:
                            try:
                                data = line
                                JSSI = {}
                                chat = data.getChats([op.param1]).chats[0]
                                for targets in myOwn:
                                    if targets not in data.talk.getProfile().mid:
                                        if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                            JSSI[targets] = True
                                        else:
                                            JSSI[targets] = True
                                    data.inviteIntoChat(op.param1, JSSI)
                                data.deleteOtherFromChat(op.param1,[op.param2])
                            except: pass
                            
        if op.type == 11 or op.type == 122:
            print (op)
            if op.param3 =="1":
               # target = line.talk.getProfile(op.param2).displayName
                line.sendMessage(op.param1, "\njiah update Name group\nSender: {target}","text")
            if op.param3 =="2":
                #target = line.talk.getProfile(op.param2).displayName
              #  line.sendMessage(op.param1, f"\n jiah update foto group\nSender: {op.param2}","text")
                img = f"https://obs-sg.line-apps.com/r/talk/g/{op.param1}/preview"
                line.sendMessage(op.param1, f"\n{img}")
            if op.param3 =="4":
                #target = line.talk.getProfile(op.param2).displayName
                line.sendMessage(op.param1, f"\njiah update QR group\nSender: {op.param2}","text")
 
        if op.type == 7:
                print (op)
        if op.type == 32 or op.type == 126:
                print (op)
#========[fets oprasi]=================
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            txt = text.lower()
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        for texx in text.split(' & '):
                            if sender:
                                try:
                                    usa.CmdText(
                                        msg.id,
                                        to,
                                        sender,
                                        texx,
                                        msg,
                                        settings,
                                        myOwn,
                                        myBots,
                                        programStart
                                    )
                                except Exception:
                                    error = traceback.format_exc()
                                    print (error)
                if msg.contentType == 16:
                	if msg.toType in (2,1,0):
                	    try:
                	        adri = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                	        line.likePost(adri[0], adri[1], 1003)
                	        line.createCommentStk(adri[0], adri[1], settings["commentPost"], id=51626501,pkgid=11538,pkgver=1)
                	        line.sendMessage(to, "Success Like Your Post!")
                	    except Exception as e:
                	        purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                	        line.likePost(purl[0], purl[1], 1003)
                	        line.createCommentStk(purl[0], purl[1], settings["commentPost"], id=51626501,pkgid=11538,pkgver=1)
                	        line.sendMessage(to, "Success Like Your Post!")
                	    print (msg.contentMetadata)
                	else: pass
                	
        if op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to = sender if not msg.toType and sender != myMid else receiver
            txt= text.lower()
            if settings['autoRead']:
            	line.talk.sendChatChecked(0, to, msg_id)
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = command(text)
                    for cmd in cmd.split(' & '):
                        if cmd == '!restart' and sender in myOwn:
                            line.sendMessage(to, "Restart Bots By Cmd ;)")
                            settings['restartPoint'] = to
                            line.restartProgram()
                        elif cmd.startswith('exc') and sender in myOwn:
                            try:
                                output = '「 Output 」\n'
                                sys.stdout = open('exec.txt', 'w')
                                try:
                                    exec(removeCmd(text, setKey))
                                    print ()
                                except Exception:
                                    exec(removeCmdV2(text, setKey))
                                    print ()
                                sys.stdout.close()
                                sys.stdout = sys.__stdout__
                                with open('exec.txt', 'r') as f:
                                    output += f.read()[:-2]
                                k = len(output)//10000
                                for aa in range(k+1):
                                    line.sendMessage(to,'{}'.format(output[aa*10000 : (aa+1)*10000]))
                            except Exception as ee:
                                line.sendMessage(to, f"{ee}")
                                os.remove('exec.txt')
                        elif cmd.startswith('$') and sender in myOwn:
                            separate = text.split(" ")
                            textny = text.replace(separate[0] + " ","")
                            a = subprocess.getoutput(textny)
                            k = len(a)//10000
                            for aa in range(k+1):
                                try: line.sendMessage(to, '\n{}'.format(a.strip()[aa*10000 : (aa+1)*10000]))
                                except:
                                    error = traceback.format_exc()
                                    line.sendMessage(to, "Access error, please try again.\n"+error)
                        elif cmd == ".sp" and sender in myOwn:
                            mess = line.sendSpeedMSG()
                            profile = line.sendSpeedProfile()
                            line.sendMessage(to, f"Speed getMessage :: {mess}\nSpeed getProfile :: {profile}")
                                
                        elif cmd == ".respon" and sender in myOwn:
                            line.sendMention(to, "@! aim induk ", [line.profile.mid])
                            
                        elif cmd == ".cek" and sender in myOwn:
                            try:
                                data = Status_Cek(line)
                                line.sendMessage(to, line.sendTextsUnicode(f"Induk :: \n=•> {data}"))
                            except TalkException:
                                data = Status_Cek(line)
                                line.sendMessage(to, line.sendTextsUnicode(f"{data}"))
                        
                        elif cmd == ".inv" and sender in myOwn:
                            try:
                                client = line
                                JSSI = {}
                                chat = client.getChats([to]).chats[0]
                                for targets in myBots:
                                    if targets not in client.talk.getProfile().mid:
                                        if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                            JSSI[targets] = True
                                        else: JSSI[targets] = True
                                    #client.inviteIntoChat(to, JSSI)
                                        client.talk.inviteIntoGroup(0, to, [botAim])
                                    else:pass
                            except TalkException as talk_error:
                                print(talk_error)
                                pass
                                
                        elif cmd =='uns' and sender in myOwn:
                            msgs = line.getRecentMessagesV2(to, 1000)
                            for m in msgs:
                                if m._from == line.profile.mid:
                                    line.unsendMessage(m.id)
                            line.sendMessage(to,"Done unsend to %s" % len(m))
                                
                        elif cmd == "removechat" and sender in myOwn:
                            try:
                                line.removeAllMessages(to)
                                line.sendMessage(to,line.sendTextsUnicode("DONE BOSS"))
                            except: pass
                                
                        elif cmd == "echat" and sender in myOwn:
                            try:
                                line.talk.sendChatRemoved(0,to, msg.id)
                                line.sendMessage(to,line.sendTextsUnicode("DONE BOSS"))
                            except: pass
            			
                        elif cmd == ".cban" and sender in myOwn:
                            line.sendMessage(to,"Done Reset Blacklist %s" % len(settings["blacklist"]["target"]))
                            settings["blacklist"]["target"] = {}
                        
                        elif cmd.startswith(".listbl") and sender in myOwn:
                            separator = text.split(' ')
                            n1 = text.replace(separator[0]+' ','')
                            texttl = n1.lower()
                            texx = 'Notings BL To list'
                            res = '╭「 <LIST BLACKLIST> 」───'
                            res += f"\n{texx}"
                            res += '\n├ Usage : '
                            res += '\n│• .Listbl'
                            res += '\n│• .Listbl reset'
                            res += '\n╰「 <UNIVERSAL> 」── '
                            if cmd == '.listbl':
                                members = []
                                Blacklist = settings["blacklist"]["target"]
                                members = [mem for mem in Blacklist]
                                if members:
                                    daftar = "LIST BLACKLIST"
                                    sqr = "Comand list For get: "
                                    sqr += "\n│.Listbl"
                                    sqr += "\n│.Listbl reset"
                                    line.mentionMembers(msg_id, to, daftar, sqr, members)
                                else:
                                    line.sendMessage(to, line.parsingRes(line.sendTextsUnicode(res)))
                            elif texttl == "reset":
                                line.sendMessage(to, 'Done reset Blacklist %s' %len(settings["blacklist"]["target"]))
                                settings["blacklist"]["target"] = {}
                            else: line.sendMessage(to,line.parsingRes(res))
                            
                        elif cmd == ".cancelall" and sender in myOwn:
                            chat = line.getChats([to]).chats[0]
                            data = list(chat.extra.groupExtra.inviteeMids)
                          #  line.talk.cancelGroupInvitation(0, to, data)
                            for target in data:
                                jmlh = 10
                                try:
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            time.sleep(0.8)
                                            line.cancelChatInvitation(to, [target])
                                except TalkException as talk_error: pass
                              #  line.talk.cancelGroupInvitation(0, to, [target])
                              #  time.sleep(0.8)

                        elif cmd.startswith('/login'):
                            textt = removeCmd(text, setKey)
                            if "desktopwin" in textt:
                                headers = {
                        		        'User-Agent': 'Line/6.7.0',
                        		        'X-Line-Application': 'DESKTOPWIN\t6.7.0.2482\tDESKTOP-USAGEO\t10.0.0-NT-x64;SECONDARY',
                        		        'x-lal': 'en_id'
                                }
                                certificate = "\n"
                            if "desktopmac" in textt:
                                headers = {
                        		        'User-Agent': 'Line/6.7.0',
                        		        'X-Line-Application': 'DESKTOPMAC\t6.7.0.2482\tDESKTOP\t10.0.0-NT-x64;SECONDARY',
                        		        'x-lal': 'en_id'
                                }
                                certificate = "\n"
                            elif "chromeos" in textt:
                                headers = {
                        		        'User-Agent': 'MozilX-Line-Application/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
                        		        'X-Line-Application': 'CHROMEOS\t2.4.7\tChrome OS\t1;SECONDARY',
                        		        'x-lal': 'en_id'
                                }
                                certificate = "\n"
                            elif "iosipad" in textt:
                                headers = {
                        		        'User-Agent': 'Line/5.21.3',
                        		        'X-Line-Application': 'IOSIPAD\t10.3.0\tiOS\t13.3;SECONDARY',
                        		        'x-lal': 'en_id'
                                }
                                certificate = "\n"
                            elif "androidlite" in textt:
                                headers = {
                        		        'User-Agent': 'LLA/2.16.0 CW-6HZ0JF',
                        		        'X-Line-Application': 'ANDROIDLITE\t2.17.0\tAndroid OS\t9',
                        		        "x-lal": "in_id",
                        		        "content-type": "application/x-thrift",
                        		        "content-length": 54,
                        		        "accept-encoding": "gzip",
                        		        "x-las":"F",
                        		        "x-lam":"w"
                        		        #'x-lal': 'en_id'
                                }
                                certificate = "\n"
                            else: pass
                            try:
                        	        #private_key = curve.generatePrivateKey(os.urandom(32))
                        	        #public_key = curve.generatePublicKey(private_key)
                        	        #secret = urllib.parse.quote(base64.b64encode(public_key).decode())
                        	        #version = 1
                        	        #secret_ = f"?secret={secret}&e2eeVersion={version}"
                        	        host = 'https://gxx.line.naver.jp'
                        	        qrEndpoint = '/acct/lgn/sq/v1'
                        	        verifierEndpoint = '/acct/lp/lgn/sq/v1'
                        	        url = host+qrEndpoint
                        	        cl = createSecondaryQrCodeLoginService(url, headers)
                        	        session = cl.createSession(CreateQrSessionRequest())
                        	        session_id = session.authSessionId
                        	        sys.stdout = open('login.txt', 'w')
                        	        qrcode = cl.createQrCode(CreateQrCodeRequest(session_id))
                        	        qrCode = qrcode.callbackUrl
                        	        print ('Qr Code : ', qrCode)
                        	        sys.stdout.close()
                        	        sys.stdout = sys.__stdout__
                        	        with open('login.txt', 'r') as f:
                        	            output = f.read()
                        	        line.sendMention(to,f"@! ››››\n{output}",[sender])
                        	        os.remove('login.txt')
                        	        url = host+verifierEndpoint
                        	        headers = {
                        		        'User-Agent': headers['User-Agent'],
                        		        'X-Line-Application': headers['X-Line-Application'],
                        		        'X-Line-Access': session_id,
                        		        'x-lal': 'en_id'
                        	        }
                        	        client_verif = createSecondaryQrCodeLoginPermitNoticeService(url, headers)
                        	        qrverified = client_verif.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session_id))
                        	        if certificate == "oke":
                        	            certificate = input('Input your certificate : ')
                        	        try:
                        	            certverified = cl.verifyCertificate(VerifyCertificateRequest(session.authSessionId, certificate))
                        	        except SecondaryQrCodeException as error:
                        	            sys.stdout = open('login.txt', 'w')
                        	            pincode = cl.createPinCode(CreatePinCodeRequest(session.authSessionId))
                        	            print ('Pin Code :', pincode.pinCode)
                        	            sys.stdout.close()
                        	            sys.stdout = sys.__stdout__
                        	            with open('login.txt', 'r') as f:
                        	                output = f.read()
                        	            line.sendMention(to,f"@! ››››\n{output}",[sender])
                        	            sys.stdout = open('login.txt', 'w')
                        	            pincodeverified = client_verif.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session.authSessionId))
                        	            print ('Login Java Script Done..')
                        	            sys.stdout.close()
                        	            sys.stdout = sys.__stdout__
                        	            with open('login.txt', 'r') as f:
                        	                output = f.read()
                        	            line.sendMention(to,f"@! ››››\n{output}",[sender])
                        	        except Exception:
                        	            traceback.print_exc()
                        	        sys.stdout = open('login.txt', 'w')
                        	        qrcodelogin = cl.qrCodeLogin(QrCodeLoginRequest(session.authSessionId, f'{headers["X-Line-Application"]}', True))
                        	        print (f'Qr AuthToken : {qrcodelogin.accessToken}\nCRT : {qrcodelogin.certificate}\nHeanders for login: {headers["X-Line-Application"]}')
                        	        sys.stdout.close()
                        	        sys.stdout = sys.__stdout__
                        	        with open('login.txt', 'r') as f:
                        	            output = f.read()
                        	        line.sendMessage(to, output.split(";SECONDARY")[0])
                        	        os.remove("login.txt")
                            except Exception as ee:
                                    os.remove("login.txt")
                                    line.sendMention(to,f"@! ›››› sᴏʀʀʏ {ee}",[sender])
                            

                        elif cmd.startswith(".jtk ") and sender in myOwn or sender in myBots:
                            try:
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                    for tr in targets:
                                        if tr in myOwn or tr in myBots: pass
                                        try: line.talk.kickoutFromGroup(0, msg.to, [tr])
                                        except: pass
                                        try: line.deleteOtherFromChat(to,[tr])
                                        except: pass
                            except TalkException as talk_error:
                                line.sendMessage(to, 'Failed kick members, the reason is `%s`\n' % talk_error.reason)
                                
                        elif cmd.startswith(".addfx ") and sender in myOwn:
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            try:
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for tr in targets:
                                    line.findAndAddContactsByMid(tr)
                                line.sendMessage(to, "Done add %s" % (tr))
                            except Exception as talk_error:
                                line.sendMessage(to, '`%s`' % talk_error)
                    
    except TalkException as talk_error:
        print(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('KEYBOARD INTERRUPT')
    except Exception as error:
        print(error)

def runningProgram():
    if settings['restartPoint'] is not None:
        try:
            line.sendMessage(settings['restartPoint'], 'Bot has restarted.')
        except TalkException:
            pass
        settings['restartPoint'] = None
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            print(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('KEYBOARD INTERRUPT')
        except Exception as error:
            print(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('\n##---------- BOT ALLAKADARE --------##')
    runningProgram()
