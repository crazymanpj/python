# encoding: UTF-8
# Date:    2017-12-15
# Author:  pangjian

from sql import Sql
import helper
import mynum


class Datanalyzer(object):
    """docstring for Datanalyzer"""
    def __init__(self, arg=''):
        super(Datanalyzer, self).__init__()
        self.arg = arg

    def get_lb_1dliucun(self, pid, m_date):
        s_inst = Sql(m_date)
        inst = s_inst.get_lb_newinst_bypid(pid)
        m_date_lc = helper.get_time_bydiff(m_date, -1)
        s_lc1d = Sql(m_date_lc)
        lc1d = s_lc1d.get_lb_liucun_1d_bypid(pid)
        ret = mynum.float_decimal2(float(lc1d) / float(inst) * 100)
        return ret

    def get_lb_7dliucun(self, pid, m_date):
        s_inst = Sql(m_date)
        inst = s_inst.get_lb_newinst_bypid(pid)
        m_date_lc = helper.get_time_bydiff(m_date, -7)
        s_lc7d = Sql(m_date_lc)
        lc7d = s_lc7d.get_lb_liucun_7d_bypid(pid)
        ret = mynum.float_decimal2(float(lc7d) /float(inst) * 100)
        return ret

    #m_date需要传入需要计算留存的那个日期
    def get_db_1dliucun(self, tid1, tid2, m_date):
        s_inst = Sql(m_date)
        inst = s_inst.get_db_newinst_bytid(tid1, tid2)
        # s_lc1d = Sql(m_date)
        if tid1 =='all' and tid2 == 'all':
            lc1d = s_inst.get_db_1dliucun_bytid_instdate('-1', '-1')
        else:
            lc1d = s_inst.get_db_1dliucun_bytid_instdate(tid1, tid2)
        ret = mynum.float_decimal2(float(lc1d) / float(inst) * 100)
        return ret

    #m_date需要传入需要计算留存的那个日期
    def get_db_7dliucun(self, tid1, tid2, m_date):
        s_inst = Sql(m_date)
        inst = s_inst.get_db_newinst_bytid(tid1, tid2)
        if tid1 == 'all' and tid2 == 'all':
            lc7d = s_inst.get_db_7dliucun_bytid_instdate('-1', '-1')
        else:
            lc7d = s_inst.get_db_7dliucun_bytid_instdate(tid1, tid2)
        ret = mynum.float_decimal2(float(lc7d) / float(inst) * 100)
        return ret

if __name__ == '__main__':
    da = Datanalyzer()
    # print da.get_lb_1dliucun('all', '2017-12-13')
    # print da.get_lb_7dliucun('all', '2017-12-07')
    da.get_db_1dliucun('all', 'all', '2018-01-09')
    da.get_db_7dliucun('all', 'all', '2018-01-03')
