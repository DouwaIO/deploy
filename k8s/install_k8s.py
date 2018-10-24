import os


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
    print("安装shadowsocks成功")


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
    install_compose()
    install_shadowsocks()
    get_google()

    print("请重启虚拟机")
