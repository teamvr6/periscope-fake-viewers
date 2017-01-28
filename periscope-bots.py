import requests
import re
from requests import Request, Session

print ('>>> QYST.RU ')
print ('>> Periscope Fake Viewers')

class PeriscopeBot:
    _apiUrl = 'https://api.periscope.tv/api/v2/'
    _session = ''
    _token = ''
    _broadcast_id = 0

    def __init__(self, broadcast_id):
        self._session = requests.Session()
        self._session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self._session.headers['Accept-Language'] = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
        self._broadcast_id = broadcast_id

    def start(self):
        self._token = self._getToken()
        print self._startWatching()
        pass

    def _startWatching(self):
        return self._session.get(self._getApiMethod('startPublic') + '?life_cycle_token=' + self._token + '&auto_play=false')

    def _getToken(self):
        return re.split('"', self._session.get(self._getApiMethod('accessVideoPublic') + '?broadcast_id=' + self._broadcast_id).content)[31]

    def _getApiMethod(self, method):
        return self._apiUrl + '/' + method

broadcastId = raw_input('Broadcast ID: ')
botsCount = raw_input('Number of bots: ')
while (botsCount > 0):
    pBot = PeriscopeBot(broadcastId)
    pBot.start()
    botsCount = int(botsCount) - 1
print ('Success')