import base64
import json
from Crypto.Cipher import AES
import requests


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))

        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


def get_session_key(code, appid, secret):
    # appid = "wxa100b18ea46591d8"
    # secret = "7dcd8ba894530a580cd8c58ae3ad24e8"
    js_code = code
    grant_type = "authorization_code"
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={js_code}&grant_type={grant_type}".format(
        appid=appid, secret=secret, js_code=js_code, grant_type=grant_type
    )

    response = requests.get(url=url)
    print(response.text)
    # {"errcode":40163,"errmsg":"code been used, rid: 61550d62-4ee11ca4-5b8e2d80"}
    # {"session_key":"gvTFdoQbA\/WG1KzzPjvdrQ==","openid":"o1q_I59HubcWpqHcyzKKrSoUB1jU"}
    return json.loads(response.text)
