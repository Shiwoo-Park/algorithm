# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if len(tokens) == 0 :
            return None

        stack = []
        operatorList = ["+","-","*","/"]
        for token in tokens :
            if token in operatorList :
                v2 = stack.pop()  # FILO
                v1 = stack.pop()
                if token == "+" :
                    stack.append(v1+v2)
                elif token == "-" :
                    stack.append(v1-v2)
                elif token == "*" :
                    stack.append(v1*v2)
                elif token == "/" :
                    minus = False
                    if (v1*v2) < 0 :
                        minus = True
                    if v1 < 0 :
                        v1 = v1 * (-1)
                    if v2 < 0 :
                        v2 = v2 * (-1)
                    val = v1/v2
                    if minus :
                        val = val * (-1)
                    stack.append(val)
            else :
                stack.append(int(token))

        return stack.pop()