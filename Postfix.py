from Regex import Regex
from Stack import Stack
from Symbol import Symbol
class Postfix:
    def __init__(self, regex):
        self.regex = regex.expression+')'
        self.pila = Stack()
        self.postfix = self.convertInfixToPostfix()

    def convertInfixToPostfix(self):
        self.pila.push('(')
        auxpost = ""
        for i in range(len(self.regex)):
            if Symbol.isOperand(self.regex[i]):
                auxpost += self.regex[i]
            elif Symbol.isLeftParenthesis(self.regex[i]):
                self.pila.push(self.regex[i])
            elif Symbol.isOperator(self.regex[i]):
                while not self.pila.isEmpty() and Symbol.isOperator(self.pila.peek()) and (Symbol.checkPrecedence(self.pila.peek()) >= Symbol.checkPrecedence(self.regex[i])):
                    auxpost += self.pila.pop()
                self.pila.push(self.regex[i])
            elif Symbol.isRightParenthesis(self.regex[i]):
                while not self.pila.isEmpty() and not Symbol.isLeftParenthesis(self.pila.peek()):
                    auxpost += self.pila.pop()
                self.pila.pop()
        return auxpost
