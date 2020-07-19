import pandas as pd
import numpy as np

np.random.seed(42)

fake_data1 = pd.DataFrame({'id': range(1, 21),
                           'age': np.random.randint(18, 66, 20),
                           'order_id': np.random.randint(1, 4, 20)})

fake_data2 = pd.DataFrame({'id': range(1, 21),
                           'age': np.random.randint(18, 66, 20),
                           'order_id': np.random.randint(1, 4, 20)})

print(fake_data1.head(3), fake_data2.head(3), sep='\n')

# select * from data
# data = pd.read_csv('path')
fake_data1.loc[:, :]

# select * from data limit 10
# data = pd.read_csv('path', nrows=10)
fake_data1.loc[:9, :]

# select id from data
fake_data1[['id']]

# select count(id) from data
fake_data1.id.count()

# select * from data where id<10 and age>30
mask = (fake_data1.id < 10) & (fake_data1.age > 30)
fake_data1[mask]

# select id,count(distinct order_id) from table1 group by id
fake_data1.groupby('id')[['order_id']].agg(lambda x: len(x.unique()))

# select * from table1 t1 inner join table2 t2 on t1.id = t2.id
fake_data1.join(fake_data2.set_index('id'), on='id',
                how='inner', rsuffix='_data2')

# select * from table1 union select * from table2
pd.concat([fake_data1, fake_data2], axis=0).reset_index(drop=True)

# delete from table1 where id=10
idx = fake_data1[fake_data1.id == 10].index
fake_data1.drop(index=idx, inplace=True)
fake_data1.reset_index(drop=True, inplace=True)

# alter table table1 drop column column_name
fake_data1.drop(columns=['age'], inplace=True)
