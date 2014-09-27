name = str(raw_input('what is your name?'))
season= str(raw_input ('what is your favorite season?'))
beverage= str(raw_input ('what is your favorite beverage?'))
state= str(raw_input ('what state do you live in?'))

madlist= {'n': name,'st': state ,'b': beverage, 's': season}
story= 'Hello %(n)s,do all people from %(st)s drink %(b)s in %(s)s'


print story % madlist


