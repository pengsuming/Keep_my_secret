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

    image Lee = "images/char/푸준.png"
    image Lhappy = "images/char/푸준_기쁨.png"
    image Lsad = "images/char/푸준_슬픔.png"
    image Lrelieve = "images/char/푸준_안심.png"

    image Han = "images/char/두부.png"
    image Hhappy = "images/char/두부_기쁨.png"
    image Hsad = "images/char/두부_슬픔.png"
    image Hrelieve = "images/char/두부_안심.png"

    image dragon = "images/char/용.png"
    image friends = "images/char/친구들.png"

    image bg school = "images/bg/school.jpg"
    image bg lobby = "images/bg/lobby.jpg"
    image bg playground = "images/bg/playground.jpg"

    image bg pro1 = "images/prologue/1_S122.jpg"
    image bg pro2 = "images/prologue/2_S3.jpg"
    image bg pro3 = "images/prologue/3_S4.jpg"
    image bg pro4 = "images/prologue/4_S5.jpg"
    image bg pro5 = "images/prologue/5_S6.jpg"
    image bg pro6 = "images/prologue/6_S62.jpg"
    image bg pro7 = "images/prologue/7_S106.jpg"
    image bg pro8 = "images/prologue/8_S114.jpg"
    image bg pro9 = "images/prologue/9_S118.jpg"
    image bg pro10 = "images/prologue/10_S7.jpg"
    image bg pro11 = "images/prologue/11_S9.jpg"
    image bg pro12 = "images/prologue/12_S10.jpg"
    image bg pro13 = "images/prologue/13_S11.jpg"
    image bg pro14 = "images/prologue/14_S66.jpg"
    image bg pro15 = "images/prologue/15_74.jpg"
    image bg pro16 = "images/prologue/16_S94.jpg"
    image bg pro17 = "images/prologue/17_S98.jpg"
    image bg pro18 = "images/prologue/18_S102.jpg"
    image bg pro19 = "images/prologue/19_S12.jpg"
    image bg pro20 = "images/prologue/20_S14.jpg"
    image bg pro21 = "images/prologue/21_S15.jpg"
    image bg pro22 = "images/prologue/22_S16.jpg"
    image bg pro23 = "images/prologue/23_S70.jpg"
    image bg pro24 = "images/prologue/24_S78.jpg"
    image bg pro25 = "images/prologue/25_S82.jpg"
    image bg pro26 = "images/prologue/26_S86.jpg"
    image bg pro27 = "images/prologue/27_S90.jpg"
    image bg pro28 = "images/prologue/28_S17.jpg"
    image bg pro29 = "images/prologue/29_S28.jpg"
    image bg pro30 = "images/prologue/30_S29.jpg"
    image bg pro31 = "images/prologue/31_S30.jpg"
    image bg pro32= "images/prologue/32_S64.jpg"
    image bg pro33 = "images/prologue/33_S108.jpg"
    image bg pro34 = "images/prologue/34_S112.jpg"
    image bg pro35 = "images/prologue/35_S116.jpg"
    image bg pro36 = "images/prologue/36_S120.jpg"

    define 여주 = Character("여주", color="000000")
    define 김완자 = Character("김완자", color="000000")
    define 이푸준 = Character("이푸준", color="000000")
    define 한두부 = Character("한두부", color="000000")
    define 용 = Character("용", color="000000")
    define 친구들 = Character("친구들", color="000000")
    define 싼다수 = Character("싼다수", color="000000")
    define 비닐봉지 = Character("비닐봉지", color="000000")
    define 플라스틱컵 = Character("플라스틱컵", color="000000")

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

    #프롤로그 시작
    show bg pro1
    "이곳은 바다가 보이는 학교,푸른 고등학교."
    show bg pro2
    여주 "올해 나는 고2가 되었다."
    show bg pro3
    여주 "나에게는 아주 소중한 남자친구 김완자가 있다."
    show bg pro4
    여주 "그런데 이틀째 학교에 나오지 않는 완자.. 혹시 무슨일이라도 생긴걸까..?"
    show bg pro5
    여주 "완자는 나에게 말도 없이 연락도 안보고, 학교에도 나오지 않는다. 담임선생님께서도 모른다고 하셨다."
    show bg pro6
    여주 "내 남자친구는 내가 지킨다!! 완자 집으로 찾아가야겠어!!"
    show bg pro7
    "하교 후 곧장 완자네 집으로 향했다."
    show bg pro8
    "띵동"
    여주 "완자야 나 왔어 ㅠㅠ 문 좀 열어봐....!!!!!!"
    show bg pro9
    "그러나 여주의 몇번의 부름에도 완자는 문을 열어주지 않았다.."
    show bg pro10
    여주 "ㅋ그렇다고 내가 못 열 것 같나\n완자의 집 열쇠는 이미 훔친지 오래다."
    "철컥"
    show bg pro11
    "어라...완자는 없고 항상 완자가 즐겨마시던 싼다수가 눈앞에 있다.."
    여주 "완자는 어디로 간 거지?"
    show bg pro12
    "완자의 방에도 가보았지만, 완자는 없는 빈 방일 뿐이였다."
    "그때, 바닥에 놓여있었던 싼다수가 말을 하기 시작했다."
    show bg pro13
    싼다수 "여주야.. 사,살려줘.."
    show bg pro14
    여주 "응...? 왜 싼다수에게서 완자 목소리가 들리지?"
    show bg pro15
    "너무 놀란 나는 정신없이 집으로 뛰어갔다."
    show bg pro16
    "다음날이 되고, 오늘도 완자는 학교에 오지 않았다..\n어제는 정말 뭐였지.."
    show bg pro17
    "그렇게 6교시가 끝날 무렵..\n어디선가 거친 숨소리가 들려왔다."
    show bg pro18
    싼다수 "헉..헉..후.."
    "이제는 부정할 수 없었다. 저건 틀림없이 내 남자친구 완자다."
    show bg pro19
    "쉬는시간 종이 치자마자 나는 싼다수로 변한 완자를 들고 서둘러 복도 끝으로 뛰어갔다."
    show bg pro20
    "뛰어서 숨이 차지만, 차분하게 완자의 말을 들어보기로 했다."
    싼다수 "여주야 놀라지 말고 들어..\n나.. 보이는 것처럼 싼다수로 변했어 ㅠㅠ"
    싼다수 "내가 평소에 싼다수 마시고 바닥에 던져놨잖아.\n그걸 본 바다에 사는 용왕님이 분노해서 나에게 쓰레기로 변하는 저주를 내렸어 ㅠㅠ"
    싼다수 "쓰레기를 함부로 버린 모든 사람에게 저주가 내려질거래..ㅠㅠ"
    show bg pro21
    "어..? 잠시만 쓰레기를 함부로 버린 '모든' 사람?!?!??!!"
    show bg pro22
    "그때 머릿속에 스쳐지나가는 두 명의 남자.."
    show bg pro23
    여주 "아악!! 이걸 어쩌면 좋지?!?!?!?"
    show bg pro24
    여주 "어떻게 하면 내가 살 수 있..ㅇ\n아니..너를 살릴 수 있어? (나만 아니면 돼)"
    show bg pro25
    "그 순간, 무언가 펑 터지는 큰 소리와 함께 바닷속에서 거대한 용이 나타나 나에게 뽑기통을 건넸다."
    show bg pro26
    용 "자 뽑아라. 네가 아이스크림 막대기를 함부로 버리는 걸 알고 있다.\n너의 남자친구가 저주로 인해 쓰레기로 변한건 알고 있지? 곧 너도 그렇게 될거다"
    show bg pro27
    용 "너의 남자친구와 주변 친구들, 그리고 너 자신의 저주도 피하고 싶다면, 이 뽑기통에서 뽑은 숫자만큼의 쓰레기를 주우면 돼. 간단하지?\n단 무슨 숫자가 나올진 모른다."
    show bg pro28
    여주 "낮은 숫자도 있는거죠..? 제발!!!!!!!!!!!"
    show bg pro29
    여주 "아 @^!ㅃ#$ 망했네."
    용 "운도 더럽게 없군. 수고해라. 지켜보고 있으니 허튼 짓은 소용 없다."
    show bg pro30
    여주 "아.. 아니야.. 이건 꿈일거야..\n귀엽고 예쁜 내게 왜 이런 일이.. 안돼!!!!!!!"
    show bg pro31
    "평소 자신을 요정이라고 생각하는 여주는 '167'개의 쓰레기를 주워야 한다는 망연자실한 사실에 그만.. 순간적회피성 기절을 하고 만다.."
    "다음날"
    show bg pro32
    여주 "우어.. 내가 언제 잠들었지.. 기억이 안나.."
    show bg pro33
    싼다수 "여주야 너 용왕님 만나서 저주 풀기 위해 쓰레기 줍는 뽑기 하고 뽑은 수가 너무 높아서 그 충격에 갑자기 쓰러졌었어.. 괜찮아..?ㅠㅠ"
    show bg pro34
    "완자의 말을 들은 여주는 믿고 싶지 않은 현실이 기억났다."
    show bg pro35
    여주 "그래 내가 그동안 함부로 버린 쓰레기에 대한 엄청난 벌이야..\n내 주변사람들까지도 쓰레기를 함부로 버리고 저주로 인해 모두 변해버렸지..\n그리고 곧 나도 그렇게 될거야.. 이제 어쩌면 좋지.."
    show bg pro36
    여주 "정신차려 나 자신!! 결심했어..!\n모두의 저주도 풀어주고 환경을 지키기로..!!!"
    #프롤로그 끝

    python:
        import subprocess
        subprocess.Popen(["python", "main.py"])

