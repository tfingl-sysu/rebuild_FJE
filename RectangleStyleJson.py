from Json import *
from Icon import *
from RectangleComponent import *
from ElementIterator import *
# 全局变量获取输出最长的长度以规整矩形
maxlen=0
# 树形Json，内部含有icon的建造和组合print
class RectangleStyleJson(Json):
    def __init__(self):
        self.icon=None
    # 建立icon
    def build_icon(self,icon):
        self.icon=Icon().setIcon(icon)
    # 建立根
    def build_tree(self,iterator:ElementIterator):
        global maxlen
        # keys=list(json_data.keys())
        keys=iter(iterator)
        # 第一个节点
        key=next(keys)
        # 子树不是叶子节点
        if type(key.content) is list:
            root=RectangleComposite(key.name)
            length=len(key.name)
            if length>maxlen:
                maxlen=length
            self.build_subtree(root,key.content,2)
        # 子树是叶子节点
        else:
            # 非空
            if key.content.name!=None:
                newname=key.name+": "+key.content.name
                root=RectangleComposite(newname)
                length=len(newname)
                if length>maxlen:
                    maxlen=length
            # 空值
            else:
                root=RectangleComposite(key.name)
                length=len(key.name)
                if length>maxlen:
                    maxlen=length
        # 1标记起始行
        root.print_tree(1,self.icon,maxlen)
        # 第二个节点，放在这里排除最后一个节点，如果没有下一个节点需要提前返回
        if not keys.hasnext():
            return None
        key=next(keys)
        while keys.hasnext():
            # 子树不是叶子节点
            if type(key.content) is list: 
                root=RectangleComposite(key.name)
                length=len(key.name)
                if length>maxlen:
                    maxlen=length
                self.build_subtree(root,key.content,2)
            # 子树是叶子节点
            else:
                # 非空
                if key.content.name!=None:
                    newname=key.name+": "+key.content.name
                    root=RectangleComposite(newname)
                    length=len(newname)
                    if length>maxlen:
                        maxlen=length
                # 空值
                else:
                    root=RectangleComposite(key.name)
                    length=len(key.name)
                    if length>maxlen:
                        maxlen=length
            # 0标记中间行
            root.print_tree(0,self.icon,maxlen) 
            key=next(keys)
        # 最后一个节点
        # 子树不是叶子节点
        if type(key.content) is list:
            root=RectangleComposite(key.name)
            length=len(key.name)
            if length>maxlen:
                maxlen=length
            self.build_subtree(root,key.content,2)
        # 子树是叶子节点
        else:
            # 非空
            if key.content.name!=None:
                newname=key.name+": "+key.content.name
                root=RectangleComposite(newname)
                length=len(newname)
                if length>maxlen:
                    maxlen=length
            # 空值
            else:
                root=RectangleComposite(key.name)
                length=len(key.name)
                if length>maxlen:
                    maxlen=length
        # -1标记最后一行
        root.print_tree(-1,self.icon,maxlen)
    # 建立子树
    def build_subtree(self,parent,children,depth):
        global maxlen
        for key in children:
            # content是列表说明要充当新的根节点
            if type(key.content) is list:
                root=RectangleComposite(key.name)
                self.build_subtree(root,key.content,depth+1)
                parent.add(root)
            # content是叶子节点，与该根节点共同做叶子
            else:
                 # 非空
                if key.content.name!=None:
                    newname=key.name+": "+key.content.name
                    leaf=RectangleLeaf(newname)
                    length=len(newname)+3*depth
                    if length>maxlen:
                        maxlen=length
                # 空值
                else:
                    leaf=RectangleLeaf(key.name)
                    length=len(key.name)+3*depth
                    if length>maxlen:
                        maxlen=length
                parent.add(leaf)            