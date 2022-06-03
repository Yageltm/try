hexadict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


# assignment 1
def hex_to_dec(num):
    summery = 0
    dig = 0
    if num.startswith('0x'):
        num = num[2:]
    for i in num[::-1]:
        if i.lower() not in hexadict:
            print("Invalid hex number")
            return
        summery += hexadict[i.lower()] * (16 ** dig)
        dig += 1
    return summery


# assignment 2
def word_to_sum(s):
    summery = 0
    s += 'k'  # אם לא נוסיף איבר שאינו הקסדצימלי בסוף הקוד יפספס את האות האחרונה
    current_word = ''
    for i in s:
        if i.lower() in hexadict:
            current_word += i
        else:
            summery += hex_to_dec(current_word)
            current_word = ''
    print(summery)


# assignment 3
def ave():
    summery = 0
    numbers_list = []
    while True:
        num = input("Enter number please: ")
        if num.isnumeric():
           numbers_list.append(num)
        else:
            break
    for i in numbers_list:
        summery += int(i)
    print(f'"The average is: {summery/len(numbers_list)}')
    numbers_list = sorted(numbers_list)
    if len(numbers_list)%2==0:
        print(f'The medians are {numbers_list[(len(numbers_list)//2)-1]} and {numbers_list[len(numbers_list)//2]}')
    else:
        print(f'The median is {numbers_list[len(numbers_list)//2]}')


if __name__ == "__main__":
    print(hex_to_dec('0xab'))
    word_to_sum('ABRAKADABRA')
    ave()

