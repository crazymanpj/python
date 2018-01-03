# encoding: UTF-8
# Date:    2017-12-14
# Author:  pangjian

from decimal import *


def float_decimal2(num, fh=False):
    if fh == True:
        return "%+.2f"%(num)
    else:
        return round(num ,2)

def float_to_decimal(f):
    "Convert a floating point number to a Decimal with no loss of information"
    n, d = f.as_integer_ratio()
    numerator, denominator = Decimal(n), Decimal(d)
    ctx = Context(prec=60)
    result = ctx.divide(numerator, denominator)
    while ctx.flags[Inexact]:
        ctx.flags[Inexact] = False
        ctx.prec *= 2
        result = ctx.divide(numerator, denominator)
    return result

def format_number_ab(num, fh=False, dc='0'):
    absdata = abs(num)
    if fh == False:
        if int(absdata) < 10000:
            num = float(num) / float(1000)
            num = float_to_decimal(num).quantize(Decimal(dc))
            return '%sk' % (num)

        elif int(absdata) >= 10000:
            num = float(num) / float(10000)
            num = float_to_decimal(num).quantize(Decimal(dc))
            return '%sw' % (num)

    else:
        if int(absdata) < 10000:
            num = float(num) / float(1000)
            num = float_to_decimal(num).quantize(Decimal(dc))
            return '%+.1fk' % (num)

        elif int(absdata) >= 10000:
            num = float(num) / float(10000)
            num = float_to_decimal(num).quantize(Decimal(dc))
            return '%+.1fw' % (num)


def getrate_str(week_d, basecount, fh=True):
    if fh == True:
        return "%+.2f" % (float(week_d) / float(basecount) * 100)
    else:
        return "%.2f" % (float(week_d) / float(basecount) * 100)


def getrate_float(week_d, basecount):
    temp = float(week_d) / float(basecount) * 100
    return float('%.2f' % temp)


if __name__ == '__main__':
    print type(round(-2.3344333, 2))
    print round(-2.3344333, 2)
    print getrate_float(2.5, 10)