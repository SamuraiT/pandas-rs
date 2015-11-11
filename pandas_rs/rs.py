import psycopg2
import pandas as pd

def create_engine(dbname, user, password, host, port):
    return Redshift.create_engine(dbname, user, password, host, port)

class Redshift(object):
    """
    Redshift client which connect to redshfit database.
    Furthermore, you can read sql from Redshift and
    returns the reuslt with pandas dataframe structure
    """

    @classmethod
    def create_engine(kls, dbname, user, password, host, port):
        rs = Redshift(
            dbname,
            user,
            password,
            host,
            port
        )
        return rs

    def __init__(self, dbname, user, password, host, port):
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
        try:
            return pd.read_sql(sql, self.con_pg, index_col, columns=columns)
        except psycopg2.InterfaceError as error:
            self.con_pg = self.connect(config=self.config)
            if count < 5:
                return self.read_sql(sql, index_col, columns, count=count+1)
            else:
                raise RedshiftConnectionError(error)



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

