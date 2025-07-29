list = [1, 2, 3, 7, 11, 13, 16, 20, 21, 33, 34, 38, 40, 41, 50]
target = 3
newlist = []


def binarySearch(list, target, newlist):
    start = 0
    end = len(list) - 1
    mid = (start + end) // 2

    # Bulunursa
    if target == list[mid]:
        print("Hedef bulundu!")
        return True

    # Listenin ortası hedeften büyükse küçükleri yok say
    elif target > list[mid]:
        headOfList = mid
        while headOfList < len(list) - 1:
            headOfList = headOfList + 1
            newlist.append(list[headOfList])
        print(newlist)
        return binarySearch(newlist, target, [])

    # Listenin ortası hedeften küçükse büyükleri yok say
    elif target < list[mid]:
        headOfList = 0
        while headOfList < mid:
            newlist.append(list[headOfList])
            headOfList = headOfList + 1
        print(newlist)
        return (newlist, target, [])

while True:
    if binarySearch(list, target, newlist):
        break
