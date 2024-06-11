# 커밋 테스트
# 다시 테스트


init:

    image Yeoju = "images/char/여주.png"
    image Yworry = "images/char/걱정.png"
    image Yhate = "images/char/극혐.png"
    image Yhappy = "images/char/기쁨.png"
    image Ysurprise = "images/char/놀람.png"
    image Yanger = "images/char/분노.png"
    image Ythink = "images/char/생각.png"
    image Yrelieve = "images/char/안도.png"

    image Kim = "images/char/완자.png"
    image Kworry = "images/char/완자_걱정.png"
    image Ksad = "images/char/완자_슬픔.png"
    image Krelieve = "images/char/완자_안심.png"

    image dragon = "images/char/용.png"
    image friends = "images/char/친구들.png"

    image bg school = "images/bg/school.jpg"
    image bg lobby = "images/bg/lobby.jpg"
    image bg playground = "images/bg/playground.jpg"

    image bg pro1 = "images/prologue/1_S122.jpg"
    image bg pro2 = "images/prologue/2_S3.jpg"
    image bg pro3 = "imagas/prologue/3_S4.jpg"
    image bg pro4 = "imagas/prologue/4_S5.jpg"
    image bg pro5 = "imagas/prologue/5_S6.jpg"
    image bg pro6 = "imagas/prologue/6_S62.jpg"
    image bg pro7 = "imagas/prologue/7_S106.jpg"
    image bg pro8 = "images/prologue/8_S114.jpg"
    image bg pro9 = "images/prologue/9_S118.jpg"
    image bg pro10 = "imagas/prologue/10_S7.jpg"
    image bg pro11 = "imagas/prologue/11_S9.jpg"
    image bg pro12 = "imagas/prologue/12_S10.jpg"
    image bg pro13 = "imagas/prologue/13_S11.jpg"
    image bg pro14 = "imagas/prologue/14_S66.jpg"
    image bg pro15 = "images/prologue/15_74.jpg"
    image bg pro16 = "images/prologue/16_S94.jpg"
    image bg pro17 = "imagas/prologue/17_S98.jpg"
    image bg pro18 = "imagas/prologue/18_S102.jpg"
    image bg pro19 = "imagas/prologue/19_S12.jpg"
    image bg pro20 = "imagas/prologue/20_S14.jpg"
    image bg pro21 = "imagas/prologue/21_S15.jpg"

    image bg pro22 = "imagas/prologue/12_S10.jpg"
    image bg pro23 = "imagas/prologue/13_S11.jpg"
    image bg pro24 = "imagas/prologue/14_S66.jpg"
    image bg pro25 = "images/prologue/1_S122.jpg"
    image bg pro26 = "images/prologue/2_S3.jpg"
    image bg pro27 = "imagas/prologue/3_S4.jpg"
    image bg pro28 = "imagas/prologue/4_S5.jpg"


    define 여주 = Character("여주", color="000000")
    define 김완자 = Character("김완자", color="000000")
    define 이푸준 = Character("이푸준", color="000000")
    define 한두부 = Character("한두부", color="000000")
    define 용 = Character("용", color="000000")
    define 친구들 = Character("친구들", color="000000")
    define 싼다수 = Character("싼다수",color="000000")
    #
    define bunker = 0

# 여주인공 이름 입력받기
label name_input:
    $ 여주이름 = renpy.input("여주인공의 이름을 입력하세요.")
    $ 여주이름 = 여주이름.strip()
    if 여주이름 == "":
        $ 여주이름 = "여주"
    $ 여주 = Character(여주이름, color="000000")
    return


label start:
    call name_input

    #프롤로그
    show bg school
    "이곳은 바다가 보이는 학교,푸른 고등학교."
    show Yeoju
    "나, 김여주 올해 고2가 되었다."
    여주 "나에게는 아주 소중한 남자친구 김완자가 있다."
    여주 "그런데 이틀째 학교에 나오지 않는 완자, 혹시 무슨일이라도 생긴걸까?"
    여주 "완자는 나에게 말도 없이 연락도 안보고, 학교에도 나오지 않는다. 담임선생님께서도 모른다고 하셨다."
    "여주는 하교 후 완자네 집으로 향했다."
    scene bg school with fade
    "띵동"
    show Yworry
    여주 "완자야 나왔어ㅠㅠ 문 좀 열어봐."
    hide Yworry
    "그러나 여주의 몇번의 부름에도 완자는 굳게 닫힌 문은 열리지 않았다."
    show Yanger
    여주 "그렇다고 내가 못 열 것 같아?(완자의 집 열쇠를 꺼내들며)"
    hide Yanger
    "철컥"
    show Ysurprise
    여주 "어라...완자가 없잖아?"
    hide Ysurprise
    "여주의 눈앞에는 항상 완자가 즐겨마시던 싼다수가 바닥에 놓여있었다."
    show Ythink
    여주 "완자는 어디로 간 거지?"
    hide Ythink
    "여주는 완자의 방에도 들어가보았지만, 사람의 인기척이 느껴지지 않는 빈 방일 뿐이었다."
    "그때, 바닥에 놓여있었던 싼다수가 말을 하기 시작했다."
    show Ksad
    싼다수 "여주야 살려줘"
    hide Ksad
    show Ysurprise
    여주 "응...? 왜 싼다수에게서 완자 목소리가 들리지?"
    여주 "너무 놀란 나는 정신없이 집으로 뛰어갔다."
    hide Ysurprise
    "다음날이 되고, 오늘도 완자는 학교에 오지 않았다."
    show Ythink
    여주 "어제는 정말 뭐였지..."
    hide Ythink
    show Krelieve
    "그렇게 6교시가 끝날 무렵...어디선가 거친 숨소리가 들렸다."
    "이제는 부정할 수 없었다. 저건 틀림없이 내 남자친구 완자였다."
    hide Krelieve
    #프롤로그 끝

    python:
        import subprocess
        subprocess.Popen(["python", "main.py"])

