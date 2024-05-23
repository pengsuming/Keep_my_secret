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

    image bg school = "images/bg/school.jpg"
    image bg lobby = "images/bg/lobby.jpg"
    image bg playground = "images/bg/playground.jpg"


    define 여주 = Character("여주", color="000000")
    define 김완자 = Character("김완자", color="000000")
    define 이푸준 = Character("이푸준", color="000000")
    define 한두부 = Character("한두부", color="000000")

    #
    define bunker = 0


label start:

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

    여주 "완자 친구들이다!! 완자도 축구 엄청 좋아하는데 ㅠㅠ"
    여주 "쟤네 무슨 일 있나..? 표정이 되게 안 좋아 보이네"

    "야 김완자 오늘도 축구 빠지냐..?"
    "ㅇㅇ 요즘 학교 계속 빠지고 연락도 안됨"
    "아 잠수탔네.. \n야야 저기 여친 지나간다 물어보자"
    "거기 잠깐만! 요즘 왜 완자 학교에 안 나오냐?"

    show Yworry

    여주 "어.. 그게.. 그럴만한 사정이 있어서 그래!"
    여주 "'완자가 싼다수로 변했다고는 절대 말하지 말자..'"
    여주 "너네 쓰레기 아무데나 버리지마!!\n쓰레기 되고 싶지 않으면!! 절대로!!"

    hide Yworry

    "뭐? 갑자기 웬 쓰레기? 잠깐!! 아니 김완자는 어디갔는데..!!"

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

#     menu:
#         "지금은 내가 바빠서..\n학교 끝나고 나서 얘기하자!":
#             jump 푸준1
#         "(무시)":
#             jump 푸준2
#         "그래.. 무슨 일이야?":
#             jump doit


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

#     menu:
#         "완자야 우린 영원히 함꼐야 Forever.":
#             jump
#         "미안해.. 나도 확실하게 대답 못해주겠어..":
#             jump



