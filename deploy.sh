#!/bin/bash
echo "hello world"

# 敏感信息(包括数据库链接,docker 仓库地址)要提前设置环境变量,然后该脚本要提前读环境变量,
# 该环境变量设置在主机里面永久设置环境变量,docker-compose从虚拟机环境变量里面读

# 安装docker 并且给赋予当前用户组docker 权限

# 安装docker-compose 需要安装pip 然后 pip 安装docker-compose

# 下载docker-compose.yml 文件,然后把服务跑起来

# 配置runner 然后让runner 注册gitlab ci