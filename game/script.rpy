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

    menu:
        "지금은 내가 바빠서..\n학교 끝나고 나서 얘기하자!":
            jump doit
        "(무시)":
            jump dontdoit
        "그래.. 무슨 일이야?":
            jump doit


label doit:
    "지금은 내가 바빠서..\n학교 끝나고 나서 얘기하자!"


    return

label dontdoit:
    "(무시해버리기~)"


    return


