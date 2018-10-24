from pprint import pprint
import os


def init_env():
    while True:
        HSCUSCODE = input("请输入客户代号HSCUSCODE:")
        print(HSCUSCODE)
        HSDB_USER = input("请输入数据库用户HSDB_USER:")
        print(HSDB_USER)
        HSDB_PASSWORD = input("请输入数据库密码HSDB_PASSWORD:")
        print(HSDB_PASSWORD)
        HSDB_HOST = input("请输入数据库主机地址HSDB_HOST:")
        print(HSDB_HOST)
        HSDB_PORT = input("请输入数据库端口号HSDB_PORT:")
        print(HSDB_PORT)
        HSDB_NAME = input("请输入数据库名称HSDB_NAME:")
        print(HSDB_NAME)
        HSDOCKER_HOST = input("请输入docker镜像仓库地址 HSDOCKER_HOST:")
        print(HSDOCKER_HOST)
        HSDOCKER_USER = input("请输入docker镜像仓库用户HSDOCKER_USER:")
        print(HSDOCKER_USER)
        HSDOCKER_PASSWORD = input("请输入docker镜像仓库密码HSDOCKER_PASSWORD:")
        print(HSDOCKER_PASSWORD)
        HSPASSWORD = "huansi.net"
        env = dict(HSCUSCODE=HSCUSCODE, HSDB_USER=HSDB_USER,
                   HSDB_PASSWORD=HSDB_PASSWORD, HSDB_HOST=HSDB_HOST,
                   HSDB_PORT=HSDB_PORT, HSDB_NAME=HSDB_NAME, HSDOCKER_HOST=HSDOCKER_HOST,
                   HSDOCKER_USER=HSDOCKER_USER, HSDOCKER_PASSWORD=HSDOCKER_PASSWORD,
                   HSPASSWORD=HSPASSWORD)
        pprint(env)
        flag = input("请检查以上环境变量设置是否争取,确认请输入Y,输入其他,重新设置:")
        if flag == 'Y':
            with open("/etc/profile.d/huansi.sh", "w") as f:
                for k, v in env.items():
                    f.writelines("export {}={}\n".format(k, v))
            print('环境变量设置成功')
            return "设置成功"
        elif flag == "N":
            continue
        else:
            continue


def install_docker():
    step1 = os.system("wget -qO- https://get.docker.com/ | sh")
    assert step1 == 0, "docker 安装失败"
    step2 = os.system('sudo usermod -aG docker huansi')
    assert step2 == 0, "docker 用户组更改失败"
    os.system("sudo mkdir -p /etc/docker")
    step3 = os.system("""
    sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://m6wlkecl.mirror.aliyuncs.com"]
}
EOF
    """)
    assert step3 == 0, "docker 镜像地址更新失败"
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl restart docker")
    print("docker安装成功")


def install_compose():
    s0 = os.system("sudo apt update")
    assert s0 == 0, "apt 更新失败"
    s2 = os.system(
        "sudo apt install -y -qq --no-install-recommends python3-pip >/dev/null")
    assert s2 == 0, "安装pip3失败"
    s = os.system('sudo pip3 install setuptools')
    assert s == 0, "setuptools 安装失败"
    s3 = os.system("sudo pip3 install docker-compose")
    assert s3 == 0, "安装docker-compose失败"
    s4 = os.system("sudo docker-compose --version")
    assert s4 == 0, "docker-compose 启动失败"
    print("安装docker-compose成功")


def install_shadowsocks():
    s0 = os.system("sudo pip3 install shadowsocks")
    assert s0 == 0, "shadowsock安装失败"
    s1 = os.system(
        "sudo cp ./openssl.py /usr/local/lib/python3.6/dist-packages/shadowsocks/crypto/openssl.py")
    assert s1 == 0, "拷贝文件失败"


def get_google():
    s0 = os.system("sudo apt update")
    assert s0 == 0, "apt 更新失败"
    s2 = os.system(
        "sudo apt install -y -qq --no-install-recommends curl >/dev/null")
    assert s2 == 0, "安装curl失败"
    s3 = os.system(
        "sudo apt install -y -qq --no-install-recommends polipo >/dev/null")
    assert s3 == 0, "安装polipo失败"
    s4 = os.system("sudo cp ./polipo.conf /etc/polipo/config")
    assert s4 == 0, "拷贝配置失败"
    s5 = os.system("sudo /etc/init.d/polipo restart")
    assert s5 == 0, "polipo重启失败"
    s6 = os.system("source ./proxy.sh")
    assert s6 == 0, "proxy 环境变量设置失败"
    s7 = os.system("sudo sslocla -c ./.shadowsocks.json -d start")
    assert s7 == 0, "翻墙成功"
    s8 = os.system("curl www.google.com")
    assert s8 == 0, "eme 没有搞定google"


def install_k8s():
    s0 = os.system(
        "sudo cp ./kubernetes.list /etc/apt/sources.list.d/kubernetes.list")
    assert s0 == 0, "拷贝list失败"
    s1 = os.system("sudo cp ./apt.conf /etc/apt/apt.conf")
    assert s1 == 0, "拷贝apt.conf失败"
    s2 = os.system(
        "sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -")
    assert s2 == 0, "增加公钥失败"
    s3 = os.system('sudo apt update')
    assert s3 == 0, "更新源失败"
    s4 = os.system(
        'sudo apt install -y -qq --no-install-recommends kubelet kubeadm kubectl >/dev/null')
    assert s4 == 0, "安装kuberadm失败"
    s5 = os.system("kubeadm version")
    assert s5 == 0, "kubeadm 安装失败"


if __name__ == "__main__":
    # init_env()
    install_docker()
    install_compose()
    install_shadowsocks()
    get_google()

    print("请重启虚拟机")
