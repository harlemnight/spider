
select sw.lvl,
				sw.hymc,
				dz.symbol
  from t_china_stock_industry_sw sw,
			 t_china_stock_industry_sw_dzb dz
where 1=1
  and sw.hy_dm = dz.hy_dm
  and sw.hymc like '%半导体%'