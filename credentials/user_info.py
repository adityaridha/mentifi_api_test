

class User():

    def __init__(self):
        pass

    name = None
    email = "base_email@yahoo.com"
    password = "ZXasqw12"


class Mentor(User):

    def __init__(self):
        super().__init__()


class Mentee(User):

    def __init__(self):
        super().__init__()

class MentorAmber(Mentor):

    def __init__(self):
        super().__init__()

    name = "Amber Heard"
    email = "amberheard@mailinator.com"
    suid = 4137

class MenteeGarry(Mentee):

    def __init__(self):
        super().__init__()

    name = "Garry Nilson"
    email = "garrynilson@mailinator.com"
    suid = 4138


if __name__=="__main__":
    user = Mentor()
    print(user.email)
    print(user.password)