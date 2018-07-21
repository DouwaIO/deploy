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
    step2 = os.system('sudo usermod -aG docker huansi')
    assert step2 == 0, "docker 用户组更改失败"
    step3 = os.system("sudo service docker start")
    assert step3 == 0, "docker 服务启动失败"
    step4 = os.system("sudo docker run hello-world")
    assert step4 == 0, "docker 运行失败"
    print("安装docker 成功")


# 安装docker-compose

def install_compose():
    s0 = os.system("sudo apt update")
    assert s0 == 0, "apt 更新失败"
    s1 = os.system("sudo apt install -y -qq --no-install-recommends python-pip >/dev/null")
    assert s1 == 0, "安装pip失败"
    s2 = os.system("sudo apt install -y -qq --no-install-recommends python3-pip >/dev/null")
    assert s2 == 0, "安装pip3失败"
    s = os.system('sudo pip install setuptools')
    assert s==0, "setuptools 安装失败"
    s3 = os.system("sudo pip install docker-compose")
    assert s3 == 0, "安装docker-compose失败"
    s4 = os.system("sudo docker-compose --version")
    assert s4 == 0, "docker-compose 启动失败"
    print("安装docker-compose成功")


# 将项目跑起来

def deploy():
    s0 = os.system(
        "curl https://raw.githubusercontent.com/DouwaIO/deploy/master/docker-compose.yml > docker-compose.yml")
    assert s0 == 0, "下载compose失败"
    s1 = os.system("docker login ${DOCKER_HOST} -u ${DOCKER_USER} -p ${DOCKER_PASSWORD}")
    assert s1 == 0, "登录镜像仓库失败"
    s2 = os.system("sudo docker-compose up -d")
    assert s2 == 0, "服务 启动失败"
    print("服务启动成功")


# 安装配置gitlab-runner


# 安装gitlab runner
def install_runner():
    # 创建配置文件
    # os.system("sudo mkdir /etc/gitlab-runner")
    # assert s0 == 0, "创建runner配置文件夹失败"
    s1 = os.system("sudo docker run --rm -t -i -v /etc/gitlab-runner:/etc/gitlab-runner gitlab/gitlab-runner register \
                   -n -u https://gitlab.com/ -r cyVyXLcrRxtgwGz_r2_q --executor docker --docker-image docker\
                   --tag-list {}".format(os.getenv("CUSCODE")))
    assert s1 == 0, "runner配置失败"
    os.system("sudo chmod 777 /etc/gitlab-runner/config.toml")
    with open('/etc/gitlab-runner/config.toml', 'r') as f:
        s = f.read()
        a = s.replace(' volumes = ["/cache"]', 'volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]')
    with open('/etc/gitlab-runner/config.toml', 'w') as f:
        f.write(a)
    s2 = os.system("sudo docker run -d --name gitlab-runner --restart always \
                   -v /etc/gitlab-runner:/etc/gitlab-runner \
                   -v /var/run/docker.sock:/var/run/docker.sock \
                   gitlab/gitlab-runner:latest")
    assert s2 == 0, "安装runner失败"
    print("安装runner成功")


if __name__ == "__main__":
    install_docker()
    install_compose()
    deploy()
    install_runner()
