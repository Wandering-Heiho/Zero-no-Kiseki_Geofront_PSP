from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "Baeckerei",              # 1
        "Kimmy",                  # 2
        "Harold",                 # 3
        "Estelle",                # 4
        "Joshua",                 # 5
        "Tourist Rutina",         # 6
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
        "chr/ch09300.itc",                   # 03
        "chr/ch00600.itc",                   # 04
        "chr/ch00700.itc",                   # 05
        "chr/ch34300.itc",                   # 06
    ))

    DeclNpc(-129,    0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4530,   0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4670,    0,       1279,    135,  405,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4409,    0,       -839,    0,    405,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5500,    0,       -180,    315,  405,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5539,    0,       750,     45,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_1A4",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_2A4",          # 02, 2
        "Function_3_2D8",          # 03, 3
        "Function_4_2DC",          # 04, 4
        "Function_5_1398",         # 05, 5
        "Function_6_1C5A",         # 06, 6
        "Function_7_1D38",         # 07, 7
        "Function_8_1E2B",         # 08, 8
        "Function_9_214A",         # 09, 9
    ))


    def Function_0_1A4(): pass

    label("Function_0_1A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1F0"),
        (2, "loc_1FC"),
        (3, "loc_208"),
        (4, "loc_214"),
        (5, "loc_220"),
        (6, "loc_22C"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_208")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_214")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_220")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_22C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_238")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_25B")

    Return()

    # Function_0_1A4 end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_290")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_290")
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xC, 0xB, 0)

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A3")
    ClearChrFlags(0xD, 0x80)

    label("loc_2A3")

    Return()

    # Function_1_25C end

    def Function_2_2A4(): pass

    label("Function_2_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_2D7")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_2D7")

    Return()

    # Function_2_2A4 end

    def Function_3_2D8(): pass

    label("Function_3_2D8")

    Call(0, 4)
    Return()

    # Function_3_2D8 end

    def Function_4_2DC(): pass

    label("Function_4_2DC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1394")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_359")
    OP_AF(0x56)
    Jump("loc_37B")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_369")
    OP_AF(0x55)
    Jump("loc_37B")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_379")
    OP_AF(0x57)
    Jump("loc_37B")

    label("loc_379")

    OP_AF(0x55)

    label("loc_37B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_138F")

    label("loc_38A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E")
    Jump("loc_138F")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")

    ChrTalk(
        0x8,
        (
            "Monster attacks, disappearances...\x01",
            "Our miners can't catch a break, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is Hoffman's time to stand tall and\x01",
            "lead the rest of his crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's his duty as the mine chief.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_554")

    label("loc_490")


    ChrTalk(
        0x8,
        (
            "If I still had two good legs, I'd be down\x01",
            "there, helping out those boys, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Never mind. Hoffman is the mine chief.\x01",
            "He will point everyone in the right direction,\x01",
            "one way or another.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_554")

    Jump("loc_138F")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_61D")

    ChrTalk(
        0x8,
        (
            "Is Gantz serious? He forced the mayor to go\x01",
            "all the way to the city for his sorry ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard that gambling has made his head\x01",
            "inflate to twice its size. What a mess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_6EC")

    ChrTalk(
        0x8,
        (
            "Gantz burnt practically all his money on\x01",
            "gambling, so he's built up quite the\x01",
            "impressive tab here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn it... If that idiot doesn't come back\x01",
            "safely and pay up, I'm going to lose it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "Kimmy! Sorry, but could you bring me\x01",
            "'you-know-what' from the shelf?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "Okay! Just one second! ♪\x02",
    )

    CloseMessageWindow()

    def lambda_77F():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_77F)

    def lambda_78C():
        OP_93(0xFE, 0x140, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_78C)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        (
            "Can't you see that I'm busy?\x01",
            "What do you need?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_860")

    label("loc_7DC")


    ChrTalk(
        0x8,
        (
            "My daughter grew up into such\x01",
            "a smart and sharp-eyed girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heck, I'm just glad she didn't end\x01",
            "up looking like me. Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_860")

    Jump("loc_138F")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_958")

    ChrTalk(
        0x8,
        (
            "It's been getting easier to tell how much\x01",
            "the mining crew's been slacking off lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Back in my days, we'd forgo sleep to\x01",
            "get a good haul in the mine and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "'Scuse me. Didn't mean to start\x01",
            "preaching to strangers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9C8")

    ChrTalk(
        0x8,
        (
            "I guess I'll knock a few back at\x01",
            "Der Ziegel later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey. I like to relax, too, you know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A9E")

    ChrTalk(
        0x8,
        (
            "Y'see, monsters love their septium.\x01",
            "That's why they drop so much sepith\x01",
            "when you take 'em out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's no wonder monsters gather like bees to honey\x01",
            "around here. This town is all about septium.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")

    ChrTalk(
        0x8,
        (
            "You folks are from the CPD, eh? I appreciate\x01",
            "you patrolling Mainz, considering it's all the\x01",
            "way out in the sticks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know, everyone starts somewhere.\x01",
            "Back before I ran this place, I worked hard\x01",
            "in the mine, earning my mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As long as you keep pushing forward,\x01",
            "you'll be able to make it big.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C28")

    label("loc_BEE")


    ChrTalk(
        0x8,
        (
            "Everyone has to start somewhere.\x01",
            "Just don't give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C28")

    Jump("loc_138F")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C80")

    ChrTalk(
        0x8,
        "Do you need something or not?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If not, scram!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE7")

    label("loc_C80")


    ChrTalk(
        0x8,
        (
            "You came in here for a reason, right?!\x01",
            "I hope you aren't wasting my time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you are, scram!\x02",
    )

    CloseMessageWindow()

    label("loc_CE7")

    Jump("loc_138F")

    label("loc_CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(
        0x8,
        (
            "Despite being a city boy, that Harold\x01",
            "is an upstanding guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Some say being too modest can sometimes\x01",
            "end up biting you in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If he really wants to make it big, he's got\x01",
            "to be a bit more confident in himself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E81")

    label("loc_DEB")


    ChrTalk(
        0x8,
        (
            "Harold's modesty may end up being\x01",
            "his biggest flaw as a trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sometimes I wonder if he's even trying\x01",
            "to make the biggest profit he could.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    Jump("loc_138F")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1048")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")

    ChrTalk(
        0x8,
        (
            "Since the Anniversary Festival is right\x01",
            "around the corner, everyone's started\x01",
            "to act all festive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know the festival is great and all, but slack\x01",
            "off too much and someone could get hurt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1043")

    label("loc_F66")


    ChrTalk(
        0x8,
        (
            "I know the festival is a good time, but\x01",
            "people should stay a bit more focused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they even want to make it to the festival,\x01",
            "they should focus and not make any stupid\x01",
            "mistakes that could get themselves injured.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1043")

    Jump("loc_138F")

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1056")
    Jump("loc_138F")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1153")

    ChrTalk(
        0x8,
        (
            "The miners' morale has been in the gutter,\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know if they're freaking out about\x01",
            "the dogs or wolves or whatever they were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But they're the town's miners, right?\x01",
            "They've got to buck up and work!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11FB")

    label("loc_1153")


    ChrTalk(
        0x8,
        (
            "I don't know if they're freaking out about\x01",
            "the dogs or wolves or whatever they were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But they're the town's miners, right?\x01",
            "They've got to buck up and work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FB")

    Jump("loc_138F")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_138F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1222")
    SetScenarioFlags(0x66, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1306")

    ChrTalk(
        0x8,
        (
            "These recent monster attacks or whatever\x01",
            "really fire up my orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know, someone in town got mauled\x01",
            "by one of those things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If something ever tried to hurt my Kimmy,\x01",
            "there'd be hell to pay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_138F")

    label("loc_1306")


    ChrTalk(
        0x8,
        (
            "You know, someone in town got mauled\x01",
            "by one of those things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If something ever tried to hurt my Kimmy,\x01",
            "there'd be hell to pay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138F")

    Jump("loc_2E9")

    label("loc_1394")

    TalkEnd(0x8)
    Return()

    # Function_4_2DC end

    def Function_5_1398(): pass

    label("Function_5_1398")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1463")

    ChrTalk(
        0xFE,
        (
            "I gotta hand all the miners drinks\x01",
            "in a little bit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Daddy said that if I bring them\x01",
            "tasty drinks, everyone will be\x01",
            "super happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daddy may seem rude,\x01",
            "but he's just shy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1501")

    ChrTalk(
        0xFE,
        (
            "Everyone at the mine is really nice\x01",
            "to me, so I like to say hi to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, everyone thinks Daddy\x01",
            "is an awesome person!\x01",
            "Heehee!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_153F")

    ChrTalk(
        0xFE,
        "What should we have for dinner tonight? ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_153F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0xFE,
        (
            "I love to help Daddy! And I know\x01",
            "Daddy loves it when I help him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1635")

    ChrTalk(
        0xFE,
        (
            "Daddy was a miner before, so he still\x01",
            "worries about everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes, he even gives extra food to\x01",
            "the miners who don't have much mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(
        0xFE,
        (
            "Daddy told me he's gonna go have fun\x01",
            "after closing the store tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The store has been crazy busy during the\x01",
            "festival, so I'm happy for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_16DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_174F")

    ChrTalk(
        0xFE,
        (
            "Did you know that sepith is just\x01",
            "little fragments of septium?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I'm smart. Real smart!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_179B")

    ChrTalk(
        0xFE,
        (
            "I kinda wish I could see Daddy\x01",
            "back when he was a miner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_187E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1838")

    ChrTalk(
        0xFE,
        (
            "Daddy was in a bad mood yesterday,\x01",
            "but he seems all right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe, I bet it's because I helped\x01",
            "him around the shop!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1879")

    label("loc_1838")


    ChrTalk(
        0xFE,
        (
            "With my help, Daddy was able to\x01",
            "turn his frown upside down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1879")

    Jump("loc_1C56")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18F3")

    ChrTalk(
        0xFE,
        (
            "You know, Mr. Hayworth always looks\x01",
            "so sad when he looks at me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did I do something to him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_18F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_19F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1998")

    ChrTalk(
        0xFE,
        (
            "Daddy gets grumpier and grumpier as the\x01",
            "Anniversary Festival comes closer for some\x01",
            "weird reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, did I do something wrong?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19EF")

    label("loc_1998")


    ChrTalk(
        0xFE,
        (
            "I started talking about the Anniversary\x01",
            "Festival, and then Daddy got all angry...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EF")

    Jump("loc_1C56")

    label("loc_19F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1A02")
    Jump("loc_1C56")

    label("loc_1A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADE")

    ChrTalk(
        0xFE,
        (
            "I bet you never would've guessed that\x01",
            "Daddy used to be a miner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People have told me that he was suuuuper\x01",
            "strong and the best miner in all of Mainz!\x01",
            "My Daddy is pretty cool, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B48")

    label("loc_1ADE")


    ChrTalk(
        0xFE,
        (
            "Some of my neighbors told me that Daddy\x01",
            "used to be the best miner in all of Mainz!\x01",
            "Pretty cool, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B48")

    Jump("loc_1C56")

    label("loc_1B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6F")
    SetScenarioFlags(0x66, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(
        0xFE,
        "I love helping Daddy with work! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Daddy may be a little rude to our\x01",
            "neighbors, but he's always nice\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C56")

    label("loc_1BF7")


    ChrTalk(
        0xFE,
        (
            "Daddy always makes sure to be\x01",
            "nice to me. He may seem grumpy,\x01",
            "but don't be afraid of him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C56")

    TalkEnd(0xFE)
    Return()

    # Function_5_1398 end

    def Function_6_1C5A(): pass

    label("Function_6_1C5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D34")
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_1D14")

    ChrTalk(
        0xC,
        (
            "#0908F(Estelle, I know how you feel, but\x01",
            "you can't be acting this suspicious...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0806F(I know that! It's just...hard...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3605F...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D28")

    label("loc_1D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 2)), scpexpr(EXPR_END)), "loc_1D25")
    Call(0, 9)
    Jump("loc_1D28")

    label("loc_1D25")

    Call(0, 8)

    label("loc_1D28")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_1D34")

    TalkEnd(0xFE)
    Return()

    # Function_6_1C5A end

    def Function_7_1D38(): pass

    label("Function_7_1D38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCD")

    ChrTalk(
        0xFE,
        "Huh. Is this a mining helmet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I probably shouldn't be surprised,\x01",
            "given there's a mine right outside the shop...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E27")

    label("loc_1DCD")


    ChrTalk(
        0xFE,
        "Maybe it'd be a nice souvenir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Though, it might be a little too heavy for that.\x02",
    )

    CloseMessageWindow()

    label("loc_1E27")

    TalkEnd(0xFE)
    Return()

    # Function_7_1D38 end

    def Function_8_1E2B(): pass

    label("Function_8_1E2B")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#0905FSo you've run your trading company\x01",
            "for seven years now, Mr. Hayworth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3609FHaha, I wouldn't go so far as to call my\x01",
            "business a trading company just yet.\x02\x03",
            "#3600FMy belief is that I should try to conduct\x01",
            "business while putting a smile on all of\x01",
            "my customers and associates' faces.\x02\x03",
            "#3604FI'm afraid I don't quite meet the expectations\x01",
            "you'd have for a Crossbell trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0904FDon't say that... I think you're doing\x01",
            "good work in Crossbell, Mr. Hayworth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0801F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Are Estelle, Joshua, and Mr. Hayworth\x01",
            "discussing something important? That's\x01",
            "what it looks like to me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0104F(Possibly, so we shouldn't interrupt.)\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 2)
    EventEnd(0x5)
    Return()

    # Function_8_1E2B end

    def Function_9_214A(): pass

    label("Function_9_214A")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()
    TurnDirection(0xA, 0xB, 300)

    ChrTalk(
        0xA,
        (
            "#3605FExcuse me. You said your name\x01",
            "was Estelle, right?\x02\x03",
            "#3600FYou've been sort of quiet. Have\x01",
            "I met you anywhere before?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_226A():
        TurnDirection(0xC, 0xB, 300)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_226A)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xB,
        (
            "#0805FN-No! Of course not! I just think\x01",
            "you resemble someone I've met\x01",
            "before, that's all!\x02\x03",
            "#0806F(He looks exactly like the one\x01",
            "that was with her...)\x02\x03",
            "#0808F(He's...the real one, right?)\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 3)
    EventEnd(0x5)
    Return()

    # Function_9_214A end

    SaveToFile()

Try(main)
