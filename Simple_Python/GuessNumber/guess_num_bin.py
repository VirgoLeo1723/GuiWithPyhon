in_num=0
max_val=0
min_val=0
def max(a,b):
    return a if a>b else b
def min(a,b):
    return a if a<b else b
def setup():
    global in_num
    global max_val
    print("I always can find your number: ")
    in_num=int(input("Input num = "))
    max_val=int(input("Range of num (0,a)="))  
    bin_search()

def bin_search():
    global in_num
    global min_val
    global max_val
    if in_num==min_val: print_result(min_val)
    elif in_num==max_val: print_result(max_val)
    else:
        temp=(min_val+max_val)//2
        print(temp)
        if temp==in_num: print_result(temp)
        if temp<in_num :min_val=max(min_val,temp)  
        else: max_val=min(max_val,temp)
        bin_search()

def print_result(result):
    print(f"Your number = {result}")
    exit()

setup()