label start2:

    "쉬는 시간 종이 치자마자 나는 싼다수로 변한 완자를 들고 서둘러 복도 끝으로 뛰어갔다. "
    "여주는 숨이 차지만, 차분히 완자의 말을 들어보기로 했다."
    김완자 "여주야 놀라지 말고 들어... 내가 싼다수로 변해버렸어ㅠㅠ"
    여주 "어째서?"
    김완자 "내가 싼다수를 마시고 바다에 던진적이 있는데, 용왕님이 분노하셔서 나에게 저주를 걸어버렸어."
    여주 "어떤 저주?"
    김완자 "쓰레기를 함부로 버린 모든 사람들이 자신이 버린 쓰레기로 변해버리는 저주야."
    여주 "어…? 잠깐, 쓰레기를 함부로 버린 모든 사람!?!?"
    "( 여주의 머릿속에는 두명의 남자들과 바닷가에서 놀며 쓰레기를 버리고 온 장면이 스쳐 지나간다.)"
    여주 "아악!! 이걸 어쩌면 좋지? 자칫하면 나까지 쓰레기로 변해버리겠어. "
    여주 "어떻게 하면 내가 살 수 있…아니아니, 너를 살릴 수 있는 거야? "
    "펑!?!"
    "무언가 터지는 큰 소리와 함께 바닷속에서 거대한 용이 눈앞에 나타났다. "
    용 "자 뽑아라. 네가 아이스크림 막대기를 함부로 버리는걸 알고 있다. 너의 남자친구가 저주로 인해 쓰레기로 변한건 알고 있겠지? 곧 너도 그렇게 될것이다. "
    여주 "안돼요!"
    용 "너의 남자친구와 주변 친구들, 그리고 너자신이 저주에 걸리는 것을 피하고 싶다면 한가지 방법이 있지"
    여주 "그게 뭐죠?"
    용 "이 뽑기통에서 뽑은 숫자만큼의 쓰레기를 주우면 된다. 정말 간단하지 않은가?"
    여주"(내가 저주에 걸리지 않으려면…) 뽑을게요!"
    용" (뽑기통을 내민다) "
    여주"(침을 삼키며)낮은 숫자도 있는 거죠? "
    "(뽑기 화면으로 전환한다.)"

    "여주는 손에 잡힌 종이를 펼쳐 숫자를 확인했다."
    여주 "167…?"
    "평소 자신을 요정이라고 생각하는 여주는 167개의 쓰레기를 주워야 한다는 사실에 충격을 받아 기절을 하고 만다."
    "(다음날)"
    여주 "어? 내가 언제 잠들었지…? 기억이 안나…"
    김완자 "여주야 일어났구나.. 하루를 꼬박 기절해 있어서 걱정했어. 괜찮아? "
    "(어제 있었던 일을 설명) "
    "여주는 167개의 쓰레기를 주워야 한다는 사실이 정말이라는 것에 충격을 받았다."
    여주 "그래, 내가 용왕의 조건을 받아들이지 않는다면 내 주변 사람들까지 저주를 받아 쓰레기로 변해버릴 거야. 나중에는 나까지 쓰레기로 변하게 되겠지…"
    여주 "그래! 결심했어. 쓰레기를 주워서 환경을 지키고 모두의 저주를 풀어주겠어."

    scene bg school with fade

    여주 "'걱정이 가득한 마음으로 학교로 향했다..'"

    scene bg lobby with fade

    show Yworry

    여주 "막상 학교로 오긴 했지만 167개를 언제 다 줍는담 ㅠㅠ 막막하다.."

    hide Yworry
    show Yeoju

    여주 "학교 운동장 쪽에 쓰레기가 많았던 것 같은데..\n 거기로 가봐야겠다!!"

    hide Yeoju

    scene bg playground with fade

    show Yeoju

    여주 "완자 친구들이다!! 완자도 축구 엄청 좋아하는데 ㅠㅠ"
    여주 "쟤네 무슨 일 있나..? 표정이 되게 안 좋아 보이네"

    hide Yeoju
    show friends

    친구들 "야 김완자 오늘도 축구 빠지냐..?"
    친구들 "ㅇㅇ 요즘 학교 계속 빠지고 연락도 안됨"
    친구들 "아 잠수탔네.. \n야야 저기 여친 지나간다 물어보자"
    친구들 "거기 잠깐만! 요즘 왜 완자 학교에 안 나오냐?"

    hide friends
    show Yworry

    여주 "어.. 그게.. 그럴만한 사정이 있어서 그래!"
    여주 "'완자가 싼다수로 변했다고는 절대 말하지 말자..'"
    여주 "너네 쓰레기 아무데나 버리지마!!\n쓰레기 되고 싶지 않으면!! 절대로!!"

    hide Yworry
    show friends

    "뭐? 갑자기 웬 쓰레기? 잠깐!! 아니 김완자는 어디갔는데..!!"

    hide friends
    show Yrelieve

    여주 "완자가 어디갔냐고..?\n완자는 지금 내 가방 속에 있다곤 절대 말 못해!!"
    여주 "헉.. 헉.. 아 숨찬다..\n여긴 아무도 없군. 얼른 쓰레기나 줍자"

    hide Yrelieve
    show Ysurprise

    여주 "어!!! 비닐봉지다!!!"

    hide Ysurprise
    show Yhappy

    여주 "아싸!! 득템이다!!"

    hide Yhappy

    "김여주! 나야.. 이푸준..! 내 얘기 좀 들어줘.."
    여주 "어..? 이 목소린 한달 전 헤어진 나의 X, 피규어 집착남 이푸준?!?!?!?!"

    menu:
        "있기야 하지~ 근데.. 내가 너를 도와줄 것 같아!?":
            jump 두부1
        "당연히 돌아갈 수 있지! 내가 도와줄게.":
            jump 두부2

