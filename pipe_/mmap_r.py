import mmap

if __name__ == '__main__':
    import mmap
    import contextlib
    import time

    while True:
        with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_READ)) as m:
            s = m.read(1024).decode('utf-8')
            print(s)
        time.sleep(1)
