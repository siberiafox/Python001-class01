import re
from scanner import d,usual_ports

def check_input_params(params):
    # keys:input params name
    # values:input params value
    keys,values = [],[]
    # input params name check
    for i in params:
        if re.match('^-[a-z]+',i):
            keys.append(i.replace('-',''))
        else:
            values.append(i)
    # use assert  key and value match
    assert len(keys) == len(values),'params key and value must match!'
    # create params dict for the next using
    params_dict = {k:v for k,v in zip(keys,values)}
    # check key fit the default keysq
    if not set(params_dict.keys()).issubset(set(d.keys())):
        raise Exception('unlegal keys')
    # check required value not be None 
    if None in [params_dict.get(k,None) for k in list(d.keys())[:4]]:
        raise Exception('key of params：n,f,ip,w must input value!')
    # check required value
    for key in params_dict:
        if key == 'n':
            try:
                # n value turn into number of int
                params_dict[key] = int(params_dict.get(key))
                if params_dict[key] not in range(1,11):
                    raise Exception('int value not in (1,10)!')
            except:
                raise Exception('n param value must be a int in (1,20)')
        if key == 'f':
            if params_dict[key] not in ('ping','tcp'):
                raise Exception('f param value input wrong!')
        if key == 'ip':
            pattern = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
            l = params_dict[key].split('-')
            if len(l) == 1:
                if not pattern.match(l[0]):
                    raise Exception('ip param value is not a IP!')
            elif len(l) == 2:
                if not pattern.match(l[0]) or not pattern.match(l[1]):
                    raise Exception('ip param value is not a IP!')
            else:
                raise Exception('ip param value input wrong!')
            # ip value turn into string of list
            params_dict[key] = l
    # optional m param check
    m = params_dict.get('m',None)
    if m:
        if m not in ('multip,thread'):
            raise Exception('m param value input wrong!')
    # if not input ,default None
    params_dict['m'] = m
    # optional v param check
    v = params_dict.get('v',None)
    if v:
        if v not in ('1','0'):
            raise Exception('v param value input wrong!')
        # v value turn into number of int if exists
        v = int(v)
    # if not input, default None
    params_dict['v'] = v
    # return input_params checked and modified
    return params_dict


def update_params(params_dict):
    global d
    d.update(params_dict)


def make_ips(ip_list):
    new_list = []
    if len(ip_list) == 1:
        return ip_list[0]
    elif len(ip_list) == 2:
        *base_ip_start,ip_start = ip_list[0].split('.')
        *base_ip_end,ip_end = ip_list[1].split('.')
        assert base_ip_start == base_ip_end,'ip domain 1rd-3rd must same'
        ip_zone = range(int(ip_start),int(ip_end)+1)
        for i in ip_zone:
            ip = '.'.join(base_ip_start)+'.'+str(i)
            new_list.append(ip)
        return new_list
            
    