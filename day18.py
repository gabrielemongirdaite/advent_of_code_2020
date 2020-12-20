import re
import copy
import time


def evaluate_exp(sgn, num):
    cont = True
    while cont:
        if sgn[0] == '+':
            num[1] = num[0]+num[1]
        else:
            num[1] = num[0] * num[1]
        sgn.pop(0)
        num.pop(0)
        if len(num) == 1:
            cont = False
    return num


def evaluate_exp_part2(sgn, num):
    cont = True
    while cont:
        while '+' in sgn:
            indx = sgn.index('+')
            num[indx+1] = num[indx] + num[indx+1]
            num.pop(indx)
            sgn.pop(indx)
        try:
            num[1] = num[0] * num[1]
            sgn.pop(0)
            num.pop(0)
        except:
            pass
        if len(num) == 1:
            cont = False
    return num


def eliminate_brackets(new_exp, exp):
    start = 0
    while {'('}.issubset(set(new_exp)) or {')'}.issubset(set(new_exp)):
        start = exp[start:].find("(")+1+start
        end = exp[start:].find(")")+start
        new_exp = exp[start:end]
    return new_exp, start, end


def simplify_exp(expression, exp_evaluation):
    new_expression = copy.deepcopy(expression)
    while {'('}.issubset(set(expression)) or {')'}.issubset(set(expression)):
        new_exp, start, end = eliminate_brackets(new_expression, expression)
        numbers = [int(s) for s in re.findall(r'\b\d+\b', new_exp)]
        signs = re.findall(r'[+*]', new_exp)
        num = exp_evaluation(signs, numbers)
        expression = list(expression)
        expression[start-1] = str(num[0])
        del expression[start:end+1]
        expression = ''.join([str(elem) for elem in expression])
    return expression


def read_file(file_name, exp_evaluation):
    with open(file_name) as file_in:
        answer = 0
        for line in file_in:
            expression = simplify_exp(line, exp_evaluation)
            numbers = [int(s) for s in re.findall(r'\b\d+\b', expression)]
            signs = re.findall(r'[+*]', expression)
            answer += exp_evaluation(signs, numbers)[0]
    return answer


start_time = time.time()
print('1st part answer: ', read_file('input_d18.txt', evaluate_exp))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
print('2nd part answer: ', read_file('input_d18.txt', evaluate_exp_part2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

