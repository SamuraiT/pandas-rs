import pandas_rs as rs
import pandas as pd
from pandas.util.testing import assert_frame_equal

class TestPandasRs(object):

    def test_create_engine(self):
        assert None is rs.create_engine(
            dbname='circle_test',
            user='ubuntu',
            password='',
            host='localhost',
            port='5432'
        )

    def test_read_sql(self):
        expected = pd.DataFrame(['hello'], columns=['test'])
        assert_frame_equal(rs.read_sql("select 'hello' test"), expected)


