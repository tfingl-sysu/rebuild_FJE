from TreeStyleJson import *
from RectangleStyleJson import *
# 抽象工厂，创建树形类工厂和矩形类工厂
class AbstractFactory:
    def createfactory(self,style):
        if style=='tree':
            factory=TreeStyleFactory()
            return factory
        elif style=='rectangle':
            factory=RectangleStyleFactory()
            return factory
        else:
            print('error!')
    def create(self,icon):
        pass
# 树形类工厂，创建树形Json
class TreeStyleFactory(AbstractFactory):
    def create(self,icon):
        style=TreeStyleJson()
        style.build_icon(icon)
        return style
# 矩形类工厂，创建矩形Json
class RectangleStyleFactory(AbstractFactory):
    def create(self,icon):
        style=RectangleStyleJson()
        style.build_icon(icon)
        return style