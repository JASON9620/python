# -*- coding:utf-8 -*-
class Node(object):
    """创建一个节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def append(self, item):
        """增加新的元素（尾插法）"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        """头插法"""
        node=Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

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


    def length(self):
        """计算列表长度"""
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历该列表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

    def search(self, num):
        """寻找某一元素是否在列表中"""
        cur = self.__head
        while cur is not None:
            if cur.elem == num:
                return True
            else:
                cur = cur.next
        return False


    def remove(self, num):
        """从列表中删除指定元素，
        当含有多个相同元素时，删除第一个元素"""
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
    # li.travel()
    li.insert(4,5)
    li.travel()
    print(li.search(3))
    li.remove(3)
    li.travel()
