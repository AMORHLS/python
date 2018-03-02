TYPE=VIEW
query=select date_format(`trqi`.`quality_time`,\'%Y-%m\') AS `month`,sum(`trqid`.`inspection_quantity`) AS `inspection_count` from (`wms`.`t_repertory_quality_inspection` `trqi` left join (select `wms`.`t_repertory_quality_inspection_detail`.`inspection_id` AS `inspection_id`,sum(`wms`.`t_repertory_quality_inspection_detail`.`inspection_quantity`) AS `inspection_quantity` from `wms`.`t_repertory_quality_inspection_detail` where (`wms`.`t_repertory_quality_inspection_detail`.`del_flag` = \'not_del\') group by `wms`.`t_repertory_quality_inspection_detail`.`inspection_id`) `trqid` on((`trqi`.`id` = `trqid`.`inspection_id`))) where (`trqi`.`type` = \'purchase\') group by date_format(`trqi`.`quality_time`,\'%y-%m\')
md5=21fa9c54ceb6a067a7a83d0ff9bf066c
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-02-09 13:34:27
create-version=1
source=select date_format(`trqi`.`quality_time`,\'%Y-%m\') AS `month`,sum(`trqid`.`inspection_quantity`) AS `inspection_count` from (`wms`.`t_repertory_quality_inspection` `trqi` left join (select `wms`.`t_repertory_quality_inspection_detail`.`inspection_id` AS `inspection_id`,sum(`wms`.`t_repertory_quality_inspection_detail`.`inspection_quantity`) AS `inspection_quantity` from `wms`.`t_repertory_quality_inspection_detail` where (`wms`.`t_repertory_quality_inspection_detail`.`del_flag` = \'not_del\') group by `wms`.`t_repertory_quality_inspection_detail`.`inspection_id`) `trqid` on((`trqi`.`id` = `trqid`.`inspection_id`))) where (`trqi`.`type` = \'purchase\') group by date_format(`trqi`.`quality_time`,\'%y-%m\')
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select date_format(`trqi`.`quality_time`,\'%Y-%m\') AS `month`,sum(`trqid`.`inspection_quantity`) AS `inspection_count` from (`wms`.`t_repertory_quality_inspection` `trqi` left join (select `wms`.`t_repertory_quality_inspection_detail`.`inspection_id` AS `inspection_id`,sum(`wms`.`t_repertory_quality_inspection_detail`.`inspection_quantity`) AS `inspection_quantity` from `wms`.`t_repertory_quality_inspection_detail` where (`wms`.`t_repertory_quality_inspection_detail`.`del_flag` = \'not_del\') group by `wms`.`t_repertory_quality_inspection_detail`.`inspection_id`) `trqid` on((`trqi`.`id` = `trqid`.`inspection_id`))) where (`trqi`.`type` = \'purchase\') group by date_format(`trqi`.`quality_time`,\'%y-%m\')
