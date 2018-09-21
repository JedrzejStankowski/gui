from sys import platform

def isWindows():
    if "win" in platform.lower():
        return True
    return False


DEFAULT_FILE_PATH = 'C:\\temp\\' if isWindows() else '/tmp/'
FILENAME = 'bulbs_ip.txt'
