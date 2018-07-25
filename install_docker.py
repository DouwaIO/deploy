import os


def install_docker():
    # step1 = os.system("wget -qO- https://get.docker.com/ | sh")
    # assert step1 == 0, "docker 安装失败"
    # step2 = os.system('sudo usermod -aG docker huansi')
    # assert step2 == 0, "docker 用户组更改失败"
    os.system("sudo mkdir -p /etc/docker")
    step3 = os.system("""
    sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://m6wlkecl.mirror.aliyuncs.com"]
}
EOF
    """)
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl restart docker")
    print("docker安装成功")


if __name__ == "__main__":
    install_docker()
    print("请重启虚拟机")
