from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0170.bin",                # FileName
        "c0170",                    # MapName
        "c0170",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0170",                  # 0
        "Receptionist Pearl",     # 1
        "Receptionist Cynthia",   # 2
        "Hanson",                 # 3
        "Gladys",                 # 4
        "Prada",                  # 5
        "Baker",                  # 6
        "Southwark",              # 7
        "Chief Sergei",           # 8
        "Manager Neston",         # 9
        "Janetta",                # 10
        "Baggio",                 # 11
        "Dorothea",               # 12
        "Kean",                   # 13
        "Old Man Honest",         # 14
        "Shanshan",               # 15
        "Rixia",                  # 16
        "Plie",                   # 17
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
        "chr/ch02500.itc",                   # 0A
        "chr/ch32500.itc",                   # 0B
        "chr/ch05200.itc",                   # 0C
        "chr/ch29000.itc",                   # 0D
        "chr/ch34600.itc",                   # 0E
        "chr/ch25900.itc",                   # 0F
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   14,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   15,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(8289,    0,       2460,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(14220,   8000,    21190,   90,   405,  0x0, 0,   11,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(14220,   8000,    22209,   90,   405,  0x0, 0,   12,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   389,  0x0, 0,   13,  0,   0,   0,   0,   28,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  37, 0x0000)
    DeclActor(5790,    0,       9800,    1000,    6620,    1500,    10670,   0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_48C",          # 00, 0
        "Function_1_544",          # 01, 1
        "Function_2_61D",          # 02, 2
        "Function_3_839",          # 03, 3
        "Function_4_8FD",          # 04, 4
        "Function_5_901",          # 05, 5
        "Function_6_189C",         # 06, 6
        "Function_7_18A0",         # 07, 7
        "Function_8_2787",         # 08, 8
        "Function_9_278B",         # 09, 9
        "Function_10_38D1",        # 0A, 10
        "Function_11_38D5",        # 0B, 11
        "Function_12_4DFB",        # 0C, 12
        "Function_13_4DFF",        # 0D, 13
        "Function_14_5DEF",        # 0E, 14
        "Function_15_5DF3",        # 0F, 15
        "Function_16_725D",        # 10, 16
        "Function_17_7261",        # 11, 17
        "Function_18_8804",        # 12, 18
        "Function_19_8A0A",        # 13, 19
        "Function_20_A555",        # 14, 20
        "Function_21_B433",        # 15, 21
        "Function_22_C2E6",        # 16, 22
        "Function_23_CC3C",        # 17, 23
        "Function_24_D4D7",        # 18, 24
        "Function_25_E2B8",        # 19, 25
        "Function_26_E2C2",        # 1A, 26
        "Function_27_E2CC",        # 1B, 27
        "Function_28_E693",        # 1C, 28
        "Function_29_E6FE",        # 1D, 29
        "Function_30_EE0F",        # 1E, 30
        "Function_31_F59C",        # 1F, 31
        "Function_32_FDA6",        # 20, 32
        "Function_33_104CB",       # 21, 33
        "Function_34_10C20",       # 22, 34
        "Function_35_10E8C",       # 23, 35
        "Function_36_1101F",       # 24, 36
        "Function_37_11A13",       # 25, 37
    ))


    def Function_0_48C(): pass

    label("Function_0_48C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4CC"),
        (1, "loc_4D8"),
        (2, "loc_4E4"),
        (3, "loc_4F0"),
        (4, "loc_4FC"),
        (5, "loc_508"),
        (6, "loc_514"),
        (SWITCH_DEFAULT, "loc_520"),
    )


    label("loc_4CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_508")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_514")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_543")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_543")

    Return()

    # Function_0_48C end

    def Function_1_544(): pass

    label("Function_1_544")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61C")
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
    Jump("Function_1_544")

    label("loc_61C")

    Return()

    # Function_1_544 end

    def Function_2_61D(): pass

    label("Function_2_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_64D")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_838")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_688")
    Jump("loc_838")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A7")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6E3")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_6DE")

    Jump("loc_838")

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70C")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_838")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_730")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_760")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrFlags(0x12, 0x80)
    Jump("loc_838")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7B6")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x11, 14040, 8000, 21830, 90)
    Jump("loc_838")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7D5")
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_813")
    SetChrPos(0x11, -5240, 8000, 5490, 0)
    Jump("loc_838")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_821")
    Jump("loc_838")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_82F")
    Jump("loc_838")

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_838")

    label("loc_838")

    Return()

    # Function_2_61D end

    def Function_3_839(): pass

    label("Function_3_839")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_84B")
    Jump("loc_860")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_860")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_66(0x8, 0x1)

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_881")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_88F")

    label("loc_881")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_8FC")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_8FC")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8FC")
    OP_1B(0x0, 0x0, 0x23)

    label("loc_8FC")

    Return()

    # Function_3_839 end

    def Function_4_8FD(): pass

    label("Function_4_8FD")

    Call(0, 5)
    Return()

    # Function_4_8FD end

    def Function_5_901(): pass

    label("Function_5_901")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    TurnDirection(0x0, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_932")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9AD")

    ChrTalk(
        0x8,
        "I'm glad you were able to find it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Remember to stop by Times whenever\x01",
            "you need something, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A34")

    ChrTalk(
        0x8,
        (
            "*sigh* When will Scott take some\x01",
            "time off work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Maybe it's too early to get married, after all...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AFE")

    label("loc_A34")


    ChrTalk(
        0x8,
        (
            "Oh, forgive me! I accidentally got lost in my\x01",
            "thoughts for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you looking for something in particular?\x01",
            "I can help point you in the right direction,\x01",
            "if you're in need of assistance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFE")

    Jump("loc_1898")

    label("loc_B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B87")

    ChrTalk(
        0x8,
        (
            "My shift has only just begun, and I already\x01",
            "feel exhausted. Oh, boy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Good luck with work today, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C51")

    ChrTalk(
        0x8,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We host all kinds of events and sales to\x01",
            "satisfy our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "'Break out a smile and charm every customer!'\x01",
            "That's our manager's motto.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E90")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CFA")

    ChrTalk(
        0x8,
        (
            "Choosing something for your significant other\x01",
            "can be really exciting, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I hope you find that perfect gift.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFC")

    label("loc_CFA")


    ChrTalk(
        0x8,
        (
            "Excuse me, are you by any chance picking out\x01",
            "something for your girlfriend? Wife, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "She must be a lucky girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "W-Wife? N-No, we aren't anywhere near\x01",
            "that level yet! I mean, maybe someday, but\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(This hurts to watch.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DFC")

    Jump("loc_E8B")

    label("loc_E01")


    ChrTalk(
        0x8,
        (
            "Welcome to Times Department Store. Did you\x01",
            "know that the mayor himself likes to frequent\x01",
            "our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmmm, was that too forward?\x02",
    )

    CloseMessageWindow()

    label("loc_E8B")

    Jump("loc_1898")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E9E")
    Jump("loc_1898")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F98")

    ChrTalk(
        0x8,
        (
            "You'd think that someone as beautiful as\x01",
            "Cynthia would always be strutting around\x01",
            "in heels, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...when I saw her commuting to work this\x01",
            "morning, she was just wearing some plain\x01",
            "old sneakers! Isn't that crazy?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1047")

    label("loc_F98")


    ChrTalk(
        0x8,
        (
            "You'd think that someone as beautiful as\x01",
            "Cynthia would always be strutting around\x01",
            "in heels, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Trust me. I assure you she was showing\x01",
            "those sneakers who's boss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")

    Jump("loc_1898")

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_115E")

    ChrTalk(
        0x8,
        (
            "I'm impressed how Neston is able to handle\x01",
            "so many different projects and still function.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You think he's ever been a part of the\x01",
            "Anniversary Festival planning board?\x01",
            "I wouldn't be surprised if he has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Believe me, he's not your standard manager.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_11F1")

    ChrTalk(
        0x8,
        (
            "Oh, is Janetta drooling in the\x01",
            "grocery aisles again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a little childish, but everyone\x01",
            "likes that about her. It's cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_12BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")
    Call(0, 7)
    Jump("loc_12B5")

    label("loc_120C")

    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x8,
        "You know, my fiance's actually a bracer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Only problem is, he can't see me often. But,\x01",
            "he loves me, and I love him. He treats me\x01",
            "like an angel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)

    label("loc_12B5")

    Jump("loc_1898")

    label("loc_12BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_143B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BC")

    ChrTalk(
        0x8,
        (
            "We even keep schedules for train, bus, and\x01",
            "airship services here for your convenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since we get a lot of customers from Erebonia\x01",
            "and Calvard, it helps to keep them on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Feel free to take a look at them, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1436")

    label("loc_13BC")


    ChrTalk(
        0x8,
        (
            "We keep schedules for train, bus, and airship\x01",
            "services here for your convenience.\x01",
            "If you need to see them, just ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1436")

    Jump("loc_1898")

    label("loc_143B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(
        0x8,
        (
            "*sigh* Oh, Scott. I wonder what you're doing\x01",
            "right now...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "P-Pardon me. I should've been paying more\x01",
            "attention to the counter...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1540")

    label("loc_14F6")


    ChrTalk(
        0x8,
        (
            "Please excuse my rudeness. I should have\x01",
            "been paying more attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1540")

    Jump("loc_1898")

    label("loc_1545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_15DB")

    ChrTalk(
        0x8,
        (
            "The manager's been lost in thought\x01",
            "over something for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do you think he might be trying to\x01",
            "plan out a new project?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_15DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1630")

    ChrTalk(
        0x8,
        "Good morning, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you all have\x01",
            "a wonderful day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1898")

    label("loc_1630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DE")

    ChrTalk(
        0x8,
        (
            "Cynthia here is the face of the\x01",
            "Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Her beauty and feminine charms make\x01",
            "her very popular with the girls around town.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1771")

    label("loc_16DE")


    ChrTalk(
        0x8,
        (
            "Cynthia here is the face of the\x01",
            "Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To tell you the truth, the reason I took\x01",
            "this job was because I also admire her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1771")

    Jump("loc_1898")

    label("loc_1776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(
        0x8,
        (
            "Imported foods, western clothes, shoes,\x01",
            "general goods, accessories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We carry all sorts of items, so why not\x01",
            "take your time and browse around?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1898")

    label("loc_182B")


    ChrTalk(
        0x8,
        (
            "We have many specialized stores set\x01",
            "up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have some time, why not go take\x01",
            "a look around?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1898")

    TalkEnd(0x8)
    Return()

    # Function_5_901 end

    def Function_6_189C(): pass

    label("Function_6_189C")

    Call(0, 7)
    Return()

    # Function_6_189C end

    def Function_7_18A0(): pass

    label("Function_7_18A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D1")
    TurnDirection(0x0, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_18D1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_19E2")

    ChrTalk(
        0x9,
        (
            "Our lost and found has been accumulating\x01",
            "a lot of items over time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're supposed to forward them to the\x01",
            "police after a week, but we try to keep\x01",
            "them for much longer than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope all of you make sure to look\x01",
            "out for lost items as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_19E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1A99")

    ChrTalk(
        0x9,
        (
            "Crossbell City draped in the sunset sky\x01",
            "is always beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I love jogging along a scenic route,\x01",
            "but being surrounded by modern\x01",
            "culture isn't so bad, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B5B")

    ChrTalk(
        0x9,
        (
            "Good morning! Welcome to\x01",
            "Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We may have just opened for the day,\x01",
            "but we're all set to serve our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please, go ahead and start\x01",
            "shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_1B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(
        0x9,
        (
            "I can tell from the manager's expression\x01",
            "that he's giddy. He reminds me of a child\x01",
            "that has a new toy to play with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "His face always perks up like that\x01",
            "when he thinks up a new project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm already looking forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D76")

    ChrTalk(
        0x9,
        (
            "We have general goods and imported foods on\x01",
            "the first floor, plus a boutique, a shoe store, and\x01",
            "an accessory shop on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Each of these shops are sure to carry goods\x01",
            "that suit our customers' needs. I'd recommend\x01",
            "paying them a visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E01")

    label("loc_1D76")


    ChrTalk(
        0x9,
        (
            "I heard the manager led projects for\x01",
            "various industries in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's also reputable in the financial and\x01",
            "political spheres.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E01")

    Jump("loc_2783")

    label("loc_1E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1EC3")

    ChrTalk(
        0x9,
        (
            "I enjoyed my time off after the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nothing beats going on a jog\x01",
            "under clear blue skies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps I'll invite Pearl to join\x01",
            "me on my next run.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_200D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(
        0x9,
        (
            "I may not look the part, but I actually\x01",
            "love going on jogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I usually go for a run around the city\x01",
            "on the days I don't work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2008")

    label("loc_1F65")


    ChrTalk(
        0x9,
        (
            "I may not look like it, but I\x01",
            "love to go on jogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I actually bought my sneakers from the\x01",
            "shoe shop on the second floor. I'd\x01",
            "recommend it to all runners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2008")

    Jump("loc_2783")

    label("loc_200D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2102")

    ChrTalk(
        0x9,
        (
            "I used to work at another department\x01",
            "store over in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Neston managed to scout me when he\x01",
            "came to visit, so I moved to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I feel honored to have captured the interest\x01",
            "of someone as talented as Neston.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_2102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2190")

    ChrTalk(
        0x9,
        "The sun has begun to set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We like to broadcast Crossbell's anthem\x01",
            "throughout the store as it approaches\x01",
            "closing time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_2190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_231B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")
    TurnDirection(0x9, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x9,
        (
            "You seem to be caught up in\x01",
            "your worries, Pearl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You must be pretty lonely, right?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Y-Yeah... You know, we've been\x01",
            "engaged for a whole year now!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2316")

    label("loc_2276")


    ChrTalk(
        0x9,
        (
            "Oh, dear... My apologies.\x01",
            "It's unlike me to slip up in front of a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do you need help with anything?\x01",
            "I would be more than happy to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2316")

    Jump("loc_2783")

    label("loc_231B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_23B1")

    ChrTalk(
        0x9,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Are you looking for anything specific?\x01",
            "I can explain the different kinds of shops we have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_23B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_243D")

    ChrTalk(
        0x9,
        (
            "Thank you for shopping at Times\x01",
            "Department Store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please take care to not forget any\x01",
            "belongings in the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_243D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2514")

    ChrTalk(
        0x9,
        (
            "Managing a department store requires you\x01",
            "to be able to hold the customer's attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The manager loves to reiterate this.\x01",
            "I can't wait to see how he plans to\x01",
            "apply this to his next project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_2514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_25B8")

    ChrTalk(
        0x9,
        (
            "Our store ensures that we take the\x01",
            "time to listen to customer opinions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do not hesitate to inform us if you\x01",
            "experience any dissatisfaction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_265A")

    ChrTalk(
        0x9,
        (
            "Thank you for shopping at Times\x01",
            "Department Store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please don't hesitate to tell us your\x01",
            "opinions or requests regarding our service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_265A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2710")

    ChrTalk(
        0x9,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This is the general information desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please don't hesitate to ask us any\x01",
            "questions regarding the store.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2783")

    label("loc_2710")


    ChrTalk(
        0x9,
        "This is the general information desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please don't hesitate to ask us any\x01",
            "questions regarding the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2783")

    TalkEnd(0x9)
    Return()

    # Function_7_18A0 end

    def Function_8_2787(): pass

    label("Function_8_2787")

    Call(0, 9)
    Return()

    # Function_8_2787 end

    def Function_9_278B(): pass

    label("Function_9_278B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_279C")
    Jump("loc_27CA")

    label("loc_279C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_27CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27B6")
    Jump("loc_27CA")

    label("loc_27B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_27CA")
    Call(0, 32)
    TalkEnd(0xA)
    Return()

    label("loc_27CA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38CD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2825")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2844")
    OP_AF(0x22)
    Jump("loc_2846")

    label("loc_2844")

    OP_AF(0x21)

    label("loc_2846")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38C8")

    label("loc_2855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2869")
    Jump("loc_38C8")

    label("loc_2869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_29D5")

    ChrTalk(
        0xA,
        (
            "Man, Prada sure loves a good competition.\x01",
            "She's been hounding me to have another\x01",
            "contest with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Might not be a terrible idea, honestly.\x01",
            "Sounds like a good excuse to sharpen\x01",
            "up my sales techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm going to accept her challenge.\x01",
            "If nothing else, it should at least push\x01",
            "us each to be better shop owners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_29D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A7E")

    ChrTalk(
        0xA,
        (
            "If you aren't used to your shoes, the best\x01",
            "thing you can do is break them in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why buy a new pair of shoes if you're\x01",
            "just going to stare at them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BA2")

    ChrTalk(
        0xA,
        "We handle shoe repairs here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I should mention that it can become costly\x01",
            "to repair older shoes, depending on how\x01",
            "difficult it is to gather the correct materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our service is a hit with people hoping to\x01",
            "cling on to their trusty partners for a\x01",
            "little bit longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_2BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CAF")

    ChrTalk(
        0xA,
        (
            "Kids these days seem to be infatuated with\x01",
            "shoes that have inflated soles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Their ability to absorb impact makes them\x01",
            "well suited for long running sessions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The famous Strega Corporation\x01",
            "also started manufacturing shoes\x01",
            "with inflated soles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_2CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_303B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2D42")

    ChrTalk(
        0xA,
        (
            "Excuse me, ma'am.\x01",
            "Did you select those shoes for that\x01",
            "sweet little child over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYes, we did.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E60")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2DD9")

    ChrTalk(
        0xA,
        (
            "Excuse me, ma'am.\x01",
            "Did you select those shoes for that\x01",
            "sweet little child over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYes, thank you for your assistance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E60")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2E60")

    ChrTalk(
        0xA,
        (
            "Hey, I recognize those shoes.\x01",
            "I believe those two lovely ladies\x01",
            "purchased them earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYeah, we're with 'em.\x02",
    )

    CloseMessageWindow()

    label("loc_2E60")


    ChrTalk(
        0xA,
        (
            "I see. How do they feel, missy? Are they\x01",
            "snug on your feet, or should I have\x01",
            "perhaps suggested a larger size?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FThat's okay. I like how comfy they are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Fantastic.\x01",
            "Don't be afraid to ask me for any further assistance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3036")

    label("loc_2F54")


    ChrTalk(
        0xA,
        (
            "Children grow up quickly. That's why it's important\x01",
            "to purchase shoes that they can adequately\x01",
            "grow into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't be a stranger. Feel free to bless me\x01",
            "with your presence the next time you\x01",
            "shop at the department store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3036")

    Jump("loc_38C8")

    label("loc_303B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30E3")

    ChrTalk(
        0xA,
        (
            "Give a child shoes too tight, and you\x01",
            "might stunt their growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's important to leave a bit of toe room,\x01",
            "rather than aim for the perfect fit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_316B")

    ChrTalk(
        0xA,
        (
            "We have a wide variety of shoes in multiple\x01",
            "sizes for you to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please, feel free to ask me anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_316B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(
        0xA,
        "Thank you for visiting us this evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Are you in a hurry to buy some new shoes?\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_32D2")

    ChrTalk(
        0xA,
        (
            "Have you heard about the sneakers that\x01",
            "emulate the appearance of leather shoes?\x01",
            "They're all the rage these days!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They're convincing enough to be worn in\x01",
            "a professional setting, so businessmen\x01",
            "have been buying them like hotcakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_32D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_33AB")

    ChrTalk(
        0xA,
        (
            "Your occupation has you walking around\x01",
            "all day, so you should treat your feet\x01",
            "to a dependable pair of shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That post-work exhaustion can be\x01",
            "completely nullified with the\x01",
            "right pair of shoes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_33AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3476")

    ChrTalk(
        0xA,
        (
            "Crossbell State celebrates its birthday\x01",
            "with a boisterous event known as the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Businesses of all shapes and sizes face\x01",
            "their busiest periods during that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_3476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_351C")

    ChrTalk(
        0xA,
        (
            "I've been hearing a few rather unpleasant\x01",
            "rumors regarding the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just praying that no tourists get\x01",
            "caught up in their petty actions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_351C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_35E4")

    ChrTalk(
        0xA,
        (
            "A shoe's design often reflects\x01",
            "the designer's personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How many different ways can you present\x01",
            "shoes of a similar manner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My heart skips a beat when I think about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_35E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3717")

    ChrTalk(
        0xA,
        (
            "I used to be a clothes salesman prior to working\x01",
            "here. I only specialize in shoes these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You see Prada at the boutique over there?\x01",
            "She and I used to be business rivals,\x01",
            "back when we owned our own stores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She still challenges me to sales competitions\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_3717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_38C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3820")

    ChrTalk(
        0xA,
        (
            "Welcome. If you're looking for a pair of\x01",
            "shoes, you've come to the right store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Runners, leather shoes, boots...you name it.\x01",
            "We have a wide selection of shoes to satisfy\x01",
            "our customers' every need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Feel free to take a look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38C8")

    label("loc_3820")


    ChrTalk(
        0xA,
        (
            "We plan to sell the Strega Corporation's newest\x01",
            "design when they release it. You'd better act\x01",
            "quickly, or you're sure to miss them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Feel free to take a look.\x02",
    )

    CloseMessageWindow()

    label("loc_38C8")

    Jump("loc_27D4")

    label("loc_38CD")

    TalkEnd(0xA)
    Return()

    # Function_9_278B end

    def Function_10_38D1(): pass

    label("Function_10_38D1")

    Call(0, 11)
    Return()

    # Function_10_38D1 end

    def Function_11_38D5(): pass

    label("Function_11_38D5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_38E6")
    Jump("loc_3914")

    label("loc_38E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3914")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3900")
    Jump("loc_3914")

    label("loc_3900")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3914")
    Call(0, 30)
    TalkEnd(0xB)
    Return()

    label("loc_3914")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_391E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_396F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_396F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398F")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DF2")

    label("loc_398F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A3")
    Jump("loc_4DF2")

    label("loc_39A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A65")

    ChrTalk(
        0xB,
        (
            "We just received a shipment of\x01",
            "fresh vegetables from Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know about you, but nothing\x01",
            "beats the taste of some fresh\x01",
            "veggies for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF2")

    label("loc_3A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B03")

    ChrTalk(
        0xB,
        (
            "Just give me a shout if you can't find\x01",
            "what you're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll try my hardest to stock up on any\x01",
            "veggies you're looking to buy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF2")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3A")

    ChrTalk(
        0xB,
        (
            "My daughter's juice stall has been\x01",
            "flourishing thanks to the nice\x01",
            "weather we've been having.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She doesn't go one day without boasting\x01",
            "about how business is booming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I couldn't be prouder of her, to be honest.\x01",
            "After all, a daughter's happiness is her\x01",
            "mother's happiness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CD0")

    label("loc_3C3A")


    ChrTalk(
        0xB,
        (
            "My daughter wanted to run her own business,\x01",
            "so she opened a juice stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't help but feel that she's in\x01",
            "her element while she runs it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD0")

    Jump("loc_4DF2")

    label("loc_3CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D5D")

    ChrTalk(
        0xB,
        "We just received a large shipment of high-quality produce.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What better chance to enrich your dining experience?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DF2")

    label("loc_3D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E99")

    ChrTalk(
        0xB,
        (
            "The quality of a dish depends on the quality\x01",
            "of the ingredients and the chef's skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Those are all important, but what matters\x01",
            "most to me is thinking of who will eat the\x01",
            "dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, can I interest you in anything?\x01",
            "If you want to cook, you're going\x01",
            "to need some ingredients.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F12")

    label("loc_3E99")


    ChrTalk(
        0xB,
        (
            "Could I interest you with some king potatoes\x01",
            "for tonight's dish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We stocked some particularly\x01",
            "good ones today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F12")

    Jump("loc_4DF2")

    label("loc_3F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4076")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400B")

    ChrTalk(
        0xB,
        (
            "I'm expecting to see a surge of customers,\x01",
            "since the Anniversary Festival is approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if my daughter is doing\x01",
            "a good job of running her business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It'd be embarrassing to be outdone by her.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4071")

    label("loc_400B")


    ChrTalk(
        0xB,
        (
            "It'd be embarrassing for a mother to be\x01",
            "outdone by her daughter, so I'm going\x01",
            "to give it my all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4071")

    Jump("loc_4DF2")

    label("loc_4076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_41BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414E")

    ChrTalk(
        0xB,
        (
            "The trains ran late this morning due to\x01",
            "a cargo inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had to spend the whole morning\x01",
            "sorting through my inventory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ouch, my hips...\x01",
            "I think I'm becoming an old lady.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41B8")

    label("loc_414E")


    ChrTalk(
        0xB,
        (
            "The trains ran late this morning due to\x01",
            "a cargo inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "This happens every once in a while.\x02",
    )

    CloseMessageWindow()

    label("loc_41B8")

    Jump("loc_4DF2")

    label("loc_41BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_425F")

    ChrTalk(
        0xB,
        (
            "It's about time for the post-work rush\x01",
            "hour to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Things are about to get serious.\x01",
            "Just one last push, and we'll be\x01",
            "done for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF2")

    label("loc_425F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_43F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4363")

    ChrTalk(
        0xB,
        (
            "Hmm, looks like we'll need about 30 bottles\x01",
            "of our finest Calvardian wine this week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The Anniversary Festival means more parties, so\x01",
            "the demand for fancy food increases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It'd be smart of me to start ordering\x01",
            "them now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43EB")

    label("loc_4363")


    ChrTalk(
        0xB,
        (
            "The Anniversary Festival means more parties, so\x01",
            "the demand for fancy food increases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Fancy food usually makes a pretty penny.\x02",
    )

    CloseMessageWindow()

    label("loc_43EB")

    Jump("loc_4DF2")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4509")

    ChrTalk(
        0xB,
        (
            "My daughter runs a juice stall\x01",
            "in the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's been boasting about how used\x01",
            "to the job she is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you ask me, she still has a long way\x01",
            "to go. She'll come to learn that the path of a\x01",
            "merchant is a treacherous one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45B7")

    label("loc_4509")


    ChrTalk(
        0xB,
        (
            "I used to manage my own stall, too, so I know all about\x01",
            "the intricacies of running a business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My daughter is doing a good job,\x01",
            "but she still has a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B7")

    Jump("loc_4DF2")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4669")

    ChrTalk(
        0xB,
        "Welcome to Legion's Foods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've got some fresh, juicy acerbic\x01",
            "tomatoes straight from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Would you like one? They're good for\x01",
            "your health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF2")

    label("loc_4669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_48D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482B")

    ChrTalk(
        0xB,
        (
            "One of our customers frequently comes\x01",
            "by to purchase high-quality black tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I believe his name was...Sergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's filled with interesting stories.\x01",
            "We ended up chatting for a full hour today. ㈱\x02",
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
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#0106F(Is this really what you're up to while\x01",
            "we're doing all the work, Chief?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(Unforgivable...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48D1")

    label("loc_482B")


    ChrTalk(
        0xB,
        (
            "Sergei comes by here frequently to\x01",
            "buy high-quality black tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heehee. He's filled with interesting stories.\x01",
            "We ended up chatting for a full hour today. ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D1")

    Jump("loc_4DF2")

    label("loc_48D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A40")

    ChrTalk(
        0xB,
        (
            "There's apparently a torrential downpour on\x01",
            "the Republic's grain-producing region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I should probably buy twenty percent more\x01",
            "Republic-grown vegetables, since they're\x01",
            "increasing the price next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hopefully, it'll ensure that I don't run\x01",
            "out of inventory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wouldn't want to inconvenience\x01",
            "the customers, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AD4")

    label("loc_4A40")


    ChrTalk(
        0xB,
        (
            "You have to pay attention to what's going on\x01",
            "in the rest of the world when you import food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's actually my favorite\x01",
            "part of this job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD4")

    Jump("loc_4DF2")

    label("loc_4AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3B")

    ChrTalk(
        0xB,
        (
            "Welcome to the Times Department Store.\x01",
            "Home of the latest and greatest foodstuffs\x01",
            "in all of Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've got ingredients from all over the continent.\x01",
            "Liberl, Remiferia, the Empire, and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've even got spices from\x01",
            "Ored State!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm still working on expanding the\x01",
            "range of products I can sell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CB7")

    label("loc_4C3B")


    ChrTalk(
        0xB,
        (
            "I actually used to be a trader\x01",
            "back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I always catch myself being giddy\x01",
            "over importing new ingredients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB7")

    Jump("loc_4DF2")

    label("loc_4CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D68")

    ChrTalk(
        0xB,
        "Welcome to Legion's Foods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I deal with a wide variety of\x01",
            "imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, make yourself comfortable\x01",
            "and take a look!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DF2")

    label("loc_4D68")


    ChrTalk(
        0xB,
        (
            "Trains and airships have made it much more\x01",
            "convenient to import ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please, make yourself comfortable\x01",
            "and take a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF2")

    Jump("loc_391E")

    label("loc_4DF7")

    TalkEnd(0xB)
    Return()

    # Function_11_38D5 end

    def Function_12_4DFB(): pass

    label("Function_12_4DFB")

    Call(0, 13)
    Return()

    # Function_12_4DFB end

    def Function_13_4DFF(): pass

    label("Function_13_4DFF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E10")
    Jump("loc_4E3E")

    label("loc_4E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4E3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E2A")
    Jump("loc_4E3E")

    label("loc_4E2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4E3E")
    Call(0, 31)
    TalkEnd(0xC)
    Return()

    label("loc_4E3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DEB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E99")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4E99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4EB8")
    OP_AF(0x1F)
    Jump("loc_4EBA")

    label("loc_4EB8")

    OP_AF(0x1E)

    label("loc_4EBA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DE6")

    label("loc_4EC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EDD")
    Jump("loc_5DE6")

    label("loc_4EDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DE6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4F98")

    ChrTalk(
        0xC,
        (
            "Discovering fashion is like awakening\x01",
            "a revolution inside yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Only those who seek out clothes will\x01",
            "experience this momentous event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_4F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_504E")

    ChrTalk(
        0xC,
        (
            "Whether you want to show off your mature\x01",
            "side or your innocent side, fashion can\x01",
            "do it all for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You can dress to impress without going\x01",
            "beyond your means.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_504E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5144")

    ChrTalk(
        0xC,
        "I love uniforms. They're beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There's an austere beauty to wearing an\x01",
            "outfit perfectly tailored to your duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think the uniforms of the Crossbell Police\x01",
            "Department and the Guardian Force\x01",
            "are highly stylish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5208")

    ChrTalk(
        0xC,
        (
            "Accessorizing your uniform to accent\x01",
            "certain features of it can completely\x01",
            "change its aesthetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You might be able to find the\x01",
            "right accessory over at\x01",
            "Baker's Accessories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_552A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_52A2")

    ChrTalk(
        0xC,
        "Oh. I remember you from earlier, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FHi again. Thanks for helping us\x01",
            "choose out those clothes\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C1")

    label("loc_52A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5330")

    ChrTalk(
        0xC,
        "Oh. I remember you from earlier, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FGreetings. I appreciate your assistance\x01",
            "in selecting a wardrobe earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C1")

    label("loc_5330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_53C1")

    ChrTalk(
        0xC,
        "Oh, aren't those child's clothes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FOh, yeah. Didn't Mademois-Elie and Tio Tot\x01",
            "come here to pick some clothes for KeDo?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C1")


    ChrTalk(
        0xC,
        (
            "Oh, I see. So the clothes were for\x01",
            "the little lady here, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FHeheh. How do I look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It looks great on you, darling.\x01",
            "I'm glad I could help you out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5525")

    label("loc_5472")


    ChrTalk(
        0xC,
        (
            "I'm glad I was able to be of help,\x01",
            "since she seems to adore them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Don't forget about us if you ever need more clothes.\x01",
            "We have a wide assortment of children's clothing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5525")

    Jump("loc_5DE6")

    label("loc_552A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5671")

    ChrTalk(
        0xC,
        (
            "I've heard news about a fancy boutique\x01",
            "opening up shop at Mishelam fairly soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm not afraid of a bit of competition. I'm sure I offer\x01",
            "a greater variety of goods. Not to mention, I've got\x01",
            "the upper hand on location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope to be able to offer my customers\x01",
            "a wider range of styles to choose from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5721")

    ChrTalk(
        0xC,
        (
            "We offer a great selection of formal attire\x01",
            "in addition to our casual wear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We hope to be your number one choice in\x01",
            "dress wear, no matter the occasion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_57EB")

    ChrTalk(
        0xC,
        "Phew... It's almost closing time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I used to overwork myself late into\x01",
            "the night back when I owned my\x01",
            "own business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I think I'm too old to handle that kind of lifestyle now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_57EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_589D")

    ChrTalk(
        0xC,
        (
            "Hanson and I had a fierce rivalry back when\x01",
            "we owned our own businesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now that we operate in different markets,\x01",
            "we haven't had much reason to compete.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_589D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_59A1")

    ChrTalk(
        0xC,
        (
            "Do you prefer durable clothes that are easy to move\x01",
            "in, or a stylish outfit that matches?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Each customer has their own preference, so\x01",
            "the possibilities are endless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's up to you to decide what style\x01",
            "of clothes works best for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_59A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5A1E")

    ChrTalk(
        0xC,
        "Welcome to Lucca Boutique.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Heheh. Business is booming, as per usual.\x01",
            "I hope you all enjoy your stay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5B0E")

    ChrTalk(
        0xC,
        (
            "Back when I first opened my store,\x01",
            "I used to fly all over the continent\x01",
            "to purchase designer goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can order them in now that I've established\x01",
            "a supply route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It was fun back then, though.\x01",
            "I kind of miss it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5C00")

    ChrTalk(
        0xC,
        (
            "Crossbell is home to many different\x01",
            "boutiques, much like this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The great thing about this store is its\x01",
            "ability to bring in smaller brands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope you're able to appreciate the wide\x01",
            "variety of brands we carry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5C95")

    ChrTalk(
        0xC,
        (
            "Crossbell has the power to bring in brand\x01",
            "name products from around the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope you all take your time\x01",
            "to look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D6D")

    ChrTalk(
        0xC,
        "Welcome to Lucca Boutique.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have every style of clothing you\x01",
            "could ever ask for, from children's clothes\x01",
            "to fancy business suits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Do not hesitate to ask me for assistance.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DE6")

    label("loc_5D6D")


    ChrTalk(
        0xC,
        (
            "We have everything from children's clothing\x01",
            "to men's suits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Allow Lucca Boutique to satisfy all of your needs.\x02",
    )

    CloseMessageWindow()

    label("loc_5DE6")

    Jump("loc_4E48")

    label("loc_5DEB")

    TalkEnd(0xC)
    Return()

    # Function_13_4DFF end

    def Function_14_5DEF(): pass

    label("Function_14_5DEF")

    Call(0, 15)
    Return()

    # Function_14_5DEF end

    def Function_15_5DF3(): pass

    label("Function_15_5DF3")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5E04")
    Jump("loc_5E32")

    label("loc_5E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5E32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5E1E")
    Jump("loc_5E32")

    label("loc_5E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5E32")
    Call(0, 33)
    TalkEnd(0xD)
    Return()

    label("loc_5E32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7259")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E8D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5E8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5EAC")
    OP_AF(0x25)
    Jump("loc_5EAE")

    label("loc_5EAC")

    OP_AF(0x24)

    label("loc_5EAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7254")

    label("loc_5EBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ED1")
    Jump("loc_7254")

    label("loc_5ED1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7254")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FBF")

    ChrTalk(
        0xD,
        (
            "I received a call from my septium\x01",
            "supplier saying that my order has\x01",
            "been processed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "All that's left is for it to be shipped out\x01",
            "from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I can't wait for it to finally arrive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_5FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_60CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6079")

    ChrTalk(
        0xD,
        (
            "Gantz? Oh, isn't he\x01",
            "that popular miner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm a little worried. He's been coming here\x01",
            "pretty often, but I haven't seen him around\x01",
            "in a couple of days.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60C8")

    label("loc_6079")


    ChrTalk(
        0xD,
        (
            "Gantz? Oh, isn't he\x01",
            "that popular miner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Did something happen to him?\x02",
    )

    CloseMessageWindow()

    label("loc_60C8")

    Jump("loc_7254")

    label("loc_60CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6192")

    ChrTalk(
        0xD,
        (
            "Gantz has been coming here pretty\x01",
            "regularly, but I haven't seen him\x01",
            "since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He seemed to be making a killing at the casino,\x01",
            "but I'm sure his luck's run out by now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_6192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_628E")

    ChrTalk(
        0xD,
        (
            "A rather wealthy-looking customer\x01",
            "came in a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He'd buy a bunch of accessories\x01",
            "and gift them to the girl that\x01",
            "would accompany him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm a bit ashamed to admit it, but I was\x01",
            "envious of how much he was earning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_628E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_673F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66BB")

    ChrTalk(
        0xD,
        (
            "I recently had a customer by the name of\x01",
            "Toma. He said he was planning on going\x01",
            "to Mishelam for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Turns out, he was planning on proposing to\x01",
            "his girlfriend there, so he purchased an\x01",
            "engagement ring.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_64ED")

    ChrTalk(
        0xD,
        (
            "Toma actually came back to talk to me\x01",
            "before he returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He was able to deliver a wonderful\x01",
            "proposal all thanks to the ring\x01",
            "he purchased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What a joyous occasion! I'm glad I went\x01",
            "the extra selge to engrave their names\x01",
            "into the ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(Sounds like the proposal went perfectly.\x01",
            "I'm glad we were able to help.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66B3")

    label("loc_64ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6670")

    ChrTalk(
        0xD,
        (
            "Toma actually came back to talk to me\x01",
            "before he returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Apparently, he lost the ring I made him,\x01",
            "but the proposal still worked out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm glad everything turned out fine, but\x01",
            "I can't help but feel that I wasted my\x01",
            "time engraving their names into the ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(I guess the proposal worked itself out.\x01",
            "I still wish we could've found the ring.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66B3")

    label("loc_6670")


    ChrTalk(
        0xD,
        (
            "I wish I could have been there to see the\x01",
            "big moment go down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66B3")

    SetScenarioFlags(0x0, 5)
    Jump("loc_673A")

    label("loc_66BB")


    ChrTalk(
        0xD,
        (
            "Ring or no ring, a successful proposal is\x01",
            "a cause for celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I was reminded of the days when I was a youngin'.\x02",
    )

    CloseMessageWindow()

    label("loc_673A")

    Jump("loc_7254")

    label("loc_673F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_68C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681B")

    ChrTalk(
        0xD,
        (
            "Looks like I'll be able to get some new products\x01",
            "aimed towards the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I hope that damned counterfeit dealer\x01",
            "doesn't come again this year and try\x01",
            "to rip anyone off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68BE")

    label("loc_681B")


    ChrTalk(
        0xD,
        (
            "Swindlers always flock to the Anniversary\x01",
            "Festival with counterfeit goods hoping to\x01",
            "pull a fast one on some sucker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I implore you to keep your guard up.\x02",
    )

    CloseMessageWindow()

    label("loc_68BE")

    Jump("loc_7254")

    label("loc_68C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6997")

    ChrTalk(
        0xD,
        (
            "It's almost time to start ordering the new\x01",
            "products aimed towards the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You can never be too careful when you\x01",
            "import accessories. They're an easy\x01",
            "target for smugglers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_6997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6A44")

    ChrTalk(
        0xD,
        (
            "I just remembered that I haven't read the\x01",
            "newest issue of the Crossbell Times yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I suppose I'll head over to Southwark's later\x01",
            "and pick up a copy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_6A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6B10")

    ChrTalk(
        0xD,
        (
            "Whoops, pardon me. I was busy\x01",
            "reading the Crossbell News\x01",
            "Service's business magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "They publish the daily exchange rates\x01",
            "for septium, so I can't help but want\x01",
            "to read up on it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_6B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C2D")

    ChrTalk(
        0xD,
        (
            "I had a trader come by earlier trying to\x01",
            "sell me art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I declined, though. I thought they stank,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I get the impression that anyone who creates\x01",
            "art for the sole purpose of making money\x01",
            "lacks the artistic vision to create great art.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6CF8")

    label("loc_6C2D")


    ChrTalk(
        0xD,
        (
            "Traders these days are too focused on\x01",
            "making a profit. They don't see the intrinsic\x01",
            "value of the goods they sell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "My advice to them is to improve their ability\x01",
            "to discern the quality of goods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF8")

    Jump("loc_7254")

    label("loc_6CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6D7E")

    ChrTalk(
        0xD,
        (
            "Mainz produces some of the most\x01",
            "beautiful septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Their rare quartz in particular fetches\x01",
            "a high price.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_6D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA9")

    ChrTalk(
        0xD,
        (
            "Thinking about the black market\x01",
            "has me feeling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Any piece of art owned by a wealthy person\x01",
            "whose business crashed and burned ends\x01",
            "up eventually going there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how beautiful the art is,\x01",
            "it becomes a part of the wicked\x01",
            "underworld. How sickening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F1E")

    label("loc_6EA9")


    ChrTalk(
        0xD,
        (
            "Thinking about the black market\x01",
            "has me feeling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wish the police would try to\x01",
            "do something about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F1E")

    Jump("loc_7254")

    label("loc_6F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7020")

    ChrTalk(
        0xD,
        (
            "When I hear news about a fine\x01",
            "piece of art, I can hardly\x01",
            "contain myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I went to the art museum in Leman State\x01",
            "to see their celadon porcelain jars the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I wish I could show them to my customers, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_708D")

    label("loc_7020")


    ChrTalk(
        0xD,
        (
            "I have to say, those were some fine\x01",
            "porcelain jars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I wish I could show them to my customers, too.\x02",
    )

    CloseMessageWindow()

    label("loc_708D")

    Jump("loc_7254")

    label("loc_7092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_71AB")

    ChrTalk(
        0xD,
        (
            "I used to run an art museum in the Empire\x01",
            "before I moved here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I got tired of appeasing only the wealthy,\x01",
            "so I opened up an accessory shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I feel much more satisfied doing what I do now.\x01",
            "I can make pieces of art that appeal to the\x01",
            "general population.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7254")

    label("loc_71AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7254")

    ChrTalk(
        0xD,
        (
            "Our humble shop primarily deals in\x01",
            "small accessories and jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't let the price deter you. Every one\x01",
            "of our products is of the highest quality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7254")

    Jump("loc_5E3C")

    label("loc_7259")

    TalkEnd(0xD)
    Return()

    # Function_15_5DF3 end

    def Function_16_725D(): pass

    label("Function_16_725D")

    Call(0, 17)
    Return()

    # Function_16_725D end

    def Function_17_7261(): pass

    label("Function_17_7261")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7272")
    Jump("loc_72A0")

    label("loc_7272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_72A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_728C")
    Jump("loc_72A0")

    label("loc_728C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_72A0")
    Call(0, 29)
    TalkEnd(0xE)
    Return()

    label("loc_72A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8800")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72FB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_72FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_738B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_731A")
    OP_AF(0x1B)
    Jump("loc_737C")

    label("loc_731A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_732A")
    OP_AF(0x1A)
    Jump("loc_737C")

    label("loc_732A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_733A")
    OP_AF(0x19)
    Jump("loc_737C")

    label("loc_733A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_734A")
    OP_AF(0x18)
    Jump("loc_737C")

    label("loc_734A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_735A")
    OP_AF(0x17)
    Jump("loc_737C")

    label("loc_735A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_736A")
    OP_AF(0x16)
    Jump("loc_737C")

    label("loc_736A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_737A")
    OP_AF(0x15)
    Jump("loc_737C")

    label("loc_737A")

    OP_AF(0x14)

    label("loc_737C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87FB")

    label("loc_738B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_739F")
    Jump("loc_87FB")

    label("loc_739F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7491")

    ChrTalk(
        0xE,
        (
            "I managed to book my first vacation in a while, so\x01",
            "I'm going to visit friends and family in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When my merchant friends found out how well\x01",
            "my shop was doing, they were oh-so bitter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_7491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7502")

    ChrTalk(
        0xE,
        "You're trying to find a missing person?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's worrying. Any idea what happened\x01",
            "to them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_7502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_75C6")

    ChrTalk(
        0xE,
        (
            "You can't just pick what to put\x01",
            "in the display case willy-nilly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you haven't thought long and hard about\x01",
            "what appeals to customers, then you've\x01",
            "already lost the battle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_75C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7653")

    ChrTalk(
        0xE,
        "I've been adjusting my lineup bit by bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "There's no better feeling than being\x01",
            "able to satisfy a customer's request.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_7653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_76ED")

    ChrTalk(
        0xE,
        (
            "The amount of business we had during the\x01",
            "Anniversary Festival was fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm looking forward to seeing a fat\x01",
            "bonus this year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_76ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_77EB")

    ChrTalk(
        0xE,
        (
            "My fellow shopkeepers and I have been stocking\x01",
            "up on Anniversary Festival-related goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Pamphlets and other tourist-targeted items\x01",
            "usually sell fairly well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's not unusual to see a corner store\x01",
            "get flooded with customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_77EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_797E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78E5")

    ChrTalk(
        0xE,
        (
            "Seems like Janetta had a bit of a chat with\x01",
            "that large bracer guy this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "She's been acting like that all morning.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0xE,
        "Um, Janetta, have you forgotten about your work?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_7979")

    label("loc_78E5")


    ChrTalk(
        0xE,
        (
            "Well, I have to admit, it is nice having\x01",
            "a bracer around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It'd be nicer if he didn't come and distract\x01",
            "her during business hours, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7979")

    Jump("loc_87FB")

    label("loc_797E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7A1B")

    ChrTalk(
        0xE,
        (
            "Welcome. Are you looking for anything\x01",
            "in particular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We just received the publications for\x01",
            "this month, if you were looking for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_7A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7A90")

    ChrTalk(
        0xE,
        "Janetta is...a bit of a scatterbrain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Her forgetfulness is basically a talent at this point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_87FB")

    label("loc_7A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BAE")

    ChrTalk(
        0xE,
        (
            "Arc en Ciel has announced their\x01",
            "newest play they'll be performing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I believe it was called 'Golden Sun, Silver Moon.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We had tickets up for sale here, but\x01",
            "they sold out on the first day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Can't say I'm surprised, they're extremely popular.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7C30")

    label("loc_7BAE")


    ChrTalk(
        0xE,
        (
            "I feel bad for Janetta, but she's\x01",
            "going to have to put up with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I really wish I could've gotten\x01",
            "one for myself, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C30")

    Jump("loc_87FB")

    label("loc_7C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E1C")

    ChrTalk(
        0xE,
        (
            "This orbal network, or whatever they're\x01",
            "making for these large corporations, has\x01",
            "finally been set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've already been asked a few\x01",
            "times if we have any manuals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe orbal network's technology is still in its\x01",
            "infancy. I do not think you will be able to\x01",
            "find anything other than research papers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I-I assumed that would be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's a shame I couldn't help out that\x01",
            "poor customer, but I can't carry\x01",
            "a book that doesn't exist.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7F6C")

    label("loc_7E1C")


    ChrTalk(
        0xE,
        (
            "I have a professional-dressing customer that\x01",
            "frequently asks me about the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "All he can ever seem to exclaim is that\x01",
            "'It looks useful, but I don't get it at all!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI can understand their struggles. Tio\x01",
            "is the only person in the SSS that has\x01",
            "any sort of proficiency with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYa got that right.\x02",
    )

    CloseMessageWindow()

    label("loc_7F6C")

    Jump("loc_87FB")

    label("loc_7F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B6")

    ChrTalk(
        0xE,
        (
            "Yep, I figured. Most of our sales come\x01",
            "from our books...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I run a general goods store, but I see\x01",
            "far more people coming to buy books\x01",
            "than medicine or sundries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've been receiving a lot of requests to order\x01",
            "books in, too... Looks like I'll have to increase\x01",
            "the shelf space for books.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_815E")

    label("loc_80B6")


    ChrTalk(
        0xE,
        (
            "We sell all sorts of sundries, but most of our\x01",
            "customers are here to purchase books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I suppose I should bring this up with the\x01",
            "manager when I get the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_815E")

    Jump("loc_87FB")

    label("loc_8163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_848F")
    TurnDirection(0xE, 0x104, 0)

    ChrTalk(
        0xE,
        (
            "Well, if it isn't our favorite swimsuit\x01",
            "magazine connoisseur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You haven't missed a week. You're going to put\x01",
            "my future kids through college at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FWhat can I say? I live for the ass and titties.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x103)

    ChrTalk(
        0x102,
        "#0111FI see. So that's the kind of man you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FUh, Randy, don't you think maybe you\x01",
            "shouldn't bring that up in front of Elie an--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FWhat was that? My best pal Lloyd wants\x01",
            "me to hook him up with the sickest mags?\x02\x03",
            "#0300FHaha. Anythin' for you, my man.\x01",
            "I'll give 'em to ya later.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0011FOh, no. No, no, no!\x01",
            "You know for a fact that wasn't what I was saying.\x01",
            "Don't you dare drag me into this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F*stare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "A-Ahaha...maybe I should've kept quiet.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 6)
    Jump("loc_852D")

    label("loc_848F")


    ChrTalk(
        0xE,
        (
            "You know, there are actually a lot of people who\x01",
            "accidentally forget their belongings here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Take care to not forget any of your belongings, either.\x02",
    )

    CloseMessageWindow()

    label("loc_852D")

    Jump("loc_87FB")

    label("loc_8532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_86CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8616")

    ChrTalk(
        0xE,
        (
            "Hey, did you know the Crossbell Times\x01",
            "building used to be in Central Square?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The origin of this department store's name, Times,\x01",
            "is actually based on how Central Square was once\x01",
            "Times Square.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_86C7")

    label("loc_8616")


    ChrTalk(
        0xE,
        (
            "The origin of this department store's name, Times,\x01",
            "is actually based on how Central Square was once\x01",
            "Times Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I can only imagine how influential the location was.\x02",
    )

    CloseMessageWindow()

    label("loc_86C7")

    Jump("loc_87FB")

    label("loc_86CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_87FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875D")

    ChrTalk(
        0xE,
        "Welcome to Southwark General Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Feel free to browse my wares. I sell the\x01",
            "Crossbell Times and much more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87FB")

    label("loc_875D")


    ChrTalk(
        0xE,
        (
            "It's not too surprising that our hottest\x01",
            "seller is the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A lot of the citizens have their noses\x01",
            "buried deep into the business world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87FB")

    Jump("loc_72AA")

    label("loc_8800")

    TalkEnd(0xE)
    Return()

    # Function_17_7261 end

    def Function_18_8804(): pass

    label("Function_18_8804")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8967")

    ChrTalk(
        0x104,
        "#0300FHey, what's the chief doin' here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FUh, Chief? What happened to your work?\x02\x03",
            "Weren't you devising a plan to deceive the\x01",
            "First Division and management?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1000FDon't worry about it. I'm planning it all out\x01",
            "inside of my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYour statement fails to carry any persuasive power.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8A06")

    label("loc_8967")


    ChrTalk(
        0xF,
        (
            "#1003FInvestigate at your own discretion and do as you\x01",
            "see fit.\x02\x03",
            "#1000FDo me a favor and file a report for me later, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FUnderstood, Chief.\x02",
    )

    CloseMessageWindow()

    label("loc_8A06")

    TalkEnd(0xFE)
    Return()

    # Function_18_8804 end

    def Function_19_8A0A(): pass

    label("Function_19_8A0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F1E")

    ChrTalk(
        0x10,
        (
            "Good afternoon. Welcome to Times\x01",
            "Department Store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9C")

    ChrTalk(
        0x10,
        "Oh, if it isn't Miss Elie!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AE4")

    label("loc_8A9C")

    TurnDirection(0x10, 0x102, 500)

    ChrTalk(
        0x10,
        "Oh, aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Miss Elie! I knew I recognized you.\x02",
    )

    CloseMessageWindow()

    label("loc_8AE4")


    ChrTalk(
        0x10,
        (
            "Thank you very much for gracing us\x01",
            "with your presence today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B46")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_8B46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B66")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_8B66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B86")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_8B86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BA6")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_8BA6")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FM-Miss Elie? What's that all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOh, well, you see...\x02\x03",
            "My grandfather and Neston are longtime\x01",
            "acquaintances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Miss Elie's been a precious client for this\x01",
            "store ever since she was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FShe is given VIP treatment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FHah, I knew it! She's a spoiled princess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0112FCut it out, you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "By the way, Miss Elie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I heard that you were looking for employment\x01",
            "within the CPD after returning from your\x01",
            "studies abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThat's correct. I'm a police officer now.\x02\x03",
            "#0108FI'd appreciate it if you'd avoid giving me\x01",
            "special treatment when I shop here.\x02\x03",
            "#0106FI know I'm being selfish, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Oh, my apologies. I will respect your\x01",
            "wishes, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That won't change the fact that you'll always\x01",
            "be an important customer in my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Please do not ever hesitate to bring any\x01",
            "problems to my attention.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_8F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FC6")

    ChrTalk(
        0x101,
        (
            "#0000F(The Times Department Store... This\x01",
            "is one of the locations Tront visited.\x01",
            "He may have lost his belongings here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_8FC6")


    ChrTalk(
        0x101,
        (
            "#0000FExcuse me, sir. Do you happen\x01",
            "to have a lost and found here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you inquiring about a lost item?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please go to the information desk.\x01",
            "They'll be able to help you with your\x01",
            "inquiry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_9093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9149")

    ChrTalk(
        0xFE,
        (
            "Looks like you guys managed to find whatever\x01",
            "it was that you were looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm happy for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We hope to see you at the Times Department\x01",
            "Store again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_9149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9249")

    ChrTalk(
        0xFE,
        (
            "Sales have been stable recently,\x01",
            "so I feel like I can relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be that as it may, it is my duty to develop\x01",
            "new methods of appealing to our patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The plan I'm cooking up now is\x01",
            "quite the work of art. Please look\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_934D")

    ChrTalk(
        0xFE,
        (
            "Satisfying the customers and giving them\x01",
            "a relaxing environment is the mission\x01",
            "statement of Times Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our staff have trained under a regimen\x01",
            "based on my own experiences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope you have a pleasant time\x01",
            "shopping here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_934D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_93FD")

    ChrTalk(
        0xFE,
        (
            "I was struck by inspiration for a new sales\x01",
            "strategy when I woke up this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You never know when or where the\x01",
            "next spark of inspiration will come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_93FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_97CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94EC")

    ChrTalk(
        0xFE,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please ask the clerks for assistance if you\x01",
            "are having trouble deciding on an item.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They'll be more than happy to explain\x01",
            "the products in detail for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97C6")

    label("loc_94EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F4")

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell praised me for my\x01",
            "management skills a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This department store shares history with\x01",
            "the area, so he wishes for it to continue\x01",
            "being a part of the citizens' lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI appreciate your modesty, Neston.\x01",
            "You never fail to place the customer's\x01",
            "needs above all.\x02\x03",
            "It appears my grandfather's praise hit\x01",
            "the mark. I hope you strive for your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're too kind, Miss Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that I'm able to allow this store to\x01",
            "live up to everyone's expectations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_97C6")

    label("loc_96F4")


    ChrTalk(
        0xFE,
        (
            "I've been acquainted with Mayor MacDowell\x01",
            "for a while, but when I heard those words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...my body tensed up completely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray I am able to let this department store\x01",
            "live up to its expectations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C6")

    Jump("loc_A551")

    label("loc_97CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_99CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9931")

    ChrTalk(
        0xFE,
        (
            "It's been quite a long time since I first\x01",
            "entered this business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I try to think of new ways to liven up\x01",
            "the store on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like to recall experiences from my younger\x01",
            "days and apply them to my planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I treasure the days in which I'd recklessly\x01",
            "try anything without thinking about\x01",
            "the consequences.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_99C7")

    label("loc_9931")


    ChrTalk(
        0xFE,
        (
            "I like to recall experiences from my younger\x01",
            "days and apply them to my planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The amount of experiences I had\x01",
            "in my youth is a blessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C7")

    Jump("loc_A551")

    label("loc_99CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B3B")

    ChrTalk(
        0xFE,
        (
            "Are you acquainted with Mishy,\x01",
            "Mishelam's historic mascot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the local mascot that's been around ever\x01",
            "since Mishelam was a wellness resort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mishy's popularity surged once the\x01",
            "theme park was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm planning a collaboration event\x01",
            "featuring Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Tio's eyes are sparkling at the idea...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9BB8")

    label("loc_9B3B")


    ChrTalk(
        0xFE,
        (
            "Times is planning a collaboration event\x01",
            "featuring Mishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love for you all to come by once\x01",
            "we open the exhibit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BB8")

    Jump("loc_A551")

    label("loc_9BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9CC3")

    ChrTalk(
        0xFE,
        (
            "I'm slowly but surely working through the\x01",
            "plan for our newest event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to contact the\x01",
            "sponsors for their agreement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please keep an eye out for any future\x01",
            "developments. There'll be an\x01",
            "announcement when we're ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9D22")

    ChrTalk(
        0xFE,
        "We are open until 8PM.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you have a relaxing time while you shop.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9E25")

    ChrTalk(
        0xFE,
        (
            "All of the shops here in Times are outstanding.\x01",
            "I personally scouted each one of them from\x01",
            "Crossbell and neighboring countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can rest easy knowing I've employed\x01",
            "the best of the best when I see all of\x01",
            "our customers' smiling faces.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9EF8")

    ChrTalk(
        0xFE,
        "Welcome to Times Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please speak to the receptionist at\x01",
            "the information desk regarding any\x01",
            "inquiries about the stores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you have a relaxing time while you shop.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9F33")

    ChrTalk(
        0xFE,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, enjoy yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A551")

    label("loc_9F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A07B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A00D")

    ChrTalk(
        0xFE,
        (
            "Hmm, quite a lot of time has passed already\x01",
            "since we had the grand reopening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suspect our customers will soon\x01",
            "lose interest in us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If only I had a few tricks up my sleeve...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A076")

    label("loc_A00D")


    ChrTalk(
        0xFE,
        (
            "It's been quite some time since the\x01",
            "grand reopening. Aren't there any\x01",
            "new ideas I can come up with?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A076")

    Jump("loc_A551")

    label("loc_A07B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A22B")

    ChrTalk(
        0x102,
        "#0100FGood morning, Neston.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, hello everyone. Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you headed off somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYes... I'm amazed you can tell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be in the business for as long as I've been,\x01",
            "and you learn to recognize these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know what they say. You'd rather\x01",
            "have it and not need it, than need it\x01",
            "and not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Prepare well, and please make sure\x01",
            "you don't forget anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 7)
    Jump("loc_A273")

    label("loc_A22B")


    ChrTalk(
        0xFE,
        (
            "Please make sure you don't\x01",
            "forget anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have a safe trip.\x02",
    )

    CloseMessageWindow()

    label("loc_A273")

    Jump("loc_A551")

    label("loc_A278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A3F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A374")

    ChrTalk(
        0xFE,
        (
            "I'm sure you're aware, but we completely\x01",
            "remodeled the store last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The aesthetic of this area has rapidly\x01",
            "changed in the last few years, so\x01",
            "we tried to match it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope our services will always\x01",
            "be of use.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A3F2")

    label("loc_A374")


    ChrTalk(
        0xFE,
        (
            "This store was completely remodeled to\x01",
            "match the aesthetics of the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope our services will always\x01",
            "be of use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F2")

    Jump("loc_A551")

    label("loc_A3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D7")

    ChrTalk(
        0xFE,
        (
            "This department store is home to many\x01",
            "different kinds of shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you each and every one of them\x01",
            "provide the highest quality of service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you all have a wonderful time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A551")

    label("loc_A4D7")


    ChrTalk(
        0xFE,
        (
            "This department store is home to\x01",
            "shops with the highest quality\x01",
            "of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you all have a wonderful time.\x02",
    )

    CloseMessageWindow()

    label("loc_A551")

    TalkEnd(0xFE)
    Return()

    # Function_19_8A0A end

    def Function_20_A555(): pass

    label("Function_20_A555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A5F2")

    ChrTalk(
        0xFE,
        (
            "I've been coming here pretty often in the\x01",
            "evening, despite not being on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohh, that smells good...\x01",
            "Now I'm getting hungry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42F")

    label("loc_A5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A76E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6F9")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Time to clean...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "*sigh* I slept in late yesterday, so now they're\x01",
            "forcing me to do some heavy-duty cleaning\x01",
            "as punishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still have to clean the warehouse after this.\x01",
            "*sigh* Today's going to be rough...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A769")

    label("loc_A6F9")


    ChrTalk(
        0xFE,
        (
            "This is all because my alarm clock\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I wonder if I'll be able to\x01",
            "get a new one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A769")

    Jump("loc_B42F")

    label("loc_A76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A82B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A802")

    ChrTalk(
        0xFE,
        "*yawn* I slept in today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's not my fault, though, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My alarm clock stopped working\x01",
            "all of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A826")

    label("loc_A802")


    ChrTalk(
        0xFE,
        "*yawn* I'm still soooo sleepy.\x02",
    )

    CloseMessageWindow()

    label("loc_A826")

    Jump("loc_B42F")

    label("loc_A82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A964")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A898")

    ChrTalk(
        0xFE,
        "Feel free to browse our wares!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Window shopping is A-OK with me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A95F")

    label("loc_A898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A946")

    ChrTalk(
        0xFE,
        "I'm working as quickly as I can!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've been busting my hump lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing else I can do if I want\x01",
            "to catch up to Cynthia and Pearl!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A95F")

    label("loc_A946")


    ChrTalk(
        0xFE,
        "You got this, girl!\x02",
    )

    CloseMessageWindow()

    label("loc_A95F")

    Jump("loc_B42F")

    label("loc_A964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AA2D")

    ChrTalk(
        0xFE,
        (
            "I've had a lot more free time on my hands\x01",
            "ever since the Anniversary Festival ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's not a problem with me, though.\x01",
            "I love me some free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I like taking it easy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B42F")

    label("loc_AA2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_AAA7")

    ChrTalk(
        0xFE,
        (
            "I always get excited as the Anniversary\x01",
            "Festival approaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heheh. What fun awaits me this year?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B42F")

    label("loc_AAA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_ABBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB72")

    ChrTalk(
        0xFE,
        "Bracers sure are cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bracer came here to escort\x01",
            "a lost child home the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you think he'd escort me away, too?\x01",
            "J-Just kidding, haha... Unless...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ABB7")

    label("loc_AB72")


    ChrTalk(
        0xFE,
        "Bracers sure are cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I'll try getting lost, too.\x02",
    )

    CloseMessageWindow()

    label("loc_ABB7")

    Jump("loc_B42F")

    label("loc_ABBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_AC19")

    ChrTalk(
        0xFE,
        "*sigh* I'm huuuungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just wanna go home early and\x01",
            "eat everything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42F")

    label("loc_AC19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_ACD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC89")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Oh, these western-looking clothes are nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want some for myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ACCF")

    label("loc_AC89")


    ChrTalk(
        0xFE,
        (
            "This is the newest model... I kind of\x01",
            "want to buy it for myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACCF")

    Jump("loc_B42F")

    label("loc_ACD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AFBD")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF11")

    ChrTalk(
        0xFE,
        "You there! Please listen to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I begged Southwark to save\x01",
            "some Arc en Ciel tickets\x01",
            "for me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He told me that they're all sold out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought I coulda scored them pretty easily,\x01",
            "since I work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, sorry about that. There's a protocol\x01",
            "I have to follow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wasn't able to buy any for myself, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Don't feel too bad about it, Janetta. I'll\x01",
            "make it up to you later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Really?\x01",
            "Fine. Take me on a date, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "S-Sure. Is that really all you want, though?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AFB4")

    label("loc_AF11")

    OP_93(0xFE, 0x2D, 0x0)

    ChrTalk(
        0xFE,
        "Wahhhhh! I really wanted those tickets...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're such a dummy, Southwark!\x01",
            "Please take me out on a date!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "No need to get desperate, Janetta...\x02",
    )

    CloseMessageWindow()

    label("loc_AFB4")

    OP_4C(0xE, 0xFF)
    Jump("loc_B42F")

    label("loc_AFBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B0D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B09E")

    ChrTalk(
        0xFE,
        (
            "Cynthia and Pearl always look like\x01",
            "they're in sync.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It almost feels like they can read\x01",
            "each other's minds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I wonder if veterans operate on\x01",
            "a different wavelength or something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B0CC")

    label("loc_B09E")


    ChrTalk(
        0xFE,
        "I need to hurry up and catch up to them.\x02",
    )

    CloseMessageWindow()

    label("loc_B0CC")

    Jump("loc_B42F")

    label("loc_B0D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B1E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B19C")

    ChrTalk(
        0xFE,
        (
            "The owner of this shop likes to dust off\x01",
            "the silverware in his spare time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention, he looks like he has a grand old time\x01",
            "doing it. Isn't that kinda weird...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B1DC")

    label("loc_B19C")


    ChrTalk(
        0xFE,
        (
            "The owner of this shop seems like a bit\x01",
            "of a weirdo to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1DC")

    Jump("loc_B42F")

    label("loc_B1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B2D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2AC")

    ChrTalk(
        0xFE,
        (
            "I showed a couple of bracers around\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a young man and lady. I kinda got\x01",
            "the impression that they were dating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Boy, am I jealous.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B2D2")

    label("loc_B2AC")


    ChrTalk(
        0xFE,
        "I wish I had a boyfriend, too...\x02",
    )

    CloseMessageWindow()

    label("loc_B2D2")

    Jump("loc_B42F")

    label("loc_B2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B348")

    ChrTalk(
        0xFE,
        (
            "Cynthia's amazing, and Pearl is stunningly\x01",
            "beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I want to become like them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B42F")

    label("loc_B348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B42F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3E5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        "Whoa, he's so cool...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Ahem. Forget I said anything.\x01",
            "Feel free to take a look around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B42F")

    label("loc_B3E5")


    ChrTalk(
        0xFE,
        "I-I help take care of sales here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "P-Please, take a look around.\x02",
    )

    CloseMessageWindow()

    label("loc_B42F")

    TalkEnd(0xFE)
    Return()

    # Function_20_A555 end

    def Function_21_B433(): pass

    label("Function_21_B433")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B4AD")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops, that was close!\x01",
            "I almost read this book in its entirety\x01",
            "while I was standing here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_B4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B620")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B586")

    ChrTalk(
        0xFE,
        "Oh, there it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This reference book is pricy, but my\x01",
            "parents gave me the money to\x01",
            "purchase it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been feeling pretty down since I failed\x01",
            "my exam, but now I'm cheering up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B61B")

    label("loc_B586")


    ChrTalk(
        0xFE,
        (
            "All right, then. Once I read through\x01",
            "this book and become a doctor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'll have to pay back the mira I borrowed,\x01",
            "first of all. Haha.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B61B")

    Jump("loc_C2E2")

    label("loc_B620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B735")

    ChrTalk(
        0xFE,
        (
            "My parents made me take care of the\x01",
            "shopping again, but...I always feel like\x01",
            "a kid in a candy store here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really gotta get my hands on that reference\x01",
            "book I found here the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think it's worth it to beg my\x01",
            "parents to give me the mira?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_B735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B89C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7D7")

    ChrTalk(
        0xFE,
        (
            "My parents always make me come here\x01",
            "to take care of the shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm still ashamed that I failed\x01",
            "the entrance exam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B897")

    label("loc_B7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B851")

    ChrTalk(
        0xFE,
        "Oh, they released a new reference book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's take a look inside...\x01",
            "Oh, this one looks great!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B897")

    label("loc_B851")


    ChrTalk(
        0xFE,
        "Man, I really want this book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's outta my budget, though.\x02",
    )

    CloseMessageWindow()

    label("loc_B897")

    Jump("loc_C2E2")

    label("loc_B89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BA17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9BA")

    ChrTalk(
        0xFE,
        "Lemme see what I was supposed to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FHi! Are you doing errands or something?\x01",
            "That's pretty nice of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I failed my entrance exam.\x01",
            "This is the least I could do, or else I'd feel useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Saying it out loud made me sad again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BA12")

    label("loc_B9BA")


    ChrTalk(
        0xFE,
        (
            "I failed my entrance exam.\x01",
            "This is the least I could do, or else I'd feel useless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA12")

    Jump("loc_C2E2")

    label("loc_BA17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BA70")

    ChrTalk(
        0xFE,
        (
            "Doesn't look like there are any new\x01",
            "reference books on display today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_BA70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BBC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB43")

    ChrTalk(
        0xFE,
        (
            "I'm going to become a doctor, damn it!\x01",
            "I'll keep retaking the entrance exams,\x01",
            "no matter how many times it takes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're unbelievably difficult, so I'm\x01",
            "still trying to pass.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BBC3")

    label("loc_BB43")


    ChrTalk(
        0xFE,
        "*sigh* Life is tough in this state.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't do much for my family, so running\x01",
            "errands for them is the least I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBC3")

    Jump("loc_C2E2")

    label("loc_BBC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_BCFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC88")

    ChrTalk(
        0xFE,
        (
            "My sister, Cirone, is a nurse at\x01",
            "St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I dunno how a klutz like her managed to\x01",
            "pull off working at a prestigious hospital\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BCF8")

    label("loc_BC88")


    ChrTalk(
        0xFE,
        (
            "Well, Cirone has always had incredible\x01",
            "luck for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oops, I'd better get back to shopping.\x02",
    )

    CloseMessageWindow()

    label("loc_BCF8")

    Jump("loc_C2E2")

    label("loc_BCFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BE2C")

    ChrTalk(
        0xFE,
        (
            "My parents are making me take care of\x01",
            "all the shopping, yet they couldn't spare\x01",
            "me a single mira of extra spending money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They gave me the exact amount needed\x01",
            "to cover the shopping list, so I can't buy\x01",
            "myself a little extra.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hate having parents that are this\x01",
            "calculating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_BE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BE82")

    ChrTalk(
        0xFE,
        (
            "Oh, cool. Some new books came in.\x01",
            "Let's see what we've got here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_BE82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C00F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7C")

    ChrTalk(
        0xFE,
        (
            "My sister is a nurse at\x01",
            "St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have you met her? Her name\x01",
            "is Cirone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My parents are forcing me to visit her\x01",
            "later, but I honestly couldn't be looking\x01",
            "forward to it any less. What a pain.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C00A")

    label("loc_BF7C")


    ChrTalk(
        0xFE,
        (
            "My sister is a nurse at\x01",
            "St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a colossal scatterbrain, so my\x01",
            "parents are constantly worrying\x01",
            "about her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C00A")

    Jump("loc_C2E2")

    label("loc_C00F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_C0D1")

    ChrTalk(
        0xFE,
        "I got forced into doing the shopping again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only wanted to look for a book to help me\x01",
            "with my studies, but my family roped me\x01",
            "into doing ALL of the grocery shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_C0D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_C1C3")

    ChrTalk(
        0xFE,
        (
            "You always find yourself coming back here,\x01",
            "since department stores have such a wide\x01",
            "variety of goods to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the impression that a lot more people\x01",
            "have been coming here since last year's\x01",
            "grand reopening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2E2")

    label("loc_C1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_C2E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29A")

    ChrTalk(
        0xFE,
        "Sugar, flour, and onion sauce...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This shop has a great selection of goods\x01",
            "to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm trying to buy some sugar, but they have\x01",
            "36 different varieties to choose from.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C2E2")

    label("loc_C29A")


    ChrTalk(
        0xFE,
        (
            "How is anyone other than a chef supposed\x01",
            "to know which one to buy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2E2")

    TalkEnd(0xFE)
    Return()

    # Function_21_B433 end

    def Function_22_C2E6(): pass

    label("Function_22_C2E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C366")

    ChrTalk(
        0xFE,
        "Oh, my. The sun has already set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't decided on what to make for dinner\x01",
            "tonight. What do I do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C3E7")

    ChrTalk(
        0xFE,
        (
            "I actually came here right at opening, today.\x01",
            "There's nothing more refreshing than a bit of\x01",
            "morning shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C441")

    ChrTalk(
        0xFE,
        "It's time to shop until I drop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to buy whatever I want!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C555")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C4")

    ChrTalk(
        0xFE,
        "I love taking a stroll around the department store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I could do this for hours on end!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C550")

    label("loc_C4C4")


    ChrTalk(
        0xFE,
        "My husband gets paid tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm scoping out the area for anything interesting.\x01",
            "I'm going to come back tomorrow and buy it all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C550")

    Jump("loc_CC38")

    label("loc_C555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C5A8")

    ChrTalk(
        0xFE,
        "*shuffle* *shuffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Phew! I could never get tired of this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C5FE")

    ChrTalk(
        0xFE,
        (
            "Hey, you! You look like you wanna join me\x01",
            "in some window shopping!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C67F")

    ChrTalk(
        0xFE,
        (
            "I actually came here right at opening, today.\x01",
            "There's nothing more refreshing than a bit of\x01",
            "morning shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_C729")

    ChrTalk(
        0xFE,
        (
            "Oh, my. Look at the time.\x01",
            "I hadn't realized it was this late, already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't had this much fun in a long time,\x01",
            "so the whole day flew past me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C77A")

    ChrTalk(
        0xFE,
        (
            "Hey, sorry about that!\x01",
            "I'm a bit busy shopping at the moment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C829")

    ChrTalk(
        0xFE,
        (
            "Crossbell has brand-name shops from\x01",
            "all over the Zemurian continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too bad I can't afford any of it, even if I\x01",
            "tap into my secret savings. *sigh*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_C829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_CA18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C984")

    ChrTalk(
        0xFE,
        (
            "Tickets for Arc en Ciel's new, highly anticipated\x01",
            "production are going on sale soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'd love to get my hands on one,\x01",
            "but they're really expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, I'm pretty sure they sold out instantly\x01",
            "the last time they went on sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no doubt people will be fighting\x01",
            "over them this year, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CA13")

    label("loc_C984")


    ChrTalk(
        0xFE,
        (
            "I've been waiting in anticipation for Arc en Ciel's\x01",
            "newest production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might be able to get some tickets if\x01",
            "I line up overnight...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA13")

    Jump("loc_CC38")

    label("loc_CA18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CAA8")

    ChrTalk(
        0xFE,
        (
            "Okay, let's see... I bought all of the ingredients\x01",
            "I needed and checked out Prada's newest\x01",
            "arrivals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhh, what else...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_CAA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CB58")

    ChrTalk(
        0xFE,
        (
            "Hey, did you see the new outfits at the shop that\x01",
            "sells western clothing? I totally want them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband was opposed to buying them, though.\x01",
            "*sigh*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_CB58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_CB96")

    ChrTalk(
        0xFE,
        "Oh? I wonder what Kean's doing over there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC38")

    label("loc_CB96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_CC38")

    ChrTalk(
        0xFE,
        (
            "Wow, look at all of the newest arrivals\x01",
            "in all of these shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to continue coming here\x01",
            "as frequently as possible to keep up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC38")

    TalkEnd(0xFE)
    Return()

    # Function_22_C2E6 end

    def Function_23_CC3C(): pass

    label("Function_23_CC3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CCD1")

    ChrTalk(
        0xFE,
        "*sigh* Why does Mom have to always be like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish she'd think about what she wants\x01",
            "to buy BEFORE leaving the house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_CCD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CD3E")

    ChrTalk(
        0xFE,
        (
            "What a surprise. I've been stuck here all\x01",
            "morning with my mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*yawn*\x01",
            "I'm so sleepy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_CD3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CDC3")

    ChrTalk(
        0xFE,
        (
            "Dad's getting paid, so you know what\x01",
            "that means, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mom's going to go on a nonstop\x01",
            "shopping spree again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_CDC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CF04")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE4A")

    ChrTalk(
        0xFE,
        (
            "How can you come here so often\x01",
            "and not buy anything, Mom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All you ever do is window-shop.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEFF")

    label("loc_CE4A")


    ChrTalk(
        0xFE,
        (
            "Dad took the wallet away from Mom.\x01",
            "He doesn't want her using it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not poor, but I don't think he did\x01",
            "anything wrong. There's nothing wrong\x01",
            "with being frugal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEFF")

    Jump("loc_D4D3")

    label("loc_CF04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_CF65")

    ChrTalk(
        0xFE,
        (
            "Mom spends her whole day looking at stores.\x01",
            "Doesn't she ever get bored of it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_CF65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D02B")

    ChrTalk(
        0xFE,
        (
            "Something is seriously wrong with my mom.\x01",
            "How does she spend hours window shopping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't help that it feels like I've thrown\x01",
            "away my whole day when she drags me along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D02B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_D0DD")

    ChrTalk(
        0xFE,
        (
            "I was forced to go shopping with my mom.\x01",
            "We've been here all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*\x01",
            "Well, there goes the promise with my friends.\x01",
            "So much for playing with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D0DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_D196")

    ChrTalk(
        0xFE,
        (
            "My dad's going to be home any minute, yet\x01",
            "neither dinner nor bath are ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dad has the patience of a saint. I don't know how\x01",
            "he hasn't gotten sick of Mom yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_D1D9")

    ChrTalk(
        0xFE,
        "Sorry, can't talk. Too busy babysitting my mom.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D22C")

    ChrTalk(
        0xFE,
        (
            "How old is Mom? She's freaking out over\x01",
            "brands like a teenager.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D2C3")

    ChrTalk(
        0xFE,
        "I wanna see an Arc en Ciel show...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To no one's surprise, Mom forgot about\x01",
            "the upcoming performance. She was too\x01",
            "busy shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D339")

    ChrTalk(
        0xFE,
        "Mom spends half of her morning shopping.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And half of her afternoon, you guessed it, shopping.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D3AB")

    ChrTalk(
        0xFE,
        "I'm helping Mom shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would have rather 'watched the house'\x01",
            "alone, but I had no choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D463")

    ChrTalk(
        0xFE,
        (
            "She wastes her time looking through every\x01",
            "cranny of every store, even though she\x01",
            "knows she's not going to buy anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "To be honest, it's pretty embarrassing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D4D3")

    label("loc_D463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D4D3")

    ChrTalk(
        0xFE,
        (
            "I'm always stuck waiting around forever, since\x01",
            "she's so slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Meh, whatever. I'm used to it.\x02",
    )

    CloseMessageWindow()

    label("loc_D4D3")

    TalkEnd(0xFE)
    Return()

    # Function_23_CC3C end

    def Function_24_D4D7(): pass

    label("Function_24_D4D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D5F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A3")

    ChrTalk(
        0xFE,
        (
            "Dang, how'd I manage to buy a brooch\x01",
            "that my wife already owns?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might end up becoming a laughing stock...\x01",
            "Still, part of me is interested in\x01",
            "seeing her reaction.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D5EE")

    label("loc_D5A3")


    ChrTalk(
        0xFE,
        (
            "I suppose it isn't so bad to have matching\x01",
            "brooches with the old bag.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5EE")

    Jump("loc_E2B4")

    label("loc_D5F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D67B")

    ChrTalk(
        0xFE,
        (
            "Have you noticed that Revache is\x01",
            "hardly around these days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's almost as if they've packed up and left town...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_D67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D736")

    ChrTalk(
        0xFE,
        "Did the mafia manage to finally push their luck?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't matter if they're the almighty Revache.\x01",
            "I don't think they'd be able to kick up a storm\x01",
            "and wave it away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_D736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D893")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C7")

    ChrTalk(
        0xFE,
        (
            "Back in my day, you had to spend three months'\x01",
            "salary on a wedding ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah... Those were the days.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D88E")

    label("loc_D7C7")


    ChrTalk(
        0xFE,
        (
            "I ended up wanting to get something for myself after\x01",
            "I bought my wife this brooch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The old bag loves to make fun of me for coming\x01",
            "here too often. She thinks I'm acting like a\x01",
            "teenage girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D88E")

    Jump("loc_E2B4")

    label("loc_D893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D987")

    ChrTalk(
        0xFE,
        (
            "The mayor delivered a wonderful speech for the\x01",
            "Anniversary Festival's closing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You weren't able to listen to it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How pitiful. What's happening to the\x01",
            "youngsters responsible for carrying\x01",
            "Crossbell's future?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_D987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D9D2")

    ChrTalk(
        0xFE,
        (
            "Hmm, a necklace...? Perhaps a bit too hip\x01",
            "for the wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_D9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DB46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAF1")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Times managed to expose\x01",
            "a politician for tax evasion a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He suddenly fell into poor health and was\x01",
            "hospitalized. Then people stopped talking\x01",
            "about his crimes altogether.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel it was all one big\x01",
            "cover-up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DB41")

    label("loc_DAF1")


    ChrTalk(
        0xFE,
        "What was his name again...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ge... Gevil? Govara? Somethin' like that.\x02",
    )

    CloseMessageWindow()

    label("loc_DB41")

    Jump("loc_E2B4")

    label("loc_DB46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_DB9F")

    ChrTalk(
        0xFE,
        (
            "Hmm... Decisions, decisions. What do I\x01",
            "buy my wife to make her happy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_DB9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_DBD7")

    ChrTalk(
        0xFE,
        "Mmm, what an elegant hat. I love it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_DBD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DDB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCF7")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Guardian Force's headquarters\x01",
            "can be found at Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, they've got the latest and\x01",
            "greatest equipment, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They haven't had the chance to make a name for\x01",
            "themselves, so they're stuck doing plain old\x01",
            "guard duty.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DDAD")

    label("loc_DCF7")


    ChrTalk(
        0xFE,
        (
            "The Crossbell Guardian Force has the latest and\x01",
            "greatest equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They haven't had the chance to make a name for\x01",
            "themselves, so they're stuck doing plain old\x01",
            "guard duty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDAD")

    Jump("loc_E2B4")

    label("loc_DDB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_DE3E")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Where'd that ring go? Did somebody buy it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, and here I was thinking it'd be a\x01",
            "perfect gift for my wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_DE3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_DF96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF1F")

    ChrTalk(
        0xFE,
        (
            "It's just a rumor, but apparently monsters\x01",
            "have been running amok in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, kinda rare for that to happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aren't there orbal lights set up to ward off\x01",
            "monsters? Did they break?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DF91")

    label("loc_DF1F")


    ChrTalk(
        0xFE,
        (
            "Monsters used to wreak havoc all the time\x01",
            "until the orbal light was invented. Now\x01",
            "they're a rare occurrence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF91")

    Jump("loc_E2B4")

    label("loc_DF96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_E0BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E080")

    ChrTalk(
        0xFE,
        (
            "Our current diet members are nothing but\x01",
            "a bunch of incompetent fools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're too preoccupied with partisan\x01",
            "politics to approve any new laws.\x01",
            "Sheesh, what a sorry state they're in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E0B5")

    label("loc_E080")


    ChrTalk(
        0xFE,
        (
            "*sigh* There's nothing but bad news\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0B5")

    Jump("loc_E2B4")

    label("loc_E0BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_E12D")

    ChrTalk(
        0xFE,
        (
            "My wife's always taking care of me, so I'd\x01",
            "like to buy her a gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah...this one's nice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2B4")

    label("loc_E12D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_E2B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E212")

    ChrTalk(
        0xFE,
        (
            "Crossbell is always getting caught up\x01",
            "in sticky situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just the other day, there was a shooting in\x01",
            "a back alley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure that the rest of the continent\x01",
            "sees us in a negative light.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E2B4")

    label("loc_E212")


    ChrTalk(
        0xFE,
        (
            "Crossbell can't seem to help getting\x01",
            "caught up in sticky situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And even when they know who did it,\x01",
            "they still don't always bring them to justice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2B4")

    TalkEnd(0xFE)
    Return()

    # Function_24_D4D7 end

    def Function_25_E2B8(): pass

    label("Function_25_E2B8")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_25_E2B8 end

    def Function_26_E2C2(): pass

    label("Function_26_E2C2")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_26_E2C2 end

    def Function_27_E2CC(): pass

    label("Function_27_E2CC")

    OP_4B(0x17, 0xFF)
    OP_4B(0x16, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_E3FD")

    ChrTalk(
        0x16,
        (
            "You're going to have a hard time fitting into\x01",
            "a slim dress with a chest like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hmm, maybe we could combine two\x01",
            "dresses to make it work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1806F#5P(An inconvenience, as always...)\x02\x03",
            "#1808F(When I'm in my 'work' clothes, I can just\x01",
            "change my figure with neigong...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E68A")

    label("loc_E3FD")


    ChrTalk(
        0x16,
        (
            "This one IS really nice, but I can't get\x01",
            "over how charming that last one was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Oh! This floral pattern is going to look\x01",
            "perfect on you, Rixia! ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 750)

    ChrTalk(
        0x17,
        (
            "#1810F#5POh, Shanshan. Thank you.\x02\x03",
            "You really didn't have to spend your day\x01",
            "off shopping for clothes with me, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 750)

    ChrTalk(
        0x16,
        (
            "Don't be silly! You may be cute, Rixia,\x01",
            "but your wardrobe is simply tragic.\x01",
            "You barely even have anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "That means I have no choice but to pick\x01",
            "out some outfits that'll make you shine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You're a famous gal. I'm baffled at how\x01",
            "little self-awareness you have when it\x01",
            "comes to your sense of fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#1809F#5PS-Sorry. I'll work on that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_E68A")

    OP_4C(0x17, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_E2CC end

    def Function_28_E693(): pass

    label("Function_28_E693")

    TalkBegin(0xFE)

    ChrTalk(
        0x18,
        "I came to buy a bunch of sweets today! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Sweets are the perfect motivation\x01",
            "for practice.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_E693 end

    def Function_29_E6FE(): pass

    label("Function_29_E6FE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16810, 1500, 23180, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, -16000, 0, 22500, 0)
    SetChrPos(0x109, -15250, 0, 22000, 0)
    SetChrPos(0x101, -16750, 0, 21250, 0)
    OP_93(0xE, 0xB4, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 3)), scpexpr(EXPR_END)), "loc_E8C0")

    ChrTalk(
        0xE,
        (
            "#5PIf you're looking for a present for a lady, you\x01",
            "can't go wrong with our stuffed Mishy plushes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThere isn't a girl in the world who doesn't\x01",
            "like stuffed toys, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FFran loves cutesy things, so that's\x01",
            "not a bad idea.\x02\x03",
            "#0503FThing is, I'm not really sure whether she\x01",
            "likes Mishy that much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB4")

    label("loc_E8C0")


    ChrTalk(
        0xE,
        "#5PWelcome to my general store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PAre you looking for anything in particular?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FActually, we're looking for a present that'd\x01",
            "be suitable for a young woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PA present for a young lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5POh, I know just the thing. How\x01",
            "about this Mishy plush?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PEvery lady likes a good plush, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12POoooh... I'm getting a good feeling about\x01",
            "this one, you guys. What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0503FIt's really cute...\x02\x03",
            "#0500FAnd considering how much Fran likes\x01",
            "cutesy things, it might just work.\x02\x03",
            "#0503FI'm not really sure whether she likes\x01",
            "Mishy that much, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12PGah, what the heck do I do? I hate\x01",
            "making decisions like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12PLloyd, do you think a Mishy plush would\x01",
            "make a good present for Fran?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 3)

    label("loc_EBB4")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Recommend it.\x01",                   # 0
            "Give it some more thought.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED55")

    ChrTalk(
        0x101,
        (
            "#12P#0000FI don't see why not. She's a fan of\x01",
            "cute things, and it's certainly cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12PWhen you put it like that, I think\x01",
            "you might be on to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12PI'll take it! If you don't mind, could you\x01",
            "wrap it with something pretty for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PCertainly. Thank you for your\x01",
            "patronage, sir.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x4)
    Call(0, 34)
    Jump("loc_EE0E")

    label("loc_ED55")


    ChrTalk(
        0x101,
        (
            "#12P#0000FWell, we still have some more time.\x01",
            "I say we take another look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#12PYeah, good idea. We should figure\x01",
            "out all our options before choosing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -16000, 0, 22500, 0)
    EventEnd(0x5)

    label("loc_EE0E")

    Return()

    # Function_29_E6FE end

    def Function_30_EE0F(): pass

    label("Function_30_EE0F")

    EventBegin(0x0)
    Fade(500)
    OP_68(15120, 1500, 7250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 16000, 0, 6500, 0)
    SetChrPos(0x109, 16750, 0, 6000, 0)
    SetChrPos(0x101, 15250, 0, 5250, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 4)), scpexpr(EXPR_END)), "loc_EFF9")

    ChrTalk(
        0xB,
        (
            "#5PHow about a jar of ice jam imported\x01",
            "straight from Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIts cool, smooth texture is absolutely\x01",
            "irresistible. It's been all the rage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FFran's diet HAS always revolved around\x01",
            "bread. Some rare jam to complement that\x01",
            "might not be bad.\x02\x03",
            "#0503FStill, a present that doesn't eventually run\x01",
            "out would probably be nicer, wouldn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F369")

    label("loc_EFF9")


    ChrTalk(
        0xB,
        "#5PWelcome to Legion's Foods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PLooking for ingredients? Well, you've come\x01",
            "to the right place! We have an assortment\x01",
            "of imported goods waiting to be bought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, ma'am. We're looking to buy\x01",
            "a present for a young woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PReally, now? Well, in that case...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHow about a jar of ice jam imported\x01",
            "straight from Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIts cool, smooth texture is absolutely\x01",
            "irresistible. It's been all the rage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PJam would definitely be an unexpected\x01",
            "kind of gift. Would Fran even like it, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FFran's diet HAS always revolved around\x01",
            "bread. Some rare jam to complement that\x01",
            "might not be bad.\x02\x03",
            "#0503FStill, a present that doesn't eventually run\x01",
            "out would probably be nicer, wouldn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PUghhh... That doesn't really help me any.\x01",
            "I'm so lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PWhat do you think, Lloyd? Should I go\x01",
            "with the ice jam?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 4)

    label("loc_F369")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Recommend it.\x01",                   # 0
            "Give it some more thought.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4FC")

    ChrTalk(
        0x101,
        (
            "#12P#0000FI don't see why not. If she's a big fan of\x01",
            "bread, then I'm sure she'd love a nice\x01",
            "jar of jam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PWhen you put it like that, I think\x01",
            "you might be on to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PI'll take it! If you don't mind, could you\x01",
            "wrap it with something pretty for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYou got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x5)
    Call(0, 34)
    Jump("loc_F59B")

    label("loc_F4FC")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI think we should look around some\x01",
            "more, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PReally? Huh. I guess we can check\x01",
            "out some of the other shops.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 16000, 0, 6500, 0)
    EventEnd(0x5)

    label("loc_F59B")

    Return()

    # Function_30_EE0F end

    def Function_31_F59C(): pass

    label("Function_31_F59C")

    EventBegin(0x0)
    Fade(500)
    OP_68(16149, 9530, 11470, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 15500, 8029, 12250, 90)
    SetChrPos(0x109, 14500, 8029, 11500, 90)
    SetChrPos(0x101, 14750, 8029, 13000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 5)), scpexpr(EXPR_END)), "loc_F769")

    ChrTalk(
        0xC,
        (
            "#11PWhy not go with one of our newest\x01",
            "products, the knitted Pom beanie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI assure you, she'll become infatuated with\x01",
            "the soft, fluffy sensation of the white Pom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FHmm... It would match her usual outfits,\x01",
            "at least.\x02\x03",
            "#0503FBut I'm not sure how well a hat like that\x01",
            "would mesh with her hairstyle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB38")

    label("loc_F769")


    ChrTalk(
        0xC,
        "#11PWelcome to Lucca Boutique!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWe have every style of clothing you\x01",
            "could ever ask for, from children's clothes\x01",
            "to fancy business suits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf you need anything or have any\x01",
            "questions, just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FActually, we're looking for a present\x01",
            "for a young woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf it's a gift for a young lady, then let's\x01",
            "see what we have in stock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhy not go with one of our newest\x01",
            "products, the knitted Pom beanie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI assure you, she'll become infatuated with\x01",
            "the soft, fluffy sensation of the white Pom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PA beanie? Well, I could definitely see\x01",
            "Fran wearing this, considering how\x01",
            "cute it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FMe, too. It would probably match most\x01",
            "of her regular outfits, I think.\x02\x03",
            "#0503FBut I'm not sure how well a hat like that\x01",
            "would mesh with her hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PY-Yeah, I didn't think about that. Looks\x01",
            "like this would be a risky bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PGive it to me straight, Lloyd. Do you\x01",
            "think getting the beanie is a good idea?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 5)

    label("loc_FB38")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Recommend it.\x01",                   # 0
            "Give it some more thought.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCC9")

    ChrTalk(
        0x101,
        (
            "#6P#0000FI don't see why not. I'm sure Fran\x01",
            "would love something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PWhen you put it like that, I think\x01",
            "you might be on to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PI'll take it! If you don't mind, could you\x01",
            "wrap it with something pretty for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PWhy, of course. Give me just a moment.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x6)
    Call(0, 34)
    Jump("loc_FDA5")

    label("loc_FCC9")


    ChrTalk(
        0x101,
        (
            "#6P#0000FThis might be the hardest request the\x01",
            "SSS has gotten yet... It's not too late\x01",
            "to look at the other shops, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#5PI think we still have time. L-Let's try\x01",
            "to hurry, guys.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 15500, 8029, 12250, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_FDA5")

    Return()

    # Function_31_F59C end

    def Function_32_FDA6(): pass

    label("Function_32_FDA6")

    EventBegin(0x0)
    Fade(500)
    OP_68(-460, 9520, 27870, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x19F, 0, 8029, 27750, 0)
    SetChrPos(0x109, 750, 8029, 27250, 0)
    SetChrPos(0x101, -750, 8029, 26500, 0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 6)), scpexpr(EXPR_END)), "loc_FF86")

    ChrTalk(
        0xA,
        "#5PWhat do you think about these Strega boots?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe Strega Corporation is as reliable as\x01",
            "shoemakers come, and the brand has\x01",
            "become quite popular among girls lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FI think I remember Fran saying she was\x01",
            "getting interested in boots recently.\x02\x03",
            "#0503FNo clue if she was talking about this\x01",
            "particular brand, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102C5")

    label("loc_FF86")


    ChrTalk(
        0xA,
        (
            "#5PWelcome, everyone. Looking for a\x01",
            "new pair of shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PRunners, leather shoes, boots...you name it.\x01",
            "We have a wide selection of shoes to satisfy\x01",
            "our customers' every need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWhat sort of women's shoes do you\x01",
            "have? We're trying to buy a gift for\x01",
            "someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHmm, let me see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHow do you feel about these Strega boots?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThe Strega Corporation is as reliable as\x01",
            "shoemakers come, and the brand has\x01",
            "become quite popular among girls lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PA pair of boots? Excuse me, dear sister.\x01",
            "Do you know if Fran wears boots?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FI'm pretty sure Fran told me she was\x01",
            "getting interested in boots recently.\x02\x03",
            "#0503FNo clue if she was talking about this\x01",
            "particular brand, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PG-Gah. I'm not sure, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PDo you think I should go with the\x01",
            "Strega boots, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 6)

    label("loc_102C5")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Recommend it.\x01",                   # 0
            "Give it some more thought.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1042C")

    ChrTalk(
        0x101,
        (
            "#12P#0000FWell, who doesn't like a nice\x01",
            "pair of boots?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PWhen you put it like that, I think\x01",
            "you might be on to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PI'll take it! If you don't mind, could you\x01",
            "wrap it with something pretty for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PI certainly can.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x7)
    Call(0, 34)
    Jump("loc_104CA")

    label("loc_1042C")


    ChrTalk(
        0x101,
        (
            "#12P#0000FWe should browse some of the other\x01",
            "stores while we still have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PYeah, that's probably a good idea...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 8029, 27700, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_104CA")

    Return()

    # Function_32_FDA6 end

    def Function_33_104CB(): pass

    label("Function_33_104CB")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12820, 9330, 7150, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x19F, -13400, 8029, 6600, 45)
    SetChrPos(0x109, -13160, 8029, 5720, 45)
    SetChrPos(0x101, -14580, 8029, 6580, 45)
    OP_93(0xD, 0xE1, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 7)), scpexpr(EXPR_END)), "loc_106A9")

    ChrTalk(
        0xD,
        (
            "#11PTake a gander at our pink moon\x01",
            "necklace. Isn't it a beauty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs you can see, it's garnished with\x01",
            "a dazzling pink jewel, only adding\x01",
            "to its grace and refinement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FPink IS one of Fran's favorite colors,\x01",
            "and the necklace itself is gorgeous...\x02\x03",
            "#0503FIsn't this far too serious a gift for\x01",
            "a first date, though?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A02")

    label("loc_106A9")


    ChrTalk(
        0xD,
        (
            "#11POur humble shop primarily deals in\x01",
            "small accessories and jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PThe price may be off-putting, but I assure\x01",
            "you everything is of the highest quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWhat would you recommend as a\x01",
            "gift? For a young woman, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PAh, I know just the thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PTake a gander at our pink moon\x01",
            "necklace. Isn't it beautiful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAs you can see, it has a dazzling\x01",
            "pink jewel, which only adds to its\x01",
            "grace and refinement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#6PI-Isn't this sort of extravagant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#0500FIt absolutely is. Still, pink IS one of\x01",
            "Fran's favorite colors, and the necklace\x01",
            "itself is gorgeous...\x02\x03",
            "#0503FIsn't this a little overboard for a first date,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#6PY-You might be on to something there...\x01",
            "I don't want her to get the wrong idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#6PStill, it's a hard call. What do you think\x01",
            "about the pink moon necklace, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 7)

    label("loc_10A02")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Recommend it.\x01",                   # 0
            "Give it some more thought.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B86")

    ChrTalk(
        0x101,
        "#6P#0000FIt's definitely a beautiful gift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#6PWhen you put it like that, I think\x01",
            "you might be on to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#6PI'll take it! If you don't mind, could you\x01",
            "wrap it with something pretty for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PHoho, wonderful. Give me a second\x01",
            "and I'll get this ready.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x8)
    Call(0, 34)
    Jump("loc_10C1F")

    label("loc_10B86")


    ChrTalk(
        0x101,
        "#6P#0000FWe should brainstorm some more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#6PG-Got'cha. Who knew picking a simple\x01",
            "present would be so complicated?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13400, 8029, 6600, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_10C1F")

    Return()

    # Function_33_104CB end

    def Function_34_10C20(): pass

    label("Function_34_10C20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x10, 0xFF)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_68(0, 1500, 3750, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19400, 0)
    SetChrPos(0x101, 0, 30, 4750, 180)
    SetChrPos(0x109, -750, 30, 3250, 45)
    SetChrPos(0x19F, 750, 30, 3250, 315)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x10, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19F,
        (
            "#11PThanks, you two. I never would have\x01",
            "been able to pick out something this\x01",
            "nice by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PAll I can do now is hope that Fran\x01",
            "loves it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#0503FWell, you won't know until you actually\x01",
            "give it to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FOh, shoot. It's almost time for us to\x01",
            "meet everyone over at Vingt-Sept.\x02\x03",
            "#0000FWe don't want to keep Fran waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PI-It's finally time... I think I'm ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#0508F(Oh, boy. Here we go.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_10C20 end

    def Function_35_10E8C(): pass

    label("Function_35_10E8C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_10F31")

    ChrTalk(
        0x101,
        (
            "#0000FAnton still hasn't picked out a gift\x01",
            "for Fran yet.\x02\x03",
            "I doubt Fran's break will last that long, so\x01",
            "we need to hurry and get this over with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11008")

    label("loc_10F31")


    ChrTalk(
        0x19F,
        "Hey! Where the heck are you going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "Aren't you going to help me pick out\x01",
            "a gift for Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FWe need to pick up the pace, or else\x01",
            "her break will already be over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FRight. Let's do this.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_11008")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 0, 0)
    EventEnd(0x4)
    Return()

    # Function_35_10E8C end

    def Function_36_1101F(): pass

    label("Function_36_1101F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3660, 2029, 7210, 0)
    MoveCamera(17, 21, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(16100, 0)
    SetChrPos(0x101, 3750, 30, 9040, 45)
    SetChrPos(0x102, 4920, 30, 7850, 45)
    SetChrPos(0x103, 2550, 0, 7830, 45)
    SetChrPos(0x104, 3730, 0, 6660, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117B")

    ChrTalk(
        0x101,
        (
            "#6P#0003F(The Times Department Store... Tront was\x01",
            "in here for a bit. He might have dropped\x01",
            "something in here.)\x02\x03",
            "#0000FExcuse me, ma'am. Do you happen to have\x01",
            "a lost and found around here?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_111CF")

    label("loc_1117B")


    ChrTalk(
        0x101,
        (
            "#6P#0000FExcuse me, ma'am. Do you happen to have\x01",
            "a lost and found around here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111CF")


    ChrTalk(
        0x9,
        "#5PYou've lost something of yours?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThis front desk more or less serves as the\x01",
            "lost and found, and we have a few things\x01",
            "on hand. What are you looking for?\x02",
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
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#0305FA few things, eh? You think they've\x01",
            "got Tront's stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FHopefully. I'm not that shocked that they\x01",
            "find a lot of dropped stuff, given how big\x01",
            "a building Times is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FTront said he lost his wallet, a souvenir,\x01",
            "and a third thing he couldn't remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FUpon reflection, it might have been\x01",
            "wise to ask for more details about\x01",
            "each of the items.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        "#11PAh, wait a minute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAre you referring to the customer whose\x01",
            "wallet fell out of a hole in his bag?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FThat's him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FOh, thank goodness. Someone ended\x01",
            "up seeing him drop it after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "O-Oh, not quite. We only discovered\x01",
            "it after the fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's just that, he stuck out like a\x01",
            "sore thumb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHe most certainly did. He was happily\x01",
            "laughing and cracking jokes with every\x01",
            "person he ran into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWhile he was shopping, he placed his\x01",
            "bag on top of one of the display cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIt was only when we were cleaning\x01",
            "up later that we found the wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FTront sure is a lucky man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203F(I hope all of our requests are this easy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FHe never bothered to come here to\x01",
            "search for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FPoor guy musta given up already.\x02\x03",
            "I s'pose that's why he came to us\x01",
            "for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PPlease wait a moment.\x01",
            "We'll bring it right away.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5PHere you are.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x337),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x337, 1)

    ChrTalk(
        0x101,
        "#6P#0000FThanks, you two. You're lifesavers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PNo problem. Just make sure that\x01",
            "gets back in the right hands.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11991")

    ChrTalk(
        0x104,
        (
            "#12P#0300FThat should be all of his stuff, right?\x01",
            "Good stuff, guys. Let's run on back\x01",
            "and give the man the good news.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11991")

    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2, 0x1, 0x1)
    SetScenarioFlags(0x1, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119C9")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_119C9")

    SetChrPos(0x0, 3740, 0, 7840, 45)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_68(3740, 1800, 7840, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    EventEnd(0x5)
    Return()

    # Function_36_1101F end

    def Function_37_11A13(): pass

    label("Function_37_11A13")

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

    # Function_37_11A13 end

    SaveToFile()

Try(main)
