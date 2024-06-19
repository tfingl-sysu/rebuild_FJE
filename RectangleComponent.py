from Icon import *
# 组合模式建立矩形结构
class RectangleComponent:
    def add(self,child):
        pass
    def remove(self,child):
        pass
    def print_tree(self,lineflag,icon,maxlen,depth=0):
        pass
# 叶子节点
class RectangleLeaf(RectangleComponent):
    def __init__(self,name):
        self.name=name
    def print_tree(self,lineflag,icon,maxlen,depth=0):
        startflag=True
        for _ in range(depth):
            # 整个矩形的最后一行(因为是叶子节点),第一个打印└──与后面和上面衔接
            if lineflag==-1 and startflag:
                print('\u2514\u2500\u2500',end='')
                startflag=False
            # 整个矩形的最后一行(因为是叶子节点),剩下的打印┴──与前后和上面衔接
            elif lineflag==-1:
                print('\u2534\u2500\u2500',end='')
            # 不是最后一行也不可能是第一行(因为是叶子节点),打印│衔接上下
            else:
                print('\u2502  ',end='')
        # 整个矩形的最后一行(因为是叶子节点),第一个打印└─与上面衔接,引出后面内容
        if lineflag==-1 and startflag:
            print('\u2514\u2500',end='')
            startflag=False
        # 整个矩形的最后一行(因为是叶子节点)但不是开头,打印┴─与前面和上面衔接,引出后面内容
        elif lineflag==-1:
            print('\u2534\u2500',end='')
        # 不是最后一行也不可能是第一行(因为是叶子节点),打印├─衔接上下,引出后面内容
        else:
            print('\u251c\u2500',end='')
        # 打印icon叶子节点对应标识
        icon.print_leaf()
        print(self.name,end='')
        length=(depth+1)*3+len(self.name)
        # 补齐长度,打印─
        while length<maxlen+4:
            print('\u2500',end='')
            length+=1
        # 最后一行最后一个打印┘
        if lineflag==-1:
            print('\u2518')
        # 否则打印┤(因为不是第一行)
        else:
            print('\u2524')
# 组合节点
class RectangleComposite(RectangleComponent):
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add(self,child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)
    def print_tree(self,lineflag,icon,maxlen,depth=0):
        size=len(self.children)
        startflag=True
        for _ in range(depth):
            # 有子树,说明不会是最后1行;无子树但传进来标识不是最后一行.以上两种情况打印│
            if size or lineflag!=-1:
                print('\u2502  ',end='')
            # 否则说明这就是最后一行,开头打印└──
            elif startflag:
                print('\u2514\u2500\u2500',end='')
                startflag=False
            # 不是最后一行的开头打印┴──
            else:
                print('\u2534\u2500\u2500',end='')
        # 第1行的打印┌─(不考虑是不是第一个,因为第一行一定是第一个)
        if lineflag==1:
            print('\u250c\u2500',end='')
        # 没有子树加上最后一行的标识说明这是最后一行
        elif lineflag==-1 and size==0:
            # 开头打印└─
            if startflag:
                print('\u2514\u2500',end='')
                startflag=False
            # 否则打印┴─
            else:
                print('\u2534\u2500',end='')
        # 中间行,打印├─
        else:
            print('\u251c\u2500',end='')
        # 打印icon中间节点对应标识
        icon.print_node()
        print(self.name,end='')
        length=(depth+1)*3+len(self.name)
        # 补齐长度,打印─
        while length<maxlen+4:
            print('\u2500',end='')
            length+=1
        # 第一行末尾打印┐
        if lineflag==1:
            print('\u2510')
        # 最后一行标识且无子树说明是最后一行,末尾打印┘
        elif lineflag==-1 and size==0:
            print('\u2518')
        # 中间行末尾打印┤
        else:
            print('\u2524')
        # 非最后一个子树作为中间行处理
        for i in range(size-1):
            self.children[i].print_tree(0,icon,maxlen,depth+1)
        # 防止空子树错误
        if size:
            # 有最后一行标识，给子树传入最后一行标识
            if lineflag==-1:
                self.children[-1].print_tree(lineflag,icon,maxlen,depth+1)
            # 无最后一行标识，给子树传入中间行标识
            else:
                self.children[-1].print_tree(0,icon,maxlen,depth+1)