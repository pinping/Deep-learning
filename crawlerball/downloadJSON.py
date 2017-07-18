import os
import re
import json
import urllib.request
import urllib








def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<![CDATA[[^>]*//]]>', re.I)  # 匹配CDATA
    re_script = re.compile('<s*script[^>]*>[^<]*<s*/s*scripts*>', re.I)  # Script
    re_style = re.compile('<s*style[^>]*>[^<]*<s*/s*styles*>', re.I)  # style
    re_br = re.compile('<brs*?/?>')  # 处理换行
    re_h = re.compile('</?w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    re_a = re.compile('<a .*?>(.*?)</a>')  # HTML标签
    re_p = re.compile('<p .*?>(.*?)</p>')  # HTML标签
    re_head = re.compile('<head>(.*?)</head>')  # HTML标签
    re_c = re.compile(',')  # HTML标签
    re_st = re.compile('<strong>')  # HTML标签
    re_str = re.compile('</strong>')  # HTML标签
    re_stro = re.compile('<strong .*?>')  # HTML标签
    re_rn = re.compile('\r\n')  # HTML标签


    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_a.sub('', s)
    s = re_p.sub('', s)
    s = re_c.sub('', s)
    s = re_st.sub('', s)
    s = re_str.sub('', s)
    s = re_stro.sub('', s)
    s = re_head.sub('', s)
    s = re_comment.sub('', s)  # 去掉HTML注释
    s = re_rn.sub('', s)
    # 去掉多余的空行
    blank_line = re.compile('n+')
    s = blank_line.sub('n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s


def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def htmlDispose(data):

    res_title = ''
    res_tr = r'<tr .*?>(.*?)</tr>'
    m_tr = re.findall(res_tr, data, re.S | re.M)
    for line in m_tr:
        # print ('line'+line)
        # 获取表格第一列th 属性
        res_th = r'<th .*?>(.*?)</th>'
        m_th = re.findall(res_th, line, re.S | re.M)
        for mm in m_th:
            if res_title == '':
                res_title = mm
            else:
                res_title = res_title + ',' + mm

    res_array = []
    res_tr = r'<tr>(.*?)</tr>'
    m_tr = re.findall(res_tr, data, re.S | re.M)
    for line in m_tr:
        # print ('line'+line)
        # 获取表格第一列th 属性

        res_data = []
        res_th = r'<td .*?>(.*?)</td>'
        m_th = re.findall(res_th, line, re.S | re.M)
        for mm in m_th:
            if len(ballDispose(mm.replace(' ', ''))) > 0:
                res_data.append(ballDispose(mm))
            else:
                res_data.append(mm.replace(' ', ''))

        res_th = r'<td>(.*?)</td>'
        m_th = re.findall(res_th, line, re.S | re.M)
        for mm in m_th:
            res_data.append(mm.replace(' ', ''))

        res_array.append(res_data)

    res_array.pop(0)
    return res_array


def ballDispose(data):

    res_data = []
    # 获取蓝色球的号码
    res_td = r'<em .*?>(.*?)</em>'
    m_td = re.findall(res_td, data, re.S | re.M)
    for nn in m_td:
        res_data.append(nn)

    # 获取蓝色球的号码
    res_td = r'<em>(.*?)</em>'
    m_td = re.findall(res_td, data, re.S | re.M)
    for nn in m_td:
        res_data.append(nn)

    return res_data



baseUrl = "http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum="
count = 0
saveData = []
new_list = []

if __name__=='__main__':
    while (count < 106):
        count = count + 1
        url = baseUrl+str(count)
        data = urllib.request.urlopen(url).read()
        data = data.decode('UTF-8')
        saveData = saveData + htmlDispose(filter_tags(data))

    for m in saveData:
        if len(m) > 1:
            new_list.append(m)

    saveStr = json.dumps(new_list)
    print('saveStr', saveStr)
    with open('data.json', 'w') as f:
        json.dump(saveStr, f)



# url = "http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=1"
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)