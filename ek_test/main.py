## Both wellcome.py and main.py are in same directory

# 1.
import welcome 
welcome.welcomeAll()

# 2.
import welcome as wc
wc.welcomeAll()

# 3.
from welcome import add
add(4,5)

# 4.
from welcome import *
welcome.add(5,7)
add(4,4) # you don't even need to use welcome. in this type(*)

## When the sub.py is ./check/ folder

# 1. importing everything
import check.sub as aman
aman.multiply(2,3)

# 2. importing specific function only
from check.sub import multiply
multiply(3,4)

# here both the ways are working bhaiya
