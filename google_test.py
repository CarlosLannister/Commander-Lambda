
def answer(s, n=1):
    equal_length = False
    equal_content = False
    new = [s[i:i+n] for i in range(0, len(s), n)]

    for i in new:
        if len(i) == len(new[0]):
            equal_length = True
        else:
            equal_length = False

    sorted_list = []
    for i in new:
        list_of = list(i) #elements to lists
        sorted_element = sorted(list_of) #sort list
        back_to_string = ''.join(sorted_element)#list back to string
        sorted_list.append(back_to_string) #append

    for i in sorted_list:
        if i == sorted_list[0]:
            equal_content = True
        else:
            equal_content = False

    if equal_length == True and equal_content == True:
        return len(sorted_list)
    return answer(s, n+1)
