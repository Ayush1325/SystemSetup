import subprocess


def install_applications(apps):
    subprocess.call(["rpm-ostree", "install"] + apps)


def add_repo(repourl: str):
    reponame = repourl.split("/").pop()
    sys_path = "/etc/yum.repos.d/" + reponame
    subprocess.call["wget", "-O", sys_path, repourl]


# Needs reboot to take effect
def add_rpmfusion():
    subprocess.call(["rpm-ostree", "install", "https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
                    "https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"])


def install_nvidia():
    packages = ["akmod-nvidia", "xorg-x11-drv-nvidia-cuda",
                "xorg-x11-drv-nvidia-cuda-libs"]
    install_applications(packages)
    subprocess.call(["rpm-ostree", "kargs", "--append=rd.driver.blacklist=nouveau",
                    "--append=modprobe.blacklist=nouveau", "--append=nvidia-drm.modeset=1"])


def jellyfin():
    repourl = "https://copr.fedorainfracloud.org/coprs/brianjmurrell/jellyfin/repo/fedora-35/brianjmurrell-jellyfin-fedora-35.repo"
    add_repo(repourl)
    install_applications(["jellyfin"])


def kde():
    packages = ["yakuake", "kcm_systemd", "ffmpegthumbs"]
    install_applications(packages)


def common():
    packages = ["libratbag-ratbagd", "hplip-gui"]
    install_applications(packages)


if __name__ == "__main__":
    common()
    install_nvidia()
    jellyfin()
