from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1020.bin",                # FileName
        "t1020",                    # MapName
        "t1020",                    # Location
        0x0095,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1020",                  # 0
        "Elise",                  # 1
        "Young Man",              # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Woman",                  # 5
        "Girl",                   # 6
        "Clerk",                  # 7
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch21600.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch25900.itc",                   # 06
    ))

    DeclNpc(-24909,  0,       5570,    90,   257,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(100139,  0,       18219,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4190,    0,       13079,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(97510,   0,       5429,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-23930,  0,       11470,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22840,  0,       10689,   315,  401,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-18940,  0,       12609,   180,  385,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  26.5,                  8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -8.833333969116211,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  8.5,                   8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.8333334922790527,   -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  -11.0,                 8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 13,  -19.030000686645508,   11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.515000343322754,     -7.53164529800415,     0.20000000298023224,   1.0])

    DeclActor(27660,   0,       10070,   1200,    27660,   1500,    10070,   0x007C, 0,  18, 0x0000)
    DeclActor(19000,   0,       11850,   2000,    19000,   1000,    11850,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_46B",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_566",          # 04, 4
        "Function_5_5CB",          # 05, 5
        "Function_6_708",          # 06, 6
        "Function_7_746",          # 07, 7
        "Function_8_8CF",          # 08, 8
        "Function_9_A6F",          # 09, 9
        "Function_10_BD9",         # 0A, 10
        "Function_11_C70",         # 0B, 11
        "Function_12_CDA",         # 0C, 12
        "Function_13_DDA",         # 0D, 13
        "Function_14_13C0",        # 0E, 14
        "Function_15_1836",        # 0F, 15
        "Function_16_1DB5",        # 10, 16
        "Function_17_1FEE",        # 11, 17
        "Function_18_2039",        # 12, 18
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A")
    OP_94(0xFE, 0x17D0E, 0x3F0C, 0x19154, 0x47A4, 0x3E8)
    Sleep(150)
    Jump("Function_1_440")

    label("loc_46A")

    Return()

    # Function_1_440 end

    def Function_2_46B(): pass

    label("Function_2_46B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_94(0xFE, 0x3AC, 0x28D2, 0x12FC, 0x37E6, 0x3E8)
    Sleep(300)
    Jump("Function_2_46B")

    label("loc_495")

    Return()

    # Function_2_46B end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    Event(0, 15)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_565")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4D4")
    Jump("loc_565")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4E2")
    Jump("loc_565")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4F0")
    Jump("loc_565")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_565")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, -13780, 0, 6020, 90)
    SetChrPos(0xA, -12240, 0, 6020, 270)
    Jump("loc_565")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_55C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_565")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_565")

    label("loc_565")

    Return()

    # Function_3_496 end

    def Function_4_566(): pass

    label("Function_4_566")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_5A8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C4")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x1, 0x1)

    label("loc_5C4")

    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_566 end

    def Function_5_5CB(): pass

    label("Function_5_5CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5DC")
    Jump("loc_704")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5EA")
    Jump("loc_704")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_704")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_704")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_704")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_65C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    Call(0, 8)
    Jump("loc_657")

    label("loc_62F")


    ChrTalk(
        0xFE,
        "These commoners are such a bother.\x02",
    )

    CloseMessageWindow()

    label("loc_657")

    Jump("loc_704")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_6FB")

    ChrTalk(
        0xFE,
        (
            "*sigh* Every time I stop by Mishelam, be it for\x01",
            "business or pleasure, it's always so crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Coming here to shop is a feat in itself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_704")

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_704")

    label("loc_704")

    TalkEnd(0xFE)
    Return()

    # Function_5_5CB end

    def Function_6_708(): pass

    label("Function_6_708")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "THE DAY HAS FINALLY COME!\x01",
            "WAIT FOR ME, MISHYYYYY!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_708 end

    def Function_7_746(): pass

    label("Function_7_746")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_757")
    Jump("loc_8CB")

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_765")
    Jump("loc_8CB")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_773")
    Jump("loc_8CB")

    label("loc_773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_781")
    Jump("loc_8CB")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_78F")
    Jump("loc_8CB")

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_7FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AA")
    Call(0, 8)
    Jump("loc_7FA")

    label("loc_7AA")


    ChrTalk(
        0xFE,
        (
            "Well... The young ladies here don't\x01",
            "seem to fall for the rich man's charm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FA")

    Jump("loc_8CB")

    label("loc_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(
        0xFE,
        (
            "Honestly, everywhere I look, there's nothing\x01",
            "but swarms of young, wealthy ladies! I shouldn't\x01",
            "have expected anything less of Mishelam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right... Time to show my stuff!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CB")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8CB")

    label("loc_8CB")

    TalkEnd(0xFE)
    Return()

    # Function_7_746 end

    def Function_8_8CF(): pass

    label("Function_8_8CF")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    ChrTalk(
        0xA,
        (
            "Hey, miss. Feeling hungry? I'd love to\x01",
            "treat you to something nice at the\x01",
            "restaurant, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mira isn't an issue! I made sure to\x01",
            "bring a lot with me for this trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks, but no thanks. I don't see\x01",
            "any particular reason why I'd want to\x01",
            "be treated to a meal by you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Besides, I'm willing to bet that I have\x01",
            "much, much more mira than you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4SHuh?!#3S\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_8CF end

    def Function_9_A6F(): pass

    label("Function_9_A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")

    ChrTalk(
        0xFE,
        (
            "The Fortuna... Hmm, it definitely knows\x01",
            "how to draw in a customer, with a\x01",
            "gorgeous aesthetic like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aesthetic or not, what truly matters is\x01",
            "how the food tastes! A food connoisseur\x01",
            "like myself won't be fooled by looks alone!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BD5")

    label("loc_B72")


    ChrTalk(
        0xFE,
        (
            "Now, by my tongue, I will test whether\x01",
            "this famous restaurant can live up to\x01",
            "expectations...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD5")

    TalkEnd(0xFE)
    Return()

    # Function_9_A6F end

    def Function_10_BD9(): pass

    label("Function_10_BD9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This jewelry store doesn't let anyone step\x01",
            "inside without a letter of introduction,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh! This is absolutely unbelievable!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_BD9 end

    def Function_11_C70(): pass

    label("Function_11_C70")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mama... You've been looking at this\x01",
            "jewelry stuff foreeever! Let's go play\x01",
            "at the theme park!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_C70 end

    def Function_12_CDA(): pass

    label("Function_12_CDA")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBD")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_DBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_DD9")

    Return()

    # Function_12_CDA end

    def Function_13_DDA(): pass

    label("Function_13_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-19000, 1000, 11800, 0)
    SetChrPos(0x101, -19330, 0, 8810, 0)
    SetChrPos(0x102, -17960, 0, 8810, 0)
    SetChrPos(0x103, -20760, 0, 10150, 45)
    SetChrPos(0x104, -16940, 0, 9380, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5F")
    SetChrPos(0x151, -18610, 0, 7180, 0)

    label("loc_E5F")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -19000, 0, 12900, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)

    def lambda_E9F():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x2C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E9F)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0x101,
        "#0005FWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PWelcome to Diamante Jewelers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PPardon me, sir. By any chance, do you\x01",
            "have a letter of introduction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FOh, umm... I assume it's necessary\x01",
            "in order to shop here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PIndeed. Store policy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThis store only serves members, so I must insist\x01",
            "that you refrain from trying to enter from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PNow, then, if you would...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(100)

    def lambda_104F():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x3264, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_104F)
    Sleep(300)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    WaitChrThread(0xE, 1)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xE, 0x80)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x103,
        "#0211FNo mercy for first-time shoppers, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0310FWh-What the hell's up with that?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1299")

    ChrTalk(
        0x151,
        (
            "#5704FDon't panic too much. That's how most of\x01",
            "the stores around here operate, actually.\x02\x03",
            "A shame. With certain, expensive jewelry\x01",
            "to accompany your outfits, your camouflage\x01",
            "would be almost foolproof.\x02\x03",
            "#5702FWell, nothing we can do for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYeah, I guess so... For now, we should\x01",
            "focus on the boutique.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131F")

    label("loc_1299")


    ChrTalk(
        0x101,
        (
            "#0006FThat guy doesn't seem too eager for us to\x01",
            "return, so let's ignore this place for now.\x01",
            "Wouldn't want security called on us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131F")

    OP_5A()
    SetScenarioFlags(0xAE, 1)
    EventEnd(0x5)
    Jump("loc_13BF")

    label("loc_132A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThe store's employee told us it's limited\x01",
            "to members only. There's no point in\x01",
            "trying to force our way inside, now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)

    label("loc_13BF")

    Return()

    # Function_13_DDA end

    def Function_14_13C0(): pass

    label("Function_14_13C0")

    EventBegin(0x0)
    Fade(1000)
    OP_68(27100, 1600, 7920, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 25000, 0, 7600, 90)
    SetChrPos(0x102, 23800, 0, 8900, 90)
    SetChrPos(0x103, 23800, 0, 7600, 90)
    SetChrPos(0x104, 25000, 0, 8900, 90)
    OP_68(25100, 1600, 7920, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#3500417V#0001F#5PAnyone know what's past here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500418V#0105F#5PI'm not sure, but it must be blocked\x01",
            "for a reason...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#3500419V#0305F#5POh, there's somethin' written here.\x02",
    )

    CloseMessageWindow()
    OP_68(26500, 1600, 7920, 3000)

    def lambda_1537():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1537)
    Sleep(300)

    def lambda_154F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_154F)
    Sleep(100)

    def lambda_1567():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1567)
    Sleep(50)

    def lambda_157F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_157F)
    WaitChrThread(0x104, 1)

    def lambda_1598():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1598)
    WaitChrThread(0x101, 1)

    def lambda_15A9():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A9)
    WaitChrThread(0x102, 1)

    def lambda_15BA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15BA)
    WaitChrThread(0x103, 1)

    def lambda_15CB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15CB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The area past this point is under construction.\x01",
            "Please refrain from trespassing.\x01",
            "      - Mishelam Development Division\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    ChrTalk(
        0x103,
        "#3500420V#0200F#6PSo the area up ahead is not finished yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500421V#0103F#5PMishelam must still have some projects in\x01",
            "the works...\x02\x03",
            "#3500422V#0100FWhatever it is, I'm sure it'll be a sight to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500423V#0306F#5PI bet they just like burnin' mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500424V#0000F#6PWell, no use in hanging around here.\x01",
            "Let's check out the other places.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 25630, 0, 8109, 270)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1833")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1833")

    EventEnd(0x5)
    Return()

    # Function_14_13C0 end

    def Function_15_1836(): pass

    label("Function_15_1836")

    EventBegin(0x0)
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(-50, 1100, 8000, 0)
    MoveCamera(335, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20090, 0)
    SetCameraDistance(18590, 2000)
    SetChrPos(0x101, 0, 0, 9300, 180)
    SetChrPos(0x102, 0, 0, 6700, 0)
    SetChrPos(0x103, 1200, 0, 8000, 270)
    SetChrPos(0x104, -1200, 0, 8000, 90)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3500425V#0003F#11PWe know one thing for sure after our\x01",
            "patrol of Mishelam...\x02\x03",
            "#3500426V#0001FWe're going to have to come up with some\x01",
            "method to enter the auction incognito.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500427V#0301F#5PTrue. After all, one glance at us, and the\x01",
            "mafia guardin' the entrance will lose it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500428V#0205F#12PSomething else has been bothering me.\x01",
            "Are the invitations really all we need?\x02\x03",
            "#3500429V#0201FThey might have a system in place to\x01",
            "check our identities, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500430V#0103F#6PI agree. It's risky.\x02\x03",
            "#3500431V#0108FI wish we thought of this sooner. Maybe\x01",
            "we could have asked Renne about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500432V#0000F#11PEither way, let's just go with the assumption\x01",
            "that if we have an invitation, we'll be let in.\x02\x03",
            "#3500433V#0006FFor now, I just want to find a place to clear\x01",
            "our heads and relax.\x02\x03",
            "#3500434V#0008FThe restaurant would be too open...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500435V#0200F#12PShould we check to see if the hotel has\x01",
            "any vacancies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500436V#0106F#6PHmm, I doubt there'd be any, with\x01",
            "Mishelam being as busy as it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500437V#0300F#5PHey, maybe we'll get lucky and someone\x01",
            "canceled their reservation.\x02\x03",
            "#3500438VMight as well ask the front desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500439V#0000F#11PYeah. Let's do that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 400, 0, 7770, 0)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0xA4, 4)
    OP_29(0x47, 0x1, 0x3)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_15_1836 end

    def Function_16_1DB5(): pass

    label("Function_16_1DB5")

    EventBegin(0x0)
    Fade(1000)
    OP_68(19000, 1000, 10600, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 19000, 0, 10600, 0)
    SetChrPos(0x102, 18350, 0, 9300, 0)
    SetChrPos(0x103, 19650, 0, 9300, 0)
    SetChrPos(0x104, 18350, 0, 8000, 0)
    SetChrPos(0x151, 19650, 0, 8000, 0)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0003F#5P(Once we get dressed, there's no going back.)\x02\x03",
            "#0001F(I have to choose who's going to accompany\x01",
            "me to the auction, too. Are we ready...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Continue investigating.\x01",           # 0
            "Get dressed at the boutique.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F52"),
        (1, "loc_1F6A"),
        (SWITCH_DEFAULT, "loc_1FED"),
    )


    label("loc_1F52")

    SetChrPos(0x0, 19000, 0, 9300, 180)
    EventEnd(0x5)
    Jump("loc_1FED")

    label("loc_1F6A")

    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(19000, 1000, 11600, 5000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x151, 3, 0, 17)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x151, 0x3)
    NewScene("t1040", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FED")

    label("loc_1FED")

    Return()

    # Function_16_1DB5 end

    def Function_17_1FEE(): pass

    label("Function_17_1FEE")

    OP_95(0xFE, 19000, 0, 10600, 2000, 0x1)

    def lambda_2007():
        OP_95(0xFE, 19000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2007)
    Sleep(400)

    def lambda_2024():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2024)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_1FEE end

    def Function_18_2039(): pass

    label("Function_18_2039")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The area past this point is under construction.\x01",
            "Please refrain from trespassing.\x01",
            "      - Mishelam Development Division\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_2039 end

    SaveToFile()

Try(main)
