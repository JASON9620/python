# -*- coding:utf-8 -*-
class Node(object):
    """创建一个节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node is not None:
            node.next = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """计算列表长度"""
        if self.__head is None:
            count = 0
        else:
            count = 1
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next
        return count

    def travel(self):
        """遍历该列表"""
        if self.__head is None:
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            #手动打印链表末尾节点的elem
            print(cur.elem)

    def append(self, item):
        """增加新的元素（尾插法）"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def add(self, item):
        """头插法"""
        node=Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            self.__head = node
            cur = node.next
            while cur.next != node.next:
                cur = cur.next
            cur.next = node
            """cur.next可以替换另一个指向，也可以指向节点
            例cur.next = self.__head
              cur.next = node"""



    def insert(self, pos, item):
        """在指定位置上添加元素
        prades: pos=0开始取"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            count=0
            node=Node(item)
            cur=self.__head
            while count != pos-1:
                count += 1
                cur=cur.next
            node.next = cur.next
            cur.next = node

    def search(self, num):
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == num:
                return True
            else:
                cur = cur.next
        if cur.elem == num:
            return True
        return False


    def remove(self, num):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == num:
                if cur == self.__head:
                    self.__head == cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next







if __name__ == "__main__":
    li = SingleLinkList()
    print(li.is_empty())
    li.append(1)
    li.append(2)
    li.append(3)
    li.add(4)
    li.add(5)
    li.travel()
    li.insert(4,5)
    li.travel()
    print(li.search(6))
    # li.remove(3)
    # li.travel()


