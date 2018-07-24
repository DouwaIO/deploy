import os


def install_docker():
    step1 = os.system("wget -qO- https://get.docker.com/ | sh")
    assert step1 == 0, "docker 安装失败"
    step2 = os.system('sudo usermod -aG docker huansi')
    assert step2 == 0, "docker 用户组更改失败"
    print("docker安装成功")


if __name__ == "__main__":
    install_docker()
