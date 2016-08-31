import  datetime
def is_day(num):
    wday = int(datetime.datetime.now().strftime('%w'))
    print wday
    if wday == int(num):
        return True
    else:
        return False
    
    