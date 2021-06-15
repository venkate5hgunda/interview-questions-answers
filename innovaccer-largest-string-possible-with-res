a_dict = {"ale", "apple", "monkey", "plea"}   
res = "aapplwer" #ptr_2
max_len=0
max_word=""

for item in a_dict:
    ptr_1=0
    ptr_2=0
    while ptr_2 < len(res) and ptr_1 < len(item):
        if item[ptr_1]==res[ptr_2]:
            ptr_1+=1
            ptr_2+=1
        else:
            ptr_2+=1
    if ptr_1>len(item)-1:
        max_len=max(len(item),max_len)
        if max_len==len(item):
            max_word=item
print(max_word)
