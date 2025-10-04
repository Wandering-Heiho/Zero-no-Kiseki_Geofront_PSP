from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1010.bin",                # FileName
        "c1010",                    # MapName
        "c1010",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1010",                  # 0
        "Receptionist Michel",    # 1
        "Arios",                  # 2
        "Arios",                  # 3
        "Estelle",                # 4
        "Estelle",                # 5
        "Joshua",                 # 6
        "Joshua",                 # 7
        "Bracer Scott",           # 8
        "Bracer Scott",           # 9
        "Bracer Wenzel",          # 10
        "Bracer Lynn",            # 11
        "Bracer Aeolia",          # 12
        "Shizuku",                # 13
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch27200.itc",                   # 04
        "chr/ch27300.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch02402.itc",                   # 07
        "chr/ch00602.itc",                   # 08
        "chr/ch00702.itc",                   # 09
        "chr/ch27202.itc",                   # 0A
        "chr/ch32002.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch27302.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1559,    0,       10220,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(180,     0,       9859,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8430,   150,     49189,   180,  469,  0x0, 0,   9,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-4780,   0,       52229,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8430,   150,     46919,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6320,   0,       52229,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6000,   150,     46930,   0,    469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-5099,   0,       51909,   270,  405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  16, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  37, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_3C4",          # 00, 0
        "Function_1_47C",          # 01, 1
        "Function_2_72E",          # 02, 2
        "Function_3_792",          # 03, 3
        "Function_4_796",          # 04, 4
        "Function_5_36B3",         # 05, 5
        "Function_6_3E06",         # 06, 6
        "Function_7_4BC7",         # 07, 7
        "Function_8_4C62",         # 08, 8
        "Function_9_515E",         # 09, 9
        "Function_10_52FF",        # 0A, 10
        "Function_11_58B4",        # 0B, 11
        "Function_12_5B8C",        # 0C, 12
        "Function_13_6191",        # 0D, 13
        "Function_14_68B3",        # 0E, 14
        "Function_15_716E",        # 0F, 15
        "Function_16_7628",        # 10, 16
        "Function_17_82BC",        # 11, 17
        "Function_18_871D",        # 12, 18
        "Function_19_8B69",        # 13, 19
        "Function_20_925D",        # 14, 20
        "Function_21_9A29",        # 15, 21
        "Function_22_A77C",        # 16, 22
        "Function_23_B2F5",        # 17, 23
        "Function_24_B536",        # 18, 24
        "Function_25_B686",        # 19, 25
        "Function_26_126D8",       # 1A, 26
        "Function_27_1325E",       # 1B, 27
        "Function_28_1482C",       # 1C, 28
        "Function_29_14877",       # 1D, 29
        "Function_30_148D2",       # 1E, 30
        "Function_31_1492D",       # 1F, 31
        "Function_32_18AD8",       # 20, 32
        "Function_33_18AFE",       # 21, 33
        "Function_34_1B8C1",       # 22, 34
        "Function_35_1B916",       # 23, 35
        "Function_36_1B98C",       # 24, 36
        "Function_37_1B9E4",       # 25, 37
    ))


    def Function_0_3C4(): pass

    label("Function_0_3C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_404"),
        (1, "loc_410"),
        (2, "loc_41C"),
        (3, "loc_428"),
        (4, "loc_434"),
        (5, "loc_440"),
        (6, "loc_44C"),
        (SWITCH_DEFAULT, "loc_458"),
    )


    label("loc_404")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_410")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_41C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_428")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_434")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_440")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_464")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_47B")

    Return()

    # Function_0_3C4 end

    def Function_1_47C(): pass

    label("Function_1_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_48A")
    Jump("loc_6DE")

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_498")
    Jump("loc_6DE")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4AB")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_501")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, -6640, 0, 51900, 90)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC")
    SetChrFlags(0x8, 0x10)

    label("loc_4FC")

    Jump("loc_6DE")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50F")
    Jump("loc_6DE")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    Jump("loc_6DE")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_583")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 2220, 0, 4610, 90)
    SetChrPos(0x11, 3840, 0, 4540, 270)
    Jump("loc_6DE")

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D8")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xD)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -6030, 0, 46890, 0)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5960, 150, 49360, 180)
    Jump("loc_6DE")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_601")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 600, 0, 39580, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6DE")

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63A")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_635")
    SetChrFlags(0x8, 0x10)

    label("loc_635")

    Jump("loc_6DE")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_679")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_68C")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F4")
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_708")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_717")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_717")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    Event(0, 21)

    label("loc_72D")

    Return()

    # Function_1_47C end

    def Function_2_72E(): pass

    label("Function_2_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_745")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_761")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_778")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791")
    SetMapObjFrame(0xFF, "red_", 0x2, "on")

    label("loc_791")

    Return()

    # Function_2_72E end

    def Function_3_792(): pass

    label("Function_3_792")

    Call(0, 4)
    Return()

    # Function_3_792 end

    def Function_4_796(): pass

    label("Function_4_796")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8E8")

    ChrTalk(
        0x8,
        (
            "I've assigned members of the guild to search\x01",
            "various locations throughout the state, so you\x01",
            "can leave the rest to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Y'all can go wild investigating those drugs, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And this goes without saying, but you better\x01",
            "take good care of Shizuku!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDon't worry. She's safe with us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_36AF")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(
        0x8,
        (
            "Hey, y'all. How we doin'? You're looking\x01",
            "mighty busy these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your hands all tied up with that mafia\x01",
            "fiasco?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FNo, not exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah? Well, does it have to do with all\x01",
            "these missin' people, then?\x02",
        )
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
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0005FHow'd the guild catch wind of it already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's 'cause Arios has been busting his hump\x01",
            "investigating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sounds like he hasn't had much luck yet.\x01",
            "I reckon the situation is turning out to be\x01",
            "more dire than we were all expectin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'd have to be pretty darn naive to think that\x01",
            "only a person or two have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FNo kiddin'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe would like to partake in an exchange\x01",
            "of information, if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, we'd absolutely love that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you sure it's fine, though? This case goes\x01",
            "beyond the SSS's jurisdiction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0003F(True... We are going off of leads handed to us\x01",
            "by the First Division.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(Dudley would blow a gasket if he found out\x01",
            "we leaked intel to the Bracer Guild.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, just come on back down once\x01",
            "you've finally made your decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll sort through any new info Arios finds\x01",
            "when he returns.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 3)
    Jump("loc_F33")

    label("loc_E22")


    ChrTalk(
        0x8,
        (
            "And speaking of the MacLaines, I'm\x01",
            "pretty sure Shizuku is on her way over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Estelle and Joshua are taking her out\x01",
            "on the town for some funsies while\x01",
            "poor Arios is busy with his investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel bad for Shizuku. I'm whoopin' her\x01",
            "daddy with all this work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F33")

    Jump("loc_36AF")

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_102E")

    ChrTalk(
        0x8,
        (
            "Think we finally got a good idea of the\x01",
            "situation, but I don't think it's about\x01",
            "to break out into a conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This is all beyond my wildest dreams.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Gotta rearrange the schedule to make sure\x01",
            "the team's available 24/7.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AF")

    label("loc_102E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1049")
    Call(0, 5)
    Jump("loc_114F")

    label("loc_1049")


    ChrTalk(
        0x8,
        (
            "There's not a doubt in my mind that Revache\x01",
            "launched that attack on Heiyue's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The real question is, why'd they do something\x01",
            "so unexpected in the public eye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But anyway, I wanna get a full picture of the\x01",
            "situation before we take any action.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114F")

    Jump("loc_36AF")

    label("loc_1154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_17DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1443")

    ChrTalk(
        0x8,
        (
            "Hey, y'all. Haven't seen you 'round these\x01",
            "parts in the last couple of weeks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, we don't have any new intel\x01",
            "on KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FNot even the guild's powerful network of\x01",
            "information was able to produce results?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah... I figured we'd hear a thing or two,\x01",
            "but it's been total silence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FThat's okay. Fortunately, KeA's gotten\x01",
            "accustomed to living with the SSS.\x02\x03",
            "#0000FWe've put more priority on giving her\x01",
            "a normal life than we have prying into\x01",
            "her past, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah? I guess that's one way to do it, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, we'll keep lookin' out for any more\x01",
            "clues in the background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do let us know if you find anythin' out\x01",
            "on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe will. Thank you for assisting us, again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 1)
    Jump("loc_17DA")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(
        0x8,
        (
            "Arios went out on a little trip to the Empire\x01",
            "last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's got some heavy work to deal with,\x01",
            "but I think he'll be back soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FOh, yeah? Something big go down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nothing that major. Just a little 'dispute'\x01",
            "between the army and one of the\x01",
            "branches still operating over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Arios is the only bracer available with enough\x01",
            "authority to handle the issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There was another bracer out in Liberl\x01",
            "perfect for handling issues like this, but\x01",
            "he recently retired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FS-Sounds like you've got your own set of problems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You've got that right, honey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You end up dealing with these kinds of problems\x01",
            "more often as you move up the ranks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17DA")

    label("loc_16FB")


    ChrTalk(
        0x8,
        (
            "The real troublesome part is that we're\x01",
            "in a rocky relationship with the Imperial\x01",
            "government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I've gotta say, we've got it lucky out here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been blessed with the support of\x01",
            "the government and citizenry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DA")

    Jump("loc_36AF")

    label("loc_17DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")

    ChrTalk(
        0x8,
        (
            "I'll give the continent-wide bracer network\x01",
            "a shot to see if I can find out anything\x01",
            "about KeA's identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can get you some basic info within a week,\x01",
            "but it'll take up to a month to get finer details.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1908")

    ChrTalk(
        0x102,
        "#0105FYou're as quick as ever, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1992")

    label("loc_1908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(
        0x103,
        "#0200FYour swiftness never ceases to impress me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1992")

    label("loc_1953")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1992")

    ChrTalk(
        0x104,
        "#0306FYou guys sure know how to haul ass.\x02",
    )

    CloseMessageWindow()

    label("loc_1992")


    ChrTalk(
        0x101,
        "#0000FThanks, I appreciate it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A75")

    label("loc_19BE")


    ChrTalk(
        0x8,
        (
            "The Bracer Guild has its own intelligence\x01",
            "network set up across the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not sure we'll be able to fully ascertain her\x01",
            "identity, but I think we should find clues.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A75")

    Jump("loc_36AF")

    label("loc_1A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5C")

    ChrTalk(
        0x8,
        (
            "Well, if it isn't my fave police officers.\x01",
            "Are y'all heading somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah. We're going to check out the\x01",
            "ruins on Ursula Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You mean Stargazer's Tower?\x01",
            "The CGF should have it barricaded, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've heard reports of some mighty fierce\x01",
            "monsters appearing lately, so you best\x01",
            "prepare those keisters of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe'll be sure to heed your warning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(His sudden pieces of advice never fail\x01",
            "to surprise me.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D86")

    label("loc_1C5C")


    ChrTalk(
        0x8,
        (
            "*sigh* I keep giving in to the temptation of prying into\x01",
            "your lives when you drop by the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is what it is, I suppose. Anyway, make sure you\x01",
            "prepare those keisters if you're going to\x01",
            "Stargazer's Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've heard reports of some mighty fierce\x01",
            "monsters appearing in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D86")

    Jump("loc_36AF")

    label("loc_1D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_211B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(
        0x8,
        (
            "Y'all realize Arc en Ciel's newest show\x01",
            "is debuting soon here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I snatched up those tickets within SECONDS.\x01",
            "I'm totes excited to go watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWhoa. Not exactly an easy feat to get\x01",
            "tickets for that thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FAre you also a fan of Ilya's, Michel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think 'comrade' would be a better\x01",
            "description than fan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can't you see how sexy I am? It should be\x01",
            "a crime to look this good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I sympathize with Ilya's goal of being\x01",
            "the baddest bitch on the block. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "You just going to sit there silently, or are\x01",
            "you going to say something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2116")

    label("loc_2052")


    ChrTalk(
        0x8,
        (
            "Ilya's obviously awesome, but I'm expectin'\x01",
            "a good show from that new chick with the\x01",
            "massive bazongas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm most excited for Theodor and Eugene's\x01",
            "delightfully seductive dance, though. ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")

    Jump("loc_36AF")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_24AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EE")

    ChrTalk(
        0x8,
        (
            "Revache is a criminal organization entrenched\x01",
            "deep within the foundation of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Committing a crime is as commonplace as tying\x01",
            "your shoes for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can't touch 'em, though. They've got their hands\x01",
            "deep in the pockets of the men who run this corrupt\x01",
            "state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The best we could do is give them a hard pounding\x01",
            "if they lay their hands on the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FRight. I think the guild has the upper hand when it\x01",
            "comes to responding to the mafia bothering citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYeah, those bracers already clean up house\x01",
            "by the time we manage to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You've got that right, honey. A little more\x01",
            "ingenuity would go a long way to help\x01",
            "both of our organizations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24A7")

    label("loc_23EE")


    ChrTalk(
        0x8,
        (
            "We're bound by certain rules that won't allow us\x01",
            "to intervene when the government's involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The most we could do is protect the civilians if\x01",
            "they bared their fangs at them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A7")

    Jump("loc_36AF")

    label("loc_24AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_271F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F0")

    ChrTalk(
        0x8,
        (
            "Revache's not even bothering to hide\x01",
            "their movements anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been getting a ton of requests, and\x01",
            "it's all directly related to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Guess when your police force is totally inept,\x01",
            "it makes more sense to come to us, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(I have absolutely no rebuttal at this time.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_271A")

    label("loc_25F0")


    ChrTalk(
        0x8,
        (
            "Oh, right. Estelle and Joshua managed to\x01",
            "make themselves right at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those two busy bees have been working their\x01",
            "bee-hinds off, but they're nowhere near the\x01",
            "bracer Arios is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I had them working up a sweat for me till\x01",
            "late last night. I'm expecting greatness\x01",
            "from the both of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271A")

    Jump("loc_36AF")

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2967")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273A")
    Call(0, 17)
    Jump("loc_2962")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2892")
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0x8,
        (
            "Anyhow, I'm gonna work you like hounds today.\x01",
            "It ain't gonna be easy, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since he's busy outside Crossbell, you're going to\x01",
            "complete Arios' request in his stead. I'm sure\x01",
            "you'll be able to finish it with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thanks for the help, sweeties.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2PYou got it!\x02",
    )


    ChrTalk(
        0xD,
        "#3PUnderstood!\x02",
    )

    OP_57(0x1)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2962")

    label("loc_2892")


    ChrTalk(
        0x8,
        (
            "Let's get this party started with some\x01",
            "supplemental info for the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here's a list of the work you're going to\x01",
            "do this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(They look pretty busy... Maybe we\x01",
            "should leave them alone.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2962")

    Jump("loc_36AF")

    label("loc_2967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7D")

    ChrTalk(
        0x8,
        (
            "The Crossbell Guardian Force has been\x01",
            "making the moves as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Their commander may be super icky, but\x01",
            "they've got a capable deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think we'll just sit back and observe for a while.\x01",
            "See where this all takes us, y'know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B18")

    label("loc_2A7D")


    ChrTalk(
        0x8,
        "Arios is out on a little trip to Calvard right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That bodacious boy is a workaholic to the core.\x01",
            "He needs to learn to relax and take a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B18")

    Jump("loc_36AF")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(
        0x8,
        "Hi, boys. How we doin' today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Didn't know you had enough free time to waltz\x01",
            "into your rivals' headquarters like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you guys are so free, do you wanna take\x01",
            "some work off our hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FNo, that's quite all right. We're actually on\x01",
            "duty right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D07")

    ChrTalk(
        0x101,
        (
            "#0001F(Oh, right. This was the Bracer Guild's\x01",
            "receptionist, Michel.)\x02\x03",
            "#0006F(We met him a little while ago, but I don't think I'll\x01",
            "ever get used to the level of sass he dishes out.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D07")


    ChrTalk(
        0x8,
        "Aw, really? That's too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, I think you should all get goin', now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0005FWait, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FYeah, why's that, pal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Don't mind me. Just talkin' to myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E8D")

    label("loc_2E11")


    ChrTalk(
        0x8,
        (
            "You're on duty, right? Might wanna get\x01",
            "goin', then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep wastin' away in here, and we'll snatch\x01",
            "up all your work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8D")

    Jump("loc_36AF")

    label("loc_2E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_30D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2F46")

    ChrTalk(
        0x8,
        (
            "I hope you guys keep workin' those\x01",
            "rears off as hard as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd love it if y'all grew into a fine team\x01",
            "and didn't get in our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B3")

    label("loc_2F46")


    ChrTalk(
        0x8,
        "Hahaha. Good job with the test, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I've got a decent idea of your\x01",
            "competency from that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FFrom an examination that simple?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's precisely because of its simplicity, little girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you guys keep workin' those\x01",
            "rears off as hard as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd love it if y'all grew into a fine team\x01",
            "and didn't get in our way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_30B3")

    Jump("loc_30CF")

    label("loc_30B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_30CC")
    Call(0, 23)
    Jump("loc_30CF")

    label("loc_30CC")

    Call(0, 22)

    label("loc_30CF")

    Jump("loc_36AF")

    label("loc_30D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_36AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F1")

    ChrTalk(
        0x8,
        "Seriously, though. The Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is it actually true your division was created\x01",
            "due to some internal drama at the CPD?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou've, uh, certainly got your sources\x01",
            "locked down tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, duh! Don't you go looking down\x01",
            "on the power of our connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We get our hands on all sorts of delicious\x01",
            "information from all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For example, we could investigate the whole\x01",
            "lot of 'fine gentlemen' they have in Erebonia,\x01",
            "if you catch my drift.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#0300F(I get that they're informed and all that, but\x01",
            "was that really the best example to try and\x01",
            "flex on us with...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "Anyway, I'm sure we'll be seeing a lot\x01",
            "of each other in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Know that you're always welcome. Actually,\x01",
            "come by again a little later, if you're free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got a lovely idea. It can mark the advent\x01",
            "of our collaboration, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FAn idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FWhat exactly did you have in mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just a little something that'll give me an idea\x01",
            "of how competent you really are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Teehee. Don't worry! It ain't gonna\x01",
            "bite ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303F(Kinda suspicious, don'tcha think?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(On that note, why the flamboyancy?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 6)
    Jump("loc_36AF")

    label("loc_35F1")


    ChrTalk(
        0x8,
        "Definitely drop by the guild later, if you're free.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got a lovely idea. It can mark the advent\x01",
            "of our collaboration, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Teehee. Don't worry! It ain't going to\x01",
            "bite ya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AF")

    TalkEnd(0x8)
    Return()

    # Function_4_796 end

    def Function_5_36B3(): pass

    label("Function_5_36B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A08")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x8,
        "The SSS boys are back again, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1401FSo you've all come. Have you already\x01",
            "heard the news?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FYeah. I assume that means you're already\x01",
            "well aware, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We contacted everybody in the branch already,\x01",
            "so they're gathered on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Gotta prepare ourselves for the possibility of a\x01",
            "war between the two organizations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FIt's just as I feared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FDamn, the police are slackin' compared to\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1403FI don't have much to offer in words, but know that\x01",
            "our procedures are much different from yours.\x02\x03",
            "#1400FWe've got our own way of handling an emergency,\x01",
            "as I'm sure you do, too.\x02\x03",
            "I think you'll be able to handle it if you conduct\x01",
            "yourselves in the usual manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FGood to know. Thanks!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0xCF, 2)
    Jump("loc_3AF0")

    label("loc_3A08")


    ChrTalk(
        0x9,
        (
            "#1403FHeiyue's Cao is an incredibly cunning man.\x02\x03",
            "I doubt he'll take this lying down. He probably\x01",
            "already has something planned for Revache.\x02\x03",
            "#1401FThere's not much we can do about it, other\x01",
            "than to be as prepared as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF0")

    Jump("loc_3E02")

    label("loc_3AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D59")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arios is talking through an old-looking\x01",
            "international communication device.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#1404F#5PIt's been some time, Your Lordship.\x02\x03",
            "Yes, right.\x02\x03",
            "...\x02\x03",
            "#1405FI understand. That does seem like it\x01",
            "poses a problem.\x02\x03",
            "#1404FUnderstood. I'll visit you as soon as I can.\x01",
            "I'm in the middle of an important task\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0012F(I-Is he speaking with royalty right now?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(I thought I heard him say 'Your Highness...'\x01",
            "Do you think he's speaking to the prince\x01",
            "of Remiferia?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E02")

    label("loc_3D59")


    ChrTalk(
        0x9,
        (
            "#1402F#5PYes, I should be able to make it there\x01",
            "by the evening.\x02\x03",
            "#1404FNot at all, Your Highness. The fact that you've\x01",
            "come to me for advice is an honor in itself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E02")

    TalkEnd(0xFE)
    Return()

    # Function_5_36B3 end

    def Function_6_3E06(): pass

    label("Function_6_3E06")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E9A")
    Jump("loc_3EE4")

    label("loc_3E9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EE4")

    label("loc_3EDA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4439")

    ChrTalk(
        0xFE,
        (
            "#1403FOh, you've all come.\x02\x03",
            "#1400FI understand that you've already met with\x01",
            "Heiyue's Cao?\x02",
        )
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
    Sleep(500)

    ChrTalk(
        0x101,
        "#0011FHow do you keep doing that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FWhere did you hear that from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1404FHmph. Information like that will reach our ears\x01",
            "within minutes.\x02\x03",
            "#1400FFrom what I gathered, Heiyue doesn't plan on\x01",
            "exacting their revenge quite yet, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYeah, that sounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FStill doesn't change the fact that we're on\x01",
            "the verge of a messy situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FWe cannot discount the possibility of their\x01",
            "main headquarters intervening, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1403FIt's true that Heiyue is a massive crime\x01",
            "syndicate wholly responsible for\x01",
            "controlling Calvard's underworld.\x02\x03",
            "#1400FHowever, they've split their organization\x01",
            "into numerous smaller units, so they're\x01",
            "essentially divided.\x02\x03",
            "Cao may be able to prevent them from\x01",
            "retaliating prematurely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FThat makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou're surprisingly well informed on\x01",
            "their affairs, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1404FI find myself traveling to the Republic on\x01",
            "work-related business frequently.\x02\x03",
            "Yin may be dangerous, but I don't believe\x01",
            "them to be a ruthless murderer of the\x01",
            "innocent.\x02\x03",
            "#1401FI'm far more worried about Revache,\x01",
            "quite frankly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 4)
    Jump("loc_4521")

    label("loc_4439")


    ChrTalk(
        0xFE,
        (
            "#1403FRevache is a cunning organization. To see them\x01",
            "act this boldly comes as a bit of a surprise.\x02\x03",
            "I believe Garcia's foothold in the ranks\x01",
            "may be slipping.\x02\x03",
            "#1401FI suspect something deeper may be\x01",
            "going on behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4521")

    Jump("loc_4BBF")

    label("loc_4526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_48F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4780")

    ChrTalk(
        0xFE,
        (
            "#1400FYou're here again.\x02\x03",
            "#1404FHas it been a month already? I can tell\x01",
            "you've grown a little bit since last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FHaha. It's good to see you again, Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FI don't think we're sizin' up at all to the great\x01",
            "Divine Blade of Wind, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1404FThere's no need to feel ashamed. Continue\x01",
            "down the path you've chosen, and you'll\x01",
            "grow immeasurably.\x02\x03",
            "#1402FTake a hard look at the current state of Crossbell.\x01",
            "I'm sure, one day, your time to shine will come.\x01",
            "When it does, your presence will be invaluable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FI-If you say so, sir...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 4)
    Jump("loc_48F4")

    label("loc_4780")


    ChrTalk(
        0xFE,
        (
            "#1404FWhatever you're doing seems to be working.\x01",
            "Continue to devote yourselves to growing.\x02\x03",
            "#1402FI'm looking forward to seeing what kind of\x01",
            "fine, upstanding police officers you\x01",
            "grow into.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F1")

    ChrTalk(
        0x101,
        (
            "#0012F(Is he messing with us, or is he\x01",
            "overly optimistic?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(I can't help but feel that he may be overestimating\x01",
            "our capabilities just a little bit.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F1")

    SetScenarioFlags(0x0, 1)

    label("loc_48F4")

    Jump("loc_4BBF")

    label("loc_48F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0D")

    ChrTalk(
        0xFE,
        "#1405FIt's good to see you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FHello again, Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FIt's been quite some time, hasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1404FHuh...\x01",
            "Why all the tension? You can relax around me.\x02\x03",
            "#1402FYou did a fine job handling the downtown incident.\x02\x03",
            "You were able to resolve the matter before we\x01",
            "were forced to intervene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FOh, no. I don't think it was that big of a deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(I bet he woulda settled the whole thing\x01",
            "with a single swing of his blade.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Are we being puppeteered by him?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 3)
    Jump("loc_4BBF")

    label("loc_4B0D")


    ChrTalk(
        0xFE,
        (
            "#1404FNow, if you'll excuse me. I'd better\x01",
            "take my leave.\x02\x03",
            "#1402FHaha. I've had a bit more free time ever since\x01",
            "those two arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F...?\x01",
            "(Who's he talking about?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BBF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_3E06 end

    def Function_7_4BC7(): pass

    label("Function_7_4BC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE5")
    Call(0, 17)
    Jump("loc_4C5E")

    label("loc_4BE5")


    ChrTalk(
        0xB,
        (
            "#0800FYou guys look pretty busy yourselves.\x02\x03",
            "#0809FI'm sure we'll bump into each other\x01",
            "again. Catch you guys later!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C5E")

    TalkEnd(0xFE)
    Return()

    # Function_7_4BC7 end

    def Function_8_4C62(): pass

    label("Function_8_4C62")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CF6")
    Jump("loc_4D40")

    label("loc_4CF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D16")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D40")

    label("loc_4D16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D40")

    label("loc_4D36")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D40")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D80")
    Call(0, 18)
    Jump("loc_4EA4")

    label("loc_4D80")


    ChrTalk(
        0xC,
        (
            "#0806FMaaaaan... I wanted to scope out some\x01",
            "details on the mafia, too.\x02\x03",
            "Those jerks barred us, though! There's apparently\x01",
            "some kinda agreement that lets the police take\x01",
            "precedence in times like this.\x02\x03",
            "#0800FSo on that note...you guys are going to do\x01",
            "the snooping for us, right?! Right?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA4")

    Jump("loc_5156")

    label("loc_4EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5055")

    ChrTalk(
        0x153,
        (
            "#1106FI'm sorry about earlier, Estelle.\x02\x03",
            "#1108FI promise I don't hate you, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0809FEheheheh. Don't worry about it, kiddo.\x01",
            "I'm totally fine!\x02\x03",
            "#0802FDon't be afraid to ask your big sis for help\x01",
            "if you get into trouble, okay?\x02\x03",
            "I'll be there in a jiffy to swoop in and\x01",
            "save the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FThanks, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FYeah, we'll be sure to rely on your assistance\x01",
            "when the need arises.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5156")

    label("loc_5055")


    ChrTalk(
        0xC,
        (
            "#0806F*sigh* Does everybody hate me or something?\x01",
            "Why do I keep getting rejected?!\x02\x03",
            "#0808FNot only that, but we didn't even get to meet up\x01",
            "with Kilika during the festival. What the heck!\x02\x03",
            "#0805FI gotta wonder why she came all the way\x01",
            "out here, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5156")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_4C62 end

    def Function_9_515E(): pass

    label("Function_9_515E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_52FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517C")
    Call(0, 17)
    Jump("loc_52FB")

    label("loc_517C")


    ChrTalk(
        0xD,
        (
            "#0900FWe'll be heading towards Armorica\x01",
            "while we fulfill our requests today.\x02\x03",
            "#0904FWe're still not fully familiar with the area\x01",
            "surrounding Crossbell City, so I figured\x01",
            "it'd be a good opportunity to solve that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F8")

    ChrTalk(
        0x101,
        (
            "#0003FYeah, that's a pretty good idea.\x02\x03",
            "#0000FI don't think you'll have any problems with\x01",
            "monsters, but be safe out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#0902FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_52F8")

    SetScenarioFlags(0x0, 3)

    label("loc_52FB")

    TalkEnd(0xFE)
    Return()

    # Function_9_515E end

    def Function_10_52FF(): pass

    label("Function_10_52FF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5393")
    Jump("loc_53DD")

    label("loc_5393")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_53B3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53DD")

    label("loc_53B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53D3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53DD")

    label("loc_53D3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53DD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541D")
    Call(0, 18)
    Jump("loc_550E")

    label("loc_541D")


    ChrTalk(
        0xE,
        (
            "#0901FI thought I had a solid grasp on the\x01",
            "situation in Crossbell...\x02\x03",
            "But when a situation like this occurs, it feels\x01",
            "like there's a huge barrier to overcome.\x02\x03",
            "#0903FFortunately, I think we were able to accurately\x01",
            "assess the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550E")

    Jump("loc_58AC")

    label("loc_5513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_57BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56FE")

    ChrTalk(
        0xE,
        (
            "#0905FYou weren't able to find any information\x01",
            "at the cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FYeah, here's what happened...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd described the events that transpired during\x01",
            "the sister's examination of KeA at the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        (
            "#0903FHuh. I see...\x02\x03",
            "#0900FYeah, there really is no choice but to rely on\x01",
            "St. Ursula in a situation like this.\x02\x03",
            "I heard they've adopted a new method of\x01",
            "treatment called neurology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FYep. We're going to try paying them a visit.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57B9")

    label("loc_56FE")


    ChrTalk(
        0xE,
        (
            "#0903FI don't think you have much of a choice but to rely\x01",
            "on St. Ursula Medical College in this situation.\x02\x03",
            "#0900FI heard they've adopted a new method of\x01",
            "treatment called neurology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B9")

    Jump("loc_58AC")

    label("loc_57BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_58AC")

    ChrTalk(
        0xE,
        (
            "#0904FThe Septian Church has passed down techniques\x01",
            "to heal the body and mind since ancient times.\x02\x03",
            "#0900FThey might have some kind of clues about\x01",
            "how to restore KeA's memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe'll be sure to pay them a visit.\x02",
    )

    CloseMessageWindow()

    label("loc_58AC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_52FF end

    def Function_11_58B4(): pass

    label("Function_11_58B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A29")

    ChrTalk(
        0xFE,
        (
            "I hope Pearl is handling her duties as the\x01",
            "Times' receptionist well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FAre you two acquainted?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, she's actually my betrothed. We've\x01",
            "been too busy to make the time to see\x01",
            "each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops. Amateur move of me to divulge\x01",
            "my personal life in a professional setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll get back to focusing on my work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5AC9")

    label("loc_5A29")


    ChrTalk(
        0xFE,
        (
            "Make sure you keep your private and professional\x01",
            "lives separate, or you'll end up neglecting them both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll get back to focusing on my work.\x02",
    )

    CloseMessageWindow()

    label("loc_5AC9")

    Jump("loc_5B88")

    label("loc_5ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5ADC")
    Jump("loc_5B88")

    label("loc_5ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF7")
    Call(0, 19)
    Jump("loc_5B88")

    label("loc_5AF7")


    ChrTalk(
        0xFE,
        (
            "I've got a couple of requests to handle\x01",
            "out in Armorica Village this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's going to be a long day, so I'd\x01",
            "better get going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B88")

    TalkEnd(0xFE)
    Return()

    # Function_11_58B4 end

    def Function_12_5B8C(): pass

    label("Function_12_5B8C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C20")
    Jump("loc_5C6A")

    label("loc_5C20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C40")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C6A")

    label("loc_5C40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C6A")

    label("loc_5C60")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C6A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAA")
    Call(0, 18)
    Jump("loc_5D74")

    label("loc_5CAA")


    ChrTalk(
        0xFE,
        (
            "We should get a full search of the mafia's\x01",
            "compound going for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all the connections they have for smuggling\x01",
            "heavy weaponry into the city, they could start a\x01",
            "huge gunfight at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D74")

    Jump("loc_6189")

    label("loc_5D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6071")
    SetChrSubChip(0x11, 0x0)

    ChrTalk(
        0x10,
        (
            "Have you guys heard about the raids on the\x01",
            "Bracer Guild that happened in the Empire\x01",
            "about two years ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Wenzel was in the Empire at the time, so he was\x01",
            "able to help resolve the conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FI do remember it. There was quite the uproar\x01",
            "over the incident.\x02\x03",
            "#0103FMany of the guild's branches were destroyed\x01",
            "by a series of terrorist attacks carried out by\x01",
            "jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FCan't say I'm too surprised that you were able to\x01",
            "help resolve such an enormous conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "What are you talking about? I didn't do much at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It was all thanks to the brilliant strategic abilities\x01",
            "of the high-ranking bracers that came to assist\x01",
            "the guild with the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "My role just happened to be in the spotlight.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6189")

    label("loc_6071")

    SetChrSubChip(0x10, 0x0)

    ChrTalk(
        0x11,
        (
            "More importantly, Scott...\x01",
            "Have you been visiting your fiancee lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I haven't had the time. Not much I can\x01",
            "do about it with a career like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Our wedding isn't for a while, anyway. I'll have\x01",
            "plenty of opportunities to make up for my\x01",
            "absence in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6189")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_5B8C end

    def Function_13_6191(): pass

    label("Function_13_6191")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6304")
    OP_4B(0x11, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x11,
        (
            "I'd like you to focus on protecting the injured\x01",
            "if an emergency happens, Aeolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I know. I've got my role locked down\x01",
            "tight already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Ideally, I'd prefer to search for a way to\x01",
            "peacefully resolve this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yeah, likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We'll have to prioritize gathering intelligence\x01",
            "in order to pull it off.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_63A6")

    label("loc_6304")


    ChrTalk(
        0xFE,
        (
            "I won't let civilians get caught up in some\x01",
            "idiotic spat because of the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll have to prioritize gathering intelligence\x01",
            "in order to pull it off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A6")

    Jump("loc_68AF")

    label("loc_63AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_65AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_652C")

    ChrTalk(
        0xFE,
        (
            "Those First Division detectives have been\x01",
            "on the move since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't like 'em one bit. They remind me of\x01",
            "the Empire's MP divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(MP? Is he referring to military police?)\x02\x03",
            "#0003F(The Imperial Army acts in secrecy, so we don't\x01",
            "know much of its military police. I'm sure their\x01",
            "structure closely resembles the CPD, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65AA")

    label("loc_652C")


    ChrTalk(
        0xFE,
        (
            "I have too many bad memories of\x01",
            "the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't like how the First Division operates\x01",
            "in secrecy, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65AA")

    Jump("loc_68AF")

    label("loc_65AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_67FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65CA")
    Call(0, 12)
    Jump("loc_67F5")

    label("loc_65CA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_665E")
    Jump("loc_66A8")

    label("loc_665E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_667E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66A8")

    label("loc_667E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_669E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66A8")

    label("loc_669E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66A8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x11,
        (
            "The Imperial government's been trying their\x01",
            "damnedest to decrease the guild's influence\x01",
            "out there ever since the whole thing went down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm just lucky that the Crossbell branch managed\x01",
            "to drag me outta that sticky situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Actually, forget it. I'm just mouthing\x01",
            "off again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_67F5")

    Jump("loc_68AF")

    label("loc_67FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_68AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6815")
    Call(0, 19)
    Jump("loc_68AF")

    label("loc_6815")


    ChrTalk(
        0xFE,
        (
            "Some promising up-and-comers are going to\x01",
            "transfer to the Crossbell branch soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll do what I can to not give them\x01",
            "the cold shoulder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AF")

    TalkEnd(0xFE)
    Return()

    # Function_13_6191 end

    def Function_14_68B3(): pass

    label("Function_14_68B3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6947")
    Jump("loc_6991")

    label("loc_6947")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6967")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6991")

    label("loc_6967")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6987")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6991")

    label("loc_6987")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6991")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D1")
    Call(0, 18)
    Jump("loc_6C0F")

    label("loc_69D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B87")

    ChrTalk(
        0xFE,
        (
            "We've got the Divine Blade of Wind himself,\x01",
            "the young heroes of Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...an expert marksman, a hard-ass refugee\x01",
            "from the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...a physician, and last but not least, a\x01",
            "specialist in the Taito school of martial\x01",
            "arts. That's me, obviously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though we're totally stacked with\x01",
            "highly-capable bracers, we still need to\x01",
            "exercise caution while working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd recommend you follow suit.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C0F")

    label("loc_6B87")


    ChrTalk(
        0xFE,
        (
            "Even with the Divine Blade of Wind at the helm,\x01",
            "we should be cautious when handling incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd recommend you follow suit.\x02",
    )

    CloseMessageWindow()

    label("loc_6C0F")

    Jump("loc_7166")

    label("loc_6C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DDF")

    ChrTalk(
        0xFE,
        "Hey, rookies. How are you doing?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8F")

    ChrTalk(
        0x101,
        "#0000F(I believe her name was...Lynn, right?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CBF")

    label("loc_6C8F")


    ChrTalk(
        0x101,
        "#0000FWe're doing good. Thanks for asking.\x02",
    )

    CloseMessageWindow()

    label("loc_6CBF")


    ChrTalk(
        0x102,
        (
            "#0100FIt's pretty rare to see you around. Are you\x01",
            "staying put today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yep! I just got back yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I complained to Michel about all of the jobs\x01",
            "he's been sending me on, so I think I'll be\x01",
            "okay for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FSounds like he has you runnin' around like a dog.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7081")

    label("loc_6DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6FC1")

    ChrTalk(
        0xFE,
        (
            "Hey, Tio. Sorry about Aeolia always going\x01",
            "bonkers around you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FI do not particularly mind. However,\x01",
            "her logic is perplexing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear you. I'm her partner, yet I can't figure out\x01",
            "what she's thinking half the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were you, I'd just abandon hope and resign\x01",
            "to being her plaything.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0003F(I'm sure there's a different solution to this.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7081")

    label("loc_6FC1")


    ChrTalk(
        0xFE,
        (
            "Aeolia's special abilities leave her in high demand\x01",
            "across the entire continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She usually has to take trips to help people, which\x01",
            "can make it a little annoying to be her partner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7081")

    Jump("loc_7166")

    label("loc_7086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A1")
    Call(0, 20)
    Jump("loc_7166")

    label("loc_70A1")


    ChrTalk(
        0xFE,
        (
            "Let's pretend you didn't hear that last part, shall we?\x01",
            "Anyway, try to keep the tomfoolery to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't beat yourself up too badly, either, 'cause\x01",
            "you have some catching up to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7166")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_68B3 end

    def Function_15_716E(): pass

    label("Function_15_716E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718C")
    Call(0, 13)
    Jump("loc_721B")

    label("loc_718C")


    ChrTalk(
        0xFE,
        (
            "I may be a licensed physician, but I'd be\x01",
            "happier if I had less work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it'd mean that fewer people are\x01",
            "getting hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_721B")

    Jump("loc_7624")

    label("loc_7220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_754A")
    TurnDirection(0x13, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7492")

    ChrTalk(
        0xFE,
        "I'm so happy to see you again, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gosh, you're such a cutie! I can never get\x01",
            "enough of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can I hug you? Pleaaaaase?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FHelp...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7367")

    ChrTalk(
        0x101,
        (
            "#0000F(Aeolia's mind totally breaks whenever she sees\x01",
            "Tio. I don't know how many times we've gone\x01",
            "through this scenario now.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73A8")

    label("loc_7367")


    ChrTalk(
        0x101,
        (
            "#0000F(Aeolia's mind totally breaks whenever she\x01",
            "sees Tio.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A8")


    ChrTalk(
        0x104,
        (
            "#0303F(Man, a smokin' hot foreigner like her\x01",
            "is totally my type, too...)\x02\x03",
            "#0301F(Not much I can do about it. She's totally smitten\x01",
            "with Tio Tot. I'll forgive you just this once!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206F(...What am I supposed to do?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7545")

    label("loc_7492")


    ChrTalk(
        0xFE,
        (
            "C'mere, Tio! I'm going to give you a\x01",
            "biiiiiiiig hug!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0000F(She's really drowning her in affection...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206F(What am I supposed to do?)\x02",
    )

    CloseMessageWindow()

    label("loc_7545")

    Jump("loc_7624")

    label("loc_754A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7565")
    Call(0, 20)
    Jump("loc_7624")

    label("loc_7565")


    ChrTalk(
        0xFE,
        (
            "Hahaha. I just got back from a job,\x01",
            "so I'm not going anywhere.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    ChrTalk(
        0xFE,
        (
            "C'mere, Tio! I'm going to make you\x01",
            "give me a hug! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Status confirmed. She is a formidable enemy.)\x02",
    )

    CloseMessageWindow()

    label("loc_7624")

    TalkEnd(0xFE)
    Return()

    # Function_15_716E end

    def Function_16_7628(): pass

    label("Function_16_7628")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bracers' shift schedule is posted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7750")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Mainz\x01",
            "Scott: Bellguard Gate\x01",
            "Wenzel: Bellguard Gate\x01",
            "Lynn: Tangram Gate\x01",
            "Aeolia: Tangram Gate\x01",
            "Estelle: Armorica\x01",
            "Joshua: Armorica\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_786B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: City Patrol\x01",
            "Scott: Bellguard Gate\x01",
            "Wenzel: Bellguard Gate\x01",
            "Lynn: Downtown District\x01",
            "Aeolia: Downtown District\x01",
            "Estelle: Private Business (East Street)\x01",
            "Joshua: Private Business (East Street)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_786B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_799C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: City Patrol\x01",
            "Scott: Bellguard Gate\x01",
            "Wenzel: Bellguard Gate\x01",
            "Lynn: Downtown District\x01",
            "Aeolia: Downtown District\x01",
            "Estelle: Private Business (Entertainment District)\x01",
            "Joshua: Private Business (Entertainment District)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_799C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_7A8F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Standby\x01",
            "Scott: Back Alley\x01",
            "Wenzel: Back Alley\x01",
            "Lynn: Crossbell Station\x01",
            "Aeolia: Crossbell Station\x01",
            "Estelle: Resting (Acacia)\x01",
            "Joshua: Resting (Acacia)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B56")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Standby\x01",
            "Scott: Standby\x01",
            "Wenzel: Standby\x01",
            "Lynn: Standby\x01",
            "Aeolia: Standby\x01",
            "Estelle: Standby\x01",
            "Joshua: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7C6A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Erebonia\x01",
            "Scott: Downtown District\x01",
            "Wenzel: Downtown District\x01",
            "Lynn: St. Ursula Medical College\x01",
            "Aeolia: St. Ursula Medical College\x01",
            "Estelle: Armorica Village\x01",
            "Joshua: Armorica Village\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7D51")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: City Perimeter Patrol\x01",
            "Scott: Resting\x01",
            "Wenzel: City Perimeter Patrol\x01",
            "Lynn: Remiferia\x01",
            "Aeolia: Remiferia\x01",
            "Estelle: Standby\x01",
            "Joshua: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7E20")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Remiferia\x01",
            "Scott: Standby\x01",
            "Wenzel: Standby\x01",
            "Lynn: Tangram Gate\x01",
            "Aeolia: Tangram Gate\x01",
            "Estelle: Mainz\x01",
            "Joshua: Mainz\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7F17")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Standby\x01",
            "Scott: Mainz\x01",
            "Wenzel: Mainz\x01",
            "Lynn: St. Ursula Medical College\x01",
            "Aeolia: St. Ursula Medical College\x01",
            "Estelle: Bellguard Gate\x01",
            "Joshua: Bellguard Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_7F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8012")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Standby\x01",
            "Scott: Mainz\x01",
            "Wenzel: Mainz\x01",
            "Lynn: St. Ursula Medical College\x01",
            "Aeolia: St. Ursula Medical College\x01",
            "Estelle: Resting (Acacia)\x01",
            "Joshua: Resting (Acacia)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_8012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_80F7")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Calvard\x01",
            "Scott: Erebonia\x01",
            "Wenzel: Erebonia\x01",
            "Lynn: City Perimeter Patrol\x01",
            "Aeolia: City Perimeter Patrol\x01",
            "Estelle: Standby\x01",
            "Joshua: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_80F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_813F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Currently rescheduling...\x01",
            "         Please wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_813F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8202")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Erebonia\x01",
            "Scott: City Perimeter Patrol\x01",
            "Wenzel: City Perimeter Patrol\x01",
            "Lynn: Standby\x01",
            "Aeolia: Standby\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A5")

    label("loc_8202")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Erebonia\x01",
            "Scott: Standby\x01",
            "Wenzel: Standby\x01",
            "Lynn: State Patrol\x01",
            "Aeolia: State Patrol\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_82A5")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_7628 end

    def Function_17_82BC(): pass

    label("Function_17_82BC")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(810, 1300, 9650, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, 1520, 0, 8250, 0)
    SetChrPos(0x102, 340, 0, 8029, 0)
    SetChrPos(0x103, 1520, 0, 6890, 0)
    SetChrPos(0x104, 340, 0, 6640, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8383():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8383)
    Sleep(50)

    def lambda_8393():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8393)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xB,
        (
            "#0805FOh, hey. I remember you guys...\x02\x03",
            "#0809FHowdy, Special Support Section!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0012FH-Hi there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204FThank you for your assistance yesterday.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, I think I see what happened.\x01",
            "Hey, Estelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8522():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8522)
    Sleep(100)

    def lambda_8532():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8532)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xB,
        "#0805FHmm? What's up, Michel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Eh, forget it. It's nothing.\x01",
            "Let's just get back to our little powwow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#0800FO...kay?\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)

    ChrTalk(
        0xD,
        (
            "#0906FWell, now you know it wasn't a fluke.\x01",
            "Estelle is like this everyday.\x02\x03",
            "#0900FI hope we haven't been too overbearing.\x01",
            "I meant what I said about us being friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FNot at all, and I'd like that, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0104FWe look forward to working with you.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1000, 0, 8250, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6D, 2)
    EventEnd(0x5)
    Return()

    # Function_17_82BC end

    def Function_18_871D(): pass

    label("Function_18_871D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5920, 1300, 48320, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -3550, 0, 48770, 270)
    SetChrPos(0x102, -3440, 0, 47510, 270)
    SetChrPos(0x103, -2420, 0, 48770, 270)
    SetChrPos(0x104, -2320, 0, 47490, 270)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xE, 0x1)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x12, 0x2)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#0801F#1POh, you guys came! You hear about\x01",
            "the big news about Heiyue already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F#11PYeah. We've already started conducting\x01",
            "our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F#11PActually, I just noticed... Haven't all of the\x01",
            "bracers gathered here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F#11PI see the Divine Blade of Wind is downstairs.\x01",
            "He is truly a sight to behold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0904F#1PHaha, yeah... They contacted all of us\x01",
            "on our Enigmas this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#6PAnd that's why we've all gathered here\x01",
            "on such short notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F#11PDamn. You guys are way too coordinated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#6PAre you sure you're not just a bunch\x01",
            "of slackers?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(200)

    ChrTalk(
        0x12,
        (
            "#12PBut anyway, Revache sure left one heck of\x01",
            "a mess for us to clean up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "#0803F#5PYou said it, sister! Sure, there might be less\x01",
            "people there at night, but civilians still could\x01",
            "have gotten caught up in their mess!\x02\x03",
            "#0801FI'm so pissed at the mafia! I can't wait to\x01",
            "rearrange their faces with my staff!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3420, 0, 48200, 270)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0xCF, 7)
    EventEnd(0x5)
    Return()

    # Function_18_871D end

    def Function_19_8B69(): pass

    label("Function_19_8B69")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(-4610, 1000, 51100, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, -3630, 0, 50910, 315)
    SetChrPos(0x102, -4250, 0, 49980, 315)
    SetChrPos(0x103, -2650, 0, 50000, 315)
    SetChrPos(0x104, -3250, 0, 48910, 315)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#11PMan, Arios is out on another business trip.\x01",
            "Guy can't seem to catch a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWho am I to talk, though? We're about\x01",
            "to get dispatched ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PLynn and Aeolia should be back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PMichel sure loves working us\x01",
            "to the bone, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PThe man's a slave driver. I'm surprised he\x01",
            "doesn't brandish a whip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FPardon us. Are you all bracers?\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8DD0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8DD0)

    def lambda_8DDD():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DDD)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)

    ChrTalk(
        0xF,
        "#5POh, I recognize you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYou're those officers from\x01",
            "the SSS, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FYou are correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0304FFigured it out in an instant, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PYeah, 'cause you guys are brimming with immaturity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PDo a bunch of guys as inexperienced as yourselves\x01",
            "REALLY plan on working in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#12P#0106F(It's frustrating to hear insults, but I can't\x01",
            "deny his reservations.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FRegardless of how you feel about us,\x01",
            "we intend to do what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHow naive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PDo you seriously think you'd ever grow\x01",
            "if you never push beyond your limits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FUgh...\x01",
            "(Wow, he's harsh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PHaha. Well, despite our onslaught just now,\x01",
            "I'll be personally cheering for you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PIf the police showed a bit more competency, we\x01",
            "wouldn't be working so damn hard all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYou actually give us even more work by making\x01",
            "us clean up after you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FS-Sorry... We'll work on fixing that.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -3630, 0, 50910, 315)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x4F, 7)
    EventEnd(0x5)
    Return()

    # Function_19_8B69 end

    def Function_20_925D(): pass

    label("Function_20_925D")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x13, 0xFF)
    OP_68(-4460, 1300, 41900, 0)
    MoveCamera(17, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20100, 0)
    SetChrPos(0x101, -3430, 0, 42620, 270)
    SetChrPos(0x103, -3440, 0, 41360, 270)
    SetChrPos(0x102, -2320, 0, 42620, 270)
    SetChrPos(0x104, -2320, 0, 41360, 270)
    TurnDirection(0x13, 0x103, 0)
    SetChrSubChip(0x12, 0x1)
    OP_0D()

    ChrTalk(
        0x12,
        "#5POh, I think I know you guys...\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#5PAaaaah! You're SO cute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0205FI beg your pardon? Are you referring\x01",
            "to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PWell, obviously!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PThat refined and mature aura...combined with\x01",
            "those large, childlike eyes being contrasted by\x01",
            "your tiny, luscious lips...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PI...I can't take this anymore!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        (
            "#11PWhat the hell am I supposed to do, Lynn?!\x01",
            "Can I take her home? CAN I?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0211F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PYour creepy habits keep scaring away\x01",
            "the kids whenever you first meet them,\x01",
            "Aeolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PWe JUST got back from a job, so I think\x01",
            "you should dial it back a bit, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0302FHey, forget about her. You can take me\x01",
            "home any day of the week, baby.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    ChrTalk(
        0x13,
        "#5PYeah, no. You get a hard pass from me. ㈱\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        "#11P#0306FDamn. Didn't stand a chance, did I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FW-Well, I'm certainly surprised from the stark\x01",
            "contrast between your graceful appearance\x01",
            "and your vivid personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FAre you two affiliated with the guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PIndeed. And might you all be with the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0005FSo you've heard of us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PYeah, Michel gave us the heads-up already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PHaha, you guys are pathetic. How's it feel to\x01",
            "get saved by Arios on your first mission?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5PDoesn't look like we can rely on the police quite yet.\x01",
            "You've still got a long road ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PI'm not surprised that a bunch of hacks work\x01",
            "like, well, a bunch of hacks.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x102,
        "#11P#0106F(That was awfully rude, wasn't it?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FWe'll...keep that in mind.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3430, 0, 42620, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x50, 0)
    EventEnd(0x5)
    Return()

    # Function_20_925D end

    def Function_21_9A29(): pass

    label("Function_21_9A29")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7120, 1300, 4730, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1750, 0, 2150, 0)
    SetChrPos(0x102, -2750, 0, 1900, 0)
    SetChrPos(0x103, -1750, 0, 650, 0)
    SetChrPos(0x104, -2750, 0, 400, 0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(950, 1300, 11510, 5000)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-2160, 1300, 4030, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0000FSo this building belongs to the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0203FIndeed. They are an international non-\x01",
            "governmental organization serving to\x01",
            "keep the peace and protect civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FIn other words, they're the continent's favorite\x01",
            "allies of justice...and our competitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FThough, I suppose we should technically\x01",
            "be collaborating with them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)

    ChrTalk(
        0x8,
        "#6POh, my. Welcome to the Bracer Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PAre you those new SSS folks I've\x01",
            "been hearin' about all over?\x02",
        )
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
        "#11P#0005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0105FMay I ask how you know of us?\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1300, 10500, 5000)
    MoveCamera(45, 26, 0, 5000)
    SetCameraDistance(21750, 5000)

    def lambda_9E2C():
        OP_96(0xFE, 0x5DC, 0x0, 0x27A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E2C)
    Sleep(50)

    def lambda_9E49():
        OP_96(0xFE, 0x1F4, 0x0, 0x26AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E49)
    Sleep(50)

    def lambda_9E66():
        OP_96(0xFE, 0x5DC, 0x0, 0x21CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E66)
    Sleep(50)

    def lambda_9E83():
        OP_96(0xFE, 0x1F4, 0x0, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E83)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    def lambda_9EAB():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9EAB)
    WaitChrThread(0x102, 1)

    def lambda_9EBC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EBC)
    WaitChrThread(0x103, 1)

    def lambda_9ECD():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9ECD)
    WaitChrThread(0x104, 1)

    def lambda_9EDE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9EDE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FIt's nice to meet you. I'm Lloyd Bannings\x01",
            "with the CPD's Special Support Section.\x02\x03",
            "#0005FAnd you would be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI'm Michel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI serve as the Bracer Guild's receptionist\x01",
            "out here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI heard about you guys from Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FOh, I guess that makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FStill, I was surprised to see you recognize\x01",
            "us immediately upon entry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHaha. I figured it out by them badges pinned\x01",
            "to your chests. Your faces scream 'Freeze!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHey, so I figure our mission statements\x01",
            "are pretty similar, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FI-I suppose so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203FI cannot deny that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FI'm guessin' you guys aren't too amused\x01",
            "about the situation, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, silly you! We totally don't mind at all.\x01",
            "In fact, we welcome you with open arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe're always drowning in requests, and our\x01",
            "bracers already have their hands tied down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou'd be doing us a huge favor by taking on\x01",
            "some of these requests, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004FI see. It's a bit of a relief to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDon't get ahead of yourselves, though.\x01",
            "You haven't done squat to prove\x01",
            "yourselves as reliable allies...yet.\x02",
        )
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
        "#12P#0001FOuch. Not pulling any punches, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI know I'm being a tad too harsh, but we seriously\x01",
            "have some of the best bracers Zemuria has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's not just Arios, either. All of our other members\x01",
            "are damn skilled and are respected by the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI get they established the SSS to help\x01",
            "regain public trust with the CPD, but all\x01",
            "of its members are total newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhether you're competent or not remains\x01",
            "to be seen, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FW-Well, when you put it that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0108F(There's no arguing that.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0303F(Bit of a hard-ass, don'tcha think?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHaha. I'll relax with the bullying now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PY'all should just do what you can\x01",
            "and keep working at improving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDon't be afraid to fall and scrape your knees,\x01",
            "'cause we've got your backs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FThanks. We'll do everything we can to\x01",
            "make your lives easier.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1000, 0, 10150, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x47, 2)
    EventEnd(0x5)
    Return()

    # Function_21_9A29 end

    def Function_22_A77C(): pass

    label("Function_22_A77C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_END)), "loc_AA64")

    ChrTalk(
        0x101,
        (
            "#11P#0005FExcuse me, Michel? We came back\x01",
            "like you asked us to.\x02\x03",
            "#0000FSo, what did you want to show us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI've been waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHow cute of you to come running like a\x01",
            "group of puppies when I call for you.\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#0003FAhem. Well, uh, if I recall correctly...\x02\x03",
            "#0000F...you mentioned you had some kind of\x01",
            "plan to measure our competency, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYou sure did recall correctly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf y'all are feeling up to the challenge,\x01",
            "do you wanna try taking a little test?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE4E")

    label("loc_AA64")


    ChrTalk(
        0x8,
        "#5PSeriously, though. The Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIs it actually true your division was created\x01",
            "due to some internal drama at the CPD?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FYou've, uh, certainly got your sources\x01",
            "locked down tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, duh! Don't you go looking down\x01",
            "on the power of our connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe get our hands on all sorts of delicious\x01",
            "information from all over the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFor example, we could investigate the whole\x01",
            "lot of 'fine gentlemen' they have in Erebonia,\x01",
            "if you catch my drift.\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#0303F(I get that they're informed and all that, but\x01",
            "was that really the best example to try and\x01",
            "flex on us with...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200F(On that note, why the flamboyancy?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5PAnyway, since I'm sure we'll be bumping into\x01",
            "each other plenty in the future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...I've got a fun little idea for us. Any interest\x01",
            "in taking a small test I've put together?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE4E")

    SetScenarioFlags(0x4F, 6)

    ChrTalk(
        0x101,
        "#11P#0005FA test?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FWhat kind of test, if you don't mind us asking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, nothin' too complicated. I'll pick out ten\x01",
            "questions at random from our test bank we\x01",
            "use in the written portion of the bracer exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat way, I'll be able to know if you're at least\x01",
            "as knowledgeable as a junior bracer if you\x01",
            "manage to get all ten of 'em right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHow-ev-er, if you were to fail...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThere will be no place for us to operate\x01",
            "in Crossbell, where some of the greatest\x01",
            "bracers have gathered.\x02\x03",
            "#0200FAm I correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FM-Man... Talk about putting on the pressure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FOh, well that's just dandy, ain't it?\x01",
            "You're gonna think we're a bunch of\x01",
            "dumbasses if we screw this up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, pshaw! Not at all! Not really interested\x01",
            "in degrading you. It's not my style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHere's a tip for you. You can study the contents\x01",
            "of the exam over at the public library in the\x01",
            "Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSimply put, I'm testing to see if you'll actually\x01",
            "be worth your salt when it comes to helping\x01",
            "out the average Crossbellan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PSo anyway, you guys up for the challenge?\x02",
    )

    CloseMessageWindow()
    OP_29(0x4, 0x4, 0x2)
    OP_29(0x4, 0x1, 0x0)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2DD")
    Call(0, 25)
    Call(0, 26)

    label("loc_B2DD")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_22_A77C end

    def Function_23_B2F5(): pass

    label("Function_23_B2F5")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PThis is a ten-question exam on general\x01",
            "knowledge that we use to test anyone\x01",
            "looking to become a junior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you can answer 'em all correctly, I'll consider\x01",
            "you at least on the level of a junior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PKeep in mind that they're easy questions that you could\x01",
            "study for at the library in the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSo how about it?\x01",
            "You up for the challenge?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B51E")
    Call(0, 25)
    Call(0, 26)

    label("loc_B51E")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_B2F5 end

    def Function_24_B536(): pass

    label("Function_24_B536")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B685")

    ChrTalk(
        0x101,
        (
            "#11P#0012FHmm... We haven't mentally prepared ourselves\x01",
            "for it yet, sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWow. Chickening out, are we? That's surprisingly\x01",
            "timid of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhat do I care, though? Feel free to come back\x01",
            "and give it a shot if you ever rack up the courage\x01",
            "to do so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B685")

    Return()

    # Function_24_B536 end

    def Function_25_B686(): pass

    label("Function_25_B686")


    ChrTalk(
        0x101,
        "#11P#0001FSure, we'll give it a shot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNow that's what I'm talkin' about, baby! ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#12P#0305FYo, Lloyd. You sure about this?\x02",
    )

    CloseMessageWindow()

    def lambda_B720():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B720)
    Sleep(50)

    def lambda_B730():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B730)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x101,
        (
            "#11P#0003FYeah. I'm not too worried about it, honestly.\x01",
            "We had to take similar exams back at the academy.\x02\x03",
            "#0001FAnd besides, it's almost like I'm running away\x01",
            "if I back out of it now. It wouldn't feel right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FI understand what you mean, and I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FLikewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHeh. I get where you're comin' from.\x01",
            "Screw it. Let's do this!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8B8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8B8)

    def lambda_B8C5():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B8C5)

    def lambda_B8D2():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B8D2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        "#5PHahaha. I like that feisty attitude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, Lloyd. I get the impression that\x01",
            "you're the leader of the group, in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWanna take a crack at answering the\x01",
            "questions on behalf of everyone else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001FYeah. Fine by me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POoooh! I love that look in your eyes.\x01",
            "It's making the hair on the back of\x01",
            "my neck stand up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POkay, let's get this party started!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Michel's Test]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_68(1000, 1950, 9200, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20390, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Bracer Guild - Receptionist Michel's Test\x01",
            "-Bracer General Education Examination-\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#5PAnd now, the first question! This one'll\x01",
            "be a cute freebie to get ya warmed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs we all know, the Orbal Revolution brought forth\x01",
            "the technological advancements of orbments to\x01",
            "our continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe question is, how many years ago did it occur?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "How long ago did the Orbal Revolution occur?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Approximately 10 years ago]\x01",      # 0
            "[② Approximately 30 years ago]\x01",      # 1
            "[③ Approximately 50 years ago]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BD75"),
        (1, "loc_BF9A"),
        (2, "loc_C1C7"),
        (SWITCH_DEFAULT, "loc_C3DC"),
    )


    label("loc_BD75")


    ChrTalk(
        0x101,
        "#12P#0000FI think it happened about 10 years ago, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PAbsolutely not, young man! Did you seriously\x01",
            "think society has advanced that quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is 50 years ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe advent of orbal technology has all\x01",
            "happened in the last five decades.\x01",
            "Pretty amazing stuff, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBack when I was a little kid, I woulda never imagined\x01",
            "riding in something as fancy as an orbal car. Seemed\x01",
            "like something straight outta some fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(I blew it straight from the get-go.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3DC")

    label("loc_BF9A")


    ChrTalk(
        0x101,
        "#12P#0000FI think it happened about 30 years ago, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PNice try, but you're WRONG! Don't just shoot\x01",
            "from the hip 'cause it seems like a safe answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is 50 years ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe advent of orbal technology has all\x01",
            "happened in the last five decades.\x01",
            "Pretty amazing stuff, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBack when I was a little kid, I woulda never imagined\x01",
            "riding in something as fancy as an orbal car. Seemed\x01",
            "like something straight outta some fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(I blew it straight from the get-go.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3DC")

    label("loc_C1C7")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI'm pretty sure it happened about 50 years ago,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PBingo! Right you are, my friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDon't let it get to your head, though.\x01",
            "Remember, it was just a freebie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's crazy to think about how much orbal technology\x01",
            "has advanced in the last few decades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBack when I was a little kid, I woulda never imagined\x01",
            "riding in something as fancy as an orbal car.\x01",
            "Seemed like something straight outta some fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(Phew... That's one hurdle down.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C3DC")

    label("loc_C3DC")


    ChrTalk(
        0x8,
        (
            "#5PAnyway, on to the next question!\x01",
            "Question numero deux!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe driving force behind the Orbal Revolution was\x01",
            "all thanks to one man's prototype orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis one's another gimme, but who is the\x01",
            "creator of said orbment?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Who invented the orbment?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Professor A. Russell]\x01",      # 0
            "[② Professor C. Epstein]\x01",      # 1
            "[③ Professor G. Schmidt]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C58C"),
        (1, "loc_C90C"),
        (2, "loc_CC59"),
        (SWITCH_DEFAULT, "loc_CFEC"),
    )


    label("loc_C58C")


    ChrTalk(
        0x101,
        "#12P#0000FWasn't it Professor A. Russell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PNo way, Jose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is Professor C. Epstein.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDid you guys know that people were skeptical\x01",
            "of his invention at first? They probably thought\x01",
            "it was some kinda sorcery at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce people began to realize just how gosh\x01",
            "darn convenient they are, they quickly became\x01",
            "became an integral part of our daily lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIncidentally, Professor Russell is one of Epstein's\x01",
            "disciples, and he made large contributions\x01",
            "to the Orbal Revolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Oh... Come to think of it, I've heard\x01",
            "all of this somewhere before.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FNeed I remind you that I am currently\x01",
            "employed by the Epstein Foundation?\x02\x03",
            "#0211FI DO believe I mentioned this recently,\x01",
            "did I not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FProbably shouldn't have blown that one.\x01",
            "(I feel like she's going to thwack me with her staff.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFEC")

    label("loc_C90C")


    ChrTalk(
        0x101,
        "#12P#0000FI know this one. It's Professor C. Epstein.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PHuzzah! You got the right answer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDid you guys know that people were skeptical\x01",
            "of his invention at first? They probably thought\x01",
            "it was some kinda sorcery at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce people began to realize just how\x01",
            "gosh darn convenient they are, they quickly\x01",
            "became an integral part of our daily lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThe Epstein Foundation has made great efforts\x01",
            "towards the research and adoption of orbal\x01",
            "technology. That much is common knowledge.\x02\x03",
            "#0200FThe orbal staff I use for combat also falls under\x01",
            "the foundation's research efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(Oh, yeah. Tio totally mentioned that she's\x01",
            "employed by the Epstein Foundation.)\x02\x03",
            "#0000F(That was a close call. She probably would have\x01",
            "given me an earful if I screwed that one up.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_CFEC")

    label("loc_CC59")


    ChrTalk(
        0x101,
        "#12P#0000FWasn't it Professor G. Schmidt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PNow you've gone and Schmidt it up! Wrong!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is Professor C. Epstein.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDid you guys know that people were skeptical\x01",
            "of his invention at first? They probably thought\x01",
            "it was some kinda sorcery at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce people began to realize just how\x01",
            "gosh darn convenient they are, they quickly\x01",
            "became an integral part of our daily lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIncidentally, Professor Schmidt is one of Epstein's\x01",
            "disciples, and he's known as the authority on\x01",
            "mechanical engineering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Oh... Come to think of it, I've heard\x01",
            "all of this somewhere before.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FNeed I remind you that I am currently\x01",
            "employed by the Epstein Foundation?\x02\x03",
            "#0211FI DO believe I mentioned this recently,\x01",
            "did I not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FProbably shouldn't have blown that.\x01",
            "(I feel like she's going to thwack me with her staff.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFEC")

    label("loc_CFEC")


    ChrTalk(
        0x8,
        "#5PEnough chitchat. Next question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe all know that quartz are the key\x01",
            "component to any orbal device, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnd to synthesize quartz, you need sepith.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd when I talk about sepith, what specific\x01",
            "form of septium am I referring to?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "What is another name for sepith?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Septium crystals]\x01",       # 0
            "[② Processed septium]\x01",      # 1
            "[③ Septium fragments]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D1AF"),
        (1, "loc_D39C"),
        (2, "loc_D58A"),
        (SWITCH_DEFAULT, "loc_D775"),
    )


    label("loc_D1AF")


    ChrTalk(
        0x101,
        "#12P#0000FUhhh...septium crystals?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PIt's crystal clear that you're WRONG!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is septium fragments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSeptium fragments are refined into quartz,\x01",
            "which we then use in our orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMonsters are inherently attracted to septium,\x01",
            "so they often end up munching on sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDefeating critters is an easy way to obtain\x01",
            "sepith, so keep that in your back pocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Whoops... Got caught off guard there.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D775")

    label("loc_D39C")


    ChrTalk(
        0x101,
        "#12P#0000FUhhh...processed septium?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PDid you PROCESS the question?! WRONG!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is septium fragments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSeptium fragments are refined into quartz,\x01",
            "which we then use in our orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMonsters are inherently attracted to septium,\x01",
            "so they often end up munching on sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDefeating critters is an easy way to obtain\x01",
            "sepith, so keep that in your back pocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Whoops... Got caught off guard there.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D775")

    label("loc_D58A")


    ChrTalk(
        0x101,
        "#12P#0000FI believe they're septium fragments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5POh, heck yeah! You got that right, buddy boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSeptium fragments are refined into quartz,\x01",
            "which we then use in our orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMonsters are inherently attracted to septium,\x01",
            "so they often end up munching on sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDefeating critters is an easy way to obtain\x01",
            "sepith, so keep that in your back pocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0004F(So far, so good. These questions are all\x01",
            "common sense.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D775")

    label("loc_D775")


    ChrTalk(
        0x8,
        "#5PIt's time to prepare...for question four!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POur fave pal, the Erebonian Empire,\x01",
            "lies to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIts important and overwhelming existence\x01",
            "can be felt by all of us Crossbellans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI imagine you've probably seen their emblem before.\x01",
            "Can you recall what the symbol of Erebonia is?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "What type of symbol can be found on Erebonia's emblem?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① The supporting gauntlet]\x01",      # 0
            "[② The white falcon]\x01",             # 1
            "[③ The golden stallion]\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D985"),
        (1, "loc_DB8A"),
        (2, "loc_DD9F"),
        (SWITCH_DEFAULT, "loc_DFDB"),
    )


    label("loc_D985")


    ChrTalk(
        0x101,
        "#12P#0000FThe...supporting gauntlet...probably?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PYou're just doing this to annoy me, aren't ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer is the golden stallion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's no secret that the pride of the Erebonian Empire\x01",
            "lies in its unmatched military prowess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe golden stallion is a symbol of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, and by the way. In case you forgot, we're\x01",
            "standing inside of the BRACER GUILD.\x01",
            "The supporting gauntlet is OUR SYMBOL. Jerk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(I have no idea what I'm doing.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFDB")

    label("loc_DB8A")


    ChrTalk(
        0x101,
        "#12P#0000FIt's a white falcon, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PCan't say it was! At least you chose an animal\x01",
            "and not the supporting gauntlet like some silly\x01",
            "goose, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe actual correct answer is the golden stallion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's no secret that the pride of the Erebonian Empire\x01",
            "lies in its unmatched military prowess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe golden stallion is a symbol of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn case you were curious, the white falcon\x01",
            "belongs to Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(I need to think about this more carefully.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFDB")

    label("loc_DD9F")


    ChrTalk(
        0x101,
        "#12P#0000FI believe it's the golden stallion, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PNeigh...! Is what I'd say if you were wrong,\x01",
            "but you're right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's no secret that the pride of the Erebonian Empire\x01",
            "lies in its unmatched military prowess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe golden stallion is a symbol of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere was once an order of knights in the Empire known as\x01",
            "the Eisenritter. They were known for employing cavalry, so\x01",
            "that may be why the Empire adopted the golden stallion as\x01",
            "its emblem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(Nice! Managed to maneuver my way through that.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_DFDB")

    label("loc_DFDB")


    ChrTalk(
        0x8,
        (
            "#5PWe're almost halfway there!\x01",
            "Six more questions to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA nation known as the Calvard Republic sits\x01",
            "directly to the east of Crossbell, diametrically\x01",
            "opposing the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's no exaggeration to state that Crossbell's entire\x01",
            "existence is reliant on the long-term struggle for\x01",
            "power between Erebonia and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWith that being said, do you know the name of the\x01",
            "primary manufacturer of orbal and heavy weaponry\x01",
            "for the Republic?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "The name of the Republic-based manufacturer is...",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Verne Company]\x01",              # 0
            "[② Reinford Company]\x01",           # 1
            "[③ Zeiss Central Factory]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E27F"),
        (1, "loc_E4C6"),
        (2, "loc_E7DE"),
        (SWITCH_DEFAULT, "loc_EAF4"),
    )


    label("loc_E27F")


    ChrTalk(
        0x101,
        "#12P#0000FOh, this one's easy. It's the Verne Company.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PLooks to me like you had Verne in your...Verne-acular!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Calvardian Verne Company and the Erebonian\x01",
            "Reinford Company are famed as the two largest\x01",
            "manufacturers of orbal weaponry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, it is a disservice to only attribute their contri-\x01",
            "butions to weaponry. They're also responsible for the\x01",
            "development of vehicles, appliances, and plenty of other\x01",
            "nifty items!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0004F(Phew... Another one down. He started rambling\x01",
            "for a bit, but I'm glad I got it right.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EAF4")

    label("loc_E4C6")


    ChrTalk(
        0x101,
        "#12P#0000FI want to say it's the Reinford Company?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PYou really failed to...take the reins on that question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe answer you were looking for was the Verne Company.\x01",
            "Though their names are similar, the Reinford Company\x01",
            "resides in Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Calvardian Verne Company and the Erebonian\x01",
            "Reinford Company are famed as the two largest\x01",
            "manufacturers of orbal weaponry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, it is a disservice to only attribute their contri-\x01",
            "butions to weaponry. They're also responsible for the\x01",
            "development of vehicles, appliances, and plenty of other\x01",
            "nifty items!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FAre you even trying, Lloyd? How did you\x01",
            "manage to get that question wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(I guess that one woulda been a no-brainer for\x01",
            "someone who uses an orbal gun, huh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF4")

    label("loc_E7DE")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI feel like it might have been Zeiss Central Factory?\x01",
            "I'm not actually sure, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PZeiss is an outrage! You get zero points!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe answer you were looking for was the Verne Company.\x01",
            "Zeiss Central Factory resides in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Calvardian Verne Company and the Erebonian\x01",
            "Reinford Company are famed as the two largest\x01",
            "manufacturers of orbal weaponry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, it is a disservice to only attribute their contri-\x01",
            "butions to weaponry. They're also responsible for the\x01",
            "development of vehicles, appliances, and plenty of other\x01",
            "nifty items!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FAre you even trying, Lloyd? How did you\x01",
            "manage to get that question wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(I guess that one woulda been a no-brainer for\x01",
            "someone who uses an orbal gun.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF4")

    label("loc_EAF4")


    ChrTalk(
        0x8,
        (
            "#5PLooks like we've made it a little past\x01",
            "the halfway point, now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED36")

    ChrTalk(
        0x103,
        "#12P#0200FYou are giving a valiant effort.\x02",
    )

    CloseMessageWindow()

    def lambda_EB7F():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB7F)
    Sleep(50)

    def lambda_EB8F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EB8F)

    def lambda_EB9C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EB9C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#6P#0309FNice job, Leader! If you keep this up,\x01",
            "I'm sure you'll have no problems\x01",
            "plowin' through the rest of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0102FI'm thoroughly impressed, Lloyd.\x01",
            "I wasn't expecting this from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FCome on, guys. Aren't you laying on the\x01",
            "compliments a bit too thick? The questions\x01",
            "were all fairly basic, weren't they?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED03():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED03)

    def lambda_ED10():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED10)

    def lambda_ED1D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED1D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_F041")

    label("loc_ED36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEB2")

    ChrTalk(
        0x103,
        "#12P#0200FI did not know you enjoyed living on the edge.\x02",
    )

    CloseMessageWindow()

    def lambda_ED88():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED88)
    Sleep(50)

    def lambda_ED98():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED98)

    def lambda_EDA5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EDA5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#6P#0303FRight in the middle of the bell curve.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FHmm... I wish you'd take this a little more\x01",
            "seriously, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FD-Don't worry, I can recover in the second half.\x02",
    )

    CloseMessageWindow()

    def lambda_EE7F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE7F)

    def lambda_EE8C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE8C)

    def lambda_EE99():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE99)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_F041")

    label("loc_EEB2")


    ChrTalk(
        0x103,
        (
            "#12P#0211FIt is painfully apparent that you came woefully\x01",
            "unprepared.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EF02():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF02)
    Sleep(50)

    def lambda_EF12():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EF12)

    def lambda_EF1F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EF1F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#6P#0306FNot gonna lie to you buddy. Things ain't\x01",
            "lookin' too hot right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FRight... Well, I'm sure you'll find some\x01",
            "way to recover...maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0003FI feel like I want to die right about now.\x02",
    )

    CloseMessageWindow()

    def lambda_F013():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F013)

    def lambda_F020():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F020)

    def lambda_F02D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F02D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    label("loc_F041")


    ChrTalk(
        0x8,
        (
            "#5PWell, regardless of how well you're doing,\x01",
            "you've still got five questions left, buckaroo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI think you've had enough time to warm up,\x01",
            "so it's time I up the ante. I hope you're ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIt's time for the sixth question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA catastrophic event known as the Great Collapse\x01",
            "befell our continent a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis disaster resulted in the complete loss of civilization\x01",
            "and fractured people into different factions that waged\x01",
            "war on one another for many centuries to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis period, now known as the 'Dark Ages,' was eventually\x01",
            "ended by one such faction that rose triumphant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThey organized themselves to bring about order and justice\x01",
            "to Zemuria, allowing for the rebuilding of society to begin.\x01",
            "You probably know who I'm talking about, right?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Which faction put an end to the Dark Ages?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Septian Church]\x01",         # 0
            "[② Bracer Guild]\x01",           # 1
            "[③ Fisherman's Guild]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F422"),
        (1, "loc_F6BD"),
        (2, "loc_F9C2"),
        (SWITCH_DEFAULT, "loc_FCCB"),
    )


    label("loc_F422")


    ChrTalk(
        0x101,
        "#12P#0000FIt was the Septian Church, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5POh, thank Aidios! You're correct!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAround year 500 of the Septian Calendar, the Septian Church\x01",
            "emerged to spread the teachings of the Goddess of the Sky,\x01",
            "Aidios. Their intent was to provide aid to those in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe church's influence grew powerful enough to establish\x01",
            "themselves across Zemuria, so the nobles who ruled during\x01",
            "the Dark Ages could no longer ignore them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe effects of Aidios and Her teachings can still be felt\x01",
            "firmly across the continent to this day, as they are deeply\x01",
            "rooted in our society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(Well, that went well.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_FCCB")

    label("loc_F6BD")


    ChrTalk(
        0x101,
        "#12P#0000FWas it the Bracer Guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PBracer yourself because you're not going to like this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe correct answer is actually the Septian Church.\x01",
            "And, c'mon... Did you even try? That was common sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAround year 500 of the Septian Calendar, the Septian Church\x01",
            "emerged to spread the teachings of the Sky Goddess, Aidios.\x01",
            "Their intent was to provide aid to those in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe church's influence grew powerful enough to establish\x01",
            "themselves across Zemuria, so the nobles who ruled during\x01",
            "the Dark Ages could no longer ignore them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe effects of Aidios and Her teachings can still be felt\x01",
            "firmly across the continent to this day, as they are deeply\x01",
            "rooted in our society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Ugh. I overthought it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_FCCB")

    label("loc_F9C2")


    ChrTalk(
        0x101,
        "#12P#0000FWas it the Fisherman's Guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PForever Great Angler Ding ding ding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...Just kidding. It was the Septian Church. The\x01",
            "Fisherman's Guild is one door over, if you want\x01",
            "to check them out, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAround year 500 of the Septian Calendar, the Septian Church\x01",
            "emerged to spread the teachings of the Sky Goddess, Aidios.\x01",
            "Their intent was to provide aid to those in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe church's influence grew powerful enough to establish\x01",
            "themselves across Zemuria, so the nobles who ruled during\x01",
            "the Dark Ages could no longer ignore them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe effects of Aidios and Her teachings can still be felt\x01",
            "firmly across the continent to this day, as they are deeply\x01",
            "rooted in our society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Ugh, I overthought it.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_FCCB")

    label("loc_FCCB")


    ChrTalk(
        0x8,
        "#5PAnyway, on to lucky number seven!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe headquarters of the Septian Church is located\x01",
            "in a city-state known as the Holy City of Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Holy City of Arteria is made up of various\x01",
            "administrative organizations that handle specific\x01",
            "tasks, giving it a state-like structure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAmong these organizations is one that handles the\x01",
            "church's ceremonial rituals. Do you happen to know\x01",
            "which organization I am referring to?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Which organization within the Septian Church\x01",
            "handles ceremonial rituals?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Papal Guard]\x01",                          # 0
            "[② Congregation for Divine Worship]\x01",      # 1
            "[③ Congregation for the Sacraments]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FF84"),
        (1, "loc_101B0"),
        (2, "loc_103B6"),
        (SWITCH_DEFAULT, "loc_10642"),
    )


    label("loc_FF84")


    ChrTalk(
        0x101,
        "#12P#0000F...Is it the Papal Guard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PNo. I bet you'd like it if it were, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Papal Guard is tasked with defending\x01",
            "the Holy City of Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe answer I was looking for was the\x01",
            "Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMost priests found within chapels and cathedrals\x01",
            "across the continent are employed by this organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere's actually a cathedral located outside of the\x01",
            "northern exit of the city that I offer the occasional\x01",
            "prayer at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Oof. That one was really tough.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10642")

    label("loc_101B0")


    ChrTalk(
        0x101,
        "#12P#0000FIs it the Congregation for Divine Worship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PBingo! Good job! That was one tough cookie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMost priests found within chapels and cathedrals\x01",
            "across the continent are employed by this organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere's actually a cathedral located outside of the\x01",
            "northern exit of the city that I offer the occasional\x01",
            "prayer at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe archbishop in charge there is also from\x01",
            "the Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(Phew... That was really tough.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10642")

    label("loc_103B6")


    ChrTalk(
        0x101,
        "#12P#0000FIs it the Congregation for the Sacraments?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PYou sacra-bleu it, because you're wrong!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Congregation for the Sacraments is responsible for\x01",
            "the management and retrieval of artifacts, but any info\x01",
            "about them isn't publicly accessible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe answer I was looking for was the\x01",
            "Congregation for Divine Worship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMost priests found within chapels and cathedrals\x01",
            "across the continent are employed by this organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere's actually a cathedral located outside of the\x01",
            "northern exit of the city that I offer the occasional\x01",
            "prayer at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Oof. That one was really tough.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10642")

    label("loc_10642")


    ChrTalk(
        0x8,
        (
            "#5PCan you feel the burn? We're almost there!\x01",
            "On to the eighth question!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs we all know, the Bracer Guild has branches\x01",
            "all across the continent. But, what I really wanna\x01",
            "know is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...just where in the heck are the main headquarters\x01",
            "located?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Where are the Bracer Guild Headquarters located?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Crossbell State]\x01",      # 0
            "[② Leman State]\x01",          # 1
            "[③ Ored State]\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10809"),
        (1, "loc_109F8"),
        (2, "loc_10B66"),
        (SWITCH_DEFAULT, "loc_10CFF"),
    )


    label("loc_10809")


    ChrTalk(
        0x101,
        "#12P#0000FOh, I got this. It's in Crossbell State.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PYou're equal parts confident and WRONG!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAfter all, we're in the Crossbell BRANCH of the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POur headquarters can be found in Leman State,\x01",
            "alongside our biggest investors: the Epstein\x01",
            "Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn the event of a serious conflict, HQ can issue\x01",
            "a direct order for all bracers to mobilize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Huh, really? I don't think I've ever seen\x01",
            "that happen in Crossbell, have I?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CFF")

    label("loc_109F8")


    ChrTalk(
        0x101,
        "#12P#0000FIt's in Leman State, obviously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PYou're le man, 'cause right you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POur headquarters can be found in Leman State,\x01",
            "alongside our biggest investors: the Epstein\x01",
            "Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn the event of a serious conflict, HQ can issue\x01",
            "a direct order for all bracers to mobilize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(Huh, I see.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10CFF")

    label("loc_10B66")


    ChrTalk(
        0x101,
        "#12P#0000FWasn't it in Ored?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PI am 'bOred' of your wrong answer! Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNot a bad guess, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POur headquarters can be found in Leman State,\x01",
            "alongside our biggest investors: the Epstein\x01",
            "Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn the event of a serious conflict, HQ can issue\x01",
            "a direct order for all bracers to mobilize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Darn. I really thought I had that one.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_10CFF")

    label("loc_10CFF")


    ChrTalk(
        0x8,
        "#5PTime for the ninth question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou ever heard of that infamous thief that lives\x01",
            "in Erebonia? He's a bit of a strange one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe steals precious works of art, and then sends out\x01",
            "calling cards with riddles on how to retrieve them.\x01",
            "Also, his identity is hidden behind a mask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PApparently, people laud him as some kind of hero.\x01",
            "Sounds more like a sadist to me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyway, I got a little off-track there. Do you\x01",
            "know what name this fella likes to go by?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "What is the nickname of the infamous\x01",
            "Erebonian thief?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Phantom Thief A]\x01",      # 0
            "[② Phantom Thief B]\x01",      # 1
            "[③ Phantom Thief C]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10FB8"),
        (1, "loc_11237"),
        (2, "loc_114E3"),
        (SWITCH_DEFAULT, "loc_1175A"),
    )


    label("loc_10FB8")


    ChrTalk(
        0x101,
        "#12P#0000FLet's go with Phantom Thief...A.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PA swing and A miss! Nice try, though!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer was Phantom Thief B.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHis infamy transcends the confines of Erebonia,\x01",
            "as people across the continent have heard of\x01",
            "his misdeeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNothing is safe from his grasp, either. He's stolen\x01",
            "anything ranging from rare paintings in museums\x01",
            "to a whole friggin' tank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRumor has it that he was recently running amok\x01",
            "in Liberl. Who knows? Maybe you'll run into him\x01",
            "sooner than you think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Oh, wow. I wasn't expecting him to pull out\x01",
            "recent events from foreign countries.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1175A")

    label("loc_11237")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI've actually heard of him before.\x01",
            "Wasn't his name Phantom Thief...B?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PUn-B-lievable! You got it right! Looks like\x01",
            "you've done your foreign affairs homework!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHis infamy transcends the confines of Erebonia,\x01",
            "as people across the continent have heard of\x01",
            "his misdeeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNothing is safe from his grasp, either. He's stolen\x01",
            "anything ranging from rare paintings in museums\x01",
            "to a whole friggin' tank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRumor has it that he was recently running amok\x01",
            "in Liberl. Who knows? Maybe you'll run into him\x01",
            "sooner than you think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Yeah, I've definitely heard rumors.\x01",
            "I'd like to avoid him if possible, though.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1175A")

    label("loc_114E3")


    ChrTalk(
        0x101,
        "#12P#0000FIs it Phantom Thief...C?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        "#5PI C what you did there, but it isn't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThe correct answer was Phantom Thief B.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHis infamy transcends the confines of Erebonia,\x01",
            "as people across the continent have heard of\x01",
            "his misdeeds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNothing is safe from his grasp, either. He's stolen\x01",
            "anything ranging from rare paintings in museums\x01",
            "to a whole friggin' tank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRumor has it that he was recently running amok\x01",
            "in Liberl. Who knows? Maybe you'll run into him\x01",
            "sooner than you think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Oh, wow. I wasn't expecting him to pull out\x01",
            "recent events from foreign countries.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1175A")

    label("loc_1175A")


    ChrTalk(
        0x8,
        "#5PIt's time for the tenth and final question!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PErebonia and Calvard have been at each other's throats\x01",
            "over the rightful ownership of Crossbell State for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThey've waged war against each other time and time again,\x01",
            "causing grief and bloodshed for many innocent civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe situation became so severe that it was brought to the\x01",
            "attention of Liberl's Queen Alicia. She proposed a treaty\x01",
            "to end the conflict between the two nations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe treaty was signed in 1202 by three nations: Liberl,\x01",
            "Erebonia, and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you're truly Crossbellan, then the answer to\x01",
            "this question should be a no-brainer, right?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "What was the name of the treaty signed\x01",
            "by the three nations?",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "[① Non-Interference Pact]\x01",      # 0
            "[② Non-Aggression Pact]\x01",        # 1
            "[③ Non-Hindrance Pact]\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11ACC"),
        (1, "loc_11E99"),
        (2, "loc_1223D"),
        (SWITCH_DEFAULT, "loc_1262F"),
    )


    label("loc_11ACC")


    ChrTalk(
        0x101,
        "#12P#0000FIt was a non-interference pact, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PGet it together, honey! Aren't you supposed\x01",
            "to be Crossbellan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThey actually signed a non-aggression pact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe treaty was drafted with the intention of\x01",
            "diffusing conflicts between any of the three\x01",
            "nations via diplomacy, as opposed to war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPrior to the signing of the treaty, anxiety was\x01",
            "at an all-time high in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll spare you most of the details, but both nations'\x01",
            "armored divisions thought it appropriate to hold\x01",
            "simultaneous military exercises at our borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POne single misstep could have had catastrophic\x01",
            "consequences. I'm sure it would have triggered\x01",
            "a full-scale war between the two of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd so, Queen Alicia proposed this treaty\x01",
            "as a means of preventing that from happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTeehee. We should be extremely grateful\x01",
            "to Liberl for saving our hides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Woooow... I sure messed that one up.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1262F")

    label("loc_11E99")


    ChrTalk(
        0x101,
        "#12P#0000FYou're referring to the Non-Aggression Pact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PAnd non-aggressive it was! That one\x01",
            "shoulda been a gimme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe treaty was drafted with the intention of\x01",
            "defusing conflicts between any of the three\x01",
            "nations via diplomacy, as opposed to war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPrior to the signing of the treaty, anxiety\x01",
            "was at an all-time high in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll spare you most of the details, but both nations'\x01",
            "armored divisions thought it appropriate to hold\x01",
            "simultaneous military exercises at our borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POne single misstep could have had catastrophic\x01",
            "consequences. I'm sure it would have triggered\x01",
            "a full-scale war between the two of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd so, Queen Alicia proposed this treaty as\x01",
            "a means of preventing that from happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTeehee. We should be extremely grateful\x01",
            "to Liberl for saving our hides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0004F(No way was I going to get that one wrong.)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1262F")

    label("loc_1223D")


    ChrTalk(
        0x101,
        "#12P#0000FI think it was called the non-hindrance pact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5PGet it together, honey! Aren't you supposed\x01",
            "to be Crossbellan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThey actually signed a non-aggression pact.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe treaty was drafted with the intention of\x01",
            "defusing conflicts between any of the three\x01",
            "nations via diplomacy, as opposed to war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPrior to the signing of the treaty, anxiety was\x01",
            "at an all-time high in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll spare you most of the details, but both nations'\x01",
            "armored divisions thought it appropriate to hold\x01",
            "simultaneous military exercises at our borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POne single misstep could have had catastrophic\x01",
            "consequences. I'm sure it would have triggered\x01",
            "a full-scale war between the two of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd so, Queen Alicia proposed this treaty\x01",
            "as a means of preventing that from happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTeehee. We should be extremely grateful\x01",
            "to Liberl for saving our hides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006F(Ugh. I remembered the events, though.\x01",
            "Doesn't that count for something?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1262F")

    label("loc_1262F")


    ChrTalk(
        0x8,
        "#5PAw, it's finally over. I was having so much fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PGood job getting through that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006F(Oh, thank Aidios. It's finally over...)\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_B686 end

    def Function_26_126D8(): pass

    label("Function_26_126D8")

    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PWhy don't we take a look at your score, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001F(*gulp*)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C52")

    ChrTalk(
        0x8,
        (
            "#5PWowza, a perfect score! Your knowledge is\x01",
            "in line with our junior bracers at least!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTeehee. Looks like you've got some potential\x01",
            "in you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FOh, well, that's relieving to know. Thank you\x01",
            "very much.\x01",
            "(W-Wow, didn't think he'd compliment me straight up.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FDude, I was clenchin' my cheeks the whole way\x01",
            "through. I'm glad I can finally take a breather.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12911():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12911)
    Sleep(50)

    def lambda_12921():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12921)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#12P#0100FI'm surprised Lloyd managed to answer questions\x01",
            "outside of his area of expertise, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI think I will ask him to assist me with filling in\x01",
            "missing information for the database.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0012FAww, you guys are embarrassing me.\x02",
    )

    CloseMessageWindow()

    def lambda_12A37():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A37)

    def lambda_12A44():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A44)

    def lambda_12A51():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12A51)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        (
            "#5PAnyway, I've got a cute little treat for the\x01",
            "doggie who managed to bark out all of\x01",
            "the correct answers.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x7F, 1)

    ChrTalk(
        0x101,
        "#11P#0005FOh, wow. Are you sure we can have this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYep! I didn't think you stood a snowball's chance\x01",
            "in Gehenna of doing so well, so think of this as\x01",
            "an apology for my ignorance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIt's all yours now, sweetie. Take it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FWell, if you say so... Thanks a lot!\x02",
    )

    CloseMessageWindow()
    OP_2C(0x4, 0x2)
    OP_29(0x4, 0x1, 0x1)
    Jump("loc_1314C")

    label("loc_12C52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F13")

    ChrTalk(
        0x8,
        (
            "#5PHmm... Looks like you managed to pull off\x01",
            "a half-decent score, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt would have been full-decent if you\x01",
            "answered all of them correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBut all's well that ends well, am I right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FYeah, I think I still have a few gaps in my\x01",
            "knowledge for certain topics.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#12P#0300FGood job on pullin' through, I guess?\x02",
    )

    CloseMessageWindow()

    def lambda_12DCD():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12DCD)
    Sleep(50)

    def lambda_12DDD():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12DDD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#6P#0104FAgreed, but I don't think it's necessarily a\x01",
            "bad thing.\x02\x03",
            "#0100FWe can use this as an opportunity to strive towards\x01",
            "filling in the gaps in our knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FGood luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FThanks, everybody.\x02",
    )

    CloseMessageWindow()

    def lambda_12ED5():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12ED5)

    def lambda_12EE2():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12EE2)

    def lambda_12EEF():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12EEF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_2C(0x4, 0x1)
    OP_29(0x4, 0x1, 0x2)
    Jump("loc_1314C")

    label("loc_12F13")


    ChrTalk(
        0x8,
        "#5PWell, wasn't that a disappointing performance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's clear to me that you came\x01",
            "grossly underprepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FI could honestly die of embarrassment right now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FHey, it's not that big a deal. Stop gettin' all\x01",
            "bent out of shape over it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1302E():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1302E)
    Sleep(50)

    def lambda_1303E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1303E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#6P#0106FI'd be worried if he didn't care. It'd cause us\x01",
            "bigger problems down the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0211FThe future looks bleak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FY-Yeah... I promise I'll do something about this.\x02",
    )

    CloseMessageWindow()

    def lambda_13118():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13118)

    def lambda_13125():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13125)

    def lambda_13132():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13132)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_29(0x4, 0x1, 0x3)

    label("loc_1314C")


    ChrTalk(
        0x8,
        "#5PThis concludes our little game.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PY'all better bust your backs making sure\x01",
            "you don't drag us down, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FYes, sir. We'll do everything we can.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Michel's Test]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x4, 0x4, 0x10)
    Return()

    # Function_26_126D8 end

    def Function_27_1325E(): pass

    label("Function_27_1325E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09102.itc", 0x1E)
    OP_68(-6000, 1100, 48100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -6000, 100, 49200, 180)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis152.itp")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#1100001VLooks like you had another rough month.\x01",
            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(22000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x9,
        (
            "#1100002V#5P#1404FIt's fine. I'm used to it already.\x02\x03",
            "#1100003V#1400FAnyway, I'll be counting on you for\x01",
            "the payment again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100004V#2PSure thing. I'll transfer it to you via the IBC.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100005V#2PI feel partially responsible given that I assign\x01",
            "your requests, but, um...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100006V#2P...maybe you should consider reducing your\x01",
            "workload just a teensy bit, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100007V#2PPoor Shizuku must be feeling lonely without\x01",
            "Daddy by her side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100008V#5P#1403F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100009V#2PI know, I know. I'm sorry. I know I said I wouldn't\x01",
            "bring this up again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#1100010V#2POh, that reminds me. Headquarters contacted\x01",
            "me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100011V#2PThey keep bugging me to get you to\x01",
            "accept the offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100012V#5P#1405FAre they seriously still at it?\x02\x03",
            "#1100013V#1403FI've rejected their offer numerous times already.\x01",
            "I wish they'd give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100014V#2PCan ya blame 'em? They're desperately searching\x01",
            "for someone with the qualifications to fill in the\x01",
            "gaping hole left by Cassius Bright's resignation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100015V#2PDidn't you two train under the same master?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100016V#2PYou're basically equals when you look at your\x01",
            "stats with the guild, so hurry up and accept\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100017V#5P#1404FWhile that may be true on paper, we're completely\x01",
            "different people.\x02\x03",
            "#1100018VUnlike Cassius, I haven't solved any conflicts on an\x01",
            "international scale. I can't help but feel that\x01",
            "people are overstating my achievements.\x02\x03",
            "#1100019V#1402FI honestly don't feel like I have the qualifications\x01",
            "to be his proper successor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100020V#2POh, phooey. You and I both know that isn't true.\x01",
            "Didn't you resolve that thing out in Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100021V#2PThe grand prince himself presented you with\x01",
            "a medal of honor, so isn't that enough of an\x01",
            "indication of your qualifications?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100022V#5P#1403FI would disagree--that case hasn't truly been\x01",
            "resolved, as far as I'm concerned.\x02\x03",
            "#1100023V#1401FI may have prevented the immediate disaster,\x01",
            "but the masterminds responsible are still out\x01",
            "there.\x02\x03",
            "#1100024VI had planned to refuse the medal, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100025V#2PGeez. You're a stick in the mud, aren't ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100026V#2PC'mon, accepting that promotion will drop\x01",
            "your workload a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100027V#2PYou've done over a hundred requests this month,\x01",
            "for Aidios' sake! That's inhuman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100028V#5P#1404FI don't feel like I bit off more than I could chew.\x02\x03",
            "#1100029V#1402FInternational travel has become far easier with the\x01",
            "increased frequency of train and flight services.\x02\x03",
            "#1100030VAnd besides, aren't two bracers transferring here?\x01",
            "My workload is going to reduce, regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100031V#2POh, you mean those kiddies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100032V#2PYeah, they're not bad. I see a lotta\x01",
            "potential in 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_END)), "loc_13F7C")

    ChrTalk(
        0x8,
        (
            "#1100033V#2PI trust them far more than those kids in the\x01",
            "Special Support Section, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FCE")

    label("loc_13F7C")


    ChrTalk(
        0x8,
        (
            "#1100034V#2PI bet they're more trustworthy than the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FCE")

    Sleep(150)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    OP_49()
    OP_90(0xB, 0, -500, 47000, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_90(0xD, 0, -500, 47000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(50)
    Sound(1700, 255, 85, 0)

    NpcTalk(
        0xB,
        "Girl's Voice",
        "#1100035V#12A#1P#2SExcuuuuuse us!\x02",
    )

    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x8,
        "#1100036V#6POh, would you speak of the devil?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -4900, 0, 46370, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(-2150, 1100, 49550, 2500)

    def lambda_14131():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14131)
    WaitChrThread(0x8, 1)

    def lambda_1414F():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1414F)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        "#1100037V#5PCome on in! We're upstairs!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Girl's Voice",
        "#1100038V#1P#2SOh, the second floor?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1774, 255, 90, 0)

    NpcTalk(
        0xD,
        "Young Man's Voice",
        "#1100039V#11P#2SThanks for having us.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(1000)
    OP_68(-3310, 900, 49440, 3000)
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(21500, 3000)
    BeginChrThread(0xB, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(500)
    WaitChrThread(0x8, 3)
    Sleep(500)

    NpcTalk(
        0xB,
        "Girl With Twintails",
        "#1100040V#10A#0809F#5PHeya, Michel!\x02",
    )

    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0xB,
        "Girl With Twintails",
        "#1100041V#0805F#11PH-Holy smokes! Arios is here, too?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)

    NpcTalk(
        0xD,
        "Black-Haired Boy",
        "#1100042V#11P#0902FOh, what a relief. I'm glad to see you here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100043V#1404FHaha. It's nothing more than a mere coincidence.\x02\x03",
            "#1100044V#1402FI haven't seen the two of you in about three months,\x01",
            "so it's good to see you're doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100045V#6PI was in for a real shock when I found out that you\x01",
            "were actually transferring to our branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100046V#6PI'm sure glad you two are here. Crossbell's bad boys\x01",
            "are about to get the spanking of a lifetime. ㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14502():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_14502)
    Sleep(100)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(200)

    NpcTalk(
        0xB,
        "Girl With Twintails",
        (
            "#1100047V#0809F#5PAhaha... We may be good, but we're not\x01",
            "THAT good!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Black-Haired Boy",
        "#1100048V#11P#0904FWe'll do our best to live up to your expectations.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Girl With Twintails")

    AnonymousTalk(
        0xFF,
        (
            "#1100049VI think it's time we got down to business.\x02\x03",
            "Estelle Bright, senior bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Black-Haired Boy")

    AnonymousTalk(
        0xFF,
        "#1100050VJoshua Bright. Likewise.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 100, -1, -1)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("Estelle & Joshua")

    AnonymousTalk(
        0xFF,
        (
            "#1100051V\x07\x00",
            "Officially reporting for duty at the\x01",
            "Crossbell branch of the Bracer Guild!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(21250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_1325E end

    def Function_28_1482C(): pass

    label("Function_28_1482C")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_14838():
        OP_95(0xFE, -4900, 0, 46370, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14838)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_28_1482C end

    def Function_29_14877(): pass

    label("Function_29_14877")


    def lambda_1487C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1487C)

    def lambda_1488D():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1488D)
    WaitChrThread(0xB, 1)

    def lambda_148AB():
        OP_95(0xFE, -3200, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_148AB)
    WaitChrThread(0xB, 1)

    def lambda_148C9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_148C9)
    Return()

    # Function_29_14877 end

    def Function_30_148D2(): pass

    label("Function_30_148D2")


    def lambda_148D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_148D7)

    def lambda_148E8():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_148E8)
    WaitChrThread(0xD, 1)

    def lambda_14906():
        OP_95(0xFE, -2400, 0, 49600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_14906)
    WaitChrThread(0xD, 1)

    def lambda_14924():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_14924)
    Return()

    # Function_30_148D2 end

    def Function_31_1492D(): pass

    label("Function_31_1492D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    OP_68(-2000, 1000, 2000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2000, 0, -1000, 0)
    SetChrPos(0xEF, -2000, 0, -1000, 0)
    SetChrPos(0x153, -2000, 0, -1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_149F2():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149F2)

    def lambda_14A0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A0C)
    Sleep(250)

    def lambda_14A20():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_14A20)

    def lambda_14A3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_14A3A)
    Sleep(600)

    def lambda_14A4E():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_14A4E)

    def lambda_14A68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_14A68)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3600252V#0000FExcuse us.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#3600253V#6PWho's there?\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, 11300, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#3600254V#5PMy, oh, my! I was wondering whose voice that was.\x01",
            "It's good to see the SSS in here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600255V#5PDon't be shy now, I'm not gonna bite!\x01",
            "Welcome to the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0xEF, 0, 0, 1900, 0)
    SetChrPos(0x153, -500, 0, 3000, 0)

    def lambda_14BD3():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BD3)
    Sleep(100)

    def lambda_14BF0():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_14BF0)
    Sleep(150)

    def lambda_14C0D():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_14C0D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3600256V#0000FGood afternoon, Michel. Been busy?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_14CB1")

    ChrTalk(
        0x102,
        "#3600257V#12P#0102FWe do apologize for the sudden visit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D50")

    label("loc_14CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_14D12")

    ChrTalk(
        0x103,
        (
            "#3600258V#12P#0202FA considerable time has passed since\x01",
            "our previous meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D50")

    label("loc_14D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_14D50")

    ChrTalk(
        0x104,
        "#3600259V#12P#0300F'Sup, man? Long time no see.\x02",
    )

    CloseMessageWindow()

    label("loc_14D50")


    ChrTalk(
        0x8,
        (
            "#3600260V#5PI'm surprised to see y'all in here. Then again,\x01",
            "Crossbell's been having its fair share of surprises\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600261V#5PTell me, though. Are you guys okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600262V#5PA little birdie told me you guys were being\x01",
            "naughty with Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600263V#0006FI figured you'd already heard about it...\x02\x03",
            "#3600264V#0001FThat mess has been settled...for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    TurnDirection(0x153, 0x101, 400)

    ChrTalk(
        0x153,
        (
            "#3600265V#6P#1100FHey, Lloyd!\x02\x03",
            "#3600266VWhy the heck's this guy talking all funny?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_14F9A():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14F9A)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1500B")

    ChrTalk(
        0x102,
        "#3600267V#12P#0105FK-KeA, that was rude of you...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1508F")

    label("loc_1500B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1504F")

    ChrTalk(
        0x103,
        "#3600268V#12P#0205FThat is not very nice, KeA...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1508F")

    label("loc_1504F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1508F")

    ChrTalk(
        0x104,
        "#3600269V#12P#0305FWhoa, KeDo. Settle down there.\x02",
    )

    CloseMessageWindow()

    label("loc_1508F")

    OP_64(0xEF)
    OP_64(0x101)
    WaitChrThread(0x101, 2)
    Sleep(300)
    OP_93(0x101, 0x0, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600270V#0006FS-Sorry about her, Michel. She's still just a kid,\x01",
            "and she doesn't quite grasp the whole concept\x01",
            "of 'manners' yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600271V#5POhoh, the little kitten has claws. Listen, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600272V#5PEveryone has their own style. Their own moxie.\x01",
            "Their own pizzazz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600273V#5PAnd as for me, little one, I've found that this style\x01",
            "suits me best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600274V#5PJust as that outfit suits you. Simply adorable! Tell\x01",
            "me, does that make sense?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x0, 0x1F4)

    ChrTalk(
        0x153,
        (
            "#3600275V#12P#1105FHmmm, I think so! Thanks, Grampy!\x02\x03",
            "#3600276V#1109FBesides, I like how you talk. It's cute and nice and\x01",
            "super pizzazz-y!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1100)

    ChrTalk(
        0x8,
        "#3600277V#5POh, I like you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600278V#5PHowever, I'm not sure if I quite like 'Grampy...'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600279V#5PI'd much rather you just call me Michel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600280V#12P#1110FOkay! Sorry, Michel.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#3600281V#5PShe's a good one, this girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600282V#5PA friend of yours, I presume?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600283V#0003FWell, about that...\x02\x03",
            "#3600284V#0001FWe actually wanted to talk to the guild\x01",
            "about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600285V#5PUs...?\x02",
    )

    CloseMessageWindow()
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 7600, 1000, 12500, 180)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 7600, 1000, 12500, 180)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(300)
    Sound(1705, 255, 95, 0)
    Sleep(1000)

    NpcTalk(
        0xB,
        "Girl's Voice",
        (
            "#3600286VAre those REQUESTS I hear? The Bracer Guild\x01",
            "is ready...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4000, 1000, 9500, 3000)

    def lambda_155E0():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_155E0)

    def lambda_155FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_155FA)
    Sleep(400)

    def lambda_1560E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1560E)
    Sleep(50)

    def lambda_1561E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_1561E)
    Sleep(50)

    def lambda_1562E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1562E)
    Sleep(50)

    def lambda_1563E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1563E)
    Sleep(100)

    def lambda_1564E():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1564E)

    def lambda_15668():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15668)
    WaitChrThread(0xB, 1)

    def lambda_1567D():
        OP_95(0xFE, 5600, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1567D)
    WaitChrThread(0xD, 1)

    def lambda_1569B():
        OP_95(0xFE, 6000, 0, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1569B)
    WaitChrThread(0xB, 1)

    def lambda_156B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_156B9)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)

    def lambda_156F1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_156F1)
    Sleep(1000)
    OP_6F(0x1)

    ChrTalk(
        0xB,
        "#3600287V#11P#0802F...to help...? Huh? The Special Support Section?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600288V#0000F#6PHey there, you two.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_15814")

    ChrTalk(
        0x102,
        "#3600289V#6P#0109FThanks for your help last week.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600292V#11P#0902FNo problem, but this is rare. You guys\x01",
            "hardly ever visit the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15985")

    label("loc_15814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_158C4")

    ChrTalk(
        0x103,
        "#3600291V#6P#0202FIt has been a while. A week or so, has it not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600290V#11P#0902FI think so, but this is rare. You guys hardly\x01",
            "ever visit the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15985")

    label("loc_158C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_15985")

    ChrTalk(
        0x104,
        (
            "#3600293V#6P#0300FYo. Been about a week since we last\x01",
            "saw each other, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600294V#11P#0902FThat sounds about right, but this is rare.\x01",
            "You guys hardly ever visit the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15985")


    ChrTalk(
        0xB,
        (
            "#3600295V#11P#0809FOooh, ooh, don't tell me! You came here\x01",
            "to hang out with us, right?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#3600296V#11P#0805FHold on a gosh darn second. Who's the kid?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(620, 1000, 9840, 1500)
    MoveCamera(35, 21, 0, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_15A91():

        label("loc_15A91")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_15A91")

    QueueWorkItem2(0x101, 2, lambda_15A91)

    def lambda_15AA3():

        label("loc_15AA3")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_15AA3")

    QueueWorkItem2(0x153, 2, lambda_15AA3)

    def lambda_15AB5():

        label("loc_15AB5")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_15AB5")

    QueueWorkItem2(0x8, 2, lambda_15AB5)

    def lambda_15AC7():
        OP_95(0xFE, 500, 0, 9000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15AC7)
    Sleep(500)

    def lambda_15AE4():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x2260, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_15AE4)
    WaitChrThread(0xB, 1)
    TurnDirection(0xB, 0x153, 800)
    WaitChrThread(0xEF, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x153, 0x2)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#3600297V#12P#0809FOh. My. GODDESS! Who is this sweet bundle\x01",
            "of raw, unadulterated cuteness?!\x02\x03",
            "#3600298V#0802FIs she okay? Do you know her? Can I keep her?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 32)

    ChrTalk(
        0x101,
        (
            "#3600299V#5P#0000FYeah, she's okay. Her name's KeA. And as for the\x01",
            "last question, I'm not sure I can answer that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600300V#1105F#5PI like that your hair keeps jumping up\x01",
            "and down, miss! It looks fun!\x02\x03",
            "#3600301V#1100FAre you one of those bracer people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600302V#12P#0800FYup! I'm Estelle. And this here is Joshua.\x02\x03",
            "#3600303V#0809FKeA, right? Nice to meet'cha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600304V#1109F#5PYou, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600305V#5P#0012FAaaaand they're already best friends.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_15E83")

    ChrTalk(
        0xD,
        (
            "#3600308V#12P#0909FHaha, I'm not shocked. Estelle and kids just\x01",
            "seem to mesh well together. But, y'know...\x02\x03",
            "#3600307V#0900F...I don't know if she's ever been THIS friendly.\x01",
            "Heck, not even when we first met Tita.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F5C")

    label("loc_15E83")


    ChrTalk(
        0xD,
        (
            "#3600306V#12P#0909FHaha, I'm not shocked. Estelle and kids just\x01",
            "seem to mesh well together. But, y'know...\x02\x03",
            "#3600309V#0900F...I don't know if she's ever been THIS friendly.\x01",
            "Heck, not even when we first met Tita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_15FA7")

    ChrTalk(
        0x102,
        "#3600310V#6P#0102FThat sounds in-character for Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1602F")

    label("loc_15FA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_15FE9")

    ChrTalk(
        0x103,
        "#3600311V#6P#0204FShe certainly seems excited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1602F")

    label("loc_15FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1602F")

    ChrTalk(
        0x104,
        "#3600312V#6P#0302FShe's on cloud nine, that's for sure.\x02",
    )

    CloseMessageWindow()

    label("loc_1602F")


    ChrTalk(
        0x8,
        "#3600313V#5PSo, back on topic. You wanted our advice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600314V#5PWhat seems to be the issue? Would the\x01",
            "second floor be more appropriate?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_160C8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_160C8)
    Sleep(100)

    def lambda_160D8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_160D8)
    Sleep(50)
    OP_93(0xEF, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#3600315V#2P#0001FYeah, as long as it's not a hassle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3600316V#12P#0805FAnd it's about her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3600317V#12P#0901FMust be. You seem on edge, Lloyd.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-8200, 900, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    SetChrChipByIndex(0xD, 0x9)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -10700, 150, 49200, 180)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -8400, 150, 49200, 180)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x2)
    OP_52(0x153, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_16270")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    Jump("loc_16297")

    label("loc_16270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_16286")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    Jump("loc_16297")

    label("loc_16286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_16297")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)

    label("loc_16297")

    SetChrPos(0x153, -10900, 200, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47000, 0)
    SetChrPos(0xEF, -6000, 100, 47000, 0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetCameraDistance(19500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xB,
        "#3600318V#5P#0801FN-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600319V#0901F#5PI knew that the Back Alley felt sketchier than\x01",
            "usual this past week, but...who knew?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600320V#11PGoodness gracious. To think that things have\x01",
            "fallen this low...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_164B4")

    ChrTalk(
        0x102,
        (
            "#3600321V#0103F#12PTrust me, we understand. And, representing the\x01",
            "police, policy dictates we accept the reason they\x01",
            "came up with for now.\x02\x03",
            "#3600322V#0101FTry to keep that in mind, please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165A3")

    label("loc_164B4")


    ChrTalk(
        0x101,
        (
            "#3600323V#12P#0003FYeah. And, as representatives of the CPD, policy\x01",
            "dictates we accept the reason Revache came up\x01",
            "with, real or not.\x02\x03",
            "#3600324V#0000FIf possible, I'd like for us to keep that in mind\x01",
            "as we continue our conversation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A3")


    ChrTalk(
        0xB,
        "#3600325V#5P#0801FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600326V#11POh, well. We ARE only consultants in this peculiar\x01",
            "situation, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600327V#11PEven so, taking matters into your own hands and\x01",
            "investigating the Schwarze Auction undercover?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600328V#11PI liked the SSS before, but I respect you now.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3600329V#6P#0002FR-Really? Thanks, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600330V#5P#0806FSame here. We tried so hard to figure out how\x01",
            "to check it out, but we kept hitting roadblocks.\x02\x03",
            "#3600331VAnd you're telling us that it was Renne, of all\x01",
            "people, who gave you the invitation...?\x02\x03",
            "#3600332V#0801FThat little punk...! She could've saved us the\x01",
            "trouble and just given it to us!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    ChrTalk(
        0xD,
        (
            "#3600333V#0904FI'm sure she had her reasons.\x02\x03",
            "#3600334V#0900FShe must just need some time before\x01",
            "she can see us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3600335V#5P#0806FW-Well, be that as it may...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600336V#12P#0008FI'm sorry if we stepped on any toes. I promise\x01",
            "that wasn't our intention.\x02\x03",
            "#3600337V#0003FWe should've contacted you, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600338V#5P#0805FDon't sweat it.\x02\x03",
            "#3600339V#0802FWe're all in the same boat, anyway. I'm\x01",
            "just worried about Renne, that's all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        "#3600340V#11P#0801FBut, yeah. She's a real mystery.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_16ACD")

    ChrTalk(
        0x102,
        "#3600341V#0108F#12PAgreed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B37")

    label("loc_16ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_16AFB")

    ChrTalk(
        0x103,
        "#3600342V#0203F#12PIndeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B37")

    label("loc_16AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_16B37")

    ChrTalk(
        0x104,
        "#3600343V#0303F#12PThat's puttin' it lightly.\x02",
    )

    CloseMessageWindow()

    label("loc_16B37")


    ChrTalk(
        0x153,
        "#3600344V#6P#1110FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600345V#11PNow, Lloyd. I assume you want me to look\x01",
            "into her family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600346V#11PUsing the guild's connections, that is.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600347V#6P#0003FYes, if possible. That's the reason we came.\x02\x03",
            "#3600348V#0000FHow much do you normally charge for\x01",
            "something like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600349V#11PCease your thoughts immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600350V#11PIn cases like these, consider it on the house.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600351V#11PI'll contact our other branches right away and\x01",
            "see what we can dig up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600352V#6P#0002FTh-Thank you!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_16DB3")

    ChrTalk(
        0x102,
        "#3600353V#0105F#12PI was expecting a bit more pushback...\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E6A")

    label("loc_16DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_16E03")

    ChrTalk(
        0x103,
        "#3600354V#0205F#12PThey agreed rather quickly, did they not?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E6A")

    label("loc_16E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_16E6A")

    ChrTalk(
        0x104,
        (
            "#3600355V#0305F#12PWell, shoot. That was a lot easier than\x01",
            "I thought it was going to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E6A")

    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#3600356V#5P#0800FHey, 'Act now and adjust later!' is our\x01",
            "motto when it comes to stuff like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600357V#0904FReally. Don't worry. We have plenty of\x01",
            "funds for these kinds of situations.\x02\x03",
            "#3600358V#0900FDon't hold back on our account, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3600359V#12P#0002FThat's reassuring.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1701E")

    ChrTalk(
        0x102,
        (
            "#3600360V#0102F#12PThe bracers really have their priorities\x01",
            "set when it comes to helping civilians.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170DB")

    label("loc_1701E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1707C")

    ChrTalk(
        0x103,
        (
            "#3600361V#0202F#12PThe Bracer Guild truly does exist to\x01",
            "protect civilians.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170DB")

    label("loc_1707C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_170DB")

    ChrTalk(
        0x104,
        (
            "#3600362V#0300F#12PThese guys are all about helpin' the\x01",
            "public, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170DB")


    ChrTalk(
        0x8,
        (
            "#3600363V#11PIt'll be some time before I hear anything\x01",
            "back, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600364V#11PYou can probably expect an answer\x01",
            "from us in a week or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600365V#12P#0004FThat's perfectly okay. I'm just glad you\x01",
            "were able to help us out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#3600366V#5P#0805FOh, right! If you want, we could totally look\x01",
            "after KeA for you.\x02\x03",
            "#3600367V#0800FFor now, we can pull all her living expenses\x01",
            "from our public protection fund.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600368V#12P#0005FYou can?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600369V#0903FWe'd be more than happy.\x02\x03",
            "#3600370V#0901FBesides, wouldn't she be safer under the\x01",
            "protection of the guild?\x02\x03",
            "#3600371VIf things get dicey, we can always arrange\x01",
            "for her to take shelter outside of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_17412")

    ChrTalk(
        0x102,
        "#3600372V#0108F#12PB-But, that would mean...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17480")

    label("loc_17412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_17454")

    ChrTalk(
        0x103,
        "#3600373V#0208F#12PI follow your logic, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17480")

    label("loc_17454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17480")

    ChrTalk(
        0x104,
        "#3600374V#0306F#12PI dunno...\x02",
    )

    CloseMessageWindow()

    label("loc_17480")


    ChrTalk(
        0x101,
        "#3600375V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600376V#6P#1105FHuh? What's wrong, Lloyd?\x02\x03",
            "#3600377V#1101FDoes your tummy hurt?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600378V#11P#0005FNo, I'm fine, but...\x02\x03",
            "#3600379V#0006F...they have a point. It's extremely possible\x01",
            "that KeA came from somewhere other than\x01",
            "Crossbell.\x02\x03",
            "#3600380V#0008FAnd, putting her safety above all else...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_17601")

    ChrTalk(
        0x102,
        "#3600381V#0108F#11PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17655")

    label("loc_17601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_17630")

    ChrTalk(
        0x103,
        "#3600382V#0208F#11PLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17655")

    label("loc_17630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17655")

    ChrTalk(
        0x104,
        "#3600383V#0308F#11P...\x02",
    )

    CloseMessageWindow()

    label("loc_17655")


    ChrTalk(
        0x153,
        "#3600384V#6P#1100FHmm...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#3600385V#11P#0800F#11PHey, um, KeA?\x02\x03",
            "#3600386VWould you be okay with living with us\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#3600387V#6P#1105FWith you two?\x02\x03",
            "#3600388V#1110FOh, I get it. You want to come live at the\x01",
            "Special Support Section building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600389V#11P#0805FUh, not exactly.\x02\x03",
            "#3600390V#0800FI was actually wondering if you wanted to\x01",
            "move over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600391V#6P#1105FWith Lloyd and everyone, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600392V#11P#0806FNo, sorry. That would be sorta complicated...\x02\x03",
            "#3600393V#0800FBut, they aren't far away! If you ever want to\x01",
            "see them, I could totally walk you over.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    Sound(2030, 255, 90, 0)
    Sleep(1700)
    OP_64(0x153)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#3600394V#6P#5S#1109F#NAbsolutely not.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    Sound(1706, 255, 100, 0)

    ChrTalk(
        0xB,
        "#3600395V#11P#0807F#4SOuch!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x101,
        "#3600396V#11P#0011FKeA...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_17AD0")

    ChrTalk(
        0x153,
        (
            "#3600405V#6P#1108FWho cares about safety? I'm not leaving Lloyd\x01",
            "and everyone else. No matter what.\x02\x03",
            "#3600398V#1103FElie and Tio and Randy and Zeit, even the grumpy\x01",
            "chief! There's no way I'm leaving them.\x02\x03",
            "#3600407V#1101FNope. Not gonna happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3600400V#0102F#11PK-KeA, sweetie... *wipes tears*\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D29")

    label("loc_17AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_17BED")

    ChrTalk(
        0x153,
        (
            "#3600405V#6P#1103FWho cares about safety? I'm not leaving Lloyd\x01",
            "and everyone else. No matter what.\x02\x03",
            "#3600402VElie and Tio and Randy and Zeit, even the grumpy\x01",
            "chief! There's no way I'm leaving them.\x02\x03",
            "#3600407V#1101FNope. Not gonna happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3600404V#0204F#11P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D29")

    label("loc_17BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17D29")

    ChrTalk(
        0x153,
        (
            "#3600405V#6P#1103FWho cares about safety? I'm not leaving Lloyd\x01",
            "and everyone else. No matter what.\x02\x03",
            "#3600406VElie and Tio and Randy and Zeit, even the grumpy\x01",
            "chief! There's no way I'm leaving them.\x02\x03",
            "#3600407V#1101FNope. Not gonna happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3600408V#0304F#11PHaha. I'm speechless, KeDo. Speechless.\x02",
    )

    CloseMessageWindow()

    label("loc_17D29")


    ChrTalk(
        0xB,
        "#3600409V#11P#0809FY-Yeah? That's fine, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3600410V#0904F#5PHaha. I think this might be first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600411V#11PI'll say. I never thought I'd see the\x01",
            "day that Estelle of all people would\x01",
            "be rejected by a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600412V#11PHow EVER are you going to recover\x01",
            "from this one?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#3600413V#5P#0801FI-It's not like I'm shocked or hurt\x01",
            "or extremely sad at all. No, siree.\x02\x03",
            "#3600414V#0806F*sigh* Okay, maybe a little bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600415V#6P#1106FI'm sorry, Estelle. Please don't think I hate\x01",
            "you or anything...\x02\x03",
            "#3600416V#1112FBut, if I don't wanna, I don't wanna.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#3600417V#11P#0809FNo, no, you're right. I was being insensitive.\x02\x03",
            "#3600418V#0802FThe Special Support Section is...well, special.\x01",
            "And if she loves you guys this much, what kind\x01",
            "of monster would I be to tear you all apart?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600419V#12P#0004FHaha. I don't even know when she became\x01",
            "so attached to us.\x02\x03",
            "#3600420V#0000FIt's possible that we remind her of someone\x01",
            "she knows, but given her amnesia...\x02\x03",
            "#3600421V...I'm not sure if that's helpful information.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(150)

    ChrTalk(
        0xD,
        (
            "#3600422V#0903FSomething just hit me.\x02\x03",
            "#3600423V#0900FPerhaps you could go further than just\x01",
            "having Michel look into her identity.\x02\x03",
            "#3600424VDon't you think you should consult with\x01",
            "some sort of expert on amnesia?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3600425V#11P#0005F...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_182C7")

    ChrTalk(
        0x102,
        "#3600426V#0105F#11PAn expert?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18336")

    label("loc_182C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_18308")

    ChrTalk(
        0x103,
        "#3600427V#0205F#11PA specialist of some kind?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18336")

    label("loc_18308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_18336")

    ChrTalk(
        0x104,
        "#3600428V#0305F#11PThat exists?\x02",
    )

    CloseMessageWindow()

    label("loc_18336")


    ChrTalk(
        0xD,
        (
            "#3600429V#0908FWell, assuming her amnesia is related to\x01",
            "something emotional or mental...\x02\x03",
            "#3600430V#0900F...you might want to check out the church.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3600431V#11P#0011FThe church?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1846D")

    ChrTalk(
        0x102,
        "#3600432V#0103F#11PThat's actually a great idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_184E8")

    label("loc_1846D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_184A4")

    ChrTalk(
        0x103,
        "#3600433V#0204F#11PThat might work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_184E8")

    label("loc_184A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_184E8")

    ChrTalk(
        0x104,
        "#3600434V#0302F#11PJoshua might be on to something...\x02",
    )

    CloseMessageWindow()

    label("loc_184E8")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#3600435V#6P#1111FChurch? What church?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600436V#11PThe Septian Church, dear. Modern medicine\x01",
            "might have found its footing in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600437V#11P...but when it comes to matters of the soul,\x01",
            "the good men and women in the church may\x01",
            "be your best option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600438V#11P#0809FFor sure!\x02\x03",
            "#3600439V#0802FThe Bracer Guild gets help from them\x01",
            "all the time!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3600440V#12P#0005FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3600441V#0904FIt's true. They've...definitely helped me through\x01",
            "some rough spots in the past.\x02\x03",
            "#3600442V#0900FOf course, I have no clue whether someone of\x01",
            "that level works at the cathedral, but it still\x01",
            "may be worth the shot.\x02\x03",
            "#3600443VWhy don't you ask over there, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600444V#12P#0004FWe definitely will. Thanks for the advice, guys.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3600445V#11P#0000FHey, KeA.\x02\x03",
            "#3600446VOnce we leave here, I want to head over to the\x01",
            "church. It's a bit of a walk, though. You okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600447V#6P#1104FYep! I'm good to go!\x02\x03",
            "#3600448V#1100FThe church thingy is where you pray to the\x01",
            "Goddess, right?\x02\x03",
            "#3600449V#1109FSounds like fun!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(50)
    SetChrSubChip(0xD, 0x0)
    Sleep(150)

    ChrTalk(
        0xB,
        "#3600450V#11P#0809FSomeone's excited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600451V#11PMy, my. What an energetic kitten.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1000, 0, 12820, 180)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_4C(0x8, 0xFF)
    OP_68(-8400, 1300, 45000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, -8400, 0, 45000, 180)
    SetChrPos(0x1, -8400, 0, 45000, 180)
    SetChrPos(0x2, -8400, 0, 45000, 180)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA8, 0)
    OP_29(0x48, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_31_1492D end

    def Function_32_18AD8(): pass

    label("Function_32_18AD8")


    def lambda_18ADD():
        OP_95(0xFE, 1400, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18ADD)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x13B, 0x1F4)
    Return()

    # Function_32_18AD8 end

    def Function_33_18AFE(): pass

    label("Function_33_18AFE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08700.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    LoadChrToIndex("chr/ch32000.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06000.itp")
    OP_68(-8200, 1600, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, -10700, 100, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47100, 0)
    SetChrPos(0x104, -6000, 100, 47100, 0)
    SetChrPos(0x103, -10700, 150, 49200, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -8400, 150, 49200, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x12, 0x24)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x9,
        (
            "#5100055VI understand. How unfortunate for things\x01",
            "to turn out this way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-8200, 1100, 48300, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5100056V#11PWe were starting to get a lead on the missing\x01",
            "persons case, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100057V#11P...it seems like we were too late\x01",
            "on figuring it out this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100058V#11PWho would have thought the cult\x01",
            "would rear its ugly head again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5100059V#5P#1403F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100060V#12P#0006FSo, Arios. You were involved with the cult\x01",
            "incident that took place six years ago, right?\x02\x03",
            "#5100061V#0013FDo you think there's a possibility that some of the\x01",
            "cultists may have survived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100062V#5P#1403FPossibly.\x02\x03",
            "#5100063V#1401FWe neutralized all of the lodges, but some\x01",
            "members may have survived.\x02\x03",
            "#5100064VIf they sought assistance from a criminal\x01",
            "organization, they could have easily taken\x01",
            "refuge underground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100065V#0208F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100066V#0306F#12PRevache definitely sounds like the most likely\x01",
            "group to have hid their asses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100067V#6P#0106FWhy would they bother engaging in something\x01",
            "that risky, though?\x02\x03",
            "#5100068V#0108FI can't imagine someone as calculating as\x01",
            "Don Marconi didn't feel uneasy about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100069V#11PDefinitely. There are a lot of groups out there that\x01",
            "would take action if they found out that the cult\x01",
            "was still worming their way around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100070V#11PThey'd be dealing with more than just us. The\x01",
            "church and that nefarious society wouldn't\x01",
            "sit still, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100071V#12P#0008FI think I get it...\x02\x03",
            "#5100072V#0001FYou're saying that there are parts to the puzzle\x01",
            "that we haven't pieced together yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100073V#5P#1403FRight. We don't have the time to look into\x01",
            "it right now, though.\x02\x03",
            "#5100074V#1401FWe need to focus our efforts on chasing down the\x01",
            "mafia and locating the missing persons.\x02\x03",
            "#5100075VI'd say there's a high chance that these incidents\x01",
            "are connected with the remaining cultists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100076V#0202F#6PExcuse me, if I may...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100077V#0305F#12PYou sure you wanna cooperate with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100078V#11PYeah, we don't have time to bicker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100079V#11PWe can't just idly stand by while some of our\x01",
            "citizens have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100080V#11PNot to mention, there's the drug-related injuries, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100081V#12P#0004FThanks for helping us out. We hope to be\x01",
            "of use to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100082V#5P#1404FYes, likewise.\x02\x03",
            "#5100083V#1402FNow that we're settled, we should decide\x01",
            "on how we want to partition our duties.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5100084V#1P#1400FPutting aside Estelle and Joshua, what are the\x01",
            "other members doing right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100085V#11PFortunately, Scott and Lynn don't have anything urgent\x01",
            "to tend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100086V#11PSo, including Estelle and Joshua,\x01",
            "that makes seven of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100087V#1P#1403FOkay, please call everyone here.\x02\x03",
            "#5100088V#1401FLet's try and cover any important\x01",
            "locations before the day is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100089V#11PYou got it. I'll go and contact them now.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -5000, 100, 49500, 90)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_1980A():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1980A)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x8, 1)
    StopBGM(0x1F40)

    def lambda_19842():
        OP_95(0xFE, 0, -500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19842)
    Sleep(700)

    def lambda_1985F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1985F)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5100090V#6P#0102FYour coordination never ceases to amaze me...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5100091V#5P#1404FIt's the strongest asset us bracers have. Being\x01",
            "powerful is more than just a numbers game.\x02\x03",
            "#5100092V#1405FCome to think of it, have you briefed Chief\x01",
            "Sergei on the situation?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5100093V#12P#0004FYeah. He's already granted us permission to\x01",
            "cooperate with you.\x02\x03",
            "#5100094V#0000FHe offered his thanks to you, too, Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100095V#5P#1402FIs that so?\x02\x03",
            "#5100096V#1403F...\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(600)
    SetCameraDistance(18800, 60000)
    MoveCamera(42, 19, 0, 60000)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#5100097V#12P#0006FExcuse me, Arios?\x02\x03",
            "#5100098VWeren't you working under the chief when you\x01",
            "were still in the force?\x02\x03",
            "#5100099V#0001F...Alongside my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100100V#5P#1402FI was.\x02\x03",
            "#5100101V#1404FIt was Sergei, Guy, and myself.\x02\x03",
            "#5100102VThe three of us were considered the most\x01",
            "successful team in the history of the force.\x02\x03",
            "We accomplished more than any other group,\x01",
            "including the First Division.\x02\x03",
            "#5100103V#1400FHowever, I quit the force five years ago\x01",
            "due to personal reasons. And with that,\x01",
            "we were no more.\x02\x03",
            "#5100104VSergei went back to the academy, and Guy was\x01",
            "transferred into the First Division.\x02\x03",
            "#5100105V#1403FAnd then, two years later...Guy was killed in\x01",
            "the line of duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100106V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100107V#0208F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100108V#5P#1403FNaturally, I don't intend to speculate what\x01",
            "would have happened if I never quit the force.\x02\x03",
            "#5100109VI had my reasons to leave. I left with the\x01",
            "determination to achieve my own goals.\x02\x03",
            "#5100110V#1402FBut...\x01",
            "Even so, I still reminisce about them.\x02\x03",
            "#5100111VThose were the glory days. I spent the best years\x01",
            "of my life working with an eccentric boss and\x01",
            "a passionate partner.\x02\x03",
            "#5100112V#1404FHaha, look at me rambling like an old man.\x01",
            "To be honest, I'm jealous of your group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100113V#12P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100114V#0302F#12PDidn't think I'd ever hear the Divine Blade\x01",
            "of Wind say that in my lifetime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100115V#6P#0106FIf anything, I'd say we're the ones who should\x01",
            "be jealous of the guild's open atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100116V#5P#1403FThe police have their own duties to perform,\x01",
            "just as the guild has theirs.\x02\x03",
            "#5100117V#1400FIf it's the guild's role to pursue justice\x01",
            "outside the scope of political authority...\x02\x03",
            "#5100118VThen it's the police's job to seek that\x01",
            "same justice, all while burdened with\x01",
            "said authority's many contradictions.\x02\x03",
            "#5100119V#1404FSurely, you've noticed the presence of a\x01",
            "number of contradictions and unreasonable\x01",
            "circumstances placed upon you.\x02\x03",
            "#5100120VYou're not alone. It's something I grappled\x01",
            "with in the past. Bad as it is now, you might\x01",
            "learn much from it, just as I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100121V#0205F#6PPursuing justice while confronting the\x01",
            "contradictions created by those same\x01",
            "political powers. A novel concept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100122V#12P#0013FSo you're saying that my brother chased\x01",
            "after this idea of 'justice' as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100123V#5P#1404FYes, I truly believe that.\x02\x03",
            "#5100124V#1402FThat's precisely why Sergei worked hard to\x01",
            "have the SSS established.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x9,
        (
            "#5100125V#5P#1404FBut, that's enough lecturing from me\x01",
            "for one day.\x02\x03",
            "#5100126V#1402FYou should work hard to find your\x01",
            "own answers.\x02\x03",
            "#5100127VThat's probably what Guy would have\x01",
            "wanted, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100128V#12P#0002FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100129V#0304F#12PDang, now that's what I call a tough assignment.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 0, -500, 47000, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 0, -500, 47000, 0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 0, -500, 47000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    Sleep(300)
    Sound(1707, 255, 90, 0)

    NpcTalk(
        0xB,
        "Girl's Voice",
        "#5100130V#10A#1P#2SWe're baaaaaack!\x02",
    )

    Sleep(800)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)
    Fade(500)
    OP_68(-1000, 900, 49400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    BeginChrThread(0xB, 3, 0, 34)
    BeginChrThread(0xD, 3, 0, 35)
    BeginChrThread(0x14, 3, 0, 36)
    Sleep(1500)
    OP_68(-6600, 900, 49400, 3000)
    MoveCamera(0, 21, 0, 3000)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x14, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5100131V#6P#0002FOh, it's Estelle, Joshua, and Shizuku.\x01",
            "Welcome back, guys.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A819")

    ChrTalk(
        0x102,
        (
            "#5100132V#6P#0102FYour clothes look absolutely\x01",
            "adorable, Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A87D")

    label("loc_1A819")


    ChrTalk(
        0x102,
        (
            "#5100133V#6P#0102FWow! Well, aren't you just wearing the most\x01",
            "adorable clothes today, Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A87D")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x14,
        (
            "#5100134VTeehee, thank you!\x02\x03",
            "#5100135VHi, everyone.\x01",
            "I'm pleased to be with you.\x02",
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
        0x103,
        "#5100136V#0202F#5PI am happy to see you again, Shizuku.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AA76")

    ChrTalk(
        0x104,
        (
            "#5100137V#6P#0309FHaha. Sounds like you enjoyed your\x01",
            "day off, kiddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100138V#1404F#5PI had to deal with some urgent requests, so\x01",
            "Estelle and Joshua accompanied her.\x02\x03",
            "#5100143V#1402FI apologize for putting this on the two of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6F")

    label("loc_1AA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_END)), "loc_1AB88")

    ChrTalk(
        0x104,
        (
            "#5100139V#6P#0309FOh, right. Shizuku did say she was headin'\x01",
            "out today, didn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100142V#1404F#5PYeah, but some last second urgent work came in.\x01",
            "I had them keep her company for me.\x02\x03",
            "#5100143V#1402FI apologize for putting this on the two of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6F")

    label("loc_1AB88")


    ChrTalk(
        0x104,
        "#5100141V#6P#0300FHey, wasn't Shizuku goin' out today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100140V#1404F#5PYeah, but some last second urgent work came in.\x01",
            "I had them keep her company for me.\x02\x03",
            "#5100143V#1402FI apologize for putting this on the two of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC6F")


    ChrTalk(
        0xB,
        (
            "#5100144V#0802F#11PHeheh, it's no biggie.\x02\x03",
            "#5100145V#0809FI had the super rare opportunity to hang out\x01",
            "with sweet little Shizuku!\x02\x03",
            "#5100146VShe even let me squish those adorable\x01",
            "cheeks of hers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5100147V#11P#6010FE-Estelle, you're embarrassing me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100148V#12P#0906FGet a grip, Estelle. You're not some\x01",
            "doting old man.\x02\x03",
            "#5100149V#0901FPutting that aside, I heard the news from\x01",
            "Michel.\x02\x03",
            "#5100150VHe told us that we're making a temporary\x01",
            "alliance with the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100151V#1403F#5PYes, that's right. I'll explain further once the\x01",
            "other members have assembled.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5100152V#5P#1402FLloyd. I'd like for the members of the SSS to\x01",
            "participate, if possible.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5100153V#6P#0000FWe can definitely do that.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Once everyone had assembled, they reviewed\x01",
            "the current situation.\x02\x03",
            "After all of the responsibilities had been divvied\x01",
            "up amongst the group, Lloyd and the others\x01",
            "returned home to the SSS.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_68(-2000, 1400, 3000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2500, 0, 1800, 0)
    SetChrPos(0x102, -1500, 0, 1800, 0)
    SetChrPos(0x103, -3200, 0, 900, 0)
    SetChrPos(0x104, -800, 0, 900, 0)
    SetChrPos(0x14, -2000, 0, 800, 0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2600, 0, 4000, 180)
    SetChrPos(0xB, 600, 0, 4200, 225)
    SetChrPos(0xD, 1200, 0, 3600, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, -1400, 0, 4000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -400, 0, 5500, 180)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -1400, 0, 5800, 180)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -2600, 0, 5500, 180)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, -3600, 0, 5200, 180)
    OP_4B(0x13, 0xFF)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#5100154V#12P#0004FOkay. We'll assume responsibility of Shizuku\x01",
            "and keep her under our care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100155V#12P#0100FChief Sergei and Zeit are usually at the SSS\x01",
            "building. They'll be able to keep watch, so\x01",
            "you needn't worry over her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100156V#1404F#5PRight. I'm counting on you.\x02\x03",
            "#5100157V#1402FBe a good girl and wait for me, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5100158V#12P#6000FYes, Father.\x02\x03",
            "#5100159V#6010FUmm...\x01",
            "Please be careful out there, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5100160V#1404F#5POf course. You don't need to worry about us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100161V#11P#0806FYeah, though it would have been better if\x01",
            "we weren't short-staffed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100162V#0900F#11PShe's right. This place is an open target once we're\x01",
            "all out there investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100163V#12P#0006FAre you sure you guys are fine with this?\x02\x03",
            "#5100164V#0001FIf we're lending you a hand with\x01",
            "your investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5100165V#5PRelax, man. Stop worrying so much.\x02\x03",
            "#5100166V#5PYou're still waiting for a callback from the\x01",
            "hospital, right? Finding out that drug's\x01",
            "composition is important information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5100167V#5PLeave the missing persons to us. You can\x01",
            "start preparing for the next mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5100168V#5PSo we're really teaming up with the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100169V#1PIt's fairly common in Remiferia, but I never\x01",
            "thought I'd see the day in Crossbell.\x02\x03",
            "#5100170VPleased to be working with you, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100171V#12P#0309FNo, ma'am. The pleasure is mine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100172V#12P#0204F#NLikewise.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5100173V#5PIf you run into any trouble, please don't hesitate\x01",
            "to contact us.\x02\x03",
            "#5100174V#5PWe'll be sure to contact you if we learn any\x01",
            "new information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100175V#11P#0800FAll right, everybody. It's time to go out there\x01",
            "and kick some butt!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        "#5100176V#6P#0000FYeah!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_18AFE end

    def Function_34_1B8C1(): pass

    label("Function_34_1B8C1")


    def lambda_1B8C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B8C6)

    def lambda_1B8D7():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B8D7)
    WaitChrThread(0xB, 1)

    def lambda_1B8F5():
        OP_95(0xFE, -4800, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B8F5)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)
    Return()

    # Function_34_1B8C1 end

    def Function_35_1B916(): pass

    label("Function_35_1B916")

    Sleep(600)

    def lambda_1B91E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B91E)

    def lambda_1B92F():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B92F)
    WaitChrThread(0xD, 1)

    def lambda_1B94D():
        OP_95(0xFE, -2700, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B94D)
    WaitChrThread(0xD, 1)

    def lambda_1B96B():
        OP_95(0xFE, -3300, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B96B)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x10E, 0x1F4)
    Return()

    # Function_35_1B916 end

    def Function_36_1B98C(): pass

    label("Function_36_1B98C")

    Sleep(1200)

    def lambda_1B994():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1B994)

    def lambda_1B9A5():
        OP_95(0xFE, 0, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B9A5)
    WaitChrThread(0x14, 1)

    def lambda_1B9C3():
        OP_95(0xFE, -3900, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B9C3)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0xE1, 0x1F4)
    Return()

    # Function_36_1B98C end

    def Function_37_1B9E4(): pass

    label("Function_37_1B9E4")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are a large number of\x01",
            "requests posted for bracers.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BABC")

    ChrTalk(
        0x104,
        (
            "#0305FSmall jobs, weird jobs, even some pretty\x01",
            "important-soundin' jobs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FI can't say I'm surprised.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_1BABC")

    TalkEnd(0xFF)
    Return()

    # Function_37_1B9E4 end

    SaveToFile()

Try(main)

