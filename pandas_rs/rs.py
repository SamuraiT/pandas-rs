import psycopg2
import pandas as pd

class Redshift(object):
    """
    Redshift client which connect to redshfit database.
    Furthermore, you can read sql from Redshift and
    returns the reuslt with pandas dataframe structure
    """

    def __init__(self, config=None):
        self.config = config
        self.con_pg = None
        if config is not None:
            self.con_pg = self.connect(config=config)

    def create_engine(self, dbname, user, password, host, port):
        self.config = dict(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.con_pg = self.connect(config=self.config)

    def connect(self, *args,**kwargs):
        config = kwargs['config']
        try:
            con_pg=psycopg2.connect(
                dbname=config['dbname'],
                host=config['host'],
                port=config['port'],
                user=config['user'],
                password=config['password']
            )
            return con_pg
        except Exception as err:
            print(err)

    def read_sql(self, sql, index_col=None, columns=None, count=0):
        return pd.read_sql(sql, self.con_pg, index_col, columns=columns)

class RedshiftConfigurationError(Exception):

    def __init__(self,
            expr="ConfigError",
            msg="Config does not exists. create engine"):
        self.expr = expr
        self.msg = msg

    def __str__(self):
        return "{} {}".format(self.expr, self.msg)


class RedshiftConnectionError(Exception):
    """Exception raised for errors in the Redshift connection.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg="Failed to connect"):
        self.expr = expr
        self.msg = msg

    def __str__(self):
        return "{} {}".format(self.expr, self.msg)


def create_engine(dbname, user, password, host, port):
    rs.create_engine(dbname, user, password, host, port)

def read_sql(sql, index_col=None, columns=None):
    if rs.con_pg is None: raise RedshiftConfigurationError()
    return  rs.read_sql(sql, index_col, columns)

# HACK:FIX.
# this code is really ugly
# I did so because I wanted to store the configuration, and
# wanted users to use `read_sql` without setting cursor everytime they access to DB
rs = Redshift()
