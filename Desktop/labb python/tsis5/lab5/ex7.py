import re
x = str(input())
def toCamel(snake):
    return ''.join( word.capitalize()
                    for word in snake.split('_') )
print(toCamel(x))