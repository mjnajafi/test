########################### Dictionary In Python#######################
Dic = {1:"one",2:"two",3:"three"}
print(Dic)

T1 = (19,20,16,14)
math,physics,arabic,english = T1


Scores = {"math":19,"physics":20,"arabic":16}
Scores["arabic"]
Scores[15]

>>> Scores[1:3]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Scores[1:3]
TypeError: unhashable type: 'slice'
>>> Dic2 = {}
>>> Dic2["first"] = "one"
>>> print(Dic2)
{'first': 'one'}
>>> Dic2["second"] = "two"
>>> Dic2
{'second': 'two', 'first': 'one'}
>>> Dic2["third"] ="three"
>>> print(Dic2)
{'third': 'three', 'second': 'two', 'first': 'one'}
>>> Dict = {(1,2):"S1",(3,6):45,"f":12,34:56}
>>> print(Dict)
{(1, 2): 'S1', 34: 56, 'f': 12, (3, 6): 45}
>>> Dict[(1,2)]
'S1'
>>> Dict[(3,6)]
45
>>> Dict[1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Dict[1]
KeyError: 1
>>> Dict[(1)]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Dict[(1)]
KeyError: 1
>>> Dict1 = {(1,2):"S1",(3,6):45,"f":12,(1,2):"ss",34:56,"f":"hi!"}
>>> Dict1[(1,2)]
'ss'
>>> Dict1["f"]
'hi!'
>>> print(Dic2)
{'third': 'three', 'second': 'two', 'first': 'one'}
>>> Dic2["second"] = "four"
>>> Dic2
{'third': 'three', 'second': 'four', 'first': 'one'}
>>> DD1 = {1:"s",3:"gh",6:"rt"}
>>> DD2 = {2:"fg",5:78}
>>> DD1 = DD1 + DD2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    DD1 = DD1 + DD2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> DD1[2] = "fg"
>>> DD1
{1: 's', 2: 'fg', 3: 'gh', 6: 'rt'}
>>> DD1*3
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    DD1*3
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> del DD1
>>> print(DD1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(DD1)
NameError: name 'DD1' is not defined
>>> Length = len(DD2)
>>> print(Length)
2
>>> Dict1 = {(1,2):"S1",(3,6):45,"f":12,(1,2):"ss",34:56,"f":"hi!"}
>>> (1,2) in Dict1
True
>>> "S1" in Dict1
False
>>> "S1" not in Dict1
True
>>> Dict2 = {(1,2):"S1",(3,6):45,"f":12,,34:56}
SyntaxError: invalid syntax
>>> Dict2 = {(1,2):"S1",(3,6):45,"f":12,34:56}
>>> Dict1 == Dict2
False
>>> Dict1 != Dict2
True
>>> Dict1 =! Dict2
SyntaxError: invalid syntax
>>> seasons = {"first":"spring","second":"summer","third":"fall","fourth":"winter"}
>>> len(seasons)
4
>>> seasons.copy()
{'third': 'fall', 'second': 'summer', 'fourth': 'winter', 'first': 'spring'}
>>> seasons.clear()
>>> print(seasons)
{}
>>> seasons.has_key("first")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    seasons.has_key("first")
AttributeError: 'dict' object has no attribute 'has_key'
>>> seasons.keys()
dict_keys([])
>>> seasons = {"first":"spring","second":"summer","third":"fall","fourth":"winter"}
>>> seasons.keys()
dict_keys(['third', 'fourth', 'second', 'first'])
>>> seasons.values()
dict_values(['fall', 'winter', 'summer', 'spring'])
>>> seasons.items()
dict_items([('third', 'fall'), ('fourth', 'winter'), ('second', 'summer'), ('first', 'spring')])
>>> mat = [[0,0,1,2],[1,0,3,4]]
>>> matrix = {(0,0):0,(0,1):0,(0,2):1,(0,3):2,(1,0):1,(1,1):0,(1,2):3,(1,3):4}
>>> len(matrix)
8
>>> matrix[(1,1)]
0
>>> matrix[(1,2)]
3
>>> mat1 = [[0,0,0,0,1],[0,2,0,0,0],[0,0,0,1,0]]
>>> matrix1 = {(0,4):1,(1,1):2,(2,3):1}
>>> len(matrix1)
3
>>> matrix1[(1,1)]
2
>>> matrix1[(2,2)]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    matrix1[(2,2)]
KeyError: (2, 2)
>>> matrix1.get((2,2),0)
0
>>> matrix1[(2,2)]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    matrix1[(2,2)]
KeyError: (2, 2)
>>> matrix1[(2,3)]
1
>>> matrix1.get((2,3),0)
1
>>> matrix1.get((2,2),3)
3
>>> scores = {"m":17,"ph":15,"a":18}
>>> len(scores)
3
>>> scores1 = scores.copy()
>>> print(scores1)
{'a': 18, 'ph': 15, 'm': 17}
>>> scores2 = scores
>>> print(scores2)
{'a': 18, 'ph': 15, 'm': 17}
>>> scores["a"] = 19
>>> print(scores)
{'a': 19, 'ph': 15, 'm': 17}
>>> print(scores1)
{'a': 18, 'ph': 15, 'm': 17}
>>> print(scores2)
{'a': 19, 'ph': 15, 'm': 17}
>>> scores["m"] = 11
>>> scores
{'a': 19, 'ph': 15, 'm': 11}
>>> scores2
{'a': 19, 'ph': 15, 'm': 11}
>>> scores1
{'a': 18, 'ph': 15, 'm': 17}
>>> 
