from rich.prompt import *
from rich import print
max = IntPrompt.ask('What is the maximum range to search?', default=10000)
name = Prompt.ask('Name? ')
print('Run each command, then tell if it returned the name.')
print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=', max, ',dy=512,dz=', max, ']', sep='')

if Confirm.ask("Did it return the name?"):
    xaxis = ''
    zaxis = ''
else:
    print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=', max, ',dy=512,dz=-', max, ']', sep='')
    if Confirm.ask("Did it return the name?"):
        xaxis = ''
        zaxis = '-'
    else:
        print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=-', max, ',dy=512,dz=-', max, ']', sep='')
        if Confirm.ask("Did it return the name?"):
            xaxis = '-'
            zaxis = '-'
        else:
            print('/w @s @e[name="', name, '",x=0,y=-140,z=0,dx=-', max, ',dy=512,dz=', max, ']', sep='')
            if Confirm.ask("Did it return the name?"):
                xaxis = ''
                zaxis = ''
            else:
                print('Try again. The target might be near one of the axes')
