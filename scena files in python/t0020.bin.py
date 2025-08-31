from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0020.bin",                # FileName
        "t0020",                    # MapName
        "t0020",                    # Location
        0x003A,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 58, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0020",                  # 0
        "Old Man Reoir",          # 1
        "Jake",                   # 2
        "Gofan",                  # 3
        "Sealy",                  # 4
        "Keith",                  # 5
        "Keith",                  # 6
        "Alfred",                 # 7
        "Aretha",                 # 8
        "Aretha",                 # 9
        "Stefan",                 # 10
        "Stefan",                 # 11
        "Chiruru",                # 12
        "Derek",                  # 13
        "Kopan",                  # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Harold",                 # 20
        "Estelle",                # 21
        "Joshua",                 # 22
        "Bracer Lynn",            # 23
        "Bracer Aeolia",          # 24
        "Bracer Scott",           # 25
        "Arios",                  # 26
        "Tourist Brad",           # 27
        "Tourist Emillianna",     # 28
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch25200.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch24402.itc",                   # 04
        "chr/ch21002.itc",                   # 05
        "chr/ch22702.itc",                   # 06
        "chr/ch20600.itc",                   # 07
        "chr/ch09300.itc",                   # 08
        "chr/ch20502.itc",                   # 09
        "chr/ch32300.itc",                   # 0A
        "chr/ch33100.itc",                   # 0B
        "chr/ch34300.itc",                   # 0C
        "chr/ch33102.itc",                   # 0D
        "chr/ch34302.itc",                   # 0E
        "chr/ch32200.itc",                   # 0F
        "chr/ch20602.itc",                   # 10
        "chr/ch22700.itc",                   # 11
        "chr/ch23602.itc",                   # 12
        "chr/ch00602.itc",                   # 13
        "chr/ch00700.itc",                   # 14
        "chr/ch32002.itc",                   # 15
        "chr/ch32102.itc",                   # 16
        "chr/ch24400.itc",                   # 17
        "chr/ch26700.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch32400.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-40529,  0,       3470,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-48360,  0,       769,     90,   261,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-39,     0,       6039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(699,     0,       2049,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-750,    0,       1500,    90,   389,  0x0, 0,   23,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(7849,    180,     2460,    0,    341,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-2059,   180,     4000,    0,    341,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(141600,  0,       -2000,   315,  389,  0x0, 0,   17,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(139320,  500,     360,     180,  468,  0x0, 0,   6,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(142940,  0,       -769,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(139320,  300,     360,     180,  469,  0x0, 0,   16,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3390,    180,     -1909,   57,   469,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-41720,  0,       3490,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2539,   180,     1019,    240,  405,  0x0, 0,   18,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(77720,   0,       -990,    45,   389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-5150,   180,     -180,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(78529,   0,       -180,    225,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-2700,   180,     1029,    237,  469,  0x0, 0,   14,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-41930,  0,       3480,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(112559,  0,       -509,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(82040,   180,     -1399,   45,   469,  0x0, 0,   19,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(81720,   0,       219,     135,  389,  0x0, 0,   20,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-5110,   150,     -200,    90,   469,  0x0, 0,   21,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-2630,   150,     1100,    225,  469,  0x0, 0,   22,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(115069,  0,       -2319,   180,  385,  0x0, 0,   24,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-43650,  0,       -1460,   180,  385,  0x0, 0,   26,  0,   0,   0,   0,   36,  255,  0)

    DeclActor(270,     0,       4460,    1000,    -40,     1500,    6040,    0x007E, 0,  25, 0x0000)
    DeclActor(-46360,  0,       30,      1000,    -48360,  1500,    770,     0x007E, 0,  27, 0x0000)
    DeclActor(6590,    0,       8770,    1000,    6590,    2000,    8770,    0x007C, 0,  34, 0x0000)

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_5EC",          # 01, 1
        "Function_2_69D",          # 02, 2
        "Function_3_6C8",          # 03, 3
        "Function_4_9BB",          # 04, 4
        "Function_5_A14",          # 05, 5
        "Function_6_1D94",         # 06, 6
        "Function_7_1EFF",         # 07, 7
        "Function_8_229B",         # 08, 8
        "Function_9_324F",         # 09, 9
        "Function_10_333A",        # 0A, 10
        "Function_11_450E",        # 0B, 11
        "Function_12_5DED",        # 0C, 12
        "Function_13_6864",        # 0D, 13
        "Function_14_6950",        # 0E, 14
        "Function_15_7651",        # 0F, 15
        "Function_16_7D2E",        # 10, 16
        "Function_17_7EFF",        # 11, 17
        "Function_18_80BE",        # 12, 18
        "Function_19_817E",        # 13, 19
        "Function_20_8307",        # 14, 20
        "Function_21_83C3",        # 15, 21
        "Function_22_88F0",        # 16, 22
        "Function_23_8A4E",        # 17, 23
        "Function_24_8E20",        # 18, 24
        "Function_25_8F06",        # 19, 25
        "Function_26_8F0A",        # 1A, 26
        "Function_27_A5C3",        # 1B, 27
        "Function_28_A5C7",        # 1C, 28
        "Function_29_B9FC",        # 1D, 29
        "Function_30_C024",        # 1E, 30
        "Function_31_C203",        # 1F, 31
        "Function_32_C2CD",        # 20, 32
        "Function_33_C59B",        # 21, 33
        "Function_34_C806",        # 22, 34
        "Function_35_C9F7",        # 23, 35
        "Function_36_CB87",        # 24, 36
        "Function_37_CC70",        # 25, 37
        "Function_38_D28D",        # 26, 38
        "Function_39_D741",        # 27, 39
        "Function_40_F8DD",        # 28, 40
        "Function_41_10EDF",       # 29, 41
        "Function_42_11F3D",       # 2A, 42
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_574"),
        (1, "loc_580"),
        (2, "loc_58C"),
        (3, "loc_598"),
        (4, "loc_5A4"),
        (5, "loc_5B0"),
        (6, "loc_5BC"),
        (SWITCH_DEFAULT, "loc_5C8"),
    )


    label("loc_574")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_580")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_58C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_598")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5EB")

    Return()

    # Function_0_534 end

    def Function_1_5EC(): pass

    label("Function_1_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69C")
    OP_95(0xFE, 700, 0, 2050, 2000, 0x0)
    OP_95(0xFE, 6210, 0, 2640, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 2810, 0, 1030, 2000, 0x0)
    OP_95(0xFE, 3120, 0, -560, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -2050, 0, -820, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    Jump("Function_1_5EC")

    label("loc_69C")

    Return()

    # Function_1_5EC end

    def Function_2_69D(): pass

    label("Function_2_69D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_94(0xFE, 0x229CA, 0xFFFFF754, 0x23212, 0xFFFFFF9C, 0x3E8)
    Sleep(250)
    Jump("Function_2_69D")

    label("loc_6C7")

    Return()

    # Function_2_69D end

    def Function_3_6C8(): pass

    label("Function_3_6C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E0")
    Event(0, 40)

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6FE")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_721")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_766")
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -41720, 0, 3490, 90)
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_9A2")

    label("loc_766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_783")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_9A2")

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_84C")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    OP_93(0x8, 0x10E, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D5")
    SetChrPos(0x17, 84000, 180, -2040, 283)
    SetChrPos(0x19, 82190, 180, -1670, 103)
    Jump("loc_847")

    label("loc_7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_811")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 750, 0, 1500, 270)
    Jump("loc_847")

    label("loc_811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_847")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0xA, 0, 0, 3700, 360)
    SetChrFlags(0xA, 0x10)

    label("loc_847")

    Jump("loc_9A2")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_864")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_9A2")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_87C")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9A2")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8B1")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0x14, 0x80)
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8EA")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2350, 0, -720, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_9A2")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_913")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_946")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_9A2")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_974")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_9A2")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9A2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BA")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)

    label("loc_9BA")

    Return()

    # Function_3_6C8 end

    def Function_4_9BB(): pass

    label("Function_4_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9D3")
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A13")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9ED")
    Jump("loc_A13")

    label("loc_9ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_A03")
    OP_65(0x0, 0x1)
    Jump("loc_A13")

    label("loc_A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A13")
    OP_65(0x0, 0x1)

    label("loc_A13")

    Return()

    # Function_4_9BB end

    def Function_5_A14(): pass

    label("Function_5_A14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B16")

    ChrTalk(
        0xFE,
        (
            "Believe it or not, this general store was\x01",
            "founded back when my great-grandfather\x01",
            "was still kicking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always try to remind Jake of that,\x01",
            "but he never even tries to appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish he'd work with more pride.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB1")

    label("loc_B16")


    ChrTalk(
        0xFE,
        (
            "I wish Jake would work with a bit\x01",
            "more pride while on the clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometime in the future, this place is\x01",
            "going to become 'Jake's General Goods'...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB1")

    Jump("loc_1D90")

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D07")

    ChrTalk(
        0xFE,
        (
            "Jake's not exactly the hardworking sort, so I\x01",
            "always give him an earful when he slacks off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every now and again, he tells me, 'Just you\x01",
            "watch! I'll go to the city and make a name\x01",
            "for myself!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, if you have enough free time to do\x01",
            "that, why don't you just learn how to run\x01",
            "the shop properly?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DBD")

    label("loc_D07")


    ChrTalk(
        0xFE,
        (
            "Jake prattles on and on about going to\x01",
            "the city and making it big...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, if you have enough free time to do\x01",
            "that, why don't you just learn how to run\x01",
            "the shop properly?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBD")

    Jump("loc_1D90")

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED1")
    OP_4B(0x1B, 0xFF)
    TurnDirection(0xFE, 0x1B, 0)

    ChrTalk(
        0xFE,
        "As always, it's a pleasure, Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, I'll throw in an extra jar of honey,\x01",
            "on the house. Make sure to share some\x01",
            "with your family, now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3609FThank you. I'm sure they'll be head\x01",
            "over heels for this delicacy.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_F9A")

    label("loc_ED1")


    ChrTalk(
        0xFE,
        (
            "Jake's half-baked, compared to\x01",
            "a genuine man like Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After everything we endured during the Anniversary\x01",
            "Festival, I thought Jake might have matured a bit.\x01",
            "Too much to wish for, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9A")

    Jump("loc_1D90")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(
        0xFE,
        (
            "The moment tourists took the bus back to\x01",
            "the city, it got a little lonelier around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think Jake's slacking off again. Hmm,\x01",
            "is it time for another pep talk already?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E1")

    label("loc_106E")


    ChrTalk(
        0xFE,
        (
            "Leaning on the counter like that isn't\x01",
            "going to attract customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, is it time for another pep talk?\x02",
    )

    CloseMessageWindow()

    label("loc_10E1")

    Jump("loc_1D90")

    label("loc_10E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_119A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1101")
    Call(0, 7)
    Jump("loc_1195")

    label("loc_1101")


    ChrTalk(
        0xFE,
        (
            "Haha! This is the best our business\x01",
            "has done in years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We didn't even get this kinda crowd\x01",
            "during last year's festival. We must\x01",
            "be lucky!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1195")

    Jump("loc_1D90")

    label("loc_119A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1262")

    ChrTalk(
        0xFE,
        (
            "Hahaha, good thing we stocked up! These\x01",
            "tourists are buying honey by the droves\x01",
            "as presents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Business is booming. Good thing I\x01",
            "decided to go along with Derek's\x01",
            "idea after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D90")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(
        0xFE,
        (
            "Earnings from our festival food stall\x01",
            "weren't too bad for the first day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can thank Arc en Ciel for that, bringing\x01",
            "as many people to the city as they did!\x01",
            "Bwahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13DF")

    label("loc_132E")


    ChrTalk(
        0xFE,
        (
            "Thanks to Arc en Ciel, our food stall\x01",
            "started off the festival with a bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew, if this luck continued until the last day\x01",
            "of the festival, that'd blow my socks off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DF")

    Jump("loc_1D90")

    label("loc_13E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_14EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FF")
    Call(0, 7)
    Jump("loc_14E9")

    label("loc_13FF")


    ChrTalk(
        0xFE,
        (
            "Derek sure knows how to come up with\x01",
            "a smart business plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the fact that he's going to be the next\x01",
            "village chief has finally dawned on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only the same would happen to Jake,\x01",
            "regarding this general store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_1D90")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")

    ChrTalk(
        0xFE,
        (
            "Derek's plan to open a food stall during the\x01",
            "Anniversary Festival was actually genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The village has been losing that spark\x01",
            "it used to have, so maybe this food stall\x01",
            "could help bring it back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1650")

    label("loc_15D5")


    ChrTalk(
        0xFE,
        (
            "In addition to returning some of the village's\x01",
            "spirit, a food stall will be really beneficial to\x01",
            "everyone monetarily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1650")

    Jump("loc_1D90")

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176B")

    ChrTalk(
        0xFE,
        (
            "Hmm, stocking up on honey from the farther\x01",
            "out farms would probably be a good call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was planning to teach Jake the ins and\x01",
            "outs of doing inventory, but it doesn't\x01",
            "look like that's going to pan out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Busy day today, so maybe next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1812")

    label("loc_176B")


    ChrTalk(
        0xFE,
        (
            "To properly run a business, you have to\x01",
            "always be on top of your inventory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to teach Jake a thing or two about\x01",
            "that...but maybe it's still too early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1812")

    Jump("loc_1D90")

    label("loc_1817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1832")
    Call(0, 6)
    Jump("loc_197E")

    label("loc_1832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190F")

    ChrTalk(
        0xFE,
        (
            "Honestly, I wish my grandkid was ready to\x01",
            "inherit the store. I'm ready to retire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately for me, Jake can't quite\x01",
            "understand how store life works...\x01",
            "What am I going to do with that boy?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197E")

    label("loc_190F")


    ChrTalk(
        0xFE,
        (
            "Goodness. Having a grandkid who\x01",
            "stinks at his job is a struggle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to be able to retire...\x02",
    )

    CloseMessageWindow()

    label("loc_197E")

    Jump("loc_1D90")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_1C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B42")

    ChrTalk(
        0xFE,
        (
            "My store may not have been hit by those\x01",
            "wolves, but unfortunately, the damages to\x01",
            "the apiary still lost me some mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The whole thing sounds so absurd when you actually\x01",
            "think about it. I mean, if some monsters were behind it,\x01",
            "shouldn't there have been more damage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, I guess we were lucky. I'll need to give\x01",
            "an extra prayer today to thank Aidios for\x01",
            "protecting us like She did.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3A")
    SetScenarioFlags(0x68, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B3A")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1C5D")

    label("loc_1B42")


    ChrTalk(
        0xFE,
        (
            "You hear what Harold did? After hearing about the\x01",
            "tough times we've been having after the attack, he\x01",
            "came and bought Armorican goods at higher prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, honesty and trustworthiness are key\x01",
            "traits for traders to have. Harold may still be\x01",
            "young, but he's a good man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    Jump("loc_1D90")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDE")

    ChrTalk(
        0xFE,
        "Customers, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I recommend the honey, Armorica's specialty.\x01",
            "Buy as much as you'd like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D90")

    label("loc_1CDE")


    ChrTalk(
        0xFE,
        (
            "Excuse me, folks. If you need to buy\x01",
            "something, head over to the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My grandson may take a little longer to get\x01",
            "your order ready, but try to be patient with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D90")

    TalkEnd(0xFE)
    Return()

    # Function_5_A14 end

    def Function_6_1D94(): pass

    label("Function_6_1D94")


    ChrTalk(
        0xFE,
        (
            "This might be sudden, but do you folks\x01",
            "have any interest in books?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Harold gave this to me when he came to\x01",
            "restock his inventory. Thing is, I don't\x01",
            "read much nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than let the book gather dust, I'm sure\x01",
            "it'd enjoy the company of those who actually\x01",
            "read it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C7, 1)
    SetScenarioFlags(0x9C, 1)
    Return()

    # Function_6_1D94 end

    def Function_7_1EFF(): pass

    label("Function_7_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F0D")
    Jump("loc_2297")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F1B")
    Jump("loc_2297")

    label("loc_1F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F29")
    Jump("loc_2297")

    label("loc_1F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F37")
    Jump("loc_2297")

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_204F")
    OP_4B(0x8, 0xFF)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x8, 0x1A, 0)
    TurnDirection(0x1A, 0x8, 0)

    ChrTalk(
        0x1A,
        (
            "I'm thinking of buying these as souvenirs\x01",
            "for my family back in the Republic. Would\x01",
            "you mind wrapping three of them for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Quite the family man, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you'll head over to the counter, I'll get\x01",
            "everything ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_2297")

    label("loc_204F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_205D")
    Jump("loc_2297")

    label("loc_205D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_206B")
    Jump("loc_2297")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2256")
    OP_4B(0x8, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x8, 0x14, 0)
    TurnDirection(0x14, 0x8, 0)

    ChrTalk(
        0x14,
        (
            "Hmm... If we do this, we should be able\x01",
            "to set up an Anniversary Festival stall\x01",
            "with a good variety of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That monster attack hurt us, but our harvest\x01",
            "this year was more than enough to make up\x01",
            "for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have a lot of things to think about. Who's\x01",
            "going to run the stall, what we want to sell,\x01",
            "getting the best possible location...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I know. All we can do is take it\x01",
            "step by step. Now, then, we should\x01",
            "probably focus on...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x14, 0xFF)
    Jump("loc_2297")

    label("loc_2256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2264")
    Jump("loc_2297")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2272")
    Jump("loc_2297")

    label("loc_2272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2280")
    Jump("loc_2297")

    label("loc_2280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_228E")
    Jump("loc_2297")

    label("loc_228E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2297")

    label("loc_2297")

    SetScenarioFlags(0x0, 0)
    Return()

    # Function_7_1EFF end

    def Function_8_229B(): pass

    label("Function_8_229B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_253A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2486")

    ChrTalk(
        0xFE,
        "Welcome, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... Our only customers today have\x01",
            "just been our regulars so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, you guys. Repeat after me, okay?\x01",
            "'We'll take everything on the menu,\x01",
            "no exceptions!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FUh, we'll pass. Besides, I doubt we'd\x01",
            "be able to eat that much food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tch. Fine.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247E")

    ChrTalk(
        0x10A,
        (
            "#0601F(What kind of service is this...? And\x01",
            "she calls herself a waitress?!)\x02\x03",
            "#0603F(I'll take care of this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(D-Dudley, please calm down.)\x02",
    )

    CloseMessageWindow()

    label("loc_247E")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2535")

    label("loc_2486")


    ChrTalk(
        0xFE,
        (
            "Are you all right, sir? Don't forget\x01",
            "that stingy people are never\x01",
            "popular with the ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you order as much as you can\x01",
            "and help fill my family's pockets?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2535")

    Jump("loc_324B")

    label("loc_253A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_26DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264C")

    ChrTalk(
        0xFE,
        (
            "Dad seems content with going with the\x01",
            "flow, but I'd rather not live in poverty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Can't Derek come up with\x01",
            "some other plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what people may claim,\x01",
            "the food stall was the only reason\x01",
            "the village got as busy as it did.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26DA")

    label("loc_264C")


    ChrTalk(
        0xFE,
        (
            "The festival was so nice. I was working\x01",
            "nonstop, but that sweet mira was worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Can't Derek come up with\x01",
            "some other plan?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DA")

    Jump("loc_324B")

    label("loc_26DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F2")

    ChrTalk(
        0xFE,
        (
            "Right now, there are two bracers staying\x01",
            "in one of the rooms on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, there's actually a surprisingly\x01",
            "large number of female bracers, now that\x01",
            "I think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a girl myself, I can't help\x01",
            "but cheer them on!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2831")

    label("loc_27F2")


    ChrTalk(
        0xFE,
        (
            "When they eat later, maybe\x01",
            "I'll sneak them a free coffee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2831")

    Jump("loc_324B")

    label("loc_2836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2844")
    Jump("loc_324B")

    label("loc_2844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2852")
    Jump("loc_324B")

    label("loc_2852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2860")
    Jump("loc_324B")

    label("loc_2860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_286E")
    Jump("loc_324B")

    label("loc_286E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DB")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I bet the Anniversary Festival is going\x01",
            "to be crazy, all across Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If things go as planned and we get a spike\x01",
            "in customers, we'll be rolling in mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh, I'm going to be so busy...\x01",
            "We aren't exactly used to having our\x01",
            "plates full, so this might be difficult...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        "I can hear you, you know.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A7C")

    label("loc_29DB")


    ChrTalk(
        0xFE,
        (
            "If this place got any business at all,\x01",
            "we'd be a bit more prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I bet I'm worrying for nothing\x01",
            "and barely any people will show up.\x01",
            "...Maybe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7C")

    Jump("loc_324B")

    label("loc_2A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2C9F")
    TurnDirection(0xFE, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD8")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Say that again? You walked here\x01",
            "all the way from Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, my... You look like you need something\x01",
            "to eat. I'll take your order as soon as you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father may look like a boring old man,\x01",
            "but his cooking is divine, I assure you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        "I can still hear you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C9A")

    label("loc_2BD8")


    ChrTalk(
        0xFE,
        (
            "I have an idea! Why don't you\x01",
            "try ordering the most expensive\x01",
            "thing on the menu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I promise, it's absolutely to die for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm sure it's great, but I'll pass.\x01",
            "I don't have the mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9A")

    Jump("loc_324B")

    label("loc_2C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D86")

    ChrTalk(
        0xFE,
        (
            "One of our regulars, Alfred, gets along\x01",
            "pretty well with my dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever the inn is especially slow,\x01",
            "I always see them chatting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess that must be a benefit of running\x01",
            "your own business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DFF")

    label("loc_2D86")


    ChrTalk(
        0xFE,
        "Alfred gets along really well with my dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I had my way, he'd spend that\x01",
            "energy working instead of talking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFF")

    Jump("loc_324B")

    label("loc_2E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2F93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC6")

    ChrTalk(
        0xFE,
        (
            "I feel like every time I work, Alfred\x01",
            "and Keith are here, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they love this place so much,\x01",
            "they might as well order meals\x01",
            "one after the other, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F8E")

    label("loc_2EC6")


    ChrTalk(
        0xFE,
        (
            "I guess business isn't too crazy\x01",
            "during the day, so them loitering\x01",
            "isn't TOO big a deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but they still ought to order something.\x01",
            "We don't make a living off anyone\x01",
            "loitering, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8E")

    Jump("loc_324B")

    label("loc_2F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308D")

    ChrTalk(
        0xFE,
        (
            "Mr. Hayworth told us that he's going\x01",
            "to be heading home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't you just love him? He's so\x01",
            "kind, genuine, and handsome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can you believe he's married? He even\x01",
            "has a kid! Oh, I am SO jealous of his wife.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30FC")

    label("loc_308D")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Mr. Hayworth,\x01",
            "he's up on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I hope he comes back soon...\x02",
    )

    CloseMessageWindow()

    label("loc_30FC")

    Jump("loc_324B")

    label("loc_3101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_324B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B2")

    ChrTalk(
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, you're first time customers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've caught us during our slow hour.\x01",
            "Take your time to look over the menu, okay? ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_324B")

    label("loc_31B2")


    ChrTalk(
        0xFE,
        (
            "My dad's cooking is legitimately amazing.\x01",
            "Order something, if you feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you order something, your energy\x01",
            "will come back in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324B")

    TalkEnd(0xFE)
    Return()

    # Function_8_229B end

    def Function_9_324F(): pass

    label("Function_9_324F")

    TalkBegin(0xFE)

    ChrTalk(
        0xC,
        (
            "I've somehow ended up making things more\x01",
            "complicated than they needed to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I just wanted to impress Gofan, but\x01",
            "maybe I rushed things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Still, I'm glad that a bracer is going\x01",
            "to be there to help out the police.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_324F end

    def Function_10_333A(): pass

    label("Function_10_333A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33CE")
    Jump("loc_3418")

    label("loc_33CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3418")

    label("loc_33EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_340E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3418")

    label("loc_340E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3418")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_360C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A3")

    ChrTalk(
        0xFE,
        (
            "Sealy's charm lies in that she doesn't\x01",
            "pretend to be some kind of angel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When she tries to get customers to buy\x01",
            "something expensive, she's honest.\x01",
            "And that's really refreshing.\x02",
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
        "#0211FWhat a peculiar taste in women...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3607")

    label("loc_35A3")


    ChrTalk(
        0xFE,
        (
            "Sealy's charm lies in that she doesn't\x01",
            "pretend to be some kind of angel and\x01",
            "that she's honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3607")

    Jump("loc_4506")

    label("loc_360C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_36E1")

    ChrTalk(
        0xFE,
        (
            "I was loitering in the inn after only buying\x01",
            "a cup of coffee, so Sealy came and hit\x01",
            "me with her feather duster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can order a light meal, I guess. After all,\x01",
            "that girl sure loves her mira.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4506")

    label("loc_36E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3819")

    ChrTalk(
        0xFE,
        (
            "*sigh* Just being in the presence of\x01",
            "Sealy as she's working soothes my\x01",
            "pounding heart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to savor my time with Sealy\x01",
            "to make up for our separation during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FIt's been a month since the festival\x01",
            "ended...and you still aren't satisfied?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3877")

    label("loc_3819")


    ChrTalk(
        0xFE,
        (
            "*sigh* Just being in the presence of\x01",
            "Sealy as she's working soothes my\x01",
            "pounding heart...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3877")

    Jump("loc_4506")

    label("loc_387C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392E")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Just kill me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No. Cheer up, me! Come tomorrow,\x01",
            "Sealy will be back in the village, and\x01",
            "everything will be right in the world!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39B1")

    label("loc_392E")


    ChrTalk(
        0xFE,
        (
            "Not having my daily dose of Sealy\x01",
            "for five whole days was horrible...but\x01",
            "that ends today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come home, my dearest Sealy...\x02",
    )

    CloseMessageWindow()

    label("loc_39B1")

    Jump("loc_4506")

    label("loc_39B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3B74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A73")

    ChrTalk(
        0xD,
        "I'm glad that couple didn't get hurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If something happened to customers\x01",
            "while Sealy was in Crossbell City,\x01",
            "she'd be pretty depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Probably.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B6F")

    label("loc_3A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B06")

    ChrTalk(
        0xFE,
        (
            "When I look around, I see Gofan,\x01",
            "Alfred, and a few random tourists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only thing that's missing is my\x01",
            "sweet Sealy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B6F")

    label("loc_3B06")


    ChrTalk(
        0xFE,
        (
            "I know Sealy isn't here, but I can't\x01",
            "help but still come to the inn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel so empty inside.\x02",
    )

    CloseMessageWindow()

    label("loc_3B6F")

    Jump("loc_4506")

    label("loc_3B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C04")

    ChrTalk(
        0xFE,
        (
            "*sigh* I wonder what she's\x01",
            "doing right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never knew this inn would be\x01",
            "so lonely without her here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C4A")

    label("loc_3C04")


    ChrTalk(
        0xFE,
        (
            "Can't the Anniversary Festival end\x01",
            "and return my Sealy to me...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4A")

    Jump("loc_4506")

    label("loc_3C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3D2C")

    ChrTalk(
        0xFE,
        (
            "H-How would I have ever guessed that\x01",
            "Sealy would go work at the food stall...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And she's working it with Derek?!\x01",
            "Together?! ALONE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it! If I wasn't busy with work,\x01",
            "I'd run to her rescue!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4506")

    label("loc_3D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DCC")

    ChrTalk(
        0xFE,
        (
            "I'm really afraid of the Ash Tree Inn\x01",
            "getting too crowded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What would I do if everyone got\x01",
            "mesmerized by Sealy's beauty?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E3E")

    label("loc_3DCC")


    ChrTalk(
        0xFE,
        (
            "I bet if new customers come here,\x01",
            "they'll all fall in love with Sealy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, no tourists this year.\x02",
    )

    CloseMessageWindow()

    label("loc_3E3E")

    Jump("loc_4506")

    label("loc_3E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_402E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F60")

    ChrTalk(
        0xFE,
        (
            "From what I can tell, Sealy seems\x01",
            "to really like Mr. Hayworth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'As if I'd ever let Sealy get swept away\x01",
            "by a married man like you!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At least, that's what I WOULD say,\x01",
            "but he's always so nice to us. I can't\x01",
            "really say anything bad about him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4029")

    label("loc_3F60")


    ChrTalk(
        0xFE,
        (
            "A-Anyway, in order to win over\x01",
            "Sealy, I'm going to start coming\x01",
            "to the inn every single day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But still...Mr. Hayworth is in a much\x01",
            "higher league than me. He's going\x01",
            "to be a formidable rival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4029")

    Jump("loc_4506")

    label("loc_402E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40FC")

    ChrTalk(
        0xFE,
        (
            "*sigh* Sealy looks even cuter\x01",
            "than usual, today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? Wolves? Why the heck\x01",
            "would I care about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't mind, you're cutting\x01",
            "into my daily time in heaven.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_418B")

    label("loc_40FC")


    ChrTalk(
        0xFE,
        (
            "*sigh* Sealy looks even cuter\x01",
            "than usual, today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if Armorica Village goes under,\x01",
            "as long as Sealy is here, I'll be a\x01",
            "happy man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418B")

    Jump("loc_4506")

    label("loc_4190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_4303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426E")

    ChrTalk(
        0xFE,
        (
            "With Sealy working here and Gofan's\x01",
            "top-notch cooking, this inn has cemented\x01",
            "itself as the greatest place ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't exactly have enough mira to\x01",
            "come here as much as I want, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42FE")

    label("loc_426E")


    ChrTalk(
        0xFE,
        (
            "Sealy's glances are becoming\x01",
            "too much to bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My budget's looking tight this month, but,\x01",
            "for her sake, I had better order something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42FE")

    Jump("loc_4506")

    label("loc_4303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_44BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441F")

    ChrTalk(
        0xFE,
        "Huh? You want information on those wolves?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the fields that I'm in charge of were\x01",
            "damaged a little bit, so that wasn't great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bear in mind, no one actually saw the beasts,\x01",
            "so they might be smarter than we think.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4417")
    SetScenarioFlags(0x68, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4417")

    SetScenarioFlags(0x0, 2)
    Jump("loc_44BA")

    label("loc_441F")


    ChrTalk(
        0xFE,
        (
            "The fields that I'm in charge of were\x01",
            "damaged a bit by the wolves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It was definitely a challenge to get\x01",
            "everything back in working order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44BA")

    Jump("loc_4506")

    label("loc_44BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4506")

    ChrTalk(
        0xFE,
        "Sealy is just so adorable!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Her smile gives me life!\x02",
    )

    CloseMessageWindow()

    label("loc_4506")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_333A end

    def Function_11_450E(): pass

    label("Function_11_450E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45A2")
    Jump("loc_45EC")

    label("loc_45A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45C2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45EC")

    label("loc_45C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45EC")

    label("loc_45E2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45EC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4716")

    ChrTalk(
        0xFE,
        (
            "My book ended up getting passed\x01",
            "around like mira at a market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the blame does fall on me\x01",
            "for giving it out in the first place...\x01",
            "I'm really sorry, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, I'll respect the\x01",
            "library's policies.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_4716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F6")

    ChrTalk(
        0xFE,
        (
            "Gofan lent the book to Elkin, the guy\x01",
            "who's always messing with the orbal\x01",
            "truck near the village entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry, everyone. I know that this\x01",
            "has cost you a lot of time and effort.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_47F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4817")
    Call(0, 42)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_4817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494D")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I wasn't sure at first, but Gambler Jack\x01",
            "ended up being really engaging.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        "Oh, you finally finished it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm a big fan of that novel as well.\x01",
            "Once I finish cleaning up the store,\x01",
            "tell me what you thought of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sure. I'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_49FD")

    label("loc_494D")


    ChrTalk(
        0xFE,
        (
            "Maybe I should read it one more\x01",
            "time, front to back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang. I went and checked out a lot\x01",
            "of books from the library, but I doubt\x01",
            "I'll find the time to finish them all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49FD")

    Jump("loc_5DE5")

    label("loc_4A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB5")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Gambler Jack is starting to hook me.\x01",
            "I can't wait to see how it ends.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        (
            "Hey, I know that book. If I remember\x01",
            "correctly, Jack ends up--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, stop it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spoiling someone on how a story\x01",
            "ends is unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, how many times do I have\x01",
            "to tell you before you break that nasty\x01",
            "habit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "S-Sorry, Alfred. You won't hear a peep\x01",
            "out of me about it anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C52")

    label("loc_4BB5")


    ChrTalk(
        0xFE,
        (
            "There's nothing worse than spoiling\x01",
            "someone on how a story ends, or\x01",
            "what its big twist is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may be good friends with Gofan,\x01",
            "but he needs to stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C52")

    Jump("loc_5DE5")

    label("loc_4C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4D64")

    ChrTalk(
        0xFE,
        (
            "I borrowed so many different books\x01",
            "from Crossbell City's library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were too many good ones to\x01",
            "choose from, so I accidentally checked\x01",
            "out more books than I can handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're due back in three days...\x01",
            "Hopefully, I can finish them all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE5")

    label("loc_4D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E13")

    ChrTalk(
        0xFE,
        (
            "The inn has finally returned to peace\x01",
            "and quiet right as I finished the book\x01",
            "I've been reading...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should grab a bite to\x01",
            "eat, now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E77")

    label("loc_4E13")


    ChrTalk(
        0xFE,
        "Was the book's due date tomorrow...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City is always way too\x01",
            "crowded nowadays...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E77")

    Jump("loc_5DE5")

    label("loc_4E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5129")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F0B")

    ChrTalk(
        0xE,
        "Phew. I think it's time for a breather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stupid Gofan, working me to the bone\x01",
            "just because we're friends...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5124")

    label("loc_4F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5086")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        "Hmm...oh? Hmmm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        (
            "Alfred. You still reading that\x01",
            "Arc en Ciel book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Must be a real page-turner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really difficult to check this particular\x01",
            "book out from the library, so I intend to\x01",
            "savor the read before I have to return it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On another note, these pictures of\x01",
            "Ilya Platiere are quite nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Easy, boy.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5124")

    label("loc_5086")


    ChrTalk(
        0xFE,
        (
            "Hmm, I see. This book was published\x01",
            "before the up-and-comer Rixia Mao\x01",
            "joined the troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I could have seen photos of\x01",
            "her, too. What a shame.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5124")

    Jump("loc_5DE5")

    label("loc_5129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52CC")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "This Arc en Ciel fan book was surprisingly\x01",
            "elusive. I had to look for it everywhere\x01",
            "before I actually found it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        (
            "Huh. I never would have guessed\x01",
            "a book like that'd be at the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the looks of it, it was put together\x01",
            "by some Arc en Ciel superfans and was\x01",
            "a limited-time printing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm half tempted to keep it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Whoa, you can't do that.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_536C")

    label("loc_52CC")


    ChrTalk(
        0xFE,
        (
            "Think about it. Because of the book's\x01",
            "popularity, I may never be able to check\x01",
            "it out again. Ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. I'll just take my sweet time\x01",
            "reading it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536C")

    Jump("loc_5DE5")

    label("loc_5371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_548E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F9")

    ChrTalk(
        0xFE,
        "I'm almost done with today's work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I take a look around Crossbell\x01",
            "City in the afternoon...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5489")

    label("loc_53F9")


    ChrTalk(
        0xFE,
        (
            "I think I'm going to try and catch the\x01",
            "bus to Crossbell City later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just really itching to check out\x01",
            "a new book from the library.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5489")

    Jump("loc_5DE5")

    label("loc_548E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_563B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B0")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Kitty-Talk for Dummies...\x01",
            "That's an interesting title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nya~~go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nya~~.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        (
            "Hey, Alfred. You aren't saying\x01",
            "something nasty, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. If you want to know what I said,\x01",
            "you should try reading the book.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5636")

    label("loc_55B0")


    ChrTalk(
        0xFE,
        (
            "Is the library going to open during\x01",
            "the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if I could still check out\x01",
            "books if I wanted to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5636")

    Jump("loc_5DE5")

    label("loc_563B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D9")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        "Hmm... Carnelia was a pretty solid read.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        (
            "Carnelia? I heard that book\x01",
            "was quite the hit back when it\x01",
            "first came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's supposedly based on a true story, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "True story or not, it was still really\x01",
            "enjoyable to read through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a good read, plain and simple,\x01",
            "and that's all I can ask for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, that's interesting, I suppose...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5830")

    label("loc_57D9")


    ChrTalk(
        0xFE,
        "Now, what to read next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There WAS one book that I've\x01",
            "been meaning to read...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5830")

    Jump("loc_5DE5")

    label("loc_5835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FF")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "'Fine Dining in Crossbell City'...\x01",
            "I've heard it covers all the best\x01",
            "restaurants in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    ChrTalk(
        0xA,
        "Hey, Alfred. I can hear you, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I know. Maybe if you keep working\x01",
            "hard, you'll be featured in a book like\x01",
            "that someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Isn't it just limited to restaurants in the city?\x01",
            "My inn may not be in it, but I promise you,\x01",
            "none of those places can match my cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, of course.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A83")

    label("loc_59FF")


    ChrTalk(
        0xFE,
        (
            "For my next read...maybe I should\x01",
            "try to borrow a new novel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll go visit the Crossbell City Library\x01",
            "next time I'm free.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A83")

    Jump("loc_5DE5")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5BCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4D")

    ChrTalk(
        0xFE,
        (
            "Now, in the meantime, I need to\x01",
            "finish up my current book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "'Fine Dining in Crossbell City'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Maybe reading it here would\x01",
            "give Gofan the wrong idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5BC6")

    label("loc_5B4D")


    ChrTalk(
        0xFE,
        (
            "The Crossbell City Library has a wide\x01",
            "selection of books to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why don't you go check something out?\x02",
    )

    CloseMessageWindow()

    label("loc_5BC6")

    Jump("loc_5DE5")

    label("loc_5BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE6")
    Call(0, 12)
    Jump("loc_5DD7")

    label("loc_5BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D20")

    ChrTalk(
        0xFE,
        (
            "The day before the attack, everyone in\x01",
            "the village went to sleep early because\x01",
            "we had to wake up at dawn for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#1PIt was like the monsters were waiting\x01",
            "for the perfect time to strike...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say whatever you want. We were just unlucky.\x01",
            "That's the only explanation that makes sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DD7")

    label("loc_5D20")


    ChrTalk(
        0xFE,
        (
            "The damages to the village as a whole\x01",
            "ended up being not that serious. That's\x01",
            "something to be thankful for, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really hope this doesn't happen to us\x01",
            "again, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD7")

    Jump("loc_5DE5")

    label("loc_5DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5DE5")

    label("loc_5DE5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_450E end

    def Function_12_5DED(): pass

    label("Function_12_5DED")

    EventBegin(0x0)
    Fade(500)
    OP_68(360, 1500, 3610, 0)
    MoveCamera(312, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22780, 0)
    SetChrPos(0x101, -470, 0, 2360, 0)
    SetChrPos(0x102, -1200, 0, 1520, 0)
    SetChrPos(0x103, 880, 0, 1830, 0)
    SetChrPos(0x104, 80, 0, 1070, 0)
    SetChrFlags(0xB, 0x80)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xE,
        "#5P*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYour omelet rice is the real deal, Gofan.\x01",
            "If I could have a plate of this on my\x01",
            "deathbed, I could die happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHaha. Good to hear the cooking is\x01",
            "worth the effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#6PExcuse us. Sorry to interrupt.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    Fade(500)
    SetChrSubChip(0xE, 0x2)
    OP_93(0xE, 0x5A, 0x0)
    OP_0D()

    ChrTalk(
        0xA,
        "#11PCan I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F#6PYes, actually. You see, we're from the\x01",
            "Crossbell Police Department.\x02\x03",
            "#0001FWe were curious to know if you had\x01",
            "any details regarding the wolf attack.\x01",
            "Can you remember anything at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PThat incident three weeks ago, you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PFrom what I remember, everyone had\x01",
            "work pretty early the next day, so we\x01",
            "were all asleep by that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PIf you think about it, it's almost as if\x01",
            "they knew exactly when to attack...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnyway, the village was just unlucky.\x01",
            "That's the only way I can make sense\x01",
            "of this craziness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PThat's about all I'd be able to tell you, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PMost of the guests I've talked to didn't see\x01",
            "anything, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F#6PThat's unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F#6PAnd here I was hopin' for some solid\x01",
            "evidence right off the bat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F#5PWell, that's how most investigations go.\x01",
            "Answers only show up when you're patient\x01",
            "and steadily gather information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F#6PThat may be, but do you think\x01",
            "we can take a break?\x02\x03",
            "#0211FMy stomach is going to implode.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11POh, you folks haven't eaten yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThis is the perfect opportunity to get\x01",
            "you four hooked on the inn's specialty\x01",
            "omelet rice. The bill's on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F#6PNo, that's not necessary, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIt's fine! Just think of it as my way\x01",
            "of making some new friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POr just think of it as a marketing tactic!\x01",
            "Next time you visit Armorica Village,\x01",
            "come stop by the Ash Tree Inn for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F#6PHaha! Can't refuse that generosity, can we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F#6PLloyd, we might as well take him up\x01",
            "on his kind offer, if that's the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204F#6PI second that notion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F#6PWell...okay, I guess.\x02\x03",
            "#0002FWe'd love some omelet rice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PIt'd be my pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWhy don't you folks find yourselves an\x01",
            "empty table while I whip up your meal?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In only a few minutes, four steaming plates of omelet\x01",
            "rice were brought to the group's table.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and others, after savoring the deliciously simple\x01",
            "meal, felt completely recovered from their hike to\x01",
            "Armorica Village.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sleep(1000)
    Sound(13, 0, 100, 0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(4000)
    OP_1F()
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0x0, -260, 0, 2660, 0)
    ClearChrFlags(0xB, 0x80)
    SetScenarioFlags(0x69, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_12_5DED end

    def Function_13_6864(): pass

    label("Function_13_6864")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Stefan has never gotten much exercise,\x01",
            "so imagine my surprise to see him running\x01",
            "around the village like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so happy for him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like he's finally starting to become\x01",
            "friends with the village children.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_6864 end

    def Function_14_6950(): pass

    label("Function_14_6950")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69E4")
    Jump("loc_6A2E")

    label("loc_69E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A04")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A2E")

    label("loc_6A04")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A24")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A2E")

    label("loc_6A24")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A2E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B25")

    ChrTalk(
        0xFE,
        (
            "Stefan has gone out to play with\x01",
            "Camille today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we lived in Crossbell City, he was\x01",
            "always so quiet and frail, but maybe the\x01",
            "change of scenery is doing him some good...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6BB7")

    label("loc_6B25")


    ChrTalk(
        0xFE,
        (
            "I'm glad that Stefan is starting to play\x01",
            "outside more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to go to Ange's house next\x01",
            "time to thank them for putting up\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BB7")

    Jump("loc_7649")

    label("loc_6BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6BCA")
    Jump("loc_7649")

    label("loc_6BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6C74")

    ChrTalk(
        0xFE,
        (
            "Stefan has been playing with the village\x01",
            "kids quite often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe our official move to Armorica\x01",
            "Village isn't as far away as I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7649")

    label("loc_6C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DAE")

    ChrTalk(
        0xFE,
        (
            "Stefan and I had a fun time at the festival.\x01",
            "We also made sure to return before we ran\x01",
            "into the closing ceremony's crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a wonderful time, but fighting the\x01",
            "city's crowds every day left me exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* The village atmosphere soothes\x01",
            "my soul like nothing else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6E67")

    label("loc_6DAE")


    ChrTalk(
        0xFE,
        (
            "Stefan told me he was going over to\x01",
            "give his friends souvenirs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wasn't expecting that, to be honest.\x01",
            "Maybe Stefan has finally come to\x01",
            "appreciate living in Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E67")

    Jump("loc_7649")

    label("loc_6E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6E7A")
    Jump("loc_7649")

    label("loc_6E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E88")
    Jump("loc_7649")

    label("loc_6E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6E96")
    Jump("loc_7649")

    label("loc_6E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FBA")

    ChrTalk(
        0xFE,
        (
            "I've heard that the village is going to\x01",
            "set up a food stall for the festival.\x01",
            "I can't wait to see how it'll turn out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son is dying to go back to\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've really acclimated to life in\x01",
            "Armorica, but maybe visiting Crossbell\x01",
            "City wouldn't be so bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7649")

    label("loc_6FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_712F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709F")

    ChrTalk(
        0xFE,
        (
            "Arc en Ciel? I went to see them\x01",
            "more times than I can count...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya Platiere's performance is so\x01",
            "incredible, it would cause even\x01",
            "Aidios to faint in awe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I would love to see them again...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_712A")

    label("loc_709F")


    ChrTalk(
        0xFE,
        (
            "Ah, the lovely Ilya Platiere... ㈱\x01",
            "The last time I saw one of her\x01",
            "shows, I was moved to tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I would love to see them again...\x02",
    )

    CloseMessageWindow()

    label("loc_712A")

    Jump("loc_7649")

    label("loc_712F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725C")

    ChrTalk(
        0xFE,
        (
            "We're still conflicted on whether moving\x01",
            "here is the right decision or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The owner of this place told us he had\x01",
            "a spare room open. He's letting us\x01",
            "rent it for cheap right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One thing is for sure. This place\x01",
            "is radically different than life in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7321")

    label("loc_725C")


    ChrTalk(
        0xFE,
        (
            "We're still conflicted on whether moving\x01",
            "here is the right decision or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to the owner, my son and I have\x01",
            "been able to stay here in order to figure out\x01",
            "if it will be a good fit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7321")

    Jump("loc_7649")

    label("loc_7326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_7438")

    ChrTalk(
        0xFE,
        (
            "A quaint life living in the countryside has\x01",
            "always been my dream, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...if these monster attacks are a common\x01",
            "occurrence, maybe it would be safer to\x01",
            "simply stay in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite that, this calm, quiet lifestyle is\x01",
            "hard to give up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7649")

    label("loc_7438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_7540")

    ChrTalk(
        0xFE,
        (
            "The recent attack gave me quite the fright.\x01",
            "Considering how peaceful it was that night,\x01",
            "I could hardly believe my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know we're living out in the countryside,\x01",
            "but it's still a bit unnerving to see monsters\x01",
            "wander into civilized areas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7649")

    label("loc_7540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7649")

    ChrTalk(
        0xFE,
        "Oh, did you come from the city, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son and I have been staying\x01",
            "in Armorica Village for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A calm place, free from the hustle and bustle\x01",
            "of the city... This is the life I've longed for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps we'll move here, after all.\x02",
    )

    CloseMessageWindow()

    label("loc_7649")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_6950 end

    def Function_15_7651(): pass

    label("Function_15_7651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7662")
    Jump("loc_7D2A")

    label("loc_7662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7670")
    Jump("loc_7D2A")

    label("loc_7670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_767E")
    Jump("loc_7D2A")

    label("loc_767E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_768C")
    Jump("loc_7D2A")

    label("loc_768C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_769A")
    Jump("loc_7D2A")

    label("loc_769A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_76A8")
    Jump("loc_7D2A")

    label("loc_76A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_76B6")
    Jump("loc_7D2A")

    label("loc_76B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7772")

    ChrTalk(
        0xFE,
        (
            "Hopefully, we'll be able to go back to\x01",
            "Crossbell City during the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure would be nice if Mom changed\x01",
            "her mind about moving to the village,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2A")

    label("loc_7772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_793D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D2")

    ChrTalk(
        0xFE,
        (
            "You know those two siblings who are always\x01",
            "playing in the square? They keep inviting me\x01",
            "to hang out, but I'm not really interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter the day, they always end up\x01",
            "wanting to play bracers. I can't take it\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These country kids are just plain annoying.\x01",
            "*sigh* I want to go back to Crossbell City...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7938")

    label("loc_78D2")


    ChrTalk(
        0xFE,
        (
            "We may be the same age, but the kids\x01",
            "here are so annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to go back to the city...\x02",
    )

    CloseMessageWindow()

    label("loc_7938")

    Jump("loc_7D2A")

    label("loc_793D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7A39")

    ChrTalk(
        0xFE,
        "The people here are TOO nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We never told the villagers that we were\x01",
            "for sure moving here, but they're already\x01",
            "treating us like we're neighbors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to move here. I'd go crazy\x01",
            "living out in the sticks like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2A")

    label("loc_7A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_7B24")

    ChrTalk(
        0xFE,
        (
            "That monster attack has my mom questioning\x01",
            "whether we should move here or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, come tomorrow, I bet she'll have forgotten\x01",
            "the entire thing. She's not the type of person to\x01",
            "worry about stuff for very long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2A")

    label("loc_7B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_7C06")

    ChrTalk(
        0xFE,
        (
            "Darned wolves sneaking into the village?\x01",
            "Something that outrageous would never\x01",
            "happen in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* This entire situation sucks.\x01",
            "Why the heck would my mom want\x01",
            "to move to a place like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2A")

    label("loc_7C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C8D")

    ChrTalk(
        0xFE,
        "Stupid fields, as far as the eye can see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we have to move, I'd much rather\x01",
            "move to Mishelam.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7D2A")

    label("loc_7C8D")


    ChrTalk(
        0xFE,
        (
            "This place has no department store,\x01",
            "no theater, and even had a monster\x01",
            "attack a while back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Wake me up when we're back\x01",
            "in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D2A")

    TalkEnd(0xFE)
    Return()

    # Function_15_7651 end

    def Function_16_7D2E(): pass

    label("Function_16_7D2E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DC2")
    Jump("loc_7E0C")

    label("loc_7DC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7DE2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E0C")

    label("loc_7DE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E02")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E0C")

    label("loc_7E02")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E0C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ED6")

    ChrTalk(
        0xFE,
        "Owwww, my poor legs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ran way too much yesterday and now my\x01",
            "legs feel like gelatin. Whew, I'm tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still, it was a lot of fun...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7EF7")

    label("loc_7ED6")


    ChrTalk(
        0xFE,
        "Yesterday was pretty fun...\x02",
    )

    CloseMessageWindow()

    label("loc_7EF7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_7D2E end

    def Function_17_7EFF(): pass

    label("Function_17_7EFF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F93")
    Jump("loc_7FDD")

    label("loc_7F93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7FB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FDD")

    label("loc_7FB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FDD")

    label("loc_7FD3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FDD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "The pleasant smells of the pastures,\x01",
            "chicken, and honey all persuaded\x01",
            "me into coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm positive that there are good meals\x01",
            "hiding here. I just need to ask around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_7EFF end

    def Function_18_80BE(): pass

    label("Function_18_80BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80D3")
    Call(0, 7)
    Jump("loc_817A")

    label("loc_80D3")


    ChrTalk(
        0xFE,
        (
            "Hmm... Setting up a food stall may\x01",
            "be harder than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that doesn't matter! I'm going to reenergize\x01",
            "this village, no matter the costs! You'll see!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_817A")

    TalkEnd(0xFE)
    Return()

    # Function_18_80BE end

    def Function_19_817E(): pass

    label("Function_19_817E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8212")
    Jump("loc_825C")

    label("loc_8212")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8232")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_825C")

    label("loc_8232")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8252")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_825C")

    label("loc_8252")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_825C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "All right, now that I've sated my\x01",
            "appetite with a big meal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's time to drop my line\x01",
            "and see what bites.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_817E end

    def Function_20_8307(): pass

    label("Function_20_8307")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You know what? I had no idea that\x01",
            "this village was such an amazing place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could definitely see myself spending\x01",
            "my later years relaxing in this kind of\x01",
            "calm environment.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_8307 end

    def Function_21_83C3(): pass

    label("Function_21_83C3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8457")
    Jump("loc_84A1")

    label("loc_8457")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8477")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84A1")

    label("loc_8477")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8497")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84A1")

    label("loc_8497")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_84A1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_86CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D6")

    ChrTalk(
        0xFE,
        (
            "We were intending to return to\x01",
            "Calvard today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...ever since yesterday, my girlfriend\x01",
            "has been begging me to let us stay\x01",
            "in Crossbell for a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn that stupid bracer... What has\x01",
            "he done to my girlfriend?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_86C5")

    label("loc_85D6")


    ChrTalk(
        0xFE,
        (
            "Is this the price I have to pay for\x01",
            "leaving my girlfriend behind...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to bring her back to the Republic\x01",
            "by force at the rate this is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe this is a good chance to make\x01",
            "her remember my charms all over again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86C5")

    Jump("loc_88E8")

    label("loc_86CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_877A")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys... I forgot to mention it\x01",
            "before, but I wanted to thank you all\x01",
            "for saving us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you hadn't shown up, I'd be...\x01",
            "*shudder*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87FB")

    label("loc_877A")


    ChrTalk(
        0xFE,
        (
            "A-Anyway...\x01",
            "My girlfriend has been acting really\x01",
            "weird ever since then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her face is so red... Do you think\x01",
            "she's okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87FB")

    Jump("loc_88E8")

    label("loc_8800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8898")

    ChrTalk(
        0xFE,
        (
            "I already ate this stuff at their food\x01",
            "stall, but it definitely tastes way\x01",
            "better here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yep. Coming here was a genius idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88E8")

    label("loc_8898")


    ChrTalk(
        0xFE,
        (
            "Everything is so tasty and delicious.\x01",
            "Coming here was definitely worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88E8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_83C3 end

    def Function_22_88F0(): pass

    label("Function_22_88F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C5")

    ChrTalk(
        0xFE,
        (
            "The view of the fields next to the\x01",
            "village chief's house is breathtaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I stayed holed up in Crossbell City during\x01",
            "the festival, I never would have seen such a\x01",
            "beautiful sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8A4A")

    label("loc_89C5")


    ChrTalk(
        0xFE,
        (
            "Crossbell City is incredibly busy\x01",
            "right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care for crowds...so I think visiting\x01",
            "Armorica was a good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4A")

    TalkEnd(0xFE)
    Return()

    # Function_22_88F0 end

    def Function_23_8A4E(): pass

    label("Function_23_8A4E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AE2")
    Jump("loc_8B2C")

    label("loc_8AE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B02")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B2C")

    label("loc_8B02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B2C")

    label("loc_8B22")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B2C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8D09")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8C")

    ChrTalk(
        0xFE,
        (
            "Listen, you better stop slandering\x01",
            "Scott's good name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's ten times the man you could\x01",
            "ever hope to be! You left me behind and\x01",
            "ran away in my time of need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Th-This is a massive misunderstanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Dear, I'm begging you. Let's just go\x01",
            "back home to Calvard already...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8D04")

    label("loc_8C8C")


    ChrTalk(
        0xFE,
        (
            "*sigh* But if we go back to the Republic,\x01",
            "I'll never be able to see Scott again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't want to go home...\x02",
    )

    CloseMessageWindow()

    label("loc_8D04")

    Jump("loc_8E18")

    label("loc_8D09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D9B")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D79")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So his name is Scott...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mmm... ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Did you just moan?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8D96")

    label("loc_8D79")


    ChrTalk(
        0xFE,
        "Scott...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mmm... ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_8D96")

    Jump("loc_8E18")

    label("loc_8D9B")


    ChrTalk(
        0xFE,
        (
            "All the cuisine here seems to suit\x01",
            "my boyfriend's palate quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe we should stop by\x01",
            "here again next year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E18")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_8A4E end

    def Function_24_8E20(): pass

    label("Function_24_8E20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E35")
    Call(0, 7)
    Jump("loc_8F02")

    label("loc_8E35")


    ChrTalk(
        0xFE,
        (
            "Yesterday, I kept hearing about Armorica\x01",
            "Village's famous apiary so much, I couldn't\x01",
            "help but start craving for some honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I have to do is carry all this home...\x01",
            "It is pretty heavy, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F02")

    TalkEnd(0xFE)
    Return()

    # Function_24_8E20 end

    def Function_25_8F06(): pass

    label("Function_25_8F06")

    Call(0, 26)
    Return()

    # Function_25_8F06 end

    def Function_26_8F0A(): pass

    label("Function_26_8F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F23")
    Call(0, 39)
    Return()

    label("loc_8F23")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5BF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F90")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8F90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB0")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5BA")

    label("loc_8FB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD0")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A5BA")

    label("loc_8FD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FE4")
    Jump("loc_A5BA")

    label("loc_8FE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5BA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_909E")

    ChrTalk(
        0xA,
        (
            "You found the book? Oh, that's a\x01",
            "weight off my shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Believe me, I won't be loaning things\x01",
            "that aren't mine from now on.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_909E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_913A")

    ChrTalk(
        0xA,
        (
            "I'm really sorry that I let Elkin\x01",
            "borrow the book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't refuse a longtime customer's\x01",
            "requests that easily after all.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_913A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_932E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_925E")

    ChrTalk(
        0xA,
        (
            "Welcome, everyone. Want to look\x01",
            "at one of our breakfast menus?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hey, Gofan! I'll have my usual!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 500)

    ChrTalk(
        0xA,
        (
            "Keith, can't you see I'm in the middle\x01",
            "of talking to some customers?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Sorry about that. Just give me a shout\x01",
            "when you're ready to order.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9329")

    label("loc_925E")


    ChrTalk(
        0xA,
        (
            "Whenever Keith or Alfred are feeling\x01",
            "hungry, they always ask for their usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'd be lying if I said I wasn't happy that\x01",
            "we're close enough to know what the\x01",
            "other wants with a few short words.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9329")

    Jump("loc_A5BA")

    label("loc_932E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_953D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9462")

    ChrTalk(
        0xA,
        (
            "'Is there a place where villagers can\x01",
            "relax and get a bite to eat?' With that\x01",
            "question in mind, I opened this inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My motto is that profit comes second\x01",
            "to my customers' happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't tell anyone else, though.\x01",
            "Sealy gets ticked off whenever she\x01",
            "hears me say that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9538")

    label("loc_9462")


    ChrTalk(
        0xA,
        (
            "I think it's perfectly okay to only make\x01",
            "enough money to live on, but Sealy\x01",
            "says that way of thinking is absurd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, once she gets accustomed to the\x01",
            "inn, I'm sure she'll start to understand\x01",
            "how I feel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9538")

    Jump("loc_A5BA")

    label("loc_953D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_960D")

    ChrTalk(
        0xA,
        (
            "Aretha and her son have really come to\x01",
            "like Armorica Village, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They've been staying on the second floor\x01",
            "for a while now, but I'd love it if they decided\x01",
            "to actually move here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5BA")

    label("loc_960D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B2")

    ChrTalk(
        0xA,
        (
            "I feel like the festival crowd is finally\x01",
            "starting to die down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Being able to cook so much for people\x01",
            "was nice while it lasted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9760")

    label("loc_96B2")


    ChrTalk(
        0xA,
        (
            "Once they finish packing up the food stall,\x01",
            "Sealy should be back to work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Starting tomorrow, I'm going to\x01",
            "have to focus on serving my\x01",
            "regular customers again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9760")

    Jump("loc_A5BA")

    label("loc_9765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_99BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9822")

    ChrTalk(
        0xA,
        (
            "Everyone, thank you so much\x01",
            "for finding my customers and\x01",
            "bringing them back safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If something like that ever happens\x01",
            "again, we'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99B8")

    label("loc_9822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_98DE")

    ChrTalk(
        0xA,
        (
            "To get to the Ancient Battlefield, you\x01",
            "have to cross the metal bridge that's\x01",
            "on Old Armorica Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm begging you...please find those\x01",
            "two and bring them back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99B8")

    label("loc_98DE")


    ChrTalk(
        0xA,
        (
            "From what I've heard, some tourists\x01",
            "have tried to enter the apiary, claiming\x01",
            "it's a cool sightseeing spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The fields and apiary aren't the safest\x01",
            "places. I wish they'd think twice before\x01",
            "trying to sneak in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99B8")

    Jump("loc_A5BA")

    label("loc_99BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A75")

    ChrTalk(
        0xA,
        (
            "Quite a few tourists have been staying\x01",
            "here since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's pretty refreshing. Most of my\x01",
            "customers end up being traders,\x01",
            "like Mr. Hayworth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9B3E")

    label("loc_9A75")


    ChrTalk(
        0xA,
        (
            "They've been telling me that after\x01",
            "eating at our food stall, they just\x01",
            "had to visit the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Something about that is genuinely\x01",
            "touching. It makes me so happy to\x01",
            "hear they liked our food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B3E")

    Jump("loc_A5BA")

    label("loc_9B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CC0")

    ChrTalk(
        0xA,
        (
            "We decided to pitch in and offer our food at\x01",
            "the village's Anniversary Festival stall. My\x01",
            "daughter even volunteered to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you ever start to miss my cooking,\x01",
            "you can go get some in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's probably going to be a lot of customers\x01",
            "asking for a room, so I'll have to focus on my\x01",
            "work soon. Especially with Sealy out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9D63")

    label("loc_9CC0")


    ChrTalk(
        0xA,
        (
            "Sealy volunteered to go help out\x01",
            "with the village's food stall in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you ever start to miss my cooking,\x01",
            "you can go get some in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D63")

    Jump("loc_A5BA")

    label("loc_9D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9E3F")

    ChrTalk(
        0xA,
        (
            "There seems to be an argument regarding\x01",
            "what we should serve at our festival stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, I'd like it if they considered\x01",
            "some of my dishes at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Who am I to turn down free advertising?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5BA")

    label("loc_9E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9F4F")

    ChrTalk(
        0xA,
        (
            "Been almost a month since those\x01",
            "monster attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Crossbell Times didn't go into\x01",
            "much detail, but you folks were the\x01",
            "ones who solved the case, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thanks to you, I'm able to sleep\x01",
            "like a baby again. I appreciate\x01",
            "the hard work, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5BA")

    label("loc_9F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A087")

    ChrTalk(
        0xA,
        (
            "The village chief reminded us to keep\x01",
            "an eye out for wolves yesterday afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hadn't realized other places in the state\x01",
            "had also been hit by monster attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Monsters typically keep to their own\x01",
            "territory, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Something about these attacks is strange.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A10E")

    label("loc_A087")


    ChrTalk(
        0xA,
        (
            "Those wolves have been attacking places\x01",
            "far and wide, rather than in their own territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Are we dealing with a new species?\x02",
    )

    CloseMessageWindow()

    label("loc_A10E")

    Jump("loc_A5BA")

    label("loc_A113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_A276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A222")

    ChrTalk(
        0xA,
        (
            "There's been a lot more fuss about that\x01",
            "monster attack lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been a while since they showed up here.\x01",
            "Honestly, I had started to forget about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess we shouldn't let our guard down\x01",
            "yet, since they haven't been caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A271")

    label("loc_A222")


    ChrTalk(
        0xA,
        (
            "We probably shouldn't let our guard\x01",
            "down until those wolves are caught...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A271")

    Jump("loc_A5BA")

    label("loc_A276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_A40E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A290")
    Call(0, 12)
    TalkEnd(0xA)
    Return()

    label("loc_A290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A362")

    ChrTalk(
        0xA,
        (
            "Most people who tend to the fields\x01",
            "come back during lunchtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't say that business is booming...\x01",
            "but we manage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just happy to keep this place\x01",
            "running for my regulars.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A409")

    label("loc_A362")


    ChrTalk(
        0xA,
        (
            "Mr. Hayworth usually spends the night\x01",
            "here when he's in town, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I consider him a regular, so I toss him\x01",
            "something free of charge every now\x01",
            "and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A409")

    Jump("loc_A5BA")

    label("loc_A40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A5BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A517")

    ChrTalk(
        0xA,
        "Welcome to the Ash Tree Inn. Feeling thirsty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From what I can see, you all look dead tired.\x01",
            "Don't go overworking yourselves, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You know what? How about something to\x01",
            "eat? I could whip up something simple in\x01",
            "no time flat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A5BA")

    label("loc_A517")


    ChrTalk(
        0xA,
        "Speaking of food, it's almost noon, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I better start getting ready for rush hour.\x01",
            "Most of the farmers like to get lunch here\x01",
            "during their break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5BA")

    Jump("loc_8F30")

    label("loc_A5BF")

    TalkEnd(0xA)
    Return()

    # Function_26_8F0A end

    def Function_27_A5C3(): pass

    label("Function_27_A5C3")

    Call(0, 28)
    Return()

    # Function_27_A5C3 end

    def Function_28_A5C7(): pass

    label("Function_28_A5C7")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A625")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A625")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A644")
    OP_AF(0x4C)
    Jump("loc_A646")

    label("loc_A644")

    OP_AF(0x4B)

    label("loc_A646")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9F3")

    label("loc_A655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A669")
    Jump("loc_B9F3")

    label("loc_A669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7B0")

    ChrTalk(
        0x9,
        (
            "Gramps always gets mad at me\x01",
            "for not taking my job seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But honestly, I couldn't care less whether\x01",
            "or not this store's been passed down for\x01",
            "generations. I didn't sign up for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Why couldn't my ancestors have invested\x01",
            "in a more profitable industry...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A85C")

    label("loc_A7B0")


    ChrTalk(
        0x9,
        (
            "Why couldn't my ancestors have invested\x01",
            "in a more profitable industry...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heck, I'd be more than happy to inherit the\x01",
            "family business if I was Dieter Crois' son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A85C")

    Jump("loc_B9F3")

    label("loc_A861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A9D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94F")

    ChrTalk(
        0x9,
        (
            "*sigh* Gramps gave me another one of\x01",
            "his angry lectures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At this point, maybe I really should ditch this\x01",
            "place and head to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But then Gramps would\x01",
            "pretty much be stuck here alone...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A9CB")

    label("loc_A94F")


    ChrTalk(
        0x9,
        (
            "Maybe I really should ditch this place\x01",
            "and head to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can't leave Gramps all by himself,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9CB")

    Jump("loc_B9F3")

    label("loc_A9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_ABD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAFC")

    ChrTalk(
        0x9,
        (
            "It looks like Gramps is in a pretty\x01",
            "cheery mood today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Him and Mr. Hayworth get along really well,\x01",
            "so that probably did the trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Compared to him, I'm just some guy that was\x01",
            "unemployed for a long time. I didn't even do\x01",
            "anything noteworthy for the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ABCE")

    label("loc_AAFC")


    ChrTalk(
        0x9,
        (
            "On the bright side, we had so much business\x01",
            "during the festival that I got a lot faster at\x01",
            "calculating sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't really feel like I've moved up from just\x01",
            "being a household helper at all, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABCE")

    Jump("loc_B9F3")

    label("loc_ABD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AD25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACB2")

    ChrTalk(
        0x9,
        (
            "*yawn*... Up until yesterday, business\x01",
            "was booming for us. I couldn't believe\x01",
            "my eyes at first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now that it's over and done with,\x01",
            "our calm, peaceful days are finally\x01",
            "going to come back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AD20")

    label("loc_ACB2")


    ChrTalk(
        0x9,
        (
            "Don't look, but I think Gramps is\x01",
            "staring daggers at me right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Did I make him mad or something?\x02",
    )

    CloseMessageWindow()

    label("loc_AD20")

    Jump("loc_B9F3")

    label("loc_AD25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AE7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADDE")

    ChrTalk(
        0x9,
        (
            "I wonder why that customer went over\x01",
            "and talked to Gramps instead of me.\x01",
            "I'm the one at the counter, aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do I not look reliable or something?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AE78")

    label("loc_ADDE")


    ChrTalk(
        0x9,
        "Maybe I really DO look unreliable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, let's look at it like this. If Gramps\x01",
            "is the one doing the negotiations, I'll\x01",
            "be able to take it easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE78")

    Jump("loc_B9F3")

    label("loc_AE7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AF2C")

    ChrTalk(
        0x9,
        (
            "Ever since yesterday, we've started to\x01",
            "get way more customers than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Gramps is pumped, but to be honest,\x01",
            "all these people make me a little dizzy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9F3")

    label("loc_AF2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFE1")

    ChrTalk(
        0x9,
        (
            "Armorica Village's honey seems to be\x01",
            "a real hit with tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we made this much mira all the\x01",
            "time, I could just kick back and live happily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B04D")

    label("loc_AFE1")


    ChrTalk(
        0x9,
        (
            "Even though I really like slacking off when\x01",
            "there's no customers, I genuinely want to\x01",
            "sell more honey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B04D")

    Jump("loc_B9F3")

    label("loc_B052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B14A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B10C")

    ChrTalk(
        0x9,
        (
            "Derek has been talking to Gramps for a\x01",
            "while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Beats me what they're talking about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess I'm not cut out to be a merchant,\x01",
            "after all...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B145")

    label("loc_B10C")


    ChrTalk(
        0x9,
        (
            "What exactly are Derek and Gramps\x01",
            "talking about...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B145")

    Jump("loc_B9F3")

    label("loc_B14A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B2F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23C")

    ChrTalk(
        0x9,
        (
            "I've started to get in the habit of reading\x01",
            "the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You guys were featured in it, weren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Man, all I want is to go to Crossbell City\x01",
            "and live an amazing life, full of mira\x01",
            "and fame.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B2EC")

    label("loc_B23C")


    ChrTalk(
        0x9,
        (
            "Just you wait. One day, I'll become a\x01",
            "great man and be featured in the\x01",
            "Crossbell Times, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though, I've still got to keep helping\x01",
            "around the general store for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2EC")

    Jump("loc_B9F3")

    label("loc_B2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B4DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B42D")

    ChrTalk(
        0x9,
        (
            "*sigh* Every time Gramps opens his\x01",
            "mouth now, it's 'Harold this' and 'Harold\x01",
            "that,' over and over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "'You should take a few pages out of his\x01",
            "book, Jake,' he keeps telling me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I literally just started working here.\x01",
            "Would it kill him to not put so much\x01",
            "pressure on me?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B4DA")

    label("loc_B42D")


    ChrTalk(
        0x9,
        (
            "Gramps seems to really like Mr. Hayworth.\x01",
            "So much that he can't help but constantly\x01",
            "compare me to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh* Can't he see that I don't work\x01",
            "well under pressure?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4DA")

    Jump("loc_B9F3")

    label("loc_B4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_B6C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B611")

    ChrTalk(
        0x9,
        (
            "Since I was recently outta work, Gramps\x01",
            "decided to get on my case about me\x01",
            "inheriting the general store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Me, inheriting a run-down store like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You think a real man would pick this\x01",
            "shop over going to Crossbell City with\x01",
            "the chance of becoming rich and famous?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B6C0")

    label("loc_B611")


    ChrTalk(
        0x9,
        (
            "I swear, someday I'll move out\x01",
            "to the city and make it big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guess helping around the store for now\x01",
            "isn't the worst thing in the world. It's easy,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6C0")

    Jump("loc_B9F3")

    label("loc_B6C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_B88E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7F9")

    ChrTalk(
        0x9,
        (
            "Huh? The attack three weeks ago?\x01",
            "You mean that one everyone's been\x01",
            "making a big deal about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was fast asleep when it happened,\x01",
            "so I don't remember much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Plus, I heard we've already made up\x01",
            "the losses we took. Why can't we just\x01",
            "forget about it and move on?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B889")

    label("loc_B7F9")


    ChrTalk(
        0x9,
        (
            "Chief Tolta already said that we've\x01",
            "recovered from all the damages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wouldn't it be better to forget about\x01",
            "those monsters and move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B889")

    Jump("loc_B9F3")

    label("loc_B88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B9F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B939")

    ChrTalk(
        0x9,
        (
            "M-Morning. Welcome to Reoir\x01",
            "General Sto--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ouch! I bit my tongue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh... Welcome to Reoir General Store.\x01",
            "Feel free to look around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B9F3")

    label("loc_B939")


    ChrTalk(
        0x9,
        (
            "Gramps can be downright evil sometimes.\x01",
            "Me, working the counter? Unbelievable.\x01",
            "You get where I'm coming from, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oops, I'm probably a little out of line.\x01",
            "Sorry about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F3")

    Jump("loc_A5D4")

    label("loc_B9F8")

    TalkEnd(0x9)
    Return()

    # Function_28_A5C7 end

    def Function_29_B9FC(): pass

    label("Function_29_B9FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA12")
    Call(0, 41)
    Jump("loc_C023")

    label("loc_BA12")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BA23")
    Jump("loc_C020")

    label("loc_BA23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BA31")
    Jump("loc_C020")

    label("loc_BA31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BD12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BAF9")

    ChrTalk(
        0x1B,
        (
            "#3600FMy wife has been doing her best to support\x01",
            "me in my business endeavors, recently.\x02\x03",
            "I owe it to her and my son to work just as\x01",
            "hard to become a loving, united family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD0D")

    label("loc_BAF9")


    ChrTalk(
        0x1B,
        (
            "#3605FOh, have you all come to purchase\x01",
            "some of Armorica's fine honey as well?\x02\x03",
            "#3600FHahaha, sorry to disappoint, but there's\x01",
            "no way I'll let you outbid me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FAs if we'd ever try to out-negotiate you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou said you were taking a vacation after\x01",
            "the Anniversary Festival, didn't you? Has\x01",
            "that already come to a close?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3600FHaha, yes. I was extremely stressed, so\x01",
            "it was a welcome change of pace.\x02\x03",
            "Don't worry, my batteries are recharged.\x01",
            "From now on, I intend to be even more\x01",
            "successful than before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_BD0D")

    Jump("loc_C020")

    label("loc_BD12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BD20")
    Jump("loc_C020")

    label("loc_BD20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BD2E")
    Jump("loc_C020")

    label("loc_BD2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BD3C")
    Jump("loc_C020")

    label("loc_BD3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BD4A")
    Jump("loc_C020")

    label("loc_BD4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BD58")
    Jump("loc_C020")

    label("loc_BD58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BD66")
    Jump("loc_C020")

    label("loc_BD66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BD74")
    Jump("loc_C020")

    label("loc_BD74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_BDF1")

    ChrTalk(
        0x1B,
        (
            "#3604FNow, then, I suppose it's almost time\x01",
            "for me to head home.\x02\x03",
            "#3608FHmmm, where did I put my car key?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C020")

    label("loc_BDF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_C017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF50")

    ChrTalk(
        0x1B,
        (
            "#3610FI wasn't near the area where the damages occurred.\x01",
            "I'm really sorry I can't be any help, everyone.\x02\x03",
            "#3608FIf these attacks continue throughout Crossbell,\x01",
            "I imagine most of the public will be on edge.\x02\x03",
            "#3600FSpecial Support Section, please continue to do\x01",
            "your best in your investigation. You have my\x01",
            "full support.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C012")

    label("loc_BF50")


    ChrTalk(
        0x1B,
        (
            "#3604FI'm sure that your investigation will clear the\x01",
            "fog surrounding these attacks. I have faith\x01",
            "in you four.\x02\x03",
            "#3600FContinue to work hard in your investigation.\x01",
            "You have my full support.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C012")

    Jump("loc_C020")

    label("loc_C017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_C020")

    label("loc_C020")

    TalkEnd(0x1B)

    label("loc_C023")

    Return()

    # Function_29_B9FC end

    def Function_30_C024(): pass

    label("Function_30_C024")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C0B8")
    Jump("loc_C102")

    label("loc_C0B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C0D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C102")

    label("loc_C0D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C102")

    label("loc_C0F8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C102")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C1FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C142")
    Call(0, 37)
    Jump("loc_C1FB")

    label("loc_C142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C154")
    Call(0, 38)
    Jump("loc_C1FB")

    label("loc_C154")


    ChrTalk(
        0x1C,
        (
            "#0803FLet's see... I say after we take a short break,\x01",
            "we check out the other highway.\x02\x03",
            "#0800FWe should double-check whether or not\x01",
            "there are any more roadblocks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1FB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_C024 end

    def Function_31_C203(): pass

    label("Function_31_C203")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C2C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C221")
    Call(0, 37)
    Jump("loc_C2C9")

    label("loc_C221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C233")
    Call(0, 38)
    Jump("loc_C2C9")

    label("loc_C233")


    ChrTalk(
        0x1D,
        (
            "#0903FThere's been confirmation that these\x01",
            "new, unknown monsters are vastly different\x01",
            "than the wanted ones from before.\x02\x03",
            "#0901FTry to stay safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2C9")

    TalkEnd(0xFE)
    Return()

    # Function_31_C203 end

    def Function_32_C2CD(): pass

    label("Function_32_C2CD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C361")
    Jump("loc_C3AB")

    label("loc_C361")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C381")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C3AB")

    label("loc_C381")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C3A1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C3AB")

    label("loc_C3A1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3AB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4E7")
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x1E,
        (
            "Hard to believe that tourists are going to\x01",
            "come stop by a remote place like Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Aeolia, let's try to stop any troublemakers\x01",
            "from entering places they shouldn't, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I hear you loud and clear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Let me finish eating first.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C593")

    label("loc_C4E7")


    ChrTalk(
        0xFE,
        (
            "The highway's full of areas most\x01",
            "people wouldn't be able to identify\x01",
            "as dangerous or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's our job to make sure no one\x01",
            "accidentally wanders into such places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C593")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_C2CD end

    def Function_33_C59B(): pass

    label("Function_33_C59B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C62F")
    Jump("loc_C679")

    label("loc_C62F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C64F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C679")

    label("loc_C64F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C66F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C679")

    label("loc_C66F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C679")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C7FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C744")

    ChrTalk(
        0xFE,
        (
            "I think I'll take on some of those\x01",
            "monster exterminations today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you leave them be, they can multiply\x01",
            "in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C7FE")

    label("loc_C744")


    ChrTalk(
        0xFE,
        (
            "The highway becomes a much more formidable\x01",
            "enemy during the festival season.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't stay in the village all day, but I\x01",
            "want to finish as many jobs as possible\x01",
            "while I'm here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7FE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_C59B end

    def Function_34_C806(): pass

    label("Function_34_C806")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98A")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★Ash Tree Inn - Recommended Special★\x01",
            "              ~ Rustic Omelet Rice ~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0000FOmelet rice? Can't say I've tried it\x01",
            "before. What about you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI think I may have. The recipe is written right\x01",
            "there, so we might as well jot it down.\x02",
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
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x9)
    Jump("loc_C9F3")

    label("loc_C98A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★Ash Tree Inn - Recommended Special★\x01",
            "              ~ Rustic Omelet Rice ~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_C9F3")

    TalkEnd(0xFF)
    Return()

    # Function_34_C806 end

    def Function_35_C9F7(): pass

    label("Function_35_C9F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CADB")

    ChrTalk(
        0xFE,
        (
            "The village's atmosphere is incredible.\x01",
            "I can almost feel myself working in the\x01",
            "fields, taking in the sun's glow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I'm old, I want to spend the rest of\x01",
            "my days in a relaxing place like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_CB83")

    label("loc_CADB")


    ChrTalk(
        0xFE,
        (
            "Going all out in the casino back\x01",
            "at Crossbell City sounds nice, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I wouldn't mind spending my later\x01",
            "years in a quiet, relaxing village like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB83")

    TalkEnd(0xFE)
    Return()

    # Function_35_C9F7 end

    def Function_36_CB87(): pass

    label("Function_36_CB87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBDD")

    ChrTalk(
        0xFE,
        "Veggies? THIS cheap...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time to stockpile while I can!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_CC6C")

    label("loc_CBDD")


    ChrTalk(
        0xFE,
        "Potatoes, onions... Even their famous honey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohoho! Everything's so cheap! In this economy?!\x01",
            "Pinch me because I must be dreaming!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC6C")

    TalkEnd(0xFE)
    Return()

    # Function_36_CB87 end

    def Function_37_CC70(): pass

    label("Function_37_CC70")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1D, 0xFF)
    OP_68(80860, 1500, -980, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 80000, 0, 0, 90)
    SetChrPos(0x102, 79750, 0, -1000, 90)
    SetChrPos(0x103, 78500, 0, 750, 90)
    SetChrPos(0x104, 78250, 0, -250, 90)
    SetChrPos(0x109, 78750, 0, -1250, 90)
    SetChrPos(0x1C, 81630, 170, -1650, 270)
    SetChrSubChip(0x1C, 0x2)
    OP_93(0x1D, 0x10E, 0x0)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()

    ChrTalk(
        0x1C,
        "#0805F#6POh! Hey, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0900F#12PLet me guess, you guys\x01",
            "are busy working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F#5PRight. We're in the middle of finishing\x01",
            "up a few small jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F#5PYou guys stayin' at the inn? Quality place.\x01",
            "I fully recommend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#0806F#6PYep, that's right. Though, we weren't planning on\x01",
            "staying. The truth is, we ran into a snag while\x01",
            "working on a monster extermination yesterday, and\x01",
            "we missed the bus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0903F#12PNot left with many options, we decided\x01",
            "to just stay at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F#5PSomething gave you two trouble?\x01",
            "I'm almost hesitant to believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F#5PWas it that strong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#0806F#6PWellll, it was like those wanted monsters\x01",
            "from before, but with a bit of a twist.\x02\x03",
            "#0801FFor some reason, a BUNCH of them showed\x01",
            "up on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0906F#12PAnd what's odder than that, they all seemed\x01",
            "much stronger than they were last time...\x02\x03",
            "#0901FIt's not just this area, either. The other highways\x01",
            "are experiencing the same weird situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F#5PThat's unusual, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503F#5PThe CGF has received reports about\x01",
            "these appearances, too.\x02\x03",
            "#0500FLuckily, they don't seem to pose any\x01",
            "threat to the bus service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F#5PHuh, would ya look at that? It ain't all bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F#5PStill, something like this isn't normal...\x01",
            "We should keep our eyes open.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80000, 0, -500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1C, 82040, 180, -1400, 45)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0x87, 0x0)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0xCF, 5)
    EventEnd(0x5)
    Return()

    # Function_37_CC70 end

    def Function_38_D28D(): pass

    label("Function_38_D28D")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1D, 0xFF)
    OP_68(80860, 1500, -980, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 80000, 0, 0, 90)
    SetChrPos(0x102, 79750, 0, -1000, 90)
    SetChrPos(0x103, 78500, 0, 750, 90)
    SetChrPos(0x104, 78250, 0, -250, 90)
    SetChrPos(0x109, 78750, 0, -1250, 90)
    SetChrPos(0x1C, 81630, 170, -1650, 270)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0xE1, 0x0)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()

    ChrTalk(
        0x1C,
        (
            "#0802F#6PPutting that mystery aside, who's this\x01",
            "girl with you guys? New member?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0900F#12PI don't think so, Estelle. You're from the\x01",
            "Crossbell Guardian Force, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500F#5PI am. Sergeant Major Noel Seeker,\x01",
            "of the Tangram Gate division.\x02\x03",
            "And you two are bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#0800F#6PYep! I'm Estelle Bright, currently registered\x01",
            "with the Bracer Guild's Crossbell branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0904F#12PNice to meet you, Sergeant Major Seeker.\x01",
            "My name's Joshua Bright.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#0505F#5PW-Wait a minute, aren't you...?!\x02\x03",
            "#0502FI saw you two in the Crossbell Times! You're\x01",
            "those young heroes who single-handedly put\x01",
            "an end to that massive incident in Liberl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#0809F#6PAhaha...haha... You must have\x01",
            "read Grace's article, too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#0904F#12PActually, we weren't the only ones who helped\x01",
            "stop that, you know... It was a team effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F#5P(Wow, Estelle and Joshua really are famous\x01",
            "if Grace thought they were newsworthy.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80000, 0, -500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1C, 82040, 180, -1400, 45)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0x87, 0x0)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0xCF, 6)
    EventEnd(0x5)
    Return()

    # Function_38_D28D end

    def Function_39_D741(): pass

    label("Function_39_D741")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    OP_68(40, 1200, 2180, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22400, 0)
    SetChrPos(0x101, 0, 0, 2000, 360)
    SetChrPos(0x102, -1000, 0, 1500, 360)
    SetChrPos(0x103, 1000, 0, 500, 360)
    SetChrPos(0x104, 0, 0, -250, 360)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -6860, 0)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -6860, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5POh, Goddess... If something ends up happening\x01",
            "to my customers, my inn is done for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PPlease be safe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FUh, excuse us. You're Mr. Gofan, right?\x02\x03",
            "We're the Special Support Section.\x01",
            "You submitted a support request\x01",
            "to the CPD, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(750)
    TurnDirection(0xA, 0x101, 750)

    ChrTalk(
        0xA,
        "#11POh, I'm saved!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI've got a monumental problem\x01",
            "on my hands, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PGah! If I knew this was going to happen,\x01",
            "I would've tied them down while they\x01",
            "were still in the village!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11POooh, this is all my fault!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FSir, please try to calm down and\x01",
            "explain the situation.\x02\x03",
            "#0001FWhat in the world happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PS-Sorry about that. I'm just a little\x01",
            "overwhelmed by this fiasco. Allow\x01",
            "me to start from the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PYesterday, a foreign couple checked\x01",
            "into my inn. Everything was fine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P...when I came to bring them breakfast\x01",
            "in the morning, the room was empty. It\x01",
            "was like they were never there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI have reason to believe that they\x01",
            "ventured to the Ancient Battlefield,\x01",
            "off of Old Armorica Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F#6PThat name rings a bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FI think I've mentioned it before. Historians\x01",
            "have found traces of an old battlefield off a\x01",
            "branch of Old Armorica Road.\x02\x03",
            "#0105FIf I remember correctly, wasn't the stone\x01",
            "bridge connecting the paths down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWell, it was. It seems that it was repaired recently,\x01",
            "though. Now any random person can wander there\x01",
            "all willy-nilly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThat couple kept on talking about how\x01",
            "they wanted to go sightseeing while they\x01",
            "were in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PUpon hearing that, I warned them about entering\x01",
            "the battlefield, but that might have backfired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FHmm, the battlefield would probably make\x01",
            "a pretty sweet tourism spot...\x02\x03",
            "#0301FIs it really THAT dangerous, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAbsolutely. That place is famous for housing\x01",
            "a multitude of incredibly powerful monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHeck, even the villagers here know it'd be\x01",
            "crazy to try and go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAnd on top of that, ever since the bridge was\x01",
            "repaired, no one's been patrolling the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThat means we can't confirm whether\x01",
            "things have gotten better or worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FAnd those tourists have unsuspectingly\x01",
            "wandered in a dangerous place.\x02\x03",
            "#0201FThis is not the optimal situation, certainly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101FAgreed. We can't take this lightly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PPlease, I'm begging you. Can you\x01",
            "find them and bring them back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PFor now, my friend Alfred is standing guard,\x01",
            "making sure no one else enters the Ancient\x01",
            "Battlefield, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAt this rate, my customers will be in\x01",
            "deep trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0004FUnderstood, sir. You can leave\x01",
            "everything to us.\x02\x03",
            "#0000FI assure you, we'll find your tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FHaha... It's not like we can refuse.\x02\x03",
            "#0300FY'know, it'd be a lot easier if tourists would\x01",
            "listen when given advice. Especially from locals.\x01",
            "Nothin' to do but track 'em down and bring 'em back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PTh-Thank you so much! You have no idea\x01",
            "how much this means to me and the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PIf I lost them, I don't kno--\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Young Man's Voice",
        "Goooofan!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E495():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E495)
    Sleep(30)

    def lambda_E4A5():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4A5)

    def lambda_E4B2():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E4B2)
    Sleep(30)

    def lambda_E4C2():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E4C2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(0, 1200, 750, 0)
    MoveCamera(303, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25990, 0)
    OP_68(0, 1200, 750, 3000)
    SetCameraDistance(22990, 3000)
    Sound(103, 0, 100, 0)

    def lambda_E532():
        OP_97(0xC, 0x0, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E532)

    def lambda_E54C():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E54C)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    ChrTalk(
        0x101,
        "#11P#0005F(One of his regulars, maybe?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P...Keith, what's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAs you can see, I was in the middle\x01",
            "of an important discussion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6PThis is no time for discussion!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYou know how that couple went\x01",
            "missing, and now the inn is in the\x01",
            "crapper because of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PYes, I'm fully aware. I just told these\x01",
            "officers about the entire situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6PWell, there's no need to freak out anymore!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PFor the sake of the inn...\x01",
            "I called in the cavalry!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#0105FThe cavalry? What are you talking about...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x20, 500)

    ChrTalk(
        0xC,
        (
            "#12PC'mon in here! Don't be shy!\x01",
            "My boss will explain this entire\x01",
            "mess to you!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Man's Voice",
        "Sure, lay it on me.\x02",
    )

    CloseMessageWindow()
    OP_68(-110, 1200, 580, 2000)
    SetCameraDistance(24140, 2000)

    def lambda_E8A4():
        OP_97(0x20, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_E8A4)

    def lambda_E8BE():
        OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_E8BE)
    OP_98(0xC, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_E8E3():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E8E3)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x20, 2)

    ChrTalk(
        0x20,
        "#6PI'm Scott of the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PSo you've got a missing couple,\x01",
            "is that right? If you don't mind,\x01",
            "could you fill me in on the details?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0011FH-Hold on... A bracer?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0105FWh-Why are you here...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x20, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x20,
        (
            "#6P...Huh? You're that Special Support\x01",
            "Section, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PGiven the circumstances, it'd be wrong\x01",
            "to call us meeting a coincidence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PK-Keith. Explain to me why you brought\x01",
            "a bracer here, immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x2D, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#5PWhat do you mean? Whenever you're\x01",
            "in a pickle, you gotta turn to the Bracer\x01",
            "Guild! Duh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWhen I heard about what happened,\x01",
            "I sprinted all the way to Crossbell City\x01",
            "to submit a request to the guild!\x02",
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
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11P*sigh* I can't fault you for caring, but I\x01",
            "really wish you cleared it with me first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0211FJust our luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306FDude, you have the worst timing. Ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHuh? Why is everyone being\x01",
            "so hostile right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PI don't really understand what's happening,\x01",
            "but it's obvious that something's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PSorry, but could I get a brief explanation\x01",
            "of what's going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0011FS-Sure. Here's the rundown...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that the SSS had come to accept the\x01",
            "same request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x20,
        "#6PSo that's how it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#6PThis whole thing is a giant misunderstanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThat may be...but what should we do about the\x01",
            "missing couple?\x02\x03",
            "#0200FI am not sure what the proper protocol is for\x01",
            "when the police and guild accept the same job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0302FHey, we could always turn this into\x01",
            "a fun competition.\x02\x03",
            "#0309FWho will be the first to find the tourists?!\x01",
            "...Somethin' like that? Maybe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FRandy... That's not the issue here.\x02\x03",
            "#0108FLloyd, what do you think we should do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0003FHmm, I have an idea...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#0001FScott, if you aren't opposed to it...\x02\x03",
            "...why don't we work together?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F1A9():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F1A9)

    def lambda_F1B6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F1B6)

    def lambda_F1C3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F1C3)
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x20,
        (
            "#6PHaha, no complaints here. I was actually\x01",
            "thinking the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FJoining forces...with the Bracer Guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FMight as well. So we're searchin' for this\x01",
            "Ancient Battlefield together, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FNo. We can split into groups.\x02\x03",
            "#0003FFrom what we've heard, this place is\x01",
            "practically a den of monsters.\x02\x03",
            "And we need to secure the safety of\x01",
            "those two tourists ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PI might be familiar with the general area,\x01",
            "but the battlefield is no small place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PIf we split up, the probability of finding\x01",
            "them will skyrocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PIf we keep in contact with our Enigmas, we\x01",
            "should be able to find them relatively soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FTrue...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0204FIndeed. That seems like the most\x01",
            "reasonable strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI'm all for that plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PLives are at stake here.\x01",
            "The more help, the merrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PSSS. Scott. I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PAnd with the client's permission,\x01",
            "we're good to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FYeah. Let's do our best.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Scott exchanged Enigma contact info.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x20,
        "#6PAll right. Let's strike while the iron's hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PI'll head on to the Ancient Battlefield. Whenever\x01",
            "you all are ready, come catch up with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#6PI'll see you later.\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x1F4)

    def lambda_F6C5():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6C5)

    def lambda_F6D2():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F6D2)

    def lambda_F6DF():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F6DF)

    def lambda_F6EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F6EC)
    OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)

    ChrTalk(
        0x101,
        (
            "#11P#0003FOkay, everyone. Once we're\x01",
            "prepared, let's make our way\x01",
            "to the Ancient Battlefield, too.\x02\x03",
            "#0001FAfter all, we don't want to fall\x01",
            "too far behind Scott.\x02",
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
            "[Missing Tourists]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(0, 1500, 0, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetChrPos(0xA, 750, 0, 1500, 270)
    SetChrPos(0xC, -750, 0, 1500, 90)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x40)
    OP_29(0x1F, 0x1, 0x0)
    SetScenarioFlags(0xD9, 4)
    FadeToBright(500, 0)
    OP_0D()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_39_D741 end

    def Function_40_F8DD(): pass

    label("Function_40_F8DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    LoadChrToIndex("chr/ch02400.itc", 0x1F)
    OP_4B(0xA, 0xFF)
    OP_68(40, 1200, 2180, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24460, 0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrPos(0x101, 0, 0, 2000, 360)
    SetChrPos(0x102, -1000, 0, 1500, 360)
    SetChrPos(0x103, 1000, 0, 500, 360)
    SetChrPos(0x104, 0, 0, -250, 360)
    SetChrPos(0xA, 0, 0, 3700, 180)
    SetChrPos(0x20, -7270, 2220, -4080, 90)
    SetChrPos(0x21, -8270, 2530, -4140, 90)
    SetCameraDistance(23460, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#11PEveryone, thank you for bringing\x01",
            "them back safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI was almost done for!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FDon't mention it, Mr. Gofan. I'm not sure\x01",
            "what would have happened if not for\x01",
            "Scott and Arios being there, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FHopefully, those tourists take a loooong,\x01",
            "nice nap before doing anything else.\x02\x03",
            "#0301FOn a side note, those bracers are some\x01",
            "serious guys. They sure like to stay on\x01",
            "top of things, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0104FI can't deny that bracers all seem\x01",
            "to have impeccable timing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#0100FAt least we were able to finish the support\x01",
            "request without too many issues.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#6P#0203FYes, but one problem remains.\x02\x03",
            "#0200FDuring the support request, the guild and\x01",
            "the police worked side-by-side...\x02\x03",
            "Now that it is over, how should we go\x01",
            "about reporting this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xAA, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#0305FHmm, good point.\x02\x03",
            "#0300FWhat's your call, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FThis definitely wasn't a standard case for\x01",
            "us, that's for sure.\x02\x03",
            "I said it before, but if Scott and Arios hadn't\x01",
            "been there, I'm not sure if we would have\x01",
            "been as successful as we were.\x02\x03",
            "#0000FI think, this time, we should give them\x01",
            "the credit for resolving the request...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Scott's Voice",
        (
            "#1PThat's not how it's going to go down\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_FF37():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF37)

    def lambda_FF44():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF44)

    def lambda_FF51():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FF51)

    def lambda_FF5E():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FF5E)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Fade(500)
    OP_68(-7560, 2000, -4170, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22120, 0)
    OP_68(210, 1500, -390, 5000)
    MoveCamera(305, 22, 0, 5000)
    SetCameraDistance(24390, 5000)

    def lambda_FFEA():
        OP_95(0x20, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_FFEA)

    def lambda_10004():
        OP_95(0x21, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10004)
    WaitChrThread(0x20, 1)

    def lambda_10022():
        OP_95(0x20, 500, 0, -1770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_10022)
    WaitChrThread(0x21, 1)

    def lambda_10040():
        OP_95(0x21, -500, 0, -2580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10040)

    def lambda_1005A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1005A)

    def lambda_10067():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10067)

    def lambda_10074():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10074)

    def lambda_10081():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10081)
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x0, 0x0)
    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x0, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#11P#0105FArios, Scott...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#6P#1403FGofan, it seems as if those two\x01",
            "wish to apologize.\x02\x03",
            "#1400FThey have reflected on their ways\x01",
            "and regret ignoring your warning\x01",
            "about the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh? Is that so? It's not as if I'm going\x01",
            "to lose sleep over this ordeal, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0304FHaha, hopefully, this was a good\x01",
            "lesson for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0205FExcuse me, Scott... What did you mean\x01",
            "by, 'going to go down this time'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PWell, I've talked it over with Arios,\x01",
            "and we came to a decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PWe want the SSS to be the ones\x01",
            "to say they completed the request.\x02",
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
            "#11P#0005FU-Umm, did I hear you right?\x02\x03",
            "#0003FLooking back on this case, you two\x01",
            "clearly did the heavier lifting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#6PThat's not true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PSince you all were able to go on ahead,\x01",
            "that bought me time to look after the lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PAnd if you hadn't made it to the man in time,\x01",
            "I'm not sure if he would have made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PSure, our results may sound nice on paper,\x01",
            "but in the grand scheme of things, we think\x01",
            "the SSS was crucial to the request's success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0309FHaha... Feels sort of embarrassin' to be\x01",
            "praised by your rivals, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#6P#1404FI wouldn't say we're rivals in the slightest.\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "#6P#1403FThe Special Support Section... It appears\x01",
            "as if you've matured a little since we first\x01",
            "crossed paths.\x02\x03",
            "#1400FEspecially you, Lloyd.\x02",
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
        "#11P#0011FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#6P#1400FDo you remember when we first met in the Geofront?\x02\x03",
            "Back then, you decided to recklessly throw away your\x01",
            "life fighting against an unbeatable foe, as if you\x01",
            "were some kind of martyr...\x02\x03",
            "#1404FBut, this time, you refrained from doing that.\x01",
            "Despite your odds being slim, you kept searching\x01",
            "for a way to break through the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#6P#1403FOne requires unwavering strength to\x01",
            "relentlessly go against all odds.\x02\x03",
            "Such strength is far more powerful than\x01",
            "sacrificing your own life.\x02\x03",
            "#1402FThough your ability can't be denied...the fact that\x01",
            "you were able to find another way, against all odds,\x01",
            "is proof in itself that you've become stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0002FThank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#11P#1404FHeh... It seems I've talked too much.\x02\x03",
            "#1402FScott. Return to Crossbell City and\x01",
            "report to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x2EE)

    ChrTalk(
        0x20,
        "#11PRoger, Arios.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#6PWell, Special Support Section, it was\x01",
            "a pleasure! I hope we get the chance\x01",
            "to work together again someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FLikewise.\x02",
    )

    CloseMessageWindow()

    def lambda_10AA3():
        OP_97(0x21, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10AA3)
    OP_93(0x20, 0xB4, 0x2EE)

    def lambda_10AC4():
        OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_10AC4)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x20, 1)
    Sound(104, 0, 100, 0)
    OP_68(-100, 1000, 2110, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(23460, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#12P#0200FI would be lying if I said I expected to hear\x01",
            "encouragement from Arios MacLaine.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#5P#0109FT-Tio, don't be rude... But you're right,\x01",
            "it was a little peculiar.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#6P#0309FHaha, I wouldn't let it bother you.\x02\x03",
            "#0300FWe finished the support request, didn't\x01",
            "we? That's enough to be happy about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PYes, I agree with the redhead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PSpecial Support Section, thank you, once again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI'll be knocking if I need help again.\x02",
    )

    CloseMessageWindow()

    def lambda_10CFC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CFC)
    Sleep(50)

    def lambda_10D0C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D0C)
    Sleep(50)

    def lambda_10D1C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10D1C)
    Sleep(50)

    def lambda_10D2C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10D2C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0000FYou can always rely on us, sir.\x01",
            "We'll be waiting at the door.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 3000, 0)
    SetChrPos(0x1, 0, 0, 3000, 0)
    SetChrPos(0x2, 0, 0, 3000, 0)
    SetChrPos(0x3, 0, 0, 3000, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
    SetChrPos(0x17, 84000, 180, -2040, 283)
    SetChrPos(0x19, 82190, 180, -1670, 103)
    OP_66(0x0, 0x1)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Missing Tourists]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x1F, 0x1, 0x4)
    OP_29(0x1F, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_40_F8DD end

    def Function_41_10EDF(): pass

    label("Function_41_10EDF")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0x1B, 0xFF)
    OP_68(113700, 1200, -1000, 0)
    MoveCamera(324, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25940, 0)
    SetChrPos(0x101, 114420, 0, -1180, 270)
    SetChrPos(0x102, 114420, 0, 0, 270)
    SetChrPos(0x103, 115760, 0, -1180, 270)
    SetChrPos(0x104, 115760, 0, 0, 270)
    SetChrPos(0x1B, 112560, 0, -510, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(24940, 2000)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1B,
        "Kind-Looking Man",
        "#1100573V#3605F#5POh, you again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100574V#0005F#12PThe one from earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100575V#0100FYou're a trader from Crossbell City,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Kind-Looking Man",
        (
            "#1100576V#3609F#5PHaha, I guess you heard about that\x01",
            "from the village chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Kind-Looking Man")

    AnonymousTalk(
        0xFF,
        (
            "#1100577VIt's a pleasure to make your\x01",
            "acquaintance.\x01",
            "I'm Harold Hayworth.\x02\x03",
            "#1100578VI run a small-scale business\x01",
            "operation out of Crossbell City.\x02\x03",
            "#1100579VAre you four here to purchase some-\x01",
            "thing, as well?\x02",
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
        0x101,
        "#1100580V#0000F#12PNo, that's not it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and others introduced themselves and explained\x01",
            "the reason they came to Armorica Village.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x1B,
        (
            "#1100581V#3605F#5POh, you're from the CPD? My apologies.\x02\x03",
            "#1100582V#3603FThe Special Support Section? That name\x01",
            "sounds so familiar... Where in the world\x01",
            "did I hear that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#1100583V#3600F#5POh, of course! The Crossbell Times!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100584V#0012F#12PH-Haha... I take it you read that article\x01",
            "on us...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100585V#0106F#2PAbout that... Please try not to let\x01",
            "that influence your opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100586V#3609F#5PHaha, there's no need to get all worked\x01",
            "up about it.\x02\x03",
            "#1100587V#3600FAll I see is a group of individuals who are\x01",
            "working hard in a newly-formed division\x01",
            "of the CPD.\x02\x03",
            "#1100588VSure, that article may not have been the\x01",
            "most flattering...\x02\x03",
            "#1100589V...but to be honest, I thought it genuinely\x01",
            "tried to paint your efforts as earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100590V#0000F#12PDo you really think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100591V#0206F#12PI suppose it could be interpreted like that,\x01",
            "from a more optimistic perspective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100592V#0309F#2PHaha. Well, we sorta know the author.\x01",
            "That said, I think you might be giving her\x01",
            "too much credit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100593V#3608F#5PAnyway, you mentioned wolf-like monsters?\x02\x03",
            "#1100594VI've heard talk of a similar incident that took\x01",
            "place over at St. Ursula Medical College.\x01",
            "I'd be lying if I told you I wasn't anxious.\x02",
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
            "#1100595V#0005F#12PDo you have some sort of partnership\x01",
            "with St. Ursula as well, Mr. Hayworth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100596V#3604F#5PYes, I do. You see, I wholesale medical\x01",
            "supplies to them every so often.\x02\x03",
            "#1100597V#3601FRumor has it that someone there was\x01",
            "injured during the attack.\x02\x03",
            "#1100598VAlso, wasn't there some damage over\x01",
            "in Mainz, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100599V#0001F#12PUnfortunately so. The Guardian Force is\x01",
            "conducting patrols there as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100600V#3608F#5PThat's reassuring...\x02\x03",
            "#1100601V#3610FHmm, perhaps I should pay Mainz\x01",
            "a visit as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100602V#0100F#2PSpeaking of which...\x02\x03",
            "#1100603VI heard you were more than generous\x01",
            "with your offers on the goods you came\x01",
            "to purchase today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100604V#3609F#5PHaha... My, the village chief must really\x01",
            "enjoy talking today.\x02\x03",
            "#1100605V#3600FI wasn't doing it as charity or anything like\x01",
            "that.\x02\x03",
            "#1100606VArmorica's specialty items, especially their\x01",
            "honey, received glowing reviews these past\x01",
            "few months.\x02\x03",
            "#1100607VI simply wanted to use this opportunity to\x01",
            "leave a good impression on the people here.\x01",
            "Nothing but a harmless marketing strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100608V#0309F#2PNot too shabby.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100609V#0202F#12PI imagine earning a client's trust is\x01",
            "vital in any sort of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100610V#0102F#2PIf that's the case, you must be\x01",
            "running a smooth operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100611V#3600F#5PNo, no. I still have a lot to learn.\x01",
            "I'm still a greenhorn in the realm\x01",
            "of business.\x02\x03",
            "#1100612V#3610FAlso, allow me to apologize...\x02\x03",
            "#1100613VI sincerely wish I had more pertinent\x01",
            "information to give you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100614V#0011F#12PNo, please don't let that bother you.\x02\x03",
            "#1100615V#0000FAfter all, we should be the ones apologizing,\x01",
            "taking up all your precious time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1100616V#3600F#5PNot at all. Best of luck to you all with\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 115180, 0, -450, 270)
    OP_93(0x1B, 0x10E, 0x0)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x60, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_41_10EDF end

    def Function_42_11F3D(): pass

    label("Function_42_11F3D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1200, 1200, 3000, 0)
    MoveCamera(306, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -470, 0, 2360, 315)
    SetChrPos(0x102, -1200, 0, 1520, 315)
    SetChrPos(0x103, 880, 0, 1830, 315)
    SetChrPos(0x104, 80, 0, 1070, 315)
    SetChrFlags(0xB, 0x80)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0xE, -1420, 180, 3810, 90)
    SetChrSubChip(0xE, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12008")
    SetChrPos(0x109, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_12033")

    label("loc_12008")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12033")
    SetChrPos(0x10A, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_12033")

    OP_0D()

    ChrTalk(
        0x101,
        "#6P#0000FExcuse us, are you Alfred?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PYes, that's me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11POh, the Special Support Section? You were\x01",
            "the ones who searched the Ancient\x01",
            "Battlefield for that couple, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PDo you need something from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYes, sir. You see, we're working on a\x01",
            "request we received from the library.\x02\x03",
            "We came to collect an overdue book\x01",
            "from you. Do you have any idea\x01",
            "where it is?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11POh, that? I apologize for being so\x01",
            "careless. That's very unlike me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        (
            "#11PGive me a second, and I'll go grab\x01",
            "it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11P...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1230C")
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_1230C")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#0005FU-Uh, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0106FDid you lose it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0xE,
        "#11PI-I don't think I LOST it, per se...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PHmm, where in the world could\x01",
            "that book have gone...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#11POh, right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    ChrTalk(
        0xE,
        (
            "#5PGofan. Do you still have that book\x01",
            "I let you borrow the other day?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)
    OP_93(0x101, 0x0, 0x190)
    OP_93(0x103, 0x0, 0x190)
    OP_93(0x104, 0x0, 0x190)
    OP_93(0x102, 0x0, 0x190)

    ChrTalk(
        0xA,
        "#11PA book...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYes, a book. THAT book. You told\x01",
            "me that you'd like to give it a read,\x01",
            "so I let you borrow it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11POhhh, that book! Yes, I remember\x01",
            "now. Sorry about that. Let me go\x01",
            "find it for you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12544():
        OP_95(0xFE, -1940, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12544)
    WaitChrThread(0xA, 1)

    def lambda_12562():
        OP_95(0xFE, -1940, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12562)
    WaitChrThread(0xA, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12603")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_12603")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#0306FLet me get this straight...\x01",
            "You subleased a library book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FHow thoughtless...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1269D")

    ChrTalk(
        0x109,
        "#6P#0509FH-Haha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_126BF")

    label("loc_1269D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_126BF")

    ChrTalk(
        0x10A,
        "#6P#0603F...\x02",
    )

    CloseMessageWindow()

    label("loc_126BF")

    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0xE,
        (
            "#11PI'm ashamed, I assure you.\x01",
            "Normally, I'd never do such\x01",
            "a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWith so many books to read, I must\x01",
            "have not thought it through all the way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    ChrTalk(
        0xE,
        "#5PGofan, did you find the book?\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0xA,
        "#11PAbout that...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1284B")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_1284B")

    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#5PWhat? How could you have\x01",
            "possibly lost it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0012FU-Uh, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PJust wait a second, please. I'll try\x01",
            "to remember what I did with it...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PI've got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIf I'm not mistaken, I accidentally let\x01",
            "a customer borrow it after he wouldn't\x01",
            "stop badgering me about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0011FWHAT?! How do you 'accidentally'\x01",
            "lend someone a book?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0305FSub-subleasing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0106FI can't say I was expecting this turn of events.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FThis is unbelievable...\x02\x03",
            "#0200FWho exactly did you lend it to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PIt was Elkin, the guy who's always tinkering\x01",
            "with the orbal truck near the village gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh, I messed up big time...\x01",
            "Please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FI-It's okay. You already lent it to\x01",
            "someone, and what's done is\x01",
            "done.\x02\x03",
            "#0000FOkay, everyone. Let's find Elkin\x01",
            "and see if he has it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12BE4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_12BE4")

    SetChrPos(0x0, -470, 0, 2360, 315)
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    OP_29(0x28, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_42_11F3D end

    SaveToFile()

Try(main)
