# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return Bracket(next, i + 1)
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return Bracket(next, i + 1)
            
    if opening_brackets_stack:
        return opening_brackets_stack.pop()
    
    return None


def main():
    input_str = input().strip()  
    i_index = input_str.find("I")  
    if i_index != -1:        
        mismatch = find_mismatch(input_str[i_index:])
    else:        
        mismatch = find_mismatch(input_str)
        
    if mismatch is None:
        print("Success")
    else:
        print(mismatch.position)
    

if __name__ == "__main__":
    main()
