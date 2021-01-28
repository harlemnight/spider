 select  operation,count(1) from  t_xt_logger_mx
 group by operation
 
 
 t_china_stock_concept_eastmoney_dzb
 
 
 delete from   t_xt_logger_mx t 
 where t."operation" = 'init_eastmoney_concept'
  and t.status = 'n';
 
 
 select * from t_xt_logger_mx t
 where t."operation" = 'init_shareholder'
 
 