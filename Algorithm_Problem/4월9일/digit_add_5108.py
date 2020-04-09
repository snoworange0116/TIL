# sw expert linkedlist 5108 숫자추가

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None #첫 번째 노드
        self.tail = None # 마지막 노드
        self.size = 0 # 노드의 수
    def printList(self):
        if self.head is None:
            return
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ')
                cur = cur.next

    def insertLast(self, new): # new: 새로추가할 노드 객체
        # 빈 리스트일 경우
        if self.head is None:
            self.head = self.tail = new
        else:
            #빈리스트 아닐경우, 마지막 노드를 찾는다.
            # cur = lst.head
            # while cur.next is not None:
            #     cur = cur.next
            # cur.next = new
            self.tail.next = new
            self.tail = new
        self.size += 1

    def deleteLast(self):
        if self.head is None: return
        pre, cur = None, self.head
        while cur.next is not None:
            pre = cur
            cur = cur.next
        if pre is None:
            self.head = self.tail = None
        else:
            pre.next = None
            self.tail = pre
        self.size -= 1
        return cur.data

    def insertFirst(self, new):
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head = new
        self.size += 1

    def deleteFirst(self):
        if self.size == 0: return # if lst.head is None: return과 같다

        self.head = self.head.next
        if self.head is None:
            self.head = self.tail = None

        self.size -= 1

    def insertAt(self, idx, new): #idx는 인덱스 값
        # 빈 리스트일 경우, idx == 0
        if self.head is None or idx == 0:
            self.insertFirst(new)
        elif idx >= self.size:
            self.insertLast(new)
        else:
            pre,cur = None, self.head
            for _ in range(idx):
                pre = cur
                cur = cur.next
            new.next = cur
            pre.next = new
            self.size += 1
    # 마지막 추가하는 경우 idx >= lst.size
    # 중간에 추가하는 경우
    def get(self,idx):
        if idx >= self.size:
            print("Error: Index out of Range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_idx == idx:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1
# deleteAt 만들어보기

t = int(input())
for tc in range(1, t+1):
    n,m,l = map(int,input().split())
    mylist = LinkedList()
    numbers = list(map(int,input().split()))
    for number in numbers:
        mylist.insertLast(Node(number))
    for _ in range(m):
        idx, num = map(int,input().split())
        mylist.insertAt(idx, Node(num))
    # mylist.printList()
    print('#{} {}'.format(tc, mylist.get(l)))