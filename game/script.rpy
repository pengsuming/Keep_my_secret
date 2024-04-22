# 커밋 테스트


init:
    image ara = "images/char/ara.png"
    image siu = "images/char/siu.png"
    image Yeoju = "images/char/여주.png"

    image bg river = "images/bg/river.jpg"
    image bg room = "images/bg/room.jpg"

    define 아라 = Character("아라", color="#ff3352")
    define 시우 = Character("시우", color="33d4ff")
    define 여주 = Character("여주", color="ffffff")

    #
    define bunker = 0


label start:

    scene bg room with fade

    "테스트중이라요~~~~"

    show Yeoju

    여주 "콩깎지 넌 방구뿡이야"

    hide Yeoju

    아라 "어쩔티비"
    "피자 먹고 싶네욤"

    menu:
        "피자 시킨다":
            jump doit
        "피자 안 시킨다":
            jump dontdoit

            call doit

    "과연 결과는?"

label doit:
    "피자 시켰지연~~~~~~~~~"


    return

label dontdoit:
    "안 시킨다는 선택지는 없지연~~~~~~~~~~~"


    return


