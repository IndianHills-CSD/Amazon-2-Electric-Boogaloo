
class postModel:
    """Model to map post info from db to python class"""
    def __init__(self,id,auth,title,desc,loc,price):
        self.PostID = id
        self.Author = auth
        self.Title = title
        self.Description = desc
        self.Location = loc
        self.Price = price

    def getId(self):
        return self.PostID

    def getAuthor(self):
        return self.Author

    def getTitle(self):
        return self.Title

    def getDescription(self):
        return self.Description

    def getLocation(self):
        return self.Location

    def getPrice(self):
        return self.Price


    
class userModel:
    def __init__(self,email,user,password):
        self.EmailID = email
        self.UserName = user
        self.Password = password