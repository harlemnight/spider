
select sw.lvl,
				sw.hymc,
				dz.symbol,
				dz.symbol_name,
				sw.index_dm
  from t_china_stock_industry_sw sw,
			 t_china_stock_industry_sw_dzb dz
where 1=1
  and sw.hy_dm = dz.hy_dm
	and sw.hymc like '%半导体%';
	


 select b2.swhy_dm,b2.swhymc,b2.swhylevel,
				li.symbol,
				li.symbol_name
   from t_jqdata_swhy_dzb b1,
				t_jqdata_swhy b2,
				t_china_security_list li
	where 1=1
	  and b1.swhy_dm = b2.swhy_dm
		and substr(b1.symbol, 1, 6) = li.symbol
		and b2.swhylevel = 'sw_l3'
		and swhymc like '%半导体%'
		