import subprocess


def add_repo(name, repo):
    subprocess.call(["flatpak", "remote-add", "--if-not-exists", name, repo])


def install_app(repo_name, app_list):
    subprocess.call(["flatpak", "install", "-y", repo_name] + app_list)


def flathub_setup():
    repos = {"flathub": "https://flathub.org/repo/flathub.flatpakrepo",
             "flathub-beta": "https://flathub.org/beta-repo/flathub-beta.flatpakrepo"}
    for name, repo in repos.items():
        add_repo(name, repo)


def common_apps():
    flathub_apps = ["us.zoom.Zoom", "org.libreoffice.LibreOffice", "org.gimp.GIMP",
                    "org.deluge_torrent.deluge", "net.cozic.joplin_desktop",
                    "io.mpv.Mpv", "io.lbry.lbry-app", "io.github.antimicrox.antimicrox", "io.exodus.Exodus",
                    "im.riot.Riot", "fr.handbrake.ghb", "eu.scarpetta.PDFMixTool", "com.visualstudio.code",
                    "com.valvesoftware.Steam", "com.obsproject.Studio", "com.github.tchx84.Flatseal",
                    "com.github.micahflee.torbrowser-launcher", "com.github.iwalton3.jellyfin-media-player",
                    "com.calibre_ebook.calibre", "com.bitwarden.desktop", "org.kde.kdenlive"]
    flathub_beta_apps = ["com.google.Chrome", "com.brave.Browser"]
    install_app("flathub", flathub_apps)
    install_app("flathub-beta", flathub_beta_apps)


def kde_apps():
    apps = ["org.kde.gwenview", "org.gtk.Gtk3theme.Breeze-Dark",
            "org.kde.kcalc", "org.kde.kwrite", "org.kde.okular"]
    install_app("flathub", apps)
    subprocess.call(["flatpak", "override", "--user", "--env=GTK_THEME=Breeze-Dark"])


if __name__ == "__main__":
    flathub_setup()
    common_apps()
    kde_apps()
