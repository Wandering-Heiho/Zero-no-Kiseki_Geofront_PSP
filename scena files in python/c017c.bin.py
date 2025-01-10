from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c017c.bin",                # FileName
        "c017c",                    # MapName
        "c017c",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c017c",                  # 0
        "Receptionist Pearl",     # 1
        "Receptionist Cynthia",   # 2
        "Hanson",                 # 3
        "Gladys",                 # 4
        "Prada",                  # 5
        "Baker",                  # 6
        "Southwark",              # 7
        "Detective Dudley",       # 8
        "Manager Neston",         # 9
        "Janetta",                # 10
        "Baggio",                 # 11
        "Dorothea",               # 12
        "Kean",                   # 13
        "Old Man Honest",         # 14
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch20400.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch00900.itc",                   # 0A
        "chr/ch34600.itc",                   # 0B
        "chr/ch25900.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5250,   8000,    5360,    360,  385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_3E0",          # 00, 0
        "Function_1_498",          # 01, 1
        "Function_2_571",          # 02, 2
        "Function_3_60F",          # 03, 3
        "Function_4_63F",          # 04, 4
        "Function_5_643",          # 05, 5
        "Function_6_10C7",         # 06, 6
        "Function_7_10CB",         # 07, 7
        "Function_8_1CC7",         # 08, 8
        "Function_9_1CCB",         # 09, 9
        "Function_10_23E8",        # 0A, 10
        "Function_11_23EC",        # 0B, 11
        "Function_12_292B",        # 0C, 12
        "Function_13_292F",        # 0D, 13
        "Function_14_2F56",        # 0E, 14
        "Function_15_2F5A",        # 0F, 15
        "Function_16_3955",        # 10, 16
        "Function_17_3959",        # 11, 17
        "Function_18_40EB",        # 12, 18
        "Function_19_4591",        # 13, 19
        "Function_20_50E8",        # 14, 20
        "Function_21_562A",        # 15, 21
        "Function_22_5BB5",        # 16, 22
        "Function_23_5F90",        # 17, 23
        "Function_24_6691",        # 18, 24
        "Function_25_6ABE",        # 19, 25
        "Function_26_6B97",        # 1A, 26
        "Function_27_6C90",        # 1B, 27
    ))


    def Function_0_3E0(): pass

    label("Function_0_3E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_420"),
        (1, "loc_42C"),
        (2, "loc_438"),
        (3, "loc_444"),
        (4, "loc_450"),
        (5, "loc_45C"),
        (6, "loc_468"),
        (SWITCH_DEFAULT, "loc_474"),
    )


    label("loc_420")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_42C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_438")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_444")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_450")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_45C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_497")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_497")

    Return()

    # Function_0_3E0 end

    def Function_1_498(): pass

    label("Function_1_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_570")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_498")

    label("loc_570")

    Return()

    # Function_1_498 end

    def Function_2_571(): pass

    label("Function_2_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_590")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5F8")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5F8")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5CB")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EA")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ClearChrFlags(0xF, 0x80)

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_60E")

    Return()

    # Function_2_571 end

    def Function_3_60F(): pass

    label("Function_3_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_63E")

    label("loc_630")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_63E")

    Return()

    # Function_3_60F end

    def Function_4_63F(): pass

    label("Function_4_63F")

    Call(0, 5)
    Return()

    # Function_4_63F end

    def Function_5_643(): pass

    label("Function_5_643")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6A7")

    ChrTalk(
        0x8,
        (
            "Apparently, Scott has to go on a\x01",
            "business trip next week, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D0")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "If you were wondering why I sighed, it's because\x01",
            "I was trying to do it like my senior, Cynthia, does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I feel like adult women like her possess\x01",
            "a different, more mature sexiness...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        (
            "Wh-What are you saying to\x01",
            "the customers, Pearl?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_87C")

    label("loc_7D0")


    ChrTalk(
        0x8,
        (
            "Hmm, adult women like her just radiate\x01",
            "this different, mature kind of sexiness.\x01",
            "That sigh is just one example of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How could a man leave a girl like her alone?\x02",
    )

    CloseMessageWindow()

    label("loc_87C")

    Jump("loc_10C3")

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B95")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x101,
        (
            "#0001F(Oh, these people might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "A missing kid?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "Oh, dear, this boy has gotten lost?\x01",
            "That's terrible to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry, but I don't think\x01",
            "I have any leads for you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EE():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9EE)

    def lambda_9FB():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9FB)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x9,
        "Pearl, have you seen this boy before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, I don't recall\x01",
            "seeing him, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were quite a few kids when\x01",
            "the parade passed by, though...\x01",
            "But they were all with their parents.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACF():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_ACF)

    def lambda_ADC():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_ADC)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x9,
        (
            "I'm terribly sorry, but odds are\x01",
            "the child didn't come into\x01",
            "the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI see...\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    Jump("loc_C20")

    label("loc_B95")


    ChrTalk(
        0x8,
        (
            "All the children who visited the department\x01",
            "store today came with their parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't think I saw the kid\x01",
            "you're looking for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C20")

    Jump("loc_10C3")

    label("loc_C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D24")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "I was trying to imitate the sigh\x01",
            "my senior, Cynthia, makes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, I feel like adult women like her possess\x01",
            "a different, more mature sexiness...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        (
            "Wh-What are you saying to\x01",
            "the customers, Pearl?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD0")

    label("loc_D24")


    ChrTalk(
        0x8,
        (
            "Hmm, adult women like her just radiate\x01",
            "this different, mature kind of sexiness.\x01",
            "That sigh is just one example of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Why would a man leave a girl like her alone?\x02",
    )

    CloseMessageWindow()

    label("loc_DD0")

    Jump("loc_10C3")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_EB6")

    ChrTalk(
        0x8,
        (
            "Typically, the manager's projects lead\x01",
            "to us employees working a lot harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's okay, though. We have nothing\x01",
            "but faith in him, because these new sales\x01",
            "projects tend to do very well for the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_F5A")

    ChrTalk(
        0x8,
        (
            "Boy, yesterday was tough.\x01",
            "We had to deal with a few lost kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this crowd of people, it's no wonder\x01",
            "so many of these incidents happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1018")

    ChrTalk(
        0x8,
        (
            "Since Cynthia is the type of woman\x01",
            "girls tend to look up to, most of her\x01",
            "friends are usually women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish I could ask her about any\x01",
            "relationships with guys, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C3")

    label("loc_1018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_10C3")

    ChrTalk(
        0x8,
        (
            "I actually saw Mishy when\x01",
            "I went to Mishelam on\x01",
            "a date with Scott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mishy is absolutely adorable!\x01",
            "Hehe, I recommend you go and\x01",
            "see him whenever you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C3")

    TalkEnd(0x8)
    Return()

    # Function_5_643 end

    def Function_6_10C7(): pass

    label("Function_6_10C7")

    Call(0, 7)
    Return()

    # Function_6_10C7 end

    def Function_7_10CB(): pass

    label("Function_7_10CB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_115F")

    ChrTalk(
        0x9,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We are open till 11PM tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please, keep on shopping to\x01",
            "your heart's content.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC3")

    label("loc_115F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124A")

    ChrTalk(
        0x9,
        "Phew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, please excuse my rudeness.\x01",
            "To have sighed in front of potential customers...\x01",
            "My fatigue must've gotten the best of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Times like these make me want to\x01",
            "go for a light jog to relax.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_130B")

    label("loc_124A")


    ChrTalk(
        0x9,
        (
            "I want to spend the vacation I'm taking for\x01",
            "the Anniversary Festival jogging around\x01",
            "all the big attractions in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's how I usually spend my days off.\x01",
            "Y-Yes, I am single...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130B")

    Jump("loc_1CC3")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AA")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x101,
        (
            "#0001F(Oh, these people might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Oh, a missing child?\x01",
            "That's terrible to hear.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1402():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1402)

    def lambda_140F():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_140F)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x9,
        "Pearl, have you seen this child before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, I don't recall ever\x01",
            "seeing him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were quite a few kids when\x01",
            "the parade passed by, though...\x01",
            "But they were all with their parents.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14E4():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14E4)

    def lambda_14F1():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14F1)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x9,
        (
            "I'm terribly sorry, but odds are\x01",
            "the child didn't come into\x01",
            "the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI see...\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    Jump("loc_162D")

    label("loc_15AA")


    ChrTalk(
        0x9,
        "I don't remember seeing him, either...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm terribly sorry, but odds are\x01",
            "the child didn't come into\x01",
            "the department store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162D")

    Jump("loc_1CC3")

    label("loc_1632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171D")

    ChrTalk(
        0x9,
        "Phew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, please excuse my rudeness.\x01",
            "To have sighed in front of potential customers...\x01",
            "my fatigue must've gotten the best of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Times like these make me want to\x01",
            "go for a light jog to relax.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17DE")

    label("loc_171D")


    ChrTalk(
        0x9,
        (
            "I want to spend the vacation I'm taking for\x01",
            "the Anniversary Festival jogging around\x01",
            "all the big attractions in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's how I usually spend my days off.\x01",
            "Y-Yes, I am single...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DE")

    Jump("loc_1CC3")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18D1")

    ChrTalk(
        0x9,
        (
            "The manager is preparing an all-new project, designed\x01",
            "to entice customers on the last day of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "His projects are always loved by the customers.\x01",
            "I'm confident this one is safe to look forward to as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC3")

    label("loc_18D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_199B")

    ChrTalk(
        0x9,
        (
            "If you're running low on supplies during\x01",
            "your travels, please, come by our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At the Times Department Store,\x01",
            "we have all the articles and goods\x01",
            "our customers could wish for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC3")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B06")

    ChrTalk(
        0x9,
        (
            "I was talking to Estelle, this bracer who\x01",
            "came to Crossbell recently, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...apparently, she's also a huge fan of\x01",
            "the Strega Corporation's sneakers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Jogging is a big hobby of mine, and I have\x01",
            "a massive weakness for sneakers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can't believe one of my interests led to\x01",
            "me hitting it off so well with a customer!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BFD")

    label("loc_1B06")


    ChrTalk(
        0x9,
        (
            "So, that bracer, Estelle, is also a huge fan\x01",
            "of the Strega Corporation, and we both hit\x01",
            "it off really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I should be careful not to mix up business\x01",
            "with personal affairs, but... Haha. Finding\x01",
            "a person who shares your hobby is so fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFD")

    Jump("loc_1CC3")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CC3")

    ChrTalk(
        0x9,
        (
            "Yesterday's event attracted so many\x01",
            "customers that some even brought\x01",
            "their whole family along!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The children were overjoyed,\x01",
            "seeing Mishy dancing around\x01",
            "the department store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC3")

    TalkEnd(0x9)
    Return()

    # Function_7_10CB end

    def Function_8_1CC7(): pass

    label("Function_8_1CC7")

    Call(0, 9)
    Return()

    # Function_8_1CC7 end

    def Function_9_1CCB(): pass

    label("Function_9_1CCB")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D29")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D48")
    OP_AF(0x22)
    Jump("loc_1D4A")

    label("loc_1D48")

    OP_AF(0x21)

    label("loc_1D4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23DF")

    label("loc_1D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6D")
    Jump("loc_23DF")

    label("loc_1D6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E4B")

    ChrTalk(
        0xA,
        (
            "That sales contest Prada\x01",
            "proposed to me had completely\x01",
            "slipped my mind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, be it victory or defeat, it doesn't matter as\x01",
            "long as you put your heart into your business!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1EF1")

    ChrTalk(
        0xA,
        "High heels emphasize a woman's femininity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sure, you don't want to wear them\x01",
            "out on a Sunday stroll, but they're\x01",
            "a must at social gatherings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_1EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2026")

    ChrTalk(
        0xA,
        (
            "The shoes made by Strega are insanely\x01",
            "popular among all the sneaker buffs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Despite being flexible and stylish,\x01",
            "they're still strong and durable...\x01",
            "It's no surprise they're so popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, it looks like that foreign bracer,\x01",
            "Estelle, is a big fan of the Strega Corporation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_2026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_212C")

    ChrTalk(
        0xA,
        (
            "I've noticed that Crossbellans prefer to buy\x01",
            "sandals and shoes that are easy to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wholeheartedly recommend the shoes we offer here,\x01",
            "due to their efficiency and the fact that they're well\x01",
            "suited for any terrain you throw at them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21E5")

    ChrTalk(
        0xA,
        (
            "Around break time, Cynthia\x01",
            "likes to come over and check\x01",
            "out all the new running shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Jogging really is a must for any\x01",
            "young woman wanting to stay in top form.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232F")

    ChrTalk(
        0xA,
        (
            "Prada proposed the idea of a\x01",
            "sales contest to me, taking place\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She wants to see which one of us can improve\x01",
            "our sales the most compared to a normal week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We used to have little wagers like that\x01",
            "back when we were business rivals.\x01",
            "They always motivated us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23DF")

    label("loc_232F")


    ChrTalk(
        0xA,
        (
            "Prada proposed that we have a sales\x01",
            "competition during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think I'll take her up on that. It reminds\x01",
            "me of the old days when we were rivals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DF")

    Jump("loc_1CD8")

    label("loc_23E4")

    TalkEnd(0xA)
    Return()

    # Function_9_1CCB end

    def Function_10_23E8(): pass

    label("Function_10_23E8")

    Call(0, 11)
    Return()

    # Function_10_23E8 end

    def Function_11_23EC(): pass

    label("Function_11_23EC")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2927")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_244A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_246A")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2922")

    label("loc_246A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247E")
    Jump("loc_2922")

    label("loc_247E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2922")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(
        0xB,
        (
            "All right, time to give it\x01",
            "my all today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't start losing to\x01",
            "my daughter just yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2922")

    label("loc_2506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_255C")

    ChrTalk(
        0xB,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My, oh, my, the customers just\x01",
            "keep on coming today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2922")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C4")

    ChrTalk(
        0xB,
        "Janetta seems to be absentminded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I wonder what's gotten into her?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_260B")

    label("loc_25C4")


    ChrTalk(
        0xB,
        (
            "Janetta sure is a strange girl.\x01",
            "It's hard not to worry about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260B")

    Jump("loc_2922")

    label("loc_2610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C0")

    ChrTalk(
        0xB,
        (
            "A customer came by earlier and bought\x01",
            "half a dozen wine bottles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Phew, that's thanks to the festival.\x01",
            "Usually makes people drink too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2773")

    label("loc_26C0")


    ChrTalk(
        0xB,
        (
            "I can't keep up with how many\x01",
            "people come to buy alcohol from\x01",
            "me during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* I'm worried that some people are\x01",
            "going to drink themselves under the table.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2773")

    Jump("loc_2922")

    label("loc_2778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_27FC")

    ChrTalk(
        0xB,
        (
            "Our selection of fruits is popular\x01",
            "for family-friendly parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By all means, please,\x01",
            "come and have a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2922")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2922")

    ChrTalk(
        0xB,
        (
            "Welcome to Legion's Foods, here in the\x01",
            "corner of Times Department Store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Erebonian smoked pork here\x01",
            "is ideal for any ham sandwich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you use Armorica-produced lettuce,\x01",
            "you can prepare a delicious sandwich.\x01",
            "How about having one as a light\x01",
            "Anniversary Festival meal?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2922")

    Jump("loc_23F9")

    label("loc_2927")

    TalkEnd(0xB)
    Return()

    # Function_11_23EC end

    def Function_12_292B(): pass

    label("Function_12_292B")

    Call(0, 13)
    Return()

    # Function_12_292B end

    def Function_13_292F(): pass

    label("Function_13_292F")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_293C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F52")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_298D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29AC")
    OP_AF(0x1F)
    Jump("loc_29AE")

    label("loc_29AC")

    OP_AF(0x1E)

    label("loc_29AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F4D")

    label("loc_29BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D1")
    Jump("loc_2F4D")

    label("loc_29D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F4D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6D")

    ChrTalk(
        0xC,
        (
            "Oh, Hanson. He completely forgot\x01",
            "about our sales contest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Geez, he's always in his own world.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AFB")

    label("loc_2A6D")


    ChrTalk(
        0xC,
        (
            "Oh, well... The contest was still fun,\x01",
            "even if there weren't any stakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I should go thank Hanson\x01",
            "for accepting in the first place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFB")

    Jump("loc_2F4D")

    label("loc_2B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2BAC")

    ChrTalk(
        0xC,
        (
            "The people of Crossbell are very\x01",
            "fashion-forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to follow what's hot in the fashion world\x01",
            "so that customers never tire of the same trends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CC0")

    ChrTalk(
        0xC,
        (
            "Personally, I just can't come to see the appeal\x01",
            "of Erebonian nobles' garments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sure, they're all made of the highest\x01",
            "quality material, but they all look so\x01",
            "similar and drab to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As you can see, I'm someone who\x01",
            "wishes for originality in fashion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2D89")

    ChrTalk(
        0xC,
        (
            "Fashion isn't just dressing up in whatever\x01",
            "expensive dress you find!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's important to embrace harmony...\x01",
            "You know, balance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You seem to understand\x01",
            "what I'm talking about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E21")

    ChrTalk(
        0xC,
        (
            "Foreigners have extremely\x01",
            "varied, peculiar styles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Running a boutique, there's still a lot\x01",
            "of things I can learn from tourists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4D")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F4D")

    ChrTalk(
        0xC,
        (
            "I look forward to finding out the result of\x01",
            "my sales contest with Hanson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If I remember correctly, when Hanson\x01",
            "ran a boutique shop, I was never able\x01",
            "to defeat him in sales...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll need to repay him for the disgrace I suffered when\x01",
            "he dropped out while he was ahead last time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4D")

    Jump("loc_293C")

    label("loc_2F52")

    TalkEnd(0xC)
    Return()

    # Function_13_292F end

    def Function_14_2F56(): pass

    label("Function_14_2F56")

    Call(0, 15)
    Return()

    # Function_14_2F56 end

    def Function_15_2F5A(): pass

    label("Function_15_2F5A")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3951")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2FD7")
    OP_AF(0x25)
    Jump("loc_2FD9")

    label("loc_2FD7")

    OP_AF(0x24)

    label("loc_2FD9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_394C")

    label("loc_2FE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFC")
    Jump("loc_394C")

    label("loc_2FFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_394C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_31F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(
        0xD,
        (
            "The final day of the festival is such a big deal\x01",
            "that there'll probably be a lot of men who try\x01",
            "to pop the big question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A guy buys a ring with three months' worth\x01",
            "of pay, waiting for that perfect moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how many years go by,\x01",
            "I doubt this custom will ever change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_31F0")

    label("loc_3154")


    ChrTalk(
        0xD,
        (
            "A guy buys a ring with three months' worth\x01",
            "of pay, waiting for that perfect moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's an old, outdated tradition,\x01",
            "but it works like a charm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F0")

    Jump("loc_394C")

    label("loc_31F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336F")

    ChrTalk(
        0xD,
        (
            "When Phantom Thief B last appeared\x01",
            "in the Empire, they say that the public\x01",
            "actually supported his ventures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I even heard that some of his more...rabid\x01",
            "fans had to be dealt with after sending\x01",
            "letters of support to various news agencies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For jewelers who became targets of his thievery,\x01",
            "the phantom thief was the bane of their existence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3432")

    label("loc_336F")


    ChrTalk(
        0xD,
        (
            "When Phantom Thief B last appeared\x01",
            "in the Empire, they say that the public\x01",
            "actually supported his ventures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't say I can understand how people\x01",
            "could look to a thief as their hero.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3432")

    Jump("loc_394C")

    label("loc_3437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3687")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A9")

    ChrTalk(
        0xD,
        (
            "Do you know about the mysterious\x01",
            "crook called 'Phantom Thief B'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He's an unusual thief who targets works of art\x01",
            "with a vast amount of history, and was also\x01",
            "insanely popular in the Empire at one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Back when I was an art dealer, even a friend\x01",
            "of mine was pilfered by the elusive thief.\x01",
            "I swear, he's too good at what he does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3682")

    label("loc_35A9")


    ChrTalk(
        0xD,
        (
            "The mysterious criminal named 'Phantom Thief B'...\x01",
            "According to rumors, there have been first-hand accounts\x01",
            "of damages he caused in Liberl two years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Maybe it's possible he'll make his way to Crossbell.\x02",
    )

    CloseMessageWindow()

    label("loc_3682")

    Jump("loc_394C")

    label("loc_3687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3782")

    ChrTalk(
        0xD,
        (
            "Recently, the Crossbell Times has become\x01",
            "a lot more gossip-like, if that's the right way\x01",
            "to describe it. Kind of like a tabloid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess the fact that I still read them proves\x01",
            "that it has some kind of charm to it, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394C")

    label("loc_3782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3836")

    ChrTalk(
        0xD,
        (
            "I've heard there was a rowdy fight in the\x01",
            "Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For goodness sake, I wish they'd realize the\x01",
            "trouble they're making for the locals down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394C")

    label("loc_3836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_394C")

    ChrTalk(
        0xD,
        (
            "During this time of the year, I find\x01",
            "that my sales start to boom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even though this shop deals in expensive accessories,\x01",
            "people's purse strings keep loosening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "While it's good for us merchants,\x01",
            "I just can't bring myself to admire such\x01",
            "frivolous behavior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394C")

    Jump("loc_2F67")

    label("loc_3951")

    TalkEnd(0xD)
    Return()

    # Function_15_2F5A end

    def Function_16_3955(): pass

    label("Function_16_3955")

    Call(0, 17)
    Return()

    # Function_16_3955 end

    def Function_17_3959(): pass

    label("Function_17_3959")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3966")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_39B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_39D6")
    OP_AF(0x1B)
    Jump("loc_3A38")

    label("loc_39D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39E6")
    OP_AF(0x1A)
    Jump("loc_3A38")

    label("loc_39E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_39F6")
    OP_AF(0x19)
    Jump("loc_3A38")

    label("loc_39F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A06")
    OP_AF(0x18)
    Jump("loc_3A38")

    label("loc_3A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3A16")
    OP_AF(0x17)
    Jump("loc_3A38")

    label("loc_3A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3A26")
    OP_AF(0x16)
    Jump("loc_3A38")

    label("loc_3A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3A36")
    OP_AF(0x15)
    Jump("loc_3A38")

    label("loc_3A36")

    OP_AF(0x14)

    label("loc_3A38")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40E2")

    label("loc_3A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5B")
    Jump("loc_40E2")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B03")

    ChrTalk(
        0xE,
        (
            "Hey there, we got some new issues\x01",
            "that came in this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stock is limited, so buy them while\x01",
            "you can!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3B8D")

    label("loc_3B03")


    ChrTalk(
        0xE,
        "This issue has been selling like wildfire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I reckon it will be sold out by noon, so if\x01",
            "you wanted to buy it, I'd do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B8D")

    Jump("loc_40E2")

    label("loc_3B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3C41")

    ChrTalk(
        0xE,
        (
            "During the Anniversary Festival, I've noticed many\x01",
            "people like to stand here reading books for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Woe is me. I wonder if they'll actually buy them?\x02",
    )

    CloseMessageWindow()
    Jump("loc_40E2")

    label("loc_3C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D23")

    ChrTalk(
        0xE,
        (
            "Wow, it looks like the Crossbell Times\x01",
            "intends to publish a new issue on the\x01",
            "Anniversary Festival's final day, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yep, have to give it to those journalists.\x01",
            "Their passion is commendable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3DE1")

    label("loc_3D23")


    ChrTalk(
        0xE,
        (
            "Wow, it looks like the Crossbell Times intends to publish\x01",
            "a new issue on the Anniversary Festival's final day, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you like a good pleasure read,\x01",
            "I'd check out the next issue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE1")

    Jump("loc_40E2")

    label("loc_3DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3EAC")

    ChrTalk(
        0xE,
        (
            "Welcome.\x01",
            "Are you looking for something in particular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My motto is that you should always have some\x01",
            "medicine on hand. After all, you never know\x01",
            "what life will throw your way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E2")

    label("loc_3EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_402F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F70")

    ChrTalk(
        0xE,
        (
            "Maps of Crossbell and bus timetables have been\x01",
            "in high demand as of yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Apparently, there're even tourists who go\x01",
            "to regions outside of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_402A")

    label("loc_3F70")


    ChrTalk(
        0xE,
        (
            "Well, during the Anniversary Festival, foreigners\x01",
            "try to have as much fun as possible, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Apparently, there're even tourists who go\x01",
            "to regions outside of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402A")

    Jump("loc_40E2")

    label("loc_402F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_40E2")

    ChrTalk(
        0xE,
        (
            "Finally, another shipment of the Arc en Ciel\x01",
            "pamphlets arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Lately, these things have been selling one after\x01",
            "the other, thanks to Arc en Ciel's popularity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E2")

    Jump("loc_3966")

    label("loc_40E7")

    TalkEnd(0xE)
    Return()

    # Function_17_3959 end

    def Function_18_40EB(): pass

    label("Function_18_40EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4465")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "#0600FYou guys again...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FD-Detective Dudley?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOh... What a rare sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FGoin' shoppin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0601FYou can obviously see that's not the case!\x01",
            "I'm patrolling important areas in Crossbell City.\x02\x03",
            "#0603FI periodically assess people in heavily\x01",
            "populated locations, like Central Square,\x01",
            "Harbor District, the main road, and so on.\x02\x03",
            "It's my duty to make sure no criminals,\x01",
            "terrorists, or the like are able to slip into\x01",
            "the Anniversary Festival unnoticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FTh-That so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt is a bit surprising to see you operating\x01",
            "out in such plain areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0603F*sigh* It's no use giving any rebuttal.\x02\x03",
            "#0600FReturn to your duties immediately.\x01",
            "I assume you've been given a variety\x01",
            "of odd jobs and requests, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 6)
    Jump("loc_458D")

    label("loc_4465")


    ChrTalk(
        0xFE,
        (
            "#0606FThere are a ridiculous amount of\x01",
            "people attending this year.\x02\x03",
            "#0608FSpotting a terrorist or jaeger in this\x01",
            "mess would be a miracle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(I honestly think Dudley\x01",
            "worries a bit too much.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(Well, he does have to deal with all these\x01",
            "foreign VIPs entering Crossbell...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458D")

    TalkEnd(0xFE)
    Return()

    # Function_18_40EB end

    def Function_19_4591(): pass

    label("Function_19_4591")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_48B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47ED")

    ChrTalk(
        0xFE,
        (
            "We're having an Anniversary Festival closing\x01",
            "sale, so we intend to stay open two more\x01",
            "hours than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later tonight, all the stores here\x01",
            "plan to hold a massive sale for\x01",
            "their popular goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FIt's definitely tempting, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe have something really important to take\x01",
            "care of at Mishelam today.\x02\x03",
            "#0003FI'm sorry that I'm depriving you\x01",
            "of this opportunity, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FDid you really just get that serious\x01",
            "'cause we're missin' some sale?\x02\x03",
            "Haha. Oh, well... Gotta say, we're\x01",
            "pros at having cruddy timing, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FI am not laughing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_48AB")

    label("loc_47ED")


    ChrTalk(
        0xFE,
        (
            "Later tonight, all the stores here\x01",
            "plan to hold a massive sale for\x01",
            "their popular goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, look forward to an extraordinary sale\x01",
            "in the dead of an Anniversary Festival night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AB")

    Jump("loc_50E4")

    label("loc_48B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_49A5")

    ChrTalk(
        0xFE,
        (
            "Occasionally, tourists come look around stores'\x01",
            "interiors like they're professional traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I warmly welcome these inspections if the\x01",
            "result is that we're able to create the best\x01",
            "department store possible for customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E4")

    label("loc_49A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4B25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A71")

    ChrTalk(
        0xFE,
        (
            "Oh, you're searching for\x01",
            "someone, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want, please ask the\x01",
            "reception desk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The department store's receptionist\x01",
            "might know something about him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4B20")

    label("loc_4A71")


    ChrTalk(
        0xFE,
        (
            "Hmm, if those two didn't even see\x01",
            "him, that probably means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...the child probably hasn't come\x01",
            "by the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sorry for not being any more help.\x02",
    )

    CloseMessageWindow()

    label("loc_4B20")

    Jump("loc_50E4")

    label("loc_4B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4C1A")

    ChrTalk(
        0xFE,
        (
            "Occasionally, tourists come look around stores'\x01",
            "interiors like they're professional traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I warmly welcome these inspections if the\x01",
            "result is that we're able to create the best\x01",
            "department store possible for customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E4")

    label("loc_4C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4CEF")

    ChrTalk(
        0xFE,
        (
            "Remember, a manager should judge the quality of\x01",
            "his goods and shops with his own two eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, inform us immediately if, by any chance,\x01",
            "you find any defective products or inadequacies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E4")

    label("loc_4CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4D96")

    ChrTalk(
        0xFE,
        (
            "Due to a strong influx of tourists, these recent\x01",
            "years have been fantastic for our business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Dear customers, please, have a look at our wares.\x02",
    )

    CloseMessageWindow()
    Jump("loc_50E4")

    label("loc_4D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E5F")

    ChrTalk(
        0xFE,
        (
            "At this department store, we offer a countless\x01",
            "number of genuine, Crossbell-made goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're also perfect as souvenirs for tourists!\x01",
            "If you'd like, please, come take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E4")

    label("loc_4E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_50E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502D")

    ChrTalk(
        0xFE,
        (
            "Yesterday, we hosted an event that featured\x01",
            "Mishelam's mascot, Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a big hit with the tourists, and the store's\x01",
            "sales grew approximately 12 percent when\x01",
            "compared to the previous fiscal year.\x01",
            "I'm happy to say the plan paid off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FTh-They hosted an event\x01",
            "like that...here?\x02\x03",
            "#0201F(Why did I have to be distracted\x01",
            "playing that game with Jona?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FT-Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FIt is nothing. Forget I said that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_50E4")

    label("loc_502D")


    ChrTalk(
        0xFE,
        (
            "Yesterday's collaboration with Mishy\x01",
            "ended up being a resounding success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just like I thought, mascots are powerful things...\x01",
            "Mishy managed to produce the intended results!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E4")

    TalkEnd(0xFE)
    Return()

    # Function_19_4591 end

    def Function_20_50E8(): pass

    label("Function_20_50E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519F")

    ChrTalk(
        0xFE,
        (
            "Pearl is so lucky, being the\x01",
            "fiancee of a bracer and all.\x01",
            "Oh, I'm so envious of her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want a fiance who will appreciate\x01",
            "my feminine charms.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_521C")

    label("loc_519F")


    ChrTalk(
        0xFE,
        (
            "I tried to see if any of the festival\x01",
            "customers would, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I didn't catch anyone's\x01",
            "eye, apparently...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_521C")

    Jump("loc_5626")

    label("loc_5221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_528C")

    ChrTalk(
        0xFE,
        "Mishy was so cute, wasn't he?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, how I wish I was as soft\x01",
            "to the touch as Mishy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5626")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_52E7")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Parade, paraaade... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll try to escape\x01",
            "work today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5626")

    label("loc_52E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5338")

    ChrTalk(
        0xFE,
        "Gah, I'm so hungryyy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't my shift hurry\x01",
            "up and end?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5626")

    label("loc_5338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_541F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CC")

    ChrTalk(
        0xFE,
        "Ah, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear customers, are you going to sightsee during the\x01",
            "festival, too? How nice! Oh, how I envy you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_541A")

    label("loc_53CC")


    ChrTalk(
        0xFE,
        (
            "I want to go enjoy myself, too, but...\x01",
            "unfortunately, I have work to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_541A")

    Jump("loc_5626")

    label("loc_541F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5626")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5579")

    ChrTalk(
        0xFE,
        "#4SHurray for the Anniversary Festival!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, um, I've actually been kind\x01",
            "of worried about something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's been a really suspicious person\x01",
            "frequenting the store since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a man with glasses\x01",
            "and a fancy suit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He strikes me as suspicious.\x01",
            "What if he's a terrorist or something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5626")

    label("loc_5579")


    ChrTalk(
        0xFE,
        (
            "The suspicious man with glasses and a suit...\x01",
            "He seems to be at the second floor displays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should report him to the police?\x01",
            "*incoherent mumbling*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5626")

    TalkEnd(0xFE)
    Return()

    # Function_20_50E8 end

    def Function_21_562A(): pass

    label("Function_21_562A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_572C")

    ChrTalk(
        0xFE,
        (
            "Phew, I was studying at home during this year's\x01",
            "Anniversary Festival, but my family has made\x01",
            "me come pick up things at the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just really want to pass my medical intern exam\x01",
            "and work at St. Ursula Medical College!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB1")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_57CB")

    ChrTalk(
        0xFE,
        (
            "Why, hello! Isn't this 10 mira cheaper\x01",
            "than what my parents said it would be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Woohoo! Pocket change for me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just 10 mira, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BB1")

    label("loc_57CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5886")

    ChrTalk(
        0xFE,
        (
            "Even though they're imported goods,\x01",
            "they're still pretty cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since they can import them directly via rail, the\x01",
            "transportation expenses are almost non-existent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB1")

    label("loc_5886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5933")

    ChrTalk(
        0xFE,
        "Reference book, reference book...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Even though the Anniversary Festival is ending,\x01",
            "the life of a student who failed exams is still a struggle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB1")

    label("loc_5933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59FA")

    ChrTalk(
        0xFE,
        (
            "When my sister, Cirone, came home yesterday,\x01",
            "it was already evening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though she had finally gotten a vacation day,\x01",
            "we were only able to see each other during dinner...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB1")

    label("loc_59FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ADB")

    ChrTalk(
        0xFE,
        (
            "Geez, what's taking her?\x01",
            "I bet she's not coming at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since Cirone had the day off today,\x01",
            "she told me she'd come pick me up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sh-She didn't cause trouble for Meifa\x01",
            "again, did she?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5BB1")

    label("loc_5ADB")


    ChrTalk(
        0xFE,
        (
            "My sister Cirone has been causing mischief\x01",
            "for Meifa, her childhood friend, since\x01",
            "before I can even remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely she didn't forget about our plans\x01",
            "to explore the Anniversary Festival\x01",
            "together, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB1")

    TalkEnd(0xFE)
    Return()

    # Function_21_562A end

    def Function_22_5BB5(): pass

    label("Function_22_5BB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C80")

    ChrTalk(
        0xFE,
        (
            "That flier that came this morning blew me away!\x01",
            "It said that Times is staying open really late today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaah! How much will they keep tickling\x01",
            "my heart until they're satisfied?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F8C")

    label("loc_5C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5D1D")

    ChrTalk(
        0xFE,
        (
            "Well, I've finished my brief, little\x01",
            "window shopping session...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should shop for dinner\x01",
            "at Legion's Foods on the first floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F8C")

    label("loc_5D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5DD8")

    ChrTalk(
        0xFE,
        (
            "The first thing I'm going to do today is\x01",
            "check out Lucca Boutique again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They don't really put out new things every day,\x01",
            "but, oh, I just can't help taking a peek!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F8C")

    label("loc_5DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5E69")

    ChrTalk(
        0xFE,
        "This one...but there's that and that one, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gah, I don't know what to choose!\x01",
            "I can't decide on what I want to buy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F8C")

    label("loc_5E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EED")

    ChrTalk(
        0xFE,
        (
            "My Kean accompanies me on my shopping\x01",
            "trips without bellyaching at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've been blessed with a great son!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F8C")

    label("loc_5EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F8C")

    ChrTalk(
        0xFE,
        (
            "As a reward for continually doing my best, I'll lift\x01",
            "the embargo on my secret savings account!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, off I go to shop\x01",
            "to my heart's content!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F8C")

    TalkEnd(0xFE)
    Return()

    # Function_22_5BB5 end

    def Function_23_5F90(): pass

    label("Function_23_5F90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6059")

    ChrTalk(
        0xFE,
        (
            "*sigh* Apparently, I have to watch\x01",
            "my mom shop until crazy late at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "News that Times was staying open late was nothing\x01",
            "short of a thrill for Mom and other regulars...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_6059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_60F8")

    ChrTalk(
        0xFE,
        (
            "Hmm, Mom's window shopping\x01",
            "session seems to finally be\x01",
            "coming to an end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really easy to see when my\x01",
            "mom is starting to get tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_60F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_62EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_624B")

    ChrTalk(
        0x101,
        (
            "#0001F(It's possible that this kid might know\x01",
            "something about Colin.)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Huh? Uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm, I've never seen him before.\x01",
            "No clue who he is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI see... Thanks. I appreciate the help.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_62E5")

    label("loc_624B")


    ChrTalk(
        0xFE,
        "I'm sorry, I've never seen this child before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've seen a ton of kids hanging out in here\x01",
            "today, but I don't remember seeing anyone\x01",
            "like him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E5")

    Jump("loc_668D")

    label("loc_62EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6384")

    ChrTalk(
        0xFE,
        (
            "Mom's window shopping session seems\x01",
            "to finally be coming to an end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really easy to see when my\x01",
            "mom is starting to get tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_6384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6430")

    ChrTalk(
        0xFE,
        (
            "Mom has an unnaturally strong interest\x01",
            "in unusual boutique trinkets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like she's still a kid. Well, I guess\x01",
            "that's something to be happy about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_6430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_64D2")

    ChrTalk(
        0xFE,
        (
            "For my mom, being indecisive about what\x01",
            "to buy is an everyday phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, boy, who knows how many hours\x01",
            "it'll be until I can go home?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_64D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_65EF")

    ChrTalk(
        0xFE,
        (
            "If I let my mom go shopping alone,\x01",
            "she'd probably loiter around the\x01",
            "department store all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why Dad made it my responsibility\x01",
            "to make sure Mom makes it home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He says this is a life-and-death situation\x01",
            "for our family, so I guess I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_668D")

    label("loc_65EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_668D")

    ChrTalk(
        0xFE,
        (
            "Mom often says that she's going\x01",
            "to buy herself a reward, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't it be nice if I got some kind\x01",
            "of reward for watching her all day?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_668D")

    TalkEnd(0xFE)
    Return()

    # Function_23_5F90 end

    def Function_24_6691(): pass

    label("Function_24_6691")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_679A")

    ChrTalk(
        0xFE,
        (
            "My wife was delighted when I gave her\x01",
            "the brooch I picked out here yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm ashamed to have been putting on\x01",
            "such a bossy attitude at the house, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I've decided to start\x01",
            "surprising her with gifts occasionally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ABA")

    label("loc_679A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_681B")

    ChrTalk(
        0xFE,
        (
            "This is a problem... We've never really\x01",
            "been the gift-giving type until now, so\x01",
            "I don't know what to get her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ABA")

    label("loc_681B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_686B")

    ChrTalk(
        0xFE,
        (
            "Hmm, what could I get my lady that\x01",
            "would make her overjoyed?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ABA")

    label("loc_686B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_691F")

    ChrTalk(
        0xFE,
        "Of course, a ring is an obvious choice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The thing is, if I got her one as a gift,\x01",
            "I'd just remember my proposal to her,\x01",
            "and my cheeks would light up red...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ABA")

    label("loc_691F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_69E2")

    ChrTalk(
        0xFE,
        (
            "Since it's the Anniversary Festival,\x01",
            "I've decided to buy my wife a gift I've\x01",
            "been meaning to get for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I haven't decided on what she would like, though...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6ABA")

    label("loc_69E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6ABA")

    ChrTalk(
        0xFE,
        (
            "I was able to go hear Mayor\x01",
            "MacDowell's amazing speech\x01",
            "at the ceremony yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While he might have different opinions\x01",
            "than Speaker Hartmann, you can tell\x01",
            "he wants to protect Crossbell's future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ABA")

    TalkEnd(0xFE)
    Return()

    # Function_24_6691 end

    def Function_25_6ABE(): pass

    label("Function_25_6ABE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B96")

    ChrTalk(
        0x160,
        (
            "#3300F(Should we conclude the Central\x01",
            "Square investigation here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yeah, I think we've covered enough ground.)\x02\x03",
            "(Let's try searching for leads\x01",
            "at Station Street next.)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_6B96")

    Return()

    # Function_25_6ABE end

    def Function_26_6B97(): pass

    label("Function_26_6B97")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F - Lucca Boutique\x01",
            "2F - Hanson Shoes\x01",
            "2F - Baker's Accessories\x01",
            "1F - Legion's Foods\x01",
            "1F - Southwark General Store\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If there is anything you are unclear on,\x01",
            "simply ask the information desk up front.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_26_6B97 end

    def Function_27_6C90(): pass

    label("Function_27_6C90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 3300, 19500, 0)
    MoveCamera(57, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44000, 0)
    SetChrPos(0x101, 600, 30, -2000, 0)
    SetChrPos(0x160, -600, 30, -2200, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    OP_68(0, 1300, 7500, 7000)
    MoveCamera(40, 25, 0, 7000)
    SetCameraDistance(29000, 7000)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_6D79():
        OP_96(0xFE, 0x258, 0x1E, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D79)

    def lambda_6D93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D93)
    Sleep(100)

    def lambda_6DA7():
        OP_96(0xFE, 0xFFFFFDA8, 0x1E, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_6DA7)

    def lambda_6DC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_6DC1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x160, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, 2500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3400366V#0006FThere sure are a lot of people...\x02\x03",
            "#3400367V#0000FLet's check out this place for a little\x01",
            "while, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400368V#12P#3300FFine with me.\x02\x03",
            "#3400369V#3304FBesides, I think asking the reception ladies\x01",
            "and the kids around here will prove sufficient.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x160, 500)

    ChrTalk(
        0x101,
        (
            "#3400370V#0012F#11PMy thoughts exactly...\x02\x03",
            "#3400371V#0000FRenne, you have a good head on your\x01",
            "shoulders, you know that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x160,
        "#3400372V#6P#3309FHeehee. It's one of my best assets.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 3)
    EventEnd(0x5)
    Return()

    # Function_27_6C90 end

    SaveToFile()

Try(main)
