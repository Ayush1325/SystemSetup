import subprocess


def install_apps(app_list):
    subprocess.call(["pacman", "-S", "--noconfirm"] + app_list)


def systemd_enable(services):
    subprocess.call(["systemctl", "enable", services])


def append_file(file_path, content):
    with open(file_path, 'a') as f:
        f.writelines(content)


def install_common():
    packages = ["cups", "hplip", "xsane",
                "nvidia", "nvidia-settings", "firewalld", "pipewire",
                "pipewire-pulse", "pipewire-alsa", "git", "rustup", "neovim",
                "sudo", "base-devel", "flatpak", "reflector", "btrfs-progs", "toolbox",
                "grub", "efibootmgr", "openssh"]
    install_apps(packages)
    services = ["cups", "firewalld", "reflector.timer", "fstrim.timer"]
    systemd_enable(services)


def install_kde():
    packages = ["plasma-desktop", "sddm", "networkmanager",
                "konsole", "yakuake", "kdeconnect", "kde-gtk-config",
                "plasma-pa", "dolphin", "kdegraphics-thumbnailers", "ffmpegthumbs",
                "kdeplasma-addons", "print-manager", "system-config-printer", "powerdevil",
                "sddm-kcm"]
    install_apps(packages)
    services = ["NetworkManager", "sddm"]
    systemd_enable(services)


def set_timezone():
    subprocess.call(
        ["ln", "-sf", "/usr/share/zoneinfo/Asia/Kolkata", "/etc/localtime"])
    subprocess.call(["hwclock", "--systohc"])


def gen_locale():
    append_file("/etc/locale.conf", ["LANG=en_IN.UTF-8"])
    append_file("/etc/locale.gen", ["en_IN.UTF-8 UTF-8"])
    subprocess.call("source /etc/locale.conf && locale-gen", shell=True)


def network_config():
    hostname = "pcarch"
    append_file("/etc/locale.conf", [hostname])
    append_file("/etc/hosts", ["127.0.0.1   localhost", "::1		localhost",
                f"127.0.1.1	{hostname}.localdomain	{hostname}"])


def gen_fstab():
    subprocess.call(["genfstab", "-U", "/mnt", "/mnt/etc/fstab"])


def create_user():
    username = "ayush"
    subprocess.call(["useradd", "-m", "-G", "wheel", username])


def setup_grub():
    subprocess.call(["grub-install", "--target=x86_64-efi",
                    "--efi-directory=/boot", "--bootloader-id=GRUB"])
    subprocess.call(["grub-mkconfig", "-o", "/boot/grub/grub.cfg"])


if __name__ == "__main__":
    set_timezone()
    gen_locale()
    network_config()
    install_common()
    install_kde()
    create_user()
    setup_grub()
    print("Create Passwords for Both Users")
    print("Edit Initramfs for nvidia")
