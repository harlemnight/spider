# https://www.jianshu.com/p/3bcb98dd2654
# https://blog.csdn.net/weixin_43174639/article/details/84643586?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# https://www.cnblogs.com/deartear/p/8616457.html
import example_price as ep
import example_property as ept


if __name__ == '__main__':
    ep.init_stocks()  # 初始化标股票 每日4点执行
    start_date = '20200101'
    end_date = '20201231'
    ep.init_history_stock_price(start_date, end_date)  # 补录历史行情
    ep.insert_batch_current_price('stock') # 记录当日股票收盘行情 4点后执行
    ept.init_industry_stocks() # 初始化申万二级行业成份股 每周执行一次
    ept.init_concepts_10jqka()    # 初始化概念 每周执行一次
    ept.init_concept_stocks_10jqka() # 初始化概念成份股 每周执行一次

