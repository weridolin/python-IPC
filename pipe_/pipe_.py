import time
import os
import subprocess


# read_pipe,write_pipe=os.pipe()


def child_pro(write_pipe):
    print('I am a child ,pid:{0}'.format(os.getpid()))

    while True:
        msg='child is sending msg'
        os.write(write_pipe,msg)
        time.sleep(1)



def parent_pro():
    read_pipe, write_pipe = os.pipe()
    pid=os.fork()  # 复制后 两个进程都连接一个OS.PIPE(),
    if pid==0:
        ###子进程只写
        os.close(read_pipe)
        child_pro(write_pipe=write_pipe)
        assert False
    else:
        ###　父进程只读
        os.close(write_pipe)
        print('parent is recive msg pid:{0}'.format(os.getpid()))
        file_obj=os.fdopen(read_pipe,"r")
        while True:
            recv=file_obj.readline()[:-1]
            print('rece msg:{0}'.format(recv))



def test():
    while True:
        print('test')
        time.sleep(3)

if __name__ == '__main__':
    # parent_pro()
    # subprocess.Popen(,shell=False,stdout=subprocess.PIPE,encoding='utf-8')
    pass
