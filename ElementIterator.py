from Json import Json
# 定义元素。属性：名字及其包含的文本
class Element():
    def __init__(self,name,content):
        self.name=name
        self.content=content
    def accept(self,visitor:Json):
        pass
# 定义迭代器
class ElementIterator():
    def __init__(self,elements):
        self.elements=elements
        self.index=0
    def __iter__(self):
        return self
    def hasnext(self):
        return self.index<len(self.elements)
    def __next__(self):
        element=self.elements[self.index]
        self.index+=1
        return element
# 定义列表
class ElementList():
    def __init__(self):
        self.elements=[]
    def add_element(self,element:Element):
        self.elements.append(element)
    def get_interator(self):# 获取迭代器
        return ElementIterator(self.elements)
# 定义叶子节点元素
class LeafElement(Element):
    def __init__(self,name):
        self.name=name
# 定义中间节点元素
class CompositeElement(Element):
    def __init__(self,name,content):
        self.name=name
        self.content=[]
        if type(content) is dict:
            for contentname in content.keys():
                self.content.append(CompositeElement(contentname,content[contentname]))
        else:
            self.content=LeafElement(content)