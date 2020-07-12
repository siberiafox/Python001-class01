import sys
import time
from queue import Queue
from threading import Lock
from collections import defaultdict
from scanner_pre import check_input_params, update_params,make_ips
from scanner_util import ScanThread,make_processes
from scanner_pre import d,usual_ports

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
        if params['f'] == 'ping':
            for ip in ips:
                q.put((ip,))
        elif params['f'] == 'tcp':
            for ip in ips:
                for type_,ports in usual_ports:
                    for port in ports:
                        q.put((ip,port))
        thread_names = [f'scan_{i}' for i in range(params['n'])]
        threads = []
        for name in thread_names:
            thread = ScanThread(name,q,params['f'],fin,lock)
            threads.append(thread)
        for t in threads:
            t.join()

    elif params['m'] == 'multip':
        pass

    fin.close()

    if params['v']:
        time_end = time.time()
    print(f'this loop costs time is {time_end-time_start} seconds!')


# this moudle test for main function
if __name__ == "__main__":
    main_scanner()
    print('main over!')
    




