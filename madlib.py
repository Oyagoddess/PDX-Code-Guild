name = str(raw_input('what is your name?'))
color= str(raw_input ('what is your favorite color?'))
food= str(raw_input ('what is your favorite food?'))
state= str(raw_input ('what state do you live in?'))

madlist= {'n': name,'c': color,'f': food, 's': state}
story= 'Hello %(n)s,do all people from %(s)s wear %(c)s hat made of %(f)s'


print story % madlist


