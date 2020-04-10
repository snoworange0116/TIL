# from collections import deque
#
# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int,(input().split())) #수열의 길이, 수열의 개수
#     arr = [list(map(int,input().split())) for i in range(m)]
#     arr = deque(arr)
#     # print(arr)
#     result = arr.popleft()
#     # print(result)
#     while arr:
#         tmp = deque(arr.popleft())
#         first = tmp[0]
#         idx = 0
#         for i in result:
#             if i > first:
#                 break
#             else:
#                 idx += 1
#         while tmp:
#             result.insert(idx,(tmp.pop()))
#     rev_result = result[::-1]
#     print('#{} {}'.format(tc, ' '.join(map(str,rev_result[:10:]))))
# 위는 시간오류 뜬 코드

class Node:
    def __init__(self,d=0,p=None,n=None):
        self.data = d
        self.prev = p
        self.next = n
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def addList(self,arr):
        # if self.head is None:
        #     self.head = self.tail = new
        # else:
        #     new.prev = self.tail # 새로 추가되는 노드를 우선적으로 바꾸는게 중요
        #     self.tail.next = new
        #     self.tail = new
        # self.size += 1
        first = last = Node(arr[0])
        for val in arr[1:]:
            new = Node(val,last)
            last.next = new
            last = new
        if self.head is None:
            self.head = first
            self.tail = last
        else:
            cur = self.head
            while cur is not None:
                if cur.data > arr[0]: break
                cur = cur.next
            if cur is None: # 마지막에 추가
                first.prev = self.tail
                self.tail.next = first
                self.tail = last
            elif cur.prev is None: # 처음 추가
                last.next = self.head
                self.head.prev = last
                self.head = first
            else: # 중간
                prev = cur.prev
                first.prev = prev
                last.next = cur
                prev.next = first
                cur.prev = last
        self.size += len(arr)

    def printList(self):
        if self.head is None: return
        cur = self.head
        while cur is not None:
            print(cur.data, end = ' ')
            cur = cur.next
        print()
        #역방향
        # cur = self.tail
        # while cur is not None:
        #     print(cur.data, end = ' ')
        #     cur = cur.prev
    def toString(self):
        result = []
        if self.head is None : return
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        result = result[::-1]
        return result[:10]

t= int(input())
for tc in range(1,t+1):
    mylist = LinkedList()
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(m)]
    # print(arr)
    while arr:
        tmp = arr.pop(0)
        mylist.addList(tmp)
    print('#{}'.format(tc),end = ' ')
    print(*(mylist.toString()))