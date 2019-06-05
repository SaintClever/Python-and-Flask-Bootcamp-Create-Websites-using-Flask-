# Providing a default for params
def report_person(jelly='BLANK'):
    print('reporting ' + jelly)

# report_person()


# RETURN vs PRINT in a function. USE return
def add_num(num1, num2):
    # print(num1 + num2)
    return num1 + num2

result = add_num(2, 4)
# print(result)
print(result + 10)
