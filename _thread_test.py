import _thread
import logging
from time import sleep, ctime
# 日志初始化，并设设置日志的输出等级为Info级别，这样的话所有的info级别的日志都会打印和输出
logging.basicConfig(level=logging.INFO)
loops = [2, 4]


# 传入三个参数，线程号标识当前是第几个loop，线程执行时间，和锁
#
def loop(nloop, nsec, lock):
    # 信息写入(线程的启动和结束)
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())
    # 释放锁
    lock.release()


def main():
    logging.info("start at all" + ctime())
    # 锁的list，他可以包含非常多的锁，我们把每一个线程都传一个锁进来，这样的话locks就包含所有的锁。
    locks = []
    nloops = range(len(loops))
    # nloop中有两个值，上两次锁
    for i in nloops:
        # 声明一个锁
        lock = _thread.allocate_lock()
        # 进行加锁
        lock.acquire()
        # 追加到locks中，这样的话locks中就有所以的锁
        locks.append(lock)
        # 不能获取锁之后直接起子线程，因为获取锁需要时间，有可能在获取锁的时候子线程就已经执行完毕了，然后就会退出
        # _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 起子线程
    for i in nloops:
        # 开启子线程，函数加函数三个参数
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 对locks中的锁进行频繁检测，如果发现locks中的锁都被释放了，main函数就退出。
    for i in nloops:
        # 判断锁是不是锁上的状态，如果是锁上的状态，会无限死循环，已经释放锁的话，会退出死循环（从而完成前面的操作等待每个线程结束，才会退出主线程）
        while locks[i].locked(): pass 

    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
