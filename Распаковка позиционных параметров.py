def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


def print_params(a, b, c):
    print(a, b, c)
values_dict = {'v':4, 'd':5, 'n':6}
values_list = [1, 2, 3]
print_params(*values_list)

def print_params(**kwargs):
    print(kwargs)
values_dict = {'v':4, 'd':5, 'n':6}
print_params(**values_dict)

def print_params(v, d, h):
    print(v, d, h)
values_list_2 = [ 0, 'привет']
print_params(*values_list_2, 42)





#print_params
# #print_params(b = 25)
#print_params(c =[1,2,3]('a=1', 'b=строка', 'c=True')
#
#