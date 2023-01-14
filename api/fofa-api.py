import requests
import base64
import json
import os,time


def print_b(str):
    print('\033[1;36m %s \033[0m'%(str))

def print_g(str):
    print('\033[1;32m %s \033[0m'%(str))

def print_r(str):
    print('\033[1;31m %s \033[0m'%(str))

def main(ini):
    try:
        args_list = eval(input('[api@fofa ~]# '))
        if args_list['rule']:
            args_list['rule'] = base64.b64encode(args_list['rule'].encode('utf-8')).decode("utf-8")
            get_json(ini,args_list)
        else:
            print_r('>rule 为必需参数.')
        main(ini)
    except:
        print_r('>请检查输入参数.')
        main(ini)


def get_json(ini,args_list):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    url = 'https://fofa.info/api/v1/search/all?email=%s&key=%s&qbase64=%s'%(ini['email'],ini['key'],args_list['rule'])
    if args_list['page']:
        url += '&page=%s'%(args_list['page'])
    if args_list['size']:
        url += '&size=%s'%(args_list['size'])
    if args_list['fields']:
        url += '&fields=%s'%(args_list['fields'])
    if args_list['is_full']:
        url += '&full=%s'%(args_list['is_full'])
    try:
        data = requests.get(url=url,headers=headers,timeout=60)
        data_dic = json.loads(data.text)
        if 'errmsg' in data_dic:
            print_r('>'+data_dic['errmsg'])
        else:
            data_list = []
            for i in data_dic['results']:
                data_list.append(str(i))
            data = '\n'.join(data_list)
            save=open('ouput.txt','wb+')
            save.write(data.encode('gbk','ignore'))
            print_g(">已导出'ouput.txt'..一共%s条数据.."%(len(data_dic['results'])))
            save.close()
    except:
        ('>获取数据错误.')

if __name__ == '__main__':
    os.system("")#玄学彩色字体
    print('''
    \033[1;36m   ______ ____  ______                 _____ _____
     |  ____/ __ \|  ____/\         /\   |  __ \_   _|
     | |__ | |  | | |__ /  \       /  \  | |__) || | \033[0m
    \033[1;32m |  __|| |  | |  __/ /\ \     / /\ \ |  ___/ | |
     | |   | |__| | | / ____ \   / ____ \| |    _| |_
     |_|    \____/|_|/_/    \_\ /_/    \_\_|   |_____| \033[0m K.Fire
---------------------------------------------------------------

Example:

{'rule':'domain="baidu.com"','page':'','size':'','fields':'host','is_full':''}
    ''')
    try:
        get_ini=open('fofa.ini','rt')
        data = get_ini.read()
        get_ini.close()
        ini = eval(data)
    except:
        print_r('>请检查fofa.ini.10秒后自动退出')
        time.sleep(10)
        exit()
    main(ini)
