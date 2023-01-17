import turtle
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.bgcolor('white')
tr = turtle.Turtle()
tr.speed("fastest")
tr.up()
# left decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(-500, 0)
        tr.down()
        tr.color("purple")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("violet")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# right decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(470, 0)
        tr.down()
        tr.color("red")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("crimson")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# top decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20, 265)
        tr.down()
        tr.color("forest green")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("lime")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
# bottom decoration
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(20, -220)
        tr.down()
        tr.color("dark turquoise")
        tr.forward(100)
        tr.circle(5, steps=4)
        tr.right(60)
        tr.color("cyan")
        tr.forward(50)
        tr.right(120)
    tr.right(30)


turtle.up()
turtle.color('red')
turtle.goto(-320, 40)
turtle.write("Happy ",  font=(None, 60))
turtle.goto(-60, 40)
turtle.color('deep pink')
turtle.write("New",  font=(None, 60))
turtle.goto(145, 40)
turtle.color('blue')
turtle.write("Year",  font=(None, 60))
turtle.goto(-74, -60)
turtle.color('green')
turtle.write("2023!", font=(None, 60))
turtle.done()



import json


def json_to_dect(jsondata):
    output_dict = {}
    for i in jsondata:
        output_dict[i] = jsondata[i]
    return output_dict

temp = {}
temp1 = {}
def stack_excecution(dic_data:dict):
    global temp
    stack = []
    all_str = False
    temp1 = temp
    temp = dic_data
    for i in dic_data.keys():
        if isinstance(dic_data.get(i),dict):
            all_str = False
            stack.extend(stack_excecution(dic_data.get(i)))
        else:
            all_str = True
    if all_str:
        stack.append(dic_data)

    return stack

def get_stack(path):
    with open(path,'r') as data :
        read_data = data.read()
        data.close()
    dict_data = json_to_dect(json.loads(read_data))
    return stack_excecution(dict_data)

# print(get_stack("olx.json"))



def get_more(dic_data):
    stack = []
    ids = ['id','name','class']
    for i in dic_data.keys():
        if isinstance(dic_data.get(i),dict):
            all_str = False
            stack.extend(stack_excecution(dic_data.get(i)))
        else:
            all_str = True
    if all_str:
        stack.append(dic_data)
    return stack

def get_stack1(path):
    with open(path,'r') as data :
        read_data = data.read()
        data.close()
    dict_data = json_to_dect(json.loads(read_data))
    return get_more(dict_data)

print(get_stack1("olx.json"))