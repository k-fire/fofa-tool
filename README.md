# fofa-IP-tool
批量提取fofa查询结果（域名 IP title）

## < spider文件夹 ><br>
### exec<br>
scrapy crawl spider -o data.json<br>
参照scrapy的数据导出<br>
### fofa.ini <br>
不登陆账号仅且只能爬取1页<br>
{<br>
'cookie':'存放已登陆账号cookie中： _fofapro_ars_session=xxxxx  中的xxxxx',<br>
'page':'你要提取的页数',<br>
'rules':'查询规则"'<br>
}<br>
### 数据示例<br>
![Image text](https://github.com/k-fire/fofa-IP-tool/blob/master/spider/img.png?raw=true)<br>

## < api文件夹（仅适用于会员）><br>
### input<br>
运行前你需要配置fofa.ini<br>
运行后你需要输入一个字典<br>
参照 {'rule':'domain="baidu.com"','page':'','size':'','fields':'host','is_full':''}<br>
每个选项参考官方接口<br>
![Image text](https://github.com/k-fire/fofa-IP-tool/blob/master/api/api.bmp?raw=true)<br>
 数据示例<br>
![Image text](https://github.com/k-fire/fofa-IP-tool/blob/master/api/img.bmp?raw=true)<br>
<
