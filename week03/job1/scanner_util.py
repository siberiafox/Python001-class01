import os
import json
from queue import Queue
import threading
from concurrent.futures import ProcessPoolExecutor
from socket import *


# multiprocess
def make_processes(q,func,fin,workers=5):
    with ProcessPoolExecutor(workers) as p:
        try:
            if func == 'ping':
                results = p.map(ScanThread.ping_ip,q)
            elif func == 'tcp':
                results = p.map(ScanThread.check_server,q)
        for r in results:
            json.dump(r,fin)
        except Exception as e:
            print(e)
        

# threads
class ScanThread(threading.Thread):
    def __init__(self,name,q,func,output,lock):
        super().__init__()
        self.name = name
        self.q = q
        self.func = func
        self.output = output
        self.lock = lock
        self.start()

    def run(self):
        print(f'{self.name} threading start...')
        self.scheduler()
        print(f'{self.name} threading end...')

    def scheduler(self):
        while True:
            if self.q.empty():
                break
            else:
                self.info = self.q.get()
                # print(self.info)
                if self.func == 'ping':
                    r = self.ping_ip(*self.info)
                elif self.func == 'tcp':
                    r = self.check_server(*self.info)
                self.lock.acquire()
                try:
                    if r:
                        json.dump(self.info,self.output)
                finally:
                    self.lock.release()

     # tcp method
    @staticmethod
    def check_server(ip,port):
        s = socket(AF_INET,SOCK_STREAM)
        try:
            s.connect((ip,port))
            s.settimeout(3)
            return True
        except:
            return False
        finally:
            s.close()

    # ping method
    @staticmethod
    def ping_ip(ip):
        flag = os.system(f'ping {ip}')
        if not flag:
            print(f'{ip} can ping')
            return True
        else:
            print(f'{ip} can not ping,abandoned')
            return False

