### foramt 메서드 ###
# format 메서드의 인수로 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식


print('My name is {}'.format('Sarah'))

print('My name is {name}'.format(name="James"))

print('My name is {}. I\'m {} year old'.format('James', 25))


# 인덱스를 지정해서 사용가능
print('My name is {1}. I\'m {0} year old.'.format(25, "James"))

print('My name is {name}. I\'m {age} year old.'.format(name='James', age=25))

name = "James"
print('My name is {name}'.format(name=name))