label start2:

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
    친구들 "뭐? 갑자기 웬 쓰레기? 잠깐!! 아니 김완자는 어디갔는데..!!"
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

    비닐봉지 "김여주! 나야.. 이푸준..! 내 얘기 좀 들어줘.."
    show Ysurprise
    여주 "어..? 이 목소린 한달 전 헤어진 나의 X, 피규어 집착남 이푸준?!?!?!?!"
    hide Ysurprise
    show Lee
    비닐봉지 "잠깐!! 김여주!! 나야 이푸준.. 내 얘기 좀 들어줘.."

    menu:
        "지금은 내가 바빠서.. 학교 끝나고 나서 얘기하자!":
            jump 푸준1
        "(무시)":
            jump 푸준2
        "그래.. 무슨 일이야?":
            jump 푸준2

label 푸준1:
    "종례후..."
    show Yeoju
    여주 "'여긴 아무도 없으니까..! 여기서 얘기하면 딱이겠다'"
    여주 "자 이제 아무도 없으니까 얘기해"
    hide Yeoju

    show Lee
    비닐봉지 "그래.."
    hide Lee
    jump 푸준2

label 푸준2:
    show Lee
    비닐봉지 "내가 평소에 피규어 엄청 좋아했던 거 알지..?"
    hide Lee

    show Yrelieve
    여주 "그래. 너 나랑 사귈때도 피규어 사느라 데이트 시간도 늦고 그랬었잖아 -_-"
    hide Yrelieve

    show Lsad
    비닐봉지 "응.. 그건 미안했어. 근데 지금 더 큰일인게 내가 피규어 사서 뜯고 버린 비닐봉지를 함부로 버리다가 이렇게 쓰레기로 변하는 저주에 걸렸어.."
    hide Lsad

    show Yrelieve
    여주 "하.. 그래 나도 지금 너희 저주 풀려고 엄청 노력하고 있다고.."
    hide Yrelieve

    show Lsad
    비닐봉지 "너는 저주 푸는 방법을 알고 있는거지..? 나 좀 도와줄래..?"
    hide Lsad

    show Yrelieve
    여주 "그래.. 근데 혹시 또 저주 걸린 얘 알고 있어??"
    hide Yrelieve

    show Lee
    비닐봉지 "음.. 나도 잘은 모르지만 근처에 또 있지 않을까?"
    hide Lee

    show Ythink
    여주 "그래.. 누군가도 또 쓰레기로 변했겠지.."
    hide Ythink

    show Yeoju
    여주 "우선 집 가는 길 방향부터 살펴보자!"
    hide Yeoju

    show Yhappy
    여주 "아 근데 목마르다. 스타벅벅긁스에서 딸기스무디 한잔 마시고 해야지 ㅎㅎ\n완자가 전에 선물로 줬던 기프티콘 써야겠당 ㅎ"
    hide Yhappy

    "멈칫"

    show Yeoju
    여주 "아니, 여기 앞에 뭔 플라스틱컵이 굴러다닌담?!\n마치 주워달라는 것 같네 ㅋ 이것도 주워야겠군"
    hide Yeoju

    "그 순간, 플라스틱컵이 말을 했다!"

    show Han
    플라스틱컵 "야..김여주..나 알아보겠냐..?"
    hide Han

    show Ysurprise
    여주 "'엥?! 이 목소린.. 알고 지낸지만 무려 10년이 된 나의 남사친 카페인 중독자 한두부?!?!'"
    hide Ysurprise

    show Hsad
    플라스틱컵 "하.. 그래 나야. 커피 마시고 있다가 갑자기 이렇게 됐는데 이거 왜 그런거냐..?"
    플라스틱컵 "내가 뭘 잘못했나..?"
    플라스틱컵 "나.. 돌아갈 수 있는거냐..?"
    hide Hsad

    menu:
        "있기야 하지~ 근데.. 내가 너를 도와줄 것 같아!?":
            jump 두부1
        "당연히 돌아갈 수 있지! 내가 도와줄게.":
            jump 두부2

