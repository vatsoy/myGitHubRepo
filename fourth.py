
# f = open('C:\\Users\\Vadim\\Projects\\Python\\Test_TXT.txt')
# text = f.read()
# for line in text.split('\n'):
#     print(line)
# f.close()
#==================================================================
# f = open('C:\\Users\Vadim\Projects\\Python\Test_TXT.txt')
# for line in f:
#     print(line)
# f.close()
#===================================================================
# #the same as previous, but with no close as 'with' closes it by itself
# with open('C:\\Users\Vadim\Projects\\Python\Test_TXT.txt') as f:
#     for line in f:
#         print(line)
#===================================================================

# testing example of try/except/else

try:
    print(int('25'))
except:                 #if printing failed
    print('Failed')
else:                   #if no except - not failed
    print('Successful')
finally:                #always implemented
    print('Done!')
