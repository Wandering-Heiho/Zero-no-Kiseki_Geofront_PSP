from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t105b.bin",                # FileName
        "t105b",                    # MapName
        "t105b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t105b",                  # 0
        "Manager Haggar",         # 1
        "Lottie",                 # 2
        "Citrus",                 # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch32300.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch20202.itc",                   # 06
        "chr/ch20302.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-93959,  0,       8260,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(94190,   0,       11579,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-99480,  0,       -80559,  90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(97559,   150,     -84309,  90,   341,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(100540,  150,     -84309,  270,  341,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  15, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_208",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_321",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_3CF",          # 05, 5
        "Function_6_3D0",          # 06, 6
        "Function_7_464",          # 07, 7
        "Function_8_468",          # 08, 8
        "Function_9_520",          # 09, 9
        "Function_10_59D",         # 0A, 10
        "Function_11_621",         # 0B, 11
        "Function_12_6D1",         # 0C, 12
        "Function_13_729",         # 0D, 13
        "Function_14_747",         # 0E, 14
        "Function_15_1841",        # 0F, 15
    ))


    def Function_0_208(): pass

    label("Function_0_208")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_248"),
        (1, "loc_254"),
        (2, "loc_260"),
        (3, "loc_26C"),
        (4, "loc_278"),
        (5, "loc_284"),
        (6, "loc_290"),
        (SWITCH_DEFAULT, "loc_29C"),
    )


    label("loc_248")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_254")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_260")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_26C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_278")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_284")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_29C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2BF")

    Return()

    # Function_0_208 end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_320")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_2C0")

    label("loc_320")

    Return()

    # Function_1_2C0 end

    def Function_2_321(): pass

    label("Function_2_321")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_381")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_321")

    label("loc_381")

    Return()

    # Function_2_321 end

    def Function_3_382(): pass

    label("Function_3_382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_94(0xFE, 0xFFFE730C, 0xFFFEC082, 0xFFFE8086, 0xFFFECBC2, 0x3E8)
    Sleep(400)
    Jump("Function_3_382")

    label("loc_3AC")

    Return()

    # Function_3_382 end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_3BC")

    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 3)
    Return()

    # Function_4_3AD end

    def Function_5_3CF(): pass

    label("Function_5_3CF")

    Return()

    # Function_5_3CF end

    def Function_6_3D0(): pass

    label("Function_6_3D0")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_447")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_463")

    Return()

    # Function_6_3D0 end

    def Function_7_464(): pass

    label("Function_7_464")

    Call(0, 8)
    Return()

    # Function_7_464 end

    def Function_8_468(): pass

    label("Function_8_468")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "You were friends of Mr. Hemisphere, yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for a place to eat, I can't\x01",
            "recommend the restaurant Fortuna enough.\x01",
            "You'll find it right down in the mall.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_8_468 end

    def Function_9_520(): pass

    label("Function_9_520")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*sigh* Why did Wazy have to leave already...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never get tired of admiring that\x01",
            "handsome face of his... ㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_520 end

    def Function_10_59D(): pass

    label("Function_10_59D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Did you order room service, by chance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can give me a few minutes,\x01",
            "I'll have your drinks and meal right out.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_59D end

    def Function_11_621(): pass

    label("Function_11_621")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Phew... It was risky, but I somehow\x01",
            "managed to grab a room here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had to wait hours, hoping someone\x01",
            "would cancel their booking.\x01",
            "Worth it in the end, I guess.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_621 end

    def Function_12_6D1(): pass

    label("Function_12_6D1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Three cheers to the Anniversary Festival\x01",
            "and the amazing parties it brings!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_6D1 end

    def Function_13_729(): pass

    label("Function_13_729")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hehe. Hear, hear.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_729 end

    def Function_14_747(): pass

    label("Function_14_747")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_7B6")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 124700, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_877")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_819")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 124700, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_877")

    label("loc_819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_877")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -97500, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -96400, 0, 124700, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)

    label("loc_877")

    OP_68(-97030, 900, 124240, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19350, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(18350, 3000)
    OP_6F(0x10)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_A42")

    ChrTalk(
        0x103,
        "#3500686V#0202F#6PHow beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500687V#5302F#6PIt's certainly a magnificent sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500688V#5006F#6PWow, there's even a fireworks show?\x01",
            "They're pulling out all the stops.\x02\x03",
            "#3500689V#5000FIs it a festival-exclusive show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500690V#0300F#6PNah, man. They do 'em daily.\x02\x03",
            "#3500691VFrom what I've heard, Mishelam's nightlife\x01",
            "is where things REALLY get wild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_BCA")

    ChrTalk(
        0x103,
        "#3500686V#5402F#6PHow beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500687V#0102F#6PIt's certainly a magnificent sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500688V#5006F#6PWow, there's even a fireworks show?\x01",
            "They're pulling out all the stops.\x02\x03",
            "#3500689V#5000FIs it a festival exclusive show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500690V#0300F#6PNah, man. They do 'em daily.\x02\x03",
            "#3500691VFrom what I've heard, Mishelam's nightlife\x01",
            "is where things REALLY get wild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_D4D")

    ChrTalk(
        0x103,
        "#3500686V#0202F#6PHow beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500687V#0102F#6PIt's certainly a magnificent sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500688V#5006F#6PWow, there's even a fireworks show?\x01",
            "They're pulling out all the stops.\x02\x03",
            "#3500689V#5000FIs it a festival exclusive show?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500690V#5600F#6PNah, man. They do 'em daily.\x02\x03",
            "#3500691VFrom what I've heard, Mishelam's nightlife\x01",
            "is where things REALLY get wild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D")


    ChrTalk(
        0x151,
        (
            "#3500692V#5704F#6PBeing surrounded by people in the nighttime parade,\x01",
            "taking moonlit rides on the towering ferris wheel...\x02\x03",
            "#3500693VHaha! It's as if Mishelam's nightlife was built for the\x01",
            "art of seduction.\x02\x03",
            "#3500694V#5700FI'm afraid we'll have to part for now, much to my\x01",
            "dismay.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-97750, 900, 123480, 2000)

    def lambda_ED5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED5)
    Sleep(50)

    def lambda_EE5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE5)
    Sleep(50)

    def lambda_EF5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EF5)
    Sleep(50)

    def lambda_F05():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F05)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#3500695V#5000F#11POh, really? You said you were meeting with\x01",
            "some lady, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#3500696V#5702F#6PHaha, something like that.\x02",
    )

    CloseMessageWindow()
    OP_93(0x151, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0x151,
        (
            "#3500697V#5704F#11PMay the Goddess watch over you, this lovely night.\x02\x03",
            "#3500698V#5702FAnd if your plan actually pans out, try to come find\x01",
            "me at the auction. I'll be waiting!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1424, 255, 90, 0)
    Sleep(500)
    OP_68(-99750, 900, 120550, 3500)
    OP_95(0x151, -100000, 0, 116800, 2000, 0x1)

    def lambda_109A():
        OP_95(0xFE, -100000, 0, 114300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_109A)
    Sleep(300)

    def lambda_10B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_10B7)
    Sound(121, 0, 100, 0)
    WaitChrThread(0x151, 1)
    WaitChrThread(0x151, 2)
    Sound(890, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-97040, 900, 124460, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1285")

    ChrTalk(
        0x104,
        "#3500699V#0306F#11PMan, that guy acts like he's on top of the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500700V#0206F#12PThe leader of a small-time gang working\x01",
            "as a host at a high-class party?\x02\x03",
            "#3500701V#0211FI do not buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500702V#5304F#11PWhatever the truth may be, the info he gave\x01",
            "us about the auction was extremely helpful.\x02\x03",
            "#3500703V#5300FI think we owe him one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156A")

    label("loc_1285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_13FA")

    ChrTalk(
        0x104,
        "#3500699V#0306F#11PMan, that guy acts like he's on top of the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500700V#5406F#11PThe leader of a small-time gang working as\x01",
            "a host at a high-class party...?\x02\x03",
            "#3500701V#5411FI do not buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500702V#0104F#12PWhatever the truth may be, the info he gave\x01",
            "us about the auction was extremely helpful.\x02\x03",
            "#3500703V#0100FI think we owe him one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_156A")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_156A")

    ChrTalk(
        0x104,
        "#3500699V#5606F#11PMan, that guy acts like he's on top of the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500700V#0206F#12PThe leader of a small-time gang working as\x01",
            "a host at a high-class party...?\x02\x03",
            "#3500701V#0211FI do not buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500702V#0104F#11PWhatever the truth may be, the info he gave\x01",
            "us about the auction was extremely helpful.\x02\x03",
            "#3500703V#0100FI think we owe him one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_156A")


    ChrTalk(
        0x101,
        "#3500704V#5000F#11PYeah, I think we do.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3500705V#5003F#5PIt's almost time for us to make our way\x01",
            "towards the auction venue.\x02\x03",
            "#3500706V#5001FFor now, our objective is to slip past the\x01",
            "security checkpoint and enter Speaker\x01",
            "Hartmann's mansion.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1685():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1685)
    Sleep(50)

    def lambda_1695():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1695)
    Sleep(50)

    def lambda_16A5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16A5)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_16E4")

    ChrTalk(
        0x102,
        "#3500707V#5301F#12PWe can do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1745")

    label("loc_16E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1711")

    ChrTalk(
        0x103,
        "#3500708V#5401F#12PRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1745")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1745")

    ChrTalk(
        0x104,
        "#3500709V#5601F#12PLet's get it done!\x02",
    )

    CloseMessageWindow()

    label("loc_1745")

    SetCameraDistance(17600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_179A")
    AddParty(0x1, 0xEF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_17C9")

    label("loc_179A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_17B4")
    AddParty(0x2, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_17C9")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_17C9")
    AddParty(0x3, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_17C9")

    SetChrPos(0x0, -99730, 0, 120850, 180)
    SetScenarioFlags(0xA4, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17FB")
    OP_29(0x24, 0x4, 0x40)
    Jump("loc_180D")

    label("loc_17FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180D")
    OP_29(0x24, 0x4, 0x40)

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_181E")
    OP_DE(0x2A, 0x0)
    Jump("loc_183B")

    label("loc_181E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_182F")
    OP_DE(0x2B, 0x0)
    Jump("loc_183B")

    label("loc_182F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_183B")
    OP_DE(0x2C, 0x0)

    label("loc_183B")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_747 end

    def Function_15_1841(): pass

    label("Function_15_1841")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "                   ~Staircase~\x01",
            "The third floor is currently reserved for\x01",
            "VIPs. Please refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_1841 end

    SaveToFile()

Try(main)
