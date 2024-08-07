import os


def getallfilesindir(dir):
    if os.path.isdir(dir) is False:
        return False
    count = 0
    for root, dirs,files in os.walk(dir):
        for i in files:
            print(i)
            count = count + 1

    return count


def quicksort(array):
    less =[]
    more =[]
    mid = []
    if len(array) <=1:
        return array

    m_item = array[0]
    mid.append(m_item)

    for i in range(1, len(array)):
        if array[i] > m_item:
            more.append(array[i])

        if array[i] == m_item:
            mid.append(array[i])

        if array[i] < m_item:
            less.append(array[i])

    return quicksort(less) + mid + quicksort(more)


def bubble_sort(array):
    print('bubble_sort')
    for i in range(0, len(array)):
        print('i: ' + str(i))
        for j in range(i+1, len(array)):
            print('j: ' +str(j))
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


def bubble_sort2(array):
    temp = 0
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) -1 -i):
            if array[j] > array[j + 1]:
                temp = array[j+1]
                array[j + 1] = array[j]
                array[j] = temp

    return array

#找出字符串中出现次数最多的字符串和第一次出现的位置
def findthestr(s):



if __name__ == '__main__':
    dir = r'c:\Users\ADMIN\.pylint.d'
    string = 'sdfeislxckvcsdfeeed'
    print(getallfilesindir(dir))
    array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    print(quicksort(array))
    print(bubble_sort2(array))
