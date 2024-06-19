import argparse
import json
from Factory import *
from ElementIterator import *
if __name__ == '__main__':
    # 创建参数解析器
    parser=argparse.ArgumentParser(description='这是一个简单的命令行工具示例')
    # 添加命令行参数
    parser.add_argument('-f','--filename')
    parser.add_argument('-s','--style',default='tree')
    parser.add_argument('-i','--icon_family',default='none')
    # 解析命令行参数
    args=parser.parse_args()
    # 处理命令行参数并输出结果
    # 读取JSON文件
    with open(args.filename) as f:
        json_data=json.load(f)
    # 创建工厂
    # factory=AbstractFactory().createfactory(args.style)
    # 获得成品
    # product=factory.create(args.icon_family)
    # 打印结果
    # product.build_tree(json_data)
    # 创建元素
    list=ElementList()
    for name in json_data.keys():
        list.add_element(CompositeElement(name,json_data[name]))
    iterator=list.get_interator()
    factory=AbstractFactory().createfactory(args.style)
    product=factory.create(args.icon_family)
    product.build_tree(iterator)