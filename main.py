from c_calc import calc_block as c_calc
from logger import result_logger as write_log
import data_transformation as d_t
import controller as con


def button_click():
    j = d_t.data_formatting(con.input_data())
    calc_result = c_calc(j)
    con.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()
