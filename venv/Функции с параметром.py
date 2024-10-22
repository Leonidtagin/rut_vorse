#def say_hello(name): # ПРИНИМАЮЩАЯ FУНКИЯ
 #   print("hello", name)
#say_hello('george')
#say_hello('jony')

#возвращающая Fункция
#import random
#def lottery():
    #tickets = [1,2,3,4,5,6,7,8,9,10]
   # win = random.choice(tickets)
   # return win
#win = lottery()
#print(win)

#import random
#def lottery(mon,thue):
  #  tickets = [1,2,3,4,5,6,7,8,9,10]
 #   win1 = random.choice(tickets)
   # tickets.remove(win1)
   # wni2 = random.choice(tickets)
   # print(mon, thue)
    #return win1, 'win2'
#win1, win2 = lottery('mon', 'thue')
#print(win1, win2)

def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
get_matrix(4, 2, 13)