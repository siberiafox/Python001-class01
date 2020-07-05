import pymysql
import pandas as pd
# mysql database info
db_info = {
    'host': '',
    'port': 3306,
    'user': '',
    'pwd': ''
}

# this function must be called after creating database once in pipelines! 
def load_proxy_from_db(
    table_name = 'freeproxy', 
    db = 'test',
    out_path = "'D:/CodeProjects/PythonProjects/PAC3/week02/job1/proxies.csv'"):

    conn = pymysql.connect(
        host = db_info['host'],
        port = db_info['port'],
        user = db_info['user'],
        password = db_info['pwd'],
        db = db,
        charset = 'utf8mb4'
    )
    cur = conn.cursor()
    try:
        cur.execute(f'select * from {table_name} into outfile {out_path}')
    except Exception:
        print('no table named %s' % table_name)
        cur.close()
        conn.close()
    
    df = pd.read_csv(out_path, dtype='str')
    df.sort_values('speed', ascending=False, inplace=True)
    df['porxy'] = df['protocol'] + '://' + df['ip'] + ':' + df['port']
    return df.proxy.values[:3].tolist()
