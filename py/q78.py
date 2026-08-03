# DSA in Python - Generate Parentheses | Recursion & Backtracking | Leetcode 22 - Part 74

def bracket(s):
    limit = s*2
    result = []
    subset = ["0"]*limit


    def recursion(indx , left, right):
        if s == 1:
            return result.append("()")

        if indx >= limit:
            return result.append("".join(subset))


        if left > 0:
            subset[indx] = "("
            recursion(indx+1 , left-1, right)
            

        if right > left:
            subset[indx] = ")"
            recursion(indx+1 , left, right-1)
            
            
    recursion(0 ,s,s)
    return result

print(bracket(3))



        