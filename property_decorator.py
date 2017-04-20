class test(object):
   
    def __init__(self, fname, lname):

        self.fname = fname
        self.lname = lname
        # Private to class, but will be revealed in class.__dir__
        # For this eample to work this has to be a private variable.
        self._email = None
        # Private to __init__ method
        fname = fname
    

    # Whenever we assign or retrieve any object attribute like fname, 
    # as show above, Python searches it in the object's __dict__ dictionary.
    # Therefore, test.fname internally becomes test.__dict__['fname'].

    @property
    def email(self):

        # Getter for self._email. Note how the name is same as the attribute
        # So, when email is called the interpreter is tricked to call this 
        # property method. Unless a setter is defined self._email cannot
        # be set.
        try:
            self._email = self.fname+'.'+self.lname+'@gmail.com'
            return self._email
        except Exception as e:
            print e


    @email.setter
    def email(self, value):

        # If commented, there is no way to set email, lol ;)
        self._email = value

    @email.deleter
    def email(self):

        self._email = None

if __name__ == '__main__':

    print ''
    tt = test('Mohan', 'Madhavan')
    print('Calling email with Mohan and Madhavan')
    print(tt.__dict__)
    print(tt.email)
    
    print ''
    print('Setting fname to MKM')
    tt.fname = 'MKM'
    print(tt.__dict__)
    # Notice how you can call the property as an attribute
    print('Calling email with MKM Madhavan')
    print(tt.email)
    print('Note the difference in __dict__ value')
    print('Email gets reset after the variable is called')
    print(tt.__dict__)

    try:
        # uncomment setter first
        print ''
        print('Setting email to some.email.com')
        tt.email = 'some.email.com'
        print(tt.__dict__)
        print('Calling email with new value')
        print(tt.email)
    except Exception as e:
        print e.message

    # This will call the deleter property
    try:
        print ''
        print('Calling the deleter property')        
        del tt.email
        print(tt.__dict__)
    except Exception as e:
        print e.message

