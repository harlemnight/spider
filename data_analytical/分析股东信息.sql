 select * from t_china_stock_shareholder_sjkzr
 where symbol = '000070';
 
 
  select * from t_china_stock_shareholder_gdrs
 where symbol = '000070'
 order by rq desc;
 
 
  select * from t_china_stock_shareholder_sdgd
 where symbol = '000070'
 order by rq desc,to_number(replace(cgs,',',''), '9999999999999999999')  desc;
 
 
  select rq ,count(1) ,sum(to_number(replace(replace(cgs,',',''),'.00',''), '9999999999999999999'))
	from t_china_stock_shareholder_jjcg
 where symbol = '000070'
group by rq 
 order by rq desc;
 
 
  select *
	from t_china_stock_shareholder_jjcg
 where symbol = '000070'
 order by rq desc;
 
 