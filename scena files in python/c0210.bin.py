from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0210.bin",                # FileName
        "c0210",                    # MapName
        "c0210",                    # Location
        0x000B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 11, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0210",                  # 0
        "Oscar",                  # 1
        "Morges",                 # 2
        "Bennet",                 # 3
        "Katerina",               # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Bracer Aeolia",          # 7
        "Tallys",                 # 8
        "Elsa",                   # 9
        "Momo",                   # 10
        "Pete",                   # 11
        "Brigitta",               # 12
        "Zeit",                   # 13
        "Harold",                 # 14
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21100.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
        "chr/ch22200.itc",                   # 09
        "chr/ch20300.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
        "chr/ch09300.itc",                   # 0C
        "chr/ch32100.itc",                   # 0D
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(58540,   0,       -2329,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(53500,   0,       5010,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(53500,   0,       6010,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(57319,   0,       -1980,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-65370,  0,       2009,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-3630,   0,       3509,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-3569,   0,       2450,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(2589,    0,       1320,    225,  404,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(2089,    0,       2250,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_407",          # 02, 2
        "Function_3_89C",          # 03, 3
        "Function_4_91C",          # 04, 4
        "Function_5_936",          # 05, 5
        "Function_6_10FA",         # 06, 6
        "Function_7_4E36",         # 07, 7
        "Function_8_532F",         # 08, 8
        "Function_9_545C",         # 09, 9
        "Function_10_6BA2",        # 0A, 10
        "Function_11_6CF1",        # 0B, 11
        "Function_12_7EFB",        # 0C, 12
        "Function_13_80CD",        # 0D, 13
        "Function_14_9329",        # 0E, 14
        "Function_15_9495",        # 0F, 15
        "Function_16_9685",        # 10, 16
        "Function_17_9689",        # 11, 17
        "Function_18_B8AA",        # 12, 18
        "Function_19_C791",        # 13, 19
        "Function_20_D181",        # 14, 20
        "Function_21_D3C4",        # 15, 21
        "Function_22_D743",        # 16, 22
        "Function_23_D7E3",        # 17, 23
        "Function_24_DBBF",        # 18, 24
        "Function_25_DDA9",        # 19, 25
        "Function_26_DE49",        # 1A, 26
        "Function_27_EC87",        # 1B, 27
        "Function_28_EDBD",        # 1C, 28
        "Function_29_EEA7",        # 1D, 29
        "Function_30_F50E",        # 1E, 30
        "Function_31_FA9D",        # 1F, 31
        "Function_32_10095",       # 20, 32
        "Function_33_104E0",       # 21, 33
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_370"),
        (2, "loc_37C"),
        (3, "loc_388"),
        (4, "loc_394"),
        (5, "loc_3A0"),
        (6, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_364")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_370")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_37C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_388")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_394")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3DB")

    Return()

    # Function_0_324 end

    def Function_1_3DC(): pass

    label("Function_1_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_406")
    OP_94(0xFE, 0xFFFEEFB2, 0x19A, 0xFFFEF926, 0xBE0, 0x3E8)
    Sleep(300)
    Jump("Function_1_3DC")

    label("loc_406")

    Return()

    # Function_1_3DC end

    def Function_2_407(): pass

    label("Function_2_407")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_44C")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_89B")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_497")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 120860, 0, 2360, 0)
    SetChrPos(0x10, 3090, 0, 4200, 90)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_89B")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E2")
    SetChrPos(0x8, 122290, 0, -2810, 90)
    SetChrPos(0x9, 56290, 0, 2020, 270)
    SetChrPos(0xA, 120860, 0, 2360, 0)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_528")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrPos(0x10, 3090, 0, 4200, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_587")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_582")

    label("loc_56B")

    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)

    label("loc_582")

    Jump("loc_89B")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5B8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_89B")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5EB")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_61E")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_651")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A0")
    SetChrPos(0x9, 120860, 0, 2360, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_89B")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_70D")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrPos(0x11, -72880, 0, 6950, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_775")
    SetChrPos(0x9, 119050, 0, -140, 180)
    SetChrPos(0xA, 119050, 0, -1650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_75A")
    SetChrPos(0x11, -72880, 0, 6950, 0)
    Jump("loc_770")

    label("loc_75A")

    SetChrPos(0x11, 2240, 0, 2350, 180)
    ClearChrFlags(0x14, 0x80)

    label("loc_770")

    Jump("loc_89B")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_799")
    SetChrPos(0xA, 55920, 1000, 10640, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7BD")
    SetChrPos(0xA, 55920, 1000, 10640, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrPos(0x10, 2090, 0, 3530, 180)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_89B")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_820")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_855")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrPos(0x9, 120860, 0, 2360, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_88D")
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_888")
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)

    label("loc_888")

    Jump("loc_89B")

    label("loc_88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_89B")
    SetChrFlags(0x10, 0x80)

    label("loc_89B")

    Return()

    # Function_2_407 end

    def Function_3_89C(): pass

    label("Function_3_89C")

    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_8E8")

    label("loc_8DC")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_91B")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_91B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_91B")

    label("loc_91B")

    Return()

    # Function_3_89C end

    def Function_4_91C(): pass

    label("Function_4_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_932")
    Call(0, 5)
    Jump("loc_935")

    label("loc_932")

    Call(0, 8)

    label("loc_935")

    Return()

    # Function_4_91C end

    def Function_5_936(): pass

    label("Function_5_936")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_962")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Call(0, 29)
    Return()

    label("loc_962")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9E")

    ChrTalk(
        0x8,
        (
            "How's your hunt for the ingredients\x01",
            "going, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Hand over ingredients]\x01",      # 0
            "[Not yet]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A36"),
        (1, "loc_A3D"),
        (SWITCH_DEFAULT, "loc_A9E"),
    )


    label("loc_A36")

    Call(0, 30)
    TalkEnd(0x8)
    Return()

    label("loc_A3D")


    ChrTalk(
        0x8,
        (
            "Okay, no biggie. Gimme a shout once you've\x01",
            "found everything, okay? I'm counting on ya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9E")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Shop\x01",                   # 1
            "Ask About Request\x01",      # 2
            "Leave\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B36")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B55")
    OP_AF(0xCE)
    Jump("loc_BA7")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B65")
    OP_AF(0xCD)
    Jump("loc_BA7")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B75")
    OP_AF(0xCC)
    Jump("loc_BA7")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B85")
    OP_AF(0xCB)
    Jump("loc_BA7")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B95")
    OP_AF(0xCA)
    Jump("loc_BA7")

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BA5")
    OP_AF(0xC9)
    Jump("loc_BA7")

    label("loc_BA5")

    OP_AF(0xC8)

    label("loc_BA7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(
        0x8,
        (
            "I want you to gather four pieces of Fish\x01",
            "Fillet and three Monster Eggs, if you're\x01",
            "up to the challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm starting to run pretty low on ingredients.\x01",
            "You'd be saving my hide if you don't mind\x01",
            "doing this for me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E49")

    ChrTalk(
        0x104,
        (
            "#0304FI think we can get some of that meat from\x01",
            "some fishy monsters.\x02\x03",
            "Birds 'n snakes are our best bet\x01",
            "for the eggs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWow. You know your stuff, Randy. Must\x01",
            "be from all that time spent in the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FI guess I have seen my fair share\x01",
            "of fights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FMany items dropped by monsters\x01",
            "can be used as ingredients.\x02\x03",
            "We'd do well to remember that. It'll aid\x01",
            "us in our investigations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 7)
    Jump("loc_F95")

    label("loc_E49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F95")

    ChrTalk(
        0x104,
        (
            "#0300FWell, the fishy monsters have all the meat\x01",
            "we need, while snakes and birds are\x01",
            "carrying our eggs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe should be able to find them with ease\x01",
            "by walking around on the highway.\x02\x03",
            "#0004FLet's check up on our equipment before we\x01",
            "head out, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thanks, bud. I'm counting on ya!\x02",
    )

    CloseMessageWindow()

    label("loc_F95")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_FA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB8")
    Jump("loc_FD4")

    label("loc_FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_FD4")

    Jump("loc_AD3")

    label("loc_FD9")

    Jump("loc_10EE")

    label("loc_FDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1039")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1039")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1058")
    OP_AF(0xCE)
    Jump("loc_10AA")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1068")
    OP_AF(0xCD)
    Jump("loc_10AA")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1078")
    OP_AF(0xCC)
    Jump("loc_10AA")

    label("loc_1078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1088")
    OP_AF(0xCB)
    Jump("loc_10AA")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1098")
    OP_AF(0xCA)
    Jump("loc_10AA")

    label("loc_1098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_10A8")
    OP_AF(0xC9)
    Jump("loc_10AA")

    label("loc_10A8")

    OP_AF(0xC8)

    label("loc_10AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10E9")

    label("loc_10B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CD")
    Jump("loc_10E9")

    label("loc_10CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_10E9")

    Jump("loc_FE8")

    label("loc_10EE")

    Jump("loc_10F6")

    label("loc_10F3")

    Call(0, 6)

    label("loc_10F6")

    TalkEnd(0x8)
    Return()

    # Function_5_936 end

    def Function_6_10FA(): pass

    label("Function_6_10FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_11E7")

    ChrTalk(
        0x8,
        (
            "You guys saved my skin. You guys should\x01",
            "pick out a loaf that looks interesting to you\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It'll be on me, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI appreciate it, Oscar. We'll be sure to take\x01",
            "you up on that offer eventually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E35")

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A1")

    ChrTalk(
        0x8,
        (
            "How's it going, Lloyd? Out on another\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, pretty much.\x02\x03",
            "#0001FHey, Oscar. This may sound weird, but has\x01",
            "anything out of the ordinary been happening\x01",
            "around here lately?\x02\x03",
            "Like, men in black suits hanging around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Out of the ordinary? Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, Bennet lost her cool and stormed\x01",
            "outta the store not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I have no clue what that was about, though.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A2")
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
        0x101,
        (
            "#0006FC'mon, Oscar. Don't make Bennet deal\x01",
            "with your cluelessness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FRegardless, it sounds like West Street\x01",
            "hasn't experienced anything strange.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_14A2")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000FO-Oh, really...?\x02\x03",
            "Isn't it your fault, Oscar? You can be as\x01",
            "dense as a brick at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wh-What? You really think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Well, it doesn't sound like West Street has\x01",
            "experienced anything strange.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1599")

    SetScenarioFlags(0xED, 2)
    Jump("loc_166B")

    label("loc_15A1")


    ChrTalk(
        0x8,
        (
            "Bennet baked a delicious loaf of bread and\x01",
            "had me sample it earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I gave her my honest opinion, and then she\x01",
            "started freakin' out and stormed outta here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The hell's her problem?\x02",
    )

    CloseMessageWindow()

    label("loc_166B")

    Jump("loc_4E35")

    label("loc_1670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176D")

    ChrTalk(
        0x8,
        (
            "Was there seriously a firefight at the\x01",
            "harbor yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Guess that means the mafia isn't playing\x01",
            "games anymore if they're willing to involve\x01",
            "the public in their spats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Can't they just chill and leave us alone?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EB")

    label("loc_176D")


    ChrTalk(
        0x8,
        (
            "And just when the bakery's sales were\x01",
            "on a steady incline...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish they'd just leave us common folk\x01",
            "alone, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EB")

    Jump("loc_4E35")

    label("loc_17F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1955")
    OP_93(0x8, 0x5A, 0x0)

    ChrTalk(
        0x8,
        "Hmm, where was the blanket again?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Bennet's been too antsy to sleep, now that she's\x01",
            "on the verge of completing her newest creation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's a mess, haha. Reminds me of sweet\x01",
            "little Lloyd when Cecile used to look after\x01",
            "you constantly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0003FH-Hey, don't drag me into this!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_199B")

    label("loc_1955")


    ChrTalk(
        0x8,
        (
            "Man, I'd better put Bennet to bed\x01",
            "before she ends up collapsing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199B")

    Jump("loc_4E35")

    label("loc_19A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D27")

    ChrTalk(
        0x8,
        "Yo, everyone. Who's the new face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, this is Sergeant Major Seeker.\x01",
            "She's from the Guardian Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FNice to meet you.\x02\x03",
            "Fran's actually told me quite a bit about\x01",
            "this bakery.\x02\x03",
            "I think she mentioned that a prodigy worked\x01",
            "here. Apparently, he was featured in the\x01",
            "Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ooooh, that article?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FThey featured you in the Crossbell Times?\x01",
            "That's sick, my man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt's not unexpected when his skills\x01",
            "are extraordinary, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. I was a little reluctant to participate, seeing\x01",
            "as how I'm still training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Didn't have much of a choice, though. Morges\x01",
            "kept pushing me to do it, since it'd help bring in\x01",
            "more sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was feelin' the pressure from the newest signature\x01",
            "creation I helped develop this month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, it's unlike you to feel any stress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI'll have to try some for myself, then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 3)
    Jump("loc_1DC2")

    label("loc_1D27")


    ChrTalk(
        0x8,
        (
            "Me, a genius? No way, man. Compared\x01",
            "to Morges, I still have a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've still got a ton of fundamentals I can\x01",
            "learn from Bennet, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC2")

    Jump("loc_4E35")

    label("loc_1DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE8")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F89")

    ChrTalk(
        0x153,
        (
            "#1110FWow, this place smells gooood! Hey mister,\x01",
            "what'cha doin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey there, missy. Just doing some baking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would you like to try a piece of our\x01",
            "delicious bread, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYeah, for sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FHey, now, don't go deciding things on your own.\x02\x03",
            "#0000F(Hmm, I don't think she has any recollection of\x01",
            "this bakery.)\x02\x03",
            "(It's looking pretty likely that she isn't\x01",
            "from Crossbell...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_201D")

    label("loc_1F89")


    ChrTalk(
        0x8,
        (
            "Don't be stingy, Lloyd. You gotta buy something\x01",
            "tasty for KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd recommend one of our limited-time products,\x01",
            "like the honey milk bread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201D")

    Jump("loc_4E35")

    label("loc_2022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A2")

    ChrTalk(
        0x8,
        "Hey, I heard you managed to find the kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What a relief. I bet his parents were worried\x01",
            "sick from losing him in that insane crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, I'm glad it all turned out okay.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FQuick question for you, Oscar.\x02\x03",
            "#0000FHave you ever been to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "I'm afraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not particularly interested in\x01",
            "theme parks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wendy goes there pretty often to have fun\x01",
            "when she needs to blow off steam, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, seems like it's the hip new trend\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It's become a staple for dates and family outings.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 4)
    Jump("loc_232B")

    label("loc_22A2")


    ChrTalk(
        0x8,
        (
            "On that note, Morges is giving me the\x01",
            "afternoon off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Figured I'd go wander around the city.\x01",
            "Not too interested in theme parks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232B")

    Jump("loc_4E35")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_24F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2475")

    ChrTalk(
        0x8,
        (
            "What's up, pals? Did you all manage to\x01",
            "find the kid yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FNot yet. We've figured out some important clues\x01",
            "to his whereabouts, so we're getting close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That so? Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Poor lil' fella must be scared outta his mind.\x01",
            "I hope you find him soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3300FI hope so, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24ED")

    label("loc_2475")


    ChrTalk(
        0x8,
        "I'm glad that you're chugging along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Poor lil' fella must be scared outta his mind.\x01",
            "I hope you find him soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24ED")

    Jump("loc_4E35")

    label("loc_24F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BF")

    ChrTalk(
        0x8,
        "Good to see you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who's the lovely lil' lady? What are\x01",
            "you two doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FWe're trying to find a missing person.\x02\x03",
            "#0001FHave you seen the child in this photo?\x02",
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
        0x8,
        "Hey, isn't that Colin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWait, you know him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah, he lives in the Residential District, I think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His family comes by here to buy bread\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Come to think of it, I haven't seen them today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, I didn't see them around here during the\x01",
            "parade, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThought so... All right, thanks for the information.\x01",
            "You've been a huge help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_282D")

    label("loc_27BF")


    ChrTalk(
        0x8,
        "I know that kid, but he hasn't been in here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I don't think I saw him pass by outside, either.\x02",
    )

    CloseMessageWindow()

    label("loc_282D")

    Jump("loc_4E35")

    label("loc_2832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_299D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2924")

    ChrTalk(
        0x8,
        (
            "Welcome to M--oh, it's Lloyd and the gang.\x01",
            "What's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Business is outta control, so we've fired up\x01",
            "the oven to bake more bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Didn't think it was possible to fit that many\x01",
            "people inside the bakery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2998")

    label("loc_2924")


    ChrTalk(
        0x8,
        "I'm shocked at how many people came this year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The old man told me that he's never seen\x01",
            "anything like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2998")

    Jump("loc_4E35")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A28")

    ChrTalk(
        0x8,
        (
            "Sounds like we're on the parade route\x01",
            "this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope no one gets hurt. Lotta people\x01",
            "out there frolicking about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E35")

    label("loc_2A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAF")

    ChrTalk(
        0x8,
        (
            "The free samples Bennet baked are\x01",
            "flying off of the tray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We're going to rake in the dough today.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B3C")

    label("loc_2AAF")


    ChrTalk(
        0x8,
        "Bennet thought to start handing out free samples.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A brilliant idea, if I do say so myself.\x01",
            "We're going to rake in the dough today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3C")

    Jump("loc_4E35")

    label("loc_2B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C63")

    ChrTalk(
        0x8,
        "Yo, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been working like dogs 'cause of the festival.\x01",
            "We're selling thrice the volume of bread\x01",
            "compared to a normal day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was worried that MacDowell gettin' hurt\x01",
            "would affect business, but I guess you\x01",
            "just can't kill the love for bread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CC9")

    label("loc_2C63")


    ChrTalk(
        0x8,
        (
            "I tried baking a new type of bread to commemorate\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wanna try some?\x02",
    )

    CloseMessageWindow()

    label("loc_2CC9")

    Jump("loc_4E35")

    label("loc_2CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E52")

    ChrTalk(
        0x8,
        (
            "A bunch of police officers have been coming\x01",
            "here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're in civilian clothing, but I can't shake the feeling\x01",
            "that they're on an undercover investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You think they're staking something out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FQuite perceptive of you, Oscar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, he's always had a knack for reading\x01",
            "between the lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, surely you jest.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2EBC")

    label("loc_2E52")


    ChrTalk(
        0x8,
        (
            "A bunch of police officers have been coming\x01",
            "here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I think they're staking something out.\x02",
    )

    CloseMessageWindow()

    label("loc_2EBC")

    Jump("loc_4E35")

    label("loc_2EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_33F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FE")

    ChrTalk(
        0x8,
        (
            "Did you guys know that Arc en Ciel has a new\x01",
            "production they'll be performing next month?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not interested in that kinda stuff, but the\x01",
            "customers have been incessantly discussing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We could go together if you're interested in\x01",
            "watching it, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I managed to score me some tickets.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FWait, WHAT?! Oscar, how'd you manage to\x01",
            "get those?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "One of the customers gave 'em to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know, the sexy lady who lives in the\x01",
            "apartments down the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I throw her an extra loaf of bread for free every once\x01",
            "in a while, so she gave me the tickets as thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_END)), "loc_32C3")
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
        "#0300F(Ya don't think he's talkin 'bout...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(I am certain that he is referring to Ilya.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Classic Oscar. I don't think he understands\x01",
            "the gravity of his actions sometimes.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F6")

    label("loc_32C3")


    ChrTalk(
        0x104,
        "#0300FY-Ya don't say? Pretty generous of her.\x02",
    )

    CloseMessageWindow()

    label("loc_32F6")

    SetScenarioFlags(0x0, 0)
    Jump("loc_33F2")

    label("loc_32FE")


    ChrTalk(
        0x8,
        (
            "She's a sexy lady that lives in the condos\x01",
            "down the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She drops by at six every morning and buys a\x01",
            "whole mountain of bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I give her one of our new products for free once\x01",
            "in a while, so she gave me the tickets as thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F2")

    Jump("loc_4E35")

    label("loc_33F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_37FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")

    ChrTalk(
        0x8,
        (
            "You know how our street continues out on\x01",
            "to the highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's been a real pain dealing with the traffic\x01",
            "from all of these orbal cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FNot to mention, shipping companies are\x01",
            "resorting to using orbal trucks to make\x01",
            "their deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah. I noticed something kinda weird, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's been a black truck hanging around here\x01",
            "lately. I noticed it when I got in at the crack of\x01",
            "dawn to prepare some bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Word on the street is that it belongs\x01",
            "to Revache. Any truth to that claim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm... They could be using the West Crossbell\x01",
            "Highway as a smuggling route between here\x01",
            "and the Empire.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Probably usin' it for some shady\x01",
            "black-market stuff.)\x02\x03",
            "(It showed up in Mainz, too. Those guys have\x01",
            "been haulin' their asses all over the place.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 1)
    Jump("loc_37FA")

    label("loc_3727")


    ChrTalk(
        0x8,
        (
            "There's been a black truck hanging around here\x01",
            "lately. I noticed it when I got in at the crack of\x01",
            "dawn to prepare some bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Word on the street is that it belongs\x01",
            "to Revache? Any truth to that claim?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FA")

    Jump("loc_4E35")

    label("loc_37FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B11")

    ChrTalk(
        0x8,
        "Hey, the gang's here to visit again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Aren't you guys popular? The customers\x01",
            "have been chitchatting about you lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, I'm flattered.\x02\x03",
            "We've mostly been doing simple support\x01",
            "requests to help out the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI'm glad our work has been paying off. We're\x01",
            "building quite the reputation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know who's even more popular, though?\x01",
            "That pup of yours. He's the talk of the town.\x02",
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
        0x101,
        "#0006FZeit? Figured as much. Ever the glory hound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I catch a glimpse of him when I'm working\x01",
            "in the morning and think to myself, 'Damn,\x01",
            "that's one cool lookin' dog.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You've gotta introduce me sometime, man. You\x01",
            "know I love dogs!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 0)
    Jump("loc_3BD4")

    label("loc_3B11")


    ChrTalk(
        0x8,
        (
            "That pup of yours is the hot topic\x01",
            "around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You've gotta introduce me sometime, man. You\x01",
            "know I love dogs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll feed him some of our new bread as\x01",
            "a little doggie treat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD4")

    Jump("loc_4E35")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEA")

    ChrTalk(
        0x8,
        (
            "Bennet's a pro at baking bread, probably 'cause\x01",
            "she's Morges' daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She taught me the ABCs of breadmaking when\x01",
            "I first began my apprenticeship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's hard to approach, though. I get the\x01",
            "impression that she's always pissed off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3D8F")

    label("loc_3CEA")


    ChrTalk(
        0x8,
        (
            "Kind of a waste for a pretty number like her\x01",
            "to be angry all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, maybe I'll bake her some milk bread.\x01",
            "Some calcium ought to help her calm down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D8F")

    Jump("loc_4E35")

    label("loc_3D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E9A")

    ChrTalk(
        0x8,
        (
            "Our daily special is made with wheat and\x01",
            "vegetables sourced from Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bread produced in the Republic is cheaper these\x01",
            "days, but they pay for it in quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FCan't say I'm surprised that you're picky\x01",
            "'bout your ingredients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E35")

    label("loc_3E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4143")

    ChrTalk(
        0x8,
        (
            "You're all here earlier than normal.\x01",
            "Any particular reason?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F85")

    ChrTalk(
        0x101,
        (
            "#0000FJust doing our rounds, is all.\x02\x03",
            "Actually, you're always here bright and early,\x01",
            "aren't you, Oscar? That's a baker for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4026")

    label("loc_3F85")


    ChrTalk(
        0x101,
        (
            "#0006FYou're the one who gave us a support request.\x02\x03",
            "#0000FBut funny of you to say that, since you're always\x01",
            "here bright and early. That's a baker for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4026")


    ChrTalk(
        0x102,
        (
            "#0100FGood morning, Oscar. It must be nice working\x01",
            "in a bakery that smells this lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know it! That's the smell of our new\x01",
            "monthly bread. There's some on the shelf\x01",
            "over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now's the best time to have some. They're out\x01",
            "of this world when they're fresh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_421F")

    label("loc_4143")


    ChrTalk(
        0x8,
        (
            "We actually begin baking at three in the morning.\x01",
            "When I first started working here, I was surprised\x01",
            "at how refreshing I found it to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's when I knew I was in the right place\x01",
            "and was meant to be a baker.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421F")

    Jump("loc_4E35")

    label("loc_4224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_END)), "loc_46FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_468D")

    ChrTalk(
        0x8,
        "Hey, Lloyd. You're back already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's been what, half a year? No, a whole year since\x01",
            "we last saw each other? Wow, time sure flies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FHey, man.\x01",
            "It's been three years already, you already said\x02\x03",
            "so yourself. That fuzzy memory of yours\x01",
            "never seems to change...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey, don't sweat the finer details!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, let's see. You got a lil' taller,\x01",
            "but I see you still haven't outgrown\x01",
            "that baby face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FUgh... Shut up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHaha, burn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FHeehee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204FHehe, poor Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006FGeez, enough already.\x02\x03",
            "#0000FHey, I heard that you've become a pro\x01",
            "at baking.\x02\x03",
            "Wendy mentioned it in a letter that you\x01",
            "invent new styles of bread every month.\x01",
            "They're apparently a hit, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nah, man. I'm still a rookie. The path of a baker\x01",
            "is a long and treacherous one, I can't get\x01",
            "complacent that easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do think that this month's bread came out\x01",
            "splendidly, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Would you all like to try some?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FFree bread? I'm all for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FEverything looks delicious, I can't decide on\x01",
            "which one I'd like to try.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_46F6")

    label("loc_468D")


    ChrTalk(
        0x8,
        (
            "I've got a lot of training ahead of me, but I'm\x01",
            "pretty confident in this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Try it sometime.\x02",
    )

    CloseMessageWindow()

    label("loc_46F6")

    Jump("loc_4C10")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0E")

    ChrTalk(
        0x8,
        "Hey, Lloyd. Have you bumped into Wendy yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I actually ran into her earlier.\x02\x03",
            "She's become quite the engineer, but, uh...\x02\x03",
            "#0003F...knowing how she behaves, aren't we moments\x01",
            "away from her getting ticked off at a customer\x01",
            "and smacking them with a wrench?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, I hear you there, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure she'll be fine. She knows how to\x01",
            "moderate herself these days, despite\x01",
            "her appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She'll probably hold back and settle for a light\x01",
            "thwacking.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0105F(This is no laughing matter...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Oh, Wendy. How can you be such\x01",
            "a cutie, and yet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(It would be wise of you to behave yourself\x01",
            "around her, Randy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_4C10")

    label("loc_4A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B74")

    ChrTalk(
        0x8,
        (
            "Oh, yeah. I noticed that more police officers\x01",
            "have been visiting the bakery lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Probably something to do with that law\x01",
            "office around here. I serve the guy who\x01",
            "runs it every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Either way, I'm grateful. It's my honor to be able\x01",
            "to wipe the serious look off of old men's faces\x01",
            "as they bite into my creations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C10")

    label("loc_4B74")


    ChrTalk(
        0x8,
        (
            "I noticed that more police officers have\x01",
            "been visiting the bakery lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They habitually stop by here before they head\x01",
            "to the law office nearby.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C10")

    Jump("loc_4E35")

    label("loc_4C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCD")

    ChrTalk(
        0x101,
        (
            "#0000FHey, I heard that you've become a pro\x01",
            "at baking.\x02\x03",
            "Wendy mentioned it in a letter about how you\x01",
            "invent new styles of bread every month.\x01",
            "They're apparently a hit, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Nah, man. I'm still a rookie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The path of a baker is a long and treacherous\x01",
            "one, so I can't get complacent that easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do think that this month's bread came out\x01",
            "splendidly, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Would you all like to try some?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E35")

    label("loc_4DCD")


    ChrTalk(
        0x8,
        (
            "I've got a lot of training ahead of me, but I'm\x01",
            "pretty confident in this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Here, try some.\x02",
    )

    CloseMessageWindow()

    label("loc_4E35")

    Return()

    # Function_6_10FA end

    def Function_7_4E36(): pass

    label("Function_7_4E36")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(54330, 1500, 1490, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, 52480, 0, 1350, 90)
    SetChrPos(0xEF, 51860, 0, 2300, 90)
    SetChrPos(0x153, 52000, 0, 260, 90)
    OP_93(0x8, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    ChrTalk(
        0x8,
        (
            "Hey, Lloyd. Don't think you've shown your\x01",
            "face around here this week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're here pretty often, so I figured that\x01",
            "something might have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThere's an explanation for that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FWow, what a funny-looking hat! It's sooo tall!\x02\x03",
            "#1104F*sniff* What's that smell? It's really nice!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "Uhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "She your sister or something, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FNo. You know I don't have one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, I'm just bustin' your chops. Relax, man!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5102")

    ChrTalk(
        0x102,
        (
            "#0100FThis girl's name is KeA. We're looking after her\x01",
            "due to some...circumstances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CE")

    label("loc_5102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5172")

    ChrTalk(
        0x103,
        (
            "#0200FThis child's name is KeA. Due to some unforeseen\x01",
            "circumstances, she is under our care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CE")

    label("loc_5172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_51CE")

    ChrTalk(
        0x104,
        (
            "#0300FThis lil' lady's name is KeA. Some events led to\x01",
            "us takin' care of her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51CE")


    ChrTalk(
        0x8,
        "Huh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, take this as a symbol of our newfound\x01",
            "friendship! You can drink it if you want.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA received a bottle of milk.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#1105FOoh, really?!\x02\x03",
            "#1109F*chug* That was tasty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha! She's an amusing one, ain't she?!\x01",
            "We got it from Armorica, if you're interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, thanks for dealing with us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 5)
    EventEnd(0x5)
    Return()

    # Function_7_4E36 end

    def Function_8_532F(): pass

    label("Function_8_532F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5455")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_534A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5450")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_539B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_53BA")
    OP_AF(0xCE)
    Jump("loc_540C")

    label("loc_53BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53CA")
    OP_AF(0xCD)
    Jump("loc_540C")

    label("loc_53CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_53DA")
    OP_AF(0xCC)
    Jump("loc_540C")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53EA")
    OP_AF(0xCB)
    Jump("loc_540C")

    label("loc_53EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53FA")
    OP_AF(0xCA)
    Jump("loc_540C")

    label("loc_53FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_540A")
    OP_AF(0xC9)
    Jump("loc_540C")

    label("loc_540A")

    OP_AF(0xC8)

    label("loc_540C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_544B")

    label("loc_541B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_542F")
    Jump("loc_544B")

    label("loc_542F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_544B")

    Jump("loc_534A")

    label("loc_5450")

    Jump("loc_5458")

    label("loc_5455")

    Call(0, 9)

    label("loc_5458")

    TalkEnd(0x9)
    Return()

    # Function_8_532F end

    def Function_9_545C(): pass

    label("Function_9_545C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5608")

    ChrTalk(
        0x9,
        (
            "I heard all about it. You guys gathered\x01",
            "up some ingredients for us, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Great, thanks for helping us out. Now we can\x01",
            "focus our attention on baking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNo problem. Don't hesitate to contact us if\x01",
            "you need any more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FWe won't even break a sweat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This is promising. You all seem reliable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe. I'll be sure to leave the problem solving\x01",
            "to you next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 6)
    Jump("loc_6BA1")

    label("loc_5608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_574F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570D")

    ChrTalk(
        0x9,
        (
            "Shoot, the delivery is late. We still don't\x01",
            "have our ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll have to use our stock more conservatively\x01",
            "today. Can't risk running out of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I feel ashamed for not being better prepared.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_574A")

    label("loc_570D")


    ChrTalk(
        0x9,
        (
            "*sigh* Here's to hoping they'll get delivered\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574A")

    Jump("loc_6BA1")

    label("loc_574F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_58A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584E")

    ChrTalk(
        0x9,
        (
            "Oscar and I gave Bennet's new bread high\x01",
            "praise. She seemed dissatisfied with it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I thought the flavors were great, but I wonder\x01",
            "if it had to do with Oscar's reaction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I don't really get it, but whatever.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_589F")

    label("loc_584E")


    ChrTalk(
        0x9,
        (
            "I don't understand my daughter at all. I think\x01",
            "she's getting to that age...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_589F")

    Jump("loc_6BA1")

    label("loc_58A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595F")

    ChrTalk(
        0x9,
        (
            "You smell that? Bennet's gone and baked another\x01",
            "loaf of bread with a mighty fine smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got high hopes for this one. I can't wait\x01",
            "to try it out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_59BB")

    label("loc_595F")


    ChrTalk(
        0x9,
        (
            "Bennet takes baking seriously, and her\x01",
            "results show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "That's a fine-smelling loaf.\x02",
    )

    CloseMessageWindow()

    label("loc_59BB")

    Jump("loc_6BA1")

    label("loc_59C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5ADE")

    ChrTalk(
        0x9,
        (
            "We've seen a surge in customers that\x01",
            "are also travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It brightens my mood to see how much people\x01",
            "care about our bread. Gotta hand it to Oscar\x01",
            "for all his hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We were recently featured in the Crossbell Times,\x01",
            "and it was all thanks to his efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_5ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C21")

    ChrTalk(
        0x9,
        (
            "Bennet's been fervently researching baking\x01",
            "theory. She ended up rethinking her approach\x01",
            "on how to bake her newest bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We decide on our newest feature bread\x01",
            "democratically. We each bake a loaf of\x01",
            "bread, taste it, then vote on a winner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It's a good method, if I do say so myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5CEE")

    label("loc_5C21")


    ChrTalk(
        0x9,
        (
            "I used to give the final say after sampling their\x01",
            "new breads, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Oscar and Bennet are fully qualified to make\x01",
            "the call these days. Voting on the best bread is\x01",
            "probably the fairest method.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CEE")

    Jump("loc_6BA1")

    label("loc_5CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4D")

    ChrTalk(
        0x9,
        "Bennet's been hogging the kitchen lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Damn it...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5D78")

    label("loc_5D4D")


    ChrTalk(
        0x9,
        "Damn it, I want to bake bread, too...\x02",
    )

    CloseMessageWindow()

    label("loc_5D78")

    Jump("loc_6BA1")

    label("loc_5D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5E31")

    ChrTalk(
        0x9,
        (
            "The rush is calming down. Perhaps we should\x01",
            "use this opportunity to take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm starting to get worn out from all the\x01",
            "physical labor baking takes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_5E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5ED4")

    ChrTalk(
        0x9,
        "I can't help but sing the parade music!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They play the same song for the parade\x01",
            "every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hearing it makes me feel like a kid again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_5ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F97")

    ChrTalk(
        0x9,
        (
            "Today's parade is the height of the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got our work cut out for us. We should\x01",
            "prepare ourselves for the oncoming rush\x01",
            "as soon as the parade ends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_5F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_600F")

    ChrTalk(
        0x9,
        "Heave-ho, heave-ho...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're having trouble keeping up with the\x01",
            "torrent of customers pouring in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_600F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_611E")

    ChrTalk(
        0x9,
        (
            "Do my eyes deceive me? Bennet, of all people,\x01",
            "is handling the stall? Color me surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She's even trying her best to maintain a\x01",
            "smile for the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're going to make your dad worry if you try\x01",
            "too hard to change, dummy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_615F")

    label("loc_611E")


    ChrTalk(
        0x9,
        "She's giving it her all, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, color me surprised.\x02",
    )

    CloseMessageWindow()

    label("loc_615F")

    Jump("loc_6BA1")

    label("loc_6164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_61EA")

    ChrTalk(
        0x9,
        (
            "Bennet's stepped it up big time ever since\x01",
            "I hired Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's comfort in knowing you have an\x01",
            "adept pupil.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BA1")

    label("loc_61EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6205")
    Call(0, 12)
    Jump("loc_626E")

    label("loc_6205")


    ChrTalk(
        0x9,
        (
            "Oscar's no slouch, either, and he's handsome,\x01",
            "to boot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "The shop's future is secured... Hahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_626E")

    Jump("loc_6BA1")

    label("loc_6273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_630D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_628F")
    Call(0, 10)
    Jump("loc_6308")

    label("loc_628F")


    ChrTalk(
        0x9,
        (
            "I should start thinking about my next signature\x01",
            "creation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It's not fair for me to keep leaving it up to Oscar.\x02",
    )

    CloseMessageWindow()

    label("loc_6308")

    Jump("loc_6BA1")

    label("loc_630D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6484")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6329")
    Call(0, 10)
    Jump("loc_647F")

    label("loc_6329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63D2")

    ChrTalk(
        0x9,
        (
            "Bennet's challenged Oscar to a bake-off\x01",
            "a bunch of times but hasn't had any luck\x01",
            "besting him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Things are heating up between the two of them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_647F")

    label("loc_63D2")


    ChrTalk(
        0x9,
        "Oscar's bread is fairly popular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It goes beyond the ingredients he uses. He\x01",
            "uses complex techniques and great intuition\x01",
            "to apply the ingredients to their fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_647F")

    Jump("loc_6BA1")

    label("loc_6484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_660B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6599")

    ChrTalk(
        0x9,
        (
            "I've been entrusting our monthly signature\x01",
            "creations to Oscar as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That kid's got talent, and he pours his heart\x01",
            "and soul into it. Not to mention, he's got\x01",
            "great intuition for baking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm running out of things to teach the kid.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6606")

    label("loc_6599")


    ChrTalk(
        0x9,
        "Oscar has great baker's intuition.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, it's mostly cause Bennet's got a fierce\x01",
            "rivalry with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6606")

    Jump("loc_6BA1")

    label("loc_660B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_67C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671D")

    ChrTalk(
        0x9,
        (
            "Not many people know this, but the key to my\x01",
            "bread is in the fragrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I always take into consideration what kind of\x01",
            "fragrance my new creations will emit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You essentially have to draw out the full\x01",
            "potential of the raw ingredients.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_67C4")

    label("loc_671D")


    ChrTalk(
        0x9,
        (
            "I started my line of signature creations as\x01",
            "a way of using ingredients in a fun\x01",
            "and creative manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They've been fairly successful with\x01",
            "the customers, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C4")

    Jump("loc_6BA1")

    label("loc_67C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_691F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685E")

    ChrTalk(
        0x9,
        "Hey, the second batch is ready!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mmm, now that's what I call fragrant. That smell\x01",
            "is why I'll never quit baking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_691A")

    label("loc_685E")


    ChrTalk(
        0x9,
        "We start baking at 5 in the morning, sharp.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We start our morning by preparing the dough,\x01",
            "and then it's full steam ahead in the ovens.\x01",
            "The bakery gets doused in a pleasant aroma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_691A")

    Jump("loc_6BA1")

    label("loc_691F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A26")

    ChrTalk(
        0x9,
        (
            "My daughter hates losing, so her fierce\x01",
            "rivalry with Oscar only continues to heat up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And to think that she had no intention of becoming\x01",
            "a baker at all. Why the sudden change?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "*sigh* What's going on in that head of hers?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6A52")

    label("loc_6A26")


    ChrTalk(
        0x9,
        "I don't understand my daughter at all.\x02",
    )

    CloseMessageWindow()

    label("loc_6A52")

    Jump("loc_6BA1")

    label("loc_6A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0B")

    ChrTalk(
        0x9,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've cleared the front of the bakery and\x01",
            "turned it into a small cafe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Pretty handy if you want to sit down and grab\x01",
            "a bite, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6BA1")

    label("loc_6B0B")


    ChrTalk(
        0x9,
        (
            "We've cleared the front of the bakery and\x01",
            "turned it into a small cafe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Check out the menu when you've got the\x01",
            "chance. We serve drinks, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA1")

    Return()

    # Function_9_545C end

    def Function_10_6BA2(): pass

    label("Function_10_6BA2")


    ChrTalk(
        0xFE,
        (
            "Welcome! Take a look at our sales. This\x01",
            "month's special is discounted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... This type of coffee would probably go\x01",
            "well with the monthly special. Here's the recipe\x01",
            "if you want to brew it yourself.\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1D3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x17)
    Return()

    # Function_10_6BA2 end

    def Function_11_6CF1(): pass

    label("Function_11_6CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D23")
    TurnDirection(0x0, 0xA, 0)
    OP_4B(0xA, 0xFF)
    Call(0, 31)
    Return()

    label("loc_6D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F01")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E53")

    ChrTalk(
        0xA,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Did you get the ingredients?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Hand over ingredients]\x01",      # 0
            "[Not yet]\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DF3"),
        (1, "loc_6DFB"),
        (SWITCH_DEFAULT, "loc_6E4E"),
    )


    label("loc_6DF3")

    Call(0, 32)
    Jump("loc_6E4E")

    label("loc_6DFB")


    ChrTalk(
        0xA,
        (
            "I see... I'd appreciate it if you could get it\x01",
            "done as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E4E")

    label("loc_6E4E")

    Jump("loc_6EFC")

    label("loc_6E53")


    ChrTalk(
        0xFE,
        "In case you forgot, I need two Monster Eggs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Get it done as soon as possible please, I need\x01",
            "them for my new secret bread. Don't tell\x01",
            "Oscar about this, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFC")

    Jump("loc_7EF7")

    label("loc_6F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7069")

    ChrTalk(
        0xFE,
        "Thanks for helping me out. You're a lifesaver.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F94")

    ChrTalk(
        0xFE,
        (
            "Heheheh... I'll be sure to outdo Oscar with my\x01",
            "latest creation...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_701B")

    label("loc_6F94")


    ChrTalk(
        0xFE,
        (
            "It may be a little bit too late, but...\x01",
            "don't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grrr... Damn that Oscar! I'll definitely beat\x01",
            "him next time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701B")


    ChrTalk(
        0x101,
        (
            "#0000FKeep persevering through your training. I know\x01",
            "you can do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_7069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7077")
    Jump("loc_7EF7")

    label("loc_7077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_71B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7147")

    ChrTalk(
        0xFE,
        (
            "Hahaha... I've finally done it. I've baked my\x01",
            "magnum opus!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This fragrant walnut loaf I spent the entire\x01",
            "month researching...it's finally complete!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come at me, Oscar!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_71B3")

    label("loc_7147")


    ChrTalk(
        0xFE,
        (
            "Hahaha... I've finally done it. I've baked my\x01",
            "magnum opus!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've got you now, Oscar! Admit defeat!\x02",
    )

    CloseMessageWindow()

    label("loc_71B3")

    Jump("loc_7EF7")

    label("loc_71B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_720E")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Zzz... Zzz...\x01",
            "Two hours of fermentation...at 144 degrees...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_720E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72DE")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Times recently featured our bakery\x01",
            "in their newspaper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They thought it'd be a good idea to interview\x01",
            "Oscar, rather than my father or myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, why?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_734E")

    label("loc_72DE")


    ChrTalk(
        0xFE,
        (
            "What is this 'young prodigious patissier'\x01",
            "crap they're calling him...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh! I'll never accept this...\x02",
    )

    CloseMessageWindow()

    label("loc_734E")

    Jump("loc_7EF7")

    label("loc_7353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_74C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7442")

    ChrTalk(
        0xFE,
        "I'm developing a new style of bread.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've incorporated a ton of honey and walnuts\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm still working out the kinks in the baking process,\x01",
            "but I think I've got a decent chance at success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_74BD")

    label("loc_7442")


    ChrTalk(
        0xFE,
        (
            "We were evenly matched in sales during\x01",
            "the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just you wait, Oscar! I've got you this time!\x02",
    )

    CloseMessageWindow()

    label("loc_74BD")

    Jump("loc_7EF7")

    label("loc_74C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757D")
    OP_93(0xA, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "*kneading viciously*\x01",
            "There, I'd say this dough is about ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got you this time... I'm going to leave\x01",
            "you speechless, you handsome jerk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7602")

    label("loc_757D")


    ChrTalk(
        0xFE,
        (
            "I'm making an original loaf of bread for the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please look forward to it.\x01",
            "It's going to be naantastic!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7602")

    Jump("loc_7EF7")

    label("loc_7607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_769B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7622")
    Call(0, 12)
    Jump("loc_7696")

    label("loc_7622")

    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0xFE,
        (
            "Anyway, is the kitchen open yet?\x01",
            "I wanna use it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be fine with just using it for a\x01",
            "short while!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7696")

    Jump("loc_7EF7")

    label("loc_769B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_77E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778E")
    OP_93(0xA, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "Huh? Where'd the high-quality flour\x01",
            "I'd secured go?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That crummy dad of mine... Stop using\x01",
            "other people's stuff as you please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How am I supposed to make my bread now?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_77DC")

    label("loc_778E")


    ChrTalk(
        0xFE,
        (
            "Grr... This is why I hate my dad!\x01",
            "Why's he have to be such a\x01",
            "numbskull?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77DC")

    Jump("loc_7EF7")

    label("loc_77E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_799C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791F")

    ChrTalk(
        0xFE,
        (
            "The first step to baking a good bread is to\x01",
            "choose the right ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goods are more readily available since the\x01",
            "introduction of the Transcontinental Railroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll try using flour produced in\x01",
            "Ored State this time. I feel like I can\x01",
            "make some great bread from it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7997")

    label("loc_791F")


    ChrTalk(
        0xFE,
        "I-I'm at least as skilled as Oscar is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't lost yet. I'll pull ahead by improving\x01",
            "upon the ingredients!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7997")

    Jump("loc_7EF7")

    label("loc_799C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_79EE")

    ChrTalk(
        0xFE,
        "I finished baking today's bread.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "D-Do you want to try it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_79EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AE7")

    ChrTalk(
        0xFE,
        (
            "All right, damn it. I'll admit Oscar's talented.\x01",
            "He rose up to the occasion and was accepted\x01",
            "under my dad's tutelage in just two years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I haven't conceded to him, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll leave him speechless tomorrow!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7B3C")

    label("loc_7AE7")


    ChrTalk(
        0xFE,
        "Ciabatta believe it, Oscar! Heheheh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll leave you speechless tomorrow!\x02",
    )

    CloseMessageWindow()

    label("loc_7B3C")

    Jump("loc_7EF7")

    label("loc_7B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7BB0")

    ChrTalk(
        0xFE,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Per usual, the only thing that has any\x01",
            "time to rest around here is the dough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_7BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CF2")

    ChrTalk(
        0xFE,
        (
            "Oscar marched up to the bakery and told\x01",
            "my dad that he wanted to become his\x01",
            "apprentice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They negotiated the terms and started\x01",
            "training ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's become a top shelf baker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Grrr... I can't believe Dad doesn't consider\x01",
            "his own daughter to be his top disciple.\x01",
            "That jerk!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7D95")

    label("loc_7CF2")


    ChrTalk(
        0xFE,
        (
            "I've been a baker for WAY longer than\x01",
            "Oscar has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, he'll come crawling back to me\x01",
            "once he sees how much better I am.\x01",
            "Too bad I won't be forgiving him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D95")

    Jump("loc_7EF7")

    label("loc_7D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DEB")

    ChrTalk(
        0xFE,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please pay your bill at the register.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_7DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9A")

    ChrTalk(
        0xFE,
        "Our newest style of bread is flying off the shelf.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm the shop's main attraction, so I should have\x01",
            "been the one to make it...\x01",
            "*grumble* *grumble*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7EF7")

    label("loc_7E9A")


    ChrTalk(
        0xFE,
        (
            "I should have been the one to make this\x01",
            "month's new style of bread.\x01",
            "*grumble* *grumble*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF7")

    TalkEnd(0xFE)
    Return()

    # Function_11_6CF1 end

    def Function_12_7EFB(): pass

    label("Function_12_7EFB")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0xA,
        (
            "Have you considered showing your face in the\x01",
            "bakery every once in a while, Dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You've been holed up in this kitchen\x01",
            "all the time lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hah, my foolish little daughter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The reason I stay back here is obvious.\x01",
            "It's because Oscar is a handsome lad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Who needs my ugly mug when we've got a\x01",
            "ladies' man? Our female demographic has\x01",
            "doubled! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Ugh. You're such a weirdo, Dad.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_7EFB end

    def Function_13_80CD(): pass

    label("Function_13_80CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8132")

    ChrTalk(
        0xFE,
        "What's the matter with Bennet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She stormed out of the store a moment ago.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9325")

    label("loc_8132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_81B2")

    ChrTalk(
        0xFE,
        "There's a nice aroma filling the store today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm, I wonder what type of bread\x01",
            "they made this time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9325")

    label("loc_81B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_834A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B6")

    ChrTalk(
        0xFE,
        (
            "I bought bread from this bakery and made\x01",
            "my mom and dad eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They told me they wanted to eat it every day,\x01",
            "and I silently nodded my head in agreement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great success! Now I can come to\x01",
            "this bakery whenever I want!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8345")

    label("loc_82B6")


    ChrTalk(
        0xFE,
        (
            "Hmm, they've got a butter bread available\x01",
            "this month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That looks super delicious... Maybe I'll buy\x01",
            "one and eat it fresh at the cafe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8345")

    Jump("loc_9325")

    label("loc_834A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_849E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8416")

    ChrTalk(
        0xFE,
        (
            "Mom and Dad found out that I come\x01",
            "to the bakery all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're so strict! They forbade me from\x01",
            "eating out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't it fine, though? Their bread is so tasty!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8499")

    label("loc_8416")


    ChrTalk(
        0xFE,
        (
            "They told me that they were going to take away\x01",
            "my allowance if I kept disobeying them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mommy and Daddy are too strict...\x02",
    )

    CloseMessageWindow()

    label("loc_8499")

    Jump("loc_9325")

    label("loc_849E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8566")

    ChrTalk(
        0xFE,
        (
            "I had so much fun playing with my friend\x01",
            "during the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But...Chiruru said she was going to\x01",
            "set off on another journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Lame. She's hardly ever in town.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9325")

    label("loc_8566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85FF")

    ChrTalk(
        0xFE,
        "Chiruru and I made a promise...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She hasn't come back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's she doing? I told her to\x01",
            "meet me at the bakery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_862D")

    label("loc_85FF")


    ChrTalk(
        0xFE,
        "Geez, don't tell me she forgot about it.\x02",
    )

    CloseMessageWindow()

    label("loc_862D")

    Jump("loc_9325")

    label("loc_8632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_87AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8728")

    ChrTalk(
        0xFE,
        "(Oscar gave me another freebie today!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(He thanked me for my continued patronage.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(It caught me off guard, so my heart ended up\x01",
            "skipping a beat...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(It doesn't help that Oscar is handsome,\x01",
            "either.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_87A7")

    label("loc_8728")


    ChrTalk(
        0xFE,
        (
            "(Becoming a regular patron at an establishment\x01",
            "usually comes with its perks.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(I'll start coming daily from now on.)\x02",
    )

    CloseMessageWindow()

    label("loc_87A7")

    Jump("loc_9325")

    label("loc_87AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8897")

    ChrTalk(
        0xFE,
        (
            "I'm supposed to be checking out the Anniversary\x01",
            "Festival with a friend, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if that girl will actually return?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried for her, considering she doesn't\x01",
            "care about other people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8921")

    label("loc_8897")


    ChrTalk(
        0xFE,
        "Will Chiruru come back for the festival...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is she going to break our promise and end up\x01",
            "disappearing to another country again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8921")

    Jump("loc_9325")

    label("loc_8926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89E8")

    ChrTalk(
        0xFE,
        (
            "*sigh* Chiruru may have set off on\x01",
            "another long journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where did she disappear to this time? And here I was\x01",
            "hoping we could try the newest bread together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8A44")

    label("loc_89E8")


    ChrTalk(
        0xFE,
        (
            "Chiruru's an eccentric, so I wonder where\x01",
            "her crazy personality has led her this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A44")

    Jump("loc_9325")

    label("loc_8A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B5A")

    ChrTalk(
        0xFE,
        "Nice! They've put out this month's signature bread.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This bakery manages to pump out so many crazy\x01",
            "styles of bread. You find yourself subconsciously\x01",
            "returning to try all of them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Keep this a secret from my parents, will you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8C13")

    label("loc_8B5A")


    ChrTalk(
        0xFE,
        (
            "*sigh* I think I've been coming too much lately.\x01",
            "All of the staff members recognize me now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's not much I can do about it. Their bread\x01",
            "is too delicious to not come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C13")

    Jump("loc_9325")

    label("loc_8C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D68")

    ChrTalk(
        0xFE,
        "Oscar is ridiculously hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's got a refined look that makes him look cool,\x01",
            "yet he's always cheery and composed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "His good looks are wasted on baking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's he doing holed up in a bakery\x01",
            "rather than putting his face out there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(Oscar's as popular as ever with the ladies...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8DB2")

    label("loc_8D68")


    ChrTalk(
        0xFE,
        "Oscar is ridiculously hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "His good looks are wasted on baking.\x02",
    )

    CloseMessageWindow()

    label("loc_8DB2")

    Jump("loc_9325")

    label("loc_8DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA0")

    ChrTalk(
        0xFE,
        "An egg sandwich and a croissant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think I'll buy some donuts, too. They're the\x01",
            "perfect afternoon snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops, I might be going a little bit overboard.\x01",
            "I do want that snack, though...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8F24")

    label("loc_8EA0")


    ChrTalk(
        0xFE,
        (
            "Do I go for the freshly baked goods, or do I go\x01",
            "for their limited-time breads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Decisions, decisions... Which do I choose?\x02",
    )

    CloseMessageWindow()

    label("loc_8F24")

    Jump("loc_9325")

    label("loc_8F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_90B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FE8")

    ChrTalk(
        0xFE,
        "I've got an eccentric friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She spends all of her free time going on adventures.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I went to go play with her, but she had already\x01",
            "left for the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_90AC")

    label("loc_8FE8")


    ChrTalk(
        0xFE,
        (
            "*sigh* Chiruru's gone and left for another journey.\x01",
            "Looks like I won't be seeing her today, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing I can do about it, so I think I'll\x01",
            "buy some bread and head back home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90AC")

    Jump("loc_9325")

    label("loc_90B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_915B")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Let's see, this month's new bread is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Crispy and Spicy Bacon Bread?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Freshly baked, too... Gosh, that looks\x01",
            "phenomenal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9210")

    label("loc_915B")


    ChrTalk(
        0xFE,
        (
            "There's a new style of bread on sale every\x01",
            "month at this bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's beautiful, to me, to experience the taste\x01",
            "of bread and to smell its fragrance when it\x01",
            "is baker-made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9210")

    Jump("loc_9325")

    label("loc_9215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C8")

    ChrTalk(
        0xFE,
        "This bakery sure is something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I came to West Street to meet up with a friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ended up discovering a treasure while I\x01",
            "was at it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9325")

    label("loc_92C8")


    ChrTalk(
        0xFE,
        "The ambiance in the bakery is lovely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to buy a loaf to take home\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9325")

    TalkEnd(0xFE)
    Return()

    # Function_13_80CD end

    def Function_14_9329(): pass

    label("Function_14_9329")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_939D")

    ChrTalk(
        0xFE,
        "I'm headed back home today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta buy a ton of souvenirs for my friends\x01",
            "and family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9491")

    label("loc_939D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_93AB")
    Jump("loc_9491")

    label("loc_93AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_93EF")

    ChrTalk(
        0xFE,
        "Want to join me for a cup of coffee at the cafe?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9491")

    label("loc_93EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9491")

    ChrTalk(
        0xFE,
        (
            "I was wandering around during the festival and\x01",
            "managed to stumble upon this bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's delicious lookin' bread as far\x01",
            "as the eye can see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9491")

    TalkEnd(0xFE)
    Return()

    # Function_14_9329 end

    def Function_15_9495(): pass

    label("Function_15_9495")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_950B")

    ChrTalk(
        0xFE,
        "I managed to get a perfect view of the parade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Suppose I'll take a stroll around the city.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9681")

    label("loc_950B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9519")
    Jump("loc_9681")

    label("loc_9519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_95D1")

    ChrTalk(
        0xFE,
        (
            "I've refrained from eating the hotel's meal service\x01",
            "in favor of coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The festive atmosphere makes you want to eat\x01",
            "in the city alongside the activities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9681")

    label("loc_95D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_964E")

    ChrTalk(
        0xFE,
        "I'm tired of walking... Crossbell is too darn big.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My dad wandered off somewhere alone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_9681")

    label("loc_964E")


    ChrTalk(
        0xFE,
        "I think I'll take a small break at this cafe.\x02",
    )

    CloseMessageWindow()

    label("loc_9681")

    TalkEnd(0xFE)
    Return()

    # Function_15_9495 end

    def Function_16_9685(): pass

    label("Function_16_9685")

    Call(0, 17)
    Return()

    # Function_16_9685 end

    def Function_17_9689(): pass

    label("Function_17_9689")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96AE")
    Call(0, 33)
    Return()

    label("loc_96AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9709")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9728")
    OP_AF(0x2F)
    Jump("loc_978A")

    label("loc_9728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9738")
    OP_AF(0x2E)
    Jump("loc_978A")

    label("loc_9738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9748")
    OP_AF(0x2D)
    Jump("loc_978A")

    label("loc_9748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9758")
    OP_AF(0x2C)
    Jump("loc_978A")

    label("loc_9758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9768")
    OP_AF(0x2B)
    Jump("loc_978A")

    label("loc_9768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9778")
    OP_AF(0x2A)
    Jump("loc_978A")

    label("loc_9778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9788")
    OP_AF(0x29)
    Jump("loc_978A")

    label("loc_9788")

    OP_AF(0x28)

    label("loc_978A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A1")

    label("loc_9799")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97AD")
    Jump("loc_B8A1")

    label("loc_97AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_988A")

    ChrTalk(
        0xF,
        (
            "Oh, it looks like you managed to get those\x01",
            "Requium Flowers I requested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Sorry to take up your time doing this. I'll have to\x01",
            "apologize to Quint later, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_988A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9957")

    ChrTalk(
        0xF,
        (
            "Follow the Mainz Mountain Path fork that leads\x01",
            "to the ruins. You'll be able to find Requium\x01",
            "Flowers at the midway point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Please be careful. It could be dangerous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_9957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ADD")

    ChrTalk(
        0xF,
        (
            "My little Momo loves to read. She recently began\x01",
            "delving into this one novel series.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She only managed to get her hands on a few\x01",
            "of the volumes, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't bear to see her sad, so I ordered the missing\x01",
            "volumes for the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Wanna give them a go, too? You might end up liking it.\x01",
            "Fair warning, though. We only have a few volumes in\x01",
            "stock.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 6)
    Jump("loc_B8A1")

    label("loc_9ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9B33")

    ChrTalk(
        0xF,
        "Momo was on the verge of tears today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Did somebody upset her?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_9B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9BFD")

    ChrTalk(
        0xF,
        "Is it true that people have gone missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Don't tell me there's a kidnapper on the loose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That's horrifying. I'll need to warn Momo\x01",
            "to be more careful when she's outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_9BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D04")

    ChrTalk(
        0xF,
        (
            "Momo recently made a new friend.\x01",
            "They've been playing together lots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Hopefully, this'll force her out of her shell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm still optimistic, despite the constant\x01",
            "bombardment of bad news concerning\x01",
            "incidents around the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9D93")

    label("loc_9D04")


    ChrTalk(
        0xF,
        (
            "Despite the constant bombardment of bad news,\x01",
            "my child's smiling face always brightens my day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I wish we'd return to peaceful times.\x02",
    )

    CloseMessageWindow()

    label("loc_9D93")

    Jump("loc_B8A1")

    label("loc_9D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EF5")

    ChrTalk(
        0xF,
        "Hey there. Welcome to Tallys' General Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I've been listening in on the gossip lately, and\x01",
            "there's been nasty rumors about Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "They've been engaging in shady business and\x01",
            "causing trouble for the cityfolk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I've gotta be careful. I have a little girl that I\x01",
            "wouldn't want to fall victim to them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9FAE")

    label("loc_9EF5")


    ChrTalk(
        0xF,
        (
            "Revache's ties run deep. They've got their hands\x01",
            "in the pockets of my fellow traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I've gotta be careful. I have a little girl that I\x01",
            "wouldn't want to fall victim to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FAE")

    Jump("loc_B8A1")

    label("loc_9FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0AE")

    ChrTalk(
        0xF,
        (
            "Looks like everybody's gone back to their\x01",
            "daily routine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's best to relax and take it slow after you've\x01",
            "partied for five days straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Elsa's telling me that I'm always taking\x01",
            "it a little too slow, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A13E")

    label("loc_A0AE")


    ChrTalk(
        0xF,
        (
            "Feels like everything's gone back to normal,\x01",
            "now that the Anniversary Festival is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Yep, I'm definitely a fan of peace and quiet.\x02",
    )

    CloseMessageWindow()

    label("loc_A13E")

    Jump("loc_B8A1")

    label("loc_A143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A2BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A234")

    ChrTalk(
        0xF,
        (
            "Elsa and Momo have headed off to Mishelam\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I told them to go enjoy themselves.\x01",
            "They've earned a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "They're always helping me out with the store,\x01",
            "so a breather will do them some good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A2BA")

    label("loc_A234")


    ChrTalk(
        0xF,
        (
            "Elsa and Momo should have arrived at Mishelam\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "My workload is going to be tough, but I'll grit my\x01",
            "teeth and bear it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2BA")

    Jump("loc_B8A1")

    label("loc_A2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_A3F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A38A")

    ChrTalk(
        0xF,
        (
            "Oh, yeah. Today was the parade,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Argh, darn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wasn't really interested in the remainder\x01",
            "of the festival, so I didn't bother checking\x01",
            "the schedule.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A3EE")

    label("loc_A38A")


    ChrTalk(
        0xF,
        "The parade went through town today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I hope Elsa and Momo managed to enjoy\x01",
            "it in my stead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3EE")

    Jump("loc_B8A1")

    label("loc_A3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A60A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A584")

    ChrTalk(
        0x101,
        (
            "#0001F(Yeah, this person might know\x01",
            "something about Colin...)\x02",
        )
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
        0xF,
        "A child has gone missing? That's horrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I barely managed to catch the parade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I only watched it from afar, so I wouldn't be\x01",
            "able to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI see. Thank you anyway.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_A605")

    label("loc_A584")


    ChrTalk(
        0xF,
        (
            "I barely managed to catch the parade. I only\x01",
            "watched it from afar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Wouldn't be able to tell you if I saw a kid or not.\x02",
    )

    CloseMessageWindow()

    label("loc_A605")

    Jump("loc_B8A1")

    label("loc_A60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A73E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6D5")

    ChrTalk(
        0xF,
        (
            "Oh, yeah. Today was the parade,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Argh, darn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wasn't really interested in the remainder of the\x01",
            "festival, so I didn't bother checking the schedule.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A739")

    label("loc_A6D5")


    ChrTalk(
        0xF,
        "The parade went through town today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I hope Elsa and Momo managed to enjoy\x01",
            "it in my stead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A739")

    Jump("loc_B8A1")

    label("loc_A73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A86F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A828")

    ChrTalk(
        0xF,
        "Elsa and Momo went to go check out the festivities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I sent them off for a stroll around the city since\x01",
            "it's a rare occurrence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Even if I can't, I want my family to be able\x01",
            "to go and enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A86A")

    label("loc_A828")


    ChrTalk(
        0xF,
        (
            "I want my family to be able to go and enjoy the\x01",
            "festivities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A86A")

    Jump("loc_B8A1")

    label("loc_A86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A9CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A947")

    ChrTalk(
        0xF,
        (
            "I didn't make any special plans for the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "This year's festival is on a whole different scale...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Maybe I should have done something to\x01",
            "contribute as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A9C7")

    label("loc_A947")


    ChrTalk(
        0xF,
        (
            "A sale to commemorate the festival would have\x01",
            "been a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Now this is a good example of being\x01",
            "fashionably late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9C7")

    Jump("loc_B8A1")

    label("loc_A9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_AB6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AABF")

    ChrTalk(
        0xF,
        (
            "This year marks the 70th anniversary of Crossbell\x01",
            "State's founding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Crossbell was established as a state when my\x01",
            "grandpa was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "When you put it into perspective, it's kind of\x01",
            "crazy to think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AB66")

    label("loc_AABF")


    ChrTalk(
        0xF,
        (
            "You never really pay attention to it, but it's easy\x01",
            "to forget that we're our own state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "When you put it into perspective, it's kind of\x01",
            "crazy to think about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB66")

    Jump("loc_B8A1")

    label("loc_AB6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_ACA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC26")

    ChrTalk(
        0xF,
        (
            "I was talking to Brigitta about that so-called\x01",
            "'police pup' of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I saw him around here a little while ago, but I\x01",
            "think he went out for a stroll.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_ACA0")

    label("loc_AC26")


    ChrTalk(
        0xF,
        "That dog of yours went out for a stroll again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He appears to be patrolling our neighborhood...\x01",
            "What a good boy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACA0")

    Jump("loc_B8A1")

    label("loc_ACA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AF3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD3E")

    ChrTalk(
        0xF,
        (
            "That's one big dog we've got on our\x01",
            "hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "So this is the dog that's been the talk of the town\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AE0F")

    label("loc_AD3E")


    ChrTalk(
        0xF,
        (
            "I gotta say, while I feel like I can probably rely\x01",
            "on him, I'm, uh...just a teensy bit intimidated\x01",
            "by how large he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Last time I tried to call for him, he just stuck up\x01",
            "his nose and strutted away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0F")

    Jump("loc_AF38")

    label("loc_AE14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEBE")

    ChrTalk(
        0xF,
        (
            "From what I can tell, he comes by around\x01",
            "two to three times a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He was just here a moment ago, actually...\x01",
            "I guess he went off somewhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_AF38")

    label("loc_AEBE")


    ChrTalk(
        0xF,
        "That dog of yours went out for a stroll again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He appears to be patrolling our neighborhood...\x01",
            "What a good boy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF38")

    Jump("loc_B8A1")

    label("loc_AF3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B04D")

    ChrTalk(
        0xF,
        (
            "Elsa has been constantly chattering on\x01",
            "about Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She gets a sparkle in her eye when she mentions\x01",
            "them. I should take her to see them sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She's never mentioned it before, but I think\x01",
            "she used to dream about performing\x01",
            "with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_B04D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B0DA")

    ChrTalk(
        0xF,
        "Did you know that Harold has a kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He also runs a family business... I can feel\x01",
            "a connection between the two of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_B0DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B28B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1F6")

    ChrTalk(
        0xF,
        (
            "Harold stopped by to inform me that the price\x01",
            "of honey for the current shipment has been\x01",
            "determined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "His diligence and attention to customers makes\x01",
            "me feel valued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I think I'll take the opportunity to ask him about\x01",
            "the next shipment as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B286")

    label("loc_B1F6")


    ChrTalk(
        0xF,
        (
            "I've known Harold for about three years now. He's\x01",
            "a hardworking man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "On that note, I have to ask him about\x01",
            "the next shipment as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B286")

    Jump("loc_B8A1")

    label("loc_B28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B3D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B32A")

    ChrTalk(
        0xF,
        (
            "I haven't seen Ryu and Anri around these\x01",
            "parts lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Where have they been? It's rare to not see\x01",
            "them playing out front.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B3D3")

    label("loc_B32A")


    ChrTalk(
        0xF,
        (
            "I haven't seen Ryu and Anri around these\x01",
            "parts lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If I recall correctly, Ryu lives in the Bellheim\x01",
            "Apartments... I wonder if he's come down\x01",
            "with the flu?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3D3")

    Jump("loc_B8A1")

    label("loc_B3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B59A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B507")

    ChrTalk(
        0xF,
        (
            "I buy Armorican honey wholesale from a trader\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It turns me a decent profit, and he gives me\x01",
            "a ton of warning in advance if the price is\x01",
            "about to rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "He always makes sure to keep me informed.\x01",
            "You hardly see businessmen with his\x01",
            "level of integrity.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B595")

    label("loc_B507")


    ChrTalk(
        0xF,
        (
            "I'm grateful for all the insider information he\x01",
            "gives me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The price of honey is going to rise soon,\x01",
            "so I've stocked up a ton of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B595")

    Jump("loc_B8A1")

    label("loc_B59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_B667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B643")

    ChrTalk(
        0xF,
        "Momo's a shy little girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She can be really difficult at times. She'll hole\x01",
            "herself upstairs whenever a customer walks in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B662")

    label("loc_B643")


    ChrTalk(
        0xF,
        "Momo's a shy little girl.\x02",
    )

    CloseMessageWindow()

    label("loc_B662")

    Jump("loc_B71E")

    label("loc_B667")


    ChrTalk(
        0xF,
        (
            "We run a general store, so we mostly dabble in\x01",
            "foodstuffs and daily necessities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It'd make me happy if you browsed\x01",
            "our wares. You can never be too\x01",
            "careful when stocking up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B71E")

    Jump("loc_B8A1")

    label("loc_B723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B8A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B830")

    ChrTalk(
        0xF,
        "Welcome to my store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If you're looking to stock up on daily necessities,\x01",
            "then you've come to the right place! Tallys'\x01",
            "General Store is your number one stop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Our store's policy is to take it easy.\x01",
            "Take your time looking around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_B8A1")

    label("loc_B830")


    ChrTalk(
        0xF,
        "Our store's policy is to take it easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We have a very easygoing pace here,\x01",
            "so take your time shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8A1")

    Jump("loc_96B8")

    label("loc_B8A6")

    TalkEnd(0xF)
    Return()

    # Function_17_9689 end

    def Function_18_B8AA(): pass

    label("Function_18_B8AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B9B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B945")

    ChrTalk(
        0xFE,
        "Did Momo get into a fight with one of her friends...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been sulking for a while and refuses\x01",
            "to speak with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B9AD")

    label("loc_B945")


    ChrTalk(
        0xFE,
        "Ah, well. Kids will be kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll whip her up a delicious meal to try and\x01",
            "cheer her up later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9AD")

    Jump("loc_C78D")

    label("loc_B9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BAD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA4B")

    ChrTalk(
        0xFE,
        (
            "Ian seems swamped lately. He probably has too\x01",
            "many cases to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "His assistant Pete has got it rough as well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BAD0")

    label("loc_BA4B")


    ChrTalk(
        0xFE,
        (
            "My husband told me that the crime rate's\x01",
            "been increasing lately. Perhaps that's\x01",
            "the cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ian and Pete have got it rough.\x02",
    )

    CloseMessageWindow()

    label("loc_BAD0")

    Jump("loc_C78D")

    label("loc_BAD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BC2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBB8")

    ChrTalk(
        0xFE,
        (
            "I was taking a peek out the window earlier, and\x01",
            "Momo was playing with a friend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momma is so proud of her.\x01",
            "She's normally very shy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll cook some red rice tonight to celebrate.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BC29")

    label("loc_BBB8")


    ChrTalk(
        0xFE,
        (
            "You've finally done it, Momo. You've brought joy\x01",
            "to your mom and dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'll have to celebrate tonight.\x02",
    )

    CloseMessageWindow()

    label("loc_BC29")

    Jump("loc_C78D")

    label("loc_BC2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BCC1")

    ChrTalk(
        0xFE,
        "Some new goods arrived today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to handle them more carefully when\x01",
            "I put them up on display. They're a bit pricey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78D")

    label("loc_BCC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BCCF")
    Jump("loc_C78D")

    label("loc_BCCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BE9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDE0")

    ChrTalk(
        0xFE,
        (
            "Momo's a quick learner, so she's been very\x01",
            "helpful with running the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only problem is, all she does is help\x01",
            "out with the store or read books all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd do her some good to make some friends and\x01",
            "play outside more often.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BE95")

    label("loc_BDE0")


    ChrTalk(
        0xFE,
        (
            "I appreciate her helping us out, but I wonder\x01",
            "if she's actually okay with continuing\x01",
            "things the way they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm constantly wondering if she'd rather be\x01",
            "outside playing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE95")

    Jump("loc_C78D")

    label("loc_BE9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF9E")

    ChrTalk(
        0xFE,
        "The Anniversary Festival is on the horizon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doesn't look like my husband has any intention\x01",
            "of running a special promotion, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It's so like him to be the only person not\x01",
            "bothering to celebrate the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C014")

    label("loc_BF9E")


    ChrTalk(
        0xFE,
        (
            "Hmm... It's pretty quiet downstairs, don't\x01",
            "you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That husband of mine better not have dozed\x01",
            "off again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C014")

    Jump("loc_C78D")

    label("loc_C019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C12A")

    ChrTalk(
        0xFE,
        (
            "Arc en Ciel's new performance will feature\x01",
            "a rookie in one of the lead roles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly she's co-starring with Ilya for her\x01",
            "debut act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't imagine what kind of person you'd have\x01",
            "to be to pull off an incredible feat like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C1FB")

    label("loc_C12A")


    ChrTalk(
        0xFE,
        (
            "I'm sure every girl here has dreamed of\x01",
            "performing with Arc en Ciel at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Co-starring with Ilya for your debuting act is\x01",
            "unbelievable. It sounds like something\x01",
            "straight out of a fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1FB")

    Jump("loc_C78D")

    label("loc_C200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C2EB")

    ChrTalk(
        0xFE,
        "Momo's at Sunday School today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a shy girl, so I'm worried she'll have trouble\x01",
            "getting along with the other kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to ask the sister if she's getting\x01",
            "along with the other kids next time I go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78D")

    label("loc_C2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C444")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "You're always leaving me in your debt,\x01",
            "Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For next month's shipment, could you please do\x01",
            "this, this, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3603FTen percent more ingredients... So it's a discount\x01",
            "you wish for then, yes?\x02\x03",
            "#3600FHaha, not to worry. I'll gladly oblige.\x01",
            "After all, you and Tallys are some\x01",
            "of my precious regulars.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_C78D")

    label("loc_C444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C609")

    ChrTalk(
        0xFE,
        "I went to go check out a shop at Central Square...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, someone's occupied the old building by\x01",
            "Central Square. I must have completely missed\x01",
            "that ever happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how long it's been occupied. I didn't\x01",
            "notice anyone move in at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(Ya think she's talkin' about the Special Support\x01",
            "Section building?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F(Yeah... We've still got a long way to go before\x01",
            "we're a household name.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C6B4")

    label("loc_C609")


    ChrTalk(
        0xFE,
        (
            "Apparently, someone's occupied the old building by\x01",
            "Central Square. I must have completely missed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't seem to keep up with the rapid change\x01",
            "in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6B4")

    Jump("loc_C78D")

    label("loc_C6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_C776")

    ChrTalk(
        0xFE,
        "Cooking, cooking... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than throwing out our unsold produce, we\x01",
            "end up using them in our own dishes and eating\x01",
            "it. Wouldn't want to waste food, now would we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78D")

    label("loc_C776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_C784")
    Jump("loc_C78D")

    label("loc_C784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_C78D")

    label("loc_C78D")

    TalkEnd(0xFE)
    Return()

    # Function_18_B8AA end

    def Function_19_C791(): pass

    label("Function_19_C791")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C7C5")

    ChrTalk(
        0xFE,
        "Wahhh...Ryu's a big meanie...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D17D")

    label("loc_C7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_CB91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF6")

    ChrTalk(
        0xFE,
        (
            "I checked out the stalls with Ryu on the last day\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I had so much fun...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish we'd play together again...\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1110FA festival?\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    TurnDirection(0xFE, 0x153, 500)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "*sniffle* It's...nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I played around with a friend at the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I had so much fun...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105FAww, that sounds fun...\x02\x03",
            "#1109FWe should go to the festival with everyone next\x01",
            "time, Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000FY-Yeah. That sounds like something we'd\x01",
            "be able to do.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_CA68")

    ChrTalk(
        0x102,
        "#0100FWe'll have to wait until next year, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAEE")

    label("loc_CA68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CAB0")

    ChrTalk(
        0x103,
        "#0202FThere will not be one until next year, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAEE")

    label("loc_CAB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_CAEE")

    ChrTalk(
        0x104,
        "#0300FYou'll be waitin' a year for that, kiddo.\x02",
    )

    CloseMessageWindow()

    label("loc_CAEE")

    SetScenarioFlags(0xAD, 6)
    Jump("loc_CB8C")

    label("loc_CAF6")


    ChrTalk(
        0xFE,
        (
            "I checked out the stalls with Ryu on the last day\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I had so much fun...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish we'd play together again...\x02",
    )

    CloseMessageWindow()

    label("loc_CB8C")

    Jump("loc_D17D")

    label("loc_CB91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CBFC")

    ChrTalk(
        0xFE,
        "*sigh* I think I'll take a break...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's tiring talking to customers all the time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D17D")

    label("loc_CBFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CC0A")
    Jump("loc_D17D")

    label("loc_CC0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_CC7B")

    ChrTalk(
        0xFE,
        "That sure was one cute doggie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna play with the doggie again! Will he\x01",
            "play with me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17D")

    label("loc_CC7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CD9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CCF8")

    ChrTalk(
        0xFE,
        "That sure was one cute doggie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna play with the doggie again! Will he\x01",
            "play with me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD99")

    label("loc_CCF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD63")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "*pet* *pet*...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "The doggie looks like he's enjoying it.\x01",
            "Good boy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_CD99")

    label("loc_CD63")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "*pet* *pet*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're a cute doggie.\x02",
    )

    CloseMessageWindow()

    label("loc_CD99")

    Jump("loc_D17D")

    label("loc_CD9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_CE32")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "*rustle*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "We put our new items up on display.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to clean them first, so that you\x01",
            "can see the labels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17D")

    label("loc_CE32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CF52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEEB")

    ChrTalk(
        0xFE,
        "Ryu told me that he was saved by a big doggie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That sounds like fun... I wanna play, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No, don't play around on the road.\x01",
            "It's dangerous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_CF4D")

    label("loc_CEEB")


    ChrTalk(
        0xFE,
        (
            "You might get hit by one of the orbal\x01",
            "cars passing by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why won't you listen to me, Ryu?\x02",
    )

    CloseMessageWindow()

    label("loc_CF4D")

    Jump("loc_D17D")

    label("loc_CF52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D10E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_D00B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFD4")

    ChrTalk(
        0xFE,
        "I don't get along well with Pete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He got mad at me for not speaking\x01",
            "clearly enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D006")

    label("loc_CFD4")


    ChrTalk(
        0xFE,
        "Pete's a nice guy, but we don't get along...\x02",
    )

    CloseMessageWindow()

    label("loc_D006")

    Jump("loc_D109")

    label("loc_D00B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0BC")

    ChrTalk(
        0xFE,
        "Let's play together, Ryu and Anri!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2SL-Let's play together...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm trying to practice my lines. I don't want to be\x01",
            "nervous when I ask for real.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D109")

    label("loc_D0BC")


    ChrTalk(
        0xFE,
        "L-Let's play together...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, how I wish I could properly say it...\x02",
    )

    CloseMessageWindow()

    label("loc_D109")

    Jump("loc_D17D")

    label("loc_D10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D17D")

    ChrTalk(
        0xFE,
        (
            "Ryu and Anri look like they're always having\x01",
            "fun together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish I could join them, too...\x02",
    )

    CloseMessageWindow()

    label("loc_D17D")

    TalkEnd(0xFE)
    Return()

    # Function_19_C791 end

    def Function_20_D181(): pass

    label("Function_20_D181")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D192")
    Jump("loc_D3C0")

    label("loc_D192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D29D")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood's been up to his neck\x01",
            "in work, so he hasn't had any time\x01",
            "to help me with my law studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel determined to study harder whenever\x01",
            "I watch Mr. Grimwood at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to be able to aid him as\x01",
            "soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_D2FB")

    label("loc_D29D")


    ChrTalk(
        0xFE,
        (
            "I've gotta become a fully-licensed lawyer as\x01",
            "soon as possible and help out Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2FB")

    Jump("loc_D3C0")

    label("loc_D300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D30E")
    Jump("loc_D3C0")

    label("loc_D30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D3C0")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood has terrible eating habits.\x01",
            "He manages to get past lunch on just\x01",
            "a single cup of coffee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I actually offered to start preparing his\x01",
            "meals for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3C0")

    TalkEnd(0xFE)
    Return()

    # Function_20_D181 end

    def Function_21_D3C4(): pass

    label("Function_21_D3C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D3D5")
    Jump("loc_D73F")

    label("loc_D3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D4E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D474")

    ChrTalk(
        0xFE,
        (
            "My husband has been working restlessly\x01",
            "in the office since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. He's been fixated on that building\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D4DF")

    label("loc_D474")


    ChrTalk(
        0xFE,
        (
            "My husband has been working restlessly\x01",
            "since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I've gotta head back home soon.\x02",
    )

    CloseMessageWindow()

    label("loc_D4DF")

    Jump("loc_D73F")

    label("loc_D4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58C")

    ChrTalk(
        0xFE,
        (
            "That dog that everybody's been talking about\x01",
            "came to Tallys' store recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sad I missed out on it.\x01",
            "I wanted to see him, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D620")

    label("loc_D58C")


    ChrTalk(
        0xFE,
        (
            "He shows up kinda frequently, according\x01",
            "to Tallys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll try to drop by earlier tomorrow.\x01",
            "I might be able to catch a glimpse of him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D620")

    Jump("loc_D73F")

    label("loc_D625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D73F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6B3")

    ChrTalk(
        0xFE,
        (
            "I tried greeting Momo when I came in, but she\x01",
            "looked uncomfortable and ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What a shy girl she is.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D73F")

    label("loc_D6B3")


    ChrTalk(
        0xFE,
        (
            "I feel for her, though. I was the same way\x01",
            "when I was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I keep greeting Momo by accident,\x01",
            "even though I know what'll happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D73F")

    TalkEnd(0xFE)
    Return()

    # Function_21_D3C4 end

    def Function_22_D743(): pass

    label("Function_22_D743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7CB")

    ChrTalk(
        0xFE,
        "#1200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FZeit? So this is where you've\x01",
            "been all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FAs popular as ever, eh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D7DF")

    label("loc_D7CB")


    ChrTalk(
        0xFE,
        "#1200FGrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_D7DF")

    TalkEnd(0xFE)
    Return()

    # Function_22_D743 end

    def Function_23_D7E3(): pass

    label("Function_23_D7E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_END)), "loc_D911")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D857")

    ChrTalk(
        0x15,
        (
            "#3600FKeep working hard, everyone. I'll continue\x01",
            "to cheer you on from the sidelines.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90C")

    label("loc_D857")


    ChrTalk(
        0x15,
        (
            "#3600FKeep working hard, everyone. I'll continue\x01",
            "to cheer you on from the sidelines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(I feel encouraged to know that\x01",
            "people support us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Absolutely.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_D90C")

    Jump("loc_DBBB")

    label("loc_D911")

    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        "#3600FHello, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHi, Mr. Hayworth.\x02\x03",
            "Are you in the middle of negotiations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3600FWas it that obvious? I'm honestly in\x01",
            "Tallys' debt. He never fails to cooperate\x01",
            "in any of my business endeavors.\x02\x03",
            "I'm here to wholesale some of the\x01",
            "items in my inventory this time.\x02\x03",
            "Hey, that reminds me. Are you guys still on\x01",
            "the hunt for those monsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe are. We were regrettably unable\x01",
            "to uncover their location yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWe were actually just about to scoot\x01",
            "on over to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3600FSounds like you've got your work cut out for you.\x02\x03",
            "Good luck, everyone. I will gladly lend you my\x01",
            "aid, if you were to ever wish for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 4)

    label("loc_DBBB")

    TalkEnd(0xFE)
    Return()

    # Function_23_D7E3 end

    def Function_24_DBBF(): pass

    label("Function_24_DBBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_DDA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCAA")

    ChrTalk(
        0xFE,
        "Oh, hello there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FFancy meeting you here, Aeolia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, I recently discovered this place\x01",
            "and got hooked instantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pretty much eat their bread for lunch\x01",
            "every day, at this point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DDA5")

    label("loc_DCAA")


    ChrTalk(
        0xFE,
        (
            "That reminds me. I think Lynn's old\x01",
            "supervisor came by the guild\x01",
            "earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think they're playing a nice, long game\x01",
            "of catch-up over lunch over at Long\x01",
            "Lao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I could see the sparks flying, so\x01",
            "I didn't want to interrupt them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA5")

    TalkEnd(0xFE)
    Return()

    # Function_24_DBBF end

    def Function_25_DDA9(): pass

    label("Function_25_DDA9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE48")
    OP_29(0x46, 0x1, 0xB)

    ChrTalk(
        0x101,
        (
            "#0001F(That should cover West Street...)\x02\x03",
            "#0003F(I wonder if the others are having\x01",
            "better luck than me?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3308F(...)\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_DE48")

    Return()

    # Function_25_DDA9 end

    def Function_26_DE49(): pass

    label("Function_26_DE49")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_68(52500, 1500, 0, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27000, 0)
    BeginChrThread(0x101, 3, 0, 27)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(26000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0000F#1PHey, Oscar!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 28)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Well, if it isn't my man, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, you finally decided to stop by\x01",
            "and visit your old buddy, Oscar, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's been way too long, dude. What's it\x01",
            "been, a year since we last hung out?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006FSeriously? It's been THREE years, Oscar.\x02\x03",
            "You're as blissfully unaware as ever.\x01",
            "Some things never change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha! I blame the fact that we kept sending\x01",
            "each other letters. It never really felt like you\x01",
            "were gone for that long, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, let's see. You got a lil' taller, but I see you\x01",
            "still haven't outgrown that baby face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FUgh... Shut up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha. He got you there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYou must be an old friend of Lloyd's, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yep, the oldest! Name's Oscar. I work as\x01",
            "an apprentice here at Morges Bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And you three must be this dummy's\x01",
            "coworkers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYup. The name's Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FNice to meet you. I'm Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FTio Plato.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Nice to meet'cha, guys!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0003F(He could tell we worked together even\x01",
            "though we aren't wearing uniforms?)\x02\x03",
            "(Sometimes I can't tell whether he's\x01",
            "completely oblivious or a lot sharper\x01",
            "than he lets on.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What's up? You look like you're thinkin'\x01",
            "pretty hard, buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, yeah! You still cook, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWhat? I mean, a little.\x02\x03",
            "#0000FI had to help my uncle with chores, so\x01",
            "that meant cooking every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sweet! Then take this. Reunion gift\x01",
            "from yours truly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hope you'll get some use out of it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E763")

    ChrTalk(
        0x8,
        (
            "How about I teach you how to make\x01",
            "a killer sandwich while you're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Trust me, it's cake. It's the perfect recipe\x01",
            "to get you in the swing of things.\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xD)

    ChrTalk(
        0x101,
        (
            "#0005FTh-Thanks, Oscar.\x02\x03",
            "#0000FThis actually looks pretty neat. It even\x01",
            "has spots to write down variations of\x01",
            "different recipes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And since all of you have access to it, how\x01",
            "it's used can vary from person to person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I think you'll get a kick out of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E87C")

    label("loc_E763")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0005FTh-Thanks, Oscar.\x02\x03",
            "#0000FThis actually looks pretty neat. It even\x01",
            "has spots to write down variations of\x01",
            "different recipes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And since all of you have access to it, how\x01",
            "it's used can vary from person to person.\x01",
            "I think you'll get a kick out of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87C")


    ChrTalk(
        0x102,
        (
            "#0105FIt'll certainly keep us well fed.\x02\x03",
            "#0104FIt's a little embarrassing, but all of my\x01",
            "cooking know-how comes from baking\x01",
            "cookies.\x02\x03",
            "#0100FWhat about you two?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FErrr... Well, I can only really roast and\x01",
            "boil stuff. You know, food you'd have\x01",
            "campin' out in the wilderness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIf a recipe has a clear and concise\x01",
            "protocol I can follow, I can manage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIf you're interested, I'd be happy to\x01",
            "teach you a thing or two.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you talk to people or examine certain things,\x01",
            "you can sometimes learn cooking recipes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Recipes are recorded in the Recipe Notebook.\x01",
            "If you use the Recipe Notebook, you can prepare\x01",
            "dishes with various effects at any time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When cooking recipes, there is a set chance to\x01",
            "get a 'supreme' or 'peculiar' variant of each dish.\x01",
            "(Cooking can sometimes result in a 'failure,' too.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Most ingredients used in cooking are sold\x01",
            "at the general stores and various shops.\x01",
            "Monsters may drop them, as well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrPos(0x0, 53750, 0, 2000, 90)
    OP_4C(0x8, 0xFF)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x46, 1)
    EventEnd(0x5)
    Return()

    # Function_26_DE49 end

    def Function_27_EC87(): pass

    label("Function_27_EC87")

    SetChrPos(0x101, 47500, 0, 0, 90)
    SetChrPos(0x102, 46350, 0, -500, 90)
    SetChrPos(0x103, 46450, 0, 750, 90)
    SetChrPos(0x104, 45250, 0, 250, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_ECFC():
        OP_98(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECFC)
    Sleep(50)

    def lambda_ED19():
        OP_98(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED19)
    Sleep(50)

    def lambda_ED36():
        OP_98(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED36)
    Sleep(50)

    def lambda_ED53():
        OP_98(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED53)
    Sleep(500)

    def lambda_ED70():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ED70)
    Sleep(50)

    def lambda_ED84():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_ED84)
    Sleep(50)

    def lambda_ED98():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ED98)
    Sleep(50)

    def lambda_EDAC():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EDAC)
    WaitChrThread(0x101, 1)
    Return()

    # Function_27_EC87 end

    def Function_28_EDBD(): pass

    label("Function_28_EDBD")

    OP_68(54000, 1500, 2000, 3000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_EDDA():
        OP_95(0x101, 53750, 0, 2000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDDA)
    Sleep(210)

    def lambda_EDF7():
        OP_95(0x103, 52800, 0, 2750, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EDF7)
    Sleep(280)

    def lambda_EE14():
        OP_95(0x102, 52700, 0, 1500, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE14)
    Sleep(140)

    def lambda_EE31():
        OP_95(0x104, 51500, 0, 2250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE31)
    Sleep(300)
    TurnDirection(0x8, 0x101, 500)
    WaitChrThread(0x101, 1)

    def lambda_EE59():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE59)
    WaitChrThread(0x103, 1)

    def lambda_EE6A():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EE6A)
    WaitChrThread(0x102, 1)

    def lambda_EE7B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE7B)
    WaitChrThread(0x104, 1)

    def lambda_EE8C():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE8C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Return()

    # Function_28_EDBD end

    def Function_29_EEA7(): pass

    label("Function_29_EEA7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53470, 1500, 1600, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20740, 0)
    SetChrPos(0x101, 53650, 0, 1940, 90)
    SetChrPos(0x102, 52230, 0, 1940, 90)
    SetChrPos(0x103, 53650, 0, 520, 90)
    SetChrPos(0x104, 52230, 0, 520, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PYo, Lloyd. How's it hanging?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHaha, you in the mood for some bread?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006FDon't just 'You in the mood for some bread?' me.\x01",
            "You already know why we're here.\x02\x03",
            "#0000FYou submitted a support request, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHuh? Did I?\x02",
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
        0x103,
        (
            "#6P#0200FPlease notify any other Oscars on the\x01",
            "premises of our arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FCome on, Oscar. We aren't here\x01",
            "to mess around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POhhh, yeah. I remember now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI wanted to see if you guys could help me\x01",
            "gather some ingredients for a new kind of\x01",
            "bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POur usual supplier's been running late,\x01",
            "so we're kinda low on stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FAh, got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FWell, you can't bake without any\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTruer words have never been spoken.\x01",
            "So, will you guys gimme a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI think we can handle that.\x02\x03",
            "So, what kind of ingredients are you\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWell, I've got plenty of butter and flour...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P..but if you could find me four Fish Fillets\x01",
            "and three Monster Eggs, that'd be great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0304FThat's it? We can totally find those\x01",
            "on the outskirts of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FThat's convenient. We'll try gathering them\x01",
            "as we deal with our other support requests.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Hunting for Ingredients]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 53210, 0, 1200, 90)
    SetChrPos(0x1, 53210, 0, 1200, 90)
    SetChrPos(0x2, 53210, 0, 1200, 90)
    SetChrPos(0x3, 53210, 0, 1200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0x6, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_EEA7 end

    def Function_30_F50E(): pass

    label("Function_30_F50E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53470, 1500, 1600, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20740, 0)
    SetChrPos(0x101, 53650, 0, 1940, 90)
    SetChrPos(0x102, 52230, 0, 1940, 90)
    SetChrPos(0x103, 53650, 0, 520, 90)
    SetChrPos(0x104, 52230, 0, 520, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FDid someone order Fish Fillets and\x01",
            "Monster Eggs?\x02",
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
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4\x01",
            "and ",
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x12D, 4)
    SubItemNumber(0x12F, 3)

    ChrTalk(
        0x8,
        (
            "#11PThanks, guys, you're the best. And as\x01",
            "for you, Lloyd, you really are quite the\x01",
            "dependable guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI've always been able to count on you\x01",
            "to have my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FYou're tellin' me Lloyd's always been\x01",
            "like this? Figures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI assumed he was, judging by his\x01",
            "overly soft-hearted nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0109FLet's cut him some slack. We ARE\x01",
            "talking about Lloyd Bannings here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0003FI don't know what I did to deserve\x01",
            "these backhanded compliments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PC'mon, loosen up! They're saying you're\x01",
            "a good guy, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, hey. You should try out some of the\x01",
            "bread I baked today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'll hook you up, if you want.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FWe appreciate it. I'm sure we'll be\x01",
            "picking a few out from time to time.\x02\x03",
            "We're going to head out now.\x01",
            "Good luck with your apprenticeship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDon't need it. It'll be a piece of cake!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Hunting for Ingredients]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 53210, 0, 1200, 90)
    SetChrPos(0x1, 53210, 0, 1200, 90)
    SetChrPos(0x2, 53210, 0, 1200, 90)
    SetChrPos(0x3, 53210, 0, 1200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0x6, 0x4, 0x10)
    OP_29(0x6, 0x1, 0x1)
    SetScenarioFlags(0x1, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_F50E end

    def Function_31_FA9D(): pass

    label("Function_31_FA9D")

    EventBegin(0x0)
    Fade(800)
    OP_68(55260, 2500, 12530, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    SetChrPos(0x101, 55190, 1000, 12700, 0)
    SetChrPos(0x102, 55190, 1000, 11280, 0)
    SetChrPos(0x103, 55940, 1000, 12200, 0)
    SetChrPos(0x104, 55940, 1000, 10780, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5POh, it's you. You're gathering a bunch\x01",
            "of ingredients for Oscar, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PThat's SO unfair...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0005F#11PUh, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI'm trying to create a new kind of bread\x01",
            "for the bakery, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWhy is Oscar the only one who gets any\x01",
            "help around here...? *grumble* *grumble*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200F(Is she okay? She sounds upset about\x01",
            "something.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#11P(On top of that, it sounds like she's big\x01",
            "rivals with our buddy Oscar over there.)\x02\x03",
            "(She upset that we agreed to his request\x01",
            "or somethin'?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F#11P(If so, isn't that sort of petty?)\x02\x03",
            "#0005F(Hold on, is this about...?)\x02\x03",
            "#0000FUmm, we heard about the delayed\x01",
            "delivery... Did you need some help\x01",
            "with that?\x02\x03",
            "We'd be more than happy to bring\x01",
            "you some ingredients, too, if you'd\x01",
            "like.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xA,
        "#5PR-Really? Th-Then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...two Monster Eggs, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PTry to hurry, okay? I really want\x01",
            "to finish this bread before Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#11PWe'll try our best.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#0305F(Ah, Lloyd's bleedin' heart once again\x01",
            "makes an appearance.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111F#12P(You know, I think I'm used to it by now.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0005F#5PSomething up, guys?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#11P#0211FNothing. Nothing at all.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x0, 55190, 1000, 12700, 0)
    OP_4C(0xA, 0xFF)
    OP_29(0x6, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_31_FA9D end

    def Function_32_10095(): pass

    label("Function_32_10095")

    EventBegin(0x0)
    Fade(800)
    OP_68(55260, 2500, 12530, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    SetChrPos(0x101, 55190, 1000, 12700, 0)
    SetChrPos(0x102, 55190, 1000, 11280, 0)
    SetChrPos(0x103, 55940, 1000, 12200, 0)
    SetChrPos(0x104, 55940, 1000, 10780, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0000FExcuse me. Here are the ingredients\x01",
            "you requested.\x02",
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
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x12F, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1022D")

    ChrTalk(
        0xA,
        "#5POh, thank you. Thank you so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHeh heh. Now I can finally take down\x01",
            "Oscar once and for all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10310")

    label("loc_1022D")


    ChrTalk(
        0xA,
        "#5PAnd it's all thanks to you four.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut it's kind of too late now. I even\x01",
            "told you to be quick about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PDarn it! I was going to catch him\x01",
            "by surprise and get that dumb\x01",
            "mouth of his fall to the floor!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 2)

    label("loc_10310")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10322")
    OP_2C(0x6, 0x3)

    label("loc_10322")

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
        (
            "#11P#0003F(I decided to lend her a hand because it\x01",
            "looked like she was having a hard time...)\x02\x03",
            "(...but did we really do the right thing?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0304F(Eh, it'll be fine.)\x02\x03",
            "#0300F(Competition will just make 'em\x01",
            "better bakers in the long run.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x0, 55190, 1000, 12700, 0)
    SetChrPos(0x1, 55190, 1000, 12700, 0)
    SetChrPos(0x2, 55190, 1000, 12700, 0)
    SetChrPos(0x3, 55190, 1000, 12700, 0)
    OP_4C(0xA, 0xFF)
    OP_29(0x6, 0x1, 0x3)
    SetScenarioFlags(0x1, 6)
    EventEnd(0x5)
    Return()

    # Function_32_10095 end

    def Function_33_104E0(): pass

    label("Function_33_104E0")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1260, 1800, 5200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27520, 0)
    SetChrPos(0x101, -600, 0, 5400, 0)
    SetChrPos(0x102, 600, 0, 5400, 0)
    SetChrPos(0x103, -600, 0, 4200, 0)
    SetChrPos(0x104, 600, 0, 4200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10584")
    SetChrPos(0x10A, 0, 0, 3000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_10584")

    OP_4B(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0xF,
        "#5PWelcome to Tallys' General Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PLooking for anything in particular?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#12PYes, actually. We're looking for some\x01",
            "Requium Flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PAh, I see. Did Mr. Quint send you?\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C1")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_106C1")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0005FThat's right. Did he tell you that\x01",
            "we'd be coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PNo need to. He's about the only person\x01",
            "who buys those flowers from us. He\x01",
            "and a few other devoted individuals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWait a minute, please. I'm sure we have\x01",
            "some behind the counter somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)

    def lambda_107DE():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_107DE)
    WaitChrThread(0xF, 1)

    def lambda_107FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_107FC)

    ChrTalk(
        0x104,
        (
            "#0306FWhew. I thought we were gonna have\x01",
            "to pay for 'em for a second there.\x02\x03",
            "I mean, the old man didn't exactly give\x01",
            "us any mira.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10890():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10890)
    Sleep(50)

    def lambda_108A0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_108A0)
    Sleep(50)

    def lambda_108B0():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_108B0)

    ChrTalk(
        0x101,
        (
            "#6P#0000FI don't know. He didn't strike me as the\x01",
            "kind of person to pull something over\x01",
            "on us like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FPerhaps, but it still would have been\x01",
            "nice to have received a little more\x01",
            "information about the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI suppose that's true. He only told us\x01",
            "the locations of the flowers. Nothing\x01",
            "more, nothing less.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#5PU-Umm, pardon me...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AC5")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_10AC5")

    Sleep(1000)

    def lambda_10ACD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10ACD)
    Sleep(50)

    def lambda_10ADD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10ADD)
    Sleep(50)

    def lambda_10AED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10AED)
    Sleep(50)

    def lambda_10AFD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10AFD)
    Sleep(50)

    ChrTalk(
        0x101,
        "#12P#0005FIs something wrong?\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#5PI'm so sorry, but it looks like we're\x01",
            "out of stock of requiums.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FS-Seriously? That's just great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAgain, I'm terribly sorry. Would\x01",
            "you mind waiting for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI'll ask the Bracer Guild if they could\x01",
            "pick some up for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10C9D")
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_10C9D")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#0005FThe bracers? I suppose they would be\x01",
            "the ones to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EDC")

    ChrTalk(
        0x10A,
        (
            "#12P#0603FI hope I don't have to remind you that\x01",
            "we don't have time to wait for them.\x02\x03",
            "#0600FIf you don't have the means to fix this ASAP,\x01",
            "I propose we return to more pressing matters.\x01",
            "You know, the Revache investigation?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10DDD():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10DDD)
    Sleep(50)

    def lambda_10DED():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10DED)
    Sleep(50)

    def lambda_10DFD():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10DFD)
    Sleep(50)

    def lambda_10E0D():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10E0D)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#6P#0012FO-Of course.\x02\x03",
            "#0003F(Sorry, Mr. Quint...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10E55():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10E55)

    ChrTalk(
        0x102,
        (
            "#0101FLloyd, why don't we go pick the\x01",
            "flowers ourselves?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10A,
        "#12P#0605FYou propose we do WHAT?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F27")

    label("loc_10EDC")


    def lambda_10EE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10EE1)

    ChrTalk(
        0x102,
        (
            "#0101FLloyd, why don't we go pick the\x01",
            "flowers ourselves?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F27")


    def lambda_10F2C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10F2C)
    Sleep(50)

    def lambda_10F3C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F3C)
    Sleep(50)

    ChrTalk(
        0x104,
        (
            "#0300FHell yeah! Why lose to the bracers\x01",
            "when we can do somethin' about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FI second that.\x02",
    )

    CloseMessageWindow()

    def lambda_10FBA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FBA)

    ChrTalk(
        0x101,
        (
            "#6P#0000FSounds like we're all on the same page.\x02\x03",
            "Going ourselves would be much more\x01",
            "efficient than waiting on them, anyway.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11049():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11049)
    Sleep(50)

    def lambda_11059():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11059)
    Sleep(50)

    def lambda_11069():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11069)
    Sleep(50)

    def lambda_11079():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11079)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me. Do you happen to know\x01",
            "where Requium Flowers grow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAh, I see! You're planning to get them\x01",
            "yourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWell, you should find some blooming\x01",
            "on the edge of Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAbout halfway down the branching road\x01",
            "that leads to those old ruins, if I recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FThanks. We'll go ahead and try looking\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWonderful. And once more, I apologize\x01",
            "for the inconvenience. Please make sure\x01",
            "to give Mr. Quint my regards.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112E5")

    ChrTalk(
        0x10A,
        (
            "#12P#0606F(It seems my efforts at rushing them\x01",
            "have backfired horribly. I don't know\x01",
            "what I expected.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112E5")

    OP_29(0x2E, 0x1, 0x3)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 5400, 0)
    SetChrPos(0xF, 200, 0, 8500, 180)
    EventEnd(0x5)
    Return()

    # Function_33_104E0 end

    SaveToFile()

Try(main)
