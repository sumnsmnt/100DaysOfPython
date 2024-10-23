# Create your own Class

# class User:
    # pass

# user01 = User()
# user01.id = "001"
# user01.username = "Suman"
# print(user01.username)
# print(user01.id)

# Class
class User:
    # Method
    def __init__(self, user_id, username):
        # Attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    # Method
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Passing attributes inside a Class
user01 = User("001", "Suman")
user02 = User("002", "Sujan")

print(user02.username)
print(user02.id)
print(user02.followers)

user01.follow(user02)

print(user01.followers)
print(user02.followers)

print(user01.following)
print(user02.following)