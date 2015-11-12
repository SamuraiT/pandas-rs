# pandas-rs

pandas-rs is oirginally designed for RedShift but
also work for PostgreSQL. Inspired by [pandas-td](https://github.com/treasure-data/pandas-td)

I may should have made the package name as pandas-pg, since It also work for
PostgreSQL.

# installation

~~~
pip install pandas-rs
~~~


# Usage

As I mentioned, above pandas-rs works for PostgreSQL as well.
First export password via shell(recommended)

~~~shell
export REDSHIFT_OR_POSTGRESQL_PASSWORD='password'
~~~

~~~py
import pandas_rs as rs
import os # use only if you will access password through environment variables

rs.create_engine(
    dbname='dev',
    user='test',
    password=os.environ['REDSHIFT_OR_POSTGRESQL_PASSWORD'],
    host='foobar.redshift.exmple',
    port='5439'
)


print(rs.read_sql("""select 'hello PostgreSQL or redshift' greeting"""))
~~~

result

~~~py
         greeting
0  hello PostgreSQL or redshift
~~~
