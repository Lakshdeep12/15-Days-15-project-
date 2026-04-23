import random 

def generate_story():
    
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
    name = ['Ali', 'Sara', 'John', 'Emily','Michael']
    where = ['in the forest', 'at the park', 'on the beach', '  in the city','at home']
    what = ['found a treasure', 'got lost', 'met a friend', 'had an adventure','found a secret']    

    print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' was ' + random.choice(where) + ' and ' + random.choice(what) + '.')
generate_story()