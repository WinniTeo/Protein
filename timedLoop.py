import time 
for in expression_list:
    pass

    sched_time = datetime.datetime(2017, 8, 10, 17, 31, 0)
    loopflag = 0
    while True:
        now = datetime.datetime.now()
        if sched_time<now<(sched_time+datetime.timedelta(seconds=1)):
            loopflag = 1
            time.sleep(1)
        if loopflag == 1:
            func() #此处为你自己想定时执行的功能函数
            loopflag = 0