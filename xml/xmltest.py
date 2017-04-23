# -*- coding: UTF-8 -*-
import xml.dom.minidom

dom = xml.dom.minidom.parse('xml.xml')
root = dom.documentElement
# print root.nodeName
# print root.nodeValue
# print root.nodeType
# print root.ELEMENT_NODE

# bb = root.getElementsByTagName('maxid')
# b = bb[0]
# print b.nodeName
#
# bb = root.getElementsByTagName('login')
# b = bb[0]
# print b.nodeName

