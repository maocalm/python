import random, string,uuid


def random_str(num):
    chars = "asdfghjklzxcvbnm"
    s = [random.choice(chars) for i in range(3)]
    print(s)
    print(''.join(s))


def random_uuid ():
    print(uuid.uuid4() )
if __name__ == '__main__':
    random_str(200)
    random_uuid()
