def hello_1 (greenting  , name  ):
    print( '{},{}'.format(greenting ,name))
def hell_2(greenting ,name):
    print('{}，{}'.format(greenting ,name))
hell_2("hello" ,"world")


def hello_3 (name , greeting = 'hello' ,pondection = '!'):
    print('{} ,{}{}'.format(greeting ,name ,pondection))


hello_3('hanwnem')
hello_3('hanwenmao' ,'nihoa')
hello_3('nihao' ,'hanwenmao')  # name 变成了nihao  greeting 变成了 hanwenmao ;



ani = (1)
print(ani,)

print('==============')
def add(x,y):
    return x+y

params = (2,4)
a  =add(*params)
print(a)
b = add(2,4)
print(a)

print('==============')


def story (**kwds):
    return  'once upon a time , there was a  {job} called {name}.'.format_map(kwds)
print(story(job ='king' , name ='guby'))


params2 = {'job':"languazge", 'name': 'python' ,'lal' :'mama'}  #   字典；

print(story(**params2))  # 参数无限制 ， 但必须是字典了；
del params2['name']
print(params2)   # 删除了 字典中字段
print(story(job ='storke of genius ' ,**params2))  #默认参数 ， 第一个填充；