label 두부1:
    show 한두부
    한두부 "나 도와주면 너 좋아하는 딸기 스무디 먹고 싶을때마다 사줄게 언제든지"
    hide 한두부

    show Ythink
    여주 "흠... 약한데..."
    hide Ythink

    show 한두부
    한두부 "야 친구끼리 좀 도와줘라.\n아 그래 딸기 스무디에 초코 케이크도 사줄게"
    hide 한두부

    show Yhappy
    여주 "오호..? 오키 콜!!!"
    hide Yhappy

    show Yeoju
    여주 "크크크.. 저주도 풀고 딸기 스무디랑 초코 케이크까지 얻어먹고야 만다 내가!!"
    hide Yeoju

    show Ythink
    여주 "근데 나 지금까지 쓰레기 몇개 주웠지..?!"
    hide Ythink

    show Ysurprise
    여주 "오왓!?!? 깜짝이야!!! 내 손목에 이건..?"
    hide Ysurprise

    show Yeoju
    여주 "요즘 세상 참 좋아졌네.. 신기하당\n그럼 이제 107개만 주우면 돼!"
    hide Yeoju

    show Yrelieve
    여주 "아 오늘 너무 힘들었다.. 일단 완자부터 꺼내주자!"
    hide Yrelieve

    show Yworry
    여주 "하루종일 답답했겠다. 완자야 괜찮아? ㅠㅠ"
    hide Yworry

    show 김완자
    김완자 "워후.. 숨막혀 하루종일 가방 안에 있으려니 좀 답답하네ㅠ"
    hide 김완자

    show Yworry
    여주 "ㅠㅠ 완자야 많이 힘들었지 내가 빨리 구해줄게!"
    hide Yworry

    show 김완자
    "'그러나 완자는 아무런 반응이 없다가 조심스럽게 나에게 말을 건넸다'"
    김완자 "만약에.. 내가 저주를 영영 풀지 못한데도 너는 나 계속 사랑해줄거야..?"

#     menu:
#         "완자야 우린 영원히 함꼐야 Forever.":
#             jump
#         "미안해.. 나도 확실하게 대답 못해주겠어..":
#             jump


