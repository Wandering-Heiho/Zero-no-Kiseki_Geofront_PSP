from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0240.bin",                # FileName
        "c0240",                    # MapName
        "c0240",                    # Location
        0x000F,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 15, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0240",                  # 0
        "Sammie",                 # 1
        "Kendall",                # 2
        "Kendall",                # 3
        "Brigitta",               # 4
        "Old Man Levick",         # 5
        "Old Man Levick",         # 6
        "Olga",                   # 7
        "Olga",                   # 8
        "Detective",              # 9
        "Detective",              # 10
        "Ilya",                   # 11
        "Ilya",                   # 12
        "Rixia",                  # 13
        "Sully",                  # 14
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch21600.itc",                   # 03
        "chr/ch21602.itc",                   # 04
        "chr/ch20100.itc",                   # 05
        "chr/ch20102.itc",                   # 06
        "chr/ch20300.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch27800.itc",                   # 09
        "apl/ch50386.itc",                   # 0A
        "chr/ch05200.itc",                   # 0B
        "chr/ch10000.itc",                   # 0C
        "chr/ch05102.itc",                   # 0D
    ))

    DeclNpc(9060,    10000,   18000,   45,   257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(3170,    1049,    60459,   90,   385,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-2009,   1149,    60479,   270,  341,  0x0, 0,   2,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(8470,    1019,    62380,   0,    257,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-45650,  1019,    60169,   180,  257,  0x0, 0,   3,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(-48700,  1200,    60400,   270,  469,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-39810,  1029,    62639,   0,    385,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(7030,    150,     6969,    180,  341,  0x0, 0,   6,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(1539,    10000,   19700,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(50069,   1049,    62479,   0,    401,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(59099,   1549,    53029,   90,   469,  0x0, 0,   10,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(59099,   1549,    53029,   90,   503,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(58290,   1029,    62500,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(51930,   1049,    60970,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)

    DeclEvent(0x0000, 0, 24,  49.79999923706055,     51.150001525878906,    0.029999999329447746,  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -16.600000381469727,   -25.575000762939453,   -0.0060000005178153515, 1.0])

    DeclActor(0,       10000,   20600,   1000,    0,       11000,   20600,   0x007C, 0,  33, 0x0000)
    DeclActor(50350,   1050,    60430,   2000,    50350,   2000,    60430,   0x007C, 0,  34, 0x0000)
    DeclActor(58690,   1000,    52860,   3000,    58690,   2000,    52860,   0x007C, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_3B4",          # 00, 0
        "Function_1_46C",          # 01, 1
        "Function_2_497",          # 02, 2
        "Function_3_4C2",          # 03, 3
        "Function_4_4ED",          # 04, 4
        "Function_5_518",          # 05, 5
        "Function_6_543",          # 06, 6
        "Function_7_8B9",          # 07, 7
        "Function_8_B4F",          # 08, 8
        "Function_9_2C3B",         # 09, 9
        "Function_10_2DA8",        # 0A, 10
        "Function_11_4777",        # 0B, 11
        "Function_12_5AF7",        # 0C, 12
        "Function_13_7139",        # 0D, 13
        "Function_14_7312",        # 0E, 14
        "Function_15_73EE",        # 0F, 15
        "Function_16_782C",        # 10, 16
        "Function_17_892E",        # 11, 17
        "Function_18_8CBB",        # 12, 18
        "Function_19_8E6C",        # 13, 19
        "Function_20_9482",        # 14, 20
        "Function_21_9876",        # 15, 21
        "Function_22_9B8E",        # 16, 22
        "Function_23_9DD3",        # 17, 23
        "Function_24_A9B8",        # 18, 24
        "Function_25_AE2A",        # 19, 25
        "Function_26_BCBF",        # 1A, 26
        "Function_27_BD15",        # 1B, 27
        "Function_28_BD31",        # 1C, 28
        "Function_29_BD4D",        # 1D, 29
        "Function_30_E190",        # 1E, 30
        "Function_31_E1BD",        # 1F, 31
        "Function_32_E1E3",        # 20, 32
        "Function_33_E212",        # 21, 33
        "Function_34_E26A",        # 22, 34
        "Function_35_E4FD",        # 23, 35
        "Function_36_E6E4",        # 24, 36
    ))


    def Function_0_3B4(): pass

    label("Function_0_3B4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3F4"),
        (1, "loc_400"),
        (2, "loc_40C"),
        (3, "loc_418"),
        (4, "loc_424"),
        (5, "loc_430"),
        (6, "loc_43C"),
        (SWITCH_DEFAULT, "loc_448"),
    )


    label("loc_3F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_400")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_40C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_418")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_424")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_430")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_448")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_46B")

    Return()

    # Function_0_3B4 end

    def Function_1_46C(): pass

    label("Function_1_46C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_496")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_46C")

    label("loc_496")

    Return()

    # Function_1_46C end

    def Function_2_497(): pass

    label("Function_2_497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C1")
    OP_94(0xFE, 0x852, 0xF01E, 0x1036, 0xE830, 0x3E8)
    Sleep(300)
    Jump("Function_2_497")

    label("loc_4C1")

    Return()

    # Function_2_497 end

    def Function_3_4C2(): pass

    label("Function_3_4C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EC")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_3_4C2")

    label("loc_4EC")

    Return()

    # Function_3_4C2 end

    def Function_4_4ED(): pass

    label("Function_4_4ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517")
    OP_94(0xFE, 0xFFFF646A, 0xCA3A, 0xFFFF688E, 0xD386, 0x3E8)
    Sleep(300)
    Jump("Function_4_4ED")

    label("loc_517")

    Return()

    # Function_4_4ED end

    def Function_5_518(): pass

    label("Function_5_518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_542")
    OP_94(0xFE, 0xDEF8, 0xD82C, 0xEBE6, 0xE2A4, 0x3E8)
    Sleep(300)
    Jump("Function_5_518")

    label("loc_542")

    Return()

    # Function_5_518 end

    def Function_6_543(): pass

    label("Function_6_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_556")
    SetChrFlags(0xC, 0x80)
    Jump("loc_892")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_564")
    Jump("loc_892")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_577")
    SetChrFlags(0xB, 0x80)
    Jump("loc_892")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_596")
    SetChrPos(0xB, 11480, 1000, 54590, 0)
    Jump("loc_892")

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5CA")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59490, 700, 52910, 315)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_892")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5E7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_62B")
    SetChrPos(0x9, -990, 5000, 14750, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, 400, 5000, 14750, 270)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, 4720, 1000, 60520, 270)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_72F")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_68F")
    SetChrPos(0x8, 1420, 5000, 17800, 45)

    label("loc_68F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -46140, 1030, 59110, 0)
    SetChrPos(0xE, -45740, 1030, 60980, 180)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F6")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_6F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72A")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x12, 52530, 1050, 60070, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)

    label("loc_72A")

    Jump("loc_892")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_747")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_796")
    SetChrPos(0x8, -210, 5000, 12250, 180)
    BeginChrThread(0x8, 0, 0, 1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xF, -49990, 1200, 61760, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_892")

    label("loc_796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrPos(0x8, -210, 5000, 12250, 180)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 58830, 1000, 56350, 180)
    BeginChrThread(0x11, 0, 0, 5)
    Jump("loc_892")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_801")
    SetChrPos(0xC, -39220, 1000, 52790, 90)
    BeginChrThread(0xC, 0, 0, 4)
    Jump("loc_892")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_80F")
    Jump("loc_892")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_839")
    SetChrPos(0xB, 3570, 1000, 60560, 269)
    BeginChrThread(0xB, 0, 0, 2)
    SetChrFlags(0xA, 0x80)
    Jump("loc_892")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_84C")
    SetChrFlags(0xB, 0x80)
    Jump("loc_892")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_87B")
    SetChrPos(0xC, -49940, 1050, 63990, 0)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_892")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_889")
    Jump("loc_892")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_892")

    label("loc_892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_8A6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)
    Jump("loc_8B8")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_8B8")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x1, 3)
    Event(0, 29)

    label("loc_8B8")

    Return()

    # Function_6_543 end

    def Function_7_8B9(): pass

    label("Function_7_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8CE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_8CE")

    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x12, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_904")

    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_9AE")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_9AE")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_942")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_9AE")

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_950")
    Jump("loc_9AE")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_975")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_970")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)

    label("loc_970")

    Jump("loc_9AE")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_983")
    Jump("loc_9AE")

    label("loc_983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_99B")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_9AE")

    label("loc_99B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9AE")
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)

    label("loc_9AE")

    SetMapObjFrame(0xFF, "huku_nugippa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bed_event", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9EF")
    Jump("loc_A7A")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A34")
    SetMapObjFrame(0xFF, "bed_event", 0x1, 0x1)
    SetMapObjFrame(0xFF, "huku_nugippa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bed_normal", 0x0, 0x1)
    Jump("loc_A7A")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A42")
    Jump("loc_A7A")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A7A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")
    SetMapObjFrame(0xFF, "huku_nugippa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)

    label("loc_A7A")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA7")
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_AA7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF0")
    OP_1B(0x8, 0x0, 0x24)

    label("loc_AF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")
    OP_10(0x0, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x7, 0x0)
    OP_10(0x9, 0x1)
    Jump("loc_B1B")

    label("loc_B0F")

    OP_10(0x0, 0x1)
    OP_10(0x8, 0x0)
    OP_10(0x7, 0x1)
    OP_10(0x9, 0x0)

    label("loc_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B4E")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B4E")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B4E")

    label("loc_B4E")

    Return()

    # Function_7_8B9 end

    def Function_8_B4F(): pass

    label("Function_8_B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1199")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(
        0x101,
        (
            "#0001F(Okay, let's try to get some answers.)\x02\x03",
            "#0000FExcuse me, do you have a moment to talk?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE9")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked for clues about the stalker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "You're looking into a stalker? I usually\x01",
            "keep my eye out for anyone suspicious\x01",
            "when I'm working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FHave you spotted anyone like that\x01",
            "recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm here every day, but it's rare to ever\x01",
            "see someone snooping around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I DID catch a glimpse of someone the\x01",
            "other day, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw a young man covering his face with\x01",
            "a hat. He disappeared too quickly before\x01",
            "I was able to get a better look at him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIs there nothing more you can tell us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let me think about it for a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I can't say anything about\x01",
            "him seemed out of the ordinary.\x02",
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
        0xFE,
        (
            "His appearance was so unremarkable\x01",
            "that I can't recall anything about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FA total Average Joe, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThis doesn't appear to be in disagreement with\x01",
            "Rixia's statement, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B9")

    ChrTalk(
        0x101,
        (
            "#0000FAll right, I think that's enough for now.\x02\x03",
            "Let's reconvene in Ilya's room and sift through\x01",
            "the evidence we've managed to obtain thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou bet'cha. It's time to put our noggins to use!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_10B9")

    Jump("loc_1194")

    label("loc_10BE")


    ChrTalk(
        0xFE,
        (
            "I saw a young man covering his face with\x01",
            "a hat. I wasn't able to catch any details\x01",
            "of his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Other than that, nothing really stood\x01",
            "out about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "His features weren't striking enough to remember.\x02",
    )

    CloseMessageWindow()

    label("loc_1194")

    Jump("loc_2C37")

    label("loc_1199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125F")

    ChrTalk(
        0xFE,
        "It's time to do some work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm saving up all of my mira so I can watch\x01",
            "Ilya perform live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, I can score some tickets for next\x01",
            "month's performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E8")

    label("loc_125F")


    ChrTalk(
        0xFE,
        (
            "Separating the trash, cleaning the drainage\x01",
            "pipes... This is all to meet Ilya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can do this, just gotta push a little harder.\x02",
    )

    CloseMessageWindow()

    label("loc_12E8")

    Jump("loc_2C37")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1445")

    ChrTalk(
        0xFE,
        (
            "I recently saw the third floor resident for\x01",
            "the first time ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only managed to see her from behind, 'cause\x01",
            "she was on her way out. All I have to say is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...meh. She was completely normal. You'd be\x01",
            "able to find someone like her anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She had long blonde hair and seemed pretty, at least.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D7")

    label("loc_1445")


    ChrTalk(
        0xFE,
        (
            "That's the bare minimum if you're a\x01",
            "fashionable woman these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, she definitely seemed normal. I don't\x01",
            "know what I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D7")

    Jump("loc_2C37")

    label("loc_14DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AD")

    ChrTalk(
        0xFE,
        "Well, back to work I go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm saving up my money to go and see\x01",
            "Arc en Ciel live again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta pour my heart and soul into working,\x01",
            "so that I can make it a reality!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1604")

    label("loc_15AD")


    ChrTalk(
        0xFE,
        "Everything I do is to meet Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm workin' my butt off every day for this!\x02",
    )

    CloseMessageWindow()

    label("loc_1604")

    Jump("loc_2C37")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179A")

    ChrTalk(
        0xFE,
        (
            "Some kid's been visiting the tenant on\x01",
            "the third floor as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never met the person actually living there,\x01",
            "but I run into the kid once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was some pretty-looking girl wearing a cap.\x01",
            "I'd wager that she's 13 or 14 years old.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Hmm, now that I think about it... I feel like\x01",
            "I've seen that person somewhere before...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_185D")

    label("loc_179A")


    ChrTalk(
        0xFE,
        (
            "Hmm, now that I think about it... I feel like\x01",
            "I've seen that person somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. Don't think it'd be appropriate\x01",
            "for a lowly maid to pry into the tenants' lives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185D")

    Jump("loc_2C37")

    label("loc_1862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")

    ChrTalk(
        0xFE,
        "Whoaaaaaaaaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ilya was simply...stunning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, that 'Moon Princess' girl was just\x01",
            "as amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that she was a rookie, but I've\x01",
            "become a fan at first sight!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A35")

    label("loc_193D")


    ChrTalk(
        0xFE,
        (
            "But more importantly, I wonder where\x01",
            "Ilya lives...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd follow her to the ends of the earth if\x01",
            "I found her address!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A35")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005F(Is Ilya aware of this girl's existence...?)\x02",
    )

    CloseMessageWindow()

    label("loc_1A35")

    Jump("loc_2C37")

    label("loc_1A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A48")
    Jump("loc_2C37")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC8")

    ChrTalk(
        0xFE,
        (
            "They've been incorporating orbal cars\x01",
            "into recent parades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The world is becoming advanced.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B37")

    label("loc_1AC8")


    ChrTalk(
        0xFE,
        (
            "Back when I was a kid, our parades only\x01",
            "used festival carts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel like I've become old and cranky.\x02",
    )

    CloseMessageWindow()

    label("loc_1B37")

    Jump("loc_2C37")

    label("loc_1B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF7")

    ChrTalk(
        0xFE,
        "Most of the tenants are currently out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Not a problem. It just makes my job easier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I accidentally overheard some impressions\x01",
            "about the new play.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C8B")

    label("loc_1BF7")


    ChrTalk(
        0xFE,
        (
            "I'm going to go watch Arc en Ciel perform\x01",
            "their new play tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep your spoilers to yourself! I want to\x01",
            "enjoy the whole thing blind!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8B")

    Jump("loc_2C37")

    label("loc_1C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D83")

    ChrTalk(
        0xFE,
        (
            "People will be out enjoying the festivities,\x01",
            "but my custodial duties will carry on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm taking a vacation day for the last day of\x01",
            "the festival. Now I'll be able to watch Arc en\x01",
            "Ciel perform their new play.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DCD")

    label("loc_1D83")


    ChrTalk(
        0xFE,
        (
            "Anyway, it's cleaning time! Just a few more\x01",
            "days of enduring this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCD")

    Jump("loc_2C37")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0F")

    ChrTalk(
        0xFE,
        (
            "It's finally here. Arc en Ciel is starting to\x01",
            "perform their newest production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to score tickets for the last day of\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I'm avoiding anything and anyone\x01",
            "until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss me with those spoilers. I'm not\x01",
            "ruining this for myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F80")

    label("loc_1F0F")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Whoops, I better keep my trap shut! You\x01",
            "better not even THINK about spoiling it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F80")

    Jump("loc_2C37")

    label("loc_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D5")

    ChrTalk(
        0xFE,
        (
            "Oh, man, my heart is racing. It feels like\x01",
            "it's beating at a million beats a minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival is starting, and\x01",
            "that means that Ilya will be shining!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was able to watch Ilya perform live\x01",
            "last year... ㈱㈱㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, did you need any help? Sammie the\x01",
            "maid here can help you out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_216B")

    label("loc_20D5")


    ChrTalk(
        0xFE,
        (
            "I wonder if those people that went up\x01",
            "to the third floor are still there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never met the lady that lives there.\x01",
            "She's hardly ever home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216B")

    Jump("loc_2C37")

    label("loc_2170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2296")

    ChrTalk(
        0xFE,
        (
            "Some guests came to visit the third floor\x01",
            "tenant this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They give off a strange vibe, though. I got the\x01",
            "impression that they were important enough\x01",
            "for me to not approach them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kind of felt like they might have\x01",
            "been with the police department.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_233E")

    label("loc_2296")


    ChrTalk(
        0xFE,
        (
            "Y'know, I always did think the third\x01",
            "floor tenant was always a teensy bit\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's hardly ever home, and I still haven't\x01",
            "had the chance to meet her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233E")

    Jump("loc_2C37")

    label("loc_2343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_253C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2461")

    ChrTalk(
        0xFE,
        "The third floor resident isn't home yet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not much I can do about it. I'll have to wait\x01",
            "until tomorrow to enter the room and clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been assigned to clean their room once\x01",
            "a month. It's a free service provided by this\x01",
            "fancy apartment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2537")

    label("loc_2461")


    ChrTalk(
        0xFE,
        (
            "I hardly know anything about whoever's\x01",
            "living up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only thing that I can tell is that\x01",
            "she's a young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bit of a slob, at that. She always leaves\x01",
            "her underwear lying all over the place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2537")

    Jump("loc_2C37")

    label("loc_253C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2619")

    ChrTalk(
        0xFE,
        (
            "I managed to score tickets for next month's\x01",
            "Arc en Ciel performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But unfortunately, they're B section seats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sheesh, after I went through such\x01",
            "great lengths to get them, too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_266E")

    label("loc_2619")


    ChrTalk(
        0xFE,
        (
            "Can't complain, though. I'll be able to see\x01",
            "my beloved Ilya! I just can't wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266E")

    Jump("loc_2C37")

    label("loc_2673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26E9")

    ChrTalk(
        0xFE,
        "The third floor tenant left really early this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder who she is and what she does.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C37")

    label("loc_26E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2826")

    ChrTalk(
        0xFE,
        (
            "I'm picky when it comes to throwing out the\x01",
            "trash. Please take care when separating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a shame that city disposal only does\x01",
            "the bare minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get peeved when I see them lump the trash together,\x01",
            "especially after I take pains to organize it all. What a\x01",
            "bunch of jerks!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2891")

    label("loc_2826")


    ChrTalk(
        0xFE,
        "I'm picky when it comes to throwing out the trash.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys better separate your trash properly!\x02",
    )

    CloseMessageWindow()

    label("loc_2891")

    Jump("loc_2C37")

    label("loc_2896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298E")

    ChrTalk(
        0xFE,
        "Hey, have you guys heard the news?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets for Arc en Ciel's newest performance\x01",
            "will be going on sale soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, how long I've waited to gaze upon Ilya's\x01",
            "majestic figure... ㈱\x01",
            "I absolutely must get tickets!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A2C")

    label("loc_298E")


    ChrTalk(
        0xFE,
        (
            "Tickets for Arc en Ciel's newest performance\x01",
            "will be going on sale soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll wait in line all night if it means being able\x01",
            "to see my beloved Ilya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2C")

    Jump("loc_2C37")

    label("loc_2A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B25")

    ChrTalk(
        0xFE,
        "The third floor resident is never home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never seen her face. She leaves early\x01",
            "in the morning and returns late at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At least she has the decency to be a good tenant\x01",
            "by paying her rent on time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B77")

    label("loc_2B25")


    ChrTalk(
        0xFE,
        (
            "I still haven't managed to get a good look\x01",
            "at the third floor tenant's face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    Jump("loc_2C37")

    label("loc_2B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2C37")

    ChrTalk(
        0xFE,
        (
            "Well, good morning to you. It is I,\x01",
            "Sammie, the maid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you here to visit one of the tenants?\x01",
            "Levick lives on the first floor, and Kendall\x01",
            "lives on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C37")

    TalkEnd(0xFE)
    Return()

    # Function_8_B4F end

    def Function_9_2C3B(): pass

    label("Function_9_2C3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C4C")
    Jump("loc_2DA4")

    label("loc_2C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C5A")
    Jump("loc_2DA4")

    label("loc_2C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C68")
    Jump("loc_2DA4")

    label("loc_2C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C76")
    Jump("loc_2DA4")

    label("loc_2C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2C84")
    Jump("loc_2DA4")

    label("loc_2C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C92")
    Jump("loc_2DA4")

    label("loc_2C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D00")

    ChrTalk(
        0xFE,
        "It was truly a sight to behold...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've got nothing but praise for this year's parade.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA4")

    label("loc_2D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DA4")

    ChrTalk(
        0xFE,
        (
            "I managed to finish all of my work, so I'm going\x01",
            "to watch the parade with my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing wrong with enjoying a parade\x01",
            "celebrating my own city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA4")

    TalkEnd(0xFE)
    Return()

    # Function_9_2C3B end

    def Function_10_2DA8(): pass

    label("Function_10_2DA8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E3C")
    Jump("loc_2E86")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E5C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E86")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E7C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E86")

    label("loc_2E7C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E86")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3478")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F59")

    ChrTalk(
        0x101,
        (
            "#0001F(Okay, let's see if we can get any information.)\x02\x03",
            "#0000FExcuse me, sir, could I borrow a moment\x01",
            "of your time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F59")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked for clues about the stalker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "A stalker, eh? Yeah, I've heard\x01",
            "some rumors about 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm usually cooped up in my home, so I haven't\x01",
            "had the chance to see them. I have heard the\x01",
            "occasional weird noise, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can sometimes hear somebody rummaging\x01",
            "through the upstairs neighbor's belongings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last I knew, the third floor resident\x01",
            "is away at work during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDo you recall when you started hearing them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As soon as the Anniversary Festival started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, in the last two or three days, I'd say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(What could he have been doing inside\x01",
            "of Ilya's room?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(I'm not sure, but there doesn't appear to\x01",
            "be any evidence of property damage\x01",
            "or tampering with her belongings.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_337B")

    ChrTalk(
        0x101,
        (
            "#0000FAll right, I don't think we'll be able to get any\x01",
            "more information.\x02\x03",
            "Let's reconvene in Ilya's room and organize\x01",
            "the evidence we've obtained thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou bet'cha. It's time to put our noggins to use!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_337B")

    Jump("loc_3473")

    label("loc_3380")


    ChrTalk(
        0xFE,
        (
            "I've been hearing strange noises coming from the\x01",
            "upstairs neighbor's room the last two or three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible the upstairs tenant was home for\x01",
            "the Crossbell Anniversary Festival, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could that have been...the stalker?\x02",
    )

    CloseMessageWindow()

    label("loc_3473")

    Jump("loc_476F")

    label("loc_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E1")

    ChrTalk(
        0xFE,
        "Damn Crossbell politicians.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Those utter disgraces are indefensible!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3523")

    label("loc_34E1")


    ChrTalk(
        0xFE,
        (
            "They should fire all of the incompetent\x01",
            "jackasses in office!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3523")

    Jump("loc_476F")

    label("loc_3528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B3")

    ChrTalk(
        0xFE,
        "The design is too elaborate? Nonsense!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They don't know the first damn thing about\x01",
            "artistic integrity!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35D3")

    label("loc_35B3")


    ChrTalk(
        0xFE,
        "Damn the Imperial Faction!\x02",
    )

    CloseMessageWindow()

    label("loc_35D3")

    Jump("loc_476F")

    label("loc_35D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_376A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D4")

    ChrTalk(
        0xFE,
        (
            "The budget for constructing the new\x01",
            "City Hall building is currently frozen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our politicians are in disagreements\x01",
            "over the materials to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really hope they resume construction within\x01",
            "this fiscal year...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3765")

    label("loc_36D4")


    ChrTalk(
        0xFE,
        (
            "I'm involved with the development of the new\x01",
            "City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm feeling nervous over today's diet regarding\x01",
            "the building's construction...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3765")

    Jump("loc_476F")

    label("loc_376A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_389C")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EC")

    ChrTalk(
        0xFE,
        "Finish the building by the mayoral election?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are my ears deceiving me?\x01",
            "Is my client mad?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3897")

    label("loc_37EC")


    ChrTalk(
        0xFE,
        (
            "Oh, sure, the timing would be excellent.\x01",
            "Except, the election is NEXT month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to raise some hell. This is going to be\x01",
            "literally impossible to pull off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3897")

    Jump("loc_476F")

    label("loc_389C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_39F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3975")

    ChrTalk(
        0xFE,
        (
            "The job requests have been pouring in\x01",
            "because of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm happy that people are using my building\x01",
            "designs, but I've become so overworked\x01",
            "that it's unbearable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39EC")

    label("loc_3975")


    ChrTalk(
        0xFE,
        "I'll never compromise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel sorry about it, but I'll have to turn away\x01",
            "the last few requests that came in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39EC")

    Jump("loc_476F")

    label("loc_39F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ABC")

    ChrTalk(
        0xFE,
        "Whoa, excuse me there. You're in the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to wrap up any remaining work\x01",
            "by the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be free by the evening\x01",
            "if I work at full force.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B14")

    label("loc_3ABC")


    ChrTalk(
        0xFE,
        (
            "I'll finish up my work and spend the rest of\x01",
            "my evening hanging out with the wife.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B14")

    Jump("loc_476F")

    label("loc_3B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B99")

    ChrTalk(
        0xFE,
        "Oh, did you need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time to deal with you, I'm\x01",
            "overwhelmed by design work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_3B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BA7")
    Jump("loc_476F")

    label("loc_3BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3BB5")
    Jump("loc_476F")

    label("loc_3BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C39")

    ChrTalk(
        0xFE,
        "I've got a huge pile of work to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel bad for my wife, but I'm not going\x01",
            "to leave any work unfinished.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_3C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C91")

    ChrTalk(
        0xFE,
        "Ugh, it's too noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't concentrate because of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_3C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3D23")

    ChrTalk(
        0xFE,
        (
            "Okay! Just one more push, and that's another\x01",
            "completed design.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta get this one to the client as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_3D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3E15")

    ChrTalk(
        0xFE,
        (
            "Both my father and grandfather were\x01",
            "famous architects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandfather actually designed\x01",
            "Crossbell City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, that thing has been around for\x01",
            "almost sixty years now... Gives me\x01",
            "goosebumps thinking about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_3E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED9")

    ChrTalk(
        0xFE,
        "I heard that Revache engages in land sharking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They forcibly evict the residents, and illegally\x01",
            "seize the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're a bunch of heinous savages.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F58")

    label("loc_3ED9")


    ChrTalk(
        0xFE,
        "I heard that Revache engages in land sharking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't we get some police intervention? How\x01",
            "can they let this go on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F58")

    Jump("loc_476F")

    label("loc_3F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_411B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407D")

    ChrTalk(
        0xFE,
        (
            "Construction has picked up to a rapid pace in\x01",
            "preparation for next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next month is Crossbell's 70th year anniversary,\x01",
            "so eyes from all nations will be on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyone who owns property is going to be\x01",
            "trying their hardest to impress during it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4116")

    label("loc_407D")


    ChrTalk(
        0xFE,
        (
            "Many of the buildings are set to have their\x01",
            "construction completed by next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's an opportunity to amass an immense\x01",
            "amount of wealth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4116")

    Jump("loc_476F")

    label("loc_411B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4129")
    Jump("loc_476F")

    label("loc_4129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_42FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4263")

    ChrTalk(
        0xFE,
        (
            "Hey, did you know that they opened up a\x01",
            "theme park at Mishelam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC financed and developed the whole\x01",
            "thing themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that they've pulled out all the stops by\x01",
            "using all the latest technology to build the thing...\x01",
            "I'd like to see it for myself at least once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42F8")

    label("loc_4263")


    ChrTalk(
        0xFE,
        (
            "I've visited some of the hotels I've designed,\x01",
            "but I've never gone to a theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm...it'd be pretty interesting to see how\x01",
            "they work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F8")

    Jump("loc_476F")

    label("loc_42FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_43BA")

    ChrTalk(
        0xFE,
        (
            "*sigh* I was struggling so much with a design\x01",
            "that I ended up pulling an all-nighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm confident it paid off. The client should be\x01",
            "pleased at tomorrow's meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476F")

    label("loc_43BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4587")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4516")

    ChrTalk(
        0xFE,
        (
            "They've been nothing but a thorn in my side!\x01",
            "I drafted up blueprints, and they outright\x01",
            "ignored the whole thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weren't you the ones who ordered the design\x01",
            "of the new City Hall building?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll object their every move. They changed\x01",
            "the design as they pleased. How do they\x01",
            "expect me to approve this?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4582")

    label("loc_4516")


    ChrTalk(
        0xFE,
        (
            "How in the HELL is that supposed to be an\x01",
            "'improved' blueprint?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's idiotic. Absolutely idiotic!\x02",
    )

    CloseMessageWindow()

    label("loc_4582")

    Jump("loc_476F")

    label("loc_4587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_476F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D0")

    ChrTalk(
        0xFE,
        (
            "The new City Hall design is poised to be\x01",
            "a 40-story skyscraper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The whole thing is unprecedented and contains\x01",
            "a plethora of original concepts. Truly a building\x01",
            "for the ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been working on designing the exterior\x01",
            "and the office spaces. I cannot wait for\x01",
            "this behemoth's completion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_476F")

    label("loc_46D0")


    ChrTalk(
        0xFE,
        (
            "The new City Hall design is poised to be a forty-\x01",
            "story skyscraper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Designing it was a leviathan of a task, so\x01",
            "I cannot wait for it to be completed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2DA8 end

    def Function_11_4777(): pass

    label("Function_11_4777")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482D")

    ChrTalk(
        0x101,
        (
            "#0001F(Okay, let's try and get some answers.)\x02\x03",
            "#0000FSorry to bother you, do you have a moment\x01",
            "to answer some questions?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_482D")

    SetScenarioFlags(0x1, 2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked for clues about the stalker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Huh, there's a stalker? That's frightening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't say I've seen him, though.\x01",
            "Perhaps I've missed him while shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FDo you usually shop during the\x01",
            "middle of the day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right. I have a pretty consistent\x01",
            "routine and always leave at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(Our stalker is striking when most\x01",
            "people are out of the house.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Yeah. He's avoiding the busiest\x01",
            "hours inside the building.)\x02\x03",
            "(We've got a crafty one on our hands.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B68")

    ChrTalk(
        0x101,
        (
            "#0000FAll right, I don't think we'll be able to get any\x01",
            "more information.\x02\x03",
            "Let's reconvene in Ilya's room and organize\x01",
            "the evidence we've obtained thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou bet'cha. It's time to put our noggins to use!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_4B68")

    Jump("loc_4BD8")

    label("loc_4B6D")


    ChrTalk(
        0xFE,
        "Huh, there's a stalker? That's frightening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't seen them when I go out to do\x01",
            "my shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD8")

    Jump("loc_5AF3")

    label("loc_4BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4C3D")

    ChrTalk(
        0xFE,
        "I'll pour my husband black tea today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hopefully, it'll calm his nerves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_4C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2B")

    ChrTalk(
        0xFE,
        (
            "They still haven't managed to reopen the\x01",
            "budget for the new City Hall building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The members of the diet complained about\x01",
            "wasteful spending during the Q&A period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My husband is absolutely furious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D7F")

    label("loc_4D2B")


    ChrTalk(
        0xFE,
        (
            "This is a problem. My husband refuses to\x01",
            "compromise when it comes to his work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D7F")

    Jump("loc_5AF3")

    label("loc_4D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D92")
    Jump("loc_5AF3")

    label("loc_4D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4E13")

    ChrTalk(
        0xFE,
        (
            "My husband has been getting a lot of\x01",
            "work requests recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even sorting the documents looks difficult.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_4E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB8")

    ChrTalk(
        0xFE,
        (
            "My husband has been bogged down with\x01",
            "work lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel sad. He doesn't have\x01",
            "the time nor energy to talk to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4F30")

    label("loc_4EB8")


    ChrTalk(
        0xFE,
        "No, I shouldn't act so selfishly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll brew him some nice, warm tea. That'll\x01",
            "help him progress with his work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F30")

    Jump("loc_5AF3")

    label("loc_4F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FC0")

    ChrTalk(
        0xFE,
        (
            "I intend to make an extraordinary feast\x01",
            "for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to put my heart and soul\x01",
            "into preparing this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_4FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_50A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502D")

    ChrTalk(
        0xFE,
        "A little boy, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry, I have no clue what you're talking about.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_509D")

    label("loc_502D")


    ChrTalk(
        0xFE,
        "Yes, we were at the parade, however...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have any useful information for you.\x01",
            "Sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_509D")

    Jump("loc_5AF3")

    label("loc_50A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_50FF")

    ChrTalk(
        0xFE,
        "This year's parade was a ton of fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I made a lot of great memories.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_50FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_51BC")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xB, 0x9, 0)

    ChrTalk(
        0x9,
        "*cough* Well, then, shall we head out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I won't be able to talk about the parade with\x01",
            "my clients if we end up missing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha... Okay, let's go.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_5AF3")

    label("loc_51BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5237")

    ChrTalk(
        0xFE,
        "My husband is a workaholic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't mind it too much, but I wish he'd take\x01",
            "better care of himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_5237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5290")

    ChrTalk(
        0xFE,
        "Welcome to Kendall's Architectural Firm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come on in. We're open.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_5290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_529E")
    Jump("loc_5AF3")

    label("loc_529E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53AB")

    ChrTalk(
        0xFE,
        (
            "One of his regular clients is the company\x01",
            "that constructed the IBC building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The foreman and my husband are friends, so\x01",
            "he likes to come here often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried for his health, though. They throw\x01",
            "far too many drinking parties.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_542B")

    label("loc_53AB")


    ChrTalk(
        0xFE,
        (
            "Construction companies tend to hold far too\x01",
            "many drinking parties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish he paid a bit more attention to his health.\x02",
    )

    CloseMessageWindow()

    label("loc_542B")

    Jump("loc_5AF3")

    label("loc_5430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_54C4")

    ChrTalk(
        0xFE,
        (
            "I'm planning on cooking my husband's favorite\x01",
            "dish today: delicious beef stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to start preparing the\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_54C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5580")

    ChrTalk(
        0xFE,
        (
            "Ilya is exceedingly popular. Must be because\x01",
            "she's the star of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know everything about her, since Sammie\x01",
            "spends every waking moment talking\x01",
            "about her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF3")

    label("loc_5580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_56E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5688")

    ChrTalk(
        0xFE,
        (
            "I've got to get the cleaning done while my\x01",
            "husband isn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm...he's probably dining in Central Square\x01",
            "over a business meeting right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is he hard to please, but he's also\x01",
            "never around due to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_56E3")

    label("loc_5688")


    ChrTalk(
        0xFE,
        (
            "Well, if you'll excuse me. I've got some cleaning\x01",
            "to do while the demon isn't around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56E3")

    Jump("loc_5AF3")

    label("loc_56E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_56F6")
    Jump("loc_5AF3")

    label("loc_56F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F8")

    ChrTalk(
        0xFE,
        (
            "That husband of mine pulled yet another\x01",
            "all-nighter. He always does this when he\x01",
            "has to design a building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, what a worrisome man he is. I've got\x01",
            "nothing to do, so I think I'll pour him a nice,\x01",
            "warm cup of black tea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5854")

    label("loc_57F8")


    ChrTalk(
        0xFE,
        (
            "My husband loves his black tea. He always\x01",
            "demands it the morning after an all-nighter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5854")

    Jump("loc_5AF3")

    label("loc_5859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_59A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_592F")

    ChrTalk(
        0xFE,
        (
            "My husband gets tunnel vision\x01",
            "when it comes to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't take any offense if he suddenly screams\x01",
            "out in frustration. He doesn't mean any harm.\x01",
            "He's just absorbed in his work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_599D")

    label("loc_592F")


    ChrTalk(
        0xFE,
        (
            "My husband gets tunnel vision when\x01",
            "it comes to work. He doesn't mean harm,\x01",
            "so please don't take offense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_599D")

    Jump("loc_5AF3")

    label("loc_59A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5AF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, sorry about that! I was busy cooking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome to Kendall's Architectural Firm.\x01",
            "Please direct any inquiries to my husband.\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He appears to be free at the moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5AF3")

    label("loc_5A8F")


    ChrTalk(
        0xFE,
        (
            "Welcome to Kendall's Architectural Firm.\x01",
            "Please direct any inquiries to my husband.\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AF3")

    TalkEnd(0xFE)
    Return()

    # Function_11_4777 end

    def Function_12_5AF7(): pass

    label("Function_12_5AF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6328")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6286")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xC,
        (
            "Oh, for Aidios' sake! I'd like to eat my\x01",
            "food outside at noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't do much about it. I already\x01",
            "prepared it earlier this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Constantly bickering won't fix it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Did we just walk into the middle of a storm?)\x02\x03",
            "#0000FE-Excuse us, do you have a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xC, 0x0, 400)
    TurnDirection(0xE, 0x0, 400)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked for clues about the stalker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0xC,
        "Geez, a stalker?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That sounds like a problem to me.\x01",
            "Have you tried consulting the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Wouldn't it be better to contact the Bracer Guild?\x01",
            "Our police force acts far too slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI...take it you don't have any information?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, that's the gist of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I spend most of my time relaxing on the sofa\x01",
            "out in the entrance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't say I've ever spotted any suspicious\x01",
            "people. Are you sure you aren't just\x01",
            "imagining it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA1")
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
        0x104,
        "#0305F(Hold on, what'd she just say?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(She didn't see him come in from the\x01",
            "main entrance...)\x02\x03",
            "(Does that mean what I think it means?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6152")

    label("loc_5FA1")

    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#0305FI think I figured it out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(If he wasn't spotted coming through the front\x01",
            "entrance, then that can only mean one thing.)\x02\x03",
            "(He may be using an alternative entrance,\x01",
            "just as we theorized.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(The probability of him using the back entrance\x01",
            "is fairly high.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(All right, I think it's time we begin devising\x01",
            "a strategy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_6152")

    OP_29(0x1D, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_626F")

    ChrTalk(
        0x101,
        (
            "#0000FAll right, I don't think we'll be able to get any\x01",
            "more information.\x02\x03",
            "Let's reconvene in Ilya's room and organize\x01",
            "the evidence we've obtained thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou bet'cha. It's time to put our noggins to use!\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x1D, 0x1, 0x9)

    label("loc_626F")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_6323")

    label("loc_6286")


    ChrTalk(
        0xFE,
        "Hoho, a stalker sounds like a problem to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You should try consulting the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(This guy's blissfully unaware of his surroundings.)\x02",
    )

    CloseMessageWindow()

    label("loc_6323")

    Jump("loc_7135")

    label("loc_6328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6336")
    Jump("loc_7135")

    label("loc_6336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6421")

    ChrTalk(
        0xFE,
        (
            "I found something that'd make a good gift\x01",
            "at the antique shop in the Back Alley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pretty good timing, considering my wedding\x01",
            "anniversary was coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it put the old lady in a\x01",
            "good mood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6463")

    label("loc_6421")


    ChrTalk(
        0xFE,
        (
            "My wife's a bit of a battle axe, so it's hard\x01",
            "to please her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6463")

    Jump("loc_7135")

    label("loc_6468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_65E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A7")

    ChrTalk(
        0xFE,
        (
            "I'm able to live a nice, peaceful life thanks to\x01",
            "the time I put into being a politician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been blessed with the gift of a politician's\x01",
            "pension to retire on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the old lady is a bit of a tough nut\x01",
            "to crack. The last gift I gave her didn't elicit\x01",
            "any sort of response.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_65E1")

    label("loc_65A7")


    ChrTalk(
        0xFE,
        (
            "Her inability to cooperate is frustrating,\x01",
            "honestly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E1")

    Jump("loc_7135")

    label("loc_65E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_66EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66AC")

    ChrTalk(
        0xFE,
        (
            "My wife wants me to stop messing around\x01",
            "with our house's interior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, you know what? She's lazy, so I've\x01",
            "been doing it in her stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's a selfish gal.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_66E7")

    label("loc_66AC")


    ChrTalk(
        0xFE,
        (
            "Hah. Not only is she selfish, but she's\x01",
            "also unkempt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E7")

    Jump("loc_7135")

    label("loc_66EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6781")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        "Oh, dear, aren't you a lovely little lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you just move here, darling?\x01",
            "I hope you enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6812")

    label("loc_6781")


    ChrTalk(
        0xFE,
        (
            "I rearranged the interior of our house\x01",
            "the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I decorated it with bright colors to match\x01",
            "the Anniversary Festival's aesthetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6812")

    Jump("loc_7135")

    label("loc_6817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6825")
    Jump("loc_7135")

    label("loc_6825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6833")
    Jump("loc_7135")

    label("loc_6833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6841")
    Jump("loc_7135")

    label("loc_6841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_684F")
    Jump("loc_7135")

    label("loc_684F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_685D")
    Jump("loc_7135")

    label("loc_685D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_686B")
    Jump("loc_7135")

    label("loc_686B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6947")

    ChrTalk(
        0xFE,
        (
            "I'm finished organizing the room, so I'll\x01",
            "reward myself with a bit of black tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'm the only one around here who\x01",
            "has a sense of purpose. My wife wastes the\x01",
            "day away with her hobbies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7135")

    label("loc_6947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_69E1")

    ChrTalk(
        0xFE,
        (
            "I tried to clean the closet up a bit, but a\x01",
            "bunch of stuff ended up falling out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I've got a long road ahead of me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7135")

    label("loc_69E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAD")

    ChrTalk(
        0xFE,
        (
            "I appreciate how everyone is feeling more festive\x01",
            "as the Anniversary Festival approaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't sit still. I need to do...stuff! I think\x01",
            "the carpet needs replacing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B3C")

    label("loc_6AAD")


    ChrTalk(
        0xFE,
        (
            "It's important to be in a good mood when\x01",
            "the Anniversary Festival approaches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might be a good idea to tidy the room up\x01",
            "a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B3C")

    Jump("loc_7135")

    label("loc_6B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C4A")

    ChrTalk(
        0xFE,
        (
            "I noticed our portable stove was rusted while\x01",
            "I was rearranging some of our furniture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ended up buying a new portable stove with\x01",
            "identical measurements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad I was able to find something that\x01",
            "was just the right size.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CED")

    label("loc_6C4A")


    ChrTalk(
        0xFE,
        (
            "According to the clerk, this bad boy's a\x01",
            "newer model with double the power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of the problems I was concerned about\x01",
            "have vanished into thin air. Phew!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CED")

    Jump("loc_7135")

    label("loc_6CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DAB")

    ChrTalk(
        0xFE,
        (
            "Wait a sec...this table isn't aligned with\x01",
            "the center of the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no, no, no. This won't do at all.\x01",
            "I've gotta go and retake the measurements.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6DEC")

    label("loc_6DAB")


    ChrTalk(
        0xFE,
        (
            "The table's position was bothering me,\x01",
            "so I moved it a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DEC")

    Jump("loc_7135")

    label("loc_6DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7C")

    ChrTalk(
        0xFE,
        "What a nice, clear morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only the diet session in a few months\x01",
            "would turn out just as peaceful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F03")

    label("loc_6E7C")


    ChrTalk(
        0xFE,
        "Well, I suppose I should get to watering the plants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My wife's really lazy when it comes to\x01",
            "housework. Someone has to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F03")

    Jump("loc_7135")

    label("loc_6F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_703E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FBE")

    ChrTalk(
        0xFE,
        (
            "My wife spends her entire day working\x01",
            "on handicrafts, completely forgoing all\x01",
            "of the housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That wife of mine... Her behavior is\x01",
            "despicable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7039")

    label("loc_6FBE")


    ChrTalk(
        0xFE,
        (
            "All she does is indulge in her own hobbies.\x01",
            "Can't she ever help out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's always been an utterly selfish woman.\x02",
    )

    CloseMessageWindow()

    label("loc_7039")

    Jump("loc_7135")

    label("loc_703E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D8")

    ChrTalk(
        0xFE,
        (
            "I felt like changing the atmosphere of the\x01",
            "place, so I bought some fancy furniture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This layout should do the trick.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7135")

    label("loc_70D8")


    ChrTalk(
        0xFE,
        "I'm in the process of redecorating our home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Would any of you like some black tea?\x02",
    )

    CloseMessageWindow()

    label("loc_7135")

    TalkEnd(0xFE)
    Return()

    # Function_12_5AF7 end

    def Function_13_7139(): pass

    label("Function_13_7139")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_71CD")
    Jump("loc_7217")

    label("loc_71CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7217")

    label("loc_71ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_720D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7217")

    label("loc_720D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7217")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_730A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7257")
    Call(0, 14)
    Jump("loc_730A")

    label("loc_7257")


    ChrTalk(
        0xFE,
        (
            "Need I remind her that my pension is\x01",
            "the only reason she can maintain\x01",
            "her comfortable lifestyle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, she hasn't forgotten about that\x01",
            "teensy little detail, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_730A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_7139 end

    def Function_14_7312(): pass

    label("Function_14_7312")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xF,
        (
            "Dear, you do know how to\x01",
            "make black tea, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't you just soak some tea leaves in\x01",
            "hot water? I'm pretty sure I did it right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Awful. Just awful.\x01",
            "This is completely undrinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_14_7312 end

    def Function_15_73EE(): pass

    label("Function_15_73EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7659")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7420")
    Call(0, 12)
    Return()

    label("loc_7420")


    ChrTalk(
        0xFE,
        (
            "I spend most of my time relaxing on the sofa\x01",
            "out in the entrance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't say I've ever spotted any suspicious\x01",
            "people. Are you sure you aren't just\x01",
            "imagining it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7654")

    ChrTalk(
        0x104,
        "#0303F(Looks like we've figured it out.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(If he wasn't spotted coming through the front\x01",
            "entrance, then that can only mean one thing.)\x02\x03",
            "(He may be using an alternative entrance,\x01",
            "just as we theorized.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(The probability of him using the back entrance\x01",
            "is fairly high.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(All right, I think it's time we begin devising\x01",
            "a strategy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 4)

    label("loc_7654")

    Jump("loc_7828")

    label("loc_7659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_776F")

    ChrTalk(
        0xFE,
        (
            "My husband was a member of the diet until\x01",
            "about five years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was an opportunist to the core. All\x01",
            "he ever did was sit there and listen\x01",
            "to what the others were saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at least he has his pension. That's\x01",
            "something, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_780C")

    label("loc_776F")


    ChrTalk(
        0xFE,
        (
            "My husband was just a petty politician. His pension\x01",
            "was the only significant part of his career.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess I can give him praise for that, at least.\x02",
    )

    CloseMessageWindow()

    label("loc_780C")

    Jump("loc_7828")

    label("loc_7811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_781F")
    Jump("loc_7828")

    label("loc_781F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7828")

    label("loc_7828")

    TalkEnd(0xFE)
    Return()

    # Function_15_73EE end

    def Function_16_782C(): pass

    label("Function_16_782C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78C0")
    Jump("loc_790A")

    label("loc_78C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_78E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_790A")

    label("loc_78E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7900")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_790A")

    label("loc_7900")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_790A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79FA")

    ChrTalk(
        0xFE,
        (
            "That damned husband of mine went off\x01",
            "and bought an orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He didn't bother to ask me! That selfish oaf...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm utterly shocked! How dare he act\x01",
            "so selfishly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7A49")

    label("loc_79FA")


    ChrTalk(
        0xFE,
        (
            "I'm so shocked at my husband's reckless\x01",
            "spending that I can't even speak!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A49")

    Jump("loc_8926")

    label("loc_7A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B10")

    ChrTalk(
        0xFE,
        (
            "My husband gave me a pendant for our\x01",
            "wedding anniversary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I suppose that even he has a good side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mean, it was my choice to marry him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7B81")

    label("loc_7B10")


    ChrTalk(
        0xFE,
        "He was a fine young man back in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He occasionally shows a small\x01",
            "trace of the man he used to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B81")

    Jump("loc_8926")

    label("loc_7B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C34")

    ChrTalk(
        0xFE,
        (
            "That husband of mine is planning to make\x01",
            "another large purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* What's it going to be this time?\x01",
            "Maybe a chandelier? Who knows?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7C78")

    label("loc_7C34")


    ChrTalk(
        0xFE,
        (
            "His habit of constantly redecorating the house\x01",
            "is frustrating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C78")

    Jump("loc_8926")

    label("loc_7C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D78")

    ChrTalk(
        0xFE,
        "The diet seems to be dragging on, yet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No surprises there. It was the same when\x01",
            "my husband was a member of the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They do nothing but cause problems. They've\x01",
            "got nothing but self-centered intentions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7DD6")

    label("loc_7D78")


    ChrTalk(
        0xFE,
        (
            "I am absolutely positive that my husband's\x01",
            "negative traits are all thanks to his career.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD6")

    Jump("loc_8926")

    label("loc_7DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC2")

    ChrTalk(
        0xFE,
        (
            "Handicrafts are adored amongst the elites\x01",
            "of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell's wife was adept at\x01",
            "handicrafting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would go as far as to say that her skills\x01",
            "influenced me to start it for myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7F35")

    label("loc_7EC2")


    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell's wife was adept at\x01",
            "handicrafting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's unfortunate, but she passed away\x01",
            "many years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F35")

    Jump("loc_8926")

    label("loc_7F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7F48")
    Jump("loc_8926")

    label("loc_7F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7F56")
    Jump("loc_8926")

    label("loc_7F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7F64")
    Jump("loc_8926")

    label("loc_7F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7F72")
    Jump("loc_8926")

    label("loc_7F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7F80")
    Jump("loc_8926")

    label("loc_7F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9B")
    Call(0, 14)
    Jump("loc_8023")

    label("loc_7F9B")


    ChrTalk(
        0xFE,
        (
            "This man can't even prepare a pot of\x01",
            "black tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can't keep up with the housework\x01",
            "at all, either. Just what is he good for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8023")

    Jump("loc_8926")

    label("loc_8028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_81A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_810E")

    ChrTalk(
        0xFE,
        (
            "Some men have been visiting the apartment\x01",
            "since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They marched up to the third floor residence\x01",
            "in complete silence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They had an air of importance...\x01",
            "I wonder what they wanted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_819E")

    label("loc_810E")


    ChrTalk(
        0xFE,
        (
            "They looked like they were all business.\x01",
            "I don't think they came here to have a\x01",
            "leisurely chat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't help but wonder who they are.\x02",
    )

    CloseMessageWindow()

    label("loc_819E")

    Jump("loc_8926")

    label("loc_81A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82B9")

    ChrTalk(
        0xFE,
        (
            "That husband of mine... I wish he'd stop\x01",
            "doing such unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's Sammie's job to clean the place up, so\x01",
            "you think you'd be able to leave it to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can't clean to save his life. He'll\x01",
            "end up creating an even bigger mess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8314")

    label("loc_82B9")


    ChrTalk(
        0xFE,
        (
            "I'm absolutely floored by his inability to\x01",
            "sit still and not do anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8314")

    Jump("loc_8926")

    label("loc_8319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83F2")

    ChrTalk(
        0xFE,
        (
            "As per tradition, I create a coaster for the\x01",
            "Anniversary Festival every year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've been doing it for twenty years now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm grateful that I'm able to continue doing\x01",
            "what I do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8473")

    label("loc_83F2")


    ChrTalk(
        0xFE,
        (
            "This year is Crossbell's 70th anniversary\x01",
            "as a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get wistful thinking about how it ages\x01",
            "with each passing year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8473")

    Jump("loc_8926")

    label("loc_8478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_852A")

    ChrTalk(
        0xFE,
        (
            "My husband bought a new portable orbal\x01",
            "stove the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He went and secretly spent a ton of money, again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Doesn't he have anything better to do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8926")

    label("loc_852A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_85F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85BF")

    ChrTalk(
        0xFE,
        (
            "Oh, for Aidios' sake! My husband's\x01",
            "bad habits have resurfaced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh... How am I even supposed to cook\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_85F1")

    label("loc_85BF")


    ChrTalk(
        0xFE,
        "*sigh* Looks like we'll be eating out again.\x02",
    )

    CloseMessageWindow()

    label("loc_85F1")

    Jump("loc_8926")

    label("loc_85F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8604")
    Jump("loc_8926")

    label("loc_8604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_87B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8735")

    ChrTalk(
        0xFE,
        (
            "This apartment complex has a free cleaning service.\x01",
            "All you have to do is ask the maid to do it, and she'll\x01",
            "do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I usually ask Sammie to take care of\x01",
            "the cleaning for our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all thanks to her help that I'm able\x01",
            "to invest more time into my hobbies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_87B0")

    label("loc_8735")


    ChrTalk(
        0xFE,
        (
            "They've even recently introduced a delivery\x01",
            "service for grocery shopping. Living life\x01",
            "has never been more convenient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B0")

    Jump("loc_8926")

    label("loc_87B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_889D")

    ChrTalk(
        0xFE,
        (
            "My husband has, yet again, decided to\x01",
            "redecorate our apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I up and leave the place whenever he does it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't stand it. How am I supposed to enjoy\x01",
            "quietly working on my handicrafts?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8926")

    label("loc_889D")


    ChrTalk(
        0xFE,
        (
            "I can't entirely blame him, though. He has too\x01",
            "much time on his hands, now that he's retired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Expensive hobbies stress me out.\x02",
    )

    CloseMessageWindow()

    label("loc_8926")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_782C end

    def Function_17_892E(): pass

    label("Function_17_892E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B04")

    ChrTalk(
        0xFE,
        "Huh? Are you the ones Dudley mentioned?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave immediately. You're getting\x01",
            "in the way of our guard duty.\x02",
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
        "#0005FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is Ilya Platiere's penthouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of the First Division have been entrusted\x01",
            "with the task of guarding her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(Damn, those First Division guys\x01",
            "move quickly.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(Th-They certainly live up to their reputation.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 1)
    Jump("loc_8CB7")

    label("loc_8B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8B12")
    Jump("loc_8CB7")

    label("loc_8B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8BB6")

    ChrTalk(
        0xFE,
        (
            "We of the First Division have been entrusted\x01",
            "with guarding Ilya Platiere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "See to it that you don't get in our way,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB7")

    label("loc_8BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8CB7")

    ChrTalk(
        0xFE,
        (
            "Judging by the contents of the letter, I'd\x01",
            "say there's a good possibility that she'll\x01",
            "be targeted while she's up on stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That being said, we can't ignore that other\x01",
            "opportunities may exist, so she'll be under\x01",
            "our constant surveillance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB7")

    TalkEnd(0xFE)
    Return()

    # Function_17_892E end

    def Function_18_8CBB(): pass

    label("Function_18_8CBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8CCC")
    Jump("loc_8E68")

    label("loc_8CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8D74")

    ChrTalk(
        0xFE,
        (
            "Hmm. There's also the possibility that somebody\x01",
            "could snipe her from the outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to investigate the perimeter before\x01",
            "Ilya returns.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E68")

    label("loc_8D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF4")

    ChrTalk(
        0xFE,
        "I wasn't able to find any wiretaps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that the coast is clear, for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8E68")

    label("loc_8DF4")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "You must be the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. Leave Ilya's protection to the\x01",
            "more qualified team.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E68")

    TalkEnd(0xFE)
    Return()

    # Function_18_8CBB end

    def Function_19_8E6C(): pass

    label("Function_19_8E6C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_92A3")
    OP_64(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_8F62")

    ChrTalk(
        0x12,
        (
            "*snore*...*snore*...\x02\x03",
            "Zzzz... Zzzz...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FShe may be super pretty, but she\x01",
            "sure snores a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(We should probably get out of here...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F5D")

    ChrTalk(
        0x104,
        "#0309F(RANDY ORLANDO, YOU LUCKY DOG!)\x02",
    )

    CloseMessageWindow()

    label("loc_8F5D")

    Jump("loc_928C")

    label("loc_8F62")


    ChrTalk(
        0x12,
        "*snore*...*snore*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x153)

    ChrTalk(
        0x153,
        "#1110FI mean, wow! She's REALLY loud!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_904F")

    ChrTalk(
        0x101,
        (
            "#0006FNot to mention, her apartment is an\x01",
            "absolute mess, as per usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908D")

    label("loc_904F")


    ChrTalk(
        0x101,
        (
            "#0006FNot to mention, her apartment is an\x01",
            "absolute mess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9107")

    ChrTalk(
        0x102,
        (
            "#0100FIt's hard to believe that this snoring woman and\x01",
            "the Fervent Dancer are one and the same.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9286")

    label("loc_9107")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9151")

    ChrTalk(
        0x103,
        "#0200FShe always slightly resembles an old man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9286")

    label("loc_9151")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9286")

    ChrTalk(
        0x104,
        (
            "#0304FThat just goes to show how unequal\x01",
            "Ilya Platiere is in her craft!\x02\x03",
            "#0309FStill can't believe I got to see her sleeping\x01",
            "face! Man, Aidios sure loves me today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1111FHuh? What's Randy talking about, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYou don't need to understand, KeA.\x02",
    )

    CloseMessageWindow()

    label("loc_9286")

    SetScenarioFlags(0xBF, 3)
    SetScenarioFlags(0x0, 6)

    label("loc_928C")

    OP_63(0x12, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_947E")

    label("loc_92A3")

    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93C0")

    ChrTalk(
        0x12,
        (
            "#1700FAll right, Sully! Just so you know, I start\x01",
            "my morning off with my regular practice\x01",
            "routines, okay?\x02\x03",
            "#1709FSo, be a doll and make sure to wake me\x01",
            "up before 5:00AM!\x02\x03",
            "#1705FOh, but I don't really have another bed.\x01",
            "...Wanna sleep in mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I'll pass!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_947A")

    label("loc_93C0")


    ChrTalk(
        0x15,
        (
            "Just tell me about the play. You know,\x01",
            "the new drama...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1702FOooh, you're interested? Okay, listen\x01",
            "up. I'll give you all the sweet details!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x15,
        "...! *nod*\x02",
    )

    CloseMessageWindow()

    label("loc_947A")

    OP_4C(0x15, 0xFF)

    label("loc_947E")

    TalkEnd(0x12)
    Return()

    # Function_19_8E6C end

    def Function_20_9482(): pass

    label("Function_20_9482")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9718")

    ChrTalk(
        0x14,
        (
            "#1802FI know I've caused you trouble by dragging\x01",
            "you into this, but...\x02\x03",
            "#1809F...thank you so, so much. Without you, things\x01",
            "may not have ended so peacefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FWe're just glad it worked out in the end.\x01",
            "None of us were expecting that twist at\x01",
            "the end there, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1804FIt certainly was a shock.\x02\x03",
            "#1810FYou know, I think I can relate to Sully\x01",
            "a little bit.\x02\x03",
            "Before meeting Ilya, I was just another\x01",
            "person who'd lost their way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou okay, Rixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1804FAh, yes... It's nothing.\x02\x03",
            "#1802FIt looks like Sully will be staying with\x01",
            "Ilya, for now. I'm sure she'd love for\x01",
            "you to visit, if you ever find the time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 4)
    Jump("loc_9872")

    label("loc_9718")


    ChrTalk(
        0x14,
        (
            "#1808FI'm just worried she'll have trouble\x01",
            "adapting, considering what she's\x01",
            "gone through.\x02\x03",
            "#1802FOf course, I intend to pitch in and help.\x01",
            "I'm sure everything will turn out okay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986F")

    ChrTalk(
        0x101,
        (
            "#0000FThat's reassuring. We'll leave Ilya and\x01",
            "Sully in your care, Rixia. Keep an eye\x01",
            "on them, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x14,
        "#1809FAbsolutely!\x02",
    )

    CloseMessageWindow()

    label("loc_986F")

    SetScenarioFlags(0x0, 7)

    label("loc_9872")

    TalkEnd(0xFE)
    Return()

    # Function_20_9482 end

    def Function_21_9876(): pass

    label("Function_21_9876")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF1")

    ChrTalk(
        0x101,
        (
            "#0002FStarting to get the feel for things\x01",
            "around here, Sully?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph. Not at all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We usually talk about random stuff.\x01",
            "But whenever she yammers on about\x01",
            "her plays, she shines. So...I listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(So she IS interested in theatre.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F(Guess she's got a girly side underneath\x01",
            "all that tomboy, after all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202F(So it seems.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 500)

    ChrTalk(
        0xFE,
        (
            "You said your name was Lloyd?\x01",
            "Well, listen up, punk! I'll see to\x01",
            "it that you pay for your crimes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This grudge is here to stay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FUgh... You're still mad about that?\x01",
            "(I wish she'd forget about it already.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0xC)
    Jump("loc_9B8A")

    label("loc_9AF1")


    ChrTalk(
        0xFE,
        (
            "Y'know, listening to Ilya isn't so bad.\x01",
            "She usually has a lot of interesting\x01",
            "stories to tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, most of the time, she's\x01",
            "a complete slob.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B8A")

    TalkEnd(0xFE)
    Return()

    # Function_21_9876 end

    def Function_22_9B8E(): pass

    label("Function_22_9B8E")

    EventBegin(0x0)
    Sound(103, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-170, 1280, 390, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -600, 0, 150, 0)
    SetChrPos(0x102, 600, 0, 150, 0)
    SetChrPos(0x103, -600, 0, -1500, 0)
    SetChrPos(0x104, 600, 0, -1500, 0)

    def lambda_9C18():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9C18)

    def lambda_9C2D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9C2D)

    def lambda_9C42():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9C42)

    def lambda_9C57():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9C57)
    OP_68(50, 1280, 1520, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x101,
        "#5P#0005FThe top floor of Villa-Raisins...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(1520, 11280, 18040, 3000)
    MoveCamera(45, 16, 0, 3000)
    Sleep(3200)

    ChrTalk(
        0x101,
        (
            "#0000FWe should be able to find Ilya's\x01",
            "room somewhere up there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(50, 1280, 1520, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#6P#0200FShall we go ahead and check on\x01",
            "her room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FDefinitely. Let's head on up.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10, 30, 990, 0)
    OP_29(0x1D, 0x1, 0x2)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_22_9B8E end

    def Function_23_9DD3(): pass

    label("Function_23_9DD3")

    EventBegin(0x0)
    Fade(500)
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -800, 10000, 19000, 0)
    SetChrPos(0x102, 200, 10000, 19000, 0)
    SetChrPos(0x103, -800, 10000, 17700, 0)
    SetChrPos(0x104, 200, 10000, 17700, 0)
    OP_0D()
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#5P#0000FAll right, the key should...\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, -140, 10030, 20150, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(400)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(600)

    ChrTalk(
        0x104,
        "#12P#0305F'Sup, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FS-Sorry. Something caught my eye...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(
        0x101,
        "#11P#0001FCheck it out. Scratches from a lock pick.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(15)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#0003FThey're small, but they're there. Whoever\x01",
            "opened it must be relatively skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FShall we take this as confirmation that\x01",
            "someone broke into the apartment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FI'd say so. That just means we have to\x01",
            "catch him even faster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FYeah, or else we run the risk of our\x01",
            "stalker making his next move.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(809, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    OP_93(0x101, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0001FLet's give this investigation everything\x01",
            "we've got! For Ilya's sake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FYou said it, pal!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    OP_68(49380, 1280, 51150, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(14880, 0)
    SetChrPos(0x101, 49100, 0, 50000, 0)
    SetChrPos(0x102, 50200, 0, 50000, 0)
    SetChrPos(0x103, 49100, 0, 49000, 0)
    SetChrPos(0x104, 50200, 0, 49000, 0)

    def lambda_A24F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A24F)

    def lambda_A264():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A264)

    def lambda_A279():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A279)

    def lambda_A28E():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A28E)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x104,
        (
            "#12P#0300FWhew. Dunno what I was expectin' from the\x01",
            "penthouse of a fancy apartment building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FTrue. I guess living alone in this spacious\x01",
            "apartment falls in line with Ilya's personality.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#0005FBut isn't this place a little...dirty?\x02",
    )

    CloseMessageWindow()
    OP_68(50860, 1280, 60190, 2200)
    Sleep(2600)
    Fade(500)
    OP_68(59700, 1280, 53950, 0)
    MoveCamera(53, 26, 0, 0)
    OP_68(59740, 1280, 53790, 2600)
    MoveCamera(37, 26, 0, 2600)
    Sleep(3000)

    ChrTalk(
        0x103,
        (
            "#0200FScattered clothes and empty\x01",
            "wine glasses...\x02\x03",
            "#0203FI can only assume that this was\x01",
            "Ilya's doing, not the stalker's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI always thought Ilya was an...interesting\x01",
            "character. Something like this isn't too\x01",
            "surprising, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FFor a fan, this must be a helluva sight to walk into.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(50120, 1280, 51750, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_93(0x0, 0x5A, 0x0)
    OP_93(0x1, 0x5A, 0x0)
    OP_93(0x2, 0x5A, 0x0)
    OP_93(0x3, 0x5A, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_A5A3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5A3)

    def lambda_A5B0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A5B0)

    def lambda_A5BD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A5BD)

    def lambda_A5CA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5CA)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0001FAnyway, let's try searching for any traces\x01",
            "the culprit might have left behind.\x02\x03",
            "#0003FOur end goal is to catch him and keep\x01",
            "him from messing with Ilya ever again.\x02\x03",
            "#0001FWe should proceed with caution for\x01",
            "the initial investigation, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1400)

    ChrTalk(
        0x102,
        (
            "#11P#0103FRight. We only have vague testimonies\x01",
            "to fall back on in a case like this.\x02\x03",
            "#0100FIf we don't catch the stalker in the midst\x01",
            "of the act, he can simply feign ignorance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FTrue, that'd end up bein' a big pain\x01",
            "in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIn order to catch him, I would like to begin\x01",
            "with examining his criminal profile, behavior,\x01",
            "and uncovering his infiltration route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FThat's a good start. We should question\x01",
            "the apartment residents while we're at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FMay as well scope out the layout of\x01",
            "the building, too.\x02\x03",
            "We ready to sniff some clues?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 49850, 30, 51640, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -46140, 1030, 59110, 0)
    SetChrPos(0xE, -45740, 1030, 60980, 180)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    OP_29(0x1D, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_9DD3 end

    def Function_24_A9B8(): pass

    label("Function_24_A9B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(49570, 1280, 52340, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21470, 0)
    SetChrPos(0x101, 48900, 0, 53200, 135)
    SetChrPos(0x102, 50400, 0, 53200, 225)
    SetChrPos(0x103, 48900, 0, 51800, 45)
    SetChrPos(0x104, 50400, 0, 51800, 315)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0003FI think we've got a basic idea of\x01",
            "his profile and entry route now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIndeed.\x02\x03",
            "The culprit, who was seen wearing a\x01",
            "hat, seems to be quite cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0101FAnd he's been sighted inside the building\x01",
            "with greater frequency as of late, too.\x02\x03",
            "#0103FAccording to what Ilya told us, nothing was\x01",
            "stolen, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FThat's weird as hell. What's the point of\x01",
            "breakin' in if you're not takin' anything?\x02\x03",
            "#0301FAnyway, I think we've figured this guy\x01",
            "out. His entry route musta been the\x01",
            "building's back entrance, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FIt looks that way. We can try to catch him\x01",
            "by surprise with the info we found.\x02\x03",
            "#0000FMind hearing me out, guys?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ACED)
    Sleep(10)

    def lambda_ACFD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACFD)
    Sleep(300)

    ChrTalk(
        0x103,
        "#12P#0205FDid you come up with another plan, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI think so. Our culprit may be a teenager,\x01",
            "but that doesn't mean that we should\x01",
            "slack off. He might catch us off guard.\x02\x03",
            "Besides, I want to be 100 percent sure\x01",
            "we can catch him before we act.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Return()

    # Function_24_A9B8 end

    def Function_25_AE2A(): pass

    label("Function_25_AE2A")

    EventBegin(0x0)
    OP_68(-9520, 1270, 4050, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(22920, 0)
    SetChrPos(0x8, 10310, 10000, 17660, 45)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x15, 0x8000)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    OP_4B(0x15, 0xFF)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7302", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(25420, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1300)
    OP_68(9410, 11270, 15790, 6000)
    MoveCamera(45, 18, 0, 6000)
    OP_6E(320, 6000)
    SetCameraDistance(28920, 6000)
    Sleep(6800)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "#5POkay, all of the hallways should be\x01",
            "squeaky clean now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5POh, darn it. Tomorrow's parade changed\x01",
            "the trash pickup schedule, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI better warn Kendall while I still\x01",
            "have the chance.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 26)
    Sleep(4500)
    OP_68(-5680, 1250, 6550, 4200)
    MoveCamera(45, 22, 0, 4200)
    OP_6E(320, 4200)
    SetCameraDistance(31420, 4200)
    SetChrPos(0x15, -5900, 30, 6280, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    OP_6F(0x1)
    Sleep(300)

    NpcTalk(
        0x15,
        "Boy",
        "#5P...\x02",
    )

    CloseMessageWindow()
    OP_95(0x15, -7610, 30, 4530, 1900, 0x1)
    OP_95(0x15, -9430, 20, 4530, 1900, 0x1)

    def lambda_B08D():
        OP_95(0xFE, -9430, 1150, 6880, 1900, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B08D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x15, 2800, 10000, 18580, 270)

    def lambda_B0F1():
        OP_95(0xFE, -250, 10000, 18580, 1700, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B0F1)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    EndChrThread(0x15, 0x1)
    OP_95(0x15, -250, 10020, 19710, 1700, 0x0)
    Sleep(300)

    NpcTalk(
        0x15,
        "Boy",
        "#5P...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The boy produced a thin wire from his pocket\x01",
            "and gracefully slid it into the keyhole.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(833, 0, 100, 0)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(200)

    NpcTalk(
        0x15,
        "Boy",
        "#5PHeh. Piece of cake.\x02",
    )

    CloseMessageWindow()
    OP_95(0x15, -250, 10000, 22830, 1500, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x2, 0x10)
    OP_68(50000, 1280, 51630, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x15, 50000, 30, 51630, 0)
    SetChrPos(0x102, 56790, 1000, 55420, 0)
    SetChrPos(0x103, 57110, 1000, 54440, 0)
    SetChrPos(0x104, 49770, 0, 50440, 0)
    SetChrPos(0x101, 56790, 1000, 55420, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x15,
        "Boy",
        "#5PI'm sure today will be the day...\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x5A, 0x1F4)
    Sleep(400)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    NpcTalk(
        0x15,
        "Boy",
        "#5PUgh, gross. This place never gets any cleaner.\x02",
    )

    CloseMessageWindow()
    OP_68(51840, 1280, 59480, 3000)
    OP_95(0x15, 50000, 1050, 57300, 1800, 0x0)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#5P*sigh* Does she always drink this much?\x01",
            "Her poor liver...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#5PGeez. Walking into a place this dirty is really\x01",
            "killing my desire to wanna steal some stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(55300, 1280, 61530, 3000)
    OP_95(0x15, 53730, 1030, 57300, 1600, 0x0)
    OP_95(0x15, 54180, 1030, 60610, 1600, 0x0)
    OP_93(0x15, 0x10E, 0x1F4)

    NpcTalk(
        0x15,
        "Boy",
        "#5PNow, what looks expensive?\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#5PNope, not this. She'd probably freak\x01",
            "out if this went missing...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(56080, 1280, 62450, 1000)
    OP_95(0x15, 54710, 1030, 61820, 1600, 0x0)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#5PHmph. I'd prefer it if she had a safe\x01",
            "I could rummage through, or...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)

    NpcTalk(
        0x101,
        "Voice",
        "#1P#4SFreeze!\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x15, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x15, 0x102, 500)
    OP_68(55910, 2280, 60270, 1200)
    MoveCamera(68, 24, 0, 1200)
    OP_6E(440, 1200)
    SetCameraDistance(21000, 1200)

    def lambda_B5C3():
        OP_95(0xFE, 56540, 1030, 58700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5C3)

    def lambda_B5DD():
        OP_95(0xFE, 55760, 1000, 57400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5DD)

    NpcTalk(
        0x15,
        "Boy",
        "#5PHuh? Who? What?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#0105FI was wondering what kind of kid\x01",
            "our stalker would be, but he really\x01",
            "is young, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWell, we have observed the crime for ourselves.\x01",
            "It is time to cooperate with us and come quietly.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#5PY-You were waiting for me?! Crap, crap,\x01",
            "crap! I screwed up big time!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Young Man's Voice",
        "Sorry, bud. You ain't goin' nowhere.\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xE1, 0x1F4)
    OP_68(51490, 880, 55350, 1500)
    MoveCamera(47, 24, 0, 1500)
    OP_6E(440, 1500)
    SetCameraDistance(21000, 1500)
    OP_95(0x104, 49860, 30, 52710, 1800, 0x0)

    ChrTalk(
        0x104,
        (
            "#0300F#12PYou've hit a dead end. Might as well\x01",
            "give up and surrender while you can.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(55210, 1280, 61550, 0)
    MoveCamera(47, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    StopBGM(0xBB8)

    NpcTalk(
        0x15,
        "Boy",
        "#5PSh-Shuddup! You'll never catch me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        "#5PI hate...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        "#5PI HATE YOU GUYS!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(49830, 1950, 54370, 3000)
    MoveCamera(50, 19, 0, 3000)
    SetCameraDistance(24490, 3000)

    def lambda_B8EA():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B8EA)

    def lambda_B8F7():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B8F7)
    OP_95(0x15, 52040, 1030, 62670, 6000, 0x1)
    OP_95(0x15, 51770, 1000, 58240, 6000, 0x1)
    SetChrChip(0x0, 0x15, 0x32, 0x12C)
    Sleep(100)
    SetChrFlags(0x15, 0x4)
    OP_9D(0x15, 0xCA6C, 0x8FC, 0xD9DA, 0x578, 0x1388)
    Sound(804, 0, 100, 0)
    Sleep(200)
    OP_9D(0x15, 0xCAB2, 0x0, 0xC88C, 0x64, 0x1388)
    SetChrFlags(0x15, 0x4)
    Sound(814, 0, 100, 0)
    OP_95(0x15, 49910, 30, 51420, 7000, 0x0)

    def lambda_B992():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B992)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_95(0x15, 49740, 0, 46610, 7000, 0x0)

    ChrTalk(
        0x104,
        "#12P#0305FThe hell?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x15, 500)
    Sleep(400)
    BeginChrThread(0x102, 1, 0, 27)
    BeginChrThread(0x103, 1, 0, 28)

    ChrTalk(
        0x104,
        "#6P#0301FQuick lil' guy, ain't he?\x02",
    )

    CloseMessageWindow()
    SetChrChip(0x1, 0x15, 0x0, 0x0)

    ChrTalk(
        0x103,
        "#11P#0201FRandy, focus!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101FFollow him!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(200)

    ChrTalk(
        0x104,
        "#0307F#12PGot'cha!\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)

    def lambda_BA9C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA9C)

    def lambda_BAB1():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAB1)

    def lambda_BAC6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BAC6)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-270, 11270, 18770, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x15, -200, 10000, 22910, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)

    def lambda_BB3A():
        OP_95(0xFE, -200, 10000, 18300, 7000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BB3A)
    OP_82(0xC8, 0x64, 0xBB8, 0x12C)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    Sound(818, 0, 80, 0)
    FadeToBright(250, 0)
    OP_0D()
    WaitChrThread(0x15, 1)
    OP_95(0x15, 7690, 10000, 18300, 7000, 0x0)

    def lambda_BB99():
        OP_95(0xFE, 9100, 10030, 15930, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BB99)
    Fade(300)
    OP_68(-3140, 1250, 4150, 0)
    OP_68(-60, 1250, 1780, 1000)
    EndChrThread(0x15, 0x1)
    SetChrPos(0x15, -3510, 30, 3820, 135)
    OP_95(0x15, -310, 0, 620, 7000, 0x0)
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(400)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The boy left the door wide open.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    NpcTalk(
        0x15,
        "Boy",
        "#11PIdiots! Just TRY to catch me!\x02",
    )

    CloseMessageWindow()
    OP_95(0x15, -5860, 0, 6840, 7000, 0x0)
    OP_95(0x15, -5860, 200, 12240, 7000, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_AE2A end

    def Function_26_BCBF(): pass

    label("Function_26_BCBF")

    OP_95(0x8, 9010, 10020, 15730, 2100, 0x0)
    OP_95(0x8, 8610, 7500, 10850, 2100, 0x0)
    OP_95(0x8, 1970, 5000, 10850, 2300, 0x0)
    OP_95(0x8, -2860, 5000, 17000, 2300, 0x0)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_26_BCBF end

    def Function_27_BD15(): pass

    label("Function_27_BD15")

    OP_95(0x102, 49750, 1050, 57720, 5000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_27_BD15 end

    def Function_28_BD31(): pass

    label("Function_28_BD31")

    OP_95(0x103, 50510, 1000, 56870, 5000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_28_BD31 end

    def Function_29_BD4D(): pass

    label("Function_29_BD4D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    LoadChrToIndex("chr/ch05100.itc", 0x1F)
    OP_68(48420, 2250, 52020, 0)
    MoveCamera(43, 12, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16100, 0)
    OP_68(48360, 2250, 51810, 0)
    MoveCamera(43, 12, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16100, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 49320, 0, 50740, 0)
    SetChrPos(0x102, 52190, 0, 53090, 270)
    SetChrPos(0x104, 52150, 0, 51670, 270)
    SetChrPos(0x103, 50770, 0, 50780, 0)
    SetChrPos(0x12, 49730, 1000, 55910, 180)
    SetChrPos(0x14, 50950, 1000, 55970, 225)
    SetChrPos(0x15, 49800, 30, 52560, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x4)
    OP_4B(0x12, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Special Support Section quickly contacted\x01",
            "Ilya and informed her of the stalker's arrest.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The boy kept struggling, but, as if resigning to\x01",
            "his fate, soon quieted down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7111", 0)
    SetCameraDistance(15100, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#5P#1705FWow! So THIS is our stalker.\x02\x03",
            "#1700FShorter than I thought you'd be... You\x01",
            "aren't from around here, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FRight. It looks like he's from a slum\x01",
            "near the border.\x02\x03",
            "#0001FThat's all we got out of him, though.\x01",
            "We don't know his motive, much less\x01",
            "his name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#1703FHmm, I see. I see...\x02\x03",
            "#1700FSo, out with it. Why all the stalking?\x02\x03",
            "Something you want from me?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x13B, 0x190)
    Sleep(300)

    NpcTalk(
        0x15,
        "Boy",
        "#6PHmph. That's not it...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PI was just wanting to harass you\x01",
            "a little, that's all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(3)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(5)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(4)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x14,
        "#1805F#11PHarass her? Why?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(300)

    NpcTalk(
        0x15,
        "Boy",
        "#6PAs if you people could ever understand...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PYou live in such fancy places and never\x01",
            "have to worry about your next meal...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x96, 0x0, 0xBB8, 0x320)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6P#4S#NPeople like you could never understand\x01",
            "how it feels to live in a dump for most of\x01",
            "your life!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x101,
        "#12P#0005F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FOh...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    OP_93(0x15, 0x13B, 0x190)
    PlayBGM("ed7005", 0)
    Sleep(300)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PAfter I came to Crossbell, I saw it time\x01",
            "after time after time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PEverybody living here is rich. They\x01",
            "foolishly party all night, throwing\x01",
            "away mira like it's worthless.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PUgh! Suit yourselves, jerks!\x01",
            "They're all scum.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PBut they all agreed that going to watch\x01",
            "Arc en Ciel was their favorite pastime,\x01",
            "so I snuck in one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1705F#5PYou...did?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FSo you saw Arc en Ciel's--no, Ilya's\x01",
            "performance?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PYeah. I hate people who get to casually\x01",
            "live their lives without any worries.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        "#6PBut y-you...! I hate you the most!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PYou prance around on that beautiful\x01",
            "stage, representing an amazing world...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PYou just stand there, dazzling, knowing\x01",
            "it's unreachable for a person like me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PI know that there's no chance I'd ever\x01",
            "get there. I know I never would...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6PI could work my entire life and never\x01",
            "even have enough for a single ticket!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x96, 0x64, 0xBB8, 0x320)

    NpcTalk(
        0x15,
        "Boy",
        (
            "#6P#4S#NTell me I'm wrong! Tell me I can get\x01",
            "there someday! You can't!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0x190, 0x0)
    Sleep(3200)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x12)
    OP_64(0x14)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#11P#0303F...\x01",
            "So that's why ya did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0008FYou came to Crossbell and ended up\x01",
            "watching Ilya perform...\x02\x03",
            "#0006FI can only imagine the culture shock\x01",
            "it must have been for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1803F#11PI think I understand where you're coming from...\x02\x03",
            "#1808FYou're not wrong. There are certain parts of\x01",
            "Crossbell that are as you described.\x02\x03",
            "#1801FIt can be a dark, overpowering city at\x01",
            "times. An oppressive metropolis that feeds\x01",
            "off the misery it brings to its citizens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1703F#5P...\x02\x03",
            "#1700FThat may be, but you still have to take\x01",
            "responsibility for your actions.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CA9B():

        label("loc_CA9B")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_CA9B")

    QueueWorkItem2(0x0, 1, lambda_CA9B)

    def lambda_CAAD():

        label("loc_CAAD")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_CAAD")

    QueueWorkItem2(0x1, 1, lambda_CAAD)

    def lambda_CABF():

        label("loc_CABF")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_CABF")

    QueueWorkItem2(0x2, 1, lambda_CABF)

    def lambda_CAD1():

        label("loc_CAD1")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_CAD1")

    QueueWorkItem2(0x3, 1, lambda_CAD1)

    def lambda_CAE3():

        label("loc_CAE3")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_CAE3")

    QueueWorkItem2(0x14, 1, lambda_CAE3)
    OP_68(48800, 2250, 51320, 2000)

    def lambda_CB06():
        OP_95(0xFE, 49730, 0, 54230, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CB06)

    ChrTalk(
        0x102,
        "#11P#0105FIlya...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0011FAre you sure about this?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 1)

    ChrTalk(
        0x12,
        "#5P#1701FI'm Ilya Platiere. What's your name?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Boy",
        "#6P...Sully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#1703FHmm... 'Sully.' I like it!\x02\x03",
            "#1701FWell, Sully. I'm going to make you\x01",
            "work as my assistant for a while.\x02\x03",
            "It's not like you can pay me off\x01",
            "with mira, can you? Oh, I'll see\x01",
            "to it that you'll work your share.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(18)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        "#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FWh-What are you talking about, Ilya?\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x87, 0x190)
    Sleep(200)

    ChrTalk(
        0x12,
        (
            "#5P#1706FSooorry, Lloyd. I know you went the\x01",
            "extra selge with everything, but...\x02\x03",
            "#1700F...how about you let me take care of\x01",
            "my stalker for the time being?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0302FFast acquittal, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0202FGood grief. There is not much we can\x01",
            "do about the matter if Ilya insists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5P#1704FHmm. Let's see, now...\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x190)
    OP_95(0x12, 49900, 0, 53370, 1000, 0x0)
    Sleep(200)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(819, 0, 100, 0)
    OP_A6(0x15, 0x0, 0xF, 0xC8, 0xBB8)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ilya gave the boy a few pats on the shoulder.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    BeginChrThread(0x15, 1, 0, 30)

    ChrTalk(
        0x15,
        "#6PWh-What do you think you're doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#1709FAha. I knew it.\x02\x03",
            "#1700FIt'd be better if you grew some\x01",
            "muscles in a few places, but...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x1)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFFA")
    OP_93(0x15, 0x10E, 0x190)

    label("loc_CFFA")

    Sleep(400)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x12,
        (
            "#5P#1702FI gotta be honest with you, Sully.\x01",
            "You've got a lot of potential.\x02\x03",
            "#1709FWith the right training, you could\x01",
            "become an amazing dancer.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        "#6P...\x02",
    )

    CloseMessageWindow()
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x15,
        "#6P#4SHUH?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#6PWh-Why me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0102FNow that you mention it, that agility\x01",
            "was nothing short of impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FTrue that. Your footwork was pretty\x01",
            "damn good, too.\x02\x03",
            "#0304FYou might be on to somethin' here,\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#1702FOh, I've got it. I hereby declare that\x01",
            "you'll be staying here with myself.\x02\x03",
            "#1709FNo ifs, ands, or buts about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x15,
        "#6PI-I... But that's...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(700)
    OP_64(0x15)
    BeginChrThread(0x12, 2, 0, 31)
    Sleep(700)
    BeginChrThread(0x15, 2, 0, 31)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#1809F#5PHow very much like Ilya.\x02\x03",
            "#1810FYou know, I basically went through\x01",
            "the same thing. I was forced into\x01",
            "staying with her for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_D321():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D321)
    Sleep(20)

    def lambda_D331():
        OP_93(0xFE, 0x0, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D331)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#12P#0002FThat's how it happened?\x02\x03",
            "#0004FGood thing we called Ilya. She\x01",
            "defused the situation way better\x01",
            "than we ever could have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0202FAgreed.\x02",
    )

    CloseMessageWindow()

    def lambda_D3DF():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D3DF)
    Sleep(20)

    def lambda_D3EF():
        OP_93(0xFE, 0x10E, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D3EF)
    Sleep(800)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x15, 0x2)
    OP_64(0x12)
    OP_64(0x15)

    ChrTalk(
        0x12,
        "#1709F#5PStraighten up! No complaints!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#6PB-But I haven't even said yes, yet!\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0x12, 2, 0, 31)
    Sleep(600)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    EndChrThread(0x12, 0x2)
    OP_64(0x12)
    OP_68(-950, 11250, 18010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22750, 0)
    SetChrPos(0x101, -660, 10000, 17460, 0)
    SetChrPos(0x102, 390, 10000, 17460, 0)
    SetChrPos(0x103, -660, 10000, 16030, 0)
    SetChrPos(0x104, 390, 10000, 16030, 0)
    SetChrPos(0x12, -730, 10030, 19740, 180)
    SetChrPos(0x14, 530, 10020, 19600, 180)
    SetChrPos(0x15, -280, 10020, 19200, 180)
    SetChrFlags(0x103, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7106", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#5P#1705FYou guys leavin' already? You can\x01",
            "always stay and have some tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F#6PI appreciate the offer, but we still\x01",
            "have some work to take care of.\x02\x03",
            "#0005FOh, right. Here's your key. You'll\x01",
            "probably need this.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -640, 10000, 18640, 1200, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Returned ",
            scpstr(SCPSTR_CODE_ITEM, 0x347),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x347, 1)
    OP_96(0x101, 0xFFFFFD6C, 0x2710, 0x44FC, 0x4B0, 0x0)

    ChrTalk(
        0x12,
        (
            "#5P#1704FWho needs a key when I have\x01",
            "Sully with me?\x02\x03",
            "#1700FThanks for the help, lil' guy. Be\x01",
            "careful on your way back, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#1809FYou have my thanks, as well.\x01",
            "You're always so reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FNo probs, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0102FWe'll leave Sully in your care, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0204FWe may have solved the case, but you\x01",
            "would be wise to pay more attention\x01",
            "when locking your door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0014F#6PWhat Tio said! If you need anything else,\x01",
            "you can always count on the SSS.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    Sleep(200)

    def lambda_D8AA():

        label("loc_D8AA")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_D8AA")

    QueueWorkItem2(0x12, 1, lambda_D8AA)

    def lambda_D8BC():

        label("loc_D8BC")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_D8BC")

    QueueWorkItem2(0x14, 1, lambda_D8BC)
    OP_95(0x101, -600, 10000, 18360, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0000F#6PSee you later, Sully.\x02\x03",
            "#0002FDon't do anything like this again, okay?\x01",
            "It's your obligation as a man to make sure\x01",
            "you pay back your debt.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(930, 11250, 17540, 2800)

    def lambda_D9AD():

        label("loc_D9AD")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_D9AD")

    QueueWorkItem2(0x15, 1, lambda_D9AD)

    def lambda_D9BF():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D9BF)

    def lambda_D9D4():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9D4)

    def lambda_D9E9():
        OP_9B(0x0, 0xFE, 0x5A, 0xA28, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D9E9)

    def lambda_D9FE():
        OP_95(0xFE, 1870, 10000, 17460, 700, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9FE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_64(0x15)

    ChrTalk(
        0x15,
        "#5POh, I hate you the most.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)

    def lambda_DA6B():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DA6B)
    Sleep(12)

    def lambda_DA7B():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DA7B)

    def lambda_DA88():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DA88)
    Sleep(10)

    def lambda_DA98():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_DA98)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0005FWhat'd I do?!\x02",
    )

    CloseMessageWindow()
    OP_68(930, 11050, 18160, 2000)
    MoveCamera(349, 25, 0, 2000)
    Sleep(500)
    OP_95(0x15, 460, 10000, 18630, 3000, 0x0)
    OP_6F(0x79)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x15,
        "#5P#4SI'm a GIRL, you moron!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#5P#4SHow much longer do you intend to\x01",
            "insult me?! You're infuriating!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x104)
    OP_64(0x102)
    Sleep(300)
    OP_82(0xC8, 0x0, 0x7D0, 0x12C)

    ChrTalk(
        0x101,
        "#6P#0011F#4S...You're a WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FYa don't say...\x02\x03",
            "#0301FWell, I guess you do kinda\x01",
            "have a girly face...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#6P#0205FYou did not notice until now either,\x01",
            "Randy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x104, 500)

    ChrTalk(
        0x14,
        (
            "#5P#1809FHow'd you make that mistake,\x01",
            "you two? Isn't it obvious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0011F...\x02\x03",
            "#0012FUhhh, so when I caught you\x01",
            "and...I... With all my strength...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_DDBC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDBC)

    def lambda_DDC9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDC9)

    def lambda_DDD6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DDD6)

    ChrTalk(
        0x104,
        "#12P#0307FDon't think about it, man!\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x15, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#11PTh-That's why I was telling you to let go\x01",
            "of me, you absolute moron!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    def lambda_DE81():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE81)
    OP_64(0x15)

    ChrTalk(
        0x101,
        (
            "#6P#0011FB-But, I swear, everything about\x01",
            "you felt like a guy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0111FYou remembered how it felt...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0211FA statement that is both incriminating and controversial.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    def lambda_DF55():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF55)

    ChrTalk(
        0x101,
        "#5P#0012FGUYS! I did NOT mean it like that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#1709FAhaha, what's the big deal? He was\x01",
            "just seizing the opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P#1806FOh, Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x101, 1, 0, 32)

    ChrTalk(
        0x101,
        (
            "#6P#0011FY-You're blowing this out of proportion!\x01",
            "I didn't have any ulterior motives!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21750, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Stalker Investigation!!!]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_64(0x101)
    EndChrThread(0x101, 0x1)
    SetChrPos(0x0, -280, 10020, 19290, 180)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x12, 52530, 1050, 60070, 270)
    SetChrPos(0x14, 58290, 1030, 62500, 0)
    SetChrPos(0x15, 51930, 1050, 60970, 135)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetMapObjFrame(0xFF, "huku_nugippa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_1B(0x8, 0xFF, 0xFFFF)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0x1D, 0x4, 0x10)
    OP_29(0x1D, 0x1, 0xA)
    OP_C7(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_BD4D end

    def Function_30_E190(): pass

    label("Function_30_E190")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1BC")
    OP_93(0xFE, 0x10E, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0x0, 0x190)
    Jump("Function_30_E190")

    label("loc_E1BC")

    Return()

    # Function_30_E190 end

    def Function_31_E1BD(): pass

    label("Function_31_E1BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1E2")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_31_E1BD")

    label("loc_E1E2")

    Return()

    # Function_31_E1BD end

    def Function_32_E1E3(): pass

    label("Function_32_E1E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E211")
    TurnDirection(0xFE, 0x12, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)
    TurnDirection(0xFE, 0x103, 500)
    Sleep(800)
    Jump("Function_32_E1E3")

    label("loc_E211")

    Return()

    # Function_32_E1E3 end

    def Function_33_E212(): pass

    label("Function_33_E212")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E238")
    Call(0, 23)
    Jump("loc_E269")

    label("loc_E238")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_E269")

    Return()

    # Function_33_E212 end

    def Function_34_E26A(): pass

    label("Function_34_E26A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E45A")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wine glasses and bottles are scattered\x01",
            "across the apartment.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All that's left in the bottles are a few drops\x01",
            "of wine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
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
        "#0012FDid she stay up all night drinking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, I've heard that Ilya Platiere\x01",
            "is a pretty heavy drinker.\x02\x03",
            "Color me impressed. Didn't think she'd\x01",
            "be able to down this much in a night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou think?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_E4F9")

    label("loc_E45A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wine glasses and bottles are scattered all\x01",
            "across the apartment.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All that's left in the bottles are a few drops\x01",
            "of wine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_E4F9")

    TalkEnd(0xFF)
    Return()

    # Function_34_E26A end

    def Function_35_E4FD(): pass

    label("Function_35_E4FD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E680")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eastern outfits and dresses are messily strewn\x01",
            "out on the bed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x102,
        "#0106FThese are all brand clothes, and yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FComplete and utter disarray.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FLooks like she left 'em there after she\x01",
            "took 'em outta the closet this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, it's not hard to imagine the chaos\x01",
            "of her getting ready to go to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_E6E0")

    label("loc_E680")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eastern outfits and dresses are messily strewn\x01",
            "out on the bed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_E6E0")

    TalkEnd(0xFF)
    Return()

    # Function_35_E4FD end

    def Function_36_E6E4(): pass

    label("Function_36_E6E4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FFor now, let's focus on finding traces\x01",
            "of the stalker.\x02\x03",
            "Ilya gave us the key to her apartment,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -160, 30, 1350, 0)
    EventEnd(0x4)
    Return()

    # Function_36_E6E4 end

    SaveToFile()

Try(main)
