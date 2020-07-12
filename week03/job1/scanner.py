import sys
import time
from queue import Queue
from threading import Lock
from collections import defaultdict
from scanner_pre import check_input_params, update_params,make_ips
from scanner_util import ping_ip,check_server,ScanThread

# global params
# init params set
d = {
    'n':None, # 并发数量,范围1-10
    'f':None, # cmd指令，包含ping/tcp
    'ip':None, # 支持连续ip 例如 192.168.0.1-192.168.0.100
    'w':None, # 扫描结果保存本机路径地址
    'm':None, # 选做，指定扫描器使用多进程或多线程模型,multip或者thread
    'v':None # 选做 打印扫描器运行耗时,'1'显示,'0'不显示
}
# init usual ports set
usual_ports = {
    'http':[80,8080,3128,8081,9098],
    'socks':[1080],
    'ftp':[21],
    'telnet':[23],
    'tftp':[69],
    'ssh':[22],
    'smtp':[25],
    'pop3':[110]
}


def main_scanner():
    try:
        params_from_cmd = sys.argv[1:]
        params = check_input_params(params_from_cmd)
        update_params(params)
    except Exception as e:
        print(f'input unlegal,input again(exit:q): reason [{e}]')
        while True:
            params = input('>>>')
            params = params.split(sep=' ')
            if params[0] == 'q':
                print('exiting')
                time.sleep(2)
                sys.exit()
            try:
                params = check_input_params(params)
                update_params(params)
            except Exception as e:
                print(f'input unlegal,input again(exit:q): reason [{e}]')
                continue
            break

    print('cmd updated! go on working!')
    print(f'cmd dict is updated to: {d}')

    # make ips
    ips = make_ips(params['ip'])
    # open file
    fin = open(params['w'],'w',encoding='utf-8')
    # create lock
    lock = Lock()
    # create time point if exists
    if params['v']:
        time_start = time.time()

    if params['m'] is None or params['m'] == 'thread':
        q = Queue(20)
        for ip in ips:
            q.put((ip))
        thread_names = [f'scan_{i}' for i in range(params['n'])]
        threads = []
        for name in thread_names:
            thread = ScanThread(name,q,params['f'],fin,lock)
            threads.append(thread)
        for t in threads:
            t.join()

    elif params['m'] == 'multip':
        pass

    if params['v']:
        time_end = time.time()
    print(f'this loop costs time is {time_end-time_start} seconds!')


# this moudle test for main function
if __name__ == "__main__":
    main_scanner()
    print('main over!')
    




