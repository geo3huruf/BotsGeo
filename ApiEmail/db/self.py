# -*- coding: utf-8 -*-
from ApiEmail.client import LINE
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
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
import traceback, time
import youtube_dl
import time, random, sys, json, codecs, re, os, shutil, requests, ast, pytz, atexit, traceback, base64, pafy, livejson, timeago, math, argparse, urllib, urllib.parse, subprocess, asyncio,humanize,threading,string
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
#==============================================
programStart = time.time()
#=================[ RUN BOTS COMPACK ]===================
certificate=""

deskwin = 'DESKTOPWIN\t6.7.0.2482\tDESKTOP-ALFINONH\t10.0.0-NT-x64'
ios = "IOS\t10.0.0\tiPhone OS\t12.1.4"
adroid = 'LLA/2.17.0 Redmi 8A Pro 9'
adroidlite = 'ANDROIDLITE\t2.17.0\tAndroid OS\t9'
TYPE = ["DESKTOPMAC\t6.7.2\tMAC\t10","DESKTOPMAC\t6.7.0\tMAC\t10","DESKTOPMAC\t6.6.0\tMAC\t10"]
chrom = "CHROMEOS\t2.3.8\tChrome\tOS\t83.0.4103.97"
Token = livejson.File('db/token.json', True, False, 4)

try: line = LINE(Token["token"],appName=chrom)
except:
    line = LINE("azasantoso057@gmail.com","Braja321",appName=chrom)
    Token["token"] = line.authToken
#Token["access"] = {line.profile.mid:{"email":"azasantoso057@gmail.com","paswd": "Braja321", "certificate": line.certificate}}
"""try: line1 = LINE(Token["token1"], appName=chrom)
except:
    line1 = LINE("denmasgeo34@gmail.com","Geo1123",appName=chrom)
    Token["token1"] = line1.authToken
#Token["access1"] = {line1.profile.mid:{"email":"denmasgeo34@gmail.com","paswd": "Geo1123", "certificate": line1.certificate}}
try: line2 = LINE(Token["token2"],appName="DESKTOPMAC\t6.7.2\tMAC\t10")
except:
    line2 = LINE("fixadri@gmail.com","Denmas321",appName=chrom)
    Token["token2"] = line2.authToken
#Token["access2"] = {line2.profile.mid: {"email":"fixadri@gmail.com","paswd": "Denmas321", "certificate": line2.certificate}}
try: line3 = LINE(Token["token3"],appName=chrom)
except:
    line3 = LINE("mungkint776@gmail.com","Braja321",appName=chrom)
    Token["token3"] = line3.authToken
#Token["access3"] = {line2.profile.mid:{"email":"mungkint776@gmail.com","paswd": "Braja321", "certificate": line3.certificate}}
"""
if line:
    print ('++ AuthToken : %s' % line.authToken)
    print ('++ ProfileMid : %s' % line.profile.mid)
   # print ('++ AuthToken : %s' % line1.authToken)
  #  print ('++ ProfileMid : %s' % line1.profile.mid)
  #  print ('++ AuthToken : %s' % line2.authToken)
 #   print ('++ ProfileMid : %s' % line2.profile.mid)
 #   print ('++ AuthToken : %s' % line3.authToken)
 #   print ('++ ProfileMid : %s' % line3.profile.mid)
else:
    sys.exit('##----- LOGIN CLIENT (Failed) -----##')
print ('##----- LOGIN CLIENT (Success) -----##')

myMid = line.profile.mid
#myMid1 = line1.profile.mid
#myMid2 = line2.profile.mid
#myMid3 = line3.profile.mid
myOwn = ['uce6d9daa08bce025bd880d7f9fea1746']
oepoll = OEPoll(line)
settings = livejson.File('db/setbot.json', True, False, 4)
Bots = livejson.File('db/bots.json', True, False, 4)
myBots = [myMid]
#memBots = [myMid2, myMid3]

usa = comandText(line)
bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}
profile = line.talk.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
settings['myProfile']['videoProfile'] = profile.videoProfile
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId

