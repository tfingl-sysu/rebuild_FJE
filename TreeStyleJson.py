from ElementIterator import *
from Json import *
from Icon import *
from TreeComponent import *
# 树形Json，内部含有icon的建造和组合print
class TreeStyleJson(Json):
    def __init__(self):
        self.icon=None
    def build_icon(self,icon):
        self.icon=Icon().setIcon(icon)
    # 建立根
    def build_tree(self,iterator:ElementIterator):
        keys=iter(iterator)
        # 先遍历可以暂时排除最后一个节点
        key=next(keys)
        while keys.hasnext():
            # 子树不是叶子节点
            if type(key.content) is list:
                root=TreeComposite(key.name)
                self.build_subtree(root,key.content)
            # 子树是叶子节点
            else:
                # 非空
                if key.content.name!=None:
                    root=TreeComposite(key.name+": "+key.content.name)
                # 空值
                else:
                    root=TreeComposite(key.name)
            root.print_tree([False],self.icon)
            key=next(keys)
        # 最后一个节点key
        # 子树不是叶子节点
        if type(key.content) is list:
            root=TreeComposite(key.name)
            self.build_subtree(root,key.content)
        # 子树是叶子节点
        else:
            # 非空
            if key.content.name!=None:
                root=TreeComposite(key.name+": "+key.content.name)
            # 空值
            else:
                root=TreeComposite(key.name)
        root.print_tree([True],self.icon)
    # 建立子树
    def build_subtree(self,parent,children):
        for key in children:
            # content是列表说明要充当新的根节点
            if type(key.content) is list:
                root=TreeComposite(key.name)
                self.build_subtree(root,key.content)
                parent.add(root)
            # content是叶子节点，与该根节点共同做叶子
            else:
                # 非空
                if key.content.name!=None:
                    leaf=TreeLeaf(key.name+": "+key.content.name)
                # 空值
                else:
                    leaf=TreeLeaf(key.name)
                parent.add(leaf)
                