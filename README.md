# pandas-rs

Pandas extension for AWS RedShift (not official)
inspired by [pandas-td](https://github.com/treasure-data/pandas-td)

# installation

~~~
pip install pandas-rs
~~~


# Usage

First export password via shell(recommended)

~~~shell
export REDSHIFT_PASSWORD='password'
~~~

~~~py
import pandas_rs as rs
import os # use only if you will access password through environment variables

rs.create_engine(
    dbname='dev',
    user='test',
    password=os.environ['REDSHIFT_PASSWORD'],
    host='foobar.redshift.exmple',
    port='5439'
)


print(rs.read_sql("""select 'hello redshift' greeting"""))
~~~

result

~~~py
         greeting
0  hello redshift
~~~
