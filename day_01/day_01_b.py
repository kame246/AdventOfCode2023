import operator
import string

result = 0
numbers = ('zero OMG', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
with open(r'real_data2.txt') as f:
    for line in f:
        s_left_index = min([x for x in [line.find(n) for n in numbers] if x != -1] or [None])
        s_right_index = max([x for x in [line.rfind(n) for n in numbers] if x != -1] or [None])
        left_index = min([x for x in [line.find(d) for d in string.digits] if x != -1] or [None])
        right_index = max([x for x in [line.rfind(d) for d in string.digits] if x != -1] or [None])

        get_s_number = lambda index: [x for x in numbers if line[index:index + 2] == x[:2]].pop()


        def calculate_number(s_num_ind, num_ind, operator_fun):
            if s_num_ind is not None:
                if num_ind is not None:
                    return get_s_number(s_num_ind) if operator_fun(s_num_ind, num_ind) else line[num_ind]
                else:
                    return get_s_number(s_num_ind)
            else:
                return line[num_ind]


        first_number = calculate_number(s_left_index, left_index, operator.lt)
        last_number = calculate_number(s_right_index, right_index, operator.gt)

        first_number = numbers.index(first_number) if len(first_number) > 1 else int(first_number)
        last_number = numbers.index(last_number) if len(last_number) > 1 else int(last_number)
        result += first_number * 10 + last_number

print(f'Answer: {result}') # 53592


