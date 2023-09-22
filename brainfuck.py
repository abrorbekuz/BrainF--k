def execute_brainfuck(brainfuck_code):
    memory = [0] * 30000
    ptr, i = 0, 0
    output, stack = [], []

    code_length = len(brainfuck_code)

    while i < code_length:
        char = brainfuck_code[i]

        if char == '>':
            ptr += 1
        elif char == '<':
            ptr -= 1
        elif char == '+':
            memory[ptr] = (memory[ptr] + 1) & 0xFF
        elif char == '-':
            memory[ptr] = (memory[ptr] - 1) & 0xFF
        elif char == '.':
            output.append(chr(memory[ptr]))
        elif char == ',':
            pass
        elif char == '[':
            if memory[ptr] == 0:
                loop_depth = 1
                while loop_depth > 0:
                    i += 1
                    if i >= code_length:
                        raise ValueError("Unmatched '[' in Brainfuck code")
                    if brainfuck_code[i] == '[':
                        loop_depth += 1
                    elif brainfuck_code[i] == ']':
                        loop_depth -= 1
            else:
                stack.append(i)
        elif char == ']':
            if memory[ptr] != 0:
                i = stack[-1]
            else:
                stack.pop()

        i += 1

    return ''.join(output)