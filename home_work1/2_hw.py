def task_1(a,b,c,d,e)->None:
    return a+b
task_1 (5, 3.3, c='tester', d=[1,2,3,4], e=5<3)
a: int=5
b: float=3.3
c: str='tester'
d: list=[1,2,3,4]
e: bool=5<3
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type (d))
print(e, type (e))
print(task_1(a,b,c,d,e))


def task_2(x)->list:
    return 'x=', x
x=[1, 2, 3, 5, 8, 13, 21]
print(task_2(x[0:3]))

def task_3(y)->int:
    return y**2
print(task_3(y=5))