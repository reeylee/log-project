from django.test import TestCase

# Create your tests here.
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='demo', charset='utf-8')

cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8