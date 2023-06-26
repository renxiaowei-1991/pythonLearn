# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os


# 自定义-业务大类编码
biz_type = "000011"

# 交易明细表-若缺失需添加
biz_typ_tab_nam_key_01 = {
    "000001": "dmf_gj.dmfgj_gj_cf_fi_hs_transaction_detail_000001_i_d",
    "000004": "dmf_gj.dmfgj_gj_sf_fi_hs_transaction_detail_000004_i_d",
    "000005": "dmf_gj.dmfgj_gj_crowdfu_fi_transaction_detail_i_d",
    "000006": "dmf_gj.dmfgj_gj_fin_fi_hs_transaction_detail_i_d",
    "000007": "dmf_gj.dmfgj_gj_ftc_fi_hs_transaction_detail_i_d",
    "000008": "dmf_gj.dmfgj_gj_sec_fi_transaction_detail_i_d",
    "000009": "dmf_gj.dmfgj_gj_insu_fi_hs_transaction_detail_i_d",
    "000010": "dmf_gj.dmfgj_gj_am_fi_hs_transaction_detail_i_d",
    "000011": "dmf_gj.dmfgj_gj_pay_fi_hs_transaction_detail_i_d",
    "000012": "dmf_gj.dmfgj_gj_sf_fi_hs_transaction_detail_000012_i_d",
    "000014": "dmf_gj.dmfgj_gj_ct_fi_hs_transaction_detail_i_d",
    "000015": "dmf_gj.dmfgj_gj_uc_fi_transaction_detail_i_d",
    "000016": "dmf_gj.dmfgj_gj_alpha_fi_hs_transaction_detail_i_d",
    "000017": "dmf_gj.dmfgj_gj_ctr_fi_transaction_detail_i_d",
    "000019": "dmf_gj.dmfgj_gj_mb_fi_hs_transaction_detail_i_d",
    "000022": "dmf_gj.dmfgj_gj_cf_fi_hs_transaction_detail_000022_i_d",
    "000023": "dmf_gj.dmfgj_gj_cf_fi_hs_transaction_detail_000023_i_d",
    "000024": "dmf_gj.dmfgj_gj_sf_fi_hs_transaction_detail_000024_i_d",
    "000031": "dmf_gj.dmfgj_gj_user_fi_hs_transaction_detail_i_d",
    "000035": "dmf_gj.dmfgj_gj_pay_fi_hs_transaction_detail_000035_i_d",
    "000036": "dmf_gj.dmfgj_gj_ftc_fi_hs_transaction_detail_000036_i_d",
    "000037": "dmf_gj.dmfgj_gj_fin_fi_hs_transaction_detail_000037_i_d",
    "000039": "dmf_gj.dmfgj_gj_cf_fi_hs_transaction_detail_000039_i_d",
    "000044": "dmf_gj.dmfgj_gj_cf_fi_hs_transaction_detail_000044_i_d",
    "000048": "dmf_gj.dmfgj_gj_user_fi_hs_tmk_transaction_detail_i_d",
}

# 交易明细表-业财对账-若缺失需添加
biz_typ_tab_nam_key_02 = {
    "000003": "dmf_gj.dmfgj_gj_ncjr_fi_hs_transaction_detail_ycdz_i_d",
    "000005": "dmf_gj.dmfgj_gj_crowdfu_fi_hs_transaction_detail_ycdz_i_d",
    "000006": "dmf_gj.dmfgj_gj_fin_fi_hs_transaction_detail_ycdz_i_d",
    "000017": "dmf_gj.dmfgj_gj_ctr_fi_hs_transaction_detail_ycdz_i_d",
    "000021": "dmf_gj.dmfgj_gj_ad_fi_hs_transaction_detail_ycdz_i_d",
}

# 临时表-库表-定义
database_name_01 = 'dmf_dev'
table_name_01 = 'dmf_dev.dmftmp_sett_script_tmp_fee_01'
table_name_02 = 'dmf_dev.dmftmp_sett_script_tmp_fee_02'
table_name_03 = 'dmf_dev.dmftmp_sett_script_tmp_fee_03'
table_name_04 = 'dmf_dev.dmftmp_sett_script_tmp_fee_04'
TX_DATE='2022-02-09'

