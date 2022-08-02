from functools import reduce
import opencc
import xml.etree.ElementTree as ET

white_dict = {
    "周":"週",
    "屏蔽":"封鎖",
    "代码":"代碼",
    "通用":"一般",
    "文件":"檔案",
    "蜂窝移动网":"行動數據",
}

converter = opencc.OpenCC('s2twp.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get('zh-TW')
    if exists:
        content = exists
    else:
        content = reduce(lambda x, y: x.replace(*y), [element.text, *list(white_dict.items())])
    element.text = converter.convert(content)

xmlTree.write('./client/zh-TW.xml', encoding='UTF-8')

converter = opencc.OpenCC('s2hk.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get('zh-HK')
    if exists:
        content = exists
    else:
        content = reduce(lambda x, y: x.replace(*y), [element.text, *list(white_dict.items())])
    element.text = converter.convert(content)

xmlTree.write('./client/zh-HK.xml', encoding='UTF-8')