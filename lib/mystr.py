# encoding: UTF-8
# Date:    2018-05-14
# Author:  pangjian

import chardet

def getstrencodingtype(str):
    encode = chardet.detect(str)
    return encode['encoding']


if __name__ == '__main__':
    pass
