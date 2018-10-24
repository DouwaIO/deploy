import os


def fix_docker():
    s0 = os.system("mkdir -p /etc/systemd/system/docker.service.d")
    assert s0 == 0, "创建文件夹"
    s1 = os.system(
        "sudo cp ./http-proxy.conf /etc/systemd/system/docker.service.d/http-proxy.conf")
    s2 = os.system(
        "sudo cp ./https-proxy.conf /etc/systemd/system/docker.service.d/https-proxy.conf")
    assert s1 == 0, "拷贝文件失败"
    assert s2 == 0, "拷贝文件失败"
    s3 = os.system('sudo systemctl daemon-reload')
    s4 = os.system('sudo systemctl restart docker')
    assert s3 == 0
    assert s4 == 0
    s5 = os.system('systemctl show --property=Environment docker')
    print("安装shadowsocks成功")

if __name__ == "__main__":
    fix_docker()
