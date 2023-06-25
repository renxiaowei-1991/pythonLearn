create table if not exists employee01(
     id int unsigned auto_increment
    ,first_name  varchar(40)   comment '名'   not null
    ,last_name   varchar(40)   comment '姓'   not null
    ,age         int           comment '年龄' not null
    ,sex         varchar(2)    comment '性别' not null
    ,income      decimal(22,2) comment '收入' not null
    ,primary key (id)
) comment '雇员表'
engine=InnoDB charset=utf8