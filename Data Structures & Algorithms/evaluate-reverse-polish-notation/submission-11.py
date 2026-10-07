class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ope = {"+", "-", "*", "/"}
        val = 0
        queue = []
        for i in range(len(tokens)):
            if tokens[i] not in ope:
                queue.append(int(tokens[i]))
            else:
                b = queue.pop()
                a = queue.pop()
                operator = tokens[i]
                if operator == "+":
                    queue.append(a + b)
                elif operator == "-":
                    queue.append(a - b)
                elif operator == "*":
                    queue.append(a * b)
                else:
                    if b < 0 and a >= 0:
                        queue.append(-(a // -b))
                    elif a < 0 and b > 0:
                        queue.append(-(-a // b))
                    else:
                        queue.append(a // b)
        return queue[0]