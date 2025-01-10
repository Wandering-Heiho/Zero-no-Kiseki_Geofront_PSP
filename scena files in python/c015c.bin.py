from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c015c.bin",                # FileName
        "c015c",                    # MapName
        "c015c",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 3, 0, 4],
    )

    BuildStringList((
        "c015c",                  # 0
        "Hoisdorf",               # 1
        "Braun",                  # 2
        "Selteo",                 # 3
        "Nonno",                  # 4
        "Chief Roberts",          # 5
        "Izuri",                  # 6
        "Ferrick",                # 7
        "Cindy",                  # 8
        "Anri",                   # 9
        "Yunks",                  # 10
        "Marietta",               # 11
        "Young Man",              # 12
        "Girl",                   # 13
        "Flotte",                 # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Tourist",                # 23
        "Gironde",                # 24
        "Bracer Wenzel",          # 25
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch34302.itc",                   # 04
        "chr/ch23402.itc",                   # 05
        "chr/ch21402.itc",                   # 06
        "chr/ch21202.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20802.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch24500.itc",                   # 0C
        "chr/ch24502.itc",                   # 0D
        "chr/ch21200.itc",                   # 0E
        "chr/ch21702.itc",                   # 0F
        "chr/ch22000.itc",                   # 10
        "chr/ch22100.itc",                   # 11
        "chr/ch22200.itc",                   # 12
        "chr/ch27600.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch32300.itc",                   # 15
        "chr/ch24500.itc",                   # 16
        "chr/ch27300.itc",                   # 17
        "chr/ch29302.itc",                   # 18
        "chr/ch29300.itc",                   # 19
    ))

    DeclNpc(-509,    0,       12449,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-45700,  0,       5530,    0,    257,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   257,  0x0, 0,   3,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-1750,   5000,    17659,   180,  341,  0x0, 0,   24,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-949,    200,     2299,    273,  405,  0x0, 2,   15,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-2190,   0,       -200,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-4670,   0,       4480,    45,   405,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5730,   0,       1269,    270,  405,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-759,    0,       3640,    180,  405,  0x0, 0,   19,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-3710,   0,       5789,    225,  405,  0x0, 0,   20,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(610,     5000,    9779,    180,  389,  0x0, 0,   21,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-500,    5000,    9770,    180,  389,  0x0, 0,   22,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6829,    150,     3569,    270,  469,  0x0, 0,   5,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(2009,    150,     3569,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(1200,    0,       -1909,   135,  385,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(2019,    0,       5309,    315,  385,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3289,    0,       6320,    315,  385,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  257,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(56479,   -1000,   -8770,   90,   389,  0x0, 0,   23,  0,   0,   0,   0,   7,   255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  5,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_488",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_5DD",          # 02, 2
        "Function_3_667",          # 03, 3
        "Function_4_7A5",          # 04, 4
        "Function_5_7A6",          # 05, 5
        "Function_6_7AA",          # 06, 6
        "Function_7_1A61",         # 07, 7
        "Function_8_1BE1",         # 08, 8
        "Function_9_1BE5",         # 09, 9
        "Function_10_2546",        # 0A, 10
        "Function_11_2BC2",        # 0B, 11
        "Function_12_3125",        # 0C, 12
        "Function_13_32D0",        # 0D, 13
        "Function_14_389E",        # 0E, 14
        "Function_15_3B10",        # 0F, 15
        "Function_16_3C7B",        # 10, 16
        "Function_17_3D1A",        # 11, 17
        "Function_18_3D8A",        # 12, 18
        "Function_19_3F38",        # 13, 19
        "Function_20_3FA0",        # 14, 20
        "Function_21_4137",        # 15, 21
        "Function_22_4180",        # 16, 22
        "Function_23_4320",        # 17, 23
        "Function_24_44CC",        # 18, 24
        "Function_25_463F",        # 19, 25
        "Function_26_47F8",        # 1A, 26
        "Function_27_4865",        # 1B, 27
        "Function_28_493C",        # 1C, 28
        "Function_29_4A55",        # 1D, 29
        "Function_30_4B7A",        # 1E, 30
        "Function_31_4C27",        # 1F, 31
        "Function_32_4EC4",        # 20, 32
        "Function_33_5D5C",        # 21, 33
    ))


    def Function_0_488(): pass

    label("Function_0_488")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4C8"),
        (1, "loc_4D4"),
        (2, "loc_4E0"),
        (3, "loc_4EC"),
        (4, "loc_4F8"),
        (5, "loc_504"),
        (6, "loc_510"),
        (SWITCH_DEFAULT, "loc_51C"),
    )


    label("loc_4C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_504")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_510")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_51C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_528")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_53F")

    Return()

    # Function_0_488 end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DC")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_540")

    label("loc_5DC")

    Return()

    # Function_1_540 end

    def Function_2_5DD(): pass

    label("Function_2_5DD")


    def lambda_5E2():
        OP_A6(0xFE, 0x4, 0x0, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E2)

    label("loc_5F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_666")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_63B")
    OP_94(0xFE, 0xFFFFF16E, 0x1C0C, 0x3B6, 0x20DA, 0x3E8)
    Sleep(100)
    Jump("loc_661")

    label("loc_63B")

    OP_93(0xFE, 0xE1, 0x3E8)
    OP_93(0xFE, 0x13B, 0x3E8)
    OP_93(0xFE, 0x2D, 0x3E8)
    OP_93(0xFE, 0x87, 0x3E8)
    OP_93(0xFE, 0xE1, 0x3E8)
    Sleep(500)

    label("loc_661")

    Jump("loc_5F6")

    label("loc_666")

    Return()

    # Function_2_5DD end

    def Function_3_667(): pass

    label("Function_3_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrPos(0xB, -6980, 0, 1280, 90)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0xC, -210, 5000, 18380, 0)
    SetChrChipByIndex(0xC, 0x19)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x10)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7A4")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0xA, -1460, 0, 7630, 180)
    BeginChrThread(0xA, 0, 0, 2)
    SetChrPos(0xB, 6810, 0, 9660, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_7A4")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_752")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_7A4")

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_76F")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78C")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A4")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_7A4")

    Return()

    # Function_3_667 end

    def Function_4_7A5(): pass

    label("Function_4_7A5")

    Return()

    # Function_4_7A5 end

    def Function_5_7A6(): pass

    label("Function_5_7A6")

    Call(0, 6)
    Return()

    # Function_5_7A6 end

    def Function_6_7AA(): pass

    label("Function_6_7AA")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB")

    ChrTalk(
        0x1F,
        (
            "As much as I wanna say come on in and\x01",
            "have a look around, I'm afraid I can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "You youngsters should already know that,\x01",
            "in Crossbell, you can't buy weapons without\x01",
            "a license. If this is a prank, scram.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe're actually from the CPD, sir. Sorry\x01",
            "for the confusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "Y'all are police officers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Oooh, you must be those kids ol' Sergei\x01",
            "was telling me about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Hmm, all right. Feel free to take a look\x01",
            "around the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When you're ready to checkout, show me\x01",
            "your Detective Notebook. That'll substitute\x01",
            "as a license.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)
    SetScenarioFlags(0xAF, 2)

    label("loc_9FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A56")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A75")
    OP_AF(0x5)
    Jump("loc_AB7")

    label("loc_A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A85")
    OP_AF(0x4)
    Jump("loc_AB7")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A95")
    OP_AF(0x3)
    Jump("loc_AB7")

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AA5")
    OP_AF(0x2)
    Jump("loc_AB7")

    label("loc_AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AB5")
    OP_AF(0x1)
    Jump("loc_AB7")

    label("loc_AB5")

    OP_AF(0x0)

    label("loc_AB7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A58")

    label("loc_AC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADA")
    Jump("loc_1A58")

    label("loc_ADA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A58")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(
        0x1F,
        (
            "Thank Aidios, all the foolin'\x01",
            "around outside ends today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, y'all enjoy yourselves\x01",
            "while you still can, ya hear?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C00")

    label("loc_B8C")


    ChrTalk(
        0x1F,
        (
            "Hopefully, everyone gets off their asses after today, eh?\x01",
            "If y'all wanna enjoy yourselves, do it while ya can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C00")

    Jump("loc_1A58")

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_CA8")

    ChrTalk(
        0x1F,
        (
            "Hey there, still lookin'\x01",
            "for that lost kid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Crossbell's a massive city, I s'pose...\x01",
            "Well, I guess all ya can do\x01",
            "is keep doin' the legwork.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A58")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_10A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1001")

    ChrTalk(
        0x101,
        (
            "#0001F(Oh, maybe this guy knows something\x01",
            "about Colin.)\x02",
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
        0x1F,
        (
            "Oh, decidin' to use a photo\x01",
            "for your investigation now, eh?\x01",
            "Look at ya, actin' all police-like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, th-thanks?\x02\x03",
            "#0001FSo, do you have any clues? He's the\x01",
            "child of an acquaintance of ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I didn't actually get to see the parade. Unless he\x01",
            "came into the store, I wouldn't have seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "However, if he stuck to the parade,\x01",
            "then shouldn't he be on East Street?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Accordin' to the parade itinerary,\x01",
            "it should've gone over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FI see...\x01",
            "(According to Randy's report,\x01",
            "East Street was a bust...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3300FWell, then, what do\x01",
            "we do now?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 0)
    Call(0, 31)

    ChrTalk(
        0x160,
        (
            "#3304FI see you're quite the cautious one.\x01",
            "I knew you'd be interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_1001")


    ChrTalk(
        0x1F,
        (
            "Accordin' to the parade itinerary,\x01",
            "it should've gone over by East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Assuming he stuck to the\x01",
            "parade, then shouldn't\x01",
            "he be in those parts?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109B")

    Jump("loc_1A58")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1195")

    ChrTalk(
        0x1F,
        (
            "Orbal vehicles... They've completely\x01",
            "changed how the parade operates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, I s'pose the cops have got it\x01",
            "rough as usual. That never changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I imagine all the rookie cops are exhausted right about now.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11EC")

    label("loc_1195")


    ChrTalk(
        0x1F,
        (
            "While the times may change,\x01",
            "the police havin' it rough will\x01",
            "remain ever constant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EC")

    Jump("loc_1A58")

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129E")

    ChrTalk(
        0x1F,
        "Today's that parade, ain't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Geez, I'm sure the boys in blue have\x01",
            "got their work cut out for them, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Sometimes I pity y'all...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_131A")

    label("loc_129E")


    ChrTalk(
        0x1F,
        (
            "If ya got spare time, try goin' to\x01",
            "the Administrative District's plaza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "You cops probably havin' a hard time, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_131A")

    Jump("loc_1A58")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1654")

    ChrTalk(
        0x1F,
        (
            "I tried to see if ol' Sergei could\x01",
            "go get a drink with me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "...apparently, he's got a meetin' today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Hmph, I hope they aren't forcin' all their\x01",
            "petty issues on that geezer again...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Ah, they've always been takin' advantage\x01",
            "of that old fool. I've been tellin' him to grow a\x01",
            "spine, but he keeps shoulderin' their problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I still can't believe he actually managed to\x01",
            "establish this 'Special Support Section'...\x02",
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
        0x103,
        "#0203FIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, the SSS is like Sergei's baby,\x01",
            "a division he built himself.\x01",
            "One reaps what one sows, I s'pose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16FF")

    label("loc_1654")


    ChrTalk(
        0x1F,
        (
            "I'd put money on that meetin' being\x01",
            "about the parade's security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, the SSS is like Sergei's baby, though...\x01",
            "Maybe Sergei's not too worried after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FF")

    Jump("loc_1A58")

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DE")

    ChrTalk(
        0x1F,
        (
            "By the way, y'all heard yet?\x01",
            "Seems like Arios is back in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Gotta admit, this year's crowd is impressive!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Even someone like him couldn't go\x01",
            "too long without returning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1844")

    label("loc_17DE")


    ChrTalk(
        0x1F,
        "Appears even old Arios came back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "This year's crowd... Better buckle down the hatches.\x02",
    )

    CloseMessageWindow()

    label("loc_1844")

    Jump("loc_1A58")

    label("loc_1849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")

    ChrTalk(
        0x1F,
        (
            "Welcome.\x01",
            "This place is for buyin' weapons, so you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Tch, it's y'all. I thought ya might 'ave\x01",
            "been some overly eager tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Don't go enterin' a gloomy place\x01",
            "on a bright, happy day like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Look, if ya finished your business\x01",
            "here, go 'head and shoo, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FHe does not want us anywhere near\x01",
            "the shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A58")

    label("loc_19C5")


    ChrTalk(
        0x1F,
        (
            "This place is a weapons shop, got it?\x01",
            "Don't y'all come on a happy day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Look, if ya finished your business\x01",
            "here, go 'head and shoo, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A58")

    Jump("loc_A05")

    label("loc_1A5D")

    TalkEnd(0x1F)
    Return()

    # Function_6_7AA end

    def Function_7_1A61(): pass

    label("Function_7_1A61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xFE,
        (
            "Due to all the requests and security gigs,\x01",
            "the bracers have been stretched thin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to be ready for emergency situations,\x01",
            "I've been put on standby in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I should use this downtime to get myself a new sword.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1BDD")

    label("loc_1B70")


    ChrTalk(
        0xFE,
        (
            "My partner, Scott, is working alone today.\x01",
            "Well, he's perfectly capable on his own,\x01",
            "so I'm not worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1A61 end

    def Function_8_1BE1(): pass

    label("Function_8_1BE1")

    Call(0, 9)
    Return()

    # Function_8_1BE1 end

    def Function_9_1BE5(): pass

    label("Function_9_1BE5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2542")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C43")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C63")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_253D")

    label("loc_1C63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C77")
    Jump("loc_253D")

    label("loc_1C77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CFD")

    ChrTalk(
        0x8,
        "Oh, man. That's a big family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I suppose I'll go help\x01",
            "out in the kitchen today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253D")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D61")

    ChrTalk(
        0x8,
        "Ahem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have you been enjoying the\x01",
            "restaurant's quality staff?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DA5")

    label("loc_1D61")


    ChrTalk(
        0x8,
        (
            "That Selteo... There's gotta be some\x01",
            "way I can outperform him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA5")

    Jump("loc_253D")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F28")

    ChrTalk(
        0x101,
        "#0001F(He might know something about Colin.)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if\x01",
            "he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, poor kid got lost?\x01",
            "That's terrible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I unfortunately don't have any clues for you.\x01",
            "I don't think he showed up in this restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI see...\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 31)
    Jump("loc_1FFF")

    label("loc_1F28")


    ChrTalk(
        0x8,
        (
            "Hey, about that photo,\x01",
            "he's really a beautiful boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I get the feeling he looks\x01",
            "similar to your friend there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Now that I think about it... They\x01",
            "do sort of resemble each other...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3308F...\x02",
    )

    CloseMessageWindow()

    label("loc_1FFF")

    Jump("loc_253D")

    label("loc_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_20B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2068")

    ChrTalk(
        0x8,
        "Ahem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have you been enjoying the\x01",
            "restaurant's quality staff?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20AC")

    label("loc_2068")


    ChrTalk(
        0x8,
        (
            "That Selteo...\x01",
            "There's gotta be some way I can outperform him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AC")

    Jump("loc_253D")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2185")

    ChrTalk(
        0x8,
        (
            "This afternoon, the restaurant's\x01",
            "staff will be putting on a little\x01",
            "performance for our patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've planned it for right after the parade,\x01",
            "so please, stop by if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E9")

    label("loc_2185")


    ChrTalk(
        0x8,
        (
            "To tell you the truth, it was\x01",
            "an impromptu idea by Selteo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, I'm hoping it goes well.\x02",
    )

    CloseMessageWindow()

    label("loc_21E9")

    Jump("loc_253D")

    label("loc_21EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_22BD")

    ChrTalk(
        0x8,
        (
            "We're currently in the middle of preparing\x01",
            "our special menu meals only available\x01",
            "during the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because quantities are so limited,\x01",
            "please, order them while you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253D")

    label("loc_22BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_240F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D3")

    ChrTalk(
        0x8,
        (
            "It's good that we're this packed, but we still\x01",
            "haven't received the shipment of ingredients\x01",
            "we needed this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears the Anniversary Festival's hectic nature\x01",
            "is causing trouble for couriers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Either way, it's a problem for us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_240A")

    label("loc_23D3")


    ChrTalk(
        0x8,
        (
            "I've got to come up with some\x01",
            "kind of solution...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240A")

    Jump("loc_253D")

    label("loc_240F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_253D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(
        0x8,
        (
            "Welcome to Vingt-Sept.\x01",
            "Just the four of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, you're welcome to sit\x01",
            "at any of the empty seats.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_253D")

    label("loc_249A")


    ChrTalk(
        0x8,
        (
            "Even though it's only the second day,\x01",
            "we've already had so many customers this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This restaurant makes sure to cater\x01",
            "to all of our customers' needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253D")

    Jump("loc_1BF2")

    label("loc_2542")

    TalkEnd(0x8)
    Return()

    # Function_9_1BE5 end

    def Function_10_2546(): pass

    label("Function_10_2546")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2630")

    ChrTalk(
        0xFE,
        (
            "Today, we're planning to throw\x01",
            "an 'appreciation' party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After we finish closing up shop, us employees\x01",
            "are going to gather and have a few drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This year's been busy for us at Vingt-Sept.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26C4")

    label("loc_2630")


    ChrTalk(
        0xFE,
        (
            "So today, we're planning to throw\x01",
            "an 'appreciation' party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In retrospect, it's probably best if we don't\x01",
            "give Selteo too much to drink...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C4")

    Jump("loc_2BBE")

    label("loc_26C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(
        0xFE,
        "Why's the restaurant so noisy all of a sudden?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBE")

    label("loc_2726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_27A3")

    ChrTalk(
        0xFE,
        (
            "Haha, I remember eagerly waiting\x01",
            "for the parade as a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Trust me, the parade doesn't disappoint.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBE")

    label("loc_27A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_28CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284B")

    ChrTalk(
        0xFE,
        (
            "Hey! One lunch special,\x01",
            "ready to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We really attract a lot of customers during the\x01",
            "Anniversary Festival. It's busy, as expected.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28C9")

    label("loc_284B")


    ChrTalk(
        0xFE,
        "This year seems particularly hectic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard whispers that a stage was\x01",
            "constructed for the Harbor District, too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C9")

    Jump("loc_2BBE")

    label("loc_28CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A11")

    ChrTalk(
        0xFE,
        (
            "Crap, the ingredients are late today.\x01",
            "Now we have no means of cooking\x01",
            "lunches A through C on the menu...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our quick and easy solution was to create\x01",
            "a new, unique meal that combines all the\x01",
            "various meals on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We call it the 'Anniversary Special'!\x01",
            "Quite a brilliant idea, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A65")

    label("loc_2A11")


    ChrTalk(
        0xFE,
        (
            "Today, we're serving an\x01",
            "extra special lunch menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Order it while you can!\x02",
    )

    CloseMessageWindow()

    label("loc_2A65")

    Jump("loc_2BBE")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5B")

    ChrTalk(
        0xFE,
        (
            "Due to the curse of the Anniversary Festival,\x01",
            "our shipments of ingredients were delayed again.\x01",
            "Looks like we have to cut lunch A from the menu...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, man...\x01",
            "I should probably go let Hoisdorf know, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BBE")

    label("loc_2B5B")


    ChrTalk(
        0xFE,
        (
            "In these times, panicking will get me nowhere...\x01",
            "I'll leave this to the manager's discretion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBE")

    TalkEnd(0xFE)
    Return()

    # Function_10_2546 end

    def Function_11_2BC2(): pass

    label("Function_11_2BC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9A")

    ChrTalk(
        0xFE,
        (
            "Ow, my aching head... Yeah, I definitely\x01",
            "had too much to drink last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My head won't stop throbbing\x01",
            "and I can't remember a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I didn't...do anything bad, right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CD2")

    label("loc_2C9A")


    ChrTalk(
        0xFE,
        (
            "Gah... This sucks.\x01",
            "I wonder what I ended up doing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD2")

    Jump("loc_3121")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D26")

    ChrTalk(
        0xFE,
        "*hic*...*hic*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Number 4, time to shine!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D6C")

    label("loc_2D26")


    ChrTalk(
        0xFE,
        "Heh ahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, we gonna drink\x01",
            "under the table tonight, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6C")

    Jump("loc_3121")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E48")

    ChrTalk(
        0xFE,
        (
            "Hmph... Actually, singing is my\x01",
            "natural, Goddess-given talent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, the customers shall behold\x01",
            "my absolutely radiant voice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that lots of babes come\x01",
            "to hear me serenade them. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3121")

    label("loc_2E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2F66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F00")

    ChrTalk(
        0xFE,
        (
            "Even though I was taught how to make the Anniversary\x01",
            "Special, I was blown away when I actually cooked it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, my raw talent scares me sometimes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F61")

    label("loc_2F00")


    ChrTalk(
        0xFE,
        (
            "Just you wait, mister.\x01",
            "An Anniversary Special, comin' rig--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "AH! Hot! The oil splashed!\x02",
    )

    CloseMessageWindow()

    label("loc_2F61")

    Jump("loc_3121")

    label("loc_2F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_306B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3035")

    ChrTalk(
        0xFE,
        (
            "Braun wasted little time lecturing\x01",
            "me on the basics of how to cook\x01",
            "the new menu items...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why does that buffoon think I can cook\x01",
            "all of this with just one little lesson?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3066")

    label("loc_3035")


    ChrTalk(
        0xFE,
        "Damn it, I wish I was out there having fun!\x02",
    )

    CloseMessageWindow()

    label("loc_3066")

    Jump("loc_3121")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3121")

    ChrTalk(
        0xFE,
        (
            "Cutting the vegetables with the right\x01",
            "hand, watching the pan with my left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "GAAAH, I can't keep up!! How can one man\x01",
            "prepare five dishes at the exact same time?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3121")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BC2 end

    def Function_12_3125(): pass

    label("Function_12_3125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_318B")

    ChrTalk(
        0xFE,
        (
            "A huge family showed up\x01",
            "to the restaurant today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C'mon, I need to perk up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_32CC")

    label("loc_318B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31DA")

    ChrTalk(
        0xFE,
        (
            "Maybe drinking all that liquor\x01",
            "wasn't Selteo's best idea...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CC")

    label("loc_31DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3256")

    ChrTalk(
        0xFE,
        "Apparently, the parade is today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's probably the cause of all\x01",
            "the noise coming from the square!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CC")

    label("loc_3256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32CC")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, we've run out\x01",
            "of Vingt-Sept's lunch A.\x01",
            "Please, choose either lunch B or C!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    TalkEnd(0xFE)
    Return()

    # Function_12_3125 end

    def Function_13_32D0(): pass

    label("Function_13_32D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3364")
    Jump("loc_33AE")

    label("loc_3364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3384")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33AE")

    label("loc_3384")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33AE")

    label("loc_33A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_34B0")

    ChrTalk(
        0xFE,
        "Today's the last day of the festival, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose I could at least go listen\x01",
            "to the mayor's closing speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like fun time is over... All in all,\x01",
            "it was a pleasant experience.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3896")

    label("loc_34B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3541")

    ChrTalk(
        0xFE,
        "Agh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, don't speak of that childish\x01",
            "cook or his unnatural culinary talent again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You made me spill my coffee.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3896")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C2")

    ChrTalk(
        0xFE,
        (
            "Parade this, parade that...\x01",
            "It's absolutely aggravating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This. This is why I hate tourists.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_362F")

    label("loc_35C2")


    ChrTalk(
        0xFE,
        (
            "Why can't they comprehend that\x01",
            "there are some customers who just\x01",
            "want to quietly sit and read in peace?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362F")

    Jump("loc_3896")

    label("loc_3634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_36D6")

    ChrTalk(
        0xFE,
        "Nothing but eager customers today, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph, screw this Anniversary Special!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll gladly just stick with my\x01",
            "nice, hot cup of joe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3896")

    label("loc_36D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_37C2")

    ChrTalk(
        0xFE,
        "*slurp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like a lot of stores are employing that\x01",
            "'limited-time offer' tactic to get more sales...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly...\x01",
            "Why not just have it for sale year-round?\x01",
            "It's just annoying when you miss out on stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3896")

    label("loc_37C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3850")

    ChrTalk(
        0xFE,
        "*slurp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone's so obnoxiously merry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is EXACTLY why I hate\x01",
            "the citizens of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3896")

    label("loc_3850")


    ChrTalk(
        0xFE,
        (
            "Hmph, thank goodness this festival\x01",
            "enthusiasm doesn't faze me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3896")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_32D0 end

    def Function_14_389E(): pass

    label("Function_14_389E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3932")
    Jump("loc_397C")

    label("loc_3932")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3952")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_397C")

    label("loc_3952")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3972")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_397C")

    label("loc_3972")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_397C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA6")

    ChrTalk(
        0xFE,
        (
            "Haha, my son seems to really\x01",
            "enjoy these kinds of festivals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We come from Eastern Zemuria. I had my\x01",
            "doubts about taking this long journey...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, I'd say it was definitely worth\x01",
            "the time and energy it took to get here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3B08")

    label("loc_3AA6")


    ChrTalk(
        0xFE,
        (
            "Since we traveled ages to get to Crossbell,\x01",
            "I just want to take it easy and enjoy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B08")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_389E end

    def Function_15_3B10(): pass

    label("Function_15_3B10")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BA4")
    Jump("loc_3BEE")

    label("loc_3BA4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BC4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BEE")

    label("loc_3BC4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BE4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BEE")

    label("loc_3BE4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BEE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "Hey, mister! Is the kid's meal ready yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanna hurry and eat so I can go play!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_3B10 end

    def Function_16_3C7B(): pass

    label("Function_16_3C7B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Tomorrow, my father is coming all the way from\x01",
            "the countryside to watch the parade with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've gotta book a good spot before it's too late!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_3C7B end

    def Function_17_3D1A(): pass

    label("Function_17_3D1A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Father, are you enjoying yourself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really glad we decided to make\x01",
            "reservations in advance!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3D1A end

    def Function_18_3D8A(): pass

    label("Function_18_3D8A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E1E")
    Jump("loc_3E68")

    label("loc_3E1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E68")

    label("loc_3E3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E68")

    label("loc_3E5E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E68")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "W-Wow, this has quite the flavor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can really appreciate it as a\x01",
            "former chef myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm delighted that I can savor these delicacies in peace.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_3D8A end

    def Function_19_3F38(): pass

    label("Function_19_3F38")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    ChrTalk(
        0xFE,
        "What awful technique!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't even begin to imagine\x01",
            "who he's trying to imitate!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3F38 end

    def Function_20_3FA0(): pass

    label("Function_20_3FA0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4034")
    Jump("loc_407E")

    label("loc_4034")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4054")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_407E")

    label("loc_4054")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4074")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_407E")

    label("loc_4074")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_407E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Whenever you say 'parade,'\x01",
            "I always think of 'Central Square.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to be an early bird\x01",
            "if I want a good spot there!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_3FA0 end

    def Function_21_4137(): pass

    label("Function_21_4137")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    ChrTalk(
        0xFE,
        "Ahaha, but it's so much fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Again! Do it again!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4137 end

    def Function_22_4180(): pass

    label("Function_22_4180")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4214")
    Jump("loc_425E")

    label("loc_4214")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4234")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_425E")

    label("loc_4234")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4254")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_425E")

    label("loc_4254")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_425E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "*munch* *munch*...\x01",
            "Still got a bit before the parade starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why not check out all the stores?\x01",
            "They're having insane sales everywhere.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_4180 end

    def Function_23_4320(): pass

    label("Function_23_4320")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43B4")
    Jump("loc_43FE")

    label("loc_43B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43D4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43FE")

    label("loc_43D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43FE")

    label("loc_43F4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43FE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xD,
        "The Anniversary Festival should be enjoyed with one's family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm pleased to see no one in the family\x01",
            "had any objections to that idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_23_4320 end

    def Function_24_44CC(): pass

    label("Function_24_44CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4590")

    ChrTalk(
        0xE,
        (
            "I promised to go hang out with my friends,\x01",
            "but I think I'll stay with my family for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't even remember the last time I saw\x01",
            "my mom and pops next to each other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_463B")

    label("loc_4590")


    ChrTalk(
        0xE,
        "Granny's word is law in this family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Haha, not a big deal that I have to be here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Today's the last day of the festival,\x01",
            "so I'll spend it with my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_463B")

    TalkEnd(0xFE)
    Return()

    # Function_24_44CC end

    def Function_25_463F(): pass

    label("Function_25_463F")

    TalkBegin(0xFE)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_46E6")
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xF,
        "It's been a while since I last saw Mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Since it's been such a long time,\x01",
            "today just blew me away!\x01",
            "That's Granny for ya!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x2D, 0x0)
    Jump("loc_47F0")

    label("loc_46E6")


    ChrTalk(
        0xF,
        (
            "Mama?!\x01",
            "When did you come back?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What about work?\x01",
            "Is it really okay for you to be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Since that granny of yours called me down,\x01",
            "I had no choice but to hurry back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "More importantly, I wanted to see my kids'\x01",
            "faces. So, I just snuck away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_47F0")

    OP_4C(0x12, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_25_463F end

    def Function_26_47F8(): pass

    label("Function_26_47F8")

    TalkBegin(0xFE)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x10,
        (
            "Excuse me, could you please\x01",
            "add one more chair?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Of course.\x01",
            "Give me just one moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_47F8 end

    def Function_27_4865(): pass

    label("Function_27_4865")

    TalkBegin(0xFE)

    ChrTalk(
        0x11,
        (
            "Mother, I still have work to finish.\x01",
            "You nagging me is just distracting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You need a break every once in a while, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Here, stop standing around and stay awhile.\x01",
            "Let's go ahead and eat.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_4865 end

    def Function_28_493C(): pass

    label("Function_28_493C")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "Mama?!\x01",
            "When did you come back?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What about work?\x01",
            "Is it really okay for you to be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Since that granny of yours called me down,\x01",
            "I had no choice but to hurry back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "More importantly, I wanted to see my kids'\x01",
            "faces. So, I just snuck away!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_493C end

    def Function_29_4A55(): pass

    label("Function_29_4A55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4AC5")

    ChrTalk(
        0x13,
        (
            "Ferrick's grandmother is\x01",
            "a ferocious woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Tch, so we can't hang\x01",
            "out today, either?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B76")

    label("loc_4AC5")


    ChrTalk(
        0x13,
        (
            "Damn, blowing us off, his friends,\x01",
            "just to have lunch with his family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Ferrick might be childish\x01",
            "at times, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I kinda envy him...\x01",
            "J-Just a little, though!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_4B76")

    TalkEnd(0xFE)
    Return()

    # Function_29_4A55 end

    def Function_30_4B7A(): pass

    label("Function_30_4B7A")

    TalkBegin(0xFE)

    ChrTalk(
        0x14,
        (
            "That Ferrick actually seems to be\x01",
            "having fun with his family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "*sigh* It would be pretty nice if\x01",
            "MY family had such a caring\x01",
            "grandmother looking after us.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_4B7A end

    def Function_31_4C27(): pass

    label("Function_31_4C27")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4D44")

    ChrTalk(
        0x101,
        (
            "#0003FLet's continue with the investigation as planned.\x01",
            "Passing judgment without all of the\x01",
            "information is never a good call.\x02\x03",
            "#0000FAll right, I think this should cover it for\x01",
            "the Central Square investigation.\x01",
            "We should check out Station Street next.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E02")

    label("loc_4D44")


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
            "#0003F(Yeah, I think we've covered enough ground.)\x02\x03",
            "#0000F(Let's try searching for leads\x01",
            "at Station Street next.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E02")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Jump("loc_4EC3")

    label("loc_4E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4EC3")

    ChrTalk(
        0x101,
        (
            "#0003FLet's keep working on the Central Square\x01",
            "investigation for a bit longer.\x02\x03",
            "#0000FPassing judgment without all of the\x01",
            "information is never a good call.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC3")

    Return()

    # Function_31_4C27 end

    def Function_32_4EC4(): pass

    label("Function_32_4EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5130")
    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4F9F")

    ChrTalk(
        0xFE,
        "Oh, man! I can't wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha, that's why there's no\x01",
            "need for concern, you know!\x02",
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
    Jump("loc_5116")

    label("loc_4F9F")


    ChrTalk(
        0xFE,
        (
            "Ahaha, that's right! There's so many tourists\x01",
            "wandering around Central Square...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, I'm planning\x01",
            "to go see Tio today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, yes, hahaha!\x01",
            "Well, no need to worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Just who are you talking to, Chief?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Isn't that your boss, Tio?\x01",
            "Shouldn't you greet him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F(I would rather not. Talking with him\x01",
            "is mentally exhausting.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5116")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5D5B")

    label("loc_5130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_537C")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51CD")
    Jump("loc_5217")

    label("loc_51CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5217")

    label("loc_51ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_520D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5217")

    label("loc_520D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5217")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Well, then, I should probably try visiting\x01",
            "Guillaume's orbal factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's always been an old fart. I doubt he\x01",
            "went out to watch the parade or anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, oh, yes, I should bring\x01",
            "him some kind of present!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Wow, Tio's boss is really getting\x01",
            "into the festival spirit, isn't he?)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5D5B")

    label("loc_537C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5527")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5419")
    Jump("loc_5463")

    label("loc_5419")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5439")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5463")

    label("loc_5439")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5459")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5463")

    label("loc_5459")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5463")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Haha! This year's parade\x01",
            "was absolutely marvelous!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I even saw the famous Mishy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I managed to get quite the wonderful photo!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5D5B")

    label("loc_5527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_57CF")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55C4")
    Jump("loc_560E")

    label("loc_55C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_560E")

    label("loc_55E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5604")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_560E")

    label("loc_5604")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_560E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_56ED")

    ChrTalk(
        0xFE,
        (
            "After taking a look at Crossbell City's\x01",
            "town map, I've spotted a neat, little\x01",
            "place I want to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, just as I thought, it's near\x01",
            "the Entertainment District!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C3")

    label("loc_56ED")


    ChrTalk(
        0xFE,
        (
            "The Crossbell parade is today!\x01",
            "Now, then, where should I watch it from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mobile terminal was made for times like these!\x01",
            "And...*bip* *bop* *beep*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FMy boss seems to be enjoying himself...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_57C3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5D5B")

    label("loc_57CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_597B")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_586C")
    Jump("loc_58B6")

    label("loc_586C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_588C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B6")

    label("loc_588C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B6")

    label("loc_58AC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58F1")
    Call(0, 33)
    Jump("loc_596F")

    label("loc_58F1")


    ChrTalk(
        0xFE,
        "The Anniversary Special meal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, well, if it's only available during this\x01",
            "period, I've got to give it a taste! ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5D5B")

    label("loc_597B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A0F")
    Jump("loc_5A59")

    label("loc_5A0F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A2F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A59")

    label("loc_5A2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A59")

    label("loc_5A4F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A59")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5B53")

    ChrTalk(
        0xFE,
        (
            "I'll make sure to bring a treat for the\x01",
            "Special Support Section later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem... Young man, I'm grateful for you\x01",
            "always looking after Tio here. As her boss,\x01",
            "I must give you my humble thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D54")

    label("loc_5B53")


    ChrTalk(
        0x103,
        "#0200FCh-Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio!\x01",
            "Isn't the Anniversary Festival incredible?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I attended last year, too, but I have the feeling\x01",
            "this year will be even more fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, Tio, do you want to eat together?\x01",
            "It'll be my treat... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FI will pass.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "I-I see. Maybe next time, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'll bring some treats to the Special\x01",
            "Support Section later, hahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0211F(This man gets too excited...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(He's in high spirits, eh?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5D54")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_5D5B")

    Return()

    # Function_32_4EC4 end

    def Function_33_5D5C(): pass

    label("Function_33_5D5C")


    ChrTalk(
        0xFE,
        (
            "Ah, Tio! It's rare to see you\x01",
            "alone with a boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, could it be?\x01",
            "Are you on a date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FStop saying stupid things, stupid.\x01",
            "It is annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hahaha... That's my Tio: always the same! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right, this'll be my treat.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#0203F(The Anniversary Festival has made him more\x01",
            "enthusiastic than I would prefer.)\x02\x03",
            "#0201F(I will have to scold him later.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(T-Tio, you're looking a little sinister...)\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x2CC, 1)
    SetScenarioFlags(0x9C, 6)
    Return()

    # Function_33_5D5C end

    SaveToFile()

Try(main)
