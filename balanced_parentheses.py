def is_balanced(parentheses):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in parentheses:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


sequence = input()

print("YES" if is_balanced(sequence) else "NO")