label 두부1:
    show Hrelieve
    한두부 "나 도와주면 너 좋아하는 딸기 스무디 먹고 싶을때마다 사줄게 언제든지"
    hide Hrelieve

    show Ythink
    여주 "흠..약한데.."
    hide Ythink

    show Hrelieve
    한두부 "야 친구끼리 좀 도와줘라. 아 그래 딸기 스무디에 초코 케이크도 사줄게"
    hide Hrelieve

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
    여주 "요즘 세상 참 좋아졌네.. 신기하당 ㅎ\n그럼 이제 107개만 주우면 돼!"
    hide Yeoju

    show Yrelieve
    여주 "하.. 오늘 쓰레기 주우러 너무 많이 돌아다녔더니 피곤하네..\n일단 오늘은 여기까지만 하고 이만 집으로 돌아가야지!"
    hide Yrelieve

    "집으로 돌아왔다"

    show Yrelieve
    여주 "아 오늘 너무 힘들었다.. 일단 완자부터 가방에서 꺼내주자!"
    hide Yrelieve

    show Yworry
    여주 "완자야 괜찮아? ㅠㅠ 하루종일 답답했겠다ㅠㅠ"
    hide Yworry

    show Krelieve
    김완자 "워후.. 숨막혀 하루종일 가방 안에 있으려니 좀 답답하네ㅠ"
    hide Krelieve


    show Yworry
    여주 "'내가 오늘 완자를 신경 못 써줬네..'"
    여주 "ㅠㅠ 완자야 많이 힘들었지.. 내가 빨리 구해줄게!!!!"
    hide Yworry

    show Kworry
    "그러나 완자는 아무런 반응이 없다가 조심스럽게 나에게 말을 건넸다"
    김완자 "만약에.. 내가 저주를 영영 풀지 못한데도 너는 나 계속 사랑해줄거야..?"
    hide Kworry

    menu:
        "완자야 우린 영원히 함께야 Forever.":
            jump 완자1
        "미안해.. 나도 확실하게 대답 못해주겠어..":
            jump 완자2

