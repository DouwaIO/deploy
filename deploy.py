"""
这是环思erp用来部署的脚本,这个脚本要用两种方式实现,先用python写一个
要做到
# 敏感信息(包括数据库链接,docker 仓库地址)要提前设置环境变量,然后该脚本要提前读环境变量,

sudo echo "export AAA=100;BBB=200" | sudo tee huansi.sh

设置环境变量的工作要提前做,给一个命令的方式搞定,要给所有用户指定环境变量

# 该环境变量设置在主机里面永久设置环境变量,docker-compose从虚拟机环境变量里面读

# 安装docker 并且给赋予当前用户组docker 权限

# 安装docker-compose 需要安装pip 然后 pip 安装docker-compose

# 下载docker-compose.yml 文件,然后把服务跑起来

# 配置runner 然后让runner 注册gitlab ci

"""

import os, sys


# 安装docker
def install_docker():
    step1 = os.system("wget -qO- https://get.docker.com/ | sh")
    assert step1 == 0, "docker 安装失败"
    step2 = os.system('echo "huansi.net" | sudo -S usermod -aG docker huansi')
    assert step2 == 0, "docker 用户组更改失败"
    step3 = os.system("sudo service docker start")
    assert step3 == 0, "docker 服务启动失败"
    step4 = os.system("docker run hello-world")
    assert step4 == 0, "docker 运行失败"


# 安装docker-compose

def install_compose():
    s0 = os.system("sudo apt update")
    assert s0 == 0, "apt 更新失败"
    s1 = os.system("sudo apt install python-pip")
    assert s1 == 0, "安装pip失败"
    s2 = os.system("sudo apt install python3-pip")
    assert s2 == 0, "安装pip3失败"
    s3 = os.system("pip install docker-compose")
    assert s3 == 0, "安装docker-compose失败"
    s4 = os.system("docker-compose --version")
    assert s4 == 0, "docker-compose 启动失败"

# 将项目跑起来

def deploy():
    s0 = os.system()

# 安装配置gitlab-runner

def install_runner():
    pass

# 安装gitlab runner

