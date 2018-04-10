# http://aflowlib.org/

import aflow

print(help(aflow))

print('\naflow.list_keywords:',type(aflow.list_keywords),'\n')
print(help(aflow.list_keywords))
print('\naflow.list_keywords():\n')
for elt in aflow.list_keywords():
    print(elt)

print('\nThe contents of aflow:\n')

for elt in dir(aflow):
    print(elt)

# print('\naflow.K:',type(aflow.K))
# print(help(aflow.K))
# print('\nThe contents of aflow.K:\n')
# for elt in dir(aflow.K):
#     print(elt)

print('\naflow.control:',type(aflow.control),'\n')
print(help(aflow.control))
print('\nThe contents of aflow.control:\n')
for elt in dir(aflow.control):
    print(elt)

print('\naflow.msg:',type(aflow.msg),'\n')
print(help(aflow.msg))
print('\nThe contents of aflow.msg:\n')
for elt in dir(aflow.msg):
    print(elt)

print('\naflow.search:',type(aflow.search),'\n')
print(help(aflow.search))






