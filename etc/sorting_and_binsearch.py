# coding=utf-8

# 주어진 array 오름차순 정렬

def sortsubarr(arr, sp, ep):
    print arr,"/", sp,"/", ep
    if (ep - sp) <= 0:
        return

    elif (ep-sp) == 1:
        if arr[sp] < arr[ep]:
            return
        else:
            tmp = arr[sp]
            arr[sp] = arr[ep]
            arr[ep] = tmp

    else:
        pivot = sp
        end = ep
        sp += 1
        while sp < ep:
            if arr[sp] < arr[pivot]:
                sp += 1
            else:
                if arr[ep] > arr[pivot]:
                    ep -= 1
                else:
                    tmp = arr[ep]
                    arr[ep] = arr[sp]
                    arr[sp] = tmp

        if arr[pivot] > arr[sp]:
            tmp = arr[pivot]
            arr[pivot] = arr[sp]
            arr[sp] = tmp

        sortsubarr(arr, pivot, sp - 1)
        sortsubarr(arr, sp + 1, end)


def mysort(arr, nArraySize):
    sp = 0
    ep = nArraySize - 1
    sortsubarr(arr, sp, ep)
    return

# 해당 value 가 arr 안에 있으면 1 리턴, 없으면 0 리턴
def mybsearch(arr, value):
    ret = 0
    sp = 0              # start
    ep = len(arr) - 1   # end
    mp = (ep - sp) / 2  # middle

    while sp < ep:
        print sp,"/",mp,"/",ep,"/",arr[mp]
        if value == arr[mp]:
            ret = 1
            break
        elif value > arr[mp]:
            sp = mp + 1
            mp = (ep - sp) / 2
        else:
            ep = mp - 1
            mp = (ep - sp) / 2

    if arr[sp] == value:
        ret = 1

    return ret


def main():
    arr = [34, 1, 9, 2, 10, 11, 45, 100, 80 , 84 , 99]
    #arr = [5,4]
    #arr.sort()
    mysort(arr, len(arr))
    print arr
    i = mybsearch(arr, 2)

    print i

main()