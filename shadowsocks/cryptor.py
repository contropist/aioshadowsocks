'''
不同加密方式的分发
'''
from shadowsocks.crypto.aes import AESCipher
from shadowsocks.crypto.none import NONECipher


class Cryptor:

    # 注册所有加密方式
    SUPPORT_METHODS = {}

    def __init__(self, method, password, flag):
        self._crypto = None
        self._register_chipher()

        # 找到指定的cipher
        for name, methods in self.SUPPORT_METHODS.items():
            if method in methods:
                if name == 'aes':
                    self._crypto = AESCipher(method, password, flag)
                elif name == 'none':
                    self._crypto = NONECipher(method, password, flag)

        if self._crypto is None:
            raise NotImplementedError

    def _register_chipher(self):
        '''注册所有的chiper'''

        # aes
        self.SUPPORT_METHODS['aes'] = AESCipher.SUPPORT_METHODS
        # none
        self.SUPPORT_METHODS['none'] = NONECipher.SUPPORT_METHODS

    def encrypt(self, data):
        return self._crypto.encrypt(data)

    def decrypt(self, data):
        try:
            return self._crypto.decrypt(data)
        except Exception as e:
            raise RuntimeError(e)
