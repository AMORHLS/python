TYPE=VIEW
query=select curdate() AS `month` union select (curdate() - interval 1 month) AS `month` union select (curdate() - interval 2 month) AS `month` union select (curdate() - interval 3 month) AS `month` union select (curdate() - interval 4 month) AS `month` union select (curdate() - interval 5 month) AS `month` union select (curdate() - interval 6 month) AS `month` union select (curdate() - interval 7 month) AS `month` union select (curdate() - interval 8 month) AS `month` union select (curdate() - interval 9 month) AS `month` union select (curdate() - interval 10 month) AS `month` union select (curdate() - interval 11 month) AS `month`
md5=74e9e31927b55e259002dfe6fc96dc4f
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=2018-02-09 10:06:32
create-version=1
source=SELECT\n	curdate() AS `month`\nUNION\n	SELECT\n			curdate() - INTERVAL 1 MONTH AS `month`\n	UNION\n		SELECT\n				curdate() - INTERVAL 2 MONTH AS `month`\n		UNION\n			SELECT \n       curdate() - INTERVAL 3 MONTH AS `month`\n			UNION\n				SELECT\n						curdate() - INTERVAL 4 MONTH AS `month`\n				UNION\n					SELECT\n							curdate() - INTERVAL 5 MONTH AS `month`\n					UNION\n						SELECT\n								curdate() - INTERVAL 6 MONTH AS `month`\n						UNION\n							SELECT\n									curdate() - INTERVAL 7 MONTH AS `month`\n							UNION\n								SELECT\n									curdate() - INTERVAL 8 MONTH AS `month`\n								UNION\n									SELECT\n											curdate() - INTERVAL 9 MONTH AS `month`\n									UNION\n										SELECT\n												curdate() - INTERVAL 10 MONTH AS `month`\n										UNION\n											SELECT\n													curdate() - INTERVAL 11 MONTH  AS `month`
client_cs_name=utf8
connection_cl_name=utf8_general_ci
view_body_utf8=select curdate() AS `month` union select (curdate() - interval 1 month) AS `month` union select (curdate() - interval 2 month) AS `month` union select (curdate() - interval 3 month) AS `month` union select (curdate() - interval 4 month) AS `month` union select (curdate() - interval 5 month) AS `month` union select (curdate() - interval 6 month) AS `month` union select (curdate() - interval 7 month) AS `month` union select (curdate() - interval 8 month) AS `month` union select (curdate() - interval 9 month) AS `month` union select (curdate() - interval 10 month) AS `month` union select (curdate() - interval 11 month) AS `month`
