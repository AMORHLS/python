TYPE=VIEW
query=select round(sum(`p`.`count`),0) AS `countProduct`,count(`o`.`order_id`) AS `countOrder`,round(sum((`p`.`product_price` * `p`.`count`)),0) AS `priceToal`,date_format(`o`.`order_date`,\'%Y-%m\') AS `orderDate` from (`aps`.`t_order` `o` left join `aps`.`t_order_product` `p` on((`o`.`id` = `p`.`order_id`))) group by date_format(`o`.`order_date`,\'%Y-%m\') order by `orderDate` desc
md5=b876978551e95c5cf2107b1cb87d3181
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-02-09 02:26:03
create-version=1
source=select round(sum(`p`.`count`),0) AS `countProduct`,count(`o`.`order_id`) AS `countOrder`,round(sum((`p`.`product_price` * `p`.`count`)),0) AS `priceToal`,date_format(`o`.`order_date`,\'%Y-%m\') AS `orderDate` from (`t_order` `o` left join `t_order_product` `p` on((`o`.`id` = `p`.`order_id`))) group by date_format(`o`.`order_date`,\'%Y-%m\') order by `orderDate` desc
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select round(sum(`p`.`count`),0) AS `countProduct`,count(`o`.`order_id`) AS `countOrder`,round(sum((`p`.`product_price` * `p`.`count`)),0) AS `priceToal`,date_format(`o`.`order_date`,\'%Y-%m\') AS `orderDate` from (`aps`.`t_order` `o` left join `aps`.`t_order_product` `p` on((`o`.`id` = `p`.`order_id`))) group by date_format(`o`.`order_date`,\'%Y-%m\') order by `orderDate` desc
