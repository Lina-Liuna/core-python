import platform

def get_like_distro():
    print(platform.version())
    print(platform.machine())
    print(platform.platform())
    print(platform.release())
    print(platform.architecture())
    print(platform.processor())
    print(platform.node())
    print(platform.mac_ver())
    print(platform.java_ver())
    print(platform.system())

print(get_like_distro())
