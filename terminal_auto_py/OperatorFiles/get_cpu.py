# -*- coding: utf-8 -*-
__author__ = 'zhh'
import OperatorFiles.GlobalData as gd
import subprocess
import os
import re

def GetCpu():
    # print(gd.PATH)
    cmd = '''adb shell top -n 1'''
    cmd1 = 'top -n 1'

    # cmd1 = 'top -o cpu -O +rsize -n 20'
    cpu = subprocess.run(cmd, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
    out = cpu.stdout

    print("*************************")
    # print(len(out))

    lines = out.split('\n')
    # print(len(lines))
    #输出写入txt文件
    output_path = gd.PATH+"/OperatorFiles/source_files/"
    output_file = open(output_path+"get_cpu.txt", 'a+')
    for i in range(len(lines)):
        # print(i,'****',lines[i])
        if i==0 or i==len(lines)-1:
            continue
        else:
            if re.search("PID",lines[i]):  #含有特殊字符的行，进行特殊处理
                lines[i] = " PID USER         PR  NI VIRT  RES  SHR S[%CPU] %MEM     TIME+ ARGS "
            print(lines[i])
            output_file.writelines(lines[i] + '\n')

        # output_file.writelines(str(n)+'**'+line+'\n')
        # if line is not None:
        #     ngix = r"(*.?)\d{1}:\d{2}.\d{2}"
        #     # ren = re.compile(ngix)
        #     before = re.findall(ngix,"2359 shell        20   0  11M 2.5M 1.5M R 48.8   0.1   0:00.24 top -n 1")
        #     print(before)

        # line  = re.sub(r'\s+', ',', line)
        # line = line.split(',')

        # if n>4:
        #     print("*************")
        #     print(before)
        # for i in range(len(line)):
        #     print("*************")
        #     print(line[i],i)

    output_file.close()




if __name__ == "__main__":
    GetCpu()
    # ngix = r"(.*?)\d{1}:\d{2}.\d{2}"
    # text = "2359 shell        20   0  11M 2.5M 1.5M R 48.8   0.1   0:00.24 top -n 1"
    # before = re.findall(ngix, text)
    # after = re.findall(r'\d{1}:\d{2}.\d{2}(.*?)$',text)[0]  #"$"匹配到结尾
    # print(before)
    # print(after)