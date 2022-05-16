class FormulaError(Exception):
    
    def __str__(self):
        return f'Mistake in your formula'


class ArithmethicError(Exception):
    def __init__(self, oper):
        self.oper = oper
    
    def __str__(self):
        return f'Your operator --> {self.oper} is incorrect! Must be + - * /'


def split_str(s):
    
    def arith(a,b,r):
       match r:
            case '+':
                return a+b
            case '-':
                return a-b
            case '*':
                return a*b
            case '/':
                try:
                    a/b
                except ZeroDivisionError:
                    return "You can't division by zero"
                else:
                    return a/b

    s=[i for i in s.split()]
    if len(s)!=3:
        raise FormulaError

    if not any(s[1] in word for word in ['+','-','/','*']):
        raise ArithmethicError(s[1])

   
    try:
        s[0]=float(s[0])
        s[2]=float(s[2])
    except ValueError:
        return FormulaError() 
    else:
        return arith(s[0],s[2],s[1])


    


print(split_str("1 + 2 _ 2"))
print(split_str("1 - 2"))
print(split_str("1 / 2"))
print(split_str("1 * 2"))
print(split_str("j * 2"))




