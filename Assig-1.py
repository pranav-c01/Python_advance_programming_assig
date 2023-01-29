#problem 1
decode_dict = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
def check_score(symb_list):
    s=0
    for i in symb_list:
        for j in i:
            s+=decode_dict[j]
    return s

r,s = check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]),check_score([
  ["#", "!"],
  ["!!", "X"]
]) 
print(r,s)


# Problem 2
def combinations(*kwargs):
    if kwargs:
        prod = 1
        for i in kwargs:
            prod*=i
        return  prod
    else:
        return 0
print(combinations(1,2,3))

#problem 3
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
def encode_morse(data_str):
    sd = ""
    for i in data_str:
        sd+=char_to_dots[i]+" "
    return sd
print(encode_morse("HELP ME !"))
print(encode_morse("EDABBIT CHALLENGE"))

# problem 4
num = 11
def isprime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
isprime(2**64-1)
isprime(56963)
isprime(5151512515524)

#problem 5
def to_boolean_list(word):
    l = list(map(lambda i:((ord(i)-96))%2!=0,word))
    return l

print(to_boolean_list("deep"))
print(to_boolean_list("loves"))
print(to_boolean_list("tesh")) 


