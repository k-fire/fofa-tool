# fofa-IP-tool
批量提取fofa查询到IP

# exec <br>
scrapy crawl spider -o data.json<br>
参照scrapy的数据导出<br>
# fofa.ini <br>
{<br>
'cookie':'存放已登陆账号cookie中： _fofapro_ars_session=xxxxx  中的xxxxx',<br>
'page':'你要提取的页数',<br>
'rules':'查询规则"'<br>
}<br>
# 数据示例<br>
![Image text](https://github.com/k-fire/fofa-IP-tool/blob/master/img.png?raw=true)
