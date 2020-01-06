from collections import OrderedDict

class Dinglemouse(object):

    def __init__(self):
        self.hello_dict = OrderedDict()
        self.hello_dict['start'] = 'Hello.'

    def setAge(self, age):
        self.hello_dict['age'] = 'I am {}.'.format(age)
        return self

    def setSex(self, sex):
        gender = "male" if sex == 'M' else "female"
        self.hello_dict['gender'] = 'I am {}.'.format(gender)
        return self

    def setName(self, name):
        self.hello_dict['name'] = 'My name is {}.'.format(name)
        return self

    def hello(self):
        return  ' '.join(x for x in self.hello_dict.values())



def testBob27Male():
    dm = Dinglemouse().setName("Bob").setAge(27).setSex('M')
    expected = "Hello. My name is Bob. I am 27. I am male."
    assert dm.hello() == expected


def test27MaleBob():
    dm = Dinglemouse().setAge(27).setSex('M').setName("Bob")
    expected = "Hello. I am 27. I am male. My name is Bob."
    assert dm.hello() == expected



def test27MaleBob():
    dm = Dinglemouse().setName("Alice").setSex('F')
    expected = "Hello. My name is Alice. I am female."
    assert dm.hello() ==  expected


def testBatman():
    dm = Dinglemouse().setName("Batman")
    expected = "Hello. My name is Batman."
    assert dm.hello() ==  expected
