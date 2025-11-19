
initial_list = []
n = int(input())

def function_creator1():
    key_num = list(map(str,userInput.split()))
    print(key_num)
    return key_num



for i in range(n):
    userInput = input()
    if "append" in userInput:
        method = getattr(initial_list,function_creator1()[0])
        method(int(function_creator1()[1]))
    elif "insert" in userInput:
        method = getattr(initial_list, function_creator1()[0])
        method(int(function_creator1()[1]),int(function_creator1()[2]))
    elif "remove" in userInput:
        method = getattr(initial_list, function_creator1()[0])
        method(int(function_creator1()[1]))
    elif "print" in userInput:
        print(initial_list)
    elif"sort" in userInput:
        method = getattr(initial_list,"sort")
        method()
    elif "pop" in userInput:
        method = getattr(initial_list, "pop")
        method()
    elif "reverse" in userInput:
        method = getattr(initial_list, "reverse")
        method()
