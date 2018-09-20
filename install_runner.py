import os


def install_runner():
    # 创建配置文件
    # os.system("sudo mkdir /etc/gitlab-runner")
    # assert s0 == 0, "创建runner配置文件夹失败"
    s1 = os.system("sudo docker run --rm -t -i -v /etc/gitlab-runner:/etc/gitlab-runner gitlab/gitlab-runner register \
                   -n -u https://gitlab.com/ -r xT6eJJxxr5GBZtJ1JttG --executor docker --docker-image docker \
                   --tag-list {}".format(os.getenv("HSCUSCODE")))
    assert s1 == 0, "runner配置失败"
    os.system("sudo chmod 777 /etc/gitlab-runner/config.toml")
    with open('/etc/gitlab-runner/config.toml', 'r') as f:
        s = f.read()
        a = s.replace(' volumes = ["/cache"]',
                      'volumes = ["/var/run/docker.sock:/var/run/docker.sock","/etc/profile.d/huansi.sh:/etc/profile.d/huansi.sh" ,"/cache"]')
    with open('/etc/gitlab-runner/config.toml', 'w') as f:
        f.write(a)
    s2 = os.system("sudo docker run -d --name gitlab-runner --restart always \
                   -v /etc/gitlab-runner:/etc/gitlab-runner \
                   -v /var/run/docker.sock:/var/run/docker.sock \
                   -v /etc/profile.d/huansi.sh:/etc/profile.d/huansi.sh \
                   gitlab/gitlab-runner:latest")
    assert s2 == 0, "安装runner失败"
    s3 = os.system("sudo docker restart gitlab-runner")
    assert s3 == 0, "runner 配置成功"
    print("安装runner成功")


if not os.path.exists('/etc/gitlab-runner'):
    install_runner()
    print("runner安装成功")
