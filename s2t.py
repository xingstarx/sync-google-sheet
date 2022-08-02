from functools import reduce
import opencc
import xml.etree.ElementTree as ET

white_dict = {
    "周":"週",
    "遮蔽":"封鎖",
    "程式碼":"代碼",
    "通用":"一般",
    "文件":"檔案",
    "蜂窩移動網":"行動數據",
    "雲盤":"雲碟",
}

converter = opencc.OpenCC('s2twp.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get('zh-TW')
    if exists:
        element.text = exists
    else:
        content = converter.convert(element.text)
        element.text = reduce(lambda x, y: x.replace(*y), [content, *list(white_dict.items())])

xmlTree.write('./client/zh-TW.xml', encoding='UTF-8')

converter = opencc.OpenCC('s2hk.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get('zh-HK')
    if exists:
        element.text = exists
    else:
        content = converter.convert(element.text)
        element.text = reduce(lambda x, y: x.replace(*y), [content, *list(white_dict.items())])

xmlTree.write('./client/zh-HK.xml', encoding='UTF-8')