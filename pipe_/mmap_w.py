import mmap
from multiprocessing import Process
import contextlib
import time



###　文件的话，可以先结束内存
###  只写在内存的话，两个程序都必须在运行

def modify(buf):
    buf[0:100]=b"5"*100



def write():
    # with contextlib.closing(mmap.mmap(-1, 4 * 200, tagname='sharemem', access=mmap.ACCESS_READ)) as m:
    #     s = m.readline()
    #     print(s.decode('utf-8'))

    with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_WRITE)) as m:
        m.seek(0)
        # print("msg".encode('utf-8'))
        m.write("msg".encode('utf-8'))
        m.flush()
        time.sleep(1)

def read():

    # mmap_file = mmap.mmap(-1, 4 * 200, access=mmap.ACCESS_WRITE, tagname='sharemem')
    # mmap_file.write('ddsdddd'.encode('utf-8'))
    with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_READ)) as m:
        s = m.read(1024).decode('utf-8')
        print(s)
    time.sleep(1)


def write_file():
    with open("test.dat", "w") as f:
        f.write('\x00' * 1024)
    with open('test.dat', 'r+') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_WRITE)) as m:
            for i in range(1, 10):
                m.seek(0)
                s = ("msg " + str(i))
                s.rjust(1024, '\x00')
                m.write(s.encode('utf-8'))
                m.flush()
                time.sleep(1)

def read_file():
    import mmap
    import contextlib
    import time


    with open('test.dat', 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_READ)) as m:
            s = m.read(1024).decode('utf-8')
            print(s)
    time.sleep(1)


if __name__ == '__main__':
    # import mmap
    # import contextlib

    # write()
    # read()
    # pw=Process(target=write(),args=())
    # pw.start()
    # pw.join()
    # pw.terminate()
    # read()
    # with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_WRITE)) as m:
    #     for i in range(1, 10001):
    #         m.seek(0)
    #         m.write(("msg " + str(i)).encode('utf-8'))
    #         m.flush()
    #         time.sleep(1)
    # write_file()
    read_file()