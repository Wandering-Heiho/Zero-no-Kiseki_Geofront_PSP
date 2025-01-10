from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c045b.bin",                # FileName
        "c045b",                    # MapName
        "c045b",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c045b",                  # 0
        "Receptionist Kyle",      # 1
        "Doris",                  # 2
        "Aeron",                  # 3
        "Manager Leticia",        # 4
        "Hotel Guest",            # 5
        "Hotel Guest",            # 6
        "Hotel Guest",            # 7
        "Hotel Guest",            # 8
        "Hotel Guest",            # 9
        "Gantz",                  # 10
        "Hostess",                # 11
        "Hostess",                # 12
        "Tableware",              # 13
        "Tableware",              # 14
        "Tableware",              # 15
        "酒",                     # 16
        "酒",                     # 17
        "酒",                     # 18
        "酒",                     # 19
        "酒",                     # 20
    ))

    AddCharChip((
        "apl/ch50403.itc",                   # 00
        "chr/ch26802.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "apl/ch50090.itc",                   # 03
        "apl/ch50091.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch25700.itc",                   # 06
        "chr/ch27500.itc",                   # 07
        "chr/ch27900.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch34300.itc",                   # 0A
        "chr/ch21800.itc",                   # 0B
        "chr/ch33000.itc",                   # 0C
        "chr/ch32400.itc",                   # 0D
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4909,    0,       59669,   270,  277,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3529,    0,       59669,   90,   277,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(115110,  0,       62319,   0,    277,  0x0, 0,   9,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(112750,  0,       57849,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(153279,  0,       61220,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1769,    0,       7150,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2640,    0,       7760,    270,  261,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(168500,  150,     6300,    180,  311,  0x0, 0,   0,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(167699,  150,     6300,    180,  261,  0x0, 1,   2,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(169300,  150,     6300,    180,  261,  0x0, 2,   1,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(168500,  349,     4599,    0,    374,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(167800,  349,     4599,    0,    374,  0x0, 1,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(169199,  349,     4599,    0,    374,  0x0, 5,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168500,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168899,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168100,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168300,  449,     3799,    0,    374,  0x0, 29,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168699,  449,     3799,    0,    374,  0x0, 30,  3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(168500,  0,       4000,    1500,    168500,  1650,    6300,    0x007E, 0,  16, 0x0000)
    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  5,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  7,  0x0000)
    DeclActor(68050,   0,       11560,   1200,    68050,   1500,    11560,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_3DC",          # 00, 0
        "Function_1_494",          # 01, 1
        "Function_2_4F5",          # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_521",          # 04, 4
        "Function_5_539",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_7F9",          # 07, 7
        "Function_8_7FD",          # 08, 8
        "Function_9_A62",          # 09, 9
        "Function_10_B0C",         # 0A, 10
        "Function_11_BC2",         # 0B, 11
        "Function_12_C36",         # 0C, 12
        "Function_13_C7D",         # 0D, 13
        "Function_14_D2C",         # 0E, 14
        "Function_15_E53",         # 0F, 15
        "Function_16_EF4",         # 10, 16
        "Function_17_EF8",         # 11, 17
        "Function_18_F0F",         # 12, 18
        "Function_19_1020",        # 13, 19
    ))


    def Function_0_3DC(): pass

    label("Function_0_3DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_41C"),
        (1, "loc_428"),
        (2, "loc_434"),
        (3, "loc_440"),
        (4, "loc_44C"),
        (5, "loc_458"),
        (6, "loc_464"),
        (SWITCH_DEFAULT, "loc_470"),
    )


    label("loc_41C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_428")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_434")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_440")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_44C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_458")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_493")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_493")

    Return()

    # Function_0_3DC end

    def Function_1_494(): pass

    label("Function_1_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F4")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_494")

    label("loc_4F4")

    Return()

    # Function_1_494 end

    def Function_2_4F5(): pass

    label("Function_2_4F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_4F5")

    label("loc_51F")

    Return()

    # Function_2_4F5 end

    def Function_3_520(): pass

    label("Function_3_520")

    Return()

    # Function_3_520 end

    def Function_4_521(): pass

    label("Function_4_521")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_538")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_538")

    Return()

    # Function_4_521 end

    def Function_5_539(): pass

    label("Function_5_539")

    Call(0, 6)
    Return()

    # Function_5_539 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C3")

    ChrTalk(
        0xB,
        "Welcome to Hotel Millennium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We provide only the finest quality of\x01",
            "service at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We make for the perfect place to rest in Crossbell,\x01",
            "the entertainment capital of Zemuria!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_6C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_71E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F0")

    label("loc_73E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_752")
    Jump("loc_7F0")

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        "Oh, will you be staying here for the night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have one vacant room currently\x01",
            "available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please make a decision ASAP.\x02",
    )

    CloseMessageWindow()

    label("loc_7F0")

    Jump("loc_6CD")

    label("loc_7F5")

    TalkEnd(0xB)
    Return()

    # Function_6_53D end

    def Function_7_7F9(): pass

    label("Function_7_7F9")

    Call(0, 8)
    Return()

    # Function_7_7F9 end

    def Function_8_7FD(): pass

    label("Function_8_7FD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_932")

    ChrTalk(
        0x8,
        "Good day. Welcome to Hotel Millenium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish to reserve a room, you may\x01",
            "do so at this front desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_932")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_98D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A59")

    label("loc_9AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C1")
    Jump("loc_A59")

    label("loc_9C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "Our deluxe suites are on the top\x01",
            "floor of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just head up the stairs behind\x01",
            "you to get to the deluxe suites.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A59")

    Jump("loc_93C")

    label("loc_A5E")

    TalkEnd(0x8)
    Return()

    # Function_8_7FD end

    def Function_9_A62(): pass

    label("Function_9_A62")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "Tips are entirely at the patron's discretion,\x01",
            "so please calm down, Doris.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This isn't something we should be discussing\x01",
            "in front of other guests.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_A62 end

    def Function_10_B0C(): pass

    label("Function_10_B0C")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "I just received an outrageous tip from\x01",
            "a guest staying on the top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wh-What am I even supposed to do with this\x01",
            "huge wad of mira? Do I tell the manager?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_10_B0C end

    def Function_11_BC2(): pass

    label("Function_11_BC2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What a wonderful night we're having.\x01",
            "Now's the time for some vintage wine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hahaha... Hahahahahaha!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_BC2 end

    def Function_12_C36(): pass

    label("Function_12_C36")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, Dad. Why do you always feel the\x01",
            "need to be so pompous?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_C36 end

    def Function_13_C7D(): pass

    label("Function_13_C7D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I wasn't expecting my client to make\x01",
            "reservations at such a lavish hotel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Half of it is just for entertainment expenses.\x01",
            "That's sure going to cost him later.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_C7D end

    def Function_14_D2C(): pass

    label("Function_14_D2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(
        0xFE,
        (
            "I've reserved a room on the\x01",
            "top floor with my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is my favorite place to stay\x01",
            "whenever I come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E4F")

    label("loc_DBF")


    ChrTalk(
        0xFE,
        (
            "Oh, apparently, somebody's reserved\x01",
            "a deluxe suite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who do you think it is? The son of a noble,\x01",
            "perhaps? I'm pretty curious about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4F")

    TalkEnd(0xFE)
    Return()

    # Function_14_D2C end

    def Function_15_E53(): pass

    label("Function_15_E53")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hotel Millennium has been famous for a long\x01",
            "time, due to its luxurious services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's my personal creed to always\x01",
            "stay in places you can trust!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_E53 end

    def Function_16_EF4(): pass

    label("Function_16_EF4")

    Call(0, 17)
    Return()

    # Function_16_EF4 end

    def Function_17_EF8(): pass

    label("Function_17_EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0E")
    Call(0, 19)
    Jump("loc_F0E")

    label("loc_F0E")

    Return()

    # Function_17_EF8 end

    def Function_18_F0F(): pass

    label("Function_18_F0F")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Gantz's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zzz...*hic*...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101C")

    ChrTalk(
        0x101,
        "#0001FSounds like Gantz is passed out drunk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FShall we return to the SSS building?\x01",
            "KeA's waiting for us back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FYeah, good call.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_101C")

    TalkEnd(0xFF)
    Return()

    # Function_18_F0F end

    def Function_19_1020(): pass

    label("Function_19_1020")

    EventBegin(0x0)
    Fade(1000)
    OP_68(168500, 1000, 4800, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 169000, 0, 2900, 0)
    SetChrPos(0x103, 169300, 0, 1800, 0)
    SetChrPos(0x102, 167700, 0, 2100, 0)
    SetChrPos(0x104, 168000, 0, 2900, 0)
    SetChrPos(0x11, 168500, 150, 6300, 180)
    SetChrPos(0x12, 167700, 150, 6300, 180)
    SetChrPos(0x13, 169300, 150, 6300, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis083.itp")
    OP_0D()
    SetChrSubChip(0x12, 0x0)
    Sleep(50)
    SetChrSubChip(0x13, 0x0)
    Sleep(300)

    ChrTalk(
        0x12,
        "#4100624V#11PIs that you, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4100625V#11POh, my. Long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100626V#0309F#5PHaha. Pleasure seein' you again.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x11,
        "Drunk Man",
        "#4100627V#11PWho da hell're you people?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100628V#6P#0003FExcuse us, sir. We're with the CPD.\x02\x03",
            "#4100629V#0000FYou must be Gantz from Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100630V#11P*hic* That'sh right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100631V#11PAin't I met'cha shomewhere before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100632V#6P#0005FHave we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100633V#6P#0211FI recognize this man...\x02\x03",
            "#4100634VDid we not save him from war hounds\x01",
            "during the Mainz incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100635V#6P#0011FOh!\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x102,
        "#4100636V#0105FThat was him...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x1F4)

    ChrTalk(
        0x11,
        "#4100637V#11PHuh... Think I 'member now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100638V#11PY'all those kidsh from way back when,\x01",
            "ain'tcha?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100639V#11PSo, what'cha want? *hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100640V#6P#0006FWell, we received a request from\x01",
            "the mayor of Mainz...\x02\x03",
            "#4100641V#0000FA request to track you down.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#4100642V#11PThe mayor'sh lookin' for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100643V#11P*hic* What in the hell for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100644V#0301F#5PC'mon, man. You've been here for, like, two\x01",
            "weeks without contactin' anyone, yeah?\x02\x03",
            "#4100645VEveryone's all worried about you. They\x01",
            "thought ya went missin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100646V#6P#0100FAs such, we were requested to\x01",
            "find you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4100647V#11P*hic* M'kay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100648V#11PWell, ya found me. Congrats. So can ya\x01",
            "go ahead an' buzz off now, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100649V#11PI ain't ever goin' back to a hellhole\x01",
            "like Mainz for as long as I live.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100650V#6P#0005FWh-Why's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100651V#6P#0205FFor what reason?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x11,
        "#4100652V#11PBwahaha! Ain't it obvious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100653V#11PI'm da greatesht gambler this shtate\x01",
            "has ever seen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100654V#11PAnd it ain't just my killer skill at da tables!\x01",
            "Lady Luck is my bitch, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100655V#11PWho da hell would wanna go back to\x01",
            "Mainz just to smash rocksh all day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100656V#6P#0106FWait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100657V#0301F#5PWatch it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100658V#6P#0006FAre you sure that's what you want?\x02\x03",
            "#4100659V#0001FEverybody's worried sick about you.\x01",
            "You could at least contact the mayor\x01",
            "and give him some peace--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x11,
        (
            "#4100660V#11P#4SSHUDDUP! YA CAN'T ORDER\x01",
            "ME TO DO SHIT!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100661V#11PHeh. One more round at Barca and it'll be\x01",
            "off to Mishelam for me...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x11,
        (
            "#4100662V#5PHey, ladies! How 'bout I take yous to that\x01",
            "fanshy shmancy theme park this weekend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4100663V#5PYa can pick whatever you want from those\x01",
            "boutiques they got, too. Bill's on me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x13, 0x2)
    Sleep(300)

    ChrTalk(
        0x12,
        "#4100664V#5PWooooow, really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4100665V#11PTeehee... We can't wait to go!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    LoadChrToIndex("chr/ch26800.itc", 0x1E)
    LoadChrToIndex("chr/ch26900.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    OP_68(68000, 1000, 10700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 68000, 0, 13000, 180)
    SetChrPos(0x102, 68000, 0, 13000, 180)
    SetChrPos(0x103, 68000, 0, 13000, 180)
    SetChrPos(0x104, 68000, 0, 13000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x12, 68000, 0, 13000, 180)
    SetChrPos(0x13, 68000, 0, 13000, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_68(68000, 1000, 7700, 3000)

    def lambda_1D96():
        OP_96(0xFE, 0x109A0, 0x0, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D96)

    def lambda_1DB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DB0)
    Sleep(500)

    def lambda_1DC4():
        OP_96(0xFE, 0x105B8, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DC4)

    def lambda_1DDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DDE)
    Sleep(300)

    def lambda_1DF2():
        OP_96(0xFE, 0x10D88, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DF2)

    def lambda_1E0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E0C)
    Sleep(500)

    def lambda_1E20():
        OP_96(0xFE, 0x109A0, 0x0, 0x21FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E20)

    def lambda_1E3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E3A)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)

    def lambda_1E61():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E61)
    WaitChrThread(0x102, 1)

    def lambda_1E72():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1E72)
    WaitChrThread(0x103, 1)

    def lambda_1E83():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E83)
    WaitChrThread(0x104, 1)

    def lambda_1E94():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E94)
    WaitChrThread(0x104, 2)
    OP_79(0x1)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#4100666V#0303F#11PAin't much we can do about him.\x02\x03",
            "#4100667V#0301FDude's way too full of himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100668V#6P#0006FThat he is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100669V#0106F#5PRegardless, we're still obligated to inform\x01",
            "the mayor of the situation.\x02\x03",
            "#4100670V#0101FIt's not our right to force him to return\x01",
            "to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100671V#12P#0206FIndeed. It was his own conscious decision.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100672V#6P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4100673V#0105F#5PWhat's on your mind, Lloyd? You look\x01",
            "like something's bothering you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20AE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_20AE)

    ChrTalk(
        0x101,
        (
            "#4100674V#6P#0006FYeah, so here's the thing...\x02\x03",
            "#4100675VHe was just an amateur gambler who\x01",
            "played casually. I doubt he's nearly\x01",
            "lucky or sharp enough to be good...\x02\x03",
            "#4100676V#0001FYet somehow, he's suddenly on multiple\x01",
            "winning streaks? No matter how I analyze\x01",
            "the situation, it just doesn't add up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100677V#0105F#5PThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100678V#0301F#11PYeah, that sure sounds fishy to me.\x02\x03",
            "#4100679V#0306FYa think he'd tell me all his tricks if\x01",
            "I butter him up with a few drinks?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#4100680V#6P#0205FAre you not already a skilled gambler,\x01",
            "Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100681V#0300F#11POnly when I'm on a hot streak, my friend!\x02\x03",
            "#4100682V#0306FNot a chance in hell I'd pull off wins for\x01",
            "two consecutive weeks and win half\x01",
            "a million mira.\x02\x03",
            "#4100683V#0302FPretty sure you'd only be able to pull that\x01",
            "off if you were as skilled as Jack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100684V#0106F#5PJack's a fictional character, Randy.\x02",
    )

    CloseMessageWindow()
    OP_68(68000, 1000, 9700, 2000)
    MoveCamera(310, 23, 0, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_247E():
        OP_96(0xFE, 0x10B94, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_247E)

    def lambda_2498():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2498)

    def lambda_24A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24A9)
    Sleep(50)

    def lambda_24B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24B9)
    Sleep(50)

    def lambda_24C9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24C9)
    Sleep(400)

    def lambda_24D9():
        OP_96(0xFE, 0x107AC, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_24D9)

    def lambda_24F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_24F3)

    def lambda_2504():
        OP_96(0xFE, 0x109A0, 0x0, 0x2008, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2504)
    WaitChrThread(0x13, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x12, 1)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x13,
        "#4100685V#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4100686V#5PThe heck? You guys were still around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100687V#0306F#6PWhoa! Take it down a notch, sweet-cheeks.\x02\x03",
            "#4100688V#0300FCan I ask you two hunnies somethin'\x01",
            "real quick?\x02\x03",
            "#4100689VI'm just a lil' curious about this Gantz\x01",
            "fellow in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4100690V#11PGo right ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4100691V#5POoh, what is it? Is he involved in\x01",
            "some sorta crime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100692V#0303F#6PNah. It ain't nothin' like that.\x02\x03",
            "#4100693V#0301FJust wonderin' if he's always been such\x01",
            "an arrogant jackass.\x02\x03",
            "#4100694VEven with the few drinks he had,\x01",
            "he laid the attitude on a bit thick, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#4100695V#11PHmm. Yeah, I can see what you mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100696V#11PIt's true, he wasn't nearly as cocky\x01",
            "when he first started gambling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4100697V#5PBut as time went on, his victories began\x01",
            "to feed his ego.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4100698V#5PThough we're just hostesses, so\x01",
            "we don't really mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100699V#0303F#6PYeah? I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100700V#6P#0008FSo it's safe to say that the arrogance\x01",
            "wasn't stemming from alcohol, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100701V#11PPersonality aside, that man is something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100702V#11PIt's almost as if he could see through\x01",
            "the cards while they were laid down.\x01",
            "He must have razor-sharp senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#4100703V#5PNo kidding! It's totally insane, to be honest.\x01",
            "He even won straight up bets at the\x01",
            "roulette table, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4100704V#5PYou think he can read the dealer's mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100705V#0105F#6PThat does sound most impressive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100706V#6P#0006F*sigh* Sounds more like a major power\x01",
            "than being perceptive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100707V#0310F#6PDamn it! Why couldn't Aidios have blessed\x01",
            "me with such wonderful talents?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100737V#6P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100709V#11PAnyway, that's about all we know\x01",
            "about Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4100710V#5PAre we good to get back to work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100711V#0309F#6PYep! You've been real helpful.\x02\x03",
            "#4100712V#0302FThink I'll come see you cuties again\x01",
            "when I get some free time 'round here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#4100713V#11PTeehee. I won't get my hopes up,\x01",
            "but I'll be waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#4100714V#5PAnyway, I'm going to go back to work now.\x02",
    )

    CloseMessageWindow()

    def lambda_2D5A():

        label("loc_2D5A")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_2D5A")

    QueueWorkItem2(0x101, 2, lambda_2D5A)

    def lambda_2D6C():

        label("loc_2D6C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_2D6C")

    QueueWorkItem2(0x102, 2, lambda_2D6C)

    def lambda_2D7E():

        label("loc_2D7E")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2D7E")

    QueueWorkItem2(0x103, 2, lambda_2D7E)

    def lambda_2D90():

        label("loc_2D90")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2D90")

    QueueWorkItem2(0x104, 2, lambda_2D90)

    def lambda_2DA2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DA2)
    Sleep(50)

    def lambda_2DB2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2DB2)
    WaitChrThread(0x12, 2)
    OP_68(65000, 1000, 7700, 5000)

    def lambda_2DD4():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DD4)
    WaitChrThread(0x13, 2)

    def lambda_2DF2():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2DF2)
    OP_6F(0x79)
    Fade(500)
    OP_68(68000, 1000, 7700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x104, 68000, 0, 8700, 270)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4100715V#0101F#5PIn any case, we should convey this\x01",
            "information to the mayor.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EE4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2EE4)

    def lambda_2EF1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2EF1)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#4100716V#6P#0006FYeah. Give me a second. I'll call him.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd pulled out Mayor Bickson's phone\x01",
            "number and dialed it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100717V\x07\x05",
            "Hello, this is Bickson speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100718V\x07\x00",
            "#0000FGood evening, sir. This is Lloyd\x01",
            "Bannings from the SSS.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100719V\x07\x05",
            "Oh, so you've called.\x02\x03",
            "#4100720VWere you able to find any\x01",
            "information on Gantz?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100721V\x07\x00",
            "#0003FWell, about that...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained everything that happened to\x01",
            "Mayor Bickson.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100722V\x07\x05",
            "I...am finding it hard to believe that\x01",
            "such a thing has happened.\x02\x03",
            "#4100723VA man like Gantz striking riches from\x01",
            "gambling and living in a luxury hotel?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100724V\x07\x00",
            "#0006FWe tried to reason with him, but he\x01",
            "refuses to return to Mainz.\x02\x03",
            "#4100725V#0000FSo we figured, the least we could do was\x01",
            "report the situation to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100726V\x07\x05",
            "Oh, no, you've done exemplary work.\x02\x03",
            "#4100727VIf this is truly the case, then I shall\x01",
            "make my way to the city tomorrow\x01",
            "and speak with Gantz directly.\x02\x03",
            "#4100728VThank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100729V\x07\x00",
            "#0004FWe're just doing our jobs, sir.\x02\x03",
            "#4100730V#0000FIf we can be of further assistance,\x01",
            "then please don't hesitate to\x01",
            "contact us again.\x02\x03",
            "#4100731VWe'll keep helping if we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100732V\x07\x05",
            "Thank you...\x01",
            "I'll be counting on you all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4100733V#0101F#5PWhat did the mayor say?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#4100734V#6P#0006FWell, he was definitely surprised\x01",
            "about Gantz.\x02\x03",
            "#4100735V#0000FHe said he'd be coming to Crossbell City\x01",
            "tomorrow so he can speak to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100736V#0300F#11PDoubt there's a better man for the job,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100708V#12P#0203F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#4100738V#5P#0005FTio?\x02\x03",
            "#4100739V#0001FYou've been quiet for a while now.\x01",
            "Is something bothering you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3745():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3745)
    Sleep(50)

    def lambda_3755():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3755)

    ChrTalk(
        0x103,
        (
            "#4100740V#12P#0203FNot particularly...\x02\x03",
            "#4100741V#0200FIt was a long day, so I am feeling\x01",
            "a bit fatigued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100742V#5P#0002FNo kidding... Investigating those ruins\x01",
            "earlier took a toll on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100743V#0104F#5PThe sun has already set, so perhaps\x01",
            "we should return home.\x02\x03",
            "#4100744V#0102FKeA's awaiting our return, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4100745V#12P#0204FIndeed she is.\x02\x03",
            "#4100746V#0202FIt is as if my exhaustion is completely\x01",
            "erased when I see her smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100747V#5P#0009FHaha. I don't know if I'd go that far.\x02\x03",
            "#4100748V#0002FI do get what you mean, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100749V#0304F#11PGeez. Talk about a group of\x01",
            "doting parents, eh?\x02\x03",
            "#4100750V#0302FLet's hurry on home and see our\x01",
            "little KeDo!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(68000, 1500, 9000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 68000, 0, 9000, 180)
    SetChrPos(0x1, 68000, 0, 9000, 180)
    SetChrPos(0x2, 68000, 0, 9000, 180)
    SetChrPos(0x3, 68000, 0, 9000, 180)
    SetScenarioFlags(0xC2, 0)
    OP_29(0x4A, 0x1, 0x5)
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_1020 end

    SaveToFile()

Try(main)
