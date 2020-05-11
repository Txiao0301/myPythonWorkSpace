import json

# json字符串和dict list的转换
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(data)
print(type(list_data))
print(list_data)

list2 = [{"name": "张三", "age": 20}, {"name": "李四", "age": 18}]
data_json = json.dumps(list2)
print(type(data_json))
print(data_json)

# 文件对象和dict list的转换
json.dump(list2, open('json_demo_01.json', 'w'))

json_result = json.load(open('json_demo_01.json', 'r'))
print(type(json_result))
print(json_result)
