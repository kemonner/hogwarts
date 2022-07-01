import _thread
import threading
import logging
from time import sleep, ctime
# 日志初始化，并设设置日志的输出等级为Info级别，这样的话所有的info级别的日志都会打印和输出
logging.basicConfig(level=logging.INFO)
loops = [2, 4]


# 传入三个参数，线程号标识当前是第几个loop，线程执行时间，和锁
#
def loop(nloop, nsec):
    # 信息写入(线程的启动和结束)
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())


def main():
    logging.info("start at all" + ctime())
    threads = []
    nloops = range(len(loops))
    # 起子线程
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        # 每生成一个新的线程，就追加到List中
        threads.append(t)
    for i in nloops:
        # 新的循环中进行调用(调用后执行loop函数)
        threads[i].start()
    for i in nloops:
        # 去等，比如等thread0是不是结束，如果没有结束，它就会阻塞，卡在这里，把main阻塞在这里，如果发现thread0执行完毕，就会解除阻塞
        threads[i].join()

    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()