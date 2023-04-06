import custommodule
from mypackage import myothermodule
from mypackage.myothermodule import say_hi

print(custommodule.say_hi('Geri'))
print(myothermodule.say_hi('Geri'))
print(say_hi('Geri'))
