##import math
##
### 45도를 라디안 값으로 변환
##
##
##angle_x = float(input("원하는 각도를 입력해줘 그러면 그 값의 Sin()값을 돌려 줄게" ))
##
####print(angle_x)
##
##radian_x = angle_x*math.pi/180
##
##
##
##print("값의 Sin 값은 :",  math.sin(radian_x))
##      

##import math
##
##while True:
##    try:
##        angle_x = float(input("원하는 각도를 입력해주세요 (0~360도): "))
##        if 0 <= angle_x <= 360:
##            radian_x = angle_x * math.pi / 180
##            print(f"{angle_x}도의 sin 값은 {math.sin(radian_x):.4f}입니다.")
##            break
##        else:
##            print("각도는 0도 이상 360도 이하의 값을 입력해주세요.")
##    except ValueError:
##        print("숫자를 입력해주세요.")
##

##number = 1234
##name = "Alice"
##pi = 3.14159
##
##print(f"정수: {number:d}")  # 출력: 정수: 1234
##print(f"문자열: {name:s}")  # 출력: 문자열: Alice
##print(f"지수 표기법: {pi:e}")  # 출력: 지수 표기법: 3.141590e+00
##print(f"퍼센트: {pi:.2%}")  # 출력: 퍼센트: 314.16%

import math

print(f"퍼센트 :{math.pi:.2%}")



