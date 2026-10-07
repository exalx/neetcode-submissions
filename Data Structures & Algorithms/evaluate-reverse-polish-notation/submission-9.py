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
                    queue.append(int(a/b))
        return queue[0]