class Solution:
    def asteroidCollision(self, asteroids):
        if len(asteroids) <= 1:
            return asteroids
        stack = []
        for item in asteroids:
            if not stack:
                stack.append(item)
            elif stack[-1] * item > 0:
                stack.append(item)
            elif stack[-1] > 0 and item < 0:
                flag = 0
                while len(stack):
                    val = stack[-1]
                    if val < 0:
                        break
                    if val < abs(item):
                        stack.pop()
                    elif val == abs(item):
                        stack.pop()
                        flag = 1
                        break
                    else:
                        flag = 1
                        break
                if not flag:
                    stack.append(item)
            else:
                stack.append(item)
        return stack

sol = Solution()
print(sol.asteroidCollision([-2, -2, 1, -2]))

