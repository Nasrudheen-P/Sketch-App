def findIndex(arr,p):
    for i,j in enumerate(arr):
        if j==p or j>p:
            return i
    return len(arr)


if __name__ == '__main__':
    str = input()[1:-1].split(',')
    try:
        arr = [int(num) for num in str]
        p = int(input())
        arr.sort()
        index = findIndex(arr,p)
        print(index)
    except Exception as ex:
        print(ex)