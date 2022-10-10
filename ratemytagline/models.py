from django.db import models


class tagLine(models.Model):
    # It seems some fields are missing, fill them up!
    tagline = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,default="test")
    # Hint: Create an IntegerFiled object 'numberOfVotes' with default value 0 here;
    
    #isPopular doesnt seem to be right. Can you fix it?
    def isPopular(self):
        if(self.numberOfVotes > 10):
            return False
        else:
            return True
    def __str__(self):
        #This was not covered in the previous tutorial, but __str__(self) is used to 
        #specify what the object should return when called without any dereferencing.
        #   What do you think __str__() should return here for the tagLine object.
