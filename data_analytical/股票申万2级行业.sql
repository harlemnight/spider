
 select sw.hymc,
			  l.symbol,
				l.symbol_name
   from t_china_stock_industry_sw sw,
				t_china_stock_industry_sw_dzb dz,
				t_china_security_list	l
  where 1=1
	  and sw.hy_dm = dz.hy_dm
		and dz.symbol = l.symbol
		and l.symbol = '002515';
		
		
		
				