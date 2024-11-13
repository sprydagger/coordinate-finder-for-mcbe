from rich.prompt import *
from rich import print
max = IntPrompt.ask('What is the maximum range to search?', default=5000)
name = Prompt.ask('What is the target\'s name? ')

def find_axes():
    global x_axis
    global z_axis
    print('Run each command, then tell if it returned the name.')
    print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=', max, ',dy=512,dz=', max, ']', sep='')
    if Confirm.ask("Did it return the name?", default=False):
        x_axis = ''
        z_axis = ''
    else:
        print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=', max, ',dy=512,dz=-', max, ']', sep='')
        if Confirm.ask("Did it return the name?", default=False):
            x_axis = ''
            z_axis = '-'
        else:
            print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=-', max, ',dy=512,dz=-', max, ']', sep='')
            if Confirm.ask("Did it return the name?", default=False):
                x_axis = '-'
                z_axis = '-'
            else:
                print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=-', max, ',dy=512,dz=', max, ']', sep='')
                if Confirm.ask("Did it return the name?", default=False):
                    x_axis = '-'
                    z_axis = ''
                else:
                    print('Try again. The target might be near one of the axes')
                    find_axes()


def find_x_coordinate():
    global x_max
    global x_min
    global x
    x_min = 0
    x_max = max
    print('Run each command and reply if the target was found.')
    print('/w @s @e[name="', name, '", x=0, y=-140, z=0, dx=', x_axis, x_max, ', dy=512, dz=', z_axis, max, ']', sep='')
    if Confirm.ask("Did it return the name?", default=True):
        asdf=0
    else:
        asdf=0
    print(x_max)
    print(x_min)
    # x_max = (x_max + x_min) / 2

find_axes()
find_x_coordinate()