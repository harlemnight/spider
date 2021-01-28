 select l.symbol,l.symbol_name,k.market
   from t_china_security_list l,
				t_china_security_market k
  where 1=1
	  and substr(l.symbol,1,3) = k.pre_symbol
		and l.type='stock'
		