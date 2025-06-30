def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n - 1)
    
print(add(100))

def print_list(list,idx):
    if idx == len(list):
        return
    else:
        print(list[idx])
        print_list(list, idx + 1)

name = ['Alice', 'Bob', 'Charlie', 'David']
nmm=print_list(name)
print(nmm)
