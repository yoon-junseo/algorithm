#========================
#도입부(통화하기)

print ("따르르릉 따르르릉")
print ("전화가 울린다. 확인해보니 동생이다.")
a= "네"
b= input ("전화를 받으시겠습니까?(네/아니요)")
if b ==  a:
    print("전화를 받았습니다.")
else:
    print("전화를 거절했습니다.")
    exit(0)
print("나 : 여보세요?")
print("동생 : 언니! 오늘 엄마 생신이셔!")
print("'큰일났다. 엄마의 생신을 까먹어버렸다.'")
print("언니! 빨리 엄마의 서프라이즈 생신파티를 준비하자!")
a= "네"
b= input ("엄마의 서프라이즈 생신파티를 준비하시겠습니까?(네/아니요)")
if b == a:
    print("얼른 파티를 준비하자!")
else:
    print("끝까지 까먹은 척 한다.")
    exit(0)

print("나 : 내가 엄마가 좋아하시는 쿠키 사가지고 갈게!")

#=================================================
#쿠키가게

print("쿠키 가게에 도착했다.")
print("쿠키 가게 사장님 : 엇 지금 쿠키가 다 나가서 초코,바닐라,딸기 쿠키 모두 굽고 있어요!")
print("나 : 각각 얼마나 걸리나요?")
print("쿠키 가게 사장님 : 각각 3분, 6분, 19분 걸립니다.")

marks = [3, 6, 19]

number = 0
chocoCookie = int(17000)
vinyl = int(3000)
box = int(5000)

for mark in marks:
    number = number +1
    if mark < 5:
        print("나 : %d번째 쿠키로 주세요." % number)
    else:
        print("%d번째는 너무 오래걸려서 구매할 수 없어요." % number)

print("쿠키 가게 사장님 : 네. 초코쿠키는 17000원 입니다. 포장하시겠어요?")
print("포장은 3000원짜리 비닐 포장과 5000원짜리 박스 포장이 있습니다.")
print("나는 쿠키를 사기 위한 예산으로 2만원이 있다.")

marks = [chocoCookie + vinyl, chocoCookie + box]

number = 0
for mark in marks:
    number = number +1
    if mark <= 20000:
        print("나 : %d번째 포장법으로 해주세요." % number)
    else:
        print("%d번째는 예산을 초과해서 할 수 없어요." % number)

#===========================================================
#장면전환

print("또 동생에게 전화가 왔다.")
print("언니! 엄마 20분 뒤에 집에 도착하신대!")
#===========================================================
#급하게 진행해야하는 긴급한 상황

a= 3000
b= int(input ("현재 주머니에 얼마가 있습니까?"))

if b >= a :
    print("택시를 타고 가세요")
else:
     print("뛰어가세요")
#===========================================================
#택시에서 내린 후 

print ("집에 도착했다. 엘리베이터를 타자!")

c= int(input ("당신은 몇층에 사나요?"))

for i in range(1, c + 1):
    print (i)
print(c, "층에 도달했습니다. 어서 집으로 가세요!")
print("집 앞에 도착했다. 비밀번호를 입력했으나 비밀번호가 틀렸단다. 기회는 5번이 있다.")

password_try = 0
while password_try < 5:
     password_try = password_try + 1
     print("현관 비밀번호 입력을 %d번 시도했습니다." % password_try)
     if password_try == 5:
        print("띠리링 열렸습니다.")

print ("집에 들어와서 허겁지겁 준비한다.")

#============================================================
#엄마가 집에 도착했다. (마무리)

print("초인종이 울린다. 엄마가 도착하셨나보다.")

condition = True

while condition:
    status = input("서프라이즈 파티 준비가 완료됐나요?(네/아니요)")
    
    if status == "네":
        print("엄마 어서 들어오세요!  라고 말하면서 문을 열어드린다.")
        condition = False
    else:
        print("엄마 잠깐만 기다려줘~")
        
#========================================================
#이야기 끝내기

print("엄마께서 감동의 눈물을 흘리신다.")
print("내게도 서프라이즈였던 사랑하는 우리 엄마의 서프라이즈 생신 파티는 성공적이다. 다음부터는 까먹지 말고 미리미리 준비하자!")





