from functools import reduce
import opencc
import xml.etree.ElementTree as ET

exact_white_dict = {
    "周":"週",
}

fuzzy_white_dict = {
    "遮蔽":"封鎖",
    "程式碼":"代碼",
    "文件":"檔案",
    "蜂窩移動網":"行動數據",
    "雲盤":"雲碟",
}

tag_attr = 'traditional'

converter = opencc.OpenCC('s2twp.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get(tag_attr)
    if exists:
        element.text = exists
        element.attrib.pop(tag_attr, None)
    else:
        content = converter.convert(element.text)
        if content in exact_white_dict.keys():
            content = exact_white_dict[content]
        elif any(c in exact_white_dict.keys() for c in content.split(' ')):
            content = reduce(lambda x, y: x.replace(*y), [content, *list(exact_white_dict.items())])

        element.text = reduce(lambda x, y: x.replace(*y), [content, *list(fuzzy_white_dict.items())])

xmlTree.write('./client/zh-TW.xml', encoding='UTF-8')

converter = opencc.OpenCC('s2hk.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    exists = element.get(tag_attr)
    if exists:
        element.text = exists
        element.attrib.pop(tag_attr, None)
    else:
        content = converter.convert(element.text)
        if content in exact_white_dict.keys():
            content = exact_white_dict[content]
        elif any(c in exact_white_dict.keys() for c in content.split(' ')):
            content = reduce(lambda x, y: x.replace(*y), [content, *list(exact_white_dict.items())])
            
        element.text = reduce(lambda x, y: x.replace(*y), [content, *list(fuzzy_white_dict.items())])

xmlTree.write('./client/zh-HK.xml', encoding='UTF-8')