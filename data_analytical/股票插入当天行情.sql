
truncate table  t_china_stock_trade_current;

	 insert into t_china_stock_trade_2020
	 select * from t_china_stock_trade_current;
	 
	 
	 