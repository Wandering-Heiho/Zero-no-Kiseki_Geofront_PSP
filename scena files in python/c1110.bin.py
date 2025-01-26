from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1110.bin",                # FileName
        "c1110",                    # MapName
        "c1110",                    # Location
        0x0017,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1110",                  # 0
        "Receptionist Shion",     # 1
        "Chief Clipp",            # 2
        "Secretary Ernest",       # 3
        "Mayor MacDowell",        # 4
        "Officer Franz",          # 5
        "City Hall Staffer",      # 6
        "City Hall Staffer",      # 7
        "City Hall Staffer",      # 8
        "Reins",                  # 9
        "Grace",                  # 10
        "Purple-Haired Girl",     # 11
        "Freight Company Staff",  # 12
        "Freight Company Staff",  # 13
        "Speaker Hartmann",       # 14
        "Representative",         # 15
        "Representative",         # 16
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch02300.itc",                   # 03
        "chr/ch05802.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch28100.itc",                   # 06
        "chr/ch28200.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch06000.itc",                   # 09
        "chr/ch05200.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
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

    DeclNpc(0,       0,       7400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3529,    4000,    16209,   315,  261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-44990,  250,     14710,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-13510,  4000,    14529,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4429,   0,       4460,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2670,    0,       -1090,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1730,    0,       5389,    315,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       5159,    360,  389,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.0,                   3.5,                   0.0,                   517.5625,              [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3076923191547394,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -1.076923131942749,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 19,  -6.400000095367432,    16.75,                 4.0,                   3136.0,                [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.4571428894996643,    -2.09375,              -0.800000011920929,    1.0])

    DeclActor(0,       0,       6000,    1500,    0,       1500,    7460,    0x007E, 0,  5,  0x0000)
    DeclActor(-44940,  0,       13190,   1500,    -44990,  1500,    14710,   0x007E, 0,  9,  0x0000)
    DeclActor(-8100,   4000,    19780,   1500,    -8100,   5500,    19780,   0x007C, 0,  36, 0x0000)
    DeclActor(8000,    4120,    19640,   1500,    8000,    5520,    19640,   0x007C, 0,  37, 0x0000)

    ScpFunction((
        "Function_0_4B4",          # 00, 0
        "Function_1_56C",          # 01, 1
        "Function_2_597",          # 02, 2
        "Function_3_5C2",          # 03, 3
        "Function_4_8E1",          # 04, 4
        "Function_5_AE4",          # 05, 5
        "Function_6_AE8",          # 06, 6
        "Function_7_34E9",         # 07, 7
        "Function_8_528A",         # 08, 8
        "Function_9_5646",         # 09, 9
        "Function_10_564A",        # 0A, 10
        "Function_11_6BEB",        # 0B, 11
        "Function_12_6C95",        # 0C, 12
        "Function_13_6FF7",        # 0D, 13
        "Function_14_7086",        # 0E, 14
        "Function_15_70F6",        # 0F, 15
        "Function_16_728A",        # 10, 16
        "Function_17_76BB",        # 11, 17
        "Function_18_96E6",        # 12, 18
        "Function_19_A306",        # 13, 19
        "Function_20_AC9B",        # 14, 20
        "Function_21_ACFC",        # 15, 21
        "Function_22_ADB2",        # 16, 22
        "Function_23_AE35",        # 17, 23
        "Function_24_BDF9",        # 18, 24
        "Function_25_C4E5",        # 19, 25
        "Function_26_CAAB",        # 1A, 26
        "Function_27_D39B",        # 1B, 27
        "Function_28_D674",        # 1C, 28
        "Function_29_DE79",        # 1D, 29
        "Function_30_E674",        # 1E, 30
        "Function_31_FD3D",        # 1F, 31
        "Function_32_FD7C",        # 20, 32
        "Function_33_10DFE",       # 21, 33
        "Function_34_10E21",       # 22, 34
        "Function_35_10E4A",       # 23, 35
        "Function_36_10ED6",       # 24, 36
        "Function_37_11173",       # 25, 37
    ))


    def Function_0_4B4(): pass

    label("Function_0_4B4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4F4"),
        (1, "loc_500"),
        (2, "loc_50C"),
        (3, "loc_518"),
        (4, "loc_524"),
        (5, "loc_530"),
        (6, "loc_53C"),
        (SWITCH_DEFAULT, "loc_548"),
    )


    label("loc_4F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_500")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_50C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_518")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_524")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_530")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_548")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_554")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_56B")

    Return()

    # Function_0_4B4 end

    def Function_1_56C(): pass

    label("Function_1_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_596")
    OP_94(0xFE, 0x193C, 0x3B1A, 0x672, 0x41BE, 0x3E8)
    Sleep(300)
    Jump("Function_1_56C")

    label("loc_596")

    Return()

    # Function_1_56C end

    def Function_2_597(): pass

    label("Function_2_597")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C1")
    OP_94(0xFE, 0xFFFFEB74, 0x37FA, 0xFFFFF5F6, 0x43EE, 0x3E8)
    Sleep(300)
    Jump("Function_2_597")

    label("loc_5C1")

    Return()

    # Function_2_597 end

    def Function_3_5C2(): pass

    label("Function_3_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5EC")
    SetChrPos(0x9, -46210, 0, 12030, 0)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_611")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_61F")
    Jump("loc_8B6")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_632")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8B6")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_645")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_68C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -1820, 4000, 17030, 225)
    SetChrPos(0xD, -3170, 4000, 16140, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_6F7")

    label("loc_68C")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 3830, 4000, 18150, 0)
    SetChrPos(0xD, -5310, 4000, 15540, 225)
    SetChrPos(0xE, -6700, 4000, 14240, 45)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6F7")
    SetChrPos(0x9, 4870, 4000, 17950, 180)

    label("loc_6F7")

    Jump("loc_8B6")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_721")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_74B")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7B0")
    SetChrPos(0xF, -5160, 4000, 16030, 90)
    SetChrPos(0x9, -3740, 4000, 16030, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -6520, 4000, 15440, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x9, -46210, 0, 12030, 0)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_815")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -5160, 4000, 16030, 90)
    SetChrPos(0x9, -3740, 4000, 16030, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_823")
    Jump("loc_8B6")

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_842")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    TurnDirection(0x8, 0x11, 0)
    Jump("loc_8B6")

    label("loc_842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_850")
    Jump("loc_8B6")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85E")
    Jump("loc_8B6")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_86C")
    Jump("loc_8B6")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_87A")
    Jump("loc_8B6")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_89F")
    SetChrPos(0x9, -4070, 4000, 16180, 180)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_8B6")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8AD")
    Jump("loc_8B6")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8B6")

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    ClearChrFlags(0x12, 0x80)
    Event(0, 25)

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_8E0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)

    label("loc_8E0")

    Return()

    # Function_3_5C2 end

    def Function_4_8E1(): pass

    label("Function_4_8E1")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_8F3")
    Jump("loc_8FC")

    label("loc_8F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8FC")

    label("loc_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_90E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_96D")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_92E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_93C")
    Jump("loc_96D")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_94E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_960")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_96D")
    OP_66(0x1, 0x1)

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_997")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997")
    SetMapObjFrame(0xFF, "model06", 0x0, 0x1)

    label("loc_997")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B0")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    Jump("loc_9B6")

    label("loc_9B0")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9E9")

    label("loc_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9E9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9E9")

    label("loc_9E9")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A05")
    OP_1B(0x2, 0x0, 0x23)

    label("loc_A05")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A28")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_A28")

    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4C")
    SetMapObjFlags(0x3, 0x4)

    label("loc_A4C")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A64")
    Jump("loc_AE3")

    label("loc_A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A7E")
    Jump("loc_AE3")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 7)), scpexpr(EXPR_END)), "loc_A91")
    OP_1B(0x1, 0x0, 0x17)
    Jump("loc_AE3")

    label("loc_A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB0")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_AE3")

    label("loc_AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_ACB")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_AE3")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 6)), scpexpr(EXPR_END)), "loc_AE3")
    ModifyEventFlags(1, 0, 0x80)
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_AE3")

    Return()

    # Function_4_8E1 end

    def Function_5_AE4(): pass

    label("Function_5_AE4")

    Call(0, 6)
    Return()

    # Function_5_AE4 end

    def Function_6_AE8(): pass

    label("Function_6_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFE")
    Call(0, 24)
    Jump("loc_34E8")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B44")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C")
    Call(0, 26)
    Jump("loc_B3F")

    label("loc_B3C")

    Call(0, 27)

    label("loc_B3F")

    Jump("loc_34E8")

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Call(0, 29)
    Jump("loc_34E8")

    label("loc_B84")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D15")

    ChrTalk(
        0x8,
        "Thank you so much for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You said you call yourselves the 'Special\x01",
            "Support Section'? Do you help citizens with\x01",
            "requests, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, either way. You've ended up being\x01",
            "an enormous help. Truly, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHaha, no problem.\x01",
            "(It's embarrassing to hear her praise.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FShould you need help again,\x01",
            "please don't hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DF7")

    label("loc_D15")


    ChrTalk(
        0x8,
        "Thank you so much for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You said you call yourselves the\x01",
            "'Special Support Section'?\x01",
            "Do you help citizens with requests, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, either way. You've ended up being\x01",
            "an enormous help. Truly, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF7")

    Jump("loc_34E5")

    label("loc_DFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECF")

    ChrTalk(
        0x8,
        (
            "Please report back to me after you've\x01",
            "inspected the three vacant residencies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll want to double-check the contents of\x01",
            "the documents, as they may contain mistakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1029")

    ChrTalk(
        0x8,
        "The diet has finally adjourned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Employees of Financial Affairs can\x01",
            "finally go home and get some\x01",
            "much-needed rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The mayor, on the other hand, is\x01",
            "working late into the night again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's busy consolidating all of the\x01",
            "documents from the diet's budget session.\x01",
            "I'm concerned he'll overwork himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A2")

    label("loc_1029")


    ChrTalk(
        0x8,
        "The mayor's working late into the night again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm worried he's pushing himself too hard\x01",
            "to complete his work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A2")

    Jump("loc_34E5")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1321")

    ChrTalk(
        0x8,
        (
            "We've been getting flooded with complaints\x01",
            "about the airport lockdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The CPD has instructed us to stay quiet\x01",
            "on the issue and, when asked, tell people\x01",
            "that it's due to extensive inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know how much longer we'll\x01",
            "be able to hold out for.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1277")
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
        "#0005F(I wonder what's actually happening at the airport.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1319")

    label("loc_1277")


    ChrTalk(
        0x103,
        (
            "#0203F('Extensive inspection' sounds more like a\x01",
            "smokescreen than an explanation.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(I feel bad for them. You know how people\x01",
            "behave over delays.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1319")

    SetScenarioFlags(0x0, 0)
    Jump("loc_13AE")

    label("loc_1321")


    ChrTalk(
        0x8,
        (
            "We've been getting flooded with complaints\x01",
            "about the airport lockdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know how much longer we'll\x01",
            "be able to hold out for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AE")

    Jump("loc_34E5")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159C")

    ChrTalk(
        0x8,
        (
            "Another day, another chaotic\x01",
            "diet meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* How will they ever face the citizens\x01",
            "of Crossbell if they keep this up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Their terrible attitudes cause them to\x01",
            "bait each other into screaming matches\x01",
            "every thirty seconds.\x02",
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
            "#0303F(You couldn't pay me to sit there and\x01",
            "watch that.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(It pains me to see our diet in such a\x01",
            "sorry state.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1620")

    label("loc_159C")


    ChrTalk(
        0x8,
        (
            "Another day, another chaotic\x01",
            "diet meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* How will they ever face the citizens\x01",
            "of Crossbell if they keep this up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1620")

    Jump("loc_34E5")

    label("loc_1625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1936")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(
        0x8,
        (
            "You've found Crossbell City Hall's\x01",
            "reception. How may I help you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16C5")

    ChrTalk(
        0x8,
        "So you've returned.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F4")

    label("loc_16C5")


    ChrTalk(
        0x8,
        "Excuse me, you're police officers, right?\x02",
    )

    CloseMessageWindow()

    label("loc_16F4")


    ChrTalk(
        0x8,
        (
            "I thought you might have been\x01",
            "another person here to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FIs it normal to receive complaints?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, the diet's budget session is\x01",
            "supposed to be wrapped up, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're neck-deep into arguing,\x01",
            "so they still haven't reached a consensus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The meeting has been extended for\x01",
            "several days as a result of their actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Same old diet...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1931")

    label("loc_1879")


    ChrTalk(
        0x8,
        (
            "They've extended the diet meeting\x01",
            "yet again, so the new budget will\x01",
            "be delayed as a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel bad for Crossbellans alike.\x01",
            "They're the ones that suffer the consequences.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1931")

    Jump("loc_34E5")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1CEC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19C0")

    ChrTalk(
        0x8,
        "I appreciate your help, everybody.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow me to extend you my utmost\x01",
            "gratitude on behalf of City Hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE7")

    label("loc_19C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(
        0x8,
        (
            "You managed to buy the mayor's\x01",
            "favorite drink, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He'll be thrilled to hear it. Why don't\x01",
            "you all go and break him the good news?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE7")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1B2A")

    ChrTalk(
        0x8,
        "You said the stall relocated?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My apologies, I haven't got a clue as to\x01",
            "where it could have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's safe to assume that they're\x01",
            "still in the city, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE7")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(
        0x8,
        (
            "You should be able to find the mayor's\x01",
            "favorite drink at the juice stall right\x01",
            "by the fountain outside of these doors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a normal menu item, so you'll\x01",
            "have to ask them about it directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must feel like a chore to you,\x01",
            "but I really appreciate the assistance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE7")

    label("loc_1C56")


    ChrTalk(
        0x8,
        (
            "The diet is assembling tomorrow\x01",
            "to begin their budget session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Members of the media will be in\x01",
            "attendance, so it's bound to be lively.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE7")

    Jump("loc_34E5")

    label("loc_1CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2E")

    ChrTalk(
        0x8,
        (
            "The closing ceremony is being held\x01",
            "at 5:00PM today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're anticipating the venue will reach\x01",
            "its maximum capacity. I'm sure we're all\x01",
            "going to be packed in there like sardines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll also be broadcasting the speech out\x01",
            "to the plaza for anybody that wasn't able\x01",
            "to enter the venue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F1C")

    label("loc_1E2E")


    ChrTalk(
        0x8,
        (
            "We're anticipating the venue will reach\x01",
            "its maximum capacity. I'm sure we're all\x01",
            "going to be packed in there like sardines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll also be broadcasting the speech out\x01",
            "to the plaza for anybody that wasn't able\x01",
            "to enter the venue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1C")

    Jump("loc_34E5")

    label("loc_1F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1FE8")

    ChrTalk(
        0x8,
        (
            "How fortunate of us to be able to\x01",
            "experience another successful parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Phew... Thank Aidios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm just glad that all citizens of Crossbell\x01",
            "were able to enjoy themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_1FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2083")

    ChrTalk(
        0x8,
        "It's about time for the parade to start...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* I'll be praying that we don't\x01",
            "run into any issues this time around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20DB")

    label("loc_2083")


    ChrTalk(
        0x8,
        (
            "We haven't had a year without something\x01",
            "regarding the parade going horribly wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    Jump("loc_34E5")

    label("loc_20E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2189")

    ChrTalk(
        0x8,
        (
            "You were required to register beforehand\x01",
            "to attend today's symposium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We regret to inform you that we\x01",
            "are no longer accepting any\x01",
            "registrations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_2189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2314")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228D")

    ChrTalk(
        0x8,
        (
            "I'm distributing informational brochures\x01",
            "regarding the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It contains information about the festival\x01",
            "schedule, the parade route, and the\x01",
            "stalls present during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Feel free to take one for yourselves.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_230F")

    label("loc_228D")


    ChrTalk(
        0x8,
        (
            "I'm distributing informational brochures\x01",
            "regarding the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're free, so feel free to take one\x01",
            "for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230F")

    Jump("loc_34E5")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(
        0x8,
        (
            "Oh, you're back already. Were you\x01",
            "able to complete the task?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FYes, it wasn't too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FIt did end up bein' kinda annoying, though.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "I'm not sure what you're referring to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, you're welcome to hold on to\x01",
            "the key in case you intend on returning\x01",
            "to the Geofront.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That way, you won't need to ask\x01",
            "me every time you want to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThanks, we'll take you up on the offer.\x02\x03",
            "#0003F(I can't help it, but I'm worried about Jona.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 2)
    Jump("loc_2653")

    label("loc_2526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B2")

    ChrTalk(
        0x8,
        "My apologies for all of the commotion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're rehearsing for the opening ceremony\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2653")

    label("loc_25B2")


    ChrTalk(
        0x8,
        (
            "They're rehearsing for the opening ceremony\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bear in mind that civilians are currently\x01",
            "prohibited from entering City Hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2653")

    Jump("loc_34E5")

    label("loc_2658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_270C")

    ChrTalk(
        0x8,
        (
            "The entrance to the Geofront's B Sector can be\x01",
            "found near the Residential District's waterway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be careful with that key. We've lost it a few\x01",
            "times already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_270C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(
        0x8,
        (
            "They're rehearsing for the opening ceremony\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bear in mind that civilians are currently\x01",
            "prohibited from entering City Hall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_287D")

    label("loc_27C8")


    ChrTalk(
        0x8,
        (
            "Actually, aren't they going over the parade's\x01",
            "security protocol with the CPD, as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Phew... I feel like I'm neck-deep in work\x01",
            "due to Anniversary Festival preparations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287D")

    Jump("loc_34E5")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_290A")

    ChrTalk(
        0x8,
        (
            "*sigh* These Crossbell Times reporters'\x01",
            "persistence is fearsome. It's like they're\x01",
            "trying their hardest to annoy us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_290A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A15")

    ChrTalk(
        0x8,
        (
            "We'll be celebrating Crossbell State's 70th\x01",
            "birthday with a festival next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The festival is being extended to five days\x01",
            "to celebrate this momentous occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please refer to our informational brochures\x01",
            "for more details.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2AAE")

    label("loc_2A15")


    ChrTalk(
        0x8,
        (
            "We'll be celebrating Crossbell State's 70th\x01",
            "birthday with a festival next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please refer to our informational brochures\x01",
            "for more details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAE")

    Jump("loc_34E5")

    label("loc_2AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCB")

    ChrTalk(
        0x8,
        (
            "Next month marks 70 years since\x01",
            "Crossbell State's founding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We plan to open a variety of attractions\x01",
            "for tourists during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll be publishing more details in\x01",
            "the city newsletter, so do keep your\x01",
            "eyes peeled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FWe have a newsletter? News to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Yes, there are informational brochures\x01",
            "right by reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We update it monthly, so it's a shame it\x01",
            "doesn't stand out. Your reaction is a\x01",
            "testament to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(Guilty as charged...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D86")

    label("loc_2CCB")


    ChrTalk(
        0x8,
        (
            "I know it's relatively unknown, but sheesh.\x01",
            "It still hurts having it rubbed in my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'd love to do something to raise awareness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Poor lady. I feel bad for her.)\x02",
    )

    CloseMessageWindow()

    label("loc_2D86")

    Jump("loc_34E5")

    label("loc_2D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_2EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E67")

    ChrTalk(
        0x8,
        (
            "We had the Transportation Division run out\x01",
            "to check up on one of the orbal buses\x01",
            "we lost contact with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What could cause communications to\x01",
            "cut out? I'm a little worried, admittedly...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2EC0")

    label("loc_2E67")


    ChrTalk(
        0x8,
        (
            "We run into the occasional problem with\x01",
            "our buses, but I hope it's nothing serious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC0")

    Jump("loc_34E5")

    label("loc_2EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2FD2")

    ChrTalk(
        0x8,
        "Welcome to the Crossbell City Hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're here to inquire about the hours\x01",
            "of operation for our orbal bus service,\x01",
            "then you've come to the right place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The service itself is under the jurisdiction\x01",
            "of the Transportation Division, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E5")

    label("loc_2FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_31E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")

    ChrTalk(
        0x8,
        (
            "Allow me to give you a rundown\x01",
            "of this fine establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "There are two facilities within City Hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The reception hall is to your left, and the\x01",
            "Crossbell Diet building to your right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most people are familiar with the\x01",
            "reception hall, thanks to all of the\x01",
            "special events we hold there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31E1")

    label("loc_311F")


    ChrTalk(
        0x8,
        (
            "The reception hall is to your left, and the\x01",
            "Crossbell Diet building to your right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most people are familiar with the\x01",
            "reception hall, thanks to all of the\x01",
            "special events we hold there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E1")

    Jump("loc_34E5")

    label("loc_31E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3304")

    ChrTalk(
        0x8,
        "Welcome to the Crossbell City Hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're here to pay your utilities or to change\x01",
            "your address, you've come to the right place.\x01",
            "Feel free to inquire about additional services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Haha... Looks like she's got her work\x01",
            "cut out for her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3390")

    label("loc_3304")


    ChrTalk(
        0x8,
        "Welcome to the Crossbell City Hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have you come to pay your utility bills\x01",
            "or change your address? I can help\x01",
            "take care of that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_34E5")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341F")

    ChrTalk(
        0x8,
        "Is that girl from earlier going to be okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope so... I referred her to those seedy\x01",
            "downtown apartments...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_34E5")

    label("loc_341F")


    ChrTalk(
        0x8,
        (
            "A lady with purple hair asked me where\x01",
            "she could find a cheap apartment\x01",
            "to rent a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Is she going to be fine? I ended up\x01",
            "referring her to those seedy\x01",
            "downtown apartments...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E5")

    TalkEnd(0x8)

    label("loc_34E8")

    Return()

    # Function_6_AE8 end

    def Function_7_34E9(): pass

    label("Function_7_34E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350A")
    Call(0, 30)
    Return()

    label("loc_350A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3600")

    ChrTalk(
        0xFE,
        "At long last, the budget session is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor said he'd be working overtime\x01",
            "to draft up the documents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It brings me great pain to idly sit by\x01",
            "while he works himself to the bone.\x01",
            "I think I'll give him a hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_3600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_375D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3692")

    ChrTalk(
        0xFE,
        (
            "The mayor has been tirelessly working\x01",
            "overtime for a little while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope the budget is finalized today.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3758")

    label("loc_3692")


    ChrTalk(
        0xFE,
        (
            "The mayor has been tirelessly working\x01",
            "overtime for a little while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's getting up there in years, so I fear\x01",
            "what might happen to his health, should\x01",
            "he continue to work so recklessly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3758")

    Jump("loc_5286")

    label("loc_375D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_38F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3877")

    ChrTalk(
        0xFE,
        (
            "Members of the staff are working hard\x01",
            "to prepare for the Q&A session following\x01",
            "the diet meeting's adjournment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There's not a moment's rest for any of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our department has plenty of free time\x01",
            "because all we do is maintain the equipment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38EE")

    label("loc_3877")


    ChrTalk(
        0xFE,
        "I feel a little bad for them. I really do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The least I can do for them is\x01",
            "clean the corridors one more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38EE")

    Jump("loc_5286")

    label("loc_38F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D5")

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell is preoccupied\x01",
            "with the diet, if you're looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things got pretty heated yesterday,\x01",
            "so they weren't able to decide on the budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Poor Mayor MacDowell.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A28")

    label("loc_39D5")


    ChrTalk(
        0xFE,
        (
            "I'm worried about his health.\x01",
            "Hopefully, he isn't pushing himself too hard...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A28")

    Jump("loc_5286")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4025")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3AD4")

    ChrTalk(
        0xFE,
        (
            "The mayor's been a huge fan of bitter\x01",
            "tomatoes for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's definitely an acquired taste, though.\x01",
            "I can't stand the stuff.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B38")

    ChrTalk(
        0xFE,
        (
            "I inadvertently end up holding my breath\x01",
            "when Speaker Hartmann is around.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3B38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE2")

    ChrTalk(
        0xFE,
        (
            "Could I get everyone's attention, please?!\x01",
            "The Saint's Prayer statue has been returned!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This statue is the symbol of City Hall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone stole it during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kind folks over at the First Division\x01",
            "managed to recover it for us the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* What a relief. We would have\x01",
            "looked incompetent to our foreign\x01",
            "counterparts had it not been found.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DA8")

    label("loc_3CE2")


    ChrTalk(
        0xFE,
        (
            "Bless Aidios for having returned\x01",
            "the Saint's Prayer statue to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel ashamed for allowing it to be stolen.\x01",
            "We showed our foreign counterparts an\x01",
            "embarrassingly incompetent side of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA8")

    Jump("loc_4020")

    label("loc_3DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E90")

    ChrTalk(
        0xFE,
        (
            "Hi, officers. Thank you so much for\x01",
            "helping us out the other day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Saint's Prayer continues to stand tall,\x01",
            "shrouded in all of its majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must not allow it to ever be tampered\x01",
            "with again!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 5)
    Jump("loc_4020")

    label("loc_3E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA2")

    ChrTalk(
        0xFE,
        (
            "I appreciate that Mayor MacDowell treats\x01",
            "all of the staff members with respect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's always calm, but on the other hand...it's\x01",
            "like he never shows what he's struggling with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. Such is the nature of all politicians.\x01",
            "How sad for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4020")

    label("loc_3FA2")


    ChrTalk(
        0xFE,
        (
            "I get the impression that Mayor MacDowell\x01",
            "doesn't reveal his true intentions to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is he hiding something from us?\x02",
    )

    CloseMessageWindow()

    label("loc_4020")

    Jump("loc_5286")

    label("loc_4025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_43CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_415F")

    ChrTalk(
        0xFE,
        (
            "I don't really get it. Regardless,\x01",
            "you've truly saved us from a\x01",
            "difficult situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As much as I'd love to do more for you,\x01",
            "we're swamped with preparations for\x01",
            "the closing ceremony later today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please understand you have our utmost\x01",
            "gratitude. I hope to rely on you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C9")

    label("loc_415F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_430E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_423E")

    ChrTalk(
        0xFE,
        (
            "I can't believe we let this happen during\x01",
            "the closing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please recover the Saint's Prayer as\x01",
            "quickly as you can. I'm begging you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, hurry! Time is of the essence!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4309")

    label("loc_423E")


    ChrTalk(
        0xFE,
        (
            "More and more guests have been entering\x01",
            "the hall since noon. There couldn't have\x01",
            "been a worse time for this to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please recover the Saint's Prayer as\x01",
            "quickly as you can. I'm begging you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4309")

    Jump("loc_43C9")

    label("loc_430E")


    ChrTalk(
        0xFE,
        (
            "I'm freaking out... The mayor is on his\x01",
            "way and is unaware of the situation.\x01",
            "Oh, sweet, merciful Aidios, save us all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(*grumble* Guess we have no choice but\x01",
            "to rely on them...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C9")

    Jump("loc_5286")

    label("loc_43CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_44AE")

    ChrTalk(
        0xFE,
        (
            "The mayor is currently busy\x01",
            "speaking with dignitaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I anticipate he'll be meeting with the\x01",
            "CEO of the IBC, Dieter Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's safe to assume he'll be\x01",
            "returning late at night, again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_44AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4589")

    ChrTalk(
        0xFE,
        (
            "The mayor looks like he's slimmed down\x01",
            "a little. Is he eating properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love for him to take better care of\x01",
            "himself, but I understand that he doesn't\x01",
            "have any time to take a break right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4618")

    ChrTalk(
        0xFE,
        (
            "*sigh* There are way more members of\x01",
            "the media here than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll have to increase the amount of seating.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46EE")

    ChrTalk(
        0xFE,
        (
            "I've been giving Mayor MacDowell\x01",
            "a helping hand with his work, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you know, he recently lost his secretary\x01",
            "in that huge incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's fine. I've got the time to spare, anyway.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_47AD")

    ChrTalk(
        0xFE,
        (
            "I'm glad Ernest is here to take them off\x01",
            "my hands. We'll be able to hold the\x01",
            "hearing without a hitch, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor's so busy that I can't seem\x01",
            "to get a hold of him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_47AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_490F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4892")

    ChrTalk(
        0xFE,
        (
            "Argh, it's almost time for the hearing, and I still\x01",
            "can't get a hold of the mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figured he was probably busy, but now\x01",
            "I'm not so sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Maybe I can get a hold of Mr. Reis...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_490A")

    label("loc_4892")


    ChrTalk(
        0xFE,
        (
            "We can't start the hearing without the mayor's\x01",
            "seal of approval.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Maybe I can get a hold of Mr. Reis...\x02",
    )

    CloseMessageWindow()

    label("loc_490A")

    Jump("loc_5286")

    label("loc_490F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A04")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. Isn't the public hearing\x01",
            "supposed to be tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Preparing the reception hall, sorting out\x01",
            "citizens' appeals... What else is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor plans to attend, so we need\x01",
            "to hold a meeting FOR the meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B35")

    ChrTalk(
        0xFE,
        (
            "Sounds like they're already at each other's\x01",
            "throats over next year's budget...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Members of the media are dying to go to\x01",
            "the diet's budget session Q&A.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Typically, this is when the senior members\x01",
            "of the diet impose their will on the junior\x01",
            "members and take control.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4BA6")

    label("loc_4B35")


    ChrTalk(
        0xFE,
        (
            "If you ask me, this is the time that the\x01",
            "diet should be working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* This is depressing...\x02",
    )

    CloseMessageWindow()

    label("loc_4BA6")

    Jump("loc_5286")

    label("loc_4BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4C51")

    ChrTalk(
        0xFE,
        (
            "The orbal bus wouldn't have broken down\x01",
            "yesterday if it had been properly maintained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's with everyone and their need\x01",
            "to take shortcuts?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_4CE9")

    ChrTalk(
        0xFE,
        (
            "I saw some guy from the Transportation\x01",
            "Division runnin' around like a headless chicken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're overworked. I feel bad for 'em.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4E32")

    ChrTalk(
        0xFE,
        (
            "I appreciate that Crossbell's government\x01",
            "has been putting more effort into expanding\x01",
            "the orbal bus service in recent years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish their intentions were better, though.\x01",
            "They're only doing it to try and become\x01",
            "more popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't complain, though. It's not like\x01",
            "it isn't a valuable part of our lives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5286")

    label("loc_4E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB5")

    ChrTalk(
        0xFE,
        (
            "The hallway on the left leads to the\x01",
            "west wing of City Hall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and this door here is where you can\x01",
            "find the mayor's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Conversely, the other hallway leads to the\x01",
            "east wing, and you can find the speaker's\x01",
            "office behind the door on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both men are important politicians\x01",
            "that hold massive amounts of\x01",
            "influence internationally.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_503F")

    label("loc_4FB5")


    ChrTalk(
        0xFE,
        (
            "Neither the mayor nor speaker are\x01",
            "currently present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're an important part of Crossbellan\x01",
            "politics, so they're always busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503F")

    Jump("loc_5286")

    label("loc_5044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_518D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511A")

    ChrTalk(
        0xFE,
        "I work for General Affairs' second division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm in charge of the diet building\x01",
            "and the reception hall, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm boooored. I'm so bored!\x01",
            "All I do is clean, clean, clean!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5188")

    label("loc_511A")


    ChrTalk(
        0xFE,
        (
            "At least things pick up a bit when\x01",
            "the diet is in session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've usually got a ton of time to spare.\x02",
    )

    CloseMessageWindow()

    label("loc_5188")

    Jump("loc_5286")

    label("loc_518D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_522E")

    ChrTalk(
        0xFE,
        "I think I'll do some cleaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll start with the reception hall\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There's not a lot to do here, you know?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5286")

    label("loc_522E")


    ChrTalk(
        0xFE,
        "Did you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to ask Shion up front\x01",
            "at the counter there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5286")

    TalkEnd(0xFE)
    Return()

    # Function_7_34E9 end

    def Function_8_528A(): pass

    label("Function_8_528A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550D")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xA, 0x9, 0)

    ChrTalk(
        0x9,
        "Here you are, Mr. Reis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2600FThank you, I appreciate it.\x01",
            "I'll be sure to make good use of these.\x02\x03",
            "#2604FOkay, as long as I've got these,\x01",
            "then the public hearing will be...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "#2600FHaha. I've been reading through the\x01",
            "comments and suggestions our\x01",
            "citizens have sent in.\x02\x03",
            "We'll be reading the comments aloud during\x01",
            "the public hearing. I'm excited to watch the\x01",
            "ensuing chaos from our esteemed politicians.\x02\x03",
            "#2603FOkay, I need to consult with the mayor\x01",
            "before the public hearing begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Does Elie still have lingering feelings\x01",
            "towards politics?)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_5642")

    label("loc_550D")


    ChrTalk(
        0xA,
        (
            "#2600FWe've sorted through all of the comments\x01",
            "and suggestions our citizens have sent in.\x02\x03",
            "We'll be reading the comments aloud during\x01",
            "the public hearing. I'm excited to watch the\x01",
            "ensuing chaos from our esteemed politicians.\x02\x03",
            "#2603FOkay, I need to consult with the mayor\x01",
            "before the public hearing begins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5642")

    TalkEnd(0xFE)
    Return()

    # Function_8_528A end

    def Function_9_5646(): pass

    label("Function_9_5646")

    Call(0, 10)
    Return()

    # Function_9_5646 end

    def Function_10_564A(): pass

    label("Function_10_564A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56DE")
    Jump("loc_5728")

    label("loc_56DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56FE")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5728")

    label("loc_56FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_571E")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5728")

    label("loc_571E")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5728")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BC7")
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#2501FYes, prepare them immediately.\x01",
            "I'll arrange the documents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5853")
    Jump("loc_589D")

    label("loc_5853")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5873")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589D")

    label("loc_5873")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5893")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589D")

    label("loc_5893")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589D")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#2500FOh, you're here.\x01",
            "Are you okay? Has something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, not at all. We're in the middle of an\x01",
            "investigation, but we figured we'd drop\x01",
            "by for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAre you all right, Grandfather?\x01",
            "I heard the news about the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2503FAh, yes. The session was prolonged\x01",
            "by three days already.\x02\x03",
            "#2500FWe wasted enough time bickering\x01",
            "over the budget allocation as is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2500FNow, now. No need to feel anxious\x01",
            "about my working habits.\x02\x03",
            "#2503FThere's no need to feel concerned.\x01",
            "It'll all be over soon.\x02\x03",
            "#2500FThis old man can handle himself, so\x01",
            "don't allow it to distract you from\x01",
            "your own tasks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FYes, Grandfather. I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FShall we depart for the hospital, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 5)
    Jump("loc_5C84")

    label("loc_5BC7")

    OP_4B(0x9, 0xFF)
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#2503FSorry, Clipp. I'll need you to contact\x01",
            "Financial Affairs in my stead.\x02\x03",
            "#2500FI will personally deliver the documents to\x01",
            "Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Understood, Mr. Mayor.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_5C84")

    Jump("loc_6BE3")

    label("loc_5C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C97")
    Jump("loc_6BE3")

    label("loc_5C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5CA5")
    Jump("loc_6BE3")

    label("loc_5CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5CB3")
    Jump("loc_6BE3")

    label("loc_5CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_610D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6105")

    ChrTalk(
        0xB,
        (
            "#2509FI'll be able to work through the afternoon\x01",
            "at full capacity, all thanks to this shake.\x02\x03",
            "#2503F*sip* *sip* *sip*\x01",
            "What an absolutely marvelous drink!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6100")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5FE2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC3")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_5E18")

    label("loc_5DC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DF0")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_5E18")

    label("loc_5DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E18")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5E18")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006F(He sure wasn't kidding about loving it...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ED0")

    ChrTalk(
        0x102,
        (
            "#0103F(Leave it up to a battle-hardened\x01",
            "politician like my grandfather to\x01",
            "enjoy a drink like that.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FAA")

    label("loc_5ED0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F45")

    ChrTalk(
        0x103,
        (
            "#0206F(I am unable to process the image my eyes\x01",
            "are perceiving. He has my utmost respect.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FAA")

    label("loc_5F45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FAA")

    ChrTalk(
        0x104,
        (
            "#0303F(He's gulpin' that shake down like it's\x01",
            "nothin'. You gotta respect that.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FAA")


    ChrTalk(
        0x153,
        "#1105F(What do you mean? That stuff's tasty!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_60FD")

    label("loc_5FE2")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6027")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_607C")

    label("loc_6027")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6054")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_607C")

    label("loc_6054")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_607C")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_607C")

    Sleep(1000)

    ChrTalk(
        0x153,
        "#1111F(I'm glad he likes that tasty looking drink.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(D-Do you think we should have tried\x01",
            "some for ourselves?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60FD")

    SetScenarioFlags(0x0, 3)

    label("loc_6100")

    Jump("loc_6108")

    label("loc_6105")

    Call(0, 17)

    label("loc_6108")

    Jump("loc_6BE3")

    label("loc_610D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_611B")
    Jump("loc_6BE3")

    label("loc_611B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6129")
    Jump("loc_6BE3")

    label("loc_6129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6463")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BE")

    ChrTalk(
        0xB,
        (
            "#2503FI have been notified that this year's\x01",
            "parade has been blessed with the\x01",
            "largest crowd in the history of the festival.\x02\x03",
            "#2500FIt is my duty to greet the audience\x01",
            "prior to the parade's commencement.\x01",
            "I must say, I'm a touch nervous, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou're nervous, Mr. Mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou're kiddin', right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F*sigh*\x01",
            "There's no justifiable reason for you to feel\x01",
            "nervous over a casual event like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2509FHahaha... You kids may be on to something.\x02\x03",
            "#2500FThe end of the parade will mark the\x01",
            "end of the festival's main event.\x02\x03",
            "And with that, your work will ease up.\x01",
            "Let us pray the day proceeds smoothly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_645E")

    label("loc_63BE")


    ChrTalk(
        0xB,
        (
            "#2500FThe end of the parade will mark the\x01",
            "end of the festival's main event.\x02\x03",
            "And with that, your work will ease up.\x01",
            "Let us pray the day proceeds smoothly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645E")

    Jump("loc_6BE3")

    label("loc_6463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_66CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E6")

    ChrTalk(
        0xB,
        (
            "#2500FThe symposium being held today\x01",
            "was my idea.\x02\x03",
            "It provides an opportunity for bright minds\x01",
            "to publicly debate Crossbell's adversities.\x02\x03",
            "#2503FI don't intend for it to be a politically charged\x01",
            "debate, and scholars from across the\x01",
            "continent will be in attendance.\x02\x03",
            "#2500FSeventy years of Crossbell's history\x01",
            "will be laid bare for us to introspect upon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_66C9")

    label("loc_65E6")


    ChrTalk(
        0xB,
        (
            "#2500FI am responsible for proposing the idea\x01",
            "of the symposium that is being held today.\x02\x03",
            "It provides the opportunity for bright minds\x01",
            "to publicly debate Crossbell's adversities.\x01",
            "I am positive it will be a meaningful one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C9")

    Jump("loc_6BE3")

    label("loc_66CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE1")

    ChrTalk(
        0xB,
        (
            "#2500FAh, welcome, everyone.\x01",
            "I am pleased to see you again.\x02\x03",
            "#2503FMy most sincere apologies.\x01",
            "I understand it's the Anniversary Festival,\x01",
            "but I have many pressing matters to tend to.\x02\x03",
            "I would have loved to have enjoyed\x01",
            "a meal with you at least once during\x01",
            "this festive period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWe understand, sir. You're the mayor\x01",
            "of Crossbell. None of us are surprised\x01",
            "that you have important duties to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FMore importantly, have you fully\x01",
            "recovered from the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2503FOh, that? That was nothing! I may be old,\x01",
            "but I won't be taken down so easily.\x02\x03",
            "#2501FHeck, this was nothing compared to the\x01",
            "tension between the Empire and Republic\x01",
            "thirty years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FPlease, Grandfather. We'll be stuck\x01",
            "here forever if you start going\x01",
            "into the details.\x02\x03",
            "#0100FI'm sure we'll have plenty more opportunities\x01",
            "in the future to share a meal together.\x02\x03",
            "And, please. Promise me you'll take\x01",
            "better care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2500FI appreciate the concern, Elie.\x01",
            "I will be able to handle myself just fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6BE3")

    label("loc_6AE1")


    ChrTalk(
        0xB,
        (
            "#2500FMy most sincere apologies.\x01",
            "I understand it's the Anniversary Festival,\x01",
            "but I have many pressing matters to tend to.\x02\x03",
            "#2503FI would have loved to engage in conversation\x01",
            "with all of you at least once.\x02\x03",
            "#2500FI'm sure another opportunity will arise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE3")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_10_564A end

    def Function_11_6BEB(): pass

    label("Function_11_6BEB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hi, guys. How are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's symposium will feature\x01",
            "Mayor MacDowell, as well as\x01",
            "foreign dignitaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We've got quite a spectacular line up.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_6BEB end

    def Function_12_6C95(): pass

    label("Function_12_6C95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6E9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DA4")

    ChrTalk(
        0xFE,
        (
            "Oh, thank Aidios! The Saint's Prayer\x01",
            "has been returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops, now's not the time to celebrate.\x01",
            "I'm falling behind on the closing ceremony\x01",
            "preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better hurry it up. I only have\x01",
            "three more hours to take care of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E99")

    label("loc_6DA4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Argh! Why must the mayor be nowhere\x01",
            "to be found at a time like this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xE,
        (
            "We're left with no other choice.\x01",
            "We must continue to proceed with\x01",
            "the preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'll go secure more chairs for the venue!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_6E99")

    Jump("loc_6FF3")

    label("loc_6E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F55")

    ChrTalk(
        0xFE,
        (
            "Could I ask those participating at\x01",
            "the symposium to be patient\x01",
            "for just a little longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will lead you to your seats once\x01",
            "the venue has opened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6FF3")

    label("loc_6F55")


    ChrTalk(
        0xFE,
        (
            "Phew... Looks like we'll be able to\x01",
            "begin the symposium smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm surprised Arios MacLaine showed up.\x01",
            "I feel safe and secure knowing he's here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF3")

    TalkEnd(0xFE)
    Return()

    # Function_12_6C95 end

    def Function_13_6FF7(): pass

    label("Function_13_6FF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_700B")
    Call(0, 12)
    Jump("loc_7082")

    label("loc_700B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7082")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "Shouldn't be much longer until\x01",
            "it begins...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attendees should be arriving\x01",
            "any minute now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7082")

    TalkEnd(0xFE)
    Return()

    # Function_13_6FF7 end

    def Function_14_7086(): pass

    label("Function_14_7086")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "General Affairs' second division is\x01",
            "busy handling an event today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's actually pretty rare.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_7086 end

    def Function_15_70F6(): pass

    label("Function_15_70F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_71D3")

    ChrTalk(
        0xFE,
        (
            "The editor-in-chief has ordered me to\x01",
            "accompany Grace to prevent her\x01",
            "from going too crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She usually ends up abandoning me\x01",
            "so she can sprint off directly to the\x01",
            "source to get her information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7286")

    label("loc_71D3")


    ChrTalk(
        0xFE,
        (
            "Grace is currently trying to gather\x01",
            "information on the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll be okay on her own...\x01",
            "I hope she doesn't try sneaking into\x01",
            "the diet without a permit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7286")

    TalkEnd(0xFE)
    Return()

    # Function_15_70F6 end

    def Function_16_728A(): pass

    label("Function_16_728A")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7360")

    ChrTalk(
        0x11,
        (
            "#2103FWhat's the big idea? I'm Crossbellan.\x01",
            "I pay my taxes!\x02\x03",
            "#2100FNothing wrong with getting the contact\x01",
            "info of the politicians I help finance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I-I don't think it works that way...\x02",
    )

    CloseMessageWindow()
    Jump("loc_76B3")

    label("loc_7360")


    ChrTalk(
        0x11,
        (
            "#2104FC'mon, can't you give me a teensy\x01",
            "bit more info?\x02\x03",
            "#2109FI'm SURE you have all of the diet members'\x01",
            "emergency contacts written down, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm prohibited from disclosing any contact\x01",
            "information, with the exception of the\x01",
            "direct line to their offices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'll have to ask you to leave. Immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2106FOh, come on! Don't be like that!\x02\x03",
            "#2100FCan't you at least hook me up with\x01",
            "their secretary's contact info?\x02\x03",
            "#2109FI'm pretty sure they're also funded by\x01",
            "the taxpayers, so I bet their info's\x01",
            "in that little registry of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "S-Sorry, but I can't entertain your request.\x02",
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
        (
            "#0006F(I feel bad for her. Grace can get pretty\x01",
            "overbearing at times.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Let's leave before she redirects\x01",
            "her attention towards us.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_76B3")

    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_728A end

    def Function_17_76BB(): pass

    label("Function_17_76BB")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch06500.itc", 0x1E)
    LoadChrToIndex("chr/ch27800.itc", 0x1F)
    LoadChrToIndex("chr/ch27400.itc", 0x20)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_68(-45850, 1600, 12420, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21760, 0)
    SetChrPos(0x101, -45750, 0, 10750, 0)
    SetChrPos(0x153, -45000, 0, 12250, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_777D")
    SetChrPos(0x102, -44250, 0, 11500, 0)
    Jump("loc_77C4")

    label("loc_777D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77A3")
    SetChrPos(0x103, -44250, 0, 11500, 0)
    Jump("loc_77C4")

    label("loc_77A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77C4")
    SetChrPos(0x104, -44250, 0, 11500, 0)

    label("loc_77C4")

    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -45000, 120, 3000, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x16, -45750, 120, 1750, 0)
    SetChrPos(0x17, -44250, 120, 2500, 0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrSubChip(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78B3")

    ChrTalk(
        0xB,
        (
            "#5P#2505FYou're here, Elie.\x01",
            "Ah, good to see you, too, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795A")

    label("loc_78B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7908")

    ChrTalk(
        0xB,
        (
            "#5P#2505FIt's good to see you, Lloyd.\x01",
            "Oh, and Tio, was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795A")

    label("loc_7908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_795A")

    ChrTalk(
        0xB,
        (
            "#5P#2505FIt's good to see you, Lloyd.\x01",
            "Oh, and Randy, was it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_795A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A32")

    ChrTalk(
        0x102,
        (
            "#12P#0103FMy apologies, Grandfather.\x01",
            "I've done a poor job of keeping\x01",
            "in contact with you lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FThanks for helping us out. Your blessing\x01",
            "saved us. How will we ever repay you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AB4")

    label("loc_7A32")


    ChrTalk(
        0x101,
        (
            "#6P#0000FIt's been a while, Mr. Mayor.\x02\x03",
            "#0003FThanks for helping us out, your blessing\x01",
            "saved us. How will we ever repay you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AB4")


    ChrTalk(
        0xB,
        (
            "#5P#2503FOh, that? Think nothing of it.\x02\x03",
            "#2500FAll I did was demand a detailed explanation\x01",
            "from any diet member involved with the auction.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7BB1")

    ChrTalk(
        0x102,
        (
            "#12P#0100FThat's not true. You were able to put\x01",
            "a damper on the speaker's actions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9B")

    label("loc_7BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C2F")

    ChrTalk(
        0x103,
        (
            "#12P#0200FI disagree. You were able to serve\x01",
            "as a restraint on the speaker from\x01",
            "acting any further.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9B")

    label("loc_7C2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C9B")

    ChrTalk(
        0x104,
        (
            "#12P#0300FI'm thinkin' you put a stop on the\x01",
            "speaker from actin' unchecked\x01",
            "any longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C9B")


    ChrTalk(
        0x101,
        (
            "#6P#0000FWell, at any rate...\x01",
            "You have our gratitude, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2509FI feel as if your praise is undeserved.\x01",
            "It's the least I could do for saving my life.\x02\x03",
            "#2503FHmm, putting that aside for a moment.\x01",
            "Is this the young lady I've been\x01",
            "hearing all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FAh, yes. Her name's KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1110FNice to meet'cha, Gramps!\x02\x03",
            "#1109FYour face looks cool! It's filled\x01",
            "with white hair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2509FCool...you say?\x01",
            "Hahaha! What an interesting lady!\x02\x03",
            "#2500FShe's bright and cheery, yet she has\x01",
            "a mysterious charm to her.\x02\x03",
            "#2501FAre you looking into her identity?\x01",
            "I heard about the memory loss.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F36")

    ChrTalk(
        0x102,
        "#12P#0103FYes, for the time being.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FC5")

    label("loc_7F36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F89")

    ChrTalk(
        0x103,
        "#12P#0203FYes, we are currently analyzing the situation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FC5")

    label("loc_7F89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FC5")

    ChrTalk(
        0x104,
        "#12P#0306FYep, we're going hard at it.\x02",
    )

    CloseMessageWindow()

    label("loc_7FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_END)), "loc_8020")

    ChrTalk(
        0x101,
        (
            "#6P#0001FWe've requested the Bracer Guild to\x01",
            "aide in the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8081")

    label("loc_8020")


    ChrTalk(
        0x101,
        (
            "#6P#0001FWe intend to request the Bracer Guild's\x01",
            "cooperation in investigating her identity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8081")


    ChrTalk(
        0xB,
        (
            "#5P#2500FHmm, sounds like you're exploring\x01",
            "multiple avenues. Hopefully, your\x01",
            "extended search leads to good results.\x02\x03",
            "#2503FFeel free to consult with me if you\x01",
            "run into any trouble. My door\x01",
            "is always open to all of you.\x02\x03",
            "I may be a worthless old man who is\x01",
            "usually bound to his own obligations...\x02\x03",
            "#2500F...but I don't mean to treat the matter lightly.\x01",
            "I will not overlook the fools that intended\x01",
            "on hurting an innocent child.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8263")

    ChrTalk(
        0x102,
        "#12P#0102FGrandfather...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82CB")

    label("loc_8263")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8294")

    ChrTalk(
        0x103,
        "#12P#0202FMr. Mayor...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82CB")

    label("loc_8294")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82CB")

    ChrTalk(
        0x104,
        "#12P#0302FNicely said, Mr. Mayor.\x02",
    )

    CloseMessageWindow()

    label("loc_82CB")


    ChrTalk(
        0x101,
        (
            "#6P#0004FThanks for the kind words, sir.\x01",
            "I needed the encouragement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1109FYou're pretty cool, Gramps!\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)

    NpcTalk(
        0x15,
        "Man's Voice",
        (
            "May I have a moment of your time,\x01",
            "Mayor MacDowell?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83EF")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_8438")

    label("loc_83EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8416")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_8438")

    label("loc_8416")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8438")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_8438")

    Sleep(1000)

    ChrTalk(
        0xB,
        "#5P#2501FHmm.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-45000, 1500, 9000, 3000)

    def lambda_846A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_846A)
    Sleep(50)

    def lambda_847A():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_847A)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84A7")

    def lambda_849A():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_849A)
    Jump("loc_84E6")

    label("loc_84A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84C9")

    def lambda_84BC():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84BC)
    Jump("loc_84E6")

    label("loc_84C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84E6")

    def lambda_84DE():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84DE)

    label("loc_84E6")


    def lambda_84EB():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_84EB)

    def lambda_8505():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8505)
    Sleep(50)

    def lambda_8519():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8519)

    def lambda_8533():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8533)
    Sleep(50)

    def lambda_8547():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8547)

    def lambda_8561():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8561)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85BA")
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_8617")

    label("loc_85BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85EB")
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_8617")

    label("loc_85EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8617")
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_8617")

    Sleep(1000)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#0005F(Wh-What's he doing here?!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_868A")

    ChrTalk(
        0x102,
        "#11P#0105F(Speaker Hartmann!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8700")

    label("loc_868A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86CD")

    ChrTalk(
        0x103,
        "#11P#0205F(The Imperial Faction leader.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8700")

    label("loc_86CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8700")

    ChrTalk(
        0x104,
        "#11P#0301F(The boss himself?)\x02",
    )

    CloseMessageWindow()

    label("loc_8700")

    OP_68(-45850, 1600, 12420, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8740")

    def lambda_8726():
        OP_97(0x102, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8726)
    Jump("loc_8799")

    label("loc_8740")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_876F")

    def lambda_8755():
        OP_97(0x103, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8755)
    Jump("loc_8799")

    label("loc_876F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8799")

    def lambda_8784():
        OP_97(0x104, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8784)

    label("loc_8799")

    Sleep(50)

    def lambda_87A1():
        OP_97(0x101, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87A1)
    Sleep(50)

    def lambda_87BE():
        OP_97(0x153, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_87BE)

    def lambda_87D8():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_87D8)
    Sleep(50)

    def lambda_87F5():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_87F5)
    Sleep(50)

    def lambda_8812():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8812)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_884D")
    WaitChrThread(0x102, 1)

    def lambda_8840():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8840)
    Jump("loc_8894")

    label("loc_884D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8873")
    WaitChrThread(0x103, 1)

    def lambda_8866():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8866)
    Jump("loc_8894")

    label("loc_8873")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8894")
    WaitChrThread(0x104, 1)

    def lambda_888C():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_888C)

    label("loc_8894")

    WaitChrThread(0x101, 1)

    def lambda_889D():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_889D)
    WaitChrThread(0x153, 1)

    def lambda_88AE():
        OP_93(0x153, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_88AE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0xB,
        (
            "#5P#2500FDo you need something, Hartmann?\x02\x03",
            "As you can see, I'm busy with guests.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x15,
        (
            "My most sincere apologies. I have some\x01",
            "pressing concerns to discuss with you.\x02\x03",
            "I'd like you to reexamine the Imperial\x01",
            "government's proposal.\x02",
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
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#5P#2503FWe already spoke of this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#12P#2703FI understand your point, but I'd like you\x01",
            "to consider my position.\x02\x03",
            "#2702FOr, do you intend to take advantage of\x01",
            "the situation to conspire with Campbell\x01",
            "and his men?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2503FPerish the thought. I have no intention\x01",
            "of siding with the Republican Faction.\x02\x03",
            "#2501FNor do I intend to with the Imperial Faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#12P#2702FFine, then. Let's see you demonstrate\x01",
            "that balanced approach of yours.\x02\x03",
            "#2703FRuining my humble party has been\x01",
            "a detriment for the entire state.\x02\x03",
            "#2700FI'd love to hear your plan to\x01",
            "reverse the damages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2503FIt seems I must have another\x01",
            "discussion with you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5P#2500FI'm sorry, everyone. I know you came all the\x01",
            "way out here to visit me, but I have important\x01",
            "matters to discuss with Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D2F():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D2F)
    Sleep(50)

    def lambda_8D3F():
        TurnDirection(0x153, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8D3F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D66")
    TurnDirection(0x102, 0xB, 500)
    Jump("loc_8D99")

    label("loc_8D66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D82")
    TurnDirection(0x103, 0xB, 500)
    Jump("loc_8D99")

    label("loc_8D82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D99")
    TurnDirection(0x104, 0xB, 500)

    label("loc_8D99")


    ChrTalk(
        0x101,
        (
            "#11P#0005FN-No, it's quite all right. You don't\x01",
            "have to worry yourself about us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E35")

    ChrTalk(
        0x102,
        "#11P#0103FWe'll see you again, Grandfather.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EA6")

    label("loc_8E35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E76")

    ChrTalk(
        0x103,
        "#11P#0203FIf you will excuse us, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EA6")

    label("loc_8E76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EA6")

    ChrTalk(
        0x104,
        "#11P#0300F'Scuse us, then.\x02",
    )

    CloseMessageWindow()

    label("loc_8EA6")


    ChrTalk(
        0x153,
        "#5P#1109FSee you again, Gramps!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(-7040, 5500, 17890, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19810, 0)
    SetChrPos(0x101, -7590, 4000, 19290, 135)
    SetChrPos(0x153, -7450, 4000, 17650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F80")
    SetChrPos(0x102, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_8FC9")

    label("loc_8F80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FA7")
    SetChrPos(0x103, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_8FC9")

    label("loc_8FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FC9")
    SetChrPos(0x104, -6220, 4000, 18950, 270)
    CloseMessageWindow()

    label("loc_8FC9")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0001FThe mayor is stuck between a rock\x01",
            "and a hard place, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90DC")

    ChrTalk(
        0x102,
        (
            "#11P#0101FRight.\x02\x03",
            "It's a scene I've seen countless\x01",
            "times over.\x02\x03",
            "#0108FIt's reprehensible. How can the man\x01",
            "responsible for hosting the Schwarze\x01",
            "Auction be so shameless?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9245")

    label("loc_90DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_915F")

    ChrTalk(
        0x103,
        (
            "#11P#0203FThe speaker is utterly shameless.\x02\x03",
            "#0200FHe opens his home to the Schwarze\x01",
            "Auction, and yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9245")

    label("loc_915F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9245")

    ChrTalk(
        0x104,
        (
            "#11P#0306FY'know, the speaker's a bit pretty\x01",
            "full of it, don'tcha think?\x02\x03",
            "#0301FWhere does he get off puttin' up such a stink\x01",
            "when he runs something like the Schwarze\x01",
            "Auction from the comfort of his own home?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9245")


    ChrTalk(
        0x101,
        (
            "#5P#0001FIt's a testament to his confidence\x01",
            "that the entire situation won't\x01",
            "blow up into a scandal.\x02\x03",
            "#0006FHe's more brutal than the mafia\x01",
            "in some ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1110FHeeey, Lloyd.\x02\x03",
            "Don't you think Gramps is\x01",
            "pretty strong?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_9340():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9340)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9376")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_93CD")

    label("loc_9376")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A4")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_93CD")

    label("loc_93A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93CD")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x104, 0x153, 500)

    label("loc_93CD")

    Sleep(500)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#5P#0005FStrong?\x01",
            "What makes you say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1111FWell, that snobby old guy brought\x01",
            "all of his friends, right?\x02\x03",
            "#1110FDidn't he bring them because he\x01",
            "thought he'd lose if he faced\x01",
            "Gramps alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FWhen you put it that way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9564")

    ChrTalk(
        0x102,
        (
            "#11P#0105FThe speaker's henchmen seemed to be\x01",
            "influential members of the Imperial Faction.\x02\x03",
            "#0104FI think I see what you mean.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9629")

    label("loc_9564")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95B4")

    ChrTalk(
        0x103,
        "#11P#0205FI see... That is another valid perspective.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9629")

    label("loc_95B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9629")

    ChrTalk(
        0x104,
        (
            "#11P#0304FHaha, makes sense to me.\x02\x03",
            "#0300FThe guy didn't have the confidence to\x01",
            "win one-on-one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9629")


    ChrTalk(
        0x101,
        (
            "#5P#0003FMaybe we were a bit naive to underestimate\x01",
            "someone as experienced as the mayor.\x02\x03",
            "(I still wish we could find a way to\x01",
            "help him, though.)\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    SetChrPos(0x0, -7590, 4000, 19290, 135)
    SetScenarioFlags(0xBE, 6)
    EventEnd(0x5)
    Return()

    # Function_17_76BB end

    def Function_18_96E6(): pass

    label("Function_18_96E6")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_976B")
    OP_68(-3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, -4500, 130, 2900, 90)
    SetChrPos(0x153, -5250, 130, 3650, 90)
    SetChrPos(0xEF, -6000, 130, 2150, 90)
    Jump("loc_97CC")

    label("loc_976B")

    OP_68(3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 4500, 130, 2900, 270)
    SetChrPos(0x153, 5250, 130, 3650, 270)
    SetChrPos(0xEF, 6000, 130, 2150, 270)

    label("loc_97CC")

    TurnDirection(0x8, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "Ah, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What happened in the mayor's office?\x02",
    )

    CloseMessageWindow()

    def lambda_9819():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9819)
    Sleep(50)

    def lambda_9829():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9829)
    Sleep(50)
    TurnDirection(0xEF, 0x8, 500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x101,
        "#0005FUmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98D4")
    OP_68(-1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_9880():
        OP_95(0xFE, -2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9880)
    Sleep(50)

    def lambda_989D():
        OP_95(0xFE, -3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_989D)
    Sleep(50)

    def lambda_98BA():
        OP_95(0xFE, -3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_98BA)
    Jump("loc_993E")

    label("loc_98D4")

    OP_68(1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_98EF():
        OP_95(0xFE, 2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98EF)
    Sleep(50)

    def lambda_990C():
        OP_95(0xFE, 3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_990C)
    Sleep(50)

    def lambda_9929():
        OP_95(0xFE, 3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9929)

    label("loc_993E")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    ClearChrFlags(0xEF, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9988")

    ChrTalk(
        0x102,
        "#0105FAre you referring to...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_99F3")

    label("loc_9988")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99BB")

    ChrTalk(
        0x103,
        "#0205FCare to elaborate?\x02",
    )

    CloseMessageWindow()
    Jump("loc_99F3")

    label("loc_99BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99F3")

    ChrTalk(
        0x104,
        "#0305FWhat's that s'posed to mean?\x02",
    )

    CloseMessageWindow()

    label("loc_99F3")


    ChrTalk(
        0x8,
        (
            "I saw what happened.\x01",
            "Speaker Hartmann stormed into the\x01",
            "mayor's office with his cronies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've seen it happen plenty of times,\x01",
            "but I felt a bit more worried than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, that?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B2F")

    ChrTalk(
        0x102,
        (
            "#0100FI'm worried like you are, but...\x01",
            "He's my grandfather, so I know he'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BF0")

    label("loc_9B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B8E")

    ChrTalk(
        0x103,
        (
            "#0200FI am slightly concerned, but I believe\x01",
            "the mayor will be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BF0")

    label("loc_9B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BF0")

    ChrTalk(
        0x104,
        (
            "#0300FI'm a lil' worried, but I think the old\x01",
            "man's tougher than he lets on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF0")


    ChrTalk(
        0x8,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's an unfortunate situation, but\x01",
            "employees of City Hall are sadly\x01",
            "powerless at times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would like to offer the mayor\x01",
            "something as a token of our\x01",
            "appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNo doubt about it. We feel the\x01",
            "same way, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#1105FWhy don't we give something nice\x01",
            "to Gramps?\x02\x03",
            "#1110FCouldn't we treat him to something\x01",
            "tasty that he likes?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0005FY-Yeah, that's a pretty good idea.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E3D")

    ChrTalk(
        0x102,
        (
            "#0100FI'm sure he would love to indulge\x01",
            "in his favorite food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E7F")

    ChrTalk(
        0x103,
        "#0203FSimple, yet effective. I like it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EDA")

    label("loc_9E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EDA")

    ChrTalk(
        0x104,
        (
            "#0304FI dunno 'bout you, but a good snack\x01",
            "always gets me goin' again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EDA")

    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x8,
        "What a great idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That being said...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's fine if you don't have the time,\x01",
            "but would you be willing to go out\x01",
            "and buy the mayor's favorite drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You should be able to purchase it\x01",
            "at the juice stall near the fountain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, no problem. A task that simple\x01",
            "isn't a bother to us.\x02\x03",
            "On that note, do you happen to know\x01",
            "what the drink in question is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm not entirely sure, but I heard it's\x01",
            "not on the menu. I believe they sell\x01",
            "a few secret items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The clerk should have no problems\x01",
            "helping you out with it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A180")

    ChrTalk(
        0x102,
        (
            "#0100FSounds like a plan, then. We'll go\x01",
            "to the juice stall near the fountain\x01",
            "and see what we can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A241")

    label("loc_A180")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1DB")

    ChrTalk(
        0x103,
        (
            "#0200FLet us depart for the juice stall near\x01",
            "the fountain, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A241")

    label("loc_A1DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A241")

    ChrTalk(
        0x104,
        (
            "#0300FLet's hop on over to the fountain and\x01",
            "get our favorite Grandpa some juice!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A241")


    ChrTalk(
        0x153,
        "#1109FLet's go!\x02",
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
            "[A Treat for the Mayor]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A2DD")
    SetChrPos(0x0, -2360, 0, 4980, 45)
    Jump("loc_A2EE")

    label("loc_A2DD")

    SetChrPos(0x0, 2360, 0, 4980, 315)

    label("loc_A2EE")

    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x26, 0x4, 0x2)
    EventEnd(0x5)
    Return()

    # Function_18_96E6 end

    def Function_19_A306(): pass

    label("Function_19_A306")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch06500.itc", 0x1E)
    LoadChrToIndex("chr/ch27800.itc", 0x1F)
    LoadChrToIndex("chr/ch27400.itc", 0x20)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 8119, 4000, 14200, 315)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A40F")
    OP_68(-7680, 5500, 15150, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -9250, 4000, 14500, 45)
    SetChrPos(0x153, -10350, 4000, 14450, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3C3")
    SetChrPos(0x102, -9600, 4000, 13150, 45)
    Jump("loc_A40A")

    label("loc_A3C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3E9")
    SetChrPos(0x103, -9600, 4000, 13150, 45)
    Jump("loc_A40A")

    label("loc_A3E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A40A")
    SetChrPos(0x104, -9600, 4000, 13150, 45)

    label("loc_A40A")

    Jump("loc_A4CC")

    label("loc_A40F")

    OP_68(-4800, 5500, 16000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1500, 4000, 14500, 270)
    SetChrPos(0x153, -750, 4000, 15250, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A485")
    SetChrPos(0x102, -500, 4000, 13750, 270)
    Jump("loc_A4CC")

    label("loc_A485")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4AB")
    SetChrPos(0x103, -500, 4000, 13750, 270)
    Jump("loc_A4CC")

    label("loc_A4AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4CC")
    SetChrPos(0x104, -500, 4000, 13750, 270)

    label("loc_A4CC")

    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -8400, 4000, 20200, 135)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x16, -8800, 4000, 21500, 135)
    SetChrPos(0x17, -9750, 4000, 21050, 135)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_0D()

    NpcTalk(
        0x15,
        "Voice",
        "#2PHmph. Excuse us.\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)

    def lambda_A5A0():
        OP_97(0x15, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A5A0)

    def lambda_A5BA():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_A5BA)
    Sleep(50)

    def lambda_A5CE():
        OP_97(0x16, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A5CE)

    def lambda_A5E8():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_A5E8)
    Sleep(50)

    def lambda_A5FC():
        OP_97(0x17, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A5FC)

    def lambda_A616():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A616)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)

    ChrTalk(
        0x16,
        (
            "#11PFor crying out loud!\x01",
            "What a stubborn old man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PHow dare he refuse the proposal our\x01",
            "glorious speaker went to great lengths\x01",
            "to write up?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#2702FWell, no matter.\x01",
            "We've succeeded in proving our point.\x02\x03",
            "#2703FWe'll prepare the usual to deal with\x01",
            "Campbell and his men.\x02\x03",
            "#2701FOur real problem right now is\x01",
            "Revache's incompetence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11PR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PI think a friendly 'reminder' of how the\x01",
            "speaker's efforts alone brought them\x01",
            "fame is in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#2703FI'll respectfully decline. I don't intend\x01",
            "on meeting Marconi for a while.\x02\x03",
            "#2702FMore importantly, we need to hold\x01",
            "a meeting later tonight.\x02\x03",
            "Inform all members of the Imperial Faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11PAs you wish, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5PWe'll issue an emergency meeting!\x02",
    )

    CloseMessageWindow()
    OP_68(6200, 5500, 17600, 6000)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x16, 3, 0, 21)
    BeginChrThread(0x17, 3, 0, 22)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A99C")
    Sleep(1000)

    def lambda_A96F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A96F)
    Sleep(50)

    def lambda_A97F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A97F)
    Sleep(50)

    def lambda_A98F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A98F)
    Jump("loc_A9CC")

    label("loc_A99C")

    Sleep(2500)

    def lambda_A9A4():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9A4)
    Sleep(50)

    def lambda_A9B4():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A9B4)
    Sleep(50)

    def lambda_A9C4():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A9C4)

    label("loc_A9CC")

    WaitChrThread(0x15, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x16, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA37")
    Fade(500)
    OP_68(-8100, 5500, 13450, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Jump("loc_AA6B")

    label("loc_AA37")

    Fade(500)
    OP_68(-820, 4500, 15700, 0)
    MoveCamera(11, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    label("loc_AA6B")


    ChrTalk(
        0x101,
        (
            "#5P#0003FPhew...\x01",
            "They're finally out of the mayor's hair.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB1B")

    ChrTalk(
        0x102,
        (
            "#12P#0100FLet's meet with Grandfather while we\x01",
            "have the chance and give him the drink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABEC")

    label("loc_AB1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB88")

    ChrTalk(
        0x103,
        (
            "#12P#0200FThis would be a good opportunity to\x01",
            "present the mayor with his beverage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABEC")

    label("loc_AB88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABEC")

    ChrTalk(
        0x104,
        (
            "#12P#0300FLet's go give the man his drink while\x01",
            "those goons are outta the way!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABEC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(-6390, 5500, 17440, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, -6390, 4000, 17440, 315)
    SetChrPos(0x1, -6390, 4000, 17440, 315)
    SetChrPos(0x153, -6390, 4000, 17440, 315)
    OP_4C(0x9, 0xFF)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x1, 0x0, 0x17)
    SetScenarioFlags(0xBE, 7)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_19_A306 end

    def Function_20_AC9B(): pass

    label("Function_20_AC9B")


    def lambda_ACA0():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACA0)
    WaitChrThread(0xFE, 1)

    def lambda_ACBE():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACBE)
    Sleep(1000)

    def lambda_ACCE():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACCE)
    Sleep(2000)

    def lambda_ACEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_ACEB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_AC9B end

    def Function_21_ACFC(): pass

    label("Function_21_ACFC")


    def lambda_AD01():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD01)
    WaitChrThread(0xFE, 1)

    def lambda_AD1F():
        OP_95(0xFE, 6720, 4000, 19320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD1F)
    WaitChrThread(0xFE, 1)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)

    def lambda_AD52():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD52)
    WaitChrThread(0xFE, 1)
    Sleep(2000)

    def lambda_AD66():
        OP_95(0xFE, 7210, 4000, 18830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD66)
    WaitChrThread(0xFE, 1)

    def lambda_AD84():
        OP_97(0xFE, 0xBB8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD84)
    Sleep(1000)

    def lambda_ADA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_ADA1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_ACFC end

    def Function_22_ADB2(): pass

    label("Function_22_ADB2")


    def lambda_ADB7():
        OP_97(0xFE, 0x2904, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADB7)
    WaitChrThread(0xFE, 1)

    def lambda_ADD5():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADD5)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_ADE9():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADE9)
    WaitChrThread(0xFE, 1)

    def lambda_AE07():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE07)
    Sleep(2000)

    def lambda_AE24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE24)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_ADB2 end

    def Function_23_AE35(): pass

    label("Function_23_AE35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    OP_68(-45000, 1500, 11000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -45750, 0, 1500, 0)
    SetChrPos(0x153, -45000, 0, 2750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEBD")
    SetChrPos(0x102, -44250, 0, 2000, 0)
    Jump("loc_AF04")

    label("loc_AEBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEE3")
    SetChrPos(0x103, -44250, 0, 2000, 0)
    Jump("loc_AF04")

    label("loc_AEE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF04")
    SetChrPos(0x104, -44250, 0, 2000, 0)

    label("loc_AF04")

    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -45000, 0, 11500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FPardon us, sir. We've been barging into\x01",
            "your office more often these days.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#5P#2500FOh, you're back again.\x01",
            "My apologies for earlier.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFDD():
        OP_98(0x153, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_AFDD)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B024")

    def lambda_B00A():
        OP_98(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B00A)
    Jump("loc_B07D")

    label("loc_B024")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B053")

    def lambda_B039():
        OP_98(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B039)
    Jump("loc_B07D")

    label("loc_B053")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B07D")

    def lambda_B068():
        OP_98(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B068)

    label("loc_B07D")

    Sleep(50)

    def lambda_B085():
        OP_98(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B085)
    OP_68(-45000, 1100, 10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0001FNo need to apologize, sir.\x01",
            "You were placed in a difficult situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B153")

    ChrTalk(
        0x102,
        "#11P#0108FIs everything all right, Grandfather?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B21A")

    label("loc_B153")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1B9")

    ChrTalk(
        0x103,
        (
            "#11P#0200FThe bombardment of sequential proposals\x01",
            "must be wearing you down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B21A")

    label("loc_B1B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B21A")

    ChrTalk(
        0x104,
        (
            "#11P#0301FEverything good? They looked like\x01",
            "they were tryin' to corner you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B21A")


    ChrTalk(
        0xB,
        (
            "#5P#2509FI'm fine, thank you. I've become talented\x01",
            "at managing their persistence.\x02\x03",
            "#2500FBy the way, is something the matter?\x01",
            "Have you forgotten a possession?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FNo, not quite...\x02\x03",
            "#0002FHey, KeA. Go ahead and give it to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#6P#1100FOkay!\x02",
    )

    CloseMessageWindow()
    OP_98(0x153, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA handed the specially made acerbic tomato\x01",
            "shake over to Mayor MacDowell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x358, 1)
    OP_98(0x153, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)

    ChrTalk(
        0xB,
        (
            "#5P#2505FOh... This is my favorite drink.\x02\x03",
            "Did you go out of your way to purchase\x01",
            "this for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#6P#1110FYep, it's our treat to you!\x02\x03",
            "#1109FYou look like you've been working\x01",
            "really hard, Gramps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#2509FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah, the receptionist suggested we\x01",
            "order this for you.\x02\x03",
            "#0000FThe clerk that runs the juice stall was\x01",
            "nice enough to give it to us for free, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2503FI see...\x01",
            "Indeed, I am most appreciative of\x01",
            "this fantastic gift.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B685")

    ChrTalk(
        0xB,
        (
            "#5P#2500FThank you, Lloyd and Elie.\x01",
            "And not to mention, KeA.\x02\x03",
            "#2509FI feel completely rejuvenated, thanks to you.\x01",
            "I'll be able to work hard through the\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0102FDon't use this as an excuse to\x01",
            "overwork yourself, Grandfather.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B86D")

    label("loc_B685")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B777")

    ChrTalk(
        0xB,
        (
            "#5P#2500FThank you, Lloyd and Tio.\x01",
            "And not to mention, KeA.\x02\x03",
            "#2509FI feel completely rejuvenated, thanks to you.\x01",
            "I'll be able to work hard through the\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FPlease do not overexert yourself, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B86D")

    label("loc_B777")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B86D")

    ChrTalk(
        0xB,
        (
            "#5P#2500FThank you, Lloyd and Randy.\x01",
            "And not to mention, KeA.\x02\x03",
            "#2509FI feel completely rejuvenated, thanks to you.\x01",
            "I'll be able to work hard through the\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FHaha, no problem! Don't go TOO\x01",
            "crazy, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B86D")


    ChrTalk(
        0xB,
        (
            "#5P#2503FOh, that reminds me.\x02\x03",
            "I have something to give you in return\x01",
            "for the pleasant treat.\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xB, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mayor MacDowell retrieved a small\x01",
            "package from beneath the shelf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B97C")
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_B9D1")

    label("loc_B97C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9A9")
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_B9D1")

    label("loc_B9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9D1")
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_B9D1")

    OP_97(0xB, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xB, 0xB4, 0x0)

    ChrTalk(
        0xB,
        (
            "#5P#2500FTake this medicinal herb I received\x01",
            "from a friend in the Republic.\x01",
            "I've heard it's quite valuable.\x02\x03",
            "Don't be shy. Please, take it.\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0xB, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    Sleep(500)
    OP_98(0xB, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1FE, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0005FTh-There's no way we could\x01",
            "possibly ever accept this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#2503FNonsense. I have no use for it.\x02\x03",
            "It makes perfect sense for you to\x01",
            "take it. You're constantly putting\x01",
            "yourselves in the face of danger.\x02\x03",
            "#2500FPlease, don't be shy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FI understand, sir.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC5F")

    ChrTalk(
        0x102,
        "#11P#0102FHeehee. We'll gladly accept it, Grandfather.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD4")

    label("loc_BC5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCA7")

    ChrTalk(
        0x103,
        "#11P#0202FWe'll accept them, then. Thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCD4")

    label("loc_BCA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCD4")

    ChrTalk(
        0x104,
        "#11P#0309FThanks a ton!\x02",
    )

    CloseMessageWindow()

    label("loc_BCD4")


    ChrTalk(
        0x153,
        "#6P#1109FThank you, Gramps!\x02",
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
            "[A Treat for the Mayor]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xB, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_68(-45000, 1500, 12000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -45000, 0, 12000, 0)
    SetChrPos(0x1, -45000, 0, 12000, 0)
    SetChrPos(0x153, -45000, 0, 12000, 0)
    SetChrPos(0xB, -45000, 250, 14700, 180)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_29(0x26, 0x4, 0x10)
    OP_29(0x26, 0x1, 0x6)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_AE35 end

    def Function_24_BDF9(): pass

    label("Function_24_BDF9")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(0, 1100, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#2200813V#5PWelcome to the Crossbell City Hall.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_BF3A")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2200814V#5POh, you're with the CPD, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200815V#5PAre you here to meet with someone?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C032")

    label("loc_BF3A")


    ChrTalk(
        0x8,
        "#2200816V#5PWhat business do you have here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200817V#12P#0000FThat's right, we're with the CPD.\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed his Detective Notebook.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#2200818V#5PAh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200819V#5PSo, are you here to meet with someone?\x02",
    )

    CloseMessageWindow()

    label("loc_C032")


    ChrTalk(
        0x102,
        "#2200820V#0103FNo, not quite...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie asked to borrow the Geofront\x01",
            "B Sector key for their investigation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#2200821V#5PThe Geofront's B Sector... I believe it's\x01",
            "in the northwestern part of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2200822V#5PWait one moment while I fetch you the key.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_C160():
        OP_95(0xFE, 0, 0, 9400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C160)
    OP_0D()
    WaitChrThread(0x8, 1)
    Sleep(500)
    OP_93(0x8, 0x0, 0x0)

    def lambda_C189():
        OP_95(0xFE, 0, 0, 7400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C189)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "#2200823V#5PHere you are.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x322),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x322, 1)

    ChrTalk(
        0x101,
        "#2200824V#12P#0002FThanks for letting us borrow it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200825V#12P#0200FIs it fine for you to lend it to us\x01",
            "without asking any questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200826V#5PNot to worry. I've been asked to cooperate\x01",
            "with your group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200827V#5PYou know, I've actually lent that very\x01",
            "same key to the Bracer Guild before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200828V#12P#0012FR-Really? I wonder what they needed it for...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200829V#5PThe entrance to the Geofront's B Sector can be\x01",
            "found near the Residential District's waterway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200830V#5PBe careful with that key. We've lost it a few\x01",
            "times already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200831V#0100FOkay, we'll be extra careful with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200832V#12P#0309FThanks for warnin' us!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x83, 2)
    OP_29(0x43, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_24_BDF9 end

    def Function_25_C4E5(): pass

    label("Function_25_C4E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_68(0, 900, 6560, 0)
    MoveCamera(54, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -650, 0, -3500, 0)
    SetChrPos(0x102, 650, 0, -3500, 0)
    SetChrPos(0x103, -900, 0, -4800, 0)
    SetChrPos(0x104, 900, 0, -4800, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PYou're looking for information on the\x01",
            "cheapest apartments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTake this brochure. I'm sure it'll\x01",
            "prove more than useful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#1805FOh, I wasn't aware these existed.\x02\x03",
            "#1809FWhat a relief... Do you mind if I\x01",
            "borrow one and read through it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNot at all, ma'am. They're there\x01",
            "for you to take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut I'd be careful with cheaper\x01",
            "apartments if I were you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#1806F*sigh* I need to hurry and sort out\x01",
            "my housing situation so I can return\x01",
            "to practicing.\x02\x03",
            "#1802F#3SMy apologies. I started thinking aloud.\x01",
            "Anyway, thank you for your assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)
    OP_68(0, 1500, -1030, 3000)

    def lambda_C7DA():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7DA)
    Sleep(50)

    def lambda_C7F7():
        OP_95(0xFE, 0, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C7F7)

    def lambda_C811():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C811)
    Sleep(50)

    def lambda_C82E():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C82E)
    Sleep(50)

    def lambda_C84B():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C84B)
    Sleep(350)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        "#5P#1805FOh, I'm so sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FNot at all.\x02",
    )

    CloseMessageWindow()

    def lambda_C8C8():
        OP_98(0x101, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8C8)
    Sleep(50)

    def lambda_C8E5():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8E5)
    Sleep(25)

    def lambda_C902():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C902)
    Sleep(25)

    def lambda_C91F():
        OP_98(0x104, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C91F)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x0)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x0)

    ChrTalk(
        0x12,
        "#5P#1804F*bows*\x02",
    )

    CloseMessageWindow()

    def lambda_C97A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFDF94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C97A)
    Sleep(500)

    def lambda_C997():

        label("loc_C997")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_C997")

    QueueWorkItem2(0x101, 2, lambda_C997)

    def lambda_C9A9():

        label("loc_C9A9")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_C9A9")

    QueueWorkItem2(0x102, 2, lambda_C9A9)

    def lambda_C9BB():

        label("loc_C9BB")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_C9BB")

    QueueWorkItem2(0x103, 2, lambda_C9BB)

    def lambda_C9CD():

        label("loc_C9CD")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_C9CD")

    QueueWorkItem2(0x104, 2, lambda_C9CD)
    Sleep(1200)

    def lambda_C9E2():
        OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_C9E2)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x12, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#0000FDidn't we just see her not too long ago?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0102FI think we'll be seeing more\x01",
            "of her in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -1720, 0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x53, 0)
    EventEnd(0x5)
    Return()

    # Function_25_C4E5 end

    def Function_26_CAAB(): pass

    label("Function_26_CAAB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PWelcome to Crossbell City Hall.\x01",
            "How may I help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease use our services to make\x01",
            "payments or to submit an application\x01",
            "for moving into or vacating the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse us. We're with the CPD.\x02\x03",
            "We're here in response to a support\x01",
            "request submitted by City Hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        "#5POh, you're with the police?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWonderful! I wasn't expecting you\x01",
            "to respond so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FCould you give us more details about\x01",
            "the request, please?\x02\x03",
            "I believe it had to do with confirming\x01",
            "vacancies of certain residences...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POkay. Let me fill you in on the details.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou're all familiar with resident\x01",
            "registrations, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyone wishing to move to Crossbell\x01",
            "must visit us to register for residency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe reality is, people will freely move in\x01",
            "and out of the city without going through\x01",
            "the appropriate avenues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's become more and more difficult\x01",
            "for us to keep track of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FI can imagine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTherefore, we're seeking your help to verify\x01",
            "any vacant residences in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe need to rectify our documents that\x01",
            "have any mislabeled vacancies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe folks over at the Residential Affairs\x01",
            "have their hands full, so we'd greatly\x01",
            "appreciate the assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYou tellin' us that we have to play errand\x01",
            "boys for the government?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#12P#0006FThat's awfully rude of you, Randy.\x02\x03",
            "#0001FVerifying vacancies is actually important in\x01",
            "catching certain criminal activities. Filing the\x01",
            "documents in a timely matter is critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FInterestin'. Woulda had me fooled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FI don't think we'll be doing more than walking\x01",
            "through the city, so it shouldn't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWill you be able to help us, then?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D270")
    Call(0, 28)
    Return()

    label("loc_D270")


    ChrTalk(
        0x101,
        (
            "#12P#0006FI'm sorry. I understand the situation,\x01",
            "but we've got other important matters\x01",
            "on our hands right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI understand. I hope you return at a\x01",
            "time more suited to your schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI don't mind when that is, as long as\x01",
            "it's by the end of today.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_26_CAAB end

    def Function_27_D39B(): pass

    label("Function_27_D39B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PI'd like to ask for your assistance to verify\x01",
            "vacant residencies around the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt doesn't look like Residential Affairs was\x01",
            "able to get around to doing it. Will you be\x01",
            "able to help us?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D549")
    Call(0, 28)
    Return()

    label("loc_D549")


    ChrTalk(
        0x101,
        (
            "#12P#0006FI'm sorry. I understand the situation,\x01",
            "but we've got other important matters\x01",
            "on our hands right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI understand. I hope you return at a\x01",
            "time more suited to your schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI don't mind when that is, as long as\x01",
            "it's by the end of today.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_27_D39B end

    def Function_28_D674(): pass

    label("Function_28_D674")

    OP_29(0x3, 0x2, 0x1F)

    ChrTalk(
        0x8,
        (
            "#5PThank you very much. I'll hand these\x01",
            "documents over to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThese files are relevant to the request\x01",
            "and will guide you in your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FOkay, we'll hold on to them for now.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_95(0x101, -70, 0, 5240, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x35A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x35A, 1)
    OP_96(0x101, 0xFFFFFDA8, 0x0, 0x125C, 0x3E8, 0x0)
    Sleep(400)

    def lambda_D7CC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7CC)
    Sleep(200)

    def lambda_D7DC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7DC)

    def lambda_D7E9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D7E9)

    def lambda_D7F6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D7F6)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#0005FLet's see... There are three different\x01",
            "locations in total.\x02\x03",
            "#0003FThere's one near the entrance of the\x01",
            "Residential District.\x02\x03",
            "Looks like the next one's on East Street.\x01",
            "Huh. According to this address, it's to\x01",
            "the right of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DA58")

    ChrTalk(
        0x104,
        (
            "#0300FTo the right of the guild? Sweet, that'll\x01",
            "be pretty easy to remember.\x02\x03",
            "#0305FLast one looks like it's in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0103FIt's an apartment complex known as\x01",
            "Lotus Heights. There appear to be three\x01",
            "documented vacancies.\x02\x03",
            "#0105FJust a moment, please. I'll note this\x01",
            "down in the Detective Notebook.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBB9")

    label("loc_DA58")


    ChrTalk(
        0x104,
        (
            "#0303FTo the right of the guild? Sweet, that'll\x01",
            "be pretty easy to remember.\x02\x03",
            "#0305FSo, where's the last place we're headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FThe last one is in the Downtown District.\x02\x03",
            "#0103FThere are three separate vacancies in an\x01",
            "apartment complex known as Lotus Heights.\x02\x03",
            "#0105FJust a moment, please. I'll note this down in\x01",
            "the Detective Notebook.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBB9")


    ChrTalk(
        0x102,
        "#11P#0103F*scribble* *scribble*\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x102,
        "#11P#0100FOkay, all done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FThanks for taking care of that, Elie.\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_DC3C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC3C)

    def lambda_DC49():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC49)

    def lambda_DC56():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC56)

    def lambda_DC63():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC63)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe'll begin working on verifying the\x01",
            "outlined vacancies now.\x02\x03",
            "We just have to report back to you\x01",
            "once we've completed the task, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, please report back to me once you've\x01",
            "completed verifying all three locations.\x01",
            "I'll leave everything in your capable hands.\x02",
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
            "[Vacancy Verification]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1500, 4000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetChrPos(0x1, 0, 0, 4000, 0)
    SetChrPos(0x2, 0, 0, 4000, 0)
    SetChrPos(0x3, 0, 0, 4000, 0)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_D674 end

    def Function_29_DE79(): pass

    label("Function_29_DE79")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PHello, everyone. Is the verification\x01",
            "process going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYeah, we wrapped up a little while ago.\x01",
            "We're here to submit our report.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_95(0x101, -70, 0, 5240, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    Sleep(400)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the corrected documents.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Sleep(300)
    OP_96(0x101, 0xFFFFFDA8, 0x0, 0x125C, 0x3E8, 0x0)
    Sleep(400)
    SubItemNumber(0x35A, 1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5PWow, you've even included footnotes\x01",
            "for each of the room numbers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you so much. I'm sure Residential Affairs\x01",
            "will be more than grateful for the help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI'd rather they worked on bein' a lil' more\x01",
            "organized with their documentation instead.\x02\x03",
            "They had us on a real wild goose chase\x01",
            "thanks to their mistakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI do not believe we have the authority\x01",
            "to comment, but the organization of the\x01",
            "original documents was less than stellar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI-I'm truly sorry for the trouble they've caused.\x01",
            "Residential Affairs tries their hardest to ensure\x01",
            "complete accuracy in their documentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, diet members are constantly\x01",
            "putting pressure on them. I hope you will\x01",
            "accept my apology on their behalf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FN-No, that's okay. We may have\x01",
            "been a little insensitive.\x02\x03",
            "(Looks like this place has its\x01",
            "own share of problems to deal with.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0108F(Right... Members of the Crossbell Diet\x01",
            "can make life harder for a lot of people.)\x02\x03",
            "#0100FAnyway, I'm glad we could be of assistance.\x02\x03",
            "I know it can get overwhelming at times,\x01",
            "so we'd be happy to help again should\x01",
            "you need us to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI agree. Assignments of a similar nature\x01",
            "should be no problem for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FJust say the word, and we'll be there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you for the offer. We'll be sure to\x01",
            "take you up on it when the time comes.\x02",
        )
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
            "[Vacancy Verification]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(0, 1500, 4000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetChrPos(0x1, 0, 0, 4000, 0)
    SetChrPos(0x2, 0, 0, 4000, 0)
    SetChrPos(0x3, 0, 0, 4000, 0)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x2, 0x1E)
    OP_29(0x3, 0x1, 0x8)
    OP_29(0x3, 0x4, 0x10)
    SetScenarioFlags(0x0, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_DE79 end

    def Function_30_E674(): pass

    label("Function_30_E674")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4650, 5200, 16390, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 4160, 4000, 16219, 0)
    SetChrPos(0x102, 5480, 4000, 16219, 0)
    SetChrPos(0x103, 4160, 4000, 14800, 0)
    SetChrPos(0x104, 5480, 4000, 14800, 0)
    SetChrPos(0x9, 4870, 4000, 18550, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5P*sigh* Oh, sweet Aidios. What\x01",
            "am I going to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#5POh, I recognize you! You're the\x01",
            "Special Support Section, right?!\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 4870, 4000, 17950, 2000, 0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0000FYes, we are. Is everything all right, sir?\x01",
            "We're here for your support request.\x02\x03",
            "I can tell that you're in a bit of a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FHas something gone missing, perhaps?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PA-Actually, yes.\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#5P#4SSomething REALLY IMPORTANT\x01",
            "was stolen!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x103,
        "#12P#0205FAre you certain it was not misplaced?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FYou tellin' me someone had the stones\x01",
            "to steal from City Hall?\x02\x03",
            "#0306FI figured the festival would bring its\x01",
            "fair share of problems, but man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FCould you tell us what was stolen, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PRight. Do you remember the giant statue\x01",
            "that used to sit on display here? That.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2790, 4200, 19050, 2000)
    MoveCamera(26, 25, 0, 2000)

    def lambda_EAD8():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EAD8)

    def lambda_EAE5():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EAE5)

    def lambda_EAF2():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EAF2)

    def lambda_EAFF():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EAFF)

    def lambda_EB0C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EB0C)
    Sleep(2000)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#6P#0003FY-You know, now that you mention it...\x01",
            "It does feel a little more spacious than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0205FUnbelievable. How could someone\x01",
            "possibly steal something that heavy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PI could hardly believe it myself!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(4650, 5200, 16390, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_EC86():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EC86)
    Sleep(10)

    def lambda_EC96():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EC96)

    def lambda_ECA3():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_ECA3)
    Sleep(18)

    def lambda_ECB3():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_ECB3)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5PThe statue is known as the Saint's Prayer.\x01",
            "A renowned sculptor crafted it when\x01",
            "Crossbell State was founded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FThis is the very same Saint's Prayer\x01",
            "by the famous Magnus Hector, yes?\x02\x03",
            "#0103FThe magnum opus of one of the greatest\x01",
            "sculptors known to Crossbell. It was a gift\x01",
            "celebrating the founding of the state.\x02\x03",
            "#0100FI've heard its historical significance has\x01",
            "made it the unofficial symbol of City Hall.\x02\x03",
            "#0108FI find it a little ironic that the Republican\x01",
            "and Imperial Factions hold so much power\x01",
            "over a diet under its protection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHaha. Well said, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PBut indeed, the statue is incredibly\x01",
            "important to City Hall. We consider\x01",
            "it to be the pride of Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PTo make matters worse, many guests will be\x01",
            "here for the closing ceremony this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P*sigh* To display such negligent behavior\x01",
            "during a joyous occasion would be an utter\x01",
            "disgrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FDefinitely. Crossbell would become a joke\x01",
            "on the international stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FYeah, and the CPD'd take a heavy blow\x01",
            "to their reputation, too.\x02\x03",
            "#0306FI can see the headlines in the Crossbell\x01",
            "Times already...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1400)

    ChrTalk(
        0x103,
        (
            "#12P#0203FRandy... Please consider thinking before\x01",
            "you add any unnecessary stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FSorry 'bout that. Kinda just slipped out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FStill, there's a very real possibility it\x01",
            "could all come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P*sigh* Please don't let it come down\x01",
            "to that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe Crossbell Times already loves to\x01",
            "write on the various scandals here at\x01",
            "City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FI think we should get started on the\x01",
            "investigation, then.\x02\x03",
            "#0105FWith that being said, do you have any idea\x01",
            "who the perpetrator might be, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell, actually... This was left at\x01",
            "the scene of the crime.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Clipp revealed a card.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Special Support Section, with my riddles,\x01",
            "I challenge you to a game of wisdom and wit!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　For the starting key, lift your eyes up\x01",
            "　within the city's beloved symbol that tells\x01",
            "　not time, but can show the dark sky!\x01",
            "         -Phantom Thief B\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        "#6P#0005FPhantom Thief B?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FI never expected him to come to Crossbell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWho does this guy think he is? Why does a\x01",
            "thief get to give himself a sick nickname?\x02\x03",
            "#0303FWait a sec. I feel like I've heard that\x01",
            "name before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI also recall hearing that name in passing.\x02\x03",
            "#0200FYou two are familiar with him, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FYeah, but I've only heard a few rumors.\x02\x03",
            "#0001FHe's an infamous thief known across\x01",
            "the continent for his exploits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FHe is both elusive and mysterious, and is\x01",
            "responsible for the theft of countless works\x01",
            "of art. He primarily operates in the Empire.\x02\x03",
            "#0100FThis is the man known as Phantom Thief B.\x02\x03",
            "His modus operandi is to send a calling\x01",
            "card to his victims to taunt them. He has\x01",
            "yet to be caught in the act a single time.\x02\x03",
            "His arsenal of bizarre magic allows him to claim\x01",
            "his spoils without being detected. The strange\x01",
            "part is, some people regard him as a hero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FSo essentially, this 'infamous thief' has\x01",
            "issued us a challenge, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PRight. That is actually the reason why I\x01",
            "called you here instead of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThe calling card clearly stated the\x01",
            "SSS by name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0304FSounds like we've got a party on our hands.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#12P#0300FYo, Lloyd. I don't really care if this guy is some\x01",
            "infamous thief, but we gotta take him down!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB10():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB10)

    def lambda_FB1D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FB1D)

    def lambda_FB2A():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FB2A)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0001FRight, but don't forget there's a missing\x01",
            "statue we need to retrieve. Let's accept\x01",
            "his challenge head-on, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FRight. Let's do this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThe riddle says 'The city's beloved symbol\x01",
            "that tells not time, but can show the dark sky!'\x01",
            "We should start by searching the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FSounds like it's time to hit the city!\x02",
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
            "[Urgent Request from City Hall]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5080, 4000, 14410, 180)
    OP_4C(0x9, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_E674 end

    def Function_31_FD3D(): pass

    label("Function_31_FD3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FD7B")
    OP_95(0xFE, 3550, 4000, 18550, 1000, 0x0)
    Sleep(200)
    OP_95(0xFE, 5980, 4000, 18550, 1000, 0x0)
    Sleep(200)
    Jump("Function_31_FD3D")

    label("loc_FD7B")

    Return()

    # Function_31_FD3D end

    def Function_32_FD7C(): pass

    label("Function_32_FD7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26000.itc", 0x1E)
    OP_4B(0x9, 0xFF)
    OP_68(-40, 5500, 20590, 0)
    MoveCamera(1, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25270, 0)
    SetChrPos(0x101, -580, 4000, 15800, 0)
    SetChrPos(0x102, 550, 4000, 15800, 0)
    SetChrPos(0x103, -580, 4000, 14500, 0)
    SetChrPos(0x104, 550, 4000, 14500, 0)
    SetChrPos(0x9, -1850, 4000, 16820, 45)
    SetChrPos(0x13, -1790, 4000, 19380, 90)
    SetChrPos(0x14, 470, 4000, 18500, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x1)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x1)
    BeginChrThread(0x13, 0, 0, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetMapObjFrame(0xFF, "model06", 0x1, 0x1)
    MoveCamera(1, 19, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x40)
    Fade(800)
    OP_68(30, 4500, 17170, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(19220, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#6PI never would have imagined you'd\x01",
            "be able to recover it so quickly...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF28():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FF28)
    Sleep(20)

    def lambda_FF38():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FF38)
    Sleep(12)

    def lambda_FF48():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FF48)

    def lambda_FF55():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FF55)
    Sleep(15)

    def lambda_FF65():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FF65)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "#6PI thank you from the bottom of my heart,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0012FIt was difficult, but thank Aidios we were\x01",
            "able to solve it without incident.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x14, 1, 0, 33)

    ChrTalk(
        0x102,
        (
            "#11P#0100FNow you'll be able to conduct the closing\x01",
            "ceremony without issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PIndeed. What a relief.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 1)
    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    def lambda_1009E():
        OP_95(0xFE, -1570, 4000, 18500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1009E)
    OP_95(0x14, -1570, 4000, 18500, 1000, 0x0)
    OP_95(0x14, -490, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0xB4, 0x1F4)

    ChrTalk(
        0x13,
        "#5POkay. We're done placing it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PThanks for conducting business with us!\x02",
    )

    CloseMessageWindow()

    def lambda_1013D():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1013D)
    Sleep(20)

    def lambda_1014D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1014D)
    Sleep(12)

    def lambda_1015D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1015D)

    def lambda_1016A():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1016A)
    Sleep(15)

    def lambda_1017A():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1017A)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6POh, right. Thank you for swiftly\x01",
            "taking care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FThanks for the help, pals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#5PHaha, no problem. That thing was pretty hefty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PIf you'll excuse us, then!\x02",
    )

    CloseMessageWindow()

    def lambda_1024B():

        label("loc_1024B")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_1024B")

    QueueWorkItem2(0x0, 1, lambda_1024B)

    def lambda_1025D():

        label("loc_1025D")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_1025D")

    QueueWorkItem2(0x1, 1, lambda_1025D)

    def lambda_1026F():

        label("loc_1026F")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_1026F")

    QueueWorkItem2(0x2, 1, lambda_1026F)

    def lambda_10281():

        label("loc_10281")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_10281")

    QueueWorkItem2(0x3, 1, lambda_10281)

    def lambda_10293():

        label("loc_10293")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_10293")

    QueueWorkItem2(0x9, 1, lambda_10293)
    BeginChrThread(0x13, 0, 0, 34)
    BeginChrThread(0x14, 0, 0, 34)
    Sleep(3500)

    ChrTalk(
        0x9,
        (
            "#6P*sigh* We had to call on them on\x01",
            "such short notice, too. I'll have to\x01",
            "give them an extra tip later.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_10345():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10345)

    def lambda_10352():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10352)

    def lambda_1035F():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1035F)

    def lambda_1036C():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1036C)

    def lambda_10379():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_10379)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6POn that note, I have a reward for\x01",
            "all of you, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x9, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(200)
    SetChrName("")
    Sound(17, 0, 100, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Received a package from Chief Clipp.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_9B(0x1, 0x9, 0xB4, 0x1F4, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#11P#0005FOh... Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PI'll be off, then. I'm going to escort the\x01",
            "shippers from the freight company.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_104AF():

        label("loc_104AF")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_104AF")

    QueueWorkItem2(0x0, 1, lambda_104AF)

    def lambda_104C1():

        label("loc_104C1")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_104C1")

    QueueWorkItem2(0x1, 1, lambda_104C1)

    def lambda_104D3():

        label("loc_104D3")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_104D3")

    QueueWorkItem2(0x2, 1, lambda_104D3)

    def lambda_104E5():

        label("loc_104E5")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_104E5")

    QueueWorkItem2(0x3, 1, lambda_104E5)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_95(0x9, -7660, 4000, 12460, 2000, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        "#12P#0303F*sigh* Case closed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FAll this walking has made my feet\x01",
            "incredibly sore.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x1)
    TurnDirection(0x103, 0x101, 400)
    Sleep(200)

    ChrTalk(
        0x103,
        "#12P#0205FWhat is in the package, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FOh, yeah. Let me open it.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_10600():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10600)

    def lambda_1060D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1060D)

    def lambda_1061A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1061A)

    def lambda_10627():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10627)
    Sleep(400)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A Sagittarius Gem was inside the package.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xA1, 1)

    ChrTalk(
        0x103,
        "#12P#0200FThis...appears to be a rare quartz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FHelluva thing for a City Hall official\x01",
            "to have, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FYeah, I have no clue why he'd have\x01",
            "something so rare.\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -15910, 4000, 10130, 39)

    NpcTalk(
        0x9,
        "Man's Voice",
        "Oh, you're all back!\x02",
    )

    CloseMessageWindow()
    SetMapObjFlags(0x3, 0x4)

    def lambda_107BB():

        label("loc_107BB")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_107BB")

    QueueWorkItem2(0x0, 1, lambda_107BB)

    def lambda_107CD():

        label("loc_107CD")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_107CD")

    QueueWorkItem2(0x1, 1, lambda_107CD)

    def lambda_107DF():

        label("loc_107DF")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_107DF")

    QueueWorkItem2(0x2, 1, lambda_107DF)

    def lambda_107F1():

        label("loc_107F1")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_107F1")

    QueueWorkItem2(0x3, 1, lambda_107F1)
    OP_68(-12890, 5500, 12540, 2200)
    Sleep(2200)

    def lambda_10817():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10817)
    OP_68(-1650, 5500, 16000, 3500)
    OP_95(0x9, -9550, 4000, 14890, 4000, 0x0)
    OP_95(0x9, -4010, 4000, 16140, 4000, 0x0)
    OP_6F(0x1)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x9,
        (
            "#6PTell me it's true! Did you really\x01",
            "recover the statue?!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#6PThere it is! I can't believe you\x01",
            "managed to find it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWow, color me impressed. You've\x01",
            "even managed to put it back in its\x01",
            "original spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x9,
        "#6PThank you, Special Support Section!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#11P#0005FW-Wait, what? Weren't you here just\x01",
            "a second ago, Chief Clipp?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PHmm? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PI've been in a meeting for the closing\x01",
            "ceremony until just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FW-Wait a second...\x01",
            "Then that must have been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThis was all Phantom Thief B's doing.\x01",
            "He is an incredibly cunning man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FLeave it up to an infamous thief to pull off a\x01",
            "party trick like that. Catching him is gonna be\x01",
            "more than a simple game of cat and mouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PUmm, what are you guys talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PAnyway, thank you so much! Now we can\x01",
            "rest easy and hold the closing ceremony\x01",
            "without reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FGlad to hear it.\x02\x03",
            "#0003F(Phantom Thief B... I didn't sense any\x01",
            "ill intent, but that doesn't excuse the\x01",
            "fact that he's a criminal.)\x02\x03",
            "#0001F(We'll have to settle things with him\x01",
            "another time...)\x02",
        )
    )

    CloseMessageWindow()
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
            "[Urgent Request from City Hall]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, -2210, 180)
    OP_4C(0x9, 0xFF)
    OP_D5(0x1E)
    ClearMapObjFlags(0x3, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x9, -1820, 4000, 17030, 225)
    SetChrPos(0xD, -3170, 4000, 16140, 45)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xD, 0x10)
    OP_29(0x22, 0x4, 0x10)
    OP_29(0x22, 0x1, 0x7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_FD7C end

    def Function_33_10DFE(): pass

    label("Function_33_10DFE")

    OP_95(0x14, -1610, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x13, 0xB4, 0x1F4)
    Return()

    # Function_33_10DFE end

    def Function_34_10E21(): pass

    label("Function_34_10E21")

    OP_95(0xFE, -4770, 4000, 17860, 2000, 0x0)
    OP_95(0xFE, -8119, 4000, 12220, 2000, 0x0)
    Return()

    # Function_34_10E21 end

    def Function_35_10E4A(): pass

    label("Function_35_10E4A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000F(The First Division and Arios are\x01",
            "acting as security for the symposium...)\x02\x03",
            "(Let's stay out of their way.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13650, 4000, 12700, 45)
    EventEnd(0x4)
    Return()

    # Function_35_10E4A end

    def Function_36_10ED6(): pass

    label("Function_36_10ED6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 6)), scpexpr(EXPR_END)), "loc_10F73")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mayor and speaker can be heard\x01",
            "having an intense conversation behind\x01",
            "the door.\x02\x03",
            "It would be best not to disturb them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_10F73")

    Jump("loc_1116F")

    label("loc_10F78")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell State Government\x01",
            "　　 Mayor's Office\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11146")

    ChrTalk(
        0x101,
        (
            "#0000FLooks like we can find Mayor MacDowell's\x01",
            "office behind these doors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FActually, Grandfather said that we could\x01",
            "stop by his office whenever we'd like.\x02\x03",
            "I'm not sure if he's in his office right\x01",
            "now, though. He's quite the busy man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FOh, really?\x02\x03",
            "#0000FIn that case, we should go in and\x01",
            "greet him sometime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 6)
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_1116F")

    label("loc_11146")

    Sound(810, 0, 100, 0)

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

    label("loc_1116F")

    TalkEnd(0xFF)
    Return()

    # Function_36_10ED6 end

    def Function_37_11173(): pass

    label("Function_37_11173")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   Crossbell State Government\x01",
            "City Hall, Administrative District\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11225")

    ChrTalk(
        0x101,
        "#0003FWe have no reason to go inside here.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_11225")

    TalkEnd(0xFF)
    Return()

    # Function_37_11173 end

    SaveToFile()

Try(main)
