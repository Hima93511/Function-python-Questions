# question no  1
#def fun1 (name, age=20):
 #   print(name, age)

#fun1('Emma', 25)
# outpu is Emma 25

#Questions 2 

#def display(**kwargs):
  #  for i in kwargs:
 #       print(i)

#display(emp="Kelly", salary=9000)
# output is salary

# Question 3
# A function can take unlimited no of arguments
# A Python Function can return multiple values


#  Question 4

#def outer_fun(a, b):
   # def inner_fun(c, d):
  #      return c + d
 #   return inner_fun(a, b)

#res = outer_fun(5,10)    

#print(res)
# output is 15

# Question 5
#def add(a,b):
 #   return a+5, b+5

#result = add(3, 2)
#print(result)
# Output is (8,7)

# Question 6
#def outer_fun(a, b):
    #def inner_fun(c, d):
   #     return c + d

  #  return inner_fun(a, b)
 #   return a

#result = outer_fun(5, 10)
#print(result)
 # output is 15


# Question 7

def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")
