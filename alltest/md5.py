# -*- coding: UTF-8 -*-

import hashlib

# md5 = hashlib.md5()
# md5.update('I am fine')
# print md5.hexdigest()
sha1 = hashlib.sha1()
sha1.update('I am fine')
print sha1.hexdigest()