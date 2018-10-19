import os


def goto_google():
    s0 = os.system("sudo pip3 install shadowsocks")
    assert s0 == 0, "shadowsocks 安装失败"
    s1 = os.system("sudo cp ${PWD}/openssl.py ")
    assert s1 == 0, "安装pip失败"
    s2 = os.system("sudo apt install -y -qq --no-install-recommends python3-pip >/dev/null")
    assert s2 == 0, "安装pip3失败"
    s = os.system('sudo pip install setuptools')
    assert s == 0, "setuptools 安装失败"
    s3 = os.system("sudo pip install docker-compose")
    assert s3 == 0, "安装docker-compose失败"
    s4 = os.system("sudo docker-compose --version")
    assert s4 == 0, "docker-compose 启动失败"
    print("安装docker-compose成功")


if __name__ == '__main__':
    goto_google()