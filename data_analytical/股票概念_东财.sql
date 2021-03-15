			select
						 e.concept_name,
						 dz.symbol,
						 dz.symbol_name
			 from	t_china_stock_concept_eastmoney e,
					  t_china_stock_concept_eastmoney_dzb dz
		  where 1=1 
		    and e.concept_dm =  dz.concept_dm
			  and e.concept_name like '%5G%'
				

	
	
	