# sql模板01-交易明细表获取01
sql_model_01 = """
    use {database_name_01};

    drop table if exists {table_name_01};
    create table {table_name_01}
    as
    select distinct biz_type,biz_line,data_source_em,trans_type,source_table,sett_biz_type,sett_scenes,fee_type,dt
    from  {table_name_detail}
    where dt>=trunc(add_months('{TX_DATE}',-2),'MM') and nvl(biz_line,'') != ''
    union all 
    select distinct biz_type,biz_line,data_source_em,trans_type,source_table,sett_biz_type,sett_scenes,fee_type,dt
    from  {table_name_detail_ycdz}
    where dt>=trunc(add_months('{TX_DATE}',-2),'MM') and nvl(biz_line,'') != ''
"""

# sql模板02-交易明细表获取02
sql_model_02 = """
    use {database_name_01};

    drop table if exists {table_name_01};
    create table {table_name_01}
    as
    select distinct biz_type,biz_line,data_source_em,trans_type,source_table,sett_biz_type,sett_scenes,fee_type,dt
    from  {table_name_detail}
    where dt>=trunc(add_months('{TX_DATE}',-2),'MM') and nvl(biz_line,'') != ''
"""
sql_model_03 = """
    use {database_name_01};

    drop table if exists dmf_dev.dmfdev_renxiaowei_sett_script_tmp_fee_07;
    create table dmf_dev.dmfdev_renxiaowei_sett_script_tmp_fee_07
    as
    select     --1、分录配置
               a1.ysyf_id as ysyf_id              --账务规则ID
              ,concat(a1.bus_big_type,',',t.node_name) as bus_big_type       --业务大类
    		  ,concat(a1.bus_small_type,',',a2.node_name) as bus_small_type  --业务小类
    		  ,concat(a1.biz_line,',',a3.node_name) as biz_line              --业务线
              ,a1.buss_link_code as buss_link_code                           --凭证号
    		  ,a1.buss_link_name as buss_link_name                           --摘要
              ,concat(a1.borrow_or_loan,',',if(a1.borrow_or_loan='0','借','贷')) as borrow_or_loan  --借贷方向
              ,a1.account_type as subject_no                                 --会计科目
              ,concat(a1.is_tax,',',if(a1.is_tax='1','是','否')) as is_tax   --是否税金科目
              ,a1.tax as tax                                                 --税率
              ,concat(a1.positive_or_negative,','
                     ,case when a1.positive_or_negative = '0' then '绝对值取正'
                           when a1.positive_or_negative = '1' then '绝对值取负'
                           when a1.positive_or_negative = '2' then '实际发生方向'
                           when a1.positive_or_negative = '3' then '取反'
                           else ''
                      end
                     ) as positive_or_negative                                --计算方式
              ,case when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '0' then '固定值-个人'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '1' then '商家名称'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '2' then '银行账户'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '3' then '供应商'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '4' then '项目编号'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '6' then '部门'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '7' then '备用字段1'
                    when a1.is_subject_1_input = '0' and a1.aux_subject_1 = '8' then '备用字段2'
                    when a1.is_subject_1_input = '1' then concat('固定值:',nvl(a1.aux_subject_1,''))
                    when a1.is_subject_1_input = '2' then concat('供应商:',nvl(a1.aux_subject_1,''))
                    when a1.is_subject_1_input = '3' then concat('银行账户:',nvl(a1.aux_subject_1,''))
                    when a1.is_subject_1_input = '4' then concat('部门:',nvl(a1.aux_subject_1,''))
                    when a1.is_subject_1_input = '7' then concat('项目:',nvl(a1.aux_subject_1,''))
                    else ''
               end as aux_subject_1                                           --辅助科目1
    		  ,case when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '0' then '固定值-个人'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '1' then '商家名称'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '2' then '银行账户'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '3' then '供应商'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '4' then '项目编号'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '6' then '部门'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '7' then '备用字段1'
                    when a1.is_subject_2_input = '0' and a1.aux_subject_2 = '8' then '备用字段2'
                    when a1.is_subject_2_input = '1' then concat('固定值:',nvl(a1.aux_subject_2,''))
                    when a1.is_subject_2_input = '2' then concat('供应商:',nvl(a1.aux_subject_2,''))
                    when a1.is_subject_2_input = '3' then concat('银行账户:',nvl(a1.aux_subject_2,''))
                    when a1.is_subject_2_input = '4' then concat('部门:',nvl(a1.aux_subject_2,''))
                    when a1.is_subject_2_input = '7' then concat('项目:',nvl(a1.aux_subject_2,''))
                    else ''
               end as aux_subject_2                                           --辅助科目2
    		  ,case when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '0' then '固定值-个人'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '1' then '商家名称'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '2' then '银行账户'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '3' then '供应商'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '4' then '项目编号'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '6' then '部门'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '7' then '备用字段1'
                    when a1.is_subject_3_input = '0' and a1.aux_subject_3 = '8' then '备用字段2'
                    when a1.is_subject_3_input = '1' then concat('固定值:',nvl(a1.aux_subject_3,''))
                    when a1.is_subject_3_input = '2' then concat('供应商:',nvl(a1.aux_subject_3,''))
                    when a1.is_subject_3_input = '3' then concat('银行账户:',nvl(a1.aux_subject_3,''))
                    when a1.is_subject_3_input = '4' then concat('部门:',nvl(a1.aux_subject_3,''))
                    when a1.is_subject_3_input = '7' then concat('项目:',nvl(a1.aux_subject_3,''))
                    else ''
               end as aux_subject_3                                           --辅助科目3
    		  ,concat(a1.fund_type,',',nvl(a6.codename,'')) as fund_type      --款项类型
    		  ,concat(a1.receipt_type,',',nvl(a7.codename,'')) as receipt_type--财务场景
    		  ,concat(a1.currency,','
    		         ,case when a1.currency = 'BB01' then '人民币'
    				       when a1.currency = 'BB02' then '美元'
    					   when a1.currency = 'BB03' then '港币'
    					   when a1.currency = 'BB04' then '新加坡元'
    					   when a1.currency = 'BB05' then '日元'
    					   when a1.currency = 'BB06' then '澳元'
    					   when a1.currency = 'BB07' then '新西兰元'
    					   when a1.currency = 'BB08' then '欧元'
    					   when a1.currency = 'BB09' then '英镑'
    					   else ''
                      end
    				 ) as currency                                            --币种
    		  --2、交易环节与会计分录映射
    		  ,concat(a4.source_sys,',',nvl(a8.codename,'')) as source_sys    --来源系统
    		  ,concat(a4.code,',',nvl(a9.codename,'')) as biz_scenes          --业务场景
    		  ,concat(a4.trans_type,',',nvl(a10.codename,'')) as trans_type   --交易环节
    		  --,a4.currency
    		  ,concat(a4.has_tax,',',if(a4.has_tax='0','含税','不含税')) as has_tax --是否含税
    		  ,if(nvl(a4.company_name,'')!='',concat('company_no',a4.company_name),'') as company_name  --主体
    		  ,if(a1.borrow_or_loan='0',if(nvl(a4.aux_account_borrow,'')!='',concat('company_no',a4.aux_account_borrow),''),if(nvl(a4.aux_account_loan,'')!='',concat('company_no',a4.aux_account_loan),''))     as aux_account_01  --辅助核算01
    		  ,if(a1.borrow_or_loan='0',if(nvl(a4.aux_account_borrow2,'')!='',concat('company_no',a4.aux_account_borrow2),''),if(nvl(a4.aux_account_loan2,'')!='',concat('company_no',a4.aux_account_loan2),'')) as aux_account_02  --辅助核算02
    		  ,if(a1.borrow_or_loan='0',if(nvl(a4.aux_account_borrow3,'')!='',concat('company_no',a4.aux_account_borrow3),''),if(nvl(a4.aux_account_loan3,'')!='',concat('company_no',a4.aux_account_loan3),'')) as aux_account_03  --辅助核算03
    		  ,if(a11.data_source_em is not null,'新模型','旧模型') as type   --模型类型
    		  --3、结算来源
    		  ,a12.source_table                                               --来源表
    		  ,a12.biz_type                                                   --结算业务类型
    		  ,a12.sett_scenes                                                --结算场景
    		  ,a12.fee_type                                                   --费用类型
    		  --4、业财对账
    		  ,a13.account_payments                                           --收支方向
    		  ,a13.acc_brief_code                                             --账户简码
    		  ,a13.acc_brief_name                                             --账户简称
    		  ,a13.account_type_capital                                       --资金帐分类
    		  ,a13.account_biz_system                                         --来源系统
    from  (select * from odm.odm_fi_dm_subject_s_d
           where dt='{TX_DATE}' and status = '0' 
           and bus_big_type='{biz_type}'
          ) a1
	left join (select id,node_id,node_name,parent_node_id,type,effective_date,expire_date,status,is_online
               from odm.odm_fi_tz_dm_busi_type_s_d  --业务线配置
               where  dt='{TX_DATE}'
                 and  status='1'  --业务线生效状态 0失效/1有效
                 and (nvl(expire_date,'') = '' or expire_date > '{TX_DATE}')
              ) t
           on  a1.bus_big_type = t.node_id
    left join (select id,node_id,node_name,parent_node_id,type,effective_date,expire_date,status,is_online
               from odm.odm_fi_tz_dm_busi_type_s_d  --业务线配置
               where  dt='{TX_DATE}'
                 and  status='1'  --业务线生效状态 0失效/1有效
                 and (nvl(expire_date,'') = '' or expire_date > '{TX_DATE}')
              ) a2
           on  a1.bus_small_type = a2.node_id
    left join (select id,node_id,node_name,parent_node_id,type,effective_date,expire_date,status,is_online
               from odm.odm_fi_tz_dm_busi_type_s_d  --业务线配置
               where  dt='{TX_DATE}'
                 and  status='1'  --业务线生效状态 0失效/1有效
                 and (nvl(expire_date,'') = '' or expire_date > '{TX_DATE}')
              ) a3
           on  nvl(a1.biz_line,'') = a3.node_id
    left join (select * from dmf_dim.dmfdim_gj_hs_fi_hs_dm_bus_enum_config_s_d
               where dt='{TX_DATE}' AND status = '1'
               and bus_big_type='{biz_type}'
              ) a4
           on  a1.bus_small_type = a4.bus_small_type
          and  if(nvl(a1.biz_line,'')='',nvl(a4.biz_line,''),a1.biz_line) = if(nvl(a4.biz_line,'')='',nvl(a1.biz_line,''),a4.biz_line)
          and  a1.buss_link_code = a4.buss_link_code
    left join (select code,codename
               from  odm.odm_fi_dm_ysyf_enums_s_d
               where dt = '{TX_DATE}' and enumstatus=1 and type=8  --款项类型
              ) a6
           on  a1.fund_type = a6.code
    left join (select code,codename
               from  odm.odm_fi_dm_ysyf_enums_s_d
               where dt = '{TX_DATE}' and enumstatus=1 and type=10  --财务场景
              ) a7
           on  a1.receipt_type = a7.code
    left join (select code,codename
               from  odm.odm_fi_dm_ysyf_enums_s_d
               where dt = '{TX_DATE}' and enumstatus=1 and type=15  --来源系统
              ) a8
           on  a4.source_sys = a8.code
    left join (select code,codename
               from  odm.odm_fi_dm_ysyf_enums_s_d
               where dt = '{TX_DATE}' and enumstatus=1 and type=56  --业务场景
              ) a9
           on  a4.code = a9.code
    left join (select type,code,codename
               from  odm.odm_fi_dm_ysyf_enums_s_d
               where dt = '{TX_DATE}' and enumstatus=1              --交易环节
              ) a10
           on  a4.code = a10.type
    	  and  a4.trans_type = a10.code
    left join (select data_source_em,trans_type,count(*) as num from dmf_bc.dmfbc_bc_fi_fst_indx_detail_s_d
               where dt='4712-12-31'
               group by data_source_em,trans_type
              ) a11
           on  a4.source_sys = a11.data_source_em
          and  a4.trans_type = a11.trans_type
    left join  dmf_dev.dmfdev_renxiaowei_sett_script_tmp_fee_04 a12
           on  a1.bus_small_type = a12.small_biz_type
    	  and  a1.biz_line   = a12.biz_line
    	  and  a4.source_sys = a12.data_source_em
    	  and  a4.trans_type = a12.trans_type
    left join  dmf_dev.dmfdev_renxiaowei_sett_script_tmp_fee_06 a13
           on  a13.bus_big_type = '{biz_type}'
    	  and  a1.bus_small_type = a13.bus_small_type
    	  and  if(nvl(a1.biz_line,'')='',nvl(a13.biz_line,''),a1.biz_line) = if(nvl(a13.biz_line,'')='',nvl(a1.biz_line,''),a13.biz_line)
    	  and  a1.buss_link_code = a13.buss_link_code
    	  and  a1.borrow_or_loan = a13.borrow_or_loan
        where  a2.node_name is not null
"""


def get_union_all_sql_03():
    # 结果sql
    union_all_sql_list = ''
    # 变量列表
    sql_model_03_list = {}
    sql_model_03_list['TX_DATE'] = TX_DATE
    sql_model_03_list['database_name_01'] = database_name_01
    sql_model_03_list['biz_type'] = biz_type

    # sql获取
    union_all_sql_list = sql_model_03.format(**sql_model_03_list)

    print(union_all_sql_list)

    # sql插入map
    sql_map = {}
    sql_map['sql_301'] = union_all_sql_list
    return sql_map


sql_map_03 = get_union_all_sql_03()

print(sql_map_03["sql_301"])