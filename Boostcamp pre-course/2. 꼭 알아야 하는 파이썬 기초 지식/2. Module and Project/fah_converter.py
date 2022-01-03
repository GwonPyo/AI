def convert_c_to_f(cel_value):
    return cel_value * 9.0 / 5 + 32

# 아래 코드에서 __name__ == '__main__'을 붙이지 않으면
# 해당 모듈을 다른 곳에서 import했을 때 test 변수값이 출력된다.
if __name__ == '__main__':
    test = "GGG"
    print(test)