from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3010.bin",                # FileName
        "t3010",                    # MapName
        "t3010",                    # Location
        0x005B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t3010",                  # 0
        "Renne",                  # 1
        "Meister Joerg",          # 2
        "Pater-Mater",            # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_F8",           # 00, 0
        "Function_1_108",          # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_16D6",         # 03, 3
    ))


    def Function_0_F8(): pass

    label("Function_0_F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_107")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_107")

    Return()

    # Function_0_F8 end

    def Function_1_108(): pass

    label("Function_1_108")

    Return()

    # Function_1_108 end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch06600.itc", 0x1F)
    LoadChrToIndex("apl/ch50500.itc", 0x20)
    LoadChrToIndex("chr/ch09502.itc", 0x21)
    LoadEffect(0x0, "event\\ev622_00.eff")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis162.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -5800, 200, 6000, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 3)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 7100, 180)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8930, 750, -140, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe same day, 2:40PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sound(850, 0, 90, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        "#5100001VOh, I see...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        "#5100002VThey've finally made it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7304", 0)
    FadeToBright(1000, 0)
    OP_68(-960, 2500, 1000, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21390, 0)
    OP_68(-5320, 2500, 3850, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-7120, 1700, 5020, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(12000, 2500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5100003V#3302F#11PAll of the pieces have received an invitation now...\x02\x03",
            "#5100004VWith this, is everything prepared for the party?\x02\x03",
            "#5100005V#3304FWho shall uncover the demon's identity first?\x01",
            "Estelle and Joshua? Or the Special Support Section?\x02\x03",
            "#5100006V#3308FOr perhaps it will be--\x02",
        )
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(250)

    NpcTalk(
        0x9,
        "Old Man's Voice",
        (
            "#5100007V#4PAs always, you act as if you've already\x01",
            "seen how things will play out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-6020, 1700, 4270, 4000)
    MoveCamera(46, 15, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(14300, 4000)

    def lambda_59B():
        OP_9B(0x0, 0xFE, 0x0, 0x708, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_59B)

    def lambda_5B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5B0)
    Sleep(500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)

    def lambda_5E7():
        OP_95(0xFE, -4200, 0, 5300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5E7)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5100008V#3309F#5PTeehee. I'm not so brash as to claim that.\x02\x03",
            "#5100009V#3300FAll I see are the threads of fate that\x01",
            "comprise the web I'm entangled in.\x02\x03",
            "#5100010VI can't help but be curious as to what kind\x01",
            "of fabric all these intertwining destinies\x01",
            "will weave in this state of Crossbell...\x02\x03",
            "#5100011V#3304FThat, dear Meister, is all I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 37, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#5100012VHmm... Very well, then.\x02\x03",
            "#5100013VI'm not aware of what the mafia and\x01",
            "that cult are planning, but I imagine\x01",
            "things are going to get noisy.\x02\x03",
            "#5100014VWell, I suppose we reap what we sow.\x01",
            "No, perhaps this is retribution.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x8,
        (
            "#5100015V#3306F#5PIndeed. One could say that this is retribution\x01",
            "for all the sin that has accumulated in that\x01",
            "vast city of gray.\x02\x03",
            "#5100016V#3300FAnd here I was, almost sure that the society\x01",
            "was involved in all of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100017V#3903F#11PCrossbell is a buffer state between Ouroboros and\x01",
            "the Septian Church, after all.\x02\x03",
            "#5100018VThe pope prohibits the knights from taking\x01",
            "action, and the Grandmaster doesn't dispatch\x01",
            "the Enforcers.\x02\x03",
            "#5100019V#3900FThat is merely their official position, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100020V#3309F#5PTeehee. I always thought that your studio was\x01",
            "rather...dubious.\x02\x03",
            "#5100021V#3302FHowever, I never imagined you'd go so far as\x01",
            "to craft your own system that can remotely\x01",
            "interfere with Crossbell's orbal network.\x02\x03",
            "#5100022VThank you for that. I've had a truly wonderful\x01",
            "time playing with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100023V#3903F#11PIf I was of use to you, then I suppose my\x01",
            "efforts were worth it.\x02\x03",
            "#5100024V#3901FWhen that man coerced me to cooperate,\x01",
            "I nearly destroyed it out of spite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100025V#3302F#5PI see that your strained relationship with the\x01",
            "professor hasn't improved in the slightest.\x02\x03",
            "#5100026V#3304FHead of the Thirteen Factories and Ouroboros'\x01",
            "Sixth Anguis: Professor Novartis...\x02\x03",
            "#5100027V#3300FHe has the Astral Code, so what about\x01",
            "the Epstein test models interests him\x01",
            "so much now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100028V#3901F#11PHmph. That scoundrel.\x02\x03",
            "#5100029VHe was probably intending to use it for\x01",
            "some confounded plan of his.\x02\x03",
            "#5100030V#3903FWhat is that fool thinking giving away test\x01",
            "models so haphazardly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100031V#3304F#5PYou're referring to that crimson warrior that\x01",
            "the Special Support Section fought, correct?\x02\x03",
            "#5100032V#3300FFrom what I've seen on the terminal, it must\x01",
            "have been quite the excellent creation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100033V#3903F#11PI had my suspicions, but it certainly had its\x01",
            "issues with situational awareness and apt\x01",
            "decision-making.\x02\x03",
            "#5100034V#3900FSeems it doesn't quite match up to your\x01",
            "partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100035V#3304F#5PHeehee...\x02\x03",
            "#5100036V#3305FThe professor must have also realized\x01",
            "that I'm staying here.\x02\x03",
            "#5100037VBut me aside, did he not have anything\x01",
            "to say about my friend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100038V#3903F#11PHe's been quiet, for now.\x02\x03",
            "#5100039VI imagine he is preoccupied with those new\x01",
            "machines he is working on.\x02\x03",
            "#5100040V#3900FI ended up spending a bit of time finishing your\x01",
            "friend's troublesome attitude control, and\x01",
            "I reinforced the structural integrity of his joints.\x02\x03",
            "#5100041VNow he won't have any room to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100042V#3304F#5PThank you very much, Meister.\x02\x03",
            "#5100043V#3308FNow, at long last...the final gamble can begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5100044V#3900F#11P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Fade(250)
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0x11)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5100045V#3300F#5PHeehee. What's with the dreary face?\x02\x03",
            "#5100046VYou crafted an assortment of dolls for\x01",
            "me, taught me how to puppet them,\x01",
            "and allowed me to take refuge here...\x02\x03",
            "#5100047V#3304FI truly am thankful, Meister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100048V#3903F#11PWhat nonsense is this? I haven't done\x01",
            "anything worthy of praise.\x02\x03",
            "#5100049V#3900FBesides...you're going to be quite busy\x01",
            "today, aren't you?\x02\x03",
            "#5100050VIt might be a little early, but let's put all\x01",
            "this aside for now and have some tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100051V#3309F#5PI would love to.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x12C)
    Sleep(100)
    Fade(1000)
    OP_68(4730, 4900, -140, 7000)
    MoveCamera(69, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13000, 7000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5100052V#3300FLet's go have some tea, Pater-Mater.\x02\x03",
            "#5100053V#3304FWe have a long day ahead of us, after all.\x02\x03",
            "#5100054V#3302FIn fact, it very well may be the longest day\x01",
            "in Crossbell's history.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_87(0x0, 0xFF, 0x1, "pm_head:Layer1(4)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Sound(943, 0, 100, 0)
    Sleep(1500)
    FadeToDark(3000, 0, -1)
    SetCameraDistance(12000, 4000)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_16D6(): pass

    label("Function_3_16D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1725")
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    Jump("Function_3_16D6")

    label("loc_1725")

    Return()

    # Function_3_16D6 end

    SaveToFile()

Try(main)
