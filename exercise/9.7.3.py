def get_word(text):
    result = []
    # print(",,,,," ,enumerate(text.split(' ')))
    for i, letter in enumerate(text.split(' ')):
        result.append(len(letter))

    return result


def han():
    d = {'x':1 ,'y':2  ,'z':3  }
    for key , value in d.items():
        print(key , value)

def wen():
    k = ['1' ,'2', '3', '4']
    for value  in  range(len(k)):
        print('value :'+k[value])



text = 'Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation.'
print(get_word(text))
han()
wen()