# fofa-IP-tool
批量提取fofa查询到IP

#exec 
scrapy crawl spider -o data.json
参照scrapy的数据导出
# fofa.ini 
{
'cookie':'存放已登陆账号cookie中： _fofapro_ars_session=xxxxx  中的xxxxx',
'page':'你要提取的页数',
'rules':'查询规则"'
}
#数据示例
![Image text](https://github.com/k-fire/fofa-IP-tool/blob/master/img.png?raw=true)