label 완자1:
    show Ksad
    싼다수 "ㅠㅠㅠ 여주야 진짜 고마워 ㅠㅠㅠ\n역시 난 너 밖에 없어"
    hide Ksad

    show Kim
    싼다수 "혹시 내가 도울 일이 있다면 언제든지 말해줘!"
    싼다수 "잘자고 내일도 힘내서 열심히 해보자!!"
    hide Kim

    show Yeoju
    여주 "응 완자야 너가 빨리 돌아왔으면 좋겠어.."
    hide Yeoju

    "여주는 스르륵 잠에 든다.."

    "꿈 속"
    용 "큼큼ㅋ 군말없이 잘 하고 있는 걸 보아 내가 너에게 한가지 꼼수를 알려주고자 이곳에 왔다."
    용 "매일 니가 원할때마다 미니게임을 통해 저주를 더욱 빨리 풀 수 있도록 해주마."
    여주 "헐... 정말요?? 진짜 대박 감사!!"
    용 "그래그래 열심히 하거라. 하지만 네가 모르는 것 같아서 알려두는데..."
    용 "마지막에 원래 모습으로 돌려두는 것은 한사람만 가능하다는 걸 알아두도록 해.\n이미 외형이 변한 자는 정말 엄청난 양의 쓰레기를 버려서 저주에 걸렸다는 사실을 잊지 말거라."
    여주 "네..?? 아니 그런게 어딨어요 아니 잠시만 어디가세요..!!!!"
    용 "그럼 20000"
    여주 "허어어억!!!! 뭐야 꿈이였잖아.."
    여주 "그나저나 한명만 살릴 수 있다니.."

    여주 "어제 완자한테 그렇게 말하면 안됐나.. 확실한 것도 아닌데.."
    jump MinigameTime

