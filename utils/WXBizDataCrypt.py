import base64
import json
from Crypto.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        try:
            sessionKey = base64.b64decode(self.sessionKey)
            encryptedData1 = base64.b64decode(encryptedData)
            iv = base64.b64decode(iv)

            cipher = AES.new(sessionKey, AES.MODE_CBC, iv)

            source = cipher.decrypt(encryptedData1)

            decrypted = json.loads(self._unpad(source.decode('utf-8', 'ignore')), strict=False)

            if decrypted['watermark']['appid'] != self.appId:
                raise Exception('Invalid Buffer')

            return decrypted

        except BaseException as err:
            print(err)
            return False

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]