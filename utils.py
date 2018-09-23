from sys import platform

def isWindows():
    if "win" in platform.lower():
        return True
    return False


DEFAULT_FILE_PATH = 'C:\\temp\\' if isWindows() else '/tmp/'
FILENAME = 'bulbs_ip.txt'

def str_color_to_rgb_tuple(color):
    return int(color[1:2], 16), int(color[3:4], 16), int(color[5:6], 16)