label 완자2:
    show Kworry
    싼다수 "아.. 알겠어.. 일단 너가 쓰레기로 변하지 않는게 제일 중요하니까 난 이해해"
    싼다수 "힘내.."
    hide Kworry

    show Yrelieve
    여주 "응.."
    hide Yrelieve

    "(그대로 스르륵 잠에 든다)"

    "꿈 속"
    용 "큼큼ㅋ 군말없이 잘 하고 있는 걸 보아 내가 너에게 한가지 꼼수를 알려주고자 이곳에 왔다."
    용 "매일 니가 원할때마다 미니게임을 통해 저주를 더욱 빨리 풀 수 있도록 해주마."
    여주 "헐... 정말요?? 진짜 대박 감사!!"
    용 "그래그래 열심히 하거라. 하지만 네가 모르는 것 같아서 알려두는데..."
    용 "마지막에 원래 모습으로 돌려두는 것은 한사람만 가능하다는 걸 알아두도록 해.\n이미 외형이 변한 자는 정말 엄청난 양의 쓰레기를 버려서 저주에 걸렸다는 사실을 잊지 말거라."
    여주 "네..?? 아니 그런게 어딨어요 아니 잠시만 어디가세요..!!!!"
    용 "그럼 20000"
    여주 "허어어억!!!! 뭐야 꿈이였잖아.."
    여주 "그나저나 한명만 살릴 수 있다니.."

    여주 "내가 어제 말한대로 확실하게 대답하면 안되는게 맞았어..\n완자는 그렇다 치고 나머지 애들은 어쩌면 좋지ㅠㅠ"
    jump MinigameTime

label MinigameTime:
    여주 "하아.. 복잡하다ㅜ"
    여주 "일단.. 다 줍고 나서 생각하는게 맞을 것 같아.."
    여주 "오늘도 힘내보자!! 할수있다 김여주!!!"

    # 미니게임 하기

    여주 "내가 드디어 다 모으다니!!!!!!!"
    여주 "하.. 이제 최종 선택의 날이네.\n세 남자 중 한 명만 되돌릴 수 있다라.."
    여주 "누굴 되돌려야하지.. 정말 고민된다.."
    여주 "그치만 완자는 내 남자친구니까 당연히 귀요미 완자를 선택해야 하는거 아냐?!?!"
    여주 "하지만 두부는 나의 10년지기 친구야.. 딸기스무디도 얻어 먹어야 하는데.."
    여주 "정말 누굴 선택하지..?"
    여주 "에이 나는 어차피 얼굴 보니까 제일 잘생긴 애로 간다!!!"
    여주 "그래 결심했어 바로 너다!!!"

    "당신은 누굴 고르시겠습니까?\n<본모습은 선택한 다음 선택한 남자의 본모습만 볼 수 있습니다.>"

    menu:
        "내 남자친구 김완자!!!":
            jump Kending
        "전남자친구 이푸준!!!":
            jump Lending
        "소꿉친구 한두부!!!":
            jump Hending


label Kending:

label Lending:

label Hending:




