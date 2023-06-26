# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os


# 执行sql的方法
def execute_hive_e_sql(sql):
    """
    使用hive -e来执行
    :param sql:
    :return:
    """
    exe_sql = 'hive -e "{}"'.format(sql)
    print("开始执行：" + exe_sql)
    result = os.popen(exe_sql).readlines()
    print("执行完成：" + exe_sql)
    # print(exe_sql)
    return result


# 获取sql的结果
def get_sys_config_data(sql_str):
    """
    读取sql结果信息
    :param sys:
    :return:
    """
    # print("sql："+sql_str)
    result_line = execute_hive_e_sql(sql_str)

    config_data = [ele.split("\t") for ele in result_line]

    # print("---配置表的信息---")
    # print(config_data)
    return config_data


month_voucher_list = [
    'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000001_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000003_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000004_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000005_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000006_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000007_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000008_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000009_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000010_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000011_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000012_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000014_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000015_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000016_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000017_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000019_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000020_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000021_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000022_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000023_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000024_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000028_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000029_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000030_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000031_month_i_i_d'
    , 'odm_fi_tz_dm_gj_general_g_journal_voucher_sync_000032_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000035_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000036_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000037_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000038_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000039_month_i_i_d'
    , 'odm_fi_hs_dm_gj_general_g_journal_voucher_sync_000041_month_i_i_d'
]

# 判断上一日快照表是否有数
sql_model_01 = """
select count(*)
from dmf_bc.dmfbc_rpt_recvbl_odm_redu_month_voucher_merge_s_d
where recvbl_dt = date_sub('{TX_DATE}',1)
"""

# 初始化
sql_model_02 = """
        select concat(id,'_',superior_biz_type) as new_id  ,cast(status as string) as status ,cast(voucher_state as string) as voucher_state ,cast(voucher_type as string) as voucher_type ,cast(manual_dt as string) as manual_dt ,cast(direction_em as string) as direction_em ,cast(subject_no as string) as subject_no ,cast(jdfin_name as string) as jdfin_name ,cast(company_name as string) as company_name ,cast(aux_subject_1_type as string) as aux_subject_1_type ,cast(aux_subject_2_type as string) as aux_subject_2_type ,cast(aux_subject_3_type as string) as aux_subject_3_type ,cast(aux_subject_1_name as string) as aux_subject_1_name ,cast(aux_subject_2_name as string) as aux_subject_2_name ,cast(aux_subject_3_name as string) as aux_subject_3_name ,cast(currency as string) as currency ,cast(update_time as string) as update_time ,cast(trans_amt as decimal(38,12)) as trans_amt ,cast(dt as string) as dt
        from {from_table_name}
	    where dt <= '{TX_DATE}'
"""

# 增量
sql_model_03 = """
        select concat(id,'_',superior_biz_type) as new_id  ,cast(status as string) as status ,cast(voucher_state as string) as voucher_state ,cast(voucher_type as string) as voucher_type ,cast(manual_dt as string) as manual_dt ,cast(direction_em as string) as direction_em ,cast(subject_no as string) as subject_no ,cast(jdfin_name as string) as jdfin_name ,cast(company_name as string) as company_name ,cast(aux_subject_1_type as string) as aux_subject_1_type ,cast(aux_subject_2_type as string) as aux_subject_2_type ,cast(aux_subject_3_type as string) as aux_subject_3_type ,cast(aux_subject_1_name as string) as aux_subject_1_name ,cast(aux_subject_2_name as string) as aux_subject_2_name ,cast(aux_subject_3_name as string) as aux_subject_3_name ,cast(currency as string) as currency ,cast(update_time as string) as update_time ,cast(trans_amt as decimal(38,12)) as trans_amt ,cast(dt as string) as dt
        from {from_table_name}
	    where dt = '{TX_DATE}'
"""

# 拼sql
sql_model_04 = """
use dmf_bc;

alter table dmf_bc.dmfbc_rpt_recvbl_odm_redu_month_voucher_merge_s_d drop partition(recvbl_dt='{TX_DATE}');
alter table dmf_bc.dmfbc_rpt_recvbl_odm_redu_month_voucher_merge_s_d drop partition(recvbl_dt<='{TX_PRE_60_DATE}');
insert into dmf_bc.dmfbc_rpt_recvbl_odm_redu_month_voucher_merge_s_d partition(recvbl_dt='{TX_DATE}')
select new_id,status,voucher_state,voucher_type,manual_dt,direction_em,subject_no,jdfin_name,company_name,aux_subject_1_type,aux_subject_2_type,aux_subject_3_type,aux_subject_1_name,aux_subject_2_name,aux_subject_3_name,currency,update_time,trans_amt,dt
from (
    select *,row_number() over(partition by new_id order by update_time desc) as rn
    from (
	    --上一日去重结果
        select new_id,status,voucher_state,voucher_type,manual_dt,direction_em,subject_no,jdfin_name,company_name,aux_subject_1_type,aux_subject_2_type,aux_subject_3_type,aux_subject_1_name,aux_subject_2_name,aux_subject_3_name,currency,update_time,trans_amt,dt
	    from dmf_bc.dmfbc_rpt_recvbl_odm_redu_month_voucher_merge_s_d
	    where recvbl_dt = date_sub('{TX_DATE}',1)
		union all
		--当日增量
	    {union_all_sql}
    ) a
) t where rn = 1
"""


# python实现add_months
def get_add_months(in_date, num):
    in_year, in_month, in_day = str(in_date).split('-')
    if (int(in_month) + num) % 12 == 0:
        out_year = str(int(in_year) + (int(in_month) + num) // 12 - 1)
        out_month = str("12")
    else:
        out_year = str(int(in_year) + (int(in_month) + num) // 12)
        out_month = str((int(in_month) + num) % 12).zfill(2)  # 月份补齐两位

    out_day = in_day
    list_date = [out_year, out_month, out_day]
    out_date = "-".join(list_date)
    return out_date


# 拼接sql
def get_select_sql():
    TX_DATE = '2021-09-26'
    TX_PRE_60_DATE = get_add_months(TX_DATE, -2)

    # 获取月凭证回抽汇总表上一日数据条数
    #date_sub_num = int(get_sys_config_data(sql_model_01.format(TX_DATE=TX_DATE))[0][0])
    date_sub_num=10

    # 个业务大类月凭证表union列表
    union_all_sql_list = []
    for tab_nm in month_voucher_list:
        if (date_sub_num == 0):
            # 上一日没数全量去重
            union_all_sql_list.append(sql_model_02.format(from_table_name=tab_nm, TX_DATE=TX_DATE))
        else:
            # 上一日有数增量加上一日去重
            union_all_sql_list.append(sql_model_03.format(from_table_name=tab_nm, TX_DATE=TX_DATE))
    union_all_sql = '        union all'.join(union_all_sql_list)
    sql_01 = sql_model_04.format(union_all_sql=union_all_sql, TX_DATE=TX_DATE, TX_PRE_60_DATE=TX_PRE_60_DATE)
    sql_map = {}
    sql_map['sql_01'] = sql_01
    return sql_map


sql_map = get_select_sql()
print(sql_map['sql_01'])
