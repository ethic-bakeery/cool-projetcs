class Student:
    def __init__ (self):
        self.morning = 'morning'
        self.afternoon = 'afternoon'
        self.evening = 'evening'

    def complement(self):
        print("""
              You look absolutely nice in this dress,
              keep on wearing blue gowns, it always suits you :)
              would mind me taking you a picture? """)
        
    def GreetFriends(self):
        print("hey,bro! what's up")
        self.complement()

    def GreedTeachers(self,time):
    
        if time == self.afternoon: 
            print("Good Afternon, Ma'am/Sir")
        elif time == self.morning:
            print("Good Morning, Ma'am/Sir")
        elif time == self.evening:
            print("Good Evening, Ma'am/Sir")
        else:
            print("Good day, Ma'am/Sir!")
        
        self.complement()

p1 = Student() #declare instance of a class called p1
isFriend = input("Greet Teacher/Friend: ").lower()

if isFriend == "teacher":
    GreetingTime = input("its Morning/Afternoon/Evening?: ").lower()
    p1.GreedTeachers(GreetingTime)
elif isFriend == "friend":
    p1.GreetFriends()
else:
    print("Invalid input :)")


# when declaring an instance varibale eg p1.name its belong to only instane p1
# and it cant be access by other instances and methods within the class
# its better to use the variables within the methods so that it can be access by all
# Note: two instance variable are different eg (p1.name = 'john') and (p2.name = 'sam')
# are not the same meaning modification of p1 does not affect p2 plus you can access both the instance
"""
p1.name = 'kamal'
print(p1.name) #kamal
print(p2.name) #kamal
p2.name = 'john'
print(p2.name) #john
print(p1.name) #john
"""
# # the other instances of a class eg p1.p2 etc
# p2 = Student() #Another instance of a class called p2
# print(type(p1)) #to see the type of object p1
# print(type(p2)) #to see type of object p2


# print(id(p1)) #to see the id
# print(id(p2)) #