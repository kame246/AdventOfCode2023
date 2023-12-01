import string

num_sum = 0
with open(r'real_data.txt') as f:
    for line in f:
        strip_line = line.strip(string.ascii_letters + string.whitespace)
        num_sum += int(f'{strip_line[0]}{strip_line[-1]}')

print(f'Answer: {num_sum}') # 55621