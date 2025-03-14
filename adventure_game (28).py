# import
import time
import random
a = 1
score = 0
# z'تعيين اسم اللاعب"
name = input('enter_your_name')
time.sleep(6)

# دالة print_pause


def print_pause(word):
    print(word)
    time.sleep(6)


print_pause('welcome'+'_'
            + 'in_the_adventure_game')
print_pause('the_adventure_game' +
            'is_a_fun_game')
print_pause('The_game_provides_many_amazing'
            + '_things_that_make_you_feel_like_you_are_in_the_real_world')
print_pause("You_should_go_far_from"
            + "_the_cave_if_you_want_to_win")

# تعيين الألوان


def color():
    colors = [
        'yellow', 'green',
        'brown', 'white'
    ]
    color_cave = random.choice(colors)
    color_door = random.choice(colors)
    color_road = random.choice(colors)
    print_pause('color_cave_is'+'_'+color_cave)
    print_pause('color_door_is'+'_'+color_door)
    print_pause('color_road_is'+'_'+color_road)

# هذه الدالة تقلل من الأخطاء


def error():
    print_pause("error")
    w = input('Do_you_want'
              + '_to_leave?')
    time.sleep(2)
    while w == 'yes' or 'No':
        if w == 'No':
            start()
        elif w == 'yes':
            for luck in [1, 2, 3, 4]:
                print('good_luck')

# دالة false


def false():
    print('enter_1_to_say_yes')
    print('enter_2_to_say_No')
    print('Are_you_sure?')
    g = input('choose_1_or_2')
    if g == '1':
        print('see_you_soon')
    else:
        if g == '2':
            repeat()

# cave


def Going_cave():
    print_pause('look_the_cave')
    print_pause('I_am'+'_'+'hungry')
    print_pause('but,_'+'I_look_meat')
    print_pause('you_have' + '_'+'to_eat_meat')
    c = ''
    while c != '1':
        c = input('choose_1_if_you'+'want_to_eat_meat')
    time.sleep(2)
    for meat in [1, 2, 3, 4, 5]:
        print('It_is_a' + '_'+'good_meat')

# دالة game تستخدم لبدء اللعبة حيث يوجد جزء كبير من اللعبة في هذه الدالة


def game():
    print_pause('if_you_answer'+'_the_question,you_will_pass')
    print_pause('1+1')
    time.sleep(2)
    path = input('answer')
    if path == '2':
        Going_cave()
        score = +1
    else:
        Going_cave()
        score = -1
     # تعيين النقاط والفوز الخسارة
    if score == 1:
        time.sleep(2)
        for wining in [1, 2, 3, 4]:
            print('You_win')
    elif score == -1:
        for losing in [1, 2, 3, 4]:
            print('You_lose')

# Do you repeat?


def repeat():

    print('Do_you'
          + '_'+'repeat?')
    choise = input('CHOOSE_yes_or_No')
    time.sleep(2)
    if choise == 'No':
        false()
    else:
        if choise == 'yes':
            start()
            score = 0
        else:
            error()


time.sleep(2)

# دالة الباب انها  المفتاح الرئيسي للعبة


def start():
    print_pause('hello'
                + '_'+name)
    color()
    print('knock'
          + 'the_door')
    print('click_1_if '
          + 'you_want_to_start')
    d = ''
    time.sleep(2)
    while d != '1':
        d = input('click_1')
    print('come_on')
    game()
    repeat()
    score = 0


# تلك الدالة تساعد أحد المؤثرات التي في اللعبة
time.sleep(3)
start()
