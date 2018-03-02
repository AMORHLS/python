TYPE=VIEW
query=select `att_g`.`id` AS `group_id`,`att_g`.`name` AS `group_name`,`att_s`.`id` AS `shiht_id`,`att_s`.`name` AS `shiht_name`,`att_s`.`code` AS `shiht_code` from ((`ehr`.`attendance_group_rule` `att_g_r` left join `ehr`.`attendance_group` `att_g` on((`att_g`.`id` = `att_g_r`.`group_id`))) left join `ehr`.`attendance_shiht` `att_s` on((`att_g_r`.`shiht_id` = `att_s`.`id`))) order by `att_g`.`id` desc
md5=11b1bcf90ad5a5301fa29055ad5b12e1
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-01-25 07:56:14
create-version=1
source=select `att_g`.`id` AS `group_id`,`att_g`.`name` AS `group_name`,`att_s`.`id` AS `shiht_id`,`att_s`.`name` AS `shiht_name`,`att_s`.`code` AS `shiht_code` from ((`attendance_group_rule` `att_g_r` left join `attendance_group` `att_g` on((`att_g`.`id` = `att_g_r`.`group_id`))) left join `attendance_shiht` `att_s` on((`att_g_r`.`shiht_id` = `att_s`.`id`))) order by `att_g`.`id` desc
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select `att_g`.`id` AS `group_id`,`att_g`.`name` AS `group_name`,`att_s`.`id` AS `shiht_id`,`att_s`.`name` AS `shiht_name`,`att_s`.`code` AS `shiht_code` from ((`ehr`.`attendance_group_rule` `att_g_r` left join `ehr`.`attendance_group` `att_g` on((`att_g`.`id` = `att_g_r`.`group_id`))) left join `ehr`.`attendance_shiht` `att_s` on((`att_g_r`.`shiht_id` = `att_s`.`id`))) order by `att_g`.`id` desc