label 두부2:
    show 한두부
    한두부 "그래 고맙다. 아휴.. 나도 이렇게 될줄 누가 알았겠냐."
    hide 한두부

    show Yrelieve
    여주 "그래. 이 저주를 푸려면 내가 쓰레기를 무려 167개나 주워야 한다고ㅠㅠ 지금 몇개나 주웠지?!?!"
    hide Yrelieve

    show Ysurprise
    여주 "오왓!?!? 깜짝이야!!! 내 손목에 이건..?"
    hide Ysurprise

    show Yeoju
    여주 "요즘 세상 참 좋아졌네.. 신기하당\n그럼 이제 107개만 주우면 돼!"
    hide Yeoju

    show Yrelieve
    여주 "하.. 오늘 쓰레기 주우러 너무 많이 돌아다녔더니 피곤하네\n일단 오늘은 여기까지만 하고 이만 집으로 돌아가야지!"
    hide Yrelieve

    scene home

    show Yrelieve
    여주 "'아 오늘 너무 힘들고 지친다..\n일단 완자부터 가방에서 꺼내주자! 하루종일 답답했겠다.'"
    hide Yrelieve

    show Yworry
    여주 "완자야 괜찮아..?"
    hide Yworry

    show 김완자
    김완자 "워후.. 숨막혀 하루종일 가방 안에 있으려니 좀 답답하네ㅠ"
    hide 김완자

    show Yworry
    여주 "'내가 오늘 완자를 신경 못 써줬네..'"
    여주 "ㅠㅠ 완자야 많이 힘들었지.. 내가 빨리 구해줄게!!!!"
    hide Yworry

    show 김완자
    "'그러나 완자는 아무런 반응이 없다가 조심스럽게 나에게 말을 건넸다.'"
    김완자 "만약에.. 내가 저주를 영영 풀지 못한데도 너는 나 계속 사랑해줄거야..?"

    menu:
        "완자야 우린 영원히 함꼐야 Forever.":
            jump dontdoit
        "미안해.. 나도 확실하게 대답 못해주겠어..":
            jump doit
#선택지 이후 (방)민서가 작성한 부분
label doit:
    "지금은 내가 바빠서..\n학교 끝나고 나서 얘기하자!"
    "종례후..."
    여주 "(주위를 둘러보며)여긴 아무도 없으니까..! 여기서 얘기하면 딱이겠다"
    이푸준 "내가 평소에 피규어 엄청 좋아했던거 알지..?"
    여주 "그래. 너 나랑 사귈때도 피규어 사느라 데이트 시간도 늦고 그랬었잖아 -_-"
    이푸준 "음.. 그건 미안했어, 근데 지금 더 큰일인데 내가 피규어 사서 뜯고 버린 비닐봉지를 함부로 버리다가 이렇게 쓰레기로 변하는 저주에 걸렸어."
    여주 "(한숨을 쉬며)하.. 그래 나도 지금 너희 저주 풀려고 엄청 노력하고 있다고.."
    이푸준 "너는 저주 푸는 방법을 알고 있는거지..? 나 좀 도와줄래??"
    여주 "그래.. 근데 혹시 또 저주 걸린 얘 알고 있어??"
    jump meet

label dontdoit:
    이푸준 "내가 평소에 피규어 엄청 좋아했던거 알지..?"
    여주 "그래. 너 나랑 사귈때도 피규어 사느라 데이트 시간도 늦고 그랬었잖아 -_-"
    "음.. 그건 미안했어, 근데 지금 더 큰일인데 내가 피규어 사서 뜯고 버린 비닐봉지를 함부로 버리다가 이렇게 쓰레기로 변하는 저주에 걸렸어."
    여주 "(한숨을 쉬며)하.. 그래 나도 지금 너희 저주 풀려고 엄청  노력하고 있다고.."
    이푸준 "너는 저주 푸는 방법을 알고 있는거지..? 나 좀 도와줄래?"
    여주 "그래.. 근데 혹시 또 저주 걸린 얘 알고 있어?"
    jump meet

label meet:
    이푸준 "음…나도 잘은 모르지만 근처에 또 있지 않을까…?  "

    여주 "(곰곰히 생각하며) 그래…누군가 또 쓰레기로 변했겠지…우선 집가는 길 방향부터 살펴보자! "
    여주 "아 근데 목마르다. 스타벅벅긁스에서 딸기 스무디 한잔 마시고 해야지 ㅎㅎ 완자가 전에 선물로 줬던 기프티콘 써야겠다. "
    여주  "(발걸음을 멈추며) 아니, 여기 앞에 플라스틱 컵이 왜 굴러다닌담?! 마치 주워달라는 것 같네 ㅋㅋㅋ 이것도 주워야겠군. "
    "그 순간, 플라스틱 컵이 말을 했다! "
    한두부   "야…김여주.. 나 알아보겠냐…? "
    여주  "엥?! 이 목소린..알고 지낸지만 무려 10년이 된 나의 남사친 카페인 중독자 한두부?!?! "
    한두부  "(한숨을 쉬며)하… 그래 나야. 커피마시고 있다가 갑자기 이렇게 됐는데 이거 왜 그런거냐…? "
    한두부  "(아리송한 표정으로) 내가 뭘 잘못했나…?  "
    한두부  "나… 돌아갈 수 있는거냐…? "

