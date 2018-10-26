import os


def rm_docker():
    s0 = os.system("sudo rm -rf -p /etc/systemd/system/docker.service.d")
    assert s0 == 0, "创建文件夹"
    s3 = os.system('sudo systemctl daemon-reload')
    s4 = os.system('sudo systemctl restart docker')
    assert s3 == 0
    assert s4 == 0
    s5 = os.system('systemctl show --property=Environment docker')
    print("docker代理配置成功")


if __name__ == "__main__":
    rm_docker()
