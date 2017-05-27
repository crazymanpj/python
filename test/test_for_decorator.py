from time import ctime,sleep

def tsfunc(func):
    def wrapfunc(*args, **kwargs):
        print('[%s] %s() called'%(ctime(),func.__name__))
        return func(*args, **kwargs)
    return wrapfunc

def tsfunc2(func):
    print('[%s] %s() called'%(ctime(),func.__name__))
    return func()

@tsfunc
def foo(x,d):
    return 1


foo(1,2)
