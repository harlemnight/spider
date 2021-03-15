 select  operation,count(1) from  t_xt_logger_mx
 group by operation
 order by 1
 
 
 delete from   t_xt_logger_mx t 
 where t."operation" = 'init_eastmoney_area'
  and t.status = 'n';
 
 
 select * from t_xt_logger_mx t
 where t."operation" = 'init_shareholder'
 
 