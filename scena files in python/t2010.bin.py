from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2010.bin",                # FileName
        "t2010",                    # MapName
        "t2010",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 6, 0, 7],
    )

    BuildStringList((
        "t2010",                  # 0
        "Guardsman Connors",      # 1
        "Guardsman Sigg",         # 2
        "Guardsman Cless",        # 3
        "Stella",                 # 4
        "Beyond",                 # 5
        "Bracer Scott",           # 6
        "Bracer Wenzel",          # 7
        "Tourist",                # 8
        "Merchant",               # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Merchant",               # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Merchant",               # 20
        "Tourist",                # 21
        "Tourist",                # 22
        "Tourist",                # 23
        "Girl",                   # 24
        "Merchant",               # 25
        "Tourist",                # 26
        "Tourist Cuoca",          # 27
        "Tourist Nat",            # 28
        "車１",                   # 29
        "Tourist",                # 30
        "Tourist",                # 31
        "車１",                   # 32
        "Mr. Crois",              # 33
        "Mr. Crois",              # 34
        "Warrant Officer Mireille",# 35
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch24900.itc",                   # 01
        "chr/ch24800.itc",                   # 02
        "chr/ch31202.itc",                   # 03
        "chr/ch32202.itc",                   # 04
        "chr/ch21800.itc",                   # 05
        "chr/ch21802.itc",                   # 06
        "chr/ch22000.itc",                   # 07
        "chr/ch21902.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch21702.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch27600.itc",                   # 0C
        "chr/ch22302.itc",                   # 0D
        "chr/ch32400.itc",                   # 0E
        "chr/ch32402.itc",                   # 0F
        "chr/ch27202.itc",                   # 10
        "chr/ch27302.itc",                   # 11
        "chr/ch32200.itc",                   # 12
        "chr/ch32600.itc",                   # 13
        "chr/ch23000.itc",                   # 14
        "chr/ch26900.itc",                   # 15
        "chr/ch00000.itc",                   # 16
    ))

    DeclNpc(-6590,   0,       7079,    200,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8720,    0,       4400,    135,  257,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-97470,  150,     -3950,   270,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-105500, 0,       2099,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-162110, 0,       -2500,   90,   257,  0x0, 0,   2,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-99519,  150,     3930,    270,  469,  0x0, 0,   16,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-101790, 150,     3930,    90,   469,  0x0, 0,   17,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   4,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-5829,   0,       2259,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-2660,   0,       3680,    90,   385,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-94699,  0,       4190,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-92129,  0,       4190,    270,  469,  0x0, 0,   8,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(10130,   0,       6190,    180,  385,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-101949, 150,     3859,    90,   469,  0x0, 0,   8,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-6329,   0,       5099,    0,    401,  0x0, 0,   9,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-94669,  150,     2319,    90,   401,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(5099,    0,       2269,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-7019,   0,       2200,    90,   401,  0x0, 0,   7,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-5929,   0,       2200,    270,  401,  0x0, 0,   11,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-1470,   0,       3309,    180,  385,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(2109,    0,       6769,    180,  385,  0x0, 0,   12,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-94669,  150,     4070,    90,   469,  0x0, 0,   15,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-94669,  150,     4070,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-9600,   0,       400,     270,  385,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   469,  0x0, 0,   4,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-93300,  0,       -1700,   0,    385,  0x0, 0,   21,  0,   0,   4,   0,   39,  255,  0)
    DeclNpc(-154259, 0,       1389,    45,   385,  0x0, 0,   20,  0,   0,   5,   0,   41,  255,  0)
    DeclNpc(-6000,   0,       0,       225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(11789,   0,       6219,    180,  385,  0x0, 0,   11,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(4150,    0,       3130,    0,    385,  0x0, 0,   18,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(16569,   0,       5380,    0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(12060,   0,       -3710,   225,  405,  0x0, 0,   19,  0,   0,   0,   0,   38,  255,  0)

    DeclActor(-6600,   0,       6140,    1000,    -6590,   1500,    7080,    0x007E, 0,  8,  0x0000)
    DeclActor(-103650, 0,       1450,    1000,    -105500, 1500,    2100,    0x007E, 0,  12, 0x0000)
    DeclActor(-161140, 0,       -2700,   1000,    -162110, 1500,    -2500,   0x007E, 0,  15, 0x0000)
    DeclActor(9250,    0,       -5930,   2000,    9650,    4000,    -8830,   0x007C, 0,  43, 0x0000)
    DeclActor(2900,    0,       -12480,  1000,    2900,    1000,    -12480,  0x007C, 0,  40, 0x0000)

    ScpFunction((
        "Function_0_630",          # 00, 0
        "Function_1_6E8",          # 01, 1
        "Function_2_785",          # 02, 2
        "Function_3_80E",          # 03, 3
        "Function_4_839",          # 04, 4
        "Function_5_864",          # 05, 5
        "Function_6_88F",          # 06, 6
        "Function_7_A1D",          # 07, 7
        "Function_8_BAB",          # 08, 8
        "Function_9_BAF",          # 09, 9
        "Function_10_16FD",        # 0A, 10
        "Function_11_2290",        # 0B, 11
        "Function_12_314D",        # 0C, 12
        "Function_13_3151",        # 0D, 13
        "Function_14_3F0C",        # 0E, 14
        "Function_15_40DB",        # 0F, 15
        "Function_16_40DF",        # 10, 16
        "Function_17_582B",        # 11, 17
        "Function_18_5B47",        # 12, 18
        "Function_19_5D14",        # 13, 19
        "Function_20_5E94",        # 14, 20
        "Function_21_5F96",        # 15, 21
        "Function_22_601A",        # 16, 22
        "Function_23_61C6",        # 17, 23
        "Function_24_6390",        # 18, 24
        "Function_25_63FA",        # 19, 25
        "Function_26_659C",        # 1A, 26
        "Function_27_676A",        # 1B, 27
        "Function_28_6808",        # 1C, 28
        "Function_29_68CA",        # 1D, 29
        "Function_30_694B",        # 1E, 30
        "Function_31_698A",        # 1F, 31
        "Function_32_6B28",        # 20, 32
        "Function_33_6CBD",        # 21, 33
        "Function_34_6CE2",        # 22, 34
        "Function_35_6D7A",        # 23, 35
        "Function_36_70B1",        # 24, 36
        "Function_37_70F4",        # 25, 37
        "Function_38_716E",        # 26, 38
        "Function_39_72EB",        # 27, 39
        "Function_40_746B",        # 28, 40
        "Function_41_750F",        # 29, 41
        "Function_42_75D7",        # 2A, 42
        "Function_43_7D6B",        # 2B, 43
        "Function_44_99AD",        # 2C, 44
        "Function_45_ACA5",        # 2D, 45
    ))


    def Function_0_630(): pass

    label("Function_0_630")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_670"),
        (1, "loc_67C"),
        (2, "loc_688"),
        (3, "loc_694"),
        (4, "loc_6A0"),
        (5, "loc_6AC"),
        (6, "loc_6B8"),
        (SWITCH_DEFAULT, "loc_6C4"),
    )


    label("loc_670")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_67C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_688")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_694")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6D0")

    label("loc_6E7")

    Return()

    # Function_0_630 end

    def Function_1_6E8(): pass

    label("Function_1_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_784")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_1_6E8")

    label("loc_784")

    Return()

    # Function_1_6E8 end

    def Function_2_785(): pass

    label("Function_2_785")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80D")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_2_785")

    label("loc_80D")

    Return()

    # Function_2_785 end

    def Function_3_80E(): pass

    label("Function_3_80E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_838")
    OP_94(0xFE, 0xFFFFFC5E, 0x12A2, 0x1194, 0x1E8C, 0x3E8)
    Sleep(300)
    Jump("Function_3_80E")

    label("loc_838")

    Return()

    # Function_3_80E end

    def Function_4_839(): pass

    label("Function_4_839")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_863")
    OP_94(0xFE, 0xFFFE8D6A, 0xFFFFF0EC, 0xFFFE9A8A, 0xFFFFFB46, 0x3E8)
    Sleep(400)
    Jump("Function_4_839")

    label("loc_863")

    Return()

    # Function_4_839 end

    def Function_5_864(): pass

    label("Function_5_864")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88E")
    OP_94(0xFE, 0xFFFD9E1E, 0x32, 0xFFFDAD46, 0xBE0, 0x3E8)
    Sleep(300)
    Jump("Function_5_864")

    label("loc_88E")

    Return()

    # Function_5_864 end

    def Function_6_88F(): pass

    label("Function_6_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8B7")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_A04")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8D5")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_A04")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8F9")
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_A04")

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x9, -110, 0, 1840, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_A04")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_94F")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_A04")

    label("loc_94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_96D")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_A04")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9D7")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x9, -6660, 0, -4750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9B1")
    ClearChrFlags(0x2A, 0x80)

    label("loc_9B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2")
    Event(0, 42)

    label("loc_9D2")

    Jump("loc_A04")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9F0")
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_A04")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A04")
    ClearChrFlags(0xF, 0x80)
    BeginChrThread(0x9, 0, 0, 1)

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1C")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x80)

    label("loc_A1C")

    Return()

    # Function_6_88F end

    def Function_7_A1D(): pass

    label("Function_7_A1D")

    OP_70(0x7, 0x8C)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x8, 0x4)
    OP_78(0x4, 0x24)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A76")
    Jump("loc_BAA")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A84")
    Jump("loc_BAA")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A92")
    Jump("loc_BAA")

    label("loc_A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_ABF")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_BAA")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AF7")
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x24, 5500, 0, 0, 0)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_BAA")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B05")
    Jump("loc_BAA")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B7A")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x24, 2840, 0, 5360, 0)
    OP_78(0x5, 0x27)
    ClearMapObjFlags(0x5, 0x4)
    OP_D3(0x27, 0x0, 0x15F90, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B75")
    OP_66(0x3, 0x1)

    label("loc_B75")

    Jump("loc_BAA")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BA1")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_BAA")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BAA")

    label("loc_BAA")

    Return()

    # Function_7_A1D end

    def Function_8_BAB(): pass

    label("Function_8_BAB")

    Call(0, 9)
    Return()

    # Function_8_BAB end

    def Function_9_BAF(): pass

    label("Function_9_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    TalkBegin(0x16)
    Jump("loc_BC8")

    label("loc_BC5")

    TalkBegin(0x8)

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC5")

    ChrTalk(
        0x8,
        (
            "Being stuck on desk duty kind of bothers me,\x01",
            "but someone has to do all this paperwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter what job I'm given, I intend\x01",
            "to do it to the best of my ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I think that should be important above all else.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D65")

    label("loc_CC5")


    ChrTalk(
        0x8,
        (
            "I'll be honest. Working for the CGF can\x01",
            "be unrewarding at times...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but since this is what I was assigned\x01",
            "to do, I'll make sure to give it my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D65")

    Jump("loc_16E3")

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DE4")

    ChrTalk(
        0x8,
        (
            "Well, time for another long day of\x01",
            "paperwork.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is this really what I wanted\x01",
            "to do when I enlisted?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E3")

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_ED4")

    ChrTalk(
        0x8,
        (
            "According to the others, the investigation\x01",
            "of those ruins was suddenly put on ice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's the commander's responsibility to know\x01",
            "when to withdraw from operations, yet I can't\x01",
            "help but feel like this was just laziness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E3")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FB7")

    ChrTalk(
        0x8,
        (
            "We've had an influx of tourists returning to\x01",
            "their home countries... Can't it be over already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This sucks. Everyone's been having fun\x01",
            "at the Anniversary Festival, and I'm stuck\x01",
            "in the middle of nowhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E3")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_107A")
    OP_4B(0x8, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x8,
        "Here's your passport. Everything checks out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please wait a little while longer while\x01",
            "we open the gate for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Hmm, okay. I'll go call my wife, then.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_16E3")

    label("loc_107A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1150")

    ChrTalk(
        0x8,
        "Phew. I think I survived rush hour...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My whole life, I've heard people talk about how\x01",
            "straightforward and solemn the Erebonian people\x01",
            "are, but I guess they also love festivals.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11D6")

    label("loc_1150")


    ChrTalk(
        0x8,
        (
            "Now that the Anniversary Festival is finally here,\x01",
            "I just want Erebonians and Calvardians to come\x01",
            "and get along with each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D6")

    Jump("loc_16E3")

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_146B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1351")

    ChrTalk(
        0x8,
        (
            "Whew, I think the inspection line is\x01",
            "starting to thin out now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's been a lot more tourists traveling on\x01",
            "foot this year. I wonder why. If they took the\x01",
            "train, they'd already be in the city by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, they ARE going to a festival. Maybe\x01",
            "they think it's more exciting to change things\x01",
            "up, even their means of transportation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1466")

    label("loc_1351")


    ChrTalk(
        0x8,
        (
            "There's been a lot more tourists traveling on\x01",
            "foot this year. I wonder why. If they took the\x01",
            "train, they'd already be in the city by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, they ARE going to a festival. Maybe\x01",
            "they think it's more exciting to change things\x01",
            "up, even their means of transportation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1466")

    Jump("loc_16E3")

    label("loc_146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154E")

    ChrTalk(
        0x8,
        (
            "Buses that travel to the Empire are\x01",
            "few and far between.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not surprised, given how expansive their\x01",
            "railway network is. Coming to Crossbell is\x01",
            "way more convenient when traveling by train.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15E9")

    label("loc_154E")


    ChrTalk(
        0x8,
        (
            "Buses that travel to the Empire are few\x01",
            "and far between...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but during the Anniversary Festival, the\x01",
            "bus service offers routes there and back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E9")

    Jump("loc_16E3")

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_16E3")

    ChrTalk(
        0x8,
        (
            "After passing that measly gate, you'll hit the\x01",
            "Erebonian border in a matter of seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't even have a thick iron door protecting\x01",
            "us from the Empire. Just a tiny strip of metal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Honestly, it makes me want to laugh.\x02",
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F9")
    TalkEnd(0x16)
    Jump("loc_16FC")

    label("loc_16F9")

    TalkEnd(0x8)

    label("loc_16FC")

    Return()

    # Function_9_BAF end

    def Function_10_16FD(): pass

    label("Function_10_16FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_19B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C3")

    ChrTalk(
        0xFE,
        (
            "Between you and me...I'm actually aiming\x01",
            "to become the CGF commander someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no doubt that I can run this place\x01",
            "better than that insensitive, old buffoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FLet's forget about the commander for a sec.\x01",
            "You realize you gotta beat out Mireille and\x01",
            "the deputy commander to do that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Darn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You may have a point. I was so focused\x01",
            "on the commander that I forgot about the\x01",
            "competition.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19B4")

    label("loc_18C3")


    ChrTalk(
        0xFE,
        (
            "I swear, one day I'll become the commander\x01",
            "and lead the Guardian Force to greatness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And as for Deputy Commander Baelz...I'm\x01",
            "sure I'll outshine her somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWell, I like your spunk, but you\x01",
            "got a loooong way to go, kid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B4")

    Jump("loc_228C")

    label("loc_19B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A82")

    ChrTalk(
        0xFE,
        (
            "Ah, that's right... You guys stole our thunder\x01",
            "and finished the investigation of those ruins...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it. If I was the commander, I would\x01",
            "have never given the order to withdraw!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_1A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBE")

    ChrTalk(
        0xFE,
        (
            "I was coerced into joining the scouting team\x01",
            "looking into those ruins... Say what you want,\x01",
            "but there's something wrong with that place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I wanted to, I doubt we would have\x01",
            "been able to properly scout it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0501FSo there really is something going\x01",
            "on with the ruins...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C4C")

    label("loc_1BBE")


    ChrTalk(
        0xFE,
        (
            "I genuinely can't describe how eerie\x01",
            "those ruins were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's something different about it,\x01",
            "but hey, you can go look for yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4C")

    Jump("loc_228C")

    label("loc_1C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CB2")

    ChrTalk(
        0xFE,
        (
            "No illegal goods, no signs of tampering...\x01",
            "Yeah, this cargo looks good to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_1CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CF0")

    ChrTalk(
        0xFE,
        "There's so many people coming and going...\x02",
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D37")

    ChrTalk(
        0xFE,
        (
            "As of now, I don't have anything\x01",
            "unusual to report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_1D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E5B")

    ChrTalk(
        0xFE,
        (
            "Since yesterday, traffic coming through\x01",
            "the gate has increased exponentially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I'm sure that international\x01",
            "spies and the like have managed to slip into\x01",
            "Crossbell through the cracks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only I could brush that aside and simply\x01",
            "go on with my day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")

    ChrTalk(
        0xFE,
        (
            "By law, it's our job to inspect people coming\x01",
            "and going through the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the railway still exists, and there\x01",
            "usually aren't inspections at the station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet there are agents from both the Empire\x01",
            "and the Republic pouring into Crossbell\x01",
            "every day, and we can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_207E")

    label("loc_1FA9")


    ChrTalk(
        0xFE,
        (
            "As things stand, international agents can\x01",
            "sneak into Crossbell without a care in the\x01",
            "world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, the 'inspections' we conduct\x01",
            "here are nothing more than performances to\x01",
            "keep the public happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207E")

    Jump("loc_228C")

    label("loc_2083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_228C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B4")

    ChrTalk(
        0xFE,
        (
            "State law prohibits Crossbell from having a\x01",
            "proper military like other nations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The brass tells us that's to protect us from\x01",
            "potential conflict with the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why we're called a self-defense force\x01",
            "and not a legitimate military organization.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_228C")

    label("loc_21B4")


    ChrTalk(
        0xFE,
        (
            "Don't mistake me, though. We're all elites\x01",
            "and follow a harsh training regimen, despite\x01",
            "how our organization may look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And it bugs me to no end that all we can do is\x01",
            "stick to self-defense and nothing more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228C")

    TalkEnd(0xFE)
    Return()

    # Function_10_16FD end

    def Function_11_2290(): pass

    label("Function_11_2290")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2324")
    Jump("loc_236E")

    label("loc_2324")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2344")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_236E")

    label("loc_2344")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2364")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_236E")

    label("loc_2364")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_236E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_256B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0xFE,
        (
            "Believe it or not, when I confessed to\x01",
            "Stella, she didn't turn me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her entire response was just,\x01",
            "'We can give it a try, sure.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really excited about it, and my nerves\x01",
            "aren't getting the best of me, surprisingly\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2566")

    label("loc_24A0")


    ChrTalk(
        0xFE,
        (
            "I mean, she says we're just 'trying'\x01",
            "for now, but even getting that far with\x01",
            "Stella makes me incredibly happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, I'm going to focus\x01",
            "on earning Stella's love and affection!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2566")

    Jump("loc_3145")

    label("loc_256B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267E")

    ChrTalk(
        0xFE,
        (
            "I've finally made my decision. After\x01",
            "wrapping up all my work today,\x01",
            "Operation Heartthrob is a go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHave fun, but prepare for the\x01",
            "heartbreak, my friend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to get my heart broken...\x01",
            "Stop spouting that ominous nonsense!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2736")

    label("loc_267E")


    ChrTalk(
        0xFE,
        (
            "If I were to go on a date with Stella,\x01",
            "where would we go...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Mishelam should be relatively\x01",
            "empty, now that the festival's over...\x01",
            "This might be the perfect time to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_3145")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_27F7")

    ChrTalk(
        0xFE,
        (
            "Stella has had more free time since\x01",
            "the Anniversary Festival has ended.\x01",
            "*sigh* She's so wonderful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Staring at her day in, day out isn't\x01",
            "going to get me anywhere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_27F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_28D8")

    ChrTalk(
        0xFE,
        (
            "I've got so much to do today that\x01",
            "I don't have any time to admire\x01",
            "Stella from a safe distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you can't fight on an empty\x01",
            "stomach! I better grab myself a big\x01",
            "meal before I start the day's work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_28D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A11")

    ChrTalk(
        0xFE,
        (
            "Stella gave me some extra food\x01",
            "again today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that she did the same for every\x01",
            "other guardsman doesn't matter... Her\x01",
            "kindness touched me all the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My dearest Stella, you are the most\x01",
            "kind, wonderful, and amazing woman\x01",
            "I've ever had the pleasure of meeting...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A86")

    label("loc_2A11")


    ChrTalk(
        0xFE,
        (
            "My dearest Stella, you are the most\x01",
            "kind, wonderful, and amazing woman\x01",
            "I've ever had the pleasure of meeting...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A86")

    Jump("loc_3145")

    label("loc_2A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA4")

    ChrTalk(
        0xFE,
        (
            "Yesterday, Stella put a little bit\x01",
            "of extra fruit on my plate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is she trying to send me a message?!\x01",
            "Something like, 'Do your best today,\x01",
            "okay? ㈱'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI'm pretty sure she does that for\x01",
            "everyone, dude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't a man dream, Randy...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C2A")

    label("loc_2BA4")


    ChrTalk(
        0xFE,
        (
            "Be that as it may...it still shows\x01",
            "how caring Stella is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, then, I plan to savor every\x01",
            "bite of this love-filled gesture!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2A")

    Jump("loc_3145")

    label("loc_2C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(
        0xFE,
        (
            "I swear, Stella glows when she works\x01",
            "behind that counter... She's angelic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right! After I finish eating, I'll have\x01",
            "to match her enthusiasm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_2CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D90")

    ChrTalk(
        0xFE,
        (
            "Bellguard Gate doesn't have the nicest\x01",
            "atmosphere thanks to our commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By contrast, that clear sweetness\x01",
            "and compassion Stella shows\x01",
            "is really refreshing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3145")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3145")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3025")

    ChrTalk(
        0xFE,
        "I want to get closer to her, if I can...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Randy, you may have crawled back to\x01",
            "Bellguard Gate...but I won't hand Stella\x01",
            "over to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHahaha! Dude, what are you on about?\x02\x03",
            "You were stationed here long before\x01",
            "I joined, but you never tried your luck\x01",
            "with her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "G-Guh... I've been meticulously clearing\x01",
            "away the obstacles standing between us,\x01",
            "I'll have you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHaha! Well, good luck with that, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(It sounds like Randy was on good\x01",
            "terms with most of the guardsmen...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Indeed. I thought that more people would\x01",
            "be at his throat, given that he was fired\x01",
            "for his womanizing ways.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3145")

    label("loc_3025")


    ChrTalk(
        0xFE,
        (
            "When my greatest rival, Randy, was stationed\x01",
            "here, I lost track of how many times he stole\x01",
            "my chances to talk to Stella...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But joke's on you! Now that you aren't a part\x01",
            "of the CGF, I have all the opportunities in the\x01",
            "world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303F(I never even flirted with her, though...)\x02",
    )

    CloseMessageWindow()

    label("loc_3145")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2290 end

    def Function_12_314D(): pass

    label("Function_12_314D")

    Call(0, 13)
    Return()

    # Function_12_314D end

    def Function_13_3151(): pass

    label("Function_13_3151")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_317C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_317C")
    Call(0, 44)
    Return()

    label("loc_317C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3186")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F08")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_31D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F7")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F03")

    label("loc_31F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320B")
    Jump("loc_3F03")

    label("loc_320B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F03")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_33F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3240")
    Call(0, 14)
    Jump("loc_33EC")

    label("loc_3240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3353")

    ChrTalk(
        0xB,
        (
            "Yesterday evening I was chatting\x01",
            "with Cless, and he suddenly blurted\x01",
            "out, 'Please go out with me!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've never really thought of him in\x01",
            "that way, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I thought this whole thing might\x01",
            "be interesting, so I told him we\x01",
            "could give it a try.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33EC")

    label("loc_3353")


    ChrTalk(
        0xB,
        (
            "I ended up deciding to go out with\x01",
            "Cless, but I just don't get it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ever since then, he's been acting so\x01",
            "depressed... I can't figure him out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EC")

    Jump("loc_3F03")

    label("loc_33F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340D")
    Call(0, 14)
    Jump("loc_34C2")

    label("loc_340D")


    ChrTalk(
        0xB,
        (
            "You know that fork in the road on the\x01",
            "way to the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The police academy is further down that road.\x01",
            "Quite a few people in the CGF Bellguard\x01",
            "division are stationed there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C2")

    Jump("loc_3F03")

    label("loc_34C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3593")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E3")
    Call(0, 14)
    Jump("loc_358E")

    label("loc_34E3")


    ChrTalk(
        0xB,
        (
            "Hello, everyone. Would you like\x01",
            "something to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The gate receives emergency dispatches\x01",
            "quite often, so you have to eat your fill\x01",
            "whenever you have the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358E")

    Jump("loc_3F03")

    label("loc_3593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3627")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AF")
    Call(0, 14)
    Jump("loc_3622")

    label("loc_35AF")


    ChrTalk(
        0xB,
        "It's awfully busy today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, I probably won't have time to add\x01",
            "anything extra to the soldiers' meals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3622")

    Jump("loc_3F03")

    label("loc_3627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_36F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3643")
    Call(0, 14)
    Jump("loc_36ED")

    label("loc_3643")


    ChrTalk(
        0xB,
        (
            "Cless has been acting REALLY strange\x01",
            "ever since yesterday. Every time I see\x01",
            "him, he's all smiles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe I'll try putting some thigh\x01",
            "cutlets in his next meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36ED")

    Jump("loc_3F03")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370E")
    Call(0, 14)
    Jump("loc_38D2")

    label("loc_370E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3843")

    ChrTalk(
        0xB,
        (
            "Yesterday, when I put some fruit in the\x01",
            "soldiers' meals as an extra treat, a bunch\x01",
            "of them came and thanked me afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha. I don't see what's wrong with\x01",
            "treating them to something nice every\x01",
            "once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...It's probably going to cut into our\x01",
            "profit margin, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38D2")

    label("loc_3843")


    ChrTalk(
        0xB,
        (
            "I think I can throw the soldiers some extra\x01",
            "treats during the festival. After all, the only\x01",
            "work I have to do is cut up a bunch of fruit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D2")

    Jump("loc_3F03")

    label("loc_38D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F3")
    Call(0, 14)
    Jump("loc_3C87")

    label("loc_38F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A94")

    ChrTalk(
        0xB,
        (
            "Phew, I bet I've burned so many\x01",
            "calories today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The soldiers are probably exhausted, too,\x01",
            "so I'll give them some sweets as a little\x01",
            "morale booster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FDang, nice. Wanna toss me\x01",
            "a few freebies, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Nope. You aren't a CGF soldier\x01",
            "anymore, so I'm not obligated to\x01",
            "give you anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Order something with your own\x01",
            "mira if you're hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FCheapskate.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B2D")

    label("loc_3A94")


    ChrTalk(
        0xB,
        (
            "Hmm, what would be a nice treat\x01",
            "to put in the soldiers' meals...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've heard fruit is good at perking\x01",
            "people up, so I think I'll go with that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2D")

    Jump("loc_3C87")

    label("loc_3B32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3BE2")

    ChrTalk(
        0xB,
        (
            "I know someone like me can't fully\x01",
            "comprehend how important that\x01",
            "key is, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...please try your best to find it,\x01",
            "for the warrant officer's sake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C87")

    label("loc_3BE2")


    ChrTalk(
        0xB,
        (
            "I had to work overtime because the commander\x01",
            "kept coming down for some late night snacks, so\x01",
            "I couldn't recover from my fatigue at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh* Soooo busy.\x02",
    )

    CloseMessageWindow()

    label("loc_3C87")

    Jump("loc_3F03")

    label("loc_3C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA8")
    Call(0, 14)
    Jump("loc_3D32")

    label("loc_3CA8")


    ChrTalk(
        0xB,
        (
            "Welcome, everyone. Feel free to\x01",
            "look at one of our menus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I doubt you'll be too impressed\x01",
            "with our selection of dishes, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D32")

    Jump("loc_3F03")

    label("loc_3D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E57")

    ChrTalk(
        0xB,
        "Welco-- ...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is that you, Randy? Haha, it's been\x01",
            "too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYo. How ya been, Stella?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've been fine. The rest of you are...\x01",
            "the Special Support Section, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, how about you come and eat\x01",
            "something for old times' sake?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 6)
    Jump("loc_3F03")

    label("loc_3E57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6A")
    Call(0, 14)
    Jump("loc_3F03")

    label("loc_3E6A")


    ChrTalk(
        0xB,
        (
            "How about we commemorate our\x01",
            "reunion with a hot meal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, let me warn you in advance:\x01",
            "I don't give discounts to acquaintances\x01",
            "or friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F03")

    Jump("loc_3186")

    label("loc_3F08")

    TalkEnd(0xB)
    Return()

    # Function_13_3151 end

    def Function_14_3F0C(): pass

    label("Function_14_3F0C")


    ChrTalk(
        0xB,
        (
            "I wanted to find a way to reinvigorate\x01",
            "the soldiers, so I decided to hold our\x01",
            "very own hotpot contest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But geez, the meat disappeared before I\x01",
            "could even lay a finger on it... Manual\x01",
            "labor really gets a girl hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why don't you join in on the next hotpot\x01",
            "contest? I can teach you how to\x01",
            "make one, if you're interested.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A0),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x6)
    Return()

    # Function_14_3F0C end

    def Function_15_40DB(): pass

    label("Function_15_40DB")

    Call(0, 16)
    Return()

    # Function_15_40DB end

    def Function_16_40DF(): pass

    label("Function_16_40DF")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5827")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_413D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415D")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5822")

    label("loc_415D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4171")
    Jump("loc_5822")

    label("loc_4171")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5822")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_43B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42EF")

    ChrTalk(
        0xC,
        (
            "It's not hard to imagine the CGF commander\x01",
            "forsaking all the guardsmen if he felt like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What the CGF needs is a leader who takes care\x01",
            "of his subordinates and can foster their potential.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42E7")

    ChrTalk(
        0x10A,
        (
            "#0603FI couldn't agree more.\x02\x03",
            "#0601FTch. Thinking about the brass in the\x01",
            "CPD and CGF gets on my last nerve...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E7")

    SetScenarioFlags(0x0, 4)
    Jump("loc_43AE")

    label("loc_42EF")


    ChrTalk(
        0xC,
        (
            "It's not hard to imagine the CGF commander\x01",
            "forsaking all the guardsmen if he felt like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If he gave one hoot about his subordinates,\x01",
            "Bellguard Gate would be a much nicer place...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AE")

    Jump("loc_5822")

    label("loc_43B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44FA")

    ChrTalk(
        0xC,
        (
            "Now that the Non-Aggression Pact is in\x01",
            "place, Crossbellans have been able to\x01",
            "rest easy, but...is everything really fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All we have are a couple iron gates separating\x01",
            "us from the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Both the Imperial and Republican\x01",
            "armies could steamroll us whenever\x01",
            "they feel like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45C9")

    label("loc_44FA")


    ChrTalk(
        0xC,
        (
            "It'd be nice if Crossbell could stay at peace\x01",
            "due to that Non-Aggression Pact, but I think\x01",
            "that's a bit too optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All we have are a couple iron gates separating\x01",
            "us from the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C9")

    Jump("loc_5822")

    label("loc_45CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_477E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470D")

    ChrTalk(
        0xC,
        (
            "Military enthusiasts like myself are often\x01",
            "misunderstood. We don't ENJOY war by\x01",
            "any stretch of the imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Simply put, we just appreciate the practical\x01",
            "beauty of military equipment and arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Don't go lumping us together with those\x01",
            "sociopaths that adore senseless killing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4779")

    label("loc_470D")


    ChrTalk(
        0xC,
        (
            "A military enthusiast is NOT someone\x01",
            "who enjoys or loves war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Make sure not to mix that up, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_4779")

    Jump("loc_5822")

    label("loc_477E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4932")

    ChrTalk(
        0xC,
        (
            "The current CGF armored car's mobility is\x01",
            "nothing to scoff at. It can take sharp turns\x01",
            "like it's nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Unfortunately, its military excellence pales\x01",
            "in comparison to other countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Empire has their mighty railway guns,\x01",
            "and the technologically advanced Liberl\x01",
            "has their high-speed cruiser, the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Having no countermeasures to such powerful\x01",
            "weapons is Crossbell's fatal flaw.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A99")

    label("loc_4932")


    ChrTalk(
        0xC,
        (
            "No matter how amazing our weapons may be,\x01",
            "if our armored cars were attacked by an airship,\x01",
            "there'd be nothing we could do to fight back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've heard that the CGF's arsenal received quite\x01",
            "the cold reception when they were introduced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Considering Crossbell's situation, it's not\x01",
            "a surprise that we aren't allowed to have\x01",
            "any worthwhile armaments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A99")

    Jump("loc_5822")

    label("loc_4A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE8")

    ChrTalk(
        0xC,
        (
            "Keep this a secret. Stella had me try\x01",
            "the rations that recently came in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...and boy, did that taste awful. Sure,\x01",
            "they may be packed with nutrients,\x01",
            "but I doubt I'd ever eat them again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I have a newfound respect for the\x01",
            "soldiers that have to eat that stuff\x01",
            "on all of their field drills.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CAF")

    label("loc_4BE8")


    ChrTalk(
        0xC,
        (
            "Anyway, those rations were so bad,\x01",
            "I thought I was going to keel over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nutrients are important and all, sure,\x01",
            "but don't you think you should be able\x01",
            "to take them without wanting to hurl?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CAF")

    Jump("loc_5822")

    label("loc_4CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E37")

    ChrTalk(
        0xC,
        (
            "I'm always hearing the soldiers complain\x01",
            "about that commander of theirs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hey, I can't blame them. I hate that\x01",
            "high-and-mighty attitude of his, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If he at least knew how to hold a rifle properly,\x01",
            "maybe he'd be bearable, but the only thing he's\x01",
            "good at is barking out orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FW-Well, isn't that what a commander's\x01",
            "supposed to do...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EF0")

    label("loc_4E37")


    ChrTalk(
        0xC,
        (
            "What kind of commanding officer doesn't\x01",
            "know how to properly use the weapons\x01",
            "that his men and women carry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Everyone's complaints about the commander\x01",
            "are all valid in my eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF0")

    Jump("loc_5822")

    label("loc_4EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_52DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509C")

    ChrTalk(
        0xC,
        (
            "With all this talk of the Anniversary Festival,\x01",
            "I was reminded that the Empire likes to have\x01",
            "their army entertain the citizenry occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Parades, public drills... I bet even a tasting\x01",
            "party with army rations would end up being\x01",
            "a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That stuff is mainly used to build up trust\x01",
            "with the people. *sigh* It sure would be\x01",
            "swell if the CGF did the same thing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5173")

    label("loc_509C")


    ChrTalk(
        0xC,
        (
            "I think Bellguard Gate should take a page\x01",
            "out of the Imperial Army's book...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The only problem is that dang commander.\x01",
            "Even if the idea was proposed, he'd strike it\x01",
            "down in a flash, calling it meaningless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5173")

    Jump("loc_52D8")

    label("loc_5178")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_526A")

    ChrTalk(
        0xC,
        (
            "Last night, I passed by the commander\x01",
            "on my way down from the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And if I'm not mistaken, he was twirling\x01",
            "a keychain as he passed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The armored car's key might have been\x01",
            "on it, now that I think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D8")

    label("loc_526A")


    ChrTalk(
        0xC,
        "Hmm, it's definitely not under the counter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Guests? Feel free to relax\x01",
            "for as long as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D8")

    Jump("loc_5822")

    label("loc_52DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5533")

    ChrTalk(
        0xC,
        (
            "Crossbell Guardian Force weapons\x01",
            "are basically split into two types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You have your stun halberds, which\x01",
            "are used for close combat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...and then you have your assault\x01",
            "rifles for long-range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mastering both of them is a necessity\x01",
            "for any soldier of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You know, I heard a rumor saying that\x01",
            "Randy used to be the best of the best in\x01",
            "the CGF when it came to stun halberds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FLet's leave old stories in the past, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, but it's true. I saw you fight during\x01",
            "combat drills, and I could hardly ever\x01",
            "follow along. You were so fast...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_560F")

    label("loc_5533")


    ChrTalk(
        0xC,
        (
            "Stun halberds and assault rifles are\x01",
            "both hard to handle, but they sure\x01",
            "pack a punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And let me tell you, I've never seen\x01",
            "someone handle a stun halberd like\x01",
            "Randy there does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "He's downright incredible...\x02",
    )

    CloseMessageWindow()

    label("loc_560F")

    Jump("loc_5822")

    label("loc_5614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5755")

    ChrTalk(
        0xC,
        (
            "I'm what you might call a military enthusiast.\x01",
            "Soldiers, weaponry, tanks... I can't get enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Unfortunately for me, the CGF is pretty conservative\x01",
            "with their large-scale drills 'cause they don't want to\x01",
            "set off any false alarms in the Empire or Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It sure is a shame...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5822")

    label("loc_5755")


    ChrTalk(
        0xC,
        (
            "Well, I guess I can't complain too much.\x01",
            "Being able to watch all their combat drills\x01",
            "has been pretty great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I still want to be able to see their armored\x01",
            "cars and orbal cannons in action someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5822")

    Jump("loc_40EC")

    label("loc_5827")

    TalkEnd(0xC)
    Return()

    # Function_16_40DF end

    def Function_17_582B(): pass

    label("Function_17_582B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58BF")
    Jump("loc_5909")

    label("loc_58BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58DF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5909")

    label("loc_58DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58FF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5909")

    label("loc_58FF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5909")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC7")

    ChrTalk(
        0xFE,
        (
            "News broke that some men in black suits\x01",
            "met the CGF commander in secret. Some\x01",
            "even said they looked like mafiosos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the recent disturbances around\x01",
            "Crossbell, we barely have any free time. I'm\x01",
            "starting to get a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, this place's commander isn't\x01",
            "here, and it's impossible to reach him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess this was just another fool's errand...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5B3F")

    label("loc_5AC7")


    ChrTalk(
        0xFE,
        "Guess this was just another fool's errand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well, time to head on back to Crossbell\x01",
            "City if he's not in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_582B end

    def Function_18_5B47(): pass

    label("Function_18_5B47")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BDB")
    Jump("loc_5C25")

    label("loc_5BDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C25")

    label("loc_5BFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C1B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C25")

    label("loc_5C1B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C25")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5D0C")

    ChrTalk(
        0xFE,
        (
            "I've gone through this gate more times\x01",
            "than I can count, but I don't think I've\x01",
            "once seen the CGF commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I can sympathize with how\x01",
            "most of the soldiers here feel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D0C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_5B47 end

    def Function_19_5D14(): pass

    label("Function_19_5D14")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DA8")
    Jump("loc_5DF2")

    label("loc_5DA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5DC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DF2")

    label("loc_5DC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DF2")

    label("loc_5DE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Mmmmm, this is good stuff...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I arrived earlier than expected, so I\x01",
            "decided to kill time with a light meal.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_5D14 end

    def Function_20_5E94(): pass

    label("Function_20_5E94")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I drive my orbal car to the Empire and\x01",
            "back all the time. The inspections can\x01",
            "get pretty annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, my car is still better suited for business\x01",
            "trips than the bus or train. I suppose I can live\x01",
            "with a few inspections every now and then.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_5E94 end

    def Function_21_5F96(): pass

    label("Function_21_5F96")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My entry inspection is finally over. That\x01",
            "long queue was hard to wait in, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, off to Crossbell City now.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_5F96 end

    def Function_22_601A(): pass

    label("Function_22_601A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60AE")
    Jump("loc_60F8")

    label("loc_60AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F8")

    label("loc_60CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F8")

    label("loc_60EE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60F8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I have some business to take care of at\x01",
            "Mishelam during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... Well, it's on the closing day, so\x01",
            "I'll take my time savoring what I can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_601A end

    def Function_23_61C6(): pass

    label("Function_23_61C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_625A")
    Jump("loc_62A4")

    label("loc_625A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_627A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62A4")

    label("loc_627A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_629A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62A4")

    label("loc_629A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "My husband decided to bring me along\x01",
            "to the special party he attends annually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hohoho. He seems to be up to the brim\x01",
            "with confidence, so I'm looking forward\x01",
            "to this new experience.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_61C6 end

    def Function_24_6390(): pass

    label("Function_24_6390")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Huh? Where'd she go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I even told her to wait here while I\x01",
            "grabbed a quick bite to eat...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_6390 end

    def Function_25_63FA(): pass

    label("Function_25_63FA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_648E")
    Jump("loc_64D8")

    label("loc_648E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_64D8")

    label("loc_64AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_64D8")

    label("loc_64CE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64D8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "It looks like I still have some time\x01",
            "before the next bus arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My stomach's growling, too... Yeah,\x01",
            "I'm going to get some food real quick.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_63FA end

    def Function_26_659C(): pass

    label("Function_26_659C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6630")
    Jump("loc_667A")

    label("loc_6630")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6650")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_667A")

    label("loc_6650")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6670")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_667A")

    label("loc_6670")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_667A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I'm waiting for my husband to wrap\x01",
            "up the departure inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had wanted to savor the Anniversary\x01",
            "Festival a little while longer, but he wasn't\x01",
            "able to take any more vacation days.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_659C end

    def Function_27_676A(): pass

    label("Function_27_676A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival? Why would I\x01",
            "care about that? I just came to sell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once I've finished doing my business,\x01",
            "I intend to hurry on home.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_676A end

    def Function_28_6808(): pass

    label("Function_28_6808")

    TalkBegin(0xFE)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x19,
        (
            "Honey, do you mind waiting here while\x01",
            "I deal with the departure inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "All right, darling. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But remember, I despise waiting,\x01",
            "so make it quick, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_6808 end

    def Function_29_68CA(): pass

    label("Function_29_68CA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, this is definitely going to take\x01",
            "some time. Coming before it got dark\x01",
            "ended up being the right call, after all.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_68CA end

    def Function_30_694B(): pass

    label("Function_30_694B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ummm...where exactly do I get\x01",
            "my passport checked?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_694B end

    def Function_31_698A(): pass

    label("Function_31_698A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A1E")
    Jump("loc_6A68")

    label("loc_6A1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A68")

    label("loc_6A3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A68")

    label("loc_6A5E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A68")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hmph. This Guardian Force has\x01",
            "a public mess hall, does it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The idea repulses me, but I guess\x01",
            "I have to endure it in order to get\x01",
            "a meal.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_698A end

    def Function_32_6B28(): pass

    label("Function_32_6B28")

    TalkBegin(0xFE)
    OP_52(0x1F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x1F, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BBF")
    Jump("loc_6C09")

    label("loc_6BBF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BDF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C09")

    label("loc_6BDF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BFF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C09")

    label("loc_6BFF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C09")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Now, now. Take some time to\x01",
            "breathe between bites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are plenty of buses to and\x01",
            "from the city, so we don't need to\x01",
            "rush.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_6B28 end

    def Function_33_6CBD(): pass

    label("Function_33_6CBD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*munch* *munch* Mmmmm...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_6CBD end

    def Function_34_6CE2(): pass

    label("Function_34_6CE2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hehehe... I got my hands on\x01",
            "many valuables while I was\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I return to Erebonia,\x01",
            "I'll sell them and make a killing!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_6CE2 end

    def Function_35_6D7A(): pass

    label("Function_35_6D7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2D")

    ChrTalk(
        0xFE,
        "*sluuuuurp* *munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*crunch* *munch* *slurp*...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aaaaah!\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E6B")
    Jump("loc_6EB5")

    label("loc_6E6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EB5")

    label("loc_6E8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EAB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EB5")

    label("loc_6EAB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EB5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Didn't your mom teach you\x01",
            "not to stare at people when\x01",
            "they're eating?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_70A9")

    label("loc_6F2D")


    ChrTalk(
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FDE")
    Jump("loc_7028")

    label("loc_6FDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FFE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7028")

    label("loc_6FFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_701E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7028")

    label("loc_701E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7028")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Do you need something? And\x01",
            "didn't I tell you to stop staring at\x01",
            "people while they eat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_6D7A end

    def Function_36_70B1(): pass

    label("Function_36_70B1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder what's under\x01",
            "that blue tarp...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_70B1 end

    def Function_37_70F4(): pass

    label("Function_37_70F4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, I should hurry and move out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to miss even a second of\x01",
            "this year's Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_70F4 end

    def Function_38_716E(): pass

    label("Function_38_716E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7286")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Randy, everyone, thank you for everything\x01",
            "you did today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we ever have any trouble again, I'll make\x01",
            "sure to submit a request to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we're experiencing a lull in\x01",
            "tourists, now's a better time than\x01",
            "any to move the car.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    Jump("loc_72E7")

    label("loc_7286")


    ChrTalk(
        0xFE,
        (
            "Now that we're experiencing low tide,\x01",
            "I should go ahead and move the car\x01",
            "while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E7")

    TalkEnd(0xFE)
    Return()

    # Function_38_716E end

    def Function_39_72EB(): pass

    label("Function_39_72EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7392")

    ChrTalk(
        0xFE,
        (
            "Whenever I go on sightseeing trips,\x01",
            "I always have to check out the local\x01",
            "cuisine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what sort of food awaits me in\x01",
            "Crossbell...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7467")

    label("loc_7392")


    ChrTalk(
        0xFE,
        (
            "A self-proclaimed food connoisseur like myself\x01",
            "can't wait to try everything it has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever I talk about my passion, I\x01",
            "can't help but get hungry. Maybe I should\x01",
            "order something while I'm here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7467")

    TalkEnd(0xFE)
    Return()

    # Function_39_72EB end

    def Function_40_746B(): pass

    label("Function_40_746B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Past this point is the Crossbell Guardian Force freight line.\x01",
            "Unauthorized entry is strictly prohibited.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_746B end

    def Function_41_750F(): pass

    label("Function_41_750F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757F")

    ChrTalk(
        0xFE,
        "Where the heck am I...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever. While I'm here,\x01",
            "I might as well explore!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_75D3")

    label("loc_757F")


    ChrTalk(
        0xFE,
        (
            "I'm completely lost, but I'm not going\x01",
            "to let it get me down. Time to explore!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D3")

    TalkEnd(0xFE)
    Return()

    # Function_41_750F end

    def Function_42_75D7(): pass

    label("Function_42_75D7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-6540, 1000, 4160, 0)
    MoveCamera(314, 35, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(37720, 0)
    SetChrPos(0x101, 14000, 0, -2300, 270)
    SetChrPos(0x102, 15300, 0, -1200, 270)
    SetChrPos(0x103, 17900, 0, -1200, 270)
    SetChrPos(0x104, 16600, 0, -2300, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    OP_68(13390, 1000, 690, 8000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    SetChrFlags(0x9, 0x80)
    OP_68(11350, 1500, -3170, 0)
    MoveCamera(254, 22, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(17830, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_770B():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_770B)

    def lambda_7725():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7725)

    def lambda_773F():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_773F)

    def lambda_7759():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7759)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7799():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7799)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#11P#0005FWhat in the world is this...?\x02",
    )

    CloseMessageWindow()

    def lambda_77D7():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77D7)
    Sleep(100)

    def lambda_77E7():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_77E7)
    Sleep(100)

    def lambda_77F7():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77F7)
    Sleep(100)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#6P#0305FHuh. Was this here the other day?\x02\x03",
            "#0309FLet's take a lil' peek, shall we...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_786F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_786F)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x102,
        "#11P#0105FRandy, is something wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_78CF():
        TurnDirection(0xFE, 0x102, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78CF)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#6P#0301FThis thing is...one of the CGF's\x01",
            "armored cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0205FWhy is it here...?\x02\x03",
            "On top of that, they went so far as\x01",
            "to conceal it with this tarp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FThey sure did a shoddy job.\x02\x03",
            "A tarp like that makes it clear as\x01",
            "day that it's hidin' somethin' fishy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FNow that we're at Bellguard Gate,\x01",
            "maybe we should take care of that\x01",
            "support request.\x02\x03",
            "#0001FMaybe this armored car has\x01",
            "something to do with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI believe that the request was\x01",
            "to search for a lost item.\x02\x03",
            "#0200FAnd as for the client...it was a\x01",
            "Warrant Officer Mireille?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_7B97")

    ChrTalk(
        0x101,
        (
            "#11P#0005FMireille... She was that blonde\x01",
            "soldier we met before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0304FYup, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C75")

    label("loc_7B97")


    ChrTalk(
        0x101,
        "#11P#0005FRandy, have you heard of her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FYeah. I worked alongside Mireille\x01",
            "back when I was in the CGF.\x02\x03",
            "#0304FBack then, she was still just a\x01",
            "sergeant major, but she moved up in\x01",
            "the ranks pretty quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C75")


    ChrTalk(
        0x102,
        (
            "#12P#0100FShe may be busy with work, but\x01",
            "we should try asking her about\x01",
            "the request.\x02\x03",
            "Perhaps you could casually bring\x01",
            "up the armored car, if you're so\x01",
            "interested in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FGood idea.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x0, 7260, 0, -2410, 192)
    OP_29(0x19, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_42_75D7 end

    def Function_43_7D6B(): pass

    label("Function_43_7D6B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrChipByIndex(0x28, 0x1E)
    SetChrSubChip(0x28, 0x0)
    OP_68(11350, 1500, -3170, 0)
    MoveCamera(253, 22, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(17830, 0)
    SetChrPos(0x101, 8000, 0, -2300, 192)
    SetChrPos(0x102, 9300, 0, -1200, 192)
    SetChrPos(0x103, 11900, 0, -1200, 192)
    SetChrPos(0x104, 10600, 0, -2300, 192)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0001FSo, according to Mireille, the commander\x01",
            "parked the car here, and it hasn't been\x01",
            "moved since.\x02\x03",
            "#0003FI'd say we should search the area for the\x01",
            "key, but I assume the CGF would have\x01",
            "found it if it was actually here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FThat's a good point. It would be a waste\x01",
            "of time to search the area again.\x02\x03",
            "#0103FBesides, since the car has those bulky\x01",
            "vulcan cannons on top, we can't exactly\x01",
            "remove the tarp to take a closer look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FDamn. I kinda wanted to see this baby\x01",
            "in all its glory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FRandy, have you ridden in an armored\x01",
            "car like this before?\x02\x03",
            "I am curious as to whether the suspension\x01",
            "has been improved from earlier models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300FYup, and I'm wonderin' about the same thing.\x02\x03",
            "#0309FIf they got permission to use 'em, I'm sure\x01",
            "they'd be super nice for patrols and stuff like\x01",
            "that. Noel would die of happiness, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0009FHaha, I think you might be right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_81B3():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81B3)
    Sleep(100)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#11P#0005FHuh, it looks like we have visitors\x01",
            "from the Empire.\x02\x03",
            "#0000FLet's go check it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-12310, 1000, -1110, 0)
    MoveCamera(333, 29, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24260, 0)
    SetChrPos(0x101, 8000, 0, -4300, 0)
    SetChrPos(0x102, 9300, 0, -4300, 0)
    SetChrPos(0x103, 11900, 0, -4300, 0)
    SetChrPos(0x104, 10600, 0, -4300, 0)
    ClearChrFlags(0x29, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x29)
    OP_D3(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x29, -33000, 0, 1000, 0)
    OP_70(0x9, 0x0)
    OP_74(0x9, 0x1E)
    OP_0D()
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_82FD():
        OP_98(0xFE, 0x36B0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_82FD)
    Sound(456, 0, 100, 0)
    WaitChrThread(0x29, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    Sleep(500)
    OP_71(0x6, 0x0, 0x8C, 0x0, 0x0)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)
    Sound(472, 0, 100, 0)
    OP_68(10280, 1000, -1250, 8000)
    MoveCamera(358, 39, 0, 8000)
    OP_6E(470, 8000)
    SetCameraDistance(24260, 8000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_83A3():
        OP_98(0xFE, 0x6D60, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_83A3)
    SetMessageWindowPos(350, 0, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#0306F#10AWhoa, a limo? Those Erebonians must\x01",
            "sure like ridin' in style.\x02",
        )
    )

    Sleep(2000)
    SetMessageWindowPos(350, 40, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#0200F#10AIt appears to be a Reinford Company\x01",
            "limousine. Custom-made as well.\x02",
        )
    )

    Sleep(2000)
    SetMessageWindowPos(310, 0, -1, -1)

    AnonymousTalk(
        0x101,
        "#0005F#10AWho owns this...?\x02",
    )

    Sleep(1000)
    Sound(456, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(310, 40, -1, -1)

    AnonymousTalk(
        0x102,
        "#0105F#10A(Wait a second...)\x02",
    )

    Sleep(2000)
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x29, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_6F(0x79)
    Fade(500)
    OP_68(9340, 1000, -2690, 0)
    MoveCamera(244, 24, 2, 0)
    OP_6E(470, 0)
    SetCameraDistance(20640, 0)
    OP_0D()
    SetMessageWindowPos(200, 250, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "Oh, if it isn't the fine ladies and gentlemen\x01",
            "of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_71(0x9, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x28, 9740, 0, 0, 180)

    def lambda_8638():
        OP_95(0xFE, 9740, 0, -1430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_8638)

    def lambda_8652():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_8652)
    WaitChrThread(0x28, 1)

    ChrTalk(
        0x28,
        (
            "#12P#2800FGood day, everyone. I trust that\x01",
            "Crossbell has been treating you well?\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5P#0105FUncle Dieter...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FIt's been a while, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2800FHahaha, it has indeed. You'll have to\x01",
            "forgive me. Did my arrival get in the\x01",
            "way of your duties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FNot at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FAs always, you can't help but feel\x01",
            "energized by that aura of his...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FAre you returning from a business\x01",
            "trip by any chance, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2800FThat's right. Negotiations in the Empire.\x02\x03",
            "#2803FNow, if you don't mind me asking...\x02\x03",
            "#2801F...what exactly is that giant thing sitting\x01",
            "behind you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#5P#0011FI guess it's hard to not notice.\x01",
            "It's kind of a long story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2803FI see... Allow me to make an educated\x01",
            "guess, then.\x02\x03",
            "#2800FCorrect me if I'm wrong, but it must be\x01",
            "one of the CGF's new armored cars or\x01",
            "something like that, right?\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5P#0105FH-How did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2804FHaha, did I catch you off guard? There's a\x01",
            "simple explanation, I assure you.\x02\x03",
            "#2800FYou see, at the party I attended yesterday,\x01",
            "I ran into the CGF commander.\x02\x03",
            "He, in his drunkenness, mentioned\x01",
            "something about that very car to one\x01",
            "of his subordinates, I believe.\x02\x03",
            "#2806FI've sat with him at multiple parties now,\x01",
            "and I really do think he should work on\x01",
            "that drinking problem of his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThat answers that.\x02\x03",
            "You must have left for the Empire\x01",
            "directly after the party, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FAnd if that's the case, you might\x01",
            "have the clue we're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#12P#2805FHmm? What exactly do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FAllow me to explain...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The SSS informed Dieter of the situation\x01",
            "and their support request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x28,
        (
            "#12P#2800FI think I'm starting to understand.\x02\x03",
            "No wonder the CGF left a weapon like this\x01",
            "in the middle of pedestrian view.\x02\x03",
            "#2803FHowever, I'm afraid I won't be of much\x01",
            "help to you all.\x02\x03",
            "Like I said earlier, I had negotiations in\x01",
            "the Empire today, so I had to leave the\x01",
            "party early in order to make it on time.\x02\x03",
            "#2800FIn other words, by the time the\x01",
            "commander made it back to Bellguard\x01",
            "Gate, I was already long gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FGeez, what a bummer...\x02\x03",
            "#0301FGuess all we can do is stick to\x01",
            "retracin' his steps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2803FThis may be presumptuous of me\x01",
            "to ask, but...\x02\x03",
            "#2800F...can I give you a piece of advice I\x01",
            "was given by Bell a long time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FMariabell gave YOU advice...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2803FAgain, it was many, many years ago,\x01",
            "but I had the habit of losing things.\x02\x03",
            "#2800FI would carry random things around\x01",
            "and, no matter the item, always forget\x01",
            "where I put them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105FReally? I would have never guessed\x01",
            "that, judging by how you act now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2804FHaha, even I was a disorganized\x01",
            "young man at one point.\x02\x03",
            "#2800FAnyway, every time I would lose\x01",
            "something, Bell would always be\x01",
            "there to find it for me.\x02\x03",
            "And each time, she would let out\x01",
            "a great, big sigh and tell me this...\x02\x03",
            "#2806F'Father, how many times do I need to tell\x01",
            "you? When you lose something, you have\x01",
            "to look where you'd least expect it to be.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FSearch the unexpected places...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FWell, I s'pose that makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2804FIn short, Bell was simply trying to tell\x01",
            "me to change my perspective.\x02\x03",
            "#2800FThough I don't know how useful you\x01",
            "all will find this advice, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FNo, sir. We appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "#12P#2804FHaha, I'm happy to have helped.\x02\x03",
            "#2805FOh, dear. I seem to have gotten\x01",
            "carried away with our conversation.\x02\x03",
            "#2800FI think my car might be a bit of a\x01",
            "nuisance, sitting in the middle of\x01",
            "the gate like this.\x02\x03",
            "If you'll excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FOh! Have a safe drive home, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FThank you, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        "#12P#2800FUntil we meet again, SSS.\x02",
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x12C)

    def lambda_95F7():
        OP_95(0xFE, 9740, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_95F7)

    def lambda_9611():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9611)
    WaitChrThread(0x28, 1)
    SetChrFlags(0x28, 0x80)
    OP_71(0x9, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    Sleep(1000)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x9)
    Sound(457, 0, 100, 0)
    OP_68(21180, 1000, 100, 4000)
    MoveCamera(320, 33, 2, 4000)
    OP_6E(470, 4000)
    SetCameraDistance(21510, 4000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_968F():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_968F)

    def lambda_96A9():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96A9)

    def lambda_96B6():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96B6)

    def lambda_96C3():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_96C3)

    def lambda_96D0():
        OP_93(0xFE, 0x5A, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_96D0)
    OP_6F(0x79)
    WaitChrThread(0x29, 1)
    Fade(500)
    OP_68(10320, 900, -2290, 0)
    MoveCamera(244, 25, 2, 0)
    OP_6E(470, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 11200, 0, 100, 90)
    SetChrPos(0x102, 10600, 0, -1500, 90)
    SetChrPos(0x103, 10600, 0, -700, 90)
    SetChrPos(0x104, 11200, 0, -2300, 90)
    OP_0D()

    ChrTalk(
        0x104,
        "#5P#0304FNever changes, that guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYou know, he gave us some pretty\x01",
            "valuable advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FChange our perspective, huh?\x02\x03",
            "#0000FThat's definitely something we forgot to\x01",
            "think about. It might be the key to finding\x01",
            "this...er, key.\x02\x03",
            "Now, then, let's keep retracing the\x01",
            "commander's steps and see where that\x01",
            "takes us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI believe Warrant Officer Mireille told us\x01",
            "that after the commander parked the car,\x01",
            "he went to the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FYeah, let's take our investigation there.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 7260, 0, -2410, 192)
    OP_29(0x19, 0x1, 0x3)
    ClearChrFlags(0x29, 0x80)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    OP_65(0x3, 0x1)
    OP_70(0x6, 0x0)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    OP_49()
    OP_D5(0x1E)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_7D6B end

    def Function_44_99AD(): pass

    label("Function_44_99AD")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-104190, 750, 1480, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25670, 0)
    SetChrPos(0x101, -102980, 0, -110, 315)
    SetChrPos(0x102, -102300, 0, 860, 270)
    SetChrPos(0x103, -103100, 0, -1390, 315)
    SetChrPos(0x104, -103380, 0, 1490, 270)
    SetChrPos(0xC, -97850, 0, 5970, 270)
    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xB, 0x104, 0)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#12P#0309FYo, Stella. Keepin' yourself busy?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#5POh, Randy? Funny seeing you here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PWere you wanting to order something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FNot exactly.\x02\x03",
            "We're searching for the armored car's\x01",
            "key, as per Warrant Officer Mireille's\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 300)

    ChrTalk(
        0xB,
        (
            "#5POh, so you guys are the ones who got\x01",
            "stuck with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThe warrant officer already asked me to\x01",
            "look around. I combed over the mess hall\x01",
            "high and low, but it's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI suppose we can mark the mess hall off\x01",
            "our list, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWe are in the process of retracing the\x01",
            "commander's steps.\x02\x03",
            "Do you mind recounting what you\x01",
            "witnessed last night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PSure. I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThe first day of the Anniversary Festival\x01",
            "was incredibly hectic here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI was finally winding down from the craziness\x01",
            "of the day when the commander stormed in\x01",
            "here, utterly wasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAll of a sudden, he yelled at me to cook\x01",
            "something that would sober him up, so\x01",
            "I had to do some forced overtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P*sigh* And it was right after I finished\x01",
            "taking inventory for the night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FHe must act like he owns the place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FOh, yeah, he loves to show people\x01",
            "who's boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FDeputy Commander Baelz is quite\x01",
            "different in that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FExcuse me. Would you know if he had\x01",
            "the key on him while he was eating\x01",
            "his meal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PBeats me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI only heard about it being lost when\x01",
            "I woke up this morning, so I'm afraid\x01",
            "I wasn't really paying attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FIs that so?\x02\x03",
            "#0003FHmm, there's no way of knowing\x01",
            "whether he had the key here or not...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xC,
        (
            "What's everyone doing gathered\x01",
            "around in the mess hall?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-103780, 750, 2029, 2000)
    BeginChrThread(0xC, 3, 0, 45)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0x5A, 0x12C)

    def lambda_A192():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A192)

    def lambda_A19F():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A19F)

    def lambda_A1AC():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1AC)

    def lambda_A1B9():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A1B9)

    def lambda_A1C6():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A1C6)
    WaitChrThread(0xC, 3)

    ChrTalk(
        0xB,
        "#5PGood timing, Beyond.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThese people are helping the CGF\x01",
            "recover that key or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FNice to meet you. We're the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh, yeah. I've heard about you all...\x01",
            "Well, good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FHey, Beyond. Still the same\x01",
            "military buff as always?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PAfraid so. It's been a while, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSo, Beyond, did you end up finding\x01",
            "the key? You know, the one the\x01",
            "warrant officer told us about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 300)

    ChrTalk(
        0xC,
        (
            "#11PAfter giving it a quick search, I can\x01",
            "safely say that it isn't in the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI'm pretty sure the commander didn't\x01",
            "bother heading there after his meal,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FDoes that mean you weren't there last\x01",
            "night?\x02\x03",
            "What makes you sure he didn't go to\x01",
            "the inn?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 300)

    ChrTalk(
        0xC,
        (
            "#11PAround the time he was eating in here,\x01",
            "I went to go take a break up on the roof.\x01",
            "Not long after, he showed up there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PWait. Hold on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0205FDid you remember something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYeah. I passed by him as I was leaving\x01",
            "the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd if I'm not wrong, I remember\x01",
            "him spinning around something\x01",
            "that looked like a keychain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThat must have been the key you\x01",
            "all are looking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#0006FThen that means...\x02\x03",
            "#0001F...it's extremely likely that the commander\x01",
            "had the key when he was on the roof, after\x01",
            "leaving the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FIt bothers me that he would act so\x01",
            "nonchalant with something so important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FI certainly agree, but at least we picked\x01",
            "up a valuable statement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FHaha. Good thing that memory of yours\x01",
            "finally kicked in, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PB-Better late than never, right?\x01",
            "H-Haha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYou have GOT to be kidding me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PDo you realize how much time I wasted\x01",
            "searching the mess hall because of you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xC, 0xB, 300)

    ChrTalk(
        0xC,
        "#11PH-Haha... Sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWell, I think it's about time for me to head\x01",
            "back to work. See ya later, Stella...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A993():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A993)
    WaitChrThread(0xC, 1)

    def lambda_A9B1():
        OP_95(0xFE, -97850, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A9B1)
    WaitChrThread(0xC, 1)
    OP_68(-104190, 750, 1480, 2000)

    ChrTalk(
        0xB,
        "#5PTch. Coward.\x02",
    )

    CloseMessageWindow()

    def lambda_A9F5():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9F5)

    def lambda_AA02():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA02)

    def lambda_AA0F():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA0F)

    def lambda_AA1C():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA1C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#12P#0300FHey, thanks to him, we bagged\x01",
            "ourselves a good lead. Couldn't\x01",
            "have done it without ya, Stella.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 300)

    ChrTalk(
        0x101,
        (
            "#12P#0000FRandy's right. Even though you only knew it\x01",
            "wasn't in the mess hall, that narrowed down\x01",
            "our list of potential hiding places by a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHmm, you're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI actually had no idea how important\x01",
            "that key was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYou have to find it. Not just for the CGF's\x01",
            "sake, but for Warrant Officer Mireille's, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FWe'll do our best. I promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FNow, is our next destination the roof?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -101240, 0, -30, 90)
    SetChrPos(0xC, -162110, 0, -2500, 90)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_29(0x19, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_99AD end

    def Function_45_ACA5(): pass

    label("Function_45_ACA5")


    def lambda_ACAA():
        OP_95(0xFE, -103000, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_ACAA)
    WaitChrThread(0xC, 1)

    def lambda_ACC8():
        OP_95(0xFE, -103000, 0, 3500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_ACC8)
    WaitChrThread(0xC, 1)
    Return()

    # Function_45_ACA5 end

    SaveToFile()

Try(main)
