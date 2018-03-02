TYPE=VIEW
query=select `tp`.`id` AS `productId`,`tp`.`name` AS `productName`,`tp`.`number` AS `productNumber`,`tp`.`specification` AS `specification`,`tp`.`category_id` AS `categoryId`,`tp`.`supplier_id` AS `supplierId`,`ts`.`name` AS `supplierName`,`tc`.`category_name` AS `categoryName`,`tp`.`unit_id` AS `unitId`,`tu`.`name` AS `unitName` from (((`wms`.`t_product` `tp` left join `wms`.`t_unit` `tu` on((`tu`.`id` = `tp`.`unit_id`))) left join `wms`.`t_category` `tc` on((`tc`.`id` = `tp`.`category_id`))) left join `wms`.`t_supplier` `ts` on((`ts`.`id` = `tp`.`supplier_id`))) where ((`tp`.`del_flag` = 0) and (`tu`.`del_flag` = 0))
md5=220b61f2f35a32916c8234bfc773d950
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-02-09 13:34:27
create-version=1
source=select `tp`.`id` AS `productId`,`tp`.`name` AS `productName`,`tp`.`number` AS `productNumber`,`tp`.`specification` AS `specification`,`tp`.`category_id` AS `categoryId`,`tp`.`supplier_id` AS `supplierId`,`ts`.`name` AS `supplierName`,`tc`.`category_name` AS `categoryName`,`tp`.`unit_id` AS `unitId`,`tu`.`name` AS `unitName` from (((`t_product` `tp` left join `t_unit` `tu` on((`tu`.`id` = `tp`.`unit_id`))) left join `t_category` `tc` on((`tc`.`id` = `tp`.`category_id`))) left join `t_supplier` `ts` on((`ts`.`id` = `tp`.`supplier_id`))) where ((`tp`.`del_flag` = 0) and (`tu`.`del_flag` = 0))
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select `tp`.`id` AS `productId`,`tp`.`name` AS `productName`,`tp`.`number` AS `productNumber`,`tp`.`specification` AS `specification`,`tp`.`category_id` AS `categoryId`,`tp`.`supplier_id` AS `supplierId`,`ts`.`name` AS `supplierName`,`tc`.`category_name` AS `categoryName`,`tp`.`unit_id` AS `unitId`,`tu`.`name` AS `unitName` from (((`wms`.`t_product` `tp` left join `wms`.`t_unit` `tu` on((`tu`.`id` = `tp`.`unit_id`))) left join `wms`.`t_category` `tc` on((`tc`.`id` = `tp`.`category_id`))) left join `wms`.`t_supplier` `ts` on((`ts`.`id` = `tp`.`supplier_id`))) where ((`tp`.`del_flag` = 0) and (`tu`.`del_flag` = 0))
