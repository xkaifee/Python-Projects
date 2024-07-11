"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 11.5 - User Privileges
Date: 11/13/2023

Description:
    This program creates a class that represents a user and a class that 
    represents a set of privileges. The user class has a privilege class 
    as an attribute. The user class has a method that prints the user's 
    privileges. The privilege class has methods that grant and revoke 
    privileges.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
class Privileges:
    def __init__(self, privs={'interact', 'post'}):
        # Set the 'privs' attribute
        self.privs = privs if privs is not None else {'interact', 'post'}

    def grant(self, priv):
        if not hasattr(self, 'privs'):
            self.privs = {'interact', 'post'}
        self.privs.add(priv)
        print(f'Granted {priv}')

    def revoke(self, priv):
        if not hasattr(self, 'privs'):
            self.privs = {'interact', 'post'}
        self.privs.discard(priv)
        print(f'Revoked {priv}')

    def get_privs(self):
        return ', '.join(sorted(self.privs))
    


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.privs = Privileges()

    def describe_user(self):
        print('User Profile')
        print(f'  Name: {self.name}')
        print(f'  Email: {self.email}')
        print(f'  Privs: {self.privs.get_privs()}')


def main():
    # create user instance
    alice = User('Alice', 'alice@example.com')
    alice.describe_user()

    # grant and revoke privileges
    alice.privs.grant('teleport')
    alice.describe_user()

    alice.privs.revoke('post')
    alice.describe_user()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