def sendNotifi(message):
    params = {"message": message}
    data = requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": "Bearer lTfVogqLPMeGtW8KjB7CtbO9NQoIXi0vwsbTwNuMGqB"}, params=params)
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
                        
        if op.type == 124:
            if(op.param3 in settings["blacklist"]["target"]):
                # if(op.param2 not in myOwn or op.param2 not in myBots):
                missu = op.param3.replace('\x1e',',').split(',')
                for absi in missu:
                    if absi not in myOwn and absi not in myBots:
                        settings["blacklist"]["target"][absi] = True
                        try:
                            USA = random.choice(myBots)
                            chat = USA.getChats([op.param1]).chats[0]
                            for target in settings["blacklist"]["target"]:
                                if target in list(chat.extra.groupExtra.memberMids) or target in list(chat.extra.groupExtra.inviteeMids):
                                    USA.deleteOtherFromChat(op.param1,[target])
                                    USA.cancelChatInvitation(op.param1,[target])
                                else:pass
                        except:
                            try:
                                bots = random.choice(myBots)
                                chat = bots.getChats([op.param1]).chats[0]
                                bots.talk.cancelGroupInvitation(0, op.param1,[op.param3])
                            except: pass
                            try:
                                chat = line2.getChats([op.param1]).chats[0]
                                for target in settings["blacklist"]["target"]:
                                    if target in list(chat.extra.groupExtra.memberMids) or target in list(chat.extra.groupExtra.inviteeMids):
                                        line2.deleteOtherFromChat(op.param1,[target])
                                        line2.cancelChatInvitation(op.param1,[target])
                                    else:pass
                            except: pass
                            try: line3.talk.cancelGroupInvitation(0, op.param1,[op.param3])
                            except: pass
            else: pass
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.talk.acceptGroupInvitation(0, op.param1)
                print ("invitan Joined")
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMention(op.param1, settings['autoJoin']['message'], [op.param2])
            if settings['autoLeave']['status'] and myMid in op.param3:
                line.talk.acceptGroupInvitation(op.param1)
                if settings['autoLeave']['reply']:
                    if '@!' not in settings['autoLeave']['message']:
                        line.sendMessage(op.param1, settings['autoLeave']['message'])
                    else:
                        line.sendMention(op.param1, settings['autoLeave']['message'], [op.param2])
                line.talk.leaveGroup(0, op.param1)
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
                                            line2.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                    else: pass
                                except: pass
                                try:
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            line3.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                    else: pass
                                except: pass
                                try:
                                    data = random.choice([line2, line3, line1])
                                    if jmlh <= 10:
                                        for x in range(jmlh):
                                            data.deleteOtherFromChat(op.param1, [op.param2])
                                    else: pass
                                except: pass
                            except TalkException as talk_error:
                                TalkException.code(109)
                    else: pass
                    
        if op.type == 18 or op.type == 132:
                if(op.param3 in myMid):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                else: pass
                        
        if op.type == 19 or op.type == 133:
                if(op.param3 in myMid):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = random.choice([line2, line3, line1])
                             JSSI = {}
                             chat = line1.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else: JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                     data.inviteIntoChat(op.param1, JSSI)
                                     line.talk.acceptGroupInvitation(0, op.param1)
                                 else: pass
                        except:
                             try:
                                 cl = line1
                                 JSSI = {}
                                 chat = cl.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in cl.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         cl.deleteOtherFromChat(op.param1,[op.param2])
                                         cl.inviteIntoChat(op.param1, JSSI)
                                         line.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line2
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line3
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                if(op.param3 in myMid1):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = random.choice([line2, line3])
                             JSSI = {}
                             chat = data.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else: JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                     data.inviteIntoChat(op.param1, JSSI)
                                     line1.talk.acceptGroupInvitation(0, op.param1)
                                 else: pass
                        except:
                             try:
                                 cl = line2
                                 JSSI = {}
                                 chat = cl.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in cl.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         cl.deleteOtherFromChat(op.param1,[op.param2])
                                         cl.inviteIntoChat(op.param1, JSSI)
                                         line1.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line3
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line1.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                if(op.param3 in myMid2):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = random.choice([line3, line1])
                             JSSI = {}
                             chat = data.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else: JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                     data.inviteIntoChat(op.param1, JSSI)
                                     line2.talk.acceptGroupInvitation(0, op.param1)
                                 else: pass
                        except:
                             try:
                                 cl = line1
                                 JSSI = {}
                                 chat = cl.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in cl.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         cl.deleteOtherFromChat(op.param1,[op.param2])
                                         cl.inviteIntoChat(op.param1, JSSI)
                                         line2.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line2
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line1.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                if(op.param3 in myMid2):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = random.choice([line3, line1])
                             JSSI = {}
                             chat = data.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else: JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                     data.inviteIntoChat(op.param1, JSSI)
                                     line2.talk.acceptGroupInvitation(0, op.param1)
                                 else: pass
                        except:
                             try:
                                 cl = line3
                                 JSSI = {}
                                 chat = cl.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in cl.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         cl.deleteOtherFromChat(op.param1,[op.param2])
                                         cl.inviteIntoChat(op.param1, JSSI)
                                         line2.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line1
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line2.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                if(op.param3 in myMid3):
                    if(op.param2 not in myOwn or op.param2 not in myBots):
                        settings["blacklist"]["target"][op.param2] = True
                        try:
                             data = random.choice([line2, line1])
                             JSSI = {}
                             chat = data.getChats([op.param1]).chats[0]
                             for targets in myBots:
                                 if targets not in data.talk.getProfile().mid:
                                     if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                         JSSI[targets] = True
                                     else: JSSI[targets] = True
                                     data.deleteOtherFromChat(op.param1,[op.param2])
                                     data.inviteIntoChat(op.param1, JSSI)
                                     line3.talk.acceptGroupInvitation(0, op.param1)
                                 else: pass
                        except:
                             try:
                                 cl = line2
                                 JSSI = {}
                                 chat = cl.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in cl.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         cl.deleteOtherFromChat(op.param1,[op.param2])
                                         cl.inviteIntoChat(op.param1, JSSI)
                                         line3.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
                             except: pass
                             try:
                                 client = line1
                                 JSSI = {}
                                 chat = client.getChats([op.param1]).chats[0]
                                 for targets in myBots:
                                     if targets not in client.talk.getProfile().mid:
                                         if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                             JSSI[targets] = True
                                         else: JSSI[targets] = True
                                         client.deleteOtherFromChat(op.param1,[op.param2])
                                         client.inviteIntoChat(op.param1, JSSI)
                                         line3.talk.acceptGroupInvitation(0, op.param1)
                                     else:pass
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
                                            line3.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                            line2.talk.inviteIntoGroup(0, op.param1, [op.param3][:1])
                                        except:pass
                                else: pass
                            except: pass
                            try:
                                if jmlh <= 10:
                                    for x in range(jmlh):
                                        try:
                                            line1.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                            line3.talk.inviteIntoGroup(0, op.param1, [op.param3][:1])
                                        except:pass
                                else: pass
                            except: pass
                            try:
                                if jmlh <= 10:
                                    for x in range(jmlh):
                                        try:
                                            line2.talk.kickoutFromGroup(0, op.param1, [op.param2])
                                            line1.talk.inviteIntoGroup(0, op.param1, [op.param3][:1])
                                        except:pass
                                else: pass
                            except: pass
                        except TalkException as talk_error:
                            TalkException.code(109)
                            pass
                        return
                    else: pass
                    
        if op.type == 11 or op.type == 122:
            if op.param3 =="1":
                target = line.talk.getContact(op.param2).displayName
                line.sendMessage(op.param1, f"\njiah update Name group\nSender: {target}","text")
            if op.param3 =="2":
                target = line.talk.getContact(op.param2).displayName
                line.sendMessage(op.param1, f"\n jiah update foto group\nSender: {target}","text")
                img = f"https://obs-sg.line-apps.com/r/talk/g/{op.param1}/preview"
                line.sendMessage(op.param1, f"\n{img}")
            if op.param3 =="4":
                target = line.talk.getContact(op.param2).displayName
                line.sendMessage(op.param1, f"\njiah update QR group\nSender: {target}","text")
            print (op)
 
        if op.type == 7:
                print (op)
        if op.type == 32:
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
                        cmd = command(text)
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
                                        myBots
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
                    if txt == '!restart' and sender in myOwn:
                        settings['restartPoint'] = to
                        line.restartProgram()
                    elif txt == ".sp" and sender in myOwn:
                        mess = line.sendSpeedMSG()
                        profile = line.sendSpeedProfile()
                        line.sendMessage(to, f"Speed getMessage :: {mess}\nSpeed getProfile :: {profile}")
                        mess = line1.sendSpeedMSG()
                        profile = line1.sendSpeedProfile()
                        line1.sendMessage(to, f"Speed getMessage :: {mess}\nSpeed getProfile :: {profile}")
                        mess = line2.sendSpeedMSG()
                        profile = line2.sendSpeedProfile()
                        line2.sendMessage(to, f"Speed getMessage :: {mess}\nSpeed getProfile :: {profile}")
                        mess = line3.sendSpeedMSG()
                        profile = line3.sendSpeedProfile()
                        line3.sendMessage(to, f"Speed getMessage :: {mess}\nSpeed getProfile :: {profile}")
                        
                    elif txt == ".inv" and sender in myOwn:
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
                                    line.talk.inviteIntoGroup(0, to, memBots)
                                    line1.talk.acceptGroupInvitation(0,to)
                                    line2.talk.acceptGroupInvitation(0, to)
                                    line3.talk.acceptGroupInvitation(0, to)
                                else:pass
                        except TalkException as talk_error:
                            print(talk_error)
                            pass
                    elif txt == ".cnl" and sender in myOwn:
                        try:
                            line.talk.cancelGroupInvitation(0, to, [line1,line2,line3])
                        except TalkException as talk_error:
                            print(talk_error)
                    elif txt == ".cban" and sender in myOwn:
                        settings["blacklist"]["target"] = {}
                        line.sendMessage(to,"Done Reset Blacklist %s" % len(settings["blacklist"]["target"]))
                    
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
