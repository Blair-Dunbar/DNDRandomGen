import random
from Tkinter import *

def d20():
    health = random.randint(1,20)    
    return (health)
    
def display_d20():
    final = retrieve_d20()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d20():
    return d20()  
# 
def d12():
    health = random.randint(1,12)    
    return (health)
    
def display_d12():
    final = retrieve_d12()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d12():
    return d12()
# 
def d10():
    health = random.randint(1,10)    
    return (health)
    
def display_d10():
    final = retrieve_d10()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d10():
    return d10()      
# 
def d8():
    health = random.randint(1,8)    
    return (health)
    
def display_d8():
    final = retrieve_d8()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d8():
    return d8()  
# 
def d6():
    health = random.randint(1,6)    
    return (health)
    
def display_d6():
    final = retrieve_d6()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d6():
    return d6()  
# 
def d4():
    health = random.randint(1,4)    
    return (health)
    
def display_d4():
    final = retrieve_d4()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d4():
    return d4()  
# 
def d100():
    health = random.randint(1,100)    
    return (health)
    
def display_d100():
    final = retrieve_d100()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_d100():
    return d100()  
#
def stats():
    Strengthroll = random.randint(6,18)
    Dexterityroll = random.randint(6,18)
    Constitutionroll = random.randint(6,18)
    Intelligenceroll = random.randint(6,18)
    Wisdomroll = random.randint(6,18)
    Charismaroll = random.randint(6,18)
    
    return (Strengthroll, Dexterityroll, Constitutionroll, Intelligenceroll, Wisdomroll, Charismaroll)
#    
def display_stats():
    final = retrieve_stats()
    stuff = Label(root, text=final)
    stuff.pack()    
def retrieve_stats():
    return stats()
#
root = Tk()
# 
text = Label(root, text='Click buttons below\nto make random stats for\na Dungeons and Dragons\nCharacter') # Instruction text
text.pack()
# 
Button1 = Button(root, width = 20, text='Random Stats', command = display_stats)
Button1.pack()
Button1 = Button(root, width = 20, text='d20', command = display_d20)
Button1.pack()
Button2 = Button(root, width = 20, text='d12', command = display_d12)
Button2.pack()
Button2 = Button(root, width = 20, text='d10', command = display_d10)
Button2.pack()
Button3 = Button(root, width = 20, text='d8', command = display_d8)
Button3.pack()
Button4 = Button(root, width = 20, text='d6', command = display_d6)
Button4.pack()
Button5 = Button(root, width = 20, text='d4', command = display_d4)
Button5.pack()
Button6 = Button(root, width = 20, text='d100', command = display_d100)
Button6.pack()
# 
root.title('AutoGen')
root.geometry("+1000+250") 
root.resizable(1, 1) 
root.mainloop()