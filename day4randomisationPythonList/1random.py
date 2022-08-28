from ctypes import sizeof
import random
import my_module
random_integar=random.randint(1,10)
print(random_integar)
print(my_module.pi)
random_float=random.random()# [0 1) arasında float değerleri alıyor
print(random_float)
random_float2=random.random()*5
print(random_float2)
