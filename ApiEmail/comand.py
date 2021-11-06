# -*- coding: utf-8 -*-
from typing import Dict, Optional, Union, Any
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
from .corever.ttypes import *
from .ttypes import (
    Message,
    Location,
    ErrorCode,
    TalkException,
    ContentType,
    OpType,
    RevokeTokenRequest,
    MediaType,
    ContactSetting,
    ContactType,
    GetAllChatMidsRequest,
    GetChatsRequest,
    UpdateChatRequest,
    InviteIntoChatRequest,
    FindChatByTicketRequest,
    ReissueChatTicketRequest,
    DeleteSelfFromChatRequest,
    DeleteOtherFromChatRequest,
    CancelChatInvitationRequest,
    AcceptChatInvitationRequest,
    RejectChatInvitationRequest,
    GetInvitationTicketUrlRequest,
    AcceptChatInvitationByTicketRequest
)

from .object import Object
from random import randint
from struct import pack, unpack

from base64 import b64encode, b64decode
from hashlib import md5, sha1
from urllib.parse import quote, unquote, re
from datetime import datetime, timedelta, date
import time, random, sys, json, codecs, threading, glob, re, string, os, six, ast, urllib, urllib3, urllib.parse, traceback, atexit, html5lib, humanize, timeago, requests, base64, tempfile, shutil, io, hashlib, subprocess, platform
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'TE': 'Trailers',
}
_user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
]
def contex(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You want to call the function, you must login to LINE')
    return checkLogin

class Comand(object):
    isLogin = False
    _messageReq = {}
    _unsendMessageReq = 0

    def __init__(self):
        self.isLogin = True
        super().__init__()
        self.session = requests.Session()
         # lTfVogqLPMeGtW8KjB7CtbO9NQoIXi0vwsbTwNuMGqB  
    @contex
    def sendNotifi(self, message):
        params = {"message": message}
        data = requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": "Bearer 8Vdsnm42BuNGVbLRPbsg628WkehWzhgSX0sVB2a3Gj8"}, params=params)
        return data
    
    @contex
    def createSecondaryQrCodeLoginService(self, host, headers):
        transport = THttpClient.THttpClient(host)
        transport.setCustomHeaders(headers)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        _client = SecondaryQrCodeLoginService.Client(protocol)
        return _client

    @contex
    def createSecondaryQrCodeLoginPermitNoticeService(self, host, headers):
        transport = THttpClient.THttpClient(host)
        transport.setCustomHeaders(headers)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        _client = SecondaryQrCodeLoginPermitNoticeService.Client(protocol)
        return _client

    @contex
    def restartProgram(self):
         print ('##----- PROGRAM RESTARTED -----##')
         python = sys.executable
         os.execl(python, python, *sys.argv)
    @contex
    def parsingRes(self, res):
            result = ''
            textt = res.split('\n')
            for texts in textt:
                if True not in [texts.startswith(s) for s in ['╭', '├', '│', '╰']]:
                    result += '\n│ ' + texts
                else:
                    if texts == textt[0]:
                        result += texts
                    else:
                        result += '\n' + texts
            return result

    @contex
    def fetchOps(self, localRev, count, globalRev=0, individualRev=0):
        return self.poll.fetchOps(self, localRev, count, globalRev, individualRev)

    @contex
    def fetchOperation(self, revision, count=1):
        return self.poll.fetchOperations(revision, count)

    @contex
    def getLastOpRevision(self):
        return self.poll.getLastOpRevision()

    @contex
    def findAndAddContactsByMid(self, mid):
        return self.talk.findAndAddContactsByMid(0, mid, 0, '')

    @contex
    def findAndAddContactsByUserid(self, userid):
        return self.talk.findAndAddContactsByUserid(0, userid)

    @contex
    def findContactsByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    @contex
    def findContactByTicket(self, ticketId):
        return self.talk.findContactByUserTicket(ticketId)
        
    @contex
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self.talk.unsendMessage(self._unsendMessageReq, messageId)
        
    @contex
    def getRecentMessagesV2(self, messageBoxId, messagesCount=1001):
        return self.talk.getRecentMessagesV2(messageBoxId, messagesCount)

    @contex
    def sendSpeedProfile(self):
        get_profile_time_start = time.time()
        get_profile = self.talk.getProfile()
        get_profile_time = time.time() - get_profile_time_start
        return "%.6f" % (get_profile_time/3)
        
    @contex
    def sendSpeedMSG(self):
        get_profile_time_start = time.time()
        get_profile = self.poll.getLastOpRevision()
        get_profile_time = time.time() - get_profile_time_start
        return "%.8f" % (get_profile_time/3)

    @contex
    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return self.talk.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))

    @contex
    def cancelChatInvitation(self, chatMid, targetUserMids=[]):
        return self.talk.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))

    @contex
    def acceptChatInvitation(self, chatMid):
        return self.talk.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))

    @contex
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self.talk.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    @contex
    def deleteOtherFromChat(self, chatMid, targetUserMids=[]):
        return self.talk.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))

    @contex
    def reissueChatTicket(self, chatMid):
        return self.talk.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))

    @contex
    def findChatByTicket(self, ticketId):
        return self.talk.findChatByTicket(FindChatByTicketRequest(ticketId))

    @contex
    def getInvitationTicketUrl(self, mid):
        return self.talk.getInvitationTicketUrl(GetInvitationTicketUrlRequest(mid))

    @contex
    def getChats(self, chatMids=[], withMembers=True, withInvitees=True):
        return self.talk.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))

    @contex
    def updateChat(self, chat, updatedAttribute):
        return self.talk.updateChat(UpdateChatRequest(0,chat,updatedAttribute))

    @contex
    def createChat(self, name, targetUserMids=[]):
        return self.talk.createChat(CreateChatRequest(0,0,name,targetUserMids,""))

    @contex
    def rejectChatInvitation(self, chatMid):
        return self.talk.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))

    @contex
    def deleteSelfFromChat(self,chatMid):
        req = DeleteSelfFromChatRequest()
        req.reqSeq = 0
        req.chatMid = chatMid
        return self.talk.deleteSelfFromChat(req)

    @contex
    def getAllChatMids(self, withMemberChats=True, withInvitedChats=True):
        return self.talk.getAllChatMids(GetAllChatMidsRequest(withMemberChats,withInvitedChats), 0)

    @contex
    def requestResendMessage(self, senderMid, messageId):
        return self.talk.requestResendMessage(0, senderMid, messageId)

    @contex
    def respondResendMessage(self, receiverMid, originalMessageId, resendMessage, errorCode):
        return self.talk.respondResendMessage(0, receiverMid, originalMessageId, resendMessage, errorCode)

    @contex
    def removeMessage(self, messageId):
        return self.talk.removeMessage(0, messageId)
        
        """Post Media"""
    @contex
    def sendImage(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @contex
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)

    @contex
    def sendGIF(self, to, path):
        return self.uploadObjTalk(path=path, type='gif', returnAs='bool', to=to)

    @contex
    def sendGIFWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendGIF(to, path)

    @contex
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @contex
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)

    @contex
    def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @contex
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)

    @contex
    def sendFile(self, to, path, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId, name=file_name)

    @contex
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)
           	
    @contex
    def sendImagev2(self, to, path):
        message = self.line_thrift.Message(to=to, text=None)
        message.contentType = self.line_thrift.ContentType.IMAGE
        message.contentPreview = None
        message.contentMetadata = None
        message_id = self.sendMessage(message).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': message_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.session.post('https://obs-sg.line-apps.com/talk/m/upload.nhn', headers=deepcopy(self.Headers), data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

    @contex
    def sendImageWithURLv2(self, to, url):
        path = 'pythonLine.data' 
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download image failure.')

        try:
            self.sendImagev2(to, path)
            if os.path.exists(path):
                os.remove(path)
                return True
            else:
                return False
        except Exception as e:
            raise e
        
    """Message"""
    @contex
    def sendText(self,
                  to: str,
                  text: str,
                  content_metadata: Optional[Dict[str, str]] = None,
                  related_message_id: Optional[str] = None):
        msg = Message(
            to=to,
            text=text,
            contentMetadata=content_metadata,
        )
        if related_message_id:
            msg.relatedMessageId = related_message_id
            msg.messageRelationType = MessageRelationType.REPLY
            msg.relatedMessageServiceCode = ServiceCode.TALK

        return self.talk.sendMessage(0, msg)
        
    @contex
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @contex
    def sendMessageObject(self, msg):
        to = msg.to
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
        
    @contex
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg

    @contex
    def sendReplyMessage(self, relatedMessageId, to, text, contentMetadata={}, contentType=0):
        msg = self.generateReplyMessage(relatedMessageId)
        msg.to = to
        msg.text = text
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @contex
    def sendMention(self, to, text="", mids=[], isUnicode=False):
        arrData = ""
        arr = []
        mention = "@sakGelemku "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            if isUnicode:
                for mid in mids:
                    unicode += str(texts[mids.index(mid)].encode('unicode-escape'))
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                    elen = len(textx) + 15
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            else:
                for mid in mids:
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx)
                    elen = len(textx) + 15
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
    @contex
    def sendTextsUnicode(self,text):
    	normal = 'abcdefghijklmnopqrstuvwxyz'
    	tochange = 'ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ'
    	for i in range(len(normal)):
    		text = text.lower().replace(normal[i], tochange[i])
    	return text
    	
    @contex
    def mentionMembers(self, msgs, to,memm, nma, mids=[]):
        myMid = self.profile.mid
        if myMid in mids: mids.remove(myMid)
        parsed_len = len(mids)//20+1
        result = f'╭─「 <{memm}> 」──\n'
        mention = '@adryanaGeo\n'
        no = 0
        for point in range(parsed_len):
            mentionees = []
            for mid in mids[point*20:(point+1)*20]:
                no += 1
                result += '│• %i. %s' % (no, mention)
                slen = len(result) - 12
                elen = len(result) + 3
                mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
                if mid == mids[-1]:
                    result += '├ %s' % (nma)
                    result += '\n╰─「 <UNIVERSAL> 」──'
            if result:
                if result.endswith('\n'): result = result[:-1]
                self.sendReplyMessage(msgs,to, self.sendTextsUnicode(result), {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
            result = ''
            
    @contex    
    def changeVideoProfileBylink(self,pict, vids):
        try:
            files = {'file': open(vids, 'rb')}
            obs_params = self.genOBSParams({'oid': self.talk.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
            data = {'params': obs_params}
            r_vp = self.server.postContent('{}/talk/vp/upload.nhn'.format(str(self.server.LINE_OBS_DOMAIN)), data=data, files=files)
            if r_vp.status_code != 201:
                return "Failed update profile"
            self.updateProfilePicture(pict, 'vp')
            return "Success update profile"
        except Exception as e:
            raise Exception("Error change video and picture profile {}".format(str(e)))
    @contex
    def changeBylink(self,to, linknya):
        contact = self.talk.getProfile()
        linkgambar = 'https://obs.line-scdn.net/{}'.format(str(contact.pictureStatus))
        self.sendMessage(to, "--[ Sedang Memikirkan data ]--")
        time.sleep(0.001)
        pict = self.downloadFileURL(linkgambar)
        vids = self.downloadFileURL(linknya)
        self.changeVideoProfileBylink(pict, vids)
        self.sendMessage(to, "--[Sukses Mengubah Video Profile]--")

    @contex
    def acquireCallRoute(self, to):
        return self.call.acquireCallRoute(to)
        
    @contex
    def acquireGroupCallRoute(self, groupId, mediaType=MediaType.AUDIO):
        return self.call.acquireGroupCallRoute(groupId, mediaType)

    @contex
    def getGroupCall(self, ChatMid):
        return self.call.getGroupCall(ChatMid)
        
    @contex
    def inviteIntoGroupCall(self, chatId, contactIds=[], mediaType=MediaType.AUDIO):
        return self.call.inviteIntoGroupCall(chatId, contactIds, mediaType)
        
"""CLASS Models"""
    
class Models(Object):
    def __init__(self):
        Object.__init__(self)
        
    def log(self, text):
        print("[%s] %s" % (str(datetime.now()), text))

    """File"""

    def saveFile(self, path, raw):
        with open(path, 'wb') as f:
            shutil.copyfileobj(raw, f)

    def deleteFile(self, path):
        if os.path.exists(path):
            os.remove(path)
            return True
        else:
            return False

    def downloadFileURL(self, fileUrl, returnAs='path', saveAs='', headers=None):
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        if saveAs == '':
            saveAs = self.genTempFile()
        r = self.server.getContent(fileUrl, headers=headers)
        if r.status_code != 404:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download file failure.')

    """Generator"""

    def validateURL(self, url, returnAs='bool'):
        if returnAs not in ['bool', 're']:
            raise Exception('Invalid returnAs value')
        result = re.match(self.server.URL_REGEX, url)
        if returnAs == 'bool':
            if result:
                return True
            else:
                return False
        return result

    def findMids(self, text):
        return self.server.MID_REGEX.findall(text)

    def findGids(self, text):
        return self.server.GID_REGEX.findall(text)

    def findRids(self, text):
        return self.server.RID_REGEX.findall(text)

    def findAllIds(self, text):
        return self.server.ALLIDS_REGEX.findall(text)

    def genTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'usa-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return os.path.join(fPath, fName)
        except:
            raise Exception('tempfile is required')

    def genOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.genTempFile('file'),'ver': '1.0'}
        if returnAs not in ['json','b64','default']:
            raise Exception('Invalid parameter returnAs')
        if 'name' in newList and not newList['name']:
            newList['name'] = oldList['name']
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList=json.dumps(oldList)
            return oldList
        elif returnAs == 'b64':
            oldList=json.dumps(oldList)
            return base64.b64encode(oldList.encode('utf-8'))
        elif returnAs == 'default':
            return oldList
            
    def uploadHome(self, path, type='image', objId=None):
        if type not in ['image','video','audio']:
            raise Exception('Invalid type value')
        if type == 'image':
            contentType = 'image/jpeg'
        elif type == 'video':
            contentType = 'video/mp4'
        elif type == 'audio':
            contentType = 'audio/mp3'
        if not objId:
            hstr = 'usa-bot_%s' % int(time.time()*1000)
            objid = hashlib.md5(hstr.encode()).hexdigest()
        file = open(path, 'rb').read()
        params = {
            'name': '%s' % str(time.time()*1000),
            'userid': '%s' % self.profile.mid,
            'oid': '%s' % str(objId),
            'type': type,
            'ver': '1.0' #2.0 :p
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': contentType,
            'Content-Length': str(len(file)),
            'x-obs-params': self.genOBSParams(params,'b64') #base64 encode
        })
        r = self.server.postContent('https://obs-tw.line-apps.com/myhome/c/upload.nhn', headers=hr, data=file)

        if r.status_code != 201:
            raise Exception(f"Upload object home failure. Receive statue code: {r.status_code}")
        return objId
        
    def uploadOcbjTalk(self, path=None, type='image', objId=None, to=None):
        if type not in ['image','gif','video','audio','file']:
            raise Exception('Invalid type value')
        headers=None
        files = {'file': open(path, 'rb')}
        #url = 'https://obs.line-apps.com/talk/m/upload.nhn' #if reqseq not working
        url = 'https://obs.line-apps.com/r/talk/m/reqseq'
        params = {
            "type": "image",
            "ver": "2.0",
            "name": files['file'].name,
            "oid": "reqseq",
            "reqseq": str(self.revision),
            "cat": "original"
        }
        if objId != None:
            params['oid'] = objId
        if to != None:
            params['tomid'] = to
        if type != 'gif':
            params['type'] = type
            data = {'params': self.genOBSParams(params)}
        elif type == 'gif':
            params = {
                'type': 'image',
                'ver': '2.0',
                'name': files['file'].name,
                'oid': 'reqseq',
                'reqseq': '%s' % str(self.revision),
                'tomid': '%s' % str(to),
                'cat': 'original'
            }
            files = None
            data = open(path, 'rb').read()
            headers = self.server.additionalHeaders(self.Headers, {
                'content-type': 'image/gif',
                'Content-Length': str(len(data)),
                'x-obs-params': self.genOBSParams(params,'b64'), #base64 encode
                'X-Line-Access': self.obs_token
            })
        r = self.postContent(url, data=data, headers=headers, files=files)
        if r.status_code != 201:
            console.log("uploadObjTalk: ", r.text)
            raise Exception('Upload %s failure.' % type)
        else:
            if objId is None:
                objId = r.headers['x-obs-oid']
            objHash = r.headers['x-obs-hash']
        return objId

#======[COMAND LINE TEXT]========#
class comandText:
    def __init__(self, cl):
        self.cl = cl
    def CmdText(self, _from, to, sender, text, msg_, settings, myOwn, myAdm, programStart, contentMetadata={}, contentType=0):
        if text == 'ping':
            if sender in myOwn or sender in myAdm:
                self.cl.sendReplyMessage(_from, to, 'pong..!')
             
        elif text =="!status":
            if sender in myOwn or sender in myAdm:
                ac = subprocess.getoutput('lsb_release -a')
                core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
                am = subprocess.getoutput('cat /proc/meminfo')
                python_imp = platform.python_implementation()
                python_ver = platform.python_version()
              #  botlot = "Aktif " + time.time() - programStart
                for B in am.splitlines():
                    if 'MemTotal:' in B:
                        mem = B.split('MemTotal:')[1].replace(' ','')
                    if 'MemFree:' in B:
                        fr = B.split('MemFree:')[1].replace(' ','')
                for B in ac.splitlines():
                    if 'Description:' in B:
                        ossys = B.split('Description:')[1].replace('  ','')
                    else:
                        ossys = "Cpython"
                    md ="╭─「 <INFO SCRIPT> 」──"
                    md +="\n• CPU Core: {}".format(core)
                    md +="\n• OS System: {} Softext".format(ossys)
                    md +="\n• Versions: {}".format(python_ver)
                    md +="\n• Langune: {}".format(python_imp)
                    md +="\n• Memory: {}".format(mem)
                    md +="\n• Free: {}".format(fr)
                  #  md +="\n• {}".format(botlot)
                md +="\n╰─「 <UNIVERSAL> 」──"
                self.cl.sendMessage(to,self.cl.parsingRes(self.cl.sendTextsUnicode(md)))
                        
        elif text == '!leave me':
            if sender in myOwn or sender in myAdm:
                self.cl.talk.leaveGroup(0, to)
        elif text == '!sp':
            if sender in myOwn or sender in myAdm:
                get_profile_time_start = time.time()
                get_profile = self.cl.talk.getProfile()
                get_profile_time = time.time() - get_profile_time_start
                self.cl.sendReplyMessage(_from,to,self.cl.sendTextsUnicode(f'─「 {int(get_profile_time*20000)} ms」─'))
                #self.cl.sendReplyMessage(_from, to,"%.3f" % len(get_profile_time/3))
        elif text == '!speed':
            if sender in myOwn or sender in myAdm:
                data = self.cl.sendSpeedMSG()
                profile = self.cl.sendSpeedProfile()
                self.cl.sendReplyMessage(_from, to, f"Send Message :: {data}\nGet Profile :: {profile}")
            
        elif text.lower().startswith('!pict '):
            if sender in myOwn or sender in myAdm:
                target = eval(msg_.contentMetadata["MENTION"])
                targets = []
                no = 0
                data = "╭───────────"
                for xx in target["MENTIONEES"]:
                    targets.append(xx["M"])
                for midd in targets:
                    no +=1
                    tag = self.cl.talk.getContact(midd).pictureStatus
                    pict = f"https://obs.line-scdn.net/{tag}"
                    data += f"\n│• {no}. https://obs.line-scdn.net/{tag}"
                data +="\n├─────────"
                data +="\n│  「 <ᴜɴɪᴠᴇʀꜱᴀʟ> 」"
                data +="\n╰───────────"
                self.cl.sendReplyMessage(_from, to, data)
                
        elif text.startswith('!mid '):
            if sender in myOwn or sender in myAdm:
                target = eval(msg_.contentMetadata["MENTION"])
                targets = []
                no = 0
                data = "╭───────────"
                for xx in target["MENTIONEES"]:
                    targets.append(xx["M"])
                for midd in targets:
                    no += 1
                    tag = self.cl.talk.getContact(midd).displayName[0:20]
                    data += f"\n│• {no}. {tag} ( {midd} )"
                data +="\n├─────────"
                data +="\n│  「 <ᴜɴɪᴠᴇʀꜱᴀʟ> 」"
                data +="\n╰───────────"
                self.cl.sendReplyMessage(_from, to, data)
            
        elif text.startswith('!kick '):
            if sender in myOwn or sender in myAdm:
                target = eval(msg_.contentMetadata["MENTION"])
                targets = []
                for xx in target["MENTIONEES"]:
                    targets.append(xx["M"])
                for midd in targets:
                    self.cl.talk.kickoutFromGroup(0, to, [midd])
                    
        elif text.startswith('!invite '):
            if sender in myOwn or sender in myAdm:
                target = eval(msg_.contentMetadata["MENTION"])
                targets = []
                for xx in target["MENTIONEES"]:
                    targets.append(xx["M"])
                for midd in targets:
                    self.cl.inviteIntoChat(to, [midd])
        elif text.lower() == "!me":
            if sender in myOwn or sender in myAdm:
                seender = self.cl.talk.getContact(sender).mid
                contentMetadata = {'mid': seender}
                contentType = msg_.contentType=13
                self.cl.sendReplyMessage(_from, to, '', contentMetadata, contentType)
                
        elif text.lower() =="!tagall":
            if sender in myOwn or sender in myAdm:
                   chat = self.cl.getChats([to]).chats[0]
                   print (list(chat.extra.groupExtra.memberMids))
                   Member = list(chat.extra.groupExtra.memberMids)
                   members = []
                   members = [mem for mem in Member]
                   tag = "Mentions Members"
                   name = "group name: \n│• " + self.cl.talk.getGroup(to).name[0:10]
                   if members:
                       self.cl.mentionMembers(_from, to, tag, name, members)
                   else:
                       self.cl.sendMessage(to, "Noting Member")
                       
        elif text.lower() == "help":
            if sender in myOwn or sender in myAdm:
                data ="╭────────────"
                data +="\n├─「 <ᴄᴍᴅ & ᴍᴇɴᴜ> 」─"
                data +="\n│• !me"
                data +="\n│• !listbl "
                data +="\n│• !sp // speed // .sp"
                data +="\n│• !kick <@>"
                data +="\n│• !pict <@>"
                data +="\n│• !mid <@>"
                data +="\n│• ping"
                data +="\n│• ᴀʙᴏᴜᴛ"
                data +="\n├─「 <ᴛʏᴘᴇ ꜱᴇʟꜰʙᴏᴛ> 」─"
                data +=f"\n│• ɴᴀᴍᴇ : {self.cl.profile.displayName[0:20]}"
                data +="\n├───────────"
                data +="\n│  「 <ᴜɴɪᴠᴇʀꜱᴀʟ> 」"
                data +="\n╰────────────"
                self.cl.sendReplyMessage(_from, to, self.cl.parsingRes(self.cl.sendTextsUnicode(data)))
                
        elif text.lower().startswith('!post '):
            if sender in myOwn or sender in myAdm:
                separator = text.split(' ')
                n1 = text.replace(separator[0]+' ','')
                texttl = n1.lower()
                if texttl == 'on':
                    if to not in settings['checkPost']:
                        self.cl.sendMessage(to, self.cl.sendTextsUnicode('Checkpost already active'))
                        settings['checkPost'].append(to)
                    else:
                        self.cl.sendMessage(to,self.cl.sendTextsUnicode('Success activated checkpost'))
                elif texttl == 'off':
                    if to in settings['checkPost']:
                        self.cl.sendMessage(to, 'Checkpost already deactive')
                        settings['checkPost'].remove(to)
                    else:
                        self.cl.sendMessage(to,self.cl.sendTextsUnicode('Success deactivated checkpost'))
        elif text.startswith('!autoread '):
            if sender in myOwn or sender in myAdm:
                separator = text.split(' ')
                n1 = text.replace(separator[0]+' ','')
                texttl = n1.lower()
                if texttl == 'on':
                    if settings['autoRead']:
                        self.cl.sendMessage(to, 'Autoread already active.')
                    else:
                        settings['autoRead'] = True
                        self.cl.sendMessage(to, 'Success activated autoread.')
                elif texttl == 'off':
                      if not settings['autoRead']:
                          self.cl.sendMessage(to, 'Autoread already deactive.')
                      else:
                          settings['autoRead'] = False
                          self.cl.sendMessage(to, 'Success deactivated autoread.')
                          
        elif text.startswith('!ts '):
            if sender in myOwn or sender in myAdm:
                separator = text.split(' ')
                n1 = text.replace(separator[0]+' ','')
                self.cl.sendNotifi("\n=•>  "+n1)
#============ [[ NEDIA LIEFTELE ]]==========
                
                
                
                
                
