from Icon import *
# 组合模式建立树形结构
class TreeComponent:
    def add(self,child):
        pass
    def remove(self,child):
        pass
    def print_tree(self,endflag,icon,depth=0):
        pass
# 叶子节点
class TreeLeaf(TreeComponent):
    def __init__(self,name):
        self.name=name
    def print_tree(self,endflag,icon,depth=0):
        for i in range(depth):
            # 如果已经是最后一个叶子，那么前面会打印└─不需要再打印│衔接
            if endflag[i]:
                print('   ',end='')
            # 如果这个不是最后一个叶子就需要打印│衔接前面
            else:
                print('\u2502  ',end='')
        # 如果是最后一个叶子要打印出└─衔接前面并终结
        if endflag[-1]:
            print('\u2514\u2500',end='')
        # 否则打印├─衔接前后
        else:
            print('\u251c\u2500',end='')
        # 打印icon叶子节点对应标识
        icon.print_leaf()
        print(self.name)
# 组合节点
class TreeComposite(TreeComponent):
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add(self,child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)
    def print_tree(self,endflag,icon,depth=0):
        for i in range(depth):
            # 如果已经是最后一个子树，那么前面会打印└─不需要再打印│衔接
            if endflag[i]:
                print('   ',end='')
            # 如果这个不是最后一个子树就需要打印│衔接前面
            else:
                print('\u2502  ',end='')
        # 如果是最后一个叶子要打印出└─衔接前面并终结
        if endflag[-1]:
            print('\u2514\u2500',end='')
        # 否则打印├─衔接前后
        else:
            print('\u251c\u2500',end='')
        # 打印icon的中间结点对应标识
        icon.print_node()
        print(self.name)
        size=len(self.children)
        endflag.append(False)
        # 先打印非最后子树，传入终结信号为False
        for i in range(size-1):
            self.children[i].print_tree(endflag,icon,depth+1)
        # 最后子树将终结信号改为True
        endflag.pop()
        endflag.append(True)
        # 防止空子树错误
        if size:
            self.children[-1].print_tree(endflag,icon,depth+1)
        endflag.pop()