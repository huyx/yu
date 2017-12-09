# pYthon Utilities

安装

```
$ pip install yu
```

## extractors - 数据提取

数据提取，支持:

* Field
  * SkipField - 直接跳过
  * PassField - 不做转换
  * StringField - 字符串，支持长度验证
  * IntegerField - 整数，支持最大、最小值验证
  * FloatField - 浮点数
  * DateField - 日期
* RowExtractor
* CSVExtractor

### 示例

CSVExtractor 用法:

```python
import csv
from yu.extractors import csv as ce


fields = [
    ce.StringField(min_length=2, max_length=4),  # 姓名
    ce.SkipField(),  # 民族
    ce.IntegerField(max_value=150),  # 年龄
    ce.FloatField(min_value=5, max_value=200),  # 体重
    ce.DateField(),  # 生日
    ce.PassField(),  # 备注
]


with open('persons.csv') as fp:
    reader = csv.reader(fp)
    extractor = ce.CSVExtractor(reader, fields=fields)
    for row in extractor:
        print(row)
```

## utils - 其他工具

包括

* cached_property - 代码来自 Django 项目
* InstanceMeta - 类的自动实例化
* Instance - 类的自动实例化（继承方式）

### InstanceMeta 示例

```python
from yu.utils import InstanceMeta

class Color(metaclass=InstanceMeta, abstract=True):
    def __str__(self):
        return f'{self.name} = {self.value}'

class Red(Color):
    name = 'red'
    value = 'FF0000'

class Green(Color):
    name = 'green'
    value = '00FF00'

print(Red)
print(Green)
```
