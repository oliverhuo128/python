import pytest
import classes_intro_ex1
import classes_intro_ex2
import classes_intro_ex3

##Exercise 1 tests
# @pytest.mark.skip
def test_classes_intro_ex1_1():
    dog = classes_intro_ex1.Dog('black', 12)
    bark = dog.bark()
    assert bark == 'Woof!'

#@pytest.mark.skip
def test_classes_intro_ex1_2():
    dog = classes_intro_ex1.Dog('black', 12)
    dog2 = classes_intro_ex1.Dog('brown', 3)
    assert dog.is_old() == True
    assert dog2.is_old() == False

#@pytest.mark.skip
def test_classes_intro_ex1_3():
    dog = classes_intro_ex1.Dog('black', 12)
    assert dog.get_age_in_dog_years() == 12 * 7

## Exercise 2 tests
#@pytest.mark.skip
def test_classes_intro_ex2_1():
    teacher = classes_intro_ex2.Teacher()
    teach_string = 'Python is great!'
    actual_string = teacher.teach()
    assert teach_string == actual_string

#@pytest.mark.skip
def test_classes_intro_ex2_2():
    teacher = classes_intro_ex2.Teacher()
    teacher.teach()
    teach_string = 'PYTHON IS GREAT!'
    actual_string = teacher.teach()
    assert teach_string == actual_string

#@pytest.mark.skip
def test_classes_intro_ex2_3():
    teacher = classes_intro_ex2.Teacher()
    teacher.drink_booze()
    teach_string = 'Python is great!'
    actual_string = teacher.teach()
    a = sorted(teach_string)
    b = sorted(actual_string)
    assert teach_string != actual_string
    assert a == b

#@pytest.mark.skip
def test_classes_intro_ex2_4():
    teacher = classes_intro_ex2.Teacher()
    teacher.drink_booze()
    teacher.teach()
    teach_string = 'PYTHON IS GREAT!'
    actual_string = teacher.teach()
    a = sorted(teach_string)
    b = sorted(actual_string)
    assert teach_string != actual_string
    assert a == b

#@pytest.mark.skip
def test_classes_intro_ex2_5():
    teacher = classes_intro_ex2.Teacher()
    teacher.teach()
    teacher.drink_booze()
    teacher.drink_water()
    teach_string = 'Python is great!'
    actual_string = teacher.teach()
    assert teach_string == actual_string


#@pytest.mark.skip
def test_classes_intro_ex3_1():
    Simon = classes_intro_ex3.Athlete('Simon', 'GB')
    Pierre = classes_intro_ex3.Athlete('Pierre', 'FR')
    Xavi = classes_intro_ex3.Athlete('Xavi', 'ESP')
    Simon.award_medal('gold')
    Pierre.award_medal('silver')
    Xavi.award_medal('bronze')
    assert classes_intro_ex3.Athlete.gold_medal_totals == {'ESP': 0, 'FR': 0, 'GB': 1}
    assert classes_intro_ex3.Athlete.silver_medal_totals == {'ESP': 0, 'FR': 1, 'GB': 0}
    assert classes_intro_ex3.Athlete.bronze_medal_totals == {'ESP': 1, 'FR': 0, 'GB': 0}
    
