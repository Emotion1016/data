# import os
# import time
#
#
# def get_battery():
#     return os.popen('adb shell dumpsys battery').read()
#
#
# def get_time():
#     return os.popen('time').read()
#
#
# while True:
#     time.sleep(60)
#     with open('D:/battery_log.txt', 'a+') as f:
#         res1 = os.popen('adb shell dumpsys battery').read()
#         res2 = time.ctime()
#         f.write(res1)
#         f.write(res2)
#         f.write('\n\n\n')
#         if 'AC powered: true' in res1:
#             continue
#         else:
#             break

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
    summary = 0
    for i in range(0, len(files)-1):
        with open(f"D:/appium_project/data/{files[i]}", "r", encoding="utf8") as f:
            summary += len(f.readlines())-1
    print(summary)


file_name(r'D:\appium_project\data')
