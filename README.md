# GXss v0.1
Python Flask 开发的XSS利用工具
## 使用说明：  
1、将gxss.sql导入到数据库  
2、data目录下的config.py 更改数据库配置  

## 启动 --start

python3 gxss.py --start ｜启动服务，默认是8080端口  
python3 gxss.py --start 80 ｜ 启动服务，指定端口  

## 生成邀请码 --kengen

python3 gxss.py --keygen ｜ 生成邀请码，默认生成一个  
python3 gxss.py --keygen 2 ｜ 生成邀请码，指定数量  
