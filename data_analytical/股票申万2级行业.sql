----新浪可以查申万二级行业对照 其他互联网上没有三级行业了
 select sw.hy_dm,
				sw.sjhy_dm,
				sw.hymc,
			  l.symbol,
				l.symbol_name
   from t_china_stock_industry_sw sw,
				t_china_stock_industry_sw_dzb dz,
				t_china_security_list	l
  where 1=1
	  and sw.hy_dm = dz.hy_dm
		and dz.symbol = l.symbol
		and l.symbol = '600519';
		
	----因此用聚宽处理申万三级行业
		
		
		
	select * from 	t_china_stock_industry_sw order by 1
	
		
				