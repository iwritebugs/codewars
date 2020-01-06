def build_string(*args):
    return "I like {}!".format(", ".join(args))




def test_build_string():
    assert build_string('Cheese', 'Milk','Chocolate') == 'I like Cheese, Milk, Chocolate!'
    assert build_string('Cheese', 'Milk') == 'I like Cheese, Milk!'
    assert build_string('Chocolate') == 'I like Chocolate!'


Person = {
  "first_name": "John",
  "second_name": "Doe",
  "email_address": "john.doe@email.com",
  "male_or_female": "M"
}

