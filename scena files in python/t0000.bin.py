from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0000.bin",                # FileName
        "t0000",                    # MapName
        "t0000",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0000",                  # 0
        "Elkin",                  # 1
        "Camille",                # 2
        "Pully",                  # 3
        "Salem",                  # 4
        "Derek",                  # 5
        "Ange",                   # 6
        "Millia",                 # 7
        "Stefan",                 # 8
        "Peter",                  # 9
        "Master Fisherman Lloyd", # 10
        "Kopan",                  # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist Murash",         # 14
        "Tourist Erte",           # 15
        "車",                     # 16
        "Harold",                 # 17
        "Bus",                    # 18
        "SE制御",                 # 19
        "Old Armorica Road",      # 20
    ))

    AddCharChip((
        "chr/ch24400.itc",                   # 00
        "chr/ch24600.itc",                   # 01
        "chr/ch24700.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch24300.itc",                   # 05
        "chr/ch23700.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch34300.itc",                   # 08
        "chr/ch32200.itc",                   # 09
        "chr/ch21200.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "apl/ch50165.itc",                   # 0C
        "apl/ch50169.itc",                   # 0D
        "apl/ch50166.itc",                   # 0E
        "chr/ch23600.itc",                   # 0F
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

    DeclNpc(8409,    0,       -12479,  17,   261,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-560,    0,       18309,   135,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(250,     0,       26870,   135,  261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13050,   0,       9680,    270,  261,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12779,   3500,    40220,   298,  389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-9899,   0,       25219,   86,   389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(16590,   3500,    42799,   135,  389,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-9899,   0,       25219,   86,   389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-759,    289,     3460,    90,   405,  0x0, 0,   12,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-740,    439,     5239,    90,   405,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-500,    500,     6000,    90,   405,  0x0, 0,   14,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(6030,    0,       15279,   178,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(7050,    0,       15500,   178,  389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5989,   0,       -7019,   265,  385,  0x0, 0,   9,   0,   0,   3,   0,   26,  255,  0)
    DeclNpc(-7639,   0,       13699,   180,  385,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-2000,   0,       -15000,  1500,    -2000,   1500,    -15000,  0x007C, 0,  30, 0x0000)
    DeclActor(11740,   0,       3950,    1200,    10890,   -1450,   1210,    0x007C, 0,  29, 0x0000)
    DeclActor(15160,   0,       -19080,  1200,    15160,   2000,    -19080,  0x007C, 0,  11, 0x0000)
    DeclActor(-16320,  3500,    61370,   5000,    -16320,  3500,    61370,   0x007C, 0,  41, 0x0000)

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "Old Armorica Road")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")
    PlaceName(16.399999618530273, 0.0, -17.799999237060547, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_4C4",          # 00, 0
        "Function_1_57C",          # 01, 1
        "Function_2_5A7",          # 02, 2
        "Function_3_5D2",          # 03, 3
        "Function_4_5FD",          # 04, 4
        "Function_5_943",          # 05, 5
        "Function_6_B2B",          # 06, 6
        "Function_7_C1B",          # 07, 7
        "Function_8_D5C",          # 08, 8
        "Function_9_DF1",          # 09, 9
        "Function_10_13CA",        # 0A, 10
        "Function_11_14B9",        # 0B, 11
        "Function_12_14C7",        # 0C, 12
        "Function_13_2C4B",        # 0D, 13
        "Function_14_386A",        # 0E, 14
        "Function_15_3E0C",        # 0F, 15
        "Function_16_47EF",        # 10, 16
        "Function_17_56D8",        # 11, 17
        "Function_18_64CA",        # 12, 18
        "Function_19_6CD7",        # 13, 19
        "Function_20_703B",        # 14, 20
        "Function_21_7310",        # 15, 21
        "Function_22_73D2",        # 16, 22
        "Function_23_747C",        # 17, 23
        "Function_24_7BB0",        # 18, 24
        "Function_25_7D3F",        # 19, 25
        "Function_26_7E82",        # 1A, 26
        "Function_27_803D",        # 1B, 27
        "Function_28_81CE",        # 1C, 28
        "Function_29_9044",        # 1D, 29
        "Function_30_912F",        # 1E, 30
        "Function_31_91E3",        # 1F, 31
        "Function_32_9CC0",        # 20, 32
        "Function_33_A42F",        # 21, 33
        "Function_34_A492",        # 22, 34
        "Function_35_A4F5",        # 23, 35
        "Function_36_A558",        # 24, 36
        "Function_37_A5AA",        # 25, 37
        "Function_38_AA86",        # 26, 38
        "Function_39_C0D7",        # 27, 39
        "Function_40_C0F3",        # 28, 40
        "Function_41_C136",        # 29, 41
        "Function_42_CFA6",        # 2A, 42
        "Function_43_D6BC",        # 2B, 43
    ))


    def Function_0_4C4(): pass

    label("Function_0_4C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_504"),
        (1, "loc_510"),
        (2, "loc_51C"),
        (3, "loc_528"),
        (4, "loc_534"),
        (5, "loc_540"),
        (6, "loc_54C"),
        (SWITCH_DEFAULT, "loc_558"),
    )


    label("loc_504")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_510")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_51C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_528")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_534")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_540")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_558")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_564")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_57B")

    Return()

    # Function_0_4C4 end

    def Function_1_57C(): pass

    label("Function_1_57C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A6")
    OP_94(0xFE, 0xFFFFECDC, 0x49FC, 0x7D0, 0x588E, 0x3E8)
    Sleep(250)
    Jump("Function_1_57C")

    label("loc_5A6")

    Return()

    # Function_1_57C end

    def Function_2_5A7(): pass

    label("Function_2_5A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D1")
    OP_94(0xFE, 0xFFFFECDC, 0x5BEA, 0xC62, 0x7242, 0x3E8)
    Sleep(300)
    Jump("Function_2_5A7")

    label("loc_5D1")

    Return()

    # Function_2_5A7 end

    def Function_3_5D2(): pass

    label("Function_3_5D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FC")
    OP_94(0xFE, 0xFFFFDF58, 0xFFFFDA3A, 0xFFFFF3BC, 0xFFFFEDF4, 0x7D0)
    Sleep(300)
    Jump("Function_3_5D2")

    label("loc_5FC")

    Return()

    # Function_3_5D2 end

    def Function_4_5FD(): pass

    label("Function_4_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7830, 0, 23860, 107)
    SetChrPos(0x9, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_69D")
    SetChrPos(0x9, -7700, 0, 24530, 0)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6ED")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7830, 0, 23860, 107)
    SetChrPos(0x9, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_727")
    SetChrPos(0x9, -8980, 0, 25880, 225)
    SetChrPos(0xA, -8960, 0, 24860, 315)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_8B9")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_746")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_8B9")

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78A")
    SetChrPos(0x9, -8980, 0, 25880, 225)
    SetChrPos(0xA, -8960, 0, 24860, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_8B9")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B3")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_8B9")

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7CD")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_8B9")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7FD")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    Jump("loc_8B9")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_837")
    SetChrPos(0x9, -6350, 0, 25950, 180)
    SetChrPos(0xA, -6330, 0, 24330, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_8B9")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_860")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_END)), "loc_889")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8B9")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    ClearChrFlags(0xD, 0x80)

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 3)
    Event(0, 31)
    Jump("loc_91B")

    label("loc_8EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    Event(0, 32)
    Jump("loc_91B")

    label("loc_905")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Event(0, 37)

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_92A")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_942")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_942")

    Return()

    # Function_4_5FD end

    def Function_5_943(): pass

    label("Function_5_943")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_964")
    Jump("loc_995")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_978")
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_995")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_986")
    Jump("loc_995")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_995")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_995")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9A7")
    Jump("loc_9E4")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9C1")
    Jump("loc_9E4")

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_9D3")
    Jump("loc_9E4")

    label("loc_9D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_9E4")
    OP_66(0x3, 0x1)

    label("loc_9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A35")
    OP_65(0x1, 0x1)

    label("loc_A35")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 10890, -1450, 1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x9, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC6")
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    OP_66(0x2, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACB")

    label("loc_AC6")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_ACB")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE3")
    OP_1B(0x0, 0x0, 0x2B)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AF4")
    OP_24(0x7B)
    Jump("loc_B2A")

    label("loc_AF4")

    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0x1B26, 0x1F4, 0x143C)
    OP_E1(0x7936, 0x1F4, 0xFFFFFD6C)

    label("loc_B2A")

    Return()

    # Function_5_943 end

    def Function_6_B2B(): pass

    label("Function_6_B2B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City - East Exit\x01",      # 0
            "Tangram Gate\x01",                    # 1
            "Bus Stop (Fork)\x01",                 # 2
            "Leave\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCE")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C13")

    label("loc_BCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_C13")

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C13")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_C13")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_B2B end

    def Function_7_C1B(): pass

    label("Function_7_C1B")

    Fade(1000)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -400, 0, -15300, 135)
    SetChrPos(0x1, -1230, 0, -15500, 135)
    SetChrPos(0x2, -2000, 0, -15700, 135)
    SetChrPos(0x3, -2750, 0, -15900, 135)
    ClearChrFlags(0x19, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x19)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x19, 15920, 0, -24600, 0)
    OP_D3(0x19, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_0D()
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_CF7():
        OP_95(0xFE, 10630, 0, -20520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CF7)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_D21():
        OP_9E(0xFE, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_D21)
    WaitChrThread(0x19, 1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x7)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_C1B end

    def Function_8_D5C(): pass

    label("Function_8_D5C")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -700, 0, -13900, 135)
    SetChrPos(0x1, -700, 0, -13900, 135)
    SetChrPos(0x2, -700, 0, -13900, 135)
    SetChrPos(0x3, -700, 0, -13900, 135)
    OP_68(-690, 1500, -13900, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_D5C end

    def Function_9_DF1(): pass

    label("Function_9_DF1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C2")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135F")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_EB2")

    label("loc_E97")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_EB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_EF6")

    label("loc_EE0")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_EF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F24")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_F3A")

    label("loc_F24")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F69")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_F80")

    label("loc_F69")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_F80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_FC6")

    label("loc_FAF")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_FC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF0")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1002")

    label("loc_FF0")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_1002")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1042")

    label("loc_102E")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_1042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107A")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_109A")

    label("loc_107A")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_109A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C8")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_10DE")

    label("loc_10C8")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_10DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1110")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_112A")

    label("loc_1110")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_112A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1164")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1186")

    label("loc_1164")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1186")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B5")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_11CC")

    label("loc_11B5")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_11CC")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1350")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A3"),
        (1, "loc_12B1"),
        (2, "loc_12BF"),
        (3, "loc_12CD"),
        (4, "loc_12DB"),
        (5, "loc_12E9"),
        (6, "loc_12F7"),
        (7, "loc_1305"),
        (8, "loc_1313"),
        (9, "loc_1321"),
        (10, "loc_132F"),
        (11, "loc_133D"),
        (SWITCH_DEFAULT, "loc_134B"),
    )


    label("loc_12A3")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12B1")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12BF")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12CD")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12DB")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12E9")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_12F7")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_1305")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_1313")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_1321")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_132F")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_133D")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_134B")

    label("loc_134B")

    Jump("loc_135A")

    label("loc_1350")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_135A")

    Jump("loc_13BD")

    label("loc_135F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AA")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_13BD")

    label("loc_13AA")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BD")

    Jump("loc_E0B")

    label("loc_13C2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_DF1 end

    def Function_10_13CA(): pass

    label("Function_10_13CA")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 13840, 0, -19790, 225)
    SetChrPos(0x1, 13840, 0, -19790, 225)
    SetChrPos(0x2, 13840, 0, -19790, 225)
    SetChrPos(0x3, 13840, 0, -19790, 225)
    SetChrPos(0x4, 13840, 0, -19790, 225)
    SetChrPos(0x5, 13840, 0, -19790, 225)
    Sleep(1)
    OP_68(13840, 1500, -19790, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_149E")
    Sound(1502, 255, 100, 0)
    Jump("loc_14A4")

    label("loc_149E")

    Sound(1503, 255, 100, 0)

    label("loc_14A4")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_13CA end

    def Function_11_14B9(): pass

    label("Function_11_14B9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_14B9 end

    def Function_12_14C7(): pass

    label("Function_12_14C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E2")

    ChrTalk(
        0xFE,
        (
            "Oh, were you able to find the book?\x01",
            "Phew, what a relief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arc en Ciel books can be pretty darn popular,\x01",
            "I suppose. He wouldn't stop pestering me\x01",
            "unless I gave it to him, so I caved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess this just goes to show the power of\x01",
            "Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_15E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16CC")

    ChrTalk(
        0xFE,
        (
            "I lent that darn book to one of the farmers,\x01",
            "Donald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for him, I'd start at his house.\x01",
            "It should be right next to Reoir General Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I'm real sorry about this, folks.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_16CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E9")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_16E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")

    ChrTalk(
        0xFE,
        (
            "What a fine morning. Perfect\x01",
            "weather for a relaxing drive, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, shucks. I'm startin' to get fired up\x01",
            "to go deliver these here veggies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahem. Just getting ready to go do\x01",
            "some work, that's all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18C0")

    label("loc_17D9")


    ChrTalk(
        0xFE,
        (
            "*sigh* I'm terrible at controlling my\x01",
            "accent when I start thinking about cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always try to keep it under control, so it's really\x01",
            "embarrassing when it accidentally starts to show.\x01",
            "Guess I just have to be more careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C0")

    Jump("loc_2C47")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_198A")

    ChrTalk(
        0xFE,
        (
            "I saw a huge crowd of people while I was\x01",
            "selling vegetables in Crossbell this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some sort of mafia dispute was going on,\x01",
            "I heard. Can't say I'm envious of city folk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C47")

    label("loc_198A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D97")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA3")

    ChrTalk(
        0xFE,
        "*yaaaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crap, I can't be dozing off. This\x01",
            "place is too relaxing for its own good...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xFE, 0x73, 0x1F4)

    ChrTalk(
        0xFE,
        (
            "Eh...? Is that one of the CGF's brand spankin'\x01",
            "new light-armored convoys?! What a beaut!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, it has such a sophisticated form with\x01",
            "no need for any crude armaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shoot, what I wouldn't give to take this baby\x01",
            "for a spin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0505FOh! You understand its greatness!\x02\x03",
            "#0509FI see you're a man of culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FHmm, I don't see the appeal...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CCC")

    label("loc_1BA3")


    ChrTalk(
        0xFE,
        "Ahem. Then allow me to inform you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The new CGF light-armored convoy vehicle\x01",
            "may fall short in combat power, but no one\x01",
            "can deny its graceful body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's just a masterpiece, an absolute masterpiece.\x01",
            "Please try not to scratch it while driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0500FHaha, she's safe in my hands.\x02",
    )

    CloseMessageWindow()

    label("loc_1CCC")

    Jump("loc_1D92")

    label("loc_1CD1")


    ChrTalk(
        0xFE,
        "*yaaaaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crap, I can't be dozing off. This\x01",
            "place is too relaxing for its own good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm always scared I'm gonna end up scratching\x01",
            "the truck on something if I get too tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    Jump("loc_2C47")

    label("loc_1D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        "Final day of the festival, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This year, we had Derek running a food stall,\x01",
            "and some tourists even went so far as to trek\x01",
            "to the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was a pretty odd but exciting festival this\x01",
            "time, I'd say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F3B")

    label("loc_1E94")


    ChrTalk(
        0xFE,
        (
            "This year we had Derek running a food stall,\x01",
            "and some tourists even went so far as to trek\x01",
            "to the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The year's festival didn't hold back.\x02",
    )

    CloseMessageWindow()

    label("loc_1F3B")

    Jump("loc_2C47")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1FEB")

    ChrTalk(
        0xFE,
        (
            "It's the second to last day of the festival, so I thought\x01",
            "I'd give myself a little break this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should take the truck for a spin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C47")

    label("loc_1FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210C")

    ChrTalk(
        0xFE,
        (
            "Just like every year, a lot of tourists have been dropping\x01",
            "by during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think the food stall we set up in the city is\x01",
            "bringing in a lot more people than usual, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, I've never seen the bus drop\x01",
            "off THIS many people before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A5")

    label("loc_210C")


    ChrTalk(
        0xFE,
        (
            "Just like every year, a lot of tourists have been dropping\x01",
            "by during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure glad Crossbell invested\x01",
            "in this nifty bus service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A5")

    Jump("loc_2C47")

    label("loc_21AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22BB")

    ChrTalk(
        0xFE,
        "Sounds like some tourists are headed our way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, Millia's going to be working the\x01",
            "apiary during the Anniversary Festival\x01",
            "instead of Derek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I for one am pretty excited, 'cause\x01",
            "this just means the village will be getting livelier!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C47")

    label("loc_22BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_24B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F2")

    ChrTalk(
        0xFE,
        (
            "Derek's plan for the festival is to open up\x01",
            "a food stall in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has to use the village's truck to transport\x01",
            "the equipment and food, but get this...\x01",
            "He said he'd let me be his driver!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heck yes! Don't worry, Derek! I'll be\x01",
            "the best dang driver you've ever seen!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24B4")

    label("loc_23F2")


    ChrTalk(
        0xFE,
        (
            "Heh. Workin' as a truck driver? My dreams\x01",
            "are finally gonna be a reality!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to knock Derek's socks off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shoot. Pretend you didn't hear\x01",
            "my accent, all right? Hah...haha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B4")

    Jump("loc_2C47")

    label("loc_24B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_266E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2594")

    ChrTalk(
        0xFE,
        (
            "Well, about time to go sell today's crops\x01",
            "over in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commerce through private traders may be\x01",
            "on the rise, but we can't neglect the city's\x01",
            "department store and the like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2669")

    label("loc_2594")


    ChrTalk(
        0xFE,
        (
            "Stores in the city like to buy up our goods\x01",
            "by the truckload, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure, business with Mr. Hayworth and others\x01",
            "is important, but we won't exactly pay the bills\x01",
            "if we ignore all the larger outlets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2669")

    Jump("loc_2C47")

    label("loc_266E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_274B")

    ChrTalk(
        0xFE,
        (
            "As a lover of orbal automobiles, it bums me\x01",
            "out that not many orbal buses stop by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I can't get too down about it. It's\x01",
            "not as if Armorica would be lost without\x01",
            "a connection to the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C47")

    label("loc_274B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_28D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280F")

    ChrTalk(
        0xFE,
        (
            "Buses come and go during the day, but\x01",
            "they rarely bring city folk with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of the riders are villagers coming\x01",
            "home after a day of shopping in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28CD")

    label("loc_280F")


    ChrTalk(
        0xFE,
        (
            "It's unbelievably rare to see people\x01",
            "from the city visit Armorica Village\x01",
            "through the bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bracers? Yeah, they stop by on occasion,\x01",
            "but almost never any regular city folk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CD")

    Jump("loc_2C47")

    label("loc_28D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A54")

    ChrTalk(
        0xFE,
        (
            "The mornin' after the incident, I found my truck\x01",
            "covered head to toe in these ugly scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess, it pisses me off every time\x01",
            "I remember!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This here truck's crucial to the village's business!\x01",
            "Whoever did this has hell to pay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Ahem... Anyway, these scratch marks\x01",
            "definitely came from some kind of canine...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4C")
    SetScenarioFlags(0x68, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A4C")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2AE4")

    label("loc_2A54")


    ChrTalk(
        0xFE,
        (
            "Sorry. Hard to control my accent\x01",
            "whenever I get overexcited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Why was I born that way?\x01",
            "It never happens to my sister, Millia...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE4")

    Jump("loc_2C47")

    label("loc_2AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB9")

    ChrTalk(
        0xFE,
        "Oh, you guys from Crossbell City?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That doesn't seem right, considering\x01",
            "the bus just left a few minutes ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? You WALKED here?! You\x01",
            "city folk must all be crazy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C47")

    label("loc_2BB9")


    ChrTalk(
        0xFE,
        "You're looking for Chief Tolta?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep heading towards the back\x01",
            "of the village and you'll run straight\x01",
            "into his house. Can't miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C47")

    TalkEnd(0xFE)
    Return()

    # Function_12_14C7 end

    def Function_13_2C4B(): pass

    label("Function_13_2C4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C69")
    Call(0, 14)
    Jump("loc_2D38")

    label("loc_2C69")

    OP_93(0xFE, 0xB4, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Okay, time to play bracers!\x01",
            "Who's going to be who?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to be Arios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Then I'll be the big bad wolf!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 500)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Really? You want to be the monster?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_2D38")

    Jump("loc_3866")

    label("loc_2D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2DED")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Stefan said he was going to take the\x01",
            "day off to rest at the Ash Tree Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, did he get sick? Might as well\x01",
            "pay him a visit later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_3866")

    label("loc_2DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2D")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "You're such a slowpoke, Stefan! How could\x01",
            "you let yourself get caught by Pully of all people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tell you what, if you move here, you can take\x01",
            "a complete training session from yours truly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0502FIt's so peaceful here...\x02\x03",
            "It reminds me of just what it\x01",
            "is I fight to protect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F76")

    label("loc_2F2D")


    ChrTalk(
        0xFE,
        "Well, Stefan's 'it,' now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try to catch us before sunset, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_2F76")

    Jump("loc_3866")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_302B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F96")
    Call(0, 14)
    Jump("loc_3026")

    label("loc_2F96")


    ChrTalk(
        0xFE,
        (
            "I really wanted to go have fun at the\x01",
            "Anniversary Festival this year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I can talk Stefan into\x01",
            "letting me come along next year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3026")

    Jump("loc_3866")

    label("loc_302B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30B8")

    ChrTalk(
        0xFE,
        (
            "Oh... So the Anniversary Festival\x01",
            "ends tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, I barely had time to blink.\x01",
            "I guess there's always next year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3866")

    label("loc_30B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D3")
    Call(0, 14)
    Jump("loc_3142")

    label("loc_30D3")


    ChrTalk(
        0xFE,
        (
            "A big race between bracers, police\x01",
            "officers, and gang leaders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, I can't believe I missed that!\x02",
    )

    CloseMessageWindow()

    label("loc_3142")

    Jump("loc_3866")

    label("loc_3147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31B7")

    ChrTalk(
        0xFE,
        (
            "*sigh* I wanted to hang out at the\x01",
            "festival, but Mom told me I couldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So annoying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3866")

    label("loc_31B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3310")

    ChrTalk(
        0xFE,
        (
            "Y'know, that Ilya Platiere from Arc en Ciel\x01",
            "scored herself a sweet nickname.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even just thinking about it gives me the\x01",
            "chills. Ilya Platiere, the Fervent Dancer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe someday I can get an awesome nickname, too...\x01",
            "Something as cool as the Divine Blade of Wind, the\x01",
            "Thunder Bringer, or the Ocean Crasher!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_338D")

    label("loc_3310")


    ChrTalk(
        0xFE,
        "The Fervent Dancer sounds so freakin' cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna be like Arios and Ilya someday\x01",
            "and have a super cool nickname!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338D")

    Jump("loc_3866")

    label("loc_3392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3442")

    ChrTalk(
        0xFE,
        (
            "I've heard people talk about how Crossbell City\x01",
            "is home to a really amazing theatre troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arc en Ciel, wasn't it? I sure hope I can\x01",
            "see them someday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3866")

    label("loc_3442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_351B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345D")
    Call(0, 14)
    Jump("loc_3516")

    label("loc_345D")


    ChrTalk(
        0xFE,
        (
            "Pully kind of sucks at being the monster.\x01",
            "She doesn't know how to be scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's okay. Now that Stefan is here,\x01",
            "we can play lots of different games\x01",
            "that we couldn't before!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3516")

    Jump("loc_3866")

    label("loc_351B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_367C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F3")

    ChrTalk(
        0xFE,
        (
            "*sigh* Arios, you're so cool... When\x01",
            "are you going to come visit again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last time the chickens got outta their coop,\x01",
            "he caught them all in, like, two seconds!\x01",
            "Oh, he's my hero...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3677")

    label("loc_35F3")


    ChrTalk(
        0xFE,
        (
            "I've made up my mind. Someday, I'm gonna\x01",
            "become a bracer, just like Arios! I doubt\x01",
            "I'll ever get to be as cool as him, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3677")

    Jump("loc_3866")

    label("loc_367C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_37D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3760")

    ChrTalk(
        0xFE,
        (
            "So I heard Chief Tolta mention that 'divine wolves'\x01",
            "were the culprit or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pshhh, we don't even need to worry.\x01",
            "If they mess with us again, the great\x01",
            "Camille will teach them a lesson!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_37CD")

    label("loc_3760")


    ChrTalk(
        0xFE,
        (
            "If I wanna become a bracer, I can't\x01",
            "afford to slack off now! Armorica,\x01",
            "you're safe under my protection!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CD")

    Jump("loc_3866")

    label("loc_37D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3866")

    ChrTalk(
        0xFE,
        (
            "Man, this place is too cheery.\x01",
            "It's just plain dull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* What I wouldn't give for something\x01",
            "crazy to happen like last time...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3866")

    TalkEnd(0xFE)
    Return()

    # Function_13_2C4B end

    def Function_14_386A(): pass

    label("Function_14_386A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_392E")
    OP_93(0xF, 0x6B, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "Sweet, the weather's looking good today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We can finally play bracers again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Let's do it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "(They sure are childish...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3E08")

    label("loc_392E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_393C")
    Jump("loc_3E08")

    label("loc_393C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_394A")
    Jump("loc_3E08")

    label("loc_394A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3AC3")
    OP_93(0xF, 0x56, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Oh! Stefan, welcome back!\x01",
            "You're early, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Y-Yeah, about that... Mom said the closing\x01",
            "ceremony would be too crowded, so we\x01",
            "had to leave early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, you better make sure to\x01",
            "tell us all about the Anniversary\x01",
            "Festival sometime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Tell us! Tell us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "S-Sure, I don't mind...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3E08")

    label("loc_3AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AD1")
    Jump("loc_3E08")

    label("loc_3AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C89")
    OP_93(0xD, 0x56, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Hey Mom, check this out. I heard this\x01",
            "from someone who was at the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They said there was this big race between\x01",
            "the bracers, police, and gang leaders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Truly? Oh, my, how scandalous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "A race? Did they fight in it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Can't say I thought people would be\x01",
            "talking about the race all the way out here...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(Hey, rumors spread quick, y'know?)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3E08")

    label("loc_3C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C97")
    Jump("loc_3E08")

    label("loc_3C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CA5")
    Jump("loc_3E08")

    label("loc_3CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CB3")
    Jump("loc_3E08")

    label("loc_3CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3DE3")
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        "Rawr! I'm the big bad wolf!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You ugly monster! How dare you\x01",
            "attack our peaceful village?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As long as the amazingly cool, super awesome\x01",
            "AAA-rank bracer Camille is here, I won't let you\x01",
            "harm this village any longer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Heheheh...! Rawr! Raaaawr!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3E08")

    label("loc_3DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_3DF1")
    Jump("loc_3E08")

    label("loc_3DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3DFF")
    Jump("loc_3E08")

    label("loc_3DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E08")

    label("loc_3E08")

    SetScenarioFlags(0x0, 1)
    Return()

    # Function_14_386A end

    def Function_15_3E0C(): pass

    label("Function_15_3E0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3E85")

    ChrTalk(
        0xFE,
        "Hahaha, I love playing with everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's always super fun being with\x01",
            "my brother and Stefan!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_3E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3EF2")

    ChrTalk(
        0xFE,
        "What are we going to play today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I like games with\x01",
            "lots of running the most.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_3EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400D")

    ChrTalk(
        0xFE,
        (
            "I've played hide-and-seek lots of times\x01",
            "with Camille and Stefan, y'know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm super-duper fast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FI bet these kids would get\x01",
            "along great with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FOh, man. I'm sure. Maybe we should get\x01",
            "her to tag along next time we visit, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4072")

    label("loc_400D")


    ChrTalk(
        0xFE,
        (
            "I've played hide-and-seek lots of times\x01",
            "with Camille and Stefan, y'know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's the funnest!\x02",
    )

    CloseMessageWindow()

    label("loc_4072")

    Jump("loc_47EB")

    label("loc_4077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4092")
    Call(0, 14)
    Jump("loc_4121")

    label("loc_4092")

    OP_93(0xFE, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        "Hey, did you get us souvenirs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Ah, yeah, I got a few... I'll try to\x01",
            "get them to you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Woohoo, thank you! ♪\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_4121")

    Jump("loc_47EB")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41FC")

    ChrTalk(
        0xFE,
        (
            "My brother kept saying he\x01",
            "wanted to see the Anniversary\x01",
            "Festival in the city this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The festival was really\x01",
            "fun for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got to play a ton with\x01",
            "my brother, after all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4254")

    label("loc_41FC")


    ChrTalk(
        0xFE,
        (
            "I had so much fun during\x01",
            "the festival since I got to\x01",
            "play with my brother so much!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4254")

    Jump("loc_47EB")

    label("loc_4259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4274")
    Call(0, 14)
    Jump("loc_42F3")

    label("loc_4274")


    ChrTalk(
        0xFE,
        (
            "Playing is all right, but fighting is\x01",
            "a biiiig no-no!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't be my fault if Mom gets\x01",
            "mad at you, just so you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F3")

    Jump("loc_47EB")

    label("loc_42F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4381")

    ChrTalk(
        0xFE,
        (
            "A lot of strangers have been\x01",
            "walking into the village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you think they will play with\x01",
            "me while they're here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_4381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_441D")

    ChrTalk(
        0xFE,
        (
            "I really want to go see those\x01",
            "ark and shell people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll still be happy if I can just\x01",
            "stay here and play with my brother, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_441D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_44FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AB")

    ChrTalk(
        0xFE,
        "Ark and...shell? What the heck is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess if my brother thinks it's\x01",
            "cool, it must be really great!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44F8")

    label("loc_44AB")


    ChrTalk(
        0xFE,
        (
            "Ark and shell... If my brother wants\x01",
            "to go see it, then I want to, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F8")

    Jump("loc_47EB")

    label("loc_44FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4518")
    Call(0, 14)
    Jump("loc_4562")

    label("loc_4518")


    ChrTalk(
        0xFE,
        "Raaaaawr! You better look out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm gonna eat yoooou! Heeheehee!\x02",
    )

    CloseMessageWindow()

    label("loc_4562")

    Jump("loc_47EB")

    label("loc_4567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_462C")

    ChrTalk(
        0xFE,
        (
            "Stefan has been staying at\x01",
            "the Ash Tree Inn for a while\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he would come play\x01",
            "with me sometimes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. I can always count\x01",
            "on my brother to play with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EB")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_471D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AE")

    ChrTalk(
        0xFE,
        (
            "Umm, did those wolves do something\x01",
            "bad to the village...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't really know what happened.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4718")

    label("loc_46AE")


    ChrTalk(
        0xFE,
        (
            "My mom came to watch me play\x01",
            "a little while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is that 'cause the wolves started appearing?\x02",
    )

    CloseMessageWindow()

    label("loc_4718")

    Jump("loc_47EB")

    label("loc_471D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_47EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A5")

    ChrTalk(
        0xFE,
        "Who the heck are you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huuuh? Police officers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(What an encouraging reaction...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47EB")

    label("loc_47A5")


    ChrTalk(
        0xFE,
        "Po-lice! I'll remember that now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But what do they do again?\x02",
    )

    CloseMessageWindow()

    label("loc_47EB")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E0C end

    def Function_16_47EF(): pass

    label("Function_16_47EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4904")

    ChrTalk(
        0xFE,
        (
            "I keep making excuses to avoid taking\x01",
            "the first step, but enough is enough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, I'm going to ask that guy to let me\x01",
            "join the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last time, I was too shy to so much as\x01",
            "step into their office, but now's the time!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4954")

    label("loc_4904")


    ChrTalk(
        0xFE,
        (
            "I love fishing and so do they! This time,\x01",
            "I'll definitely become a member!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4954")

    Jump("loc_56D4")

    label("loc_4959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4A18")

    ChrTalk(
        0xFE,
        (
            "That Fisherman's Guild member over there...\x01",
            "All he does is cast his line and stare out into space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks pretty relaxing. Maybe someday I'll\x01",
            "get to cast a rod, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_4A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AA5")

    ChrTalk(
        0xFE,
        "One of the Fisherman's Guild members has returned?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wh-What do I do? Is this finally my big chance\x01",
            "to join the guild?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_4AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4BB3")

    ChrTalk(
        0xFE,
        (
            "I just can't do it. The whole festival has passed by,\x01",
            "and I couldn't bring myself to go to their guild at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not the end of the world. They were\x01",
            "probably insanely busy with the festival, anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I'm hopeless, aren't I?\x02",
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_4BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4C76")

    ChrTalk(
        0xFE,
        (
            "A bunch of tourists stopped by today,\x01",
            "but I couldn't find any members of the\x01",
            "Fisherman's Guild among them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe waiting to be scouted by one of\x01",
            "them isn't the best idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_4C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D5B")

    ChrTalk(
        0xFE,
        (
            "Wait, on the bridge over there...\x01",
            "Those guys are fishing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They must be Fisherman's Guild members...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Think, Salem, think! Should I go for it\x01",
            "and try to strike up a conversation...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DFB")

    label("loc_4D5B")


    ChrTalk(
        0xFE,
        (
            "I'd love to be a part of the Fisherman's Guild,\x01",
            "and there are members standing right there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But what if they don't want to be\x01",
            "bothered right now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFB")

    Jump("loc_56D4")

    label("loc_4E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE6")

    ChrTalk(
        0xFE,
        (
            "Loads of tourists have been coming\x01",
            "to visit the village lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll stay here by the water, in case someone\x01",
            "from the Fisherman's Guild stops by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why, you ask? To be recruited, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F8B")

    label("loc_4EE6")


    ChrTalk(
        0xFE,
        (
            "Maybe if I stare at the water long enough,\x01",
            "someone from the Fisherman's Guild will\x01",
            "notice and strike up a conversation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hopefully, someone notices me...\x02",
    )

    CloseMessageWindow()

    label("loc_4F8B")

    Jump("loc_56D4")

    label("loc_4F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E9")

    ChrTalk(
        0xFE,
        (
            "I tried gathering every bit of courage I could\x01",
            "muster yesterday to travel to the Fisherman's\x01",
            "Guild in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I joined them, I'd be able to spend the\x01",
            "rest of my days in bliss, fishing all day\x01",
            "long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But in the end, I wasn't confident\x01",
            "enough to go inside. Ugh, why do I\x01",
            "have to be so timid?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5143")

    label("loc_50E9")


    ChrTalk(
        0xFE,
        (
            "*sigh* I'm a joke. It looks like the Fisherman's Guild\x01",
            "is still far out of my reach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5143")

    Jump("loc_56D4")

    label("loc_5148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_52EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523D")

    ChrTalk(
        0xFE,
        (
            "I thought that my desire to fish would\x01",
            "overpower my shyness, but it seems I\x01",
            "was sadly mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's it! I'm going to take the bus to the\x01",
            "Fisherman's Guild and pass whatever\x01",
            "entrance exam they throw at me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52E5")

    label("loc_523D")


    ChrTalk(
        0xFE,
        (
            "I think I'm finally going to visit the\x01",
            "Fisherman's Guild a bit later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* My heart is going to beat out\x01",
            "of my chest. Are they going to let me\x01",
            "join or not?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E5")

    Jump("loc_56D4")

    label("loc_52EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_53A0")

    ChrTalk(
        0xFE,
        "*sigh* I just want to be able to fish...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I joined the Fisherman's Guild, would\x01",
            "they give me some starting gear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If only I could find a way to join...\x02",
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_53A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5459")

    ChrTalk(
        0xFE,
        (
            "Oh... You four must have come\x01",
            "from Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys have a Fisherman's Guild\x01",
            "there, right? Must be nice having\x01",
            "one within walking distance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5503")

    label("loc_5459")


    ChrTalk(
        0xFE,
        (
            "Oh, being a part of the Fisherman's Guild\x01",
            "sure sounds nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet they spend every day fishing\x01",
            "all over Crossbell. Honestly, it's\x01",
            "hard not to feel jealous...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5503")

    Jump("loc_56D4")

    label("loc_5508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_55C6")

    ChrTalk(
        0xFE,
        (
            "Huh? You want to know about the\x01",
            "night those wolves attacked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm... Well, I know it's been about three weeks\x01",
            "since then. Sorry, I don't remember much more\x01",
            "than that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_55C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_56D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5664")

    ChrTalk(
        0xFE,
        (
            "That clean gleam of the water...\x01",
            "The shadows of the fish outlined\x01",
            "by the bright sunlight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Amazing. Absolutely amazing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_56D4")

    label("loc_5664")


    ChrTalk(
        0xFE,
        (
            "Oh, man! I think I saw a massive\x01",
            "shadow just now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, what I wouldn't give to own\x01",
            "my own fishing rod!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D4")

    TalkEnd(0xFE)
    Return()

    # Function_16_47EF end

    def Function_17_56D8(): pass

    label("Function_17_56D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_589D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5804")

    ChrTalk(
        0xFE,
        (
            "It's not as if I want the village to give up\x01",
            "traditions, or harm the environment in the\x01",
            "name of progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I want is for the villagers to be able to\x01",
            "live a long, abundant life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to do that, we have to make people\x01",
            "interested and want to come here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5898")

    label("loc_5804")


    ChrTalk(
        0xFE,
        (
            "All I want is for the villagers to be able to\x01",
            "live a long, abundant life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father always--\x01",
            "The village chief never seems to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5898")

    Jump("loc_64C6")

    label("loc_589D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59BA")

    ChrTalk(
        0xFE,
        (
            "Why exactly has Crossbell City decided\x01",
            "to modernize like they have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And why is Armorica Village so intent on\x01",
            "living in the past, when the future is now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can't figure out those reasons,\x01",
            "any hope of modernizing the village\x01",
            "will disappear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A5A")

    label("loc_59BA")


    ChrTalk(
        0xFE,
        (
            "Why exactly has Crossbell City decided\x01",
            "to modernize like they have?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Armorica has any chance of doing the\x01",
            "same, we'll have to answer that question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A5A")

    Jump("loc_64C6")

    label("loc_5A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B46")

    ChrTalk(
        0xFE,
        (
            "When I ran a stall during the Anniversary\x01",
            "Festival, a lot of tourists started coming\x01",
            "to the village. Talk about a surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to come up with new, improved\x01",
            "ways to do things around here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BB9")

    label("loc_5B46")


    ChrTalk(
        0xFE,
        (
            "As the next village chief, it falls onto me\x01",
            "to make sure our beloved village doesn't\x01",
            "come to an untimely end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB9")

    Jump("loc_64C6")

    label("loc_5BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5BCC")
    Jump("loc_64C6")

    label("loc_5BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5BDA")
    Jump("loc_64C6")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5BE8")
    Jump("loc_64C6")

    label("loc_5BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BF6")
    Jump("loc_64C6")

    label("loc_5BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C04")
    Jump("loc_64C6")

    label("loc_5C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D4A")

    ChrTalk(
        0xFE,
        (
            "I proposed that Armorica Village open up a\x01",
            "stall in Crossbell City during the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given how many people are going to show\x01",
            "up, I think it's a good opportunity to get\x01",
            "Armorica Village's name out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Displaying our honey would probably\x01",
            "attract people by the droves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DCB")

    label("loc_5D4A")


    ChrTalk(
        0xFE,
        (
            "Putting our honey front and center in\x01",
            "the stall is probably our best bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe Mr. Reoir would give me some advice...\x02",
    )

    CloseMessageWindow()

    label("loc_5DCB")

    Jump("loc_64C6")

    label("loc_5DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EAC")

    ChrTalk(
        0xFE,
        (
            "Do you think it's strange for the village\x01",
            "chief's son to work in the apiary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You shouldn't. How can I ever succeed my\x01",
            "father if I don't understand the work that\x01",
            "sustains our village?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F7F")

    label("loc_5EAC")


    ChrTalk(
        0xFE,
        (
            "After all, it's impossible to govern a\x01",
            "community you know nothing about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not in it for my ego or to be admired.\x01",
            "All that matters to me is doing whatever\x01",
            "I can to improve our village's way of life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7F")

    Jump("loc_64C6")

    label("loc_5F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_610E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_608F")

    ChrTalk(
        0xFE,
        (
            "Thanks to humble traders like Mr. Hayworth,\x01",
            "Armorica Village is able to stay afloat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of the village's children inevitably end\x01",
            "up living in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, there will be no one left.\x01",
            "I have to do something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6109")

    label("loc_608F")


    ChrTalk(
        0xFE,
        (
            "If our village wants to survive, we can't keep\x01",
            "living in the past. And it's my job to help us\x01",
            "start looking forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6109")

    Jump("loc_64C6")

    label("loc_610E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_6340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_625C")

    ChrTalk(
        0xFE,
        (
            "Earlier, I heard the chief mention something\x01",
            "about divine wolves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He may be my father, but I can't help getting\x01",
            "annoyed that he won't let go of silly things like\x01",
            "so-called 'divine wolves.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just want him to start focusing on\x01",
            "improving the village, not worrying\x01",
            "about things from the past.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_633B")

    label("loc_625C")


    ChrTalk(
        0xFE,
        (
            "We lost livestock in the attack, which was a\x01",
            "direct result of a lack of village defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was right. The village HAS to adapt. Chief\x01",
            "Tolta's--no, Father's way of running the village\x01",
            "isn't going to work anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_633B")

    Jump("loc_64C6")

    label("loc_6340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_64C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6432")
    OP_93(0xFE, 0x12A, 0x0)

    ChrTalk(
        0xFE,
        (
            "If things keep going like this, I don't know how\x01",
            "long the village will last...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "What? Can't you see that I'm busy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? You have business with Chief Tolta?\x01",
            "His house is right over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_64C6")

    label("loc_6432")


    ChrTalk(
        0xFE,
        (
            "You have business with Chief Tolta, right?\x01",
            "His house is right over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has a guest, but they should be\x01",
            "wrapping up right about now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C6")

    TalkEnd(0xFE)
    Return()

    # Function_17_56D8 end

    def Function_18_64CA(): pass

    label("Function_18_64CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64DB")
    Jump("loc_6CD3")

    label("loc_64DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_664D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65FD")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Earlier, I baked an apple pie that we\x01",
            "could have for an afternoon snack, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...if Stefan doesn't hurry up, this tasty\x01",
            "snack is going to have to wait.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65A6():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_65A6)

    def lambda_65B3():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_65B3)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0x9,
        "You serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No way!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    SetScenarioFlags(0x0, 5)
    Jump("loc_6648")

    label("loc_65FD")


    ChrTalk(
        0xFE,
        (
            "If Stefan doesn't hurry and get over\x01",
            "here, the pie will have to wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6648")

    Jump("loc_6CD3")

    label("loc_664D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_665B")
    Jump("loc_6CD3")

    label("loc_665B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6669")
    Jump("loc_6CD3")

    label("loc_6669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6677")
    Jump("loc_6CD3")

    label("loc_6677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_66E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6692")
    Call(0, 14)
    Jump("loc_66DD")

    label("loc_6692")


    ChrTalk(
        0xFE,
        (
            "Goodness, the city sounds more dangerous\x01",
            "with every new story I hear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66DD")

    Jump("loc_6CD3")

    label("loc_66E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_66F0")
    Jump("loc_6CD3")

    label("loc_66F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_66FE")
    Jump("loc_6CD3")

    label("loc_66FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_670C")
    Jump("loc_6CD3")

    label("loc_670C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681F")

    ChrTalk(
        0xFE,
        (
            "He's making his little sister be the monster while\x01",
            "he keeps the bracer role to himself? My son\x01",
            "has a thing or two to learn about selfishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess Pully does look like she's having the time\x01",
            "of her life, so I'll let it slide this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_688D")

    label("loc_681F")

    OP_93(0xD, 0x56, 0x0)

    ChrTalk(
        0xFE,
        "Camille!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the big brother, you should let Pully\x01",
            "be the bracer every once in a while,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_688D")

    Jump("loc_6CD3")

    label("loc_6892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_6A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693D")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xD,
        "Camille, Pully, it's time to go home!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "But we're still playing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah, we're playing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "*sigh* Oh, dear.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_69FD")

    label("loc_693D")


    ChrTalk(
        0xFE,
        (
            "If you left them alone, kids would play\x01",
            "until they ran completely out of juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, they always eat their meals and\x01",
            "play, so I should be happy that they're\x01",
            "as healthy as they are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69FD")

    Jump("loc_6CD3")

    label("loc_6A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_6C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5E")

    ChrTalk(
        0xFE,
        (
            "During the day, you'll find my husband\x01",
            "tending the fields near the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's on his lunch break now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all this talk of monsters and\x01",
            "the recent attack, I wish he wouldn't\x01",
            "stray too far from the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been worried sick ever since that\x01",
            "happened. I rarely let my kids out of\x01",
            "my sight now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C2C")

    label("loc_6B5E")


    ChrTalk(
        0xFE,
        (
            "With all this talk of monsters and\x01",
            "the recent attack, I wish he wouldn't\x01",
            "stray too far from the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been worried sick ever since that\x01",
            "happened. I rarely let my kids out of\x01",
            "my sight now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2C")

    Jump("loc_6CD3")

    label("loc_6C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6CD3")

    ChrTalk(
        0xFE,
        (
            "These two bundles of energy are my kids.\x01",
            "Cute, aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, after what happened, I'm afraid\x01",
            "to let them play outside by themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6CD3")

    TalkEnd(0xFE)
    Return()

    # Function_18_64CA end

    def Function_19_6CD7(): pass

    label("Function_19_6CD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6CE8")
    Jump("loc_7037")

    label("loc_6CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CF6")
    Jump("loc_7037")

    label("loc_6CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6D04")
    Jump("loc_7037")

    label("loc_6D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6DA1")

    ChrTalk(
        0xFE,
        (
            "Derek should be coming back any minute\x01",
            "now, so I'll take care of the apiary until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* It was as tough as I thought it'd be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7037")

    label("loc_6DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6E65")

    ChrTalk(
        0xFE,
        (
            "It's nice that people came to visit the village,\x01",
            "but their looks kind of make me uneasy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get that they're curious, but all the staring\x01",
            "makes it easy to get distracted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7037")

    label("loc_6E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6F16")

    ChrTalk(
        0xFE,
        (
            "A whole lot of tourists came\x01",
            "to visit Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad that they're enjoying themselves, but\x01",
            "I hope they don't get in the way of our farmwork.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7037")

    label("loc_6F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6FE8")

    ChrTalk(
        0xFE,
        (
            "Derek volunteered to be our Anniversary\x01",
            "Festival stall's salesman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that ended with me in charge of the apiary\x01",
            "for the whole Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, 'bout time I got to work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7037")

    label("loc_6FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FF6")
    Jump("loc_7037")

    label("loc_6FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7004")
    Jump("loc_7037")

    label("loc_7004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7012")
    Jump("loc_7037")

    label("loc_7012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_7020")
    Jump("loc_7037")

    label("loc_7020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_702E")
    Jump("loc_7037")

    label("loc_702E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7037")

    label("loc_7037")

    TalkEnd(0xFE)
    Return()

    # Function_19_6CD7 end

    def Function_20_703B(): pass

    label("Function_20_703B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70DA")

    ChrTalk(
        0xFE,
        (
            "Honestly, life in Armorica Village doesn't\x01",
            "look too shabby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should try asking Mom if we\x01",
            "could move out here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7150")

    label("loc_70DA")


    ChrTalk(
        0xFE,
        (
            "The other kids are pretty childish, and\x01",
            "this place is deep in the sticks.\x01",
            "...But maybe life here isn't that bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7150")

    Jump("loc_730C")

    label("loc_7155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7163")
    Jump("loc_730C")

    label("loc_7163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7203")

    ChrTalk(
        0xFE,
        (
            "*pant* *pant* Did I really just lose\x01",
            "in a race against a girl...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe living among nature has given\x01",
            "them an edge against city kids...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_730C")

    label("loc_7203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7293")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721E")
    Call(0, 14)
    Jump("loc_728E")

    label("loc_721E")


    ChrTalk(
        0xFE,
        (
            "(These kids aren't too bad... They\x01",
            "keep inviting me to play with them,\x01",
            "and we end up having a lot of fun.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_728E")

    Jump("loc_730C")

    label("loc_7293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_72A1")
    Jump("loc_730C")

    label("loc_72A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_72AF")
    Jump("loc_730C")

    label("loc_72AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_72BD")
    Jump("loc_730C")

    label("loc_72BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_72CB")
    Jump("loc_730C")

    label("loc_72CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_72D9")
    Jump("loc_730C")

    label("loc_72D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_72E7")
    Jump("loc_730C")

    label("loc_72E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_72F5")
    Jump("loc_730C")

    label("loc_72F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_7303")
    Jump("loc_730C")

    label("loc_7303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_730C")

    label("loc_730C")

    TalkEnd(0xFE)
    Return()

    # Function_20_703B end

    def Function_21_7310(): pass

    label("Function_21_7310")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_73CE")

    ChrTalk(
        0xFE,
        (
            "Taking it easy and relaxing in Armorica\x01",
            "Village is one of life's greatest treasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know what? I think I'll treat myself to\x01",
            "a tasty carp I caught today for lunch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73CE")

    TalkEnd(0xFE)
    Return()

    # Function_21_7310 end

    def Function_22_73D2(): pass

    label("Function_22_73D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7478")

    ChrTalk(
        0xFE,
        (
            "Hmm, the weather around these parts\x01",
            "is wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure that this stream's carp are\x01",
            "going to be a one-of-a-kind delicacy.\x01",
            "Let the fun begin!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7478")

    TalkEnd(0xFE)
    Return()

    # Function_22_73D2 end

    def Function_23_747C(): pass

    label("Function_23_747C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7510")
    Jump("loc_755A")

    label("loc_7510")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7530")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_755A")

    label("loc_7530")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7550")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_755A")

    label("loc_7550")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_755A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7726")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_763F")

    ChrTalk(
        0xFE,
        (
            "People say that there's an elusive species of\x01",
            "fish that swims near Old Armorica Road and\x01",
            "somewhere in the Mainz area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, why don't you try to catch one?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7721")

    label("loc_763F")


    ChrTalk(
        0xFE,
        (
            "People say that there's an elusive species of\x01",
            "fish that swims near Old Armorica Road and\x01",
            "somewhere in the Mainz area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, without using some deluxe dumplings as bait,\x01",
            "you're going to have a hard time catching one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7721")

    Jump("loc_7BA8")

    label("loc_7726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_776D")

    ChrTalk(
        0xFE,
        "Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The butterflies sure are out and about.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BA8")

    label("loc_776D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_784F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7836")

    ChrTalk(
        0xFE,
        (
            "Unfortunately, Master Fisherman Lloyd had to\x01",
            "head on back to his home in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without an angler like him around, things\x01",
            "went from exciting to boring real quick.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_784A")

    label("loc_7836")


    ChrTalk(
        0xFE,
        "So relaxing...\x02",
    )

    CloseMessageWindow()

    label("loc_784A")

    Jump("loc_7BA8")

    label("loc_784F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_79D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7941")

    ChrTalk(
        0x12,
        "The weather is incredible today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Still, I'll have to return to the city eventually.\x01",
            "Just going to do a little more fishin' first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Me and the branch manager had\x01",
            "some plans to go night fishing later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_79CE")

    label("loc_7941")


    ChrTalk(
        0x12,
        (
            "Branch Manager Cerdan is an oddball,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You can find the Fisherman's Guild on\x01",
            "East Street, if you want to say hello.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79CE")

    Jump("loc_7BA8")

    label("loc_79D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_7BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A07")
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A02")
    SetScenarioFlags(0x68, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A02")

    Jump("loc_7BA8")

    label("loc_7A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B25")

    ChrTalk(
        0x12,
        (
            "Armorica Village has a ton of real\x01",
            "good fishing spots, so me and my\x01",
            "buddies come out here often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Plus, they got a really good inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSo, I take it you're a regular?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You got that right. Hard to beat a place\x01",
            "as comfortable and quiet as Armorica.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7BA8")

    label("loc_7B25")


    ChrTalk(
        0x12,
        (
            "By the way, you can find the Fisherman's\x01",
            "Guild on East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you're in the area, make sure to stop\x01",
            "by for a minute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BA8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_747C end

    def Function_24_7BB0(): pass

    label("Function_24_7BB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CAD")

    ChrTalk(
        0xFE,
        (
            "All I really had planned for the festival was watching\x01",
            "Arc en Ciel perform, so I thought I might as well come\x01",
            "spend some time in this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Place is pretty nice. I'll probably take it\x01",
            "easy here until the festival ends.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D3B")

    label("loc_7CAD")


    ChrTalk(
        0xFE,
        (
            "I'm happy enough just being able to see an Arc en Ciel\x01",
            "performance, so I'm just going to spend\x01",
            "the rest of the festival in this village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D3B")

    TalkEnd(0xFE)
    Return()

    # Function_24_7BB0 end

    def Function_25_7D3F(): pass

    label("Function_25_7D3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DD6")

    ChrTalk(
        0xFE,
        "Whoa... This place is so soothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After seeing the city's crowds, it's hard\x01",
            "to believe we're still in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7E7E")

    label("loc_7DD6")


    ChrTalk(
        0xFE,
        (
            "The sights so far are really pretty, too...\x01",
            "Maybe coming here wasn't such a bad\x01",
            "idea after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that an inn over there? We should\x01",
            "book a room first thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E7E")

    TalkEnd(0xFE)
    Return()

    # Function_25_7D3F end

    def Function_26_7E82(): pass

    label("Function_26_7E82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F8F")

    ChrTalk(
        0xFE,
        (
            "It's crazy how different the culture is\x01",
            "in Armorica compared to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And here I thought I was going to see all\x01",
            "sorts of high-tech agriculture orbments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess it's refreshing to have places\x01",
            "that withstand modern times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8039")

    label("loc_7F8F")


    ChrTalk(
        0xFE,
        (
            "I guess it's refreshing to have places\x01",
            "that withstand modern times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this place was exactly like Crossbell City,\x01",
            "there wouldn't be anything special about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8039")

    TalkEnd(0xFE)
    Return()

    # Function_26_7E82 end

    def Function_27_803D(): pass

    label("Function_27_803D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8119")

    ChrTalk(
        0xFE,
        (
            "The soft murmuring of the river, the chirping\x01",
            "of the birds, the gorgeous scenery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet Armorica would be the perfect\x01",
            "place for a nice picnic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And speaking of picnics, I'm starving.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_81CA")

    label("loc_8119")


    ChrTalk(
        0xFE,
        (
            "I bet Armorica would be the perfect\x01",
            "place for a nice picnic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Plenty of rice balls with a tiny sprinkle\x01",
            "of salt... Mmm, I can't help but drool\x01",
            "when I think about them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81CA")

    TalkEnd(0xFE)
    Return()

    # Function_27_803D end

    def Function_28_81CE(): pass

    label("Function_28_81CE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1250, 1750, 6100, 0)
    MoveCamera(316, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -2000, 500, 6000, 90)
    SetChrPos(0x102, -2200, 400, 7250, 135)
    SetChrPos(0x103, -1800, 410, 4760, 45)
    SetChrPos(0x104, -3000, 450, 5750, 90)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    ChrTalk(
        0x12,
        "Such a pretty day...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0x12, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x12, 0x10E, 0x1F4)

    ChrTalk(
        0x12,
        (
            "Oh, you guys here to do a little\x01",
            "fishing, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FNot exactly. We're officers from the Crossbell\x01",
            "Police Department.\x02\x03",
            "#0001FWe're here to investigate the monster attack\x01",
            "that took place roughly three weeks ago.\x02\x03",
            "You don't strike me as Armorican, but if you\x01",
            "know anything about it, anything at all, I'd\x01",
            "appreciate it if you told us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Oh, you came about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If memory serves me right, I was trying to\x01",
            "catch a pythonhead around then, so I wasn't\x01",
            "actually in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You can bet your horses I heard the stories\x01",
            "afterwards, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FI see... Thank you for your help.\x01",
            "We'll have to find leads elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Sorry I couldn't tell you more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "But man, y'all have to travel all\x01",
            "the way out here for police stuff?\x01",
            "Not gonna lie, that sounds rough.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        "Oh, that reminds me. You guys happen to fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "A day as beautiful as this comes once in a blue\x01",
            "moon. Would be a shame if you weren't able to\x01",
            "kick back and enjoy the sun for a bit!\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x12, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x32),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 and\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x18B, 10)
    AddItemNumber(0x187, 10)

    ChrTalk(
        0x12,
        "Oh! I can't forget about this, either.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x3, 10)
    OP_98(0x12, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)

    ChrTalk(
        0x12,
        "This notebook is an angler's best friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You can use it to record every detail\x01",
            "about every catch, from color to size!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FA-Are you sure this is okay? It's like you're\x01",
            "giving us an entire starting kit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Eh, no worries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm a part of the Fisherman's Guild.\x01",
            "Our whole mission is to promote\x01",
            "the culture and greatness of fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's common practice for us to have a few\x01",
            "beginner sets on hand, in case we run into\x01",
            "someone interested in fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8A3A")

    ChrTalk(
        0x101,
        (
            "#0003F(We stopped by their building before...\x01",
            "I think I have a better idea of what they\x01",
            "do now after meeting this guy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A63")

    label("loc_8A3A")


    ChrTalk(
        0x101,
        "#0003F(Is this guild a real thing?)\x02",
    )

    CloseMessageWindow()

    label("loc_8A63")


    ChrTalk(
        0x104,
        (
            "#0300FHey, this is a stroke of luck. Now we've\x01",
            "got a nice hobby we can do between\x01",
            "jobs or somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FRight. While one of us--not me--fishes,\x01",
            "the rest can take the chance to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FRest is a necessity, you know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_8C26")

    ChrTalk(
        0x101,
        (
            "#0011FFrom what you're saying, I'm guessing you\x01",
            "two are still tired from the walk here.\x02\x03",
            "#0000FWell, who am I to refuse a gift?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Awesome. I hope it serves ya well!\x02",
    )

    CloseMessageWindow()
    Jump("loc_901A")

    label("loc_8C26")


    ChrTalk(
        0x101,
        (
            "#0006FFrom what you're saying, I'm guessing you\x01",
            "two are still tired from the walk here.\x02\x03",
            "#0008F(Now that I think about it, the last time\x01",
            "I fished was when Guy first taught me...)\x02\x03",
            "#0003F(Once Guy joined the police, we never\x01",
            "had much time to go, but maybe I should\x01",
            "try to get back into it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "If you're itchin' to try it out, there's a\x01",
            "pretty nice fishing spot in Armorica.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9520, 1750, -180, 5000)
    MoveCamera(329, 23, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(18580, 5000)
    OP_93(0x12, 0x5A, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x12,
        (
            "See that lil' jetty over there? Cast your line\x01",
            "'round there and you'll get bites in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI appreciate the advice.\x01",
            "Thanks for everything.\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A ripple on the water's surface indicates a prime\x01",
            "spot for fishing.\x02\x03",
            "After interacting with a fishing spot and selecting\x01",
            "the proper rod and bait, Lloyd will cast his line.\x02\x03",
            "When the ! mark pops up, quickly press #163I\x01",
            "to reel in Lloyd's catch.\x01",
            "(Careful! The fish can get away with the bait!)\x02\x03",
            "Information regarding caught fish is recorded in\x01",
            "the Fishing Notebook, so give it a look!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_901A")

    SetChrPos(0x0, -2000, 500, 6000, 90)
    OP_93(0x12, 0x5A, 0x0)
    SetChrChipByIndex(0x12, 0xE)
    SetChrSubChip(0x12, 0x0)
    SetScenarioFlags(0x69, 1)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_81CE end

    def Function_29_9044(): pass

    label("Function_29_9044")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FSorry, Armorican carp, but you're\x01",
            "about to get schooled.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(11620, 1500, 1410, 1500)
    MoveCamera(328, 26, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16250, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912A")
    OP_E0(0x2)
    MiniGame(0x6, 0x17, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_912A")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_29_9044 end

    def Function_30_912F(): pass

    label("Function_30_912F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9145")
    Call(0, 38)
    Jump("loc_91E2")

    label("loc_9145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9156")
    Call(0, 6)
    Jump("loc_91E2")

    label("loc_9156")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0003FWhile we're here, let's dig up whatever leads\x01",
            "we can about the monsters and then head back.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_91E2")

    Return()

    # Function_30_912F end

    def Function_31_91E3(): pass

    label("Function_31_91E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(16300, 1500, -24840, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15300, 0)
    OP_68(15110, 1350, -23260, 2500)
    SetChrPos(0x101, 17180, 0, -23450, 315)
    SetChrPos(0x102, 18600, 0, -25290, 315)
    SetChrPos(0x103, 17790, 0, -26560, 315)
    SetChrPos(0x104, 16230, 0, -24520, 315)

    def lambda_9281():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9281)

    def lambda_929B():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_929B)

    def lambda_92B5():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92B5)

    def lambda_92CF():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92CF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100386V#11P#0002FPhew. So this is Armorica Village.\x02",
    )

    CloseMessageWindow()

    def lambda_9343():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9343)

    def lambda_9350():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9350)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1100387V#0000F#5PElie, Tio, how are you holding up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100388V#0102F#12PI'm okay... Though, I'm not sure how\x01",
            "I'd be faring without that break.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1100389V#0206F#6PI am also alive, by some miracle.\x02\x03",
            "#1100390V#0202FThough, miracles aside, this village\x01",
            "is absolutely breathtaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    OP_24(0x7B)
    OP_68(15110, 2350, -23260, 2500)

    def lambda_94A7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94A7)

    def lambda_94B4():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94B4)
    Sleep(100)

    def lambda_94C4():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94C4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sleep(1000)
    Fade(1000)
    OP_68(-37350, 1500, 69780, 0)
    MoveCamera(338, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(53190, 0)
    OP_68(-21000, 1500, 74410, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(7400, 1500, 48380, 0)
    MoveCamera(323, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37470, 0)
    OP_68(-12130, 1500, 35080, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(-1020, 5100, 4110, 0)
    MoveCamera(338, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44250, 0)
    PlaceName2(340, 40, "c_plac14", 0x0, 3000)
    OP_68(-1020, 2800, 4110, 7000)
    OP_6F(0x1)
    Fade(1000)
    OP_68(15110, 1350, -23260, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_E6()

    ChrTalk(
        0x102,
        (
            "#1100391V#0109F#12PA rural village, surrounded by fields\x01",
            "of blooming flowers. It's absolutely\x01",
            "mesmerizing.\x02\x03",
            "#1100392V#0105FAnd there's a sweet smell hanging\x01",
            "in the air...\x02\x03",
            "#1100393V#0102FIs that honey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100394V#0300F#6PYup. You can almost see the apiary\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100395V#0202F#6PAccording to the database, the honey from\x01",
            "Armorica Village is one of the area's specialties.\x02\x03",
            "#1100396VDue to its quality, the demand for Armorican\x01",
            "honey is quite high, so it is exported all across\x01",
            "the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100397V#0004F#6PYeah, I believe it.\x02\x03",
            "#1100398V#0000FI'd always see it being sold in grocery stores\x01",
            "and markets. This is where it comes from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100399V#0103F#12PThat's right.\x02\x03",
            "#1100400V#0108FIt's rather surreal, experiencing something\x01",
            "firsthand when you've only read about it in\x01",
            "books...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_9976():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9976)
    Sleep(50)

    def lambda_9986():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9986)
    Sleep(50)

    def lambda_9996():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9996)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        "#1100401V#0005F#5P...Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100402V#0104F#12PIt's nothing. Simply thinking aloud.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1100403V#0101F#12PA tranquil place like this fell victim\x01",
            "to a monster attack...\x02\x03",
            "#1100404VIt's almost hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100405V#0306F#5PCan't blame ya. At first glance, all I see\x01",
            "is a carefree, happy village.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9AEF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AEF)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1100406V#6P#0200FBased on the CGF's report...\x02\x03",
            "#1100407V...they first spoke to the village chief\x01",
            "for details on the incident.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B87():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B87)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100408V#0000F#5POkay, let's do the same. Besides, he probably\x01",
            "stays on top of what happens in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100409V#0100F#12PAll that's left is to find out where he lives.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15500, 0, -23930, 315)
    SetScenarioFlags(0x60, 4)
    OP_29(0x3F, 0x1, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0x1B26, 0x1F4, 0x143C)
    OP_E1(0x7936, 0x1F4, 0xFFFFFD6C)
    ClearScenarioFlags(0x1, 3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_91E3 end

    def Function_32_9CC0(): pass

    label("Function_32_9CC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2170, 4650, 55620, 0)
    MoveCamera(326, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0x101, -2170, 3760, 56260, 180)
    SetChrPos(0x102, -2170, 3760, 56260, 180)
    SetChrPos(0x103, -2170, 3760, 56260, 180)
    SetChrPos(0x104, -2170, 3760, 56260, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(500)
    OP_68(-2170, 4650, 51620, 6000)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(900)
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(900)
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(500)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#1100552V#11P#0303FDivine wolves, eh?\x02\x03",
            "#1100553V#0300FWasn't expectin' such an interesting\x01",
            "story when we walked in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100554V#6P#0003FAgreed.\x02\x03",
            "#1100555V#0001FUnfortunately, there's no way we\x01",
            "can confirm or deny their existence.\x02\x03",
            "#1100556VStill, we can at least count them\x01",
            "among our list of potential suspects.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#1100557V#5P#0102FI thought you might say something\x01",
            "like that.\x02\x03",
            "#1100558V#0103FThat's right. The paw prints found at the\x01",
            "scene of the crime confirm the presence\x01",
            "of some kind of wolf-like beasts.\x02\x03",
            "#1100559V#0101FBut they somehow managed to vanish\x01",
            "without a trace...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#1100560V#2P#0203FIt is certainly bizarre.\x02\x03",
            "#1100561V#0200FIf they left paw prints, you would normally\x01",
            "be able to follow them back to their origin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100562V#6P#0001FRight. Chalk that up as another mystery.\x02\x03",
            "#1100563V#0008FWe're dealing with something that was\x01",
            "able to elude the CGF's investigators...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100564V#11P#0306FWell, if they escaped on a path we could\x01",
            "never follow, there's kinda nothin' we can\x01",
            "do about it.\x02\x03",
            "#1100565V#0300FNo use in frying your brain over it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100566V#6P#0003FI suppose so.\x02\x03",
            "#1100567V#0000FAll right. Let's start with gathering whatever\x01",
            "intel we can around here.\x02\x03",
            "#1100568VAnd considering it's already noon, we might\x01",
            "as well grab lunch while we're here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100569V#5P#0104FI can't wait.\x02\x03",
            "#1100570V#0100FThat hike really stirred up my appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100571V#2P#0202FSame here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100572V#11P#0302FWe could always grab a bite at the inn\x01",
            "while we grab some info, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2100, 3500, 51200, 180)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x60, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_9CC0 end

    def Function_33_A42F(): pass

    label("Function_33_A42F")


    def lambda_A434():
        OP_95(0xFE, -2280, 3500, 51520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A434)

    def lambda_A44E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A44E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_A467():
        OP_95(0xFE, -2230, 3500, 50390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A467)
    WaitChrThread(0x101, 1)

    def lambda_A485():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A485)
    WaitChrThread(0x101, 1)
    Return()

    # Function_33_A42F end

    def Function_34_A492(): pass

    label("Function_34_A492")


    def lambda_A497():
        OP_95(0xFE, -2350, 3500, 52640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A497)

    def lambda_A4B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A4B1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)

    def lambda_A4CA():
        OP_95(0xFE, -3520, 3500, 51770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4CA)
    WaitChrThread(0x102, 1)

    def lambda_A4E8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4E8)
    WaitChrThread(0x102, 1)
    Return()

    # Function_34_A492 end

    def Function_35_A4F5(): pass

    label("Function_35_A4F5")


    def lambda_A4FA():
        OP_95(0xFE, -2340, 3500, 53740, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A4FA)

    def lambda_A514():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A514)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)

    def lambda_A52D():
        OP_95(0xFE, -940, 3500, 51820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A52D)
    WaitChrThread(0x103, 1)

    def lambda_A54B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A54B)
    WaitChrThread(0x103, 1)
    Return()

    # Function_35_A4F5 end

    def Function_36_A558(): pass

    label("Function_36_A558")


    def lambda_A55D():
        OP_95(0xFE, -2430, 3500, 54990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A55D)

    def lambda_A577():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A577)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    def lambda_A590():
        OP_95(0xFE, -2260, 3500, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A590)
    WaitChrThread(0x104, 1)
    Return()

    # Function_36_A558 end

    def Function_37_A5AA(): pass

    label("Function_37_A5AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1760, 750, 20490, 0)
    MoveCamera(332, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18850, 0)
    SetChrPos(0x101, -1500, 0, 19000, 0)
    SetChrPos(0x102, -1500, 0, 21000, 180)
    SetChrPos(0x103, -500, 0, 20000, 270)
    SetChrPos(0x104, -2500, 0, 20000, 90)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    SetCameraDistance(17850, 2000)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#1100617V#12P#0200FShould we put a hold on our\x01",
            "investigation for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100618V#6P#0000FI guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100619V#5P#0306FKinda sucks that we didn't hear anything\x01",
            "useful, though.\x02\x03",
            "#1100620V#0301FSettin' aside the eyewitness testimonies,\x01",
            "I was almost positive someone would have\x01",
            "heard some howlin', y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100621V#11P#0103FIt is strange...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100622V#6P#0006FHmm...\x02\x03",
            "#1100623V#0000FAnyway, I think we've covered just about\x01",
            "everything we can here.\x02\x03",
            "#1100624VWe should pay St. Ursula Medical College\x01",
            "a visit next, so let's start by heading back\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100625V#11P#0100FNo complaints from me.\x02\x03",
            "#1100626V#0106FThough, I can't say I have any desire to\x01",
            "make the trek on foot again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100627V#12P#0206FMe, neither. It is not worth the trouble...\x01",
            "or pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100628V#5P#0302FHaha. You heard the ladies, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100629V#6P#0012FI did, and I agree. Let's go check when\x01",
            "the next bus arrives at the bus stop.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1500, 0, 20000, 135)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x9, 1570, 0, 22510, 135)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x61, 0)
    OP_29(0x3F, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_A5AA end

    def Function_38_AA86(): pass

    label("Function_38_AA86")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00254.itc", 0x20)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(770, 1400, -15710, 0)
    MoveCamera(290, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1460, 0, -15390, 315)
    SetChrPos(0x102, -40, 0, -16470, 315)
    SetChrPos(0x103, 1890, 0, -16120, 270)
    SetChrPos(0x104, 300, 0, -14900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 0, 0, -5910, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1100630V#0000F#5PSo, the next bus comes in...30 minutes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100631V#0306F#12PGeez, that's the absolute worst wait.\x01",
            "It's not too long, but still not short.\x02\x03",
            "#1100632V#0301FI was wantin' to grab a drink at the inn,\x01",
            "but that doesn't give me enough time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100633V#0106F#6PWho cares whether there's enough time or not?\x01",
            "Drinking on duty isn't appropriate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 39)

    ChrTalk(
        0x103,
        "#1100634V#0200F#11P...?\x02",
    )

    CloseMessageWindow()

    def lambda_AD59():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD59)
    Sleep(50)

    def lambda_AD69():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD69)
    Sleep(50)

    def lambda_AD79():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AD79)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1100635V#0005F#5PTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100636V#0105FIs something wrong?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x103,
        (
            "#1100637V#0208F#11PNo... I simply thought I heard something\x01",
            "in the distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100638V#0301FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100639V#0203F#11PI will try maximizing the sensitivity\x01",
            "in order to amplify the sound.\x02\x03",
            "#1100640V#0200FPlease stay quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100641V#0005F#5PS-Sure.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1278, 255, 90, 0)
    OP_68(1340, 1400, -15920, 2000)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    BeginChrThread(0x1A, 1, 0, 40)
    Sound(820, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    TurnDirection(0x103, 0x101, 300)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#1100642V#0203F#6PI am sorry, everyone. It must have been\x01",
            "my imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100643V#0001F#5PDon't worry about it. You don't\x01",
            "have to apologize.\x02\x03",
            "#1100644VThat sound you heard. Could you\x01",
            "describe what it was like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100645V#0208F#6PPossibly.\x02\x03",
            "#1100646V#0201FI could have sworn I heard howling.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1100647V#0301F#2PSeriously...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100648V#0101F#1PAs in, wolf-like monsters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100649V#0206F#6PPlease, do not get your hopes up.\x01",
            "I likely misheard it.\x02\x03",
            "#1100650VIt could have also been a simple\x01",
            "sensor malfunction.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1100651V#0101F#6PWhat should we do? Search the surrounding\x01",
            "area for signs of wolves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100652V#0003F#5PLet me think...\x02\x03",
            "#1100653V#0001FTio, what's the range on your sensors?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B3D2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B3D2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1100654V#0203F#6PWhen operating normally...\x02\x03",
            "#1100655V#0200F...it should be around 50 selge.\x02\x03",
            "#1100656VHowever, in the presence of wind, sound\x01",
            "waves can travel even further. The exact\x01",
            "location is near impossible to pinpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100657V#0305F#2PWhew, damn! That far, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100658V#0108F#1PBut we still won't be able to determine\x01",
            "where the sound came from...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100659V#0006F#5PThat's okay. In the meantime, we'll\x01",
            "just have to keep our ears open.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#1100660V#0208F#6PUm...\x02\x03",
            "#1100661VDo you not think I was simply mistaken?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100662V#0005F#5PNo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100663V#0105F#1PYou said you heard it, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100664V#0203F#6PYes, I did say that...\x02\x03",
            "#1100665V#0208FStill, it is not something the average\x01",
            "person would be able to catch...\x02\x03",
            "#1100666V#0201FWould it not be normal to think I am lying\x01",
            "or that my mind was playing tricks on me...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)
    OP_64(0x102)

    ChrTalk(
        0x104,
        (
            "#1100667V#0306F#2PEh. Maybe, maybe not.\x02\x03",
            "#1100668V#0300FBut we all know that you're one\x01",
            "in a million, Tio Tot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100669V#0205F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100670V#0102F#1PIt's true. Plus, why wouldn't we believe you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100671V#0004F#5PWe might have met recently, but you've\x01",
            "already saved us more times than I can count.\x02\x03",
            "#1100672V#0000FI can't think of any reason to ever doubt you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100673V#0205F#6P...\x02\x03",
            "#1100674V#0203FI apologize, everyone. That question\x01",
            "was silly of me to ask.\x02\x03",
            "#1100675V#0200FPlease, forget about it, if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100676V#0002F#5PU-Uh, sure? I'm not sure if it's that\x01",
            "big a deal...\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    NpcTalk(
        0x18,
        "Man's Voice",
        "#1100677V#3POh, you're still here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BAC5():

        label("loc_BAC5")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_BAC5")

    QueueWorkItem2(0x101, 1, lambda_BAC5)

    def lambda_BAD7():

        label("loc_BAD7")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_BAD7")

    QueueWorkItem2(0x102, 1, lambda_BAD7)

    def lambda_BAE9():

        label("loc_BAE9")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_BAE9")

    QueueWorkItem2(0x103, 1, lambda_BAE9)

    def lambda_BAFB():

        label("loc_BAFB")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_BAFB")

    QueueWorkItem2(0x104, 1, lambda_BAFB)
    Fade(1000)
    OP_68(1210, 1500, -15280, 0)
    MoveCamera(332, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)

    def lambda_BB40():
        OP_95(0xFE, 470, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BB40)
    WaitChrThread(0x18, 1)
    OP_0D()

    ChrTalk(
        0x101,
        "#1100678V#0000FOh, Mr. Hayworth!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x18,
        (
            "#1100679VWere you about to head back to\x01",
            "Crossbell City?\x02",
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
        0x102,
        (
            "#1100680V#0100F#6PYes, that's right.\x02\x03",
            "#1100681VAre you doing the same, Mr. Hayworth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1100682V#3609F#11PIndeed I am. Now that I've picked up souvenirs\x01",
            "for my family, I'm about to return home.\x02\x03",
            "#1100683V#3600FForgive me for assuming, but were you\x01",
            "planning on taking the bus back?\x02\x03",
            "#1100684VWhen does it arrive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100685V#0200F#6PUnfortunately, it will be another half hour,\x01",
            "according to the schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100686V#0300F#6PHey, if you wanna pop a squat and wait\x01",
            "with us, we'd be happy to have ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1100687V#3605F#11POh, I appreciate the offer, but...\x02\x03",
            "#1100688V#3600FHmm, five in total. There should be room,\x01",
            "I think...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x5A, 0x190)

    def lambda_BEBE():
        OP_95(0xFE, 5640, 0, -14430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BEBE)

    def lambda_BED8():

        label("loc_BED8")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_BED8")

    QueueWorkItem2(0x101, 1, lambda_BED8)

    def lambda_BEEA():

        label("loc_BEEA")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_BEEA")

    QueueWorkItem2(0x102, 1, lambda_BEEA)

    def lambda_BEFC():

        label("loc_BEFC")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_BEFC")

    QueueWorkItem2(0x103, 1, lambda_BEFC)

    def lambda_BF0E():

        label("loc_BF0E")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_BF0E")

    QueueWorkItem2(0x104, 1, lambda_BF0E)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Fade(1000)
    OP_68(10480, 1500, -13970, 0)
    MoveCamera(54, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    EndChrThread(0x18, 0x1)
    SetChrPos(0x18, 11830, 0, -13810, 270)
    SetChrSubChip(0x18, 0x0)
    TurnDirection(0x101, 0x18, 0)
    TurnDirection(0x102, 0x18, 0)
    TurnDirection(0x103, 0x18, 0)
    TurnDirection(0x104, 0x18, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#1100689V#3609F#11PEveryone, instead of waiting for the bus,\x01",
            "how about you all hop in my car instead?\x02\x03",
            "#1100690V#3600FI'll get you to Crossbell City in no time flat.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18870, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    EndChrThread(0x1A, 0x1)
    OP_24(0x348)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_AA86 end

    def Function_39_C0D7(): pass

    label("Function_39_C0D7")

    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_39_C0D7 end

    def Function_40_C0F3(): pass

    label("Function_40_C0F3")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_40_C0F3 end

    def Function_41_C136(): pass

    label("Function_41_C136")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-18160, 4700, 64330, 0)
    MoveCamera(339, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18530, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x1E)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -17500, 3500, 60470, 330)
    SetChrPos(0x102, -19270, 3500, 61620, 15)
    SetChrPos(0x103, -15110, 3500, 62020, 330)
    SetChrPos(0x104, -15900, 3500, 59800, 330)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0000FArmorica Village's fields and apiary are\x01",
            "as beautiful as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FCrossbell's esteemed farming village...\x02\x03",
            "Grace's tourist guide might benefit from a\x01",
            "landscape shot of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FIt's picture perfect, that's for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FDue to Armorica's clean air,\x01",
            "it's easy to see from far away.\x02\x03",
            "This may very well be the only place in\x01",
            "Crossbell that you can witness such a\x01",
            "beautiful, untainted sight.\x02\x03",
            "If only there were farmers working in the\x01",
            "fields for our picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThis spot would make a nice photo\x01",
            "for Grace's article, farmers or not.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF7")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#0000FDo you mind taking a few photos\x01",
            "for us, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0108FN-Not at all. Don't expect a masterpiece\x01",
            "from me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
            "Ya just gotta peek through that lens,\x01",
            "give it a lil' click, then bam, we good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0103F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "There are no second chances when\x01",
            "it comes to a picture-perfect moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThe difference in quality between\x01",
            "amateur and professional photography\x01",
            "is immediately apparent.\x02\x03",
            "#0200FI would imagine a simpleton would have\x01",
            "difficulty grasping any level of intricacy\x01",
            "or nuance, however.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#12P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FC-Calm down, everyone. We should\x01",
            "let Elie focus on taking the photo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FRight... I'll try to live up to your\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0xF, 0x1F4)
    OP_93(0x101, 0x14A, 0x1F4)
    OP_93(0x103, 0x14A, 0x1F4)
    OP_93(0x104, 0x14A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#0103FPhew... There we go. I took a\x01",
            "couple of extras, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHey, it looks like you pulled through.\x02\x03",
            "Well? How'd they turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI won't have an answer for you until\x01",
            "I've seen the developed photos.\x02\x03",
            "At the very least, I think they'll\x01",
            "get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt would be a safe assumption to think\x01",
            "Elie has regained her photography skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF70")

    label("loc_CBF7")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0xF, 0x1F4)
    OP_93(0x101, 0x14A, 0x1F4)
    OP_93(0x103, 0x14A, 0x1F4)
    OP_93(0x104, 0x14A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#0103FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_CD8D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_CDA4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_CDBB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_CDD2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_CDE9")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CDE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_CE00")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CE00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_CE17")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CE17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_CE2E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CE2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_CE45")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CE45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF12")

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF70")

    label("loc_CF12")


    ChrTalk(
        0x101,
        (
            "#6P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF70")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16320, 3500, 61370, 330)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x1E)
    OP_29(0x18, 0x1, 0x3)
    Sleep(500)
    OP_65(0x3, 0x1)
    EventEnd(0x5)
    Return()

    # Function_41_C136 end

    def Function_42_CFA6(): pass

    label("Function_42_CFA6")

    EventBegin(0x0)
    Fade(500)
    OP_68(7350, 1500, -13970, 0)
    MoveCamera(6, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23390, 0)
    SetChrPos(0x101, 7060, 0, -13810, 45)
    SetChrPos(0x102, 5760, 0, -14490, 45)
    SetChrPos(0x103, 7000, 0, -15130, 45)
    SetChrPos(0x104, 5890, 0, -13280, 45)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D05E")
    SetChrPos(0x109, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_D089")

    label("loc_D05E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D089")
    SetChrPos(0x10A, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_D089")

    OP_0D()

    ChrTalk(
        0x101,
        "#6P#0000FExcuse me, are you Elkin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHmm? That's right. Need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWe're from the CPD. If you have time,\x01",
            "we'd like to speak with you about something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained they were here to collect the overdue book.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11POh... Yeah, I borrowed that book.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FDo you have it on you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWell, funny thing, that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI may have lent it to someone.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2AD")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_D2AD")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0005FAre you serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FDamn, this is gettin' ridiculous...\x01",
            "Are we at sub-sub-subleasing now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D363")

    ChrTalk(
        0x109,
        "#12P#0505FI wasn't expecting this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D386")

    label("loc_D363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D386")

    ChrTalk(
        0x10A,
        "#12P#0603F...\x02",
    )

    CloseMessageWindow()

    label("loc_D386")


    ChrTalk(
        0x102,
        (
            "#6P#0100FI'm just wondering what sort of book\x01",
            "would get passed around like this. It's\x01",
            "pretty unbelievable, at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI-I'm so sorry! I know I messed up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's just, he wanted to read the book\x01",
            "so badly, I let him borrow it against\x01",
            "my better thinkin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PY'all gotta understand, I'd ain't have done it\x01",
            "if I knew it was gonna turn out like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FP-Please, calm down! If you lent it,\x01",
            "you lent it! What's in the past is in\x01",
            "the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0205FWho exactly did you give it to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAhem. Sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PU-Um, it was Mr. Donald,\x01",
            "one of the farmers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe lives in the house next to\x01",
            "Reoir General Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006F*sigh* Well, everyone, let's hope\x01",
            "that this is the final stretch.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D697")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D697")

    SetChrPos(0x0, 7060, 0, -13810, 45)
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x28, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_42_CFA6 end

    def Function_43_D6BC(): pass

    label("Function_43_D6BC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D777")

    ChrTalk(
        0x101,
        (
            "#0005FOops. We still haven't talked to all the villagers.\x01",
            "That's sort of the reason why we're here.\x02\x03",
            "#0000FWith luck, someone will know something\x01",
            "about the monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7F4")

    ChrTalk(
        0x101,
        (
            "#0004FLet's ride the bus back to the city.\x02\x03",
            "#0000FIf we check the bus stop, we can\x01",
            "see when it'll arrive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7F4")

    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)
    Return()

    # Function_43_D6BC end

    SaveToFile()

Try(main)
