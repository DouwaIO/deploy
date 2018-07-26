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


if __name__ == "__main__":
    init_env()
    install_docker()
    print("请重启虚拟机")
