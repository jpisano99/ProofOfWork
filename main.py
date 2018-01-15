import hashlib


my_string = 'Hello World!'
my_string_hash = hashlib.sha256(my_string.encode('utf-8')).hexdigest()
# nonce = str(1)
# pow = my_string + nonce
# print (my_string,pow)
# print ('String >>>  ', hashlib.sha256(my_string.encode('utf-8')).hexdigest())
# print ('String + nonce >>> ',hashlib.sha256(pow.encode('utf-8')).hexdigest())

num_matched = 0

# One million guesses to match 5 leading zeroes
for x in range (0,1000000):
    nonce = str(x)
    pow = my_string + nonce
    my_pow_hash = hashlib.sha256(pow.encode('utf-8')).hexdigest()

    if my_pow_hash[:5] == '00000' :
        num_matched = num_matched +1
        print ('Match it with Nonce value>> ',x)
        print('POW    >>> ', my_pow_hash)

print ('Num Matched>> ', num_matched)





