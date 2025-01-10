from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1530.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("t1530", "t1530_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 5, 0, 7],
    )

    BuildStringList((
        "t1530",                  # 0
        "Receptionist Sera",      # 1
        "Chief Clark",            # 2
        "Nurse Lan",              # 3
        "Doctor Lago",            # 4
        "Doctor Lago",            # 5
        "Medical Intern Gwen",    # 6
        "Doctor Gailey",          # 7
        "Doctor Gailey",          # 8
        "Medical Intern Chaleur", # 9
        "Doctor Guenter",         # 10
        "Doctor Belldine",        # 11
        "Chief Ursuline",         # 12
        "Chief Ursuline",         # 13
        "Medical Intern Lytton",  # 14
        "Amisa",                  # 15
        "Mr. Crois",              # 16
        "Kienz",                  # 17
        "Outpatient",             # 18
        "Outpatient",             # 19
        "Outpatient",             # 20
        "Outpatient",             # 21
        "Outpatient",             # 22
        "Outpatient",             # 23
        "Outpatient",             # 24
        "Outpatient",             # 25
        "Outpatient",             # 26
        "Outpatient",             # 27
        "Outpatient",             # 28
        "Outpatient",             # 29
        "Outpatient",             # 30
        "Outpatient",             # 31
        "Outpatient",             # 32
        "Outpatient",             # 33
        "Outpatient",             # 34
        "Outpatient",             # 35
        "Outpatient",             # 36
        "Outpatient",             # 37
        "Outpatient",             # 38
        "Outpatient",             # 39
        "Outpatient",             # 40
        "Outpatient",             # 41
        "Outpatient",             # 42
        "Citizen",                # 43
        "Outpatient",             # 44
        "Outpatient",             # 45
        "Outpatient",             # 46
        "Outpatient",             # 47
        "Outpatient",             # 48
        "Outpatient",             # 49
        "Outpatient",             # 50
        "Outpatient",             # 51
        "Outpatient",             # 52
        "Outpatient",             # 53
        "Outpatient",             # 54
        "Outpatient",             # 55
        "Outpatient",             # 56
        "Girl",                   # 57
        "Boy",                    # 58
        "Tourist",                # 59
        "Tourist",                # 60
        "Cecile",                 # 61
        "Michaud",                # 62
        "Bracer Lynn",            # 63
        "Bracer Aeolia",          # 64
    ))

    AddCharChip((
        "chr/ch05300.itc",                   # 00
        "chr/ch28200.itc",                   # 01
        "chr/ch28000.itc",                   # 02
        "chr/ch29700.itc",                   # 03
        "chr/ch21002.itc",                   # 04
        "chr/ch20002.itc",                   # 05
        "chr/ch20402.itc",                   # 06
        "chr/ch20302.itc",                   # 07
        "chr/ch22300.itc",                   # 08
        "chr/ch29202.itc",                   # 09
        "chr/ch29500.itc",                   # 0A
        "chr/ch32702.itc",                   # 0B
        "chr/ch32800.itc",                   # 0C
        "chr/ch07100.itc",                   # 0D
        "chr/ch29300.itc",                   # 0E
        "chr/ch32900.itc",                   # 0F
        "chr/ch29200.itc",                   # 10
        "chr/ch32700.itc",                   # 11
        "chr/ch29400.itc",                   # 12
        "chr/ch21602.itc",                   # 13
        "chr/ch20600.itc",                   # 14
        "chr/ch22702.itc",                   # 15
        "chr/ch21802.itc",                   # 16
        "chr/ch23702.itc",                   # 17
        "chr/ch23602.itc",                   # 18
        "chr/ch21902.itc",                   # 19
        "chr/ch22202.itc",                   # 1A
        "chr/ch20502.itc",                   # 1B
        "chr/ch22802.itc",                   # 1C
        "chr/ch20102.itc",                   # 1D
        "chr/ch21600.itc",                   # 1E
        "chr/ch24402.itc",                   # 1F
        "chr/ch24502.itc",                   # 20
        "chr/ch32200.itc",                   # 21
        "chr/ch21102.itc",                   # 22
        "chr/ch20602.itc",                   # 23
        "chr/ch20802.itc",                   # 24
        "chr/ch21502.itc",                   # 25
        "chr/ch21702.itc",                   # 26
        "apl/ch50146.itc",                   # 27
        "chr/ch05600.itc",                   # 28
        "apl/ch50385.itc",                   # 29
        "chr/ch24400.itc",                   # 2A
        "chr/ch32000.itc",                   # 2B
        "chr/ch32100.itc",                   # 2C
    ))

    DeclNpc(17209,   0,       7429,    266,  261,  0x0, 0,   1,   0,   0,   0,   1,   1,   255,  0)
    DeclNpc(19739,   0,       4889,    180,  261,  0x0, 0,   2,   0,   0,   0,   1,   3,   255,  0)
    DeclNpc(10539,   0,       -4489,   325,  261,  0x0, 0,   3,   0,   0,   0,   1,   4,   255,  0)
    DeclNpc(55650,   0,       500,     180,  405,  0x0, 0,   16,  0,   0,   0,   1,   6,   255,  0)
    DeclNpc(50979,   119,     59069,   300,  469,  0x0, 0,   9,   0,   255, 255, 1,   7,   255,  0)
    DeclNpc(58849,   0,       58389,   0,    389,  0x0, 0,   10,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(55650,   0,       -620,    0,    405,  0x0, 0,   17,  0,   0,   0,   1,   9,   255,  0)
    DeclNpc(49930,   119,     -59340,  260,  469,  0x0, 0,   11,  0,   255, 255, 1,   10,  255,  0)
    DeclNpc(60270,   0,       -56930,  90,   389,  0x0, 0,   12,  0,   0,   0,   1,   13,  255,  0)
    DeclNpc(17180,   0,       -4079,   180,  389,  0x0, 0,   13,  0,   0,   0,   1,   14,  255,  0)
    DeclNpc(17180,   0,       -5289,   0,    389,  0x0, 0,   14,  0,   0,   0,   1,   15,  255,  0)
    DeclNpc(56430,   0,       -55270,  90,   389,  0x0, 0,   15,  0,   0,   0,   1,   17,  255,  0)
    DeclNpc(56889,   800,     -58250,  0,    469,  0x0, 0,   39,  0,   255, 255, 1,   18,  255,  0)
    DeclNpc(53970,   0,       51840,   135,  389,  0x0, 0,   18,  0,   0,   0,   1,   19,  255,  0)
    DeclNpc(16049,   100,     -6989,   0,    469,  0x0, 0,   37,  0,   255, 255, 1,   20,  255,  0)
    DeclNpc(14470,   0,       7309,    90,   389,  0x0, 0,   40,  0,   0,   0,   1,   24,  255,  0)
    DeclNpc(14470,   0,       7309,    90,   389,  0x0, 0,   41,  0,   0,   0,   1,   25,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   4,   0,   255, 255, 1,   27,  255,  0)
    DeclNpc(16559,   119,     -9979,   0,    469,  0x0, 0,   5,   0,   255, 255, 1,   28,  255,  0)
    DeclNpc(8340,    119,     9890,    180,  469,  0x0, 0,   6,   0,   255, 255, 1,   29,  255,  0)
    DeclNpc(5000,    119,     4530,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   30,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   31,  255,  0)
    DeclNpc(21840,   119,     -7219,   270,  469,  0x0, 0,   6,   0,   255, 255, 1,   32,  255,  0)
    DeclNpc(5099,    119,     4739,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   33,  255,  0)
    DeclNpc(21840,   119,     -4429,   270,  469,  0x0, 0,   21,  0,   255, 255, 1,   34,  255,  0)
    DeclNpc(16799,   119,     -6889,   0,    469,  0x0, 0,   22,  0,   255, 255, 1,   35,  255,  0)
    DeclNpc(7400,    119,     6849,    180,  469,  0x0, 0,   23,  0,   255, 255, 1,   36,  255,  0)
    DeclNpc(2000,    119,     7880,    90,   469,  0x0, 0,   24,  0,   255, 255, 1,   37,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   38,  255,  0)
    DeclNpc(19729,   119,     -9960,   0,    469,  0x0, 0,   5,   0,   255, 255, 1,   39,  255,  0)
    DeclNpc(5110,    119,     5170,    90,   469,  0x0, 0,   25,  0,   255, 255, 1,   40,  255,  0)
    DeclNpc(5110,    119,     4329,    90,   469,  0x0, 0,   26,  0,   255, 255, 1,   41,  255,  0)
    DeclNpc(18850,   119,     -3970,   270,  469,  0x0, 0,   4,   0,   255, 255, 1,   42,  255,  0)
    DeclNpc(18850,   119,     -5050,   270,  469,  0x0, 0,   27,  0,   255, 255, 1,   43,  255,  0)
    DeclNpc(7750,    119,     9800,    180,  469,  0x0, 0,   28,  0,   255, 255, 1,   44,  255,  0)
    DeclNpc(16809,   119,     -6920,   0,    469,  0x0, 0,   6,   0,   255, 255, 1,   45,  255,  0)
    DeclNpc(21840,   119,     -8199,   270,  469,  0x0, 0,   5,   0,   255, 255, 1,   46,  255,  0)
    DeclNpc(21840,   119,     -7449,   270,  469,  0x0, 0,   29,  0,   255, 255, 1,   47,  255,  0)
    DeclNpc(18850,   119,     -4309,   270,  469,  0x0, 0,   31,  0,   255, 255, 1,   48,  255,  0)
    DeclNpc(18850,   119,     -5219,   270,  469,  0x0, 0,   32,  0,   255, 255, 1,   49,  255,  0)
    DeclNpc(7519,    119,     6840,    180,  469,  0x0, 0,   19,  0,   255, 255, 1,   50,  255,  0)
    DeclNpc(21829,   119,     -3789,   270,  469,  0x0, 0,   19,  0,   255, 255, 1,   51,  255,  0)
    DeclNpc(21829,   119,     -4869,   270,  469,  0x0, 0,   34,  0,   255, 255, 1,   52,  255,  0)
    DeclNpc(4989,    119,     5469,    90,   469,  0x0, 0,   5,   0,   255, 255, 1,   54,  255,  0)
    DeclNpc(4989,    119,     4360,    90,   469,  0x0, 0,   7,   0,   255, 255, 1,   55,  255,  0)
    DeclNpc(18819,   119,     -4750,   270,  469,  0x0, 0,   35,  0,   255, 255, 1,   56,  255,  0)
    DeclNpc(19659,   119,     -9970,   0,    469,  0x0, 0,   28,  0,   255, 255, 1,   57,  255,  0)
    DeclNpc(7349,    119,     6849,    180,  469,  0x0, 0,   25,  0,   255, 255, 1,   58,  255,  0)
    DeclNpc(2000,    119,     4139,    90,   469,  0x0, 0,   36,  0,   255, 255, 1,   59,  255,  0)
    DeclNpc(2000,    119,     7510,    90,   469,  0x0, 0,   4,   0,   255, 255, 1,   60,  255,  0)
    DeclNpc(18909,   119,     -4409,   270,  469,  0x0, 0,   34,  0,   255, 255, 1,   61,  255,  0)
    DeclNpc(18909,   119,     -5349,   270,  469,  0x0, 0,   37,  0,   255, 255, 1,   62,  255,  0)
    DeclNpc(16049,   119,     -6989,   0,    469,  0x0, 0,   6,   0,   255, 255, 1,   63,  255,  0)
    DeclNpc(21829,   119,     -4110,   270,  469,  0x0, 0,   32,  0,   255, 255, 1,   64,  255,  0)
    DeclNpc(8069,    119,     9880,    180,  469,  0x0, 0,   19,  0,   255, 255, 1,   65,  255,  0)
    DeclNpc(5099,    119,     4739,    90,   469,  0x0, 0,   38,  0,   255, 255, 1,   66,  255,  0)
    DeclNpc(7250,    0,       -7599,   90,   389,  0x0, 0,   8,   0,   0,   0,   1,   67,  255,  0)
    DeclNpc(7400,    0,       3740,    270,  389,  0x0, 0,   20,  0,   0,   0,   1,   68,  255,  0)
    DeclNpc(18930,   0,       2579,    15,   389,  0x0, 0,   30,  0,   0,   0,   1,   69,  255,  0)
    DeclNpc(2000,    0,       -7670,   90,   389,  0x0, 0,   33,  0,   0,   0,   1,   70,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   1,   22,  255,  0)
    DeclNpc(11579,   0,       5699,    225,  389,  0x0, 0,   42,  0,   0,   4,   1,   71,  255,  0)
    DeclNpc(22700,   0,       1799,    270,  389,  0x0, 0,   43,  0,   0,   0,   1,   72,  255,  0)
    DeclNpc(49849,   0,       58180,   0,    389,  0x0, 0,   44,  0,   0,   0,   1,   73,  255,  0)

    DeclEvent(0x0000, 0, 15,  12.0,                  12.0,                  -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.0,                  -6.0,                  0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 16,  24.93000030517578,     0.1899999976158142,    -0.0,                  20.25,                 [0.23570220172405243,  0.23570235073566437,   -0.0,                  0.0,                   -0.23570235073566437,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -5.831272602081299,    -5.920843124389648,    0.0,                   1.0])

    DeclActor(16000,   0,       7000,    2000,    17210,   1500,    7430,    0x007E, 1,  0,  0x0000)
    DeclActor(19680,   0,       3710,    2000,    19740,   1500,    4890,    0x007E, 1,  2,  0x0000)
    DeclActor(65800,   0,       2430,    1200,    65800,   1500,    2430,    0x007C, 0,  17, 0x0000)

    ScpFunction((
        "Function_0_9BC",          # 00, 0
        "Function_1_A74",          # 01, 1
        "Function_2_A8C",          # 02, 2
        "Function_3_B3D",          # 03, 3
        "Function_4_B68",          # 04, 4
        "Function_5_B93",          # 05, 5
        "Function_6_1131",         # 06, 6
        "Function_7_1138",         # 07, 7
        "Function_8_11DB",         # 08, 8
        "Function_9_1412",         # 09, 9
        "Function_10_2274",        # 0A, 10
        "Function_11_25AD",        # 0B, 11
        "Function_12_263E",        # 0C, 12
        "Function_13_2E4F",        # 0D, 13
        "Function_14_2EAE",        # 0E, 14
        "Function_15_3512",        # 0F, 15
        "Function_16_3568",        # 10, 16
        "Function_17_35BE",        # 11, 17
    ))


    def Function_0_9BC(): pass

    label("Function_0_9BC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9FC"),
        (1, "loc_A08"),
        (2, "loc_A14"),
        (3, "loc_A20"),
        (4, "loc_A2C"),
        (5, "loc_A38"),
        (6, "loc_A44"),
        (SWITCH_DEFAULT, "loc_A50"),
    )


    label("loc_9FC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A08")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A14")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A20")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A2C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A38")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A44")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A50")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A73")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A5C")

    label("loc_A73")

    Return()

    # Function_0_9BC end

    def Function_1_A74(): pass

    label("Function_1_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_A1(0xFE, 0x4B0, 0x0)
    ExitThread()
    Jump("Function_1_A74")

    label("loc_A8B")

    Return()

    # Function_1_A74 end

    def Function_2_A8C(): pass

    label("Function_2_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3C")
    OP_95(0xFE, 7400, 0, -1600, 1500, 0x0)
    OP_95(0xFE, 7400, 0, 1420, 1500, 0x0)
    OP_95(0xFE, 10380, 0, 4530, 1500, 0x0)
    OP_95(0xFE, 13330, 0, 4550, 1500, 0x0)
    OP_95(0xFE, 16420, 0, 1470, 1500, 0x0)
    OP_95(0xFE, 16420, 0, -1430, 1500, 0x0)
    OP_95(0xFE, 13440, 0, -4490, 1500, 0x0)
    OP_95(0xFE, 10540, 0, -4490, 1500, 0x0)
    Jump("Function_2_A8C")

    label("loc_B3C")

    Return()

    # Function_2_A8C end

    def Function_3_B3D(): pass

    label("Function_3_B3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B67")
    OP_94(0xFE, 0x1932, 0x148C, 0x1DBA, 0xDCA, 0x3E8)
    Sleep(400)
    Jump("Function_3_B3D")

    label("loc_B67")

    Return()

    # Function_3_B3D end

    def Function_4_B68(): pass

    label("Function_4_B68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B92")
    OP_94(0xFE, 0x26D4, 0xBCC, 0x34EE, 0x235A, 0x3E8)
    Sleep(300)
    Jump("Function_4_B68")

    label("loc_B92")

    Return()

    # Function_4_B68 end

    def Function_5_B93(): pass

    label("Function_5_B93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAB")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 6)

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C19")
    SetChrPos(0xA, 16050, 0, -5480, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 56790, 0, 5200, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 57420, 0, -56730, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    Jump("loc_10DC")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C60")
    SetChrPos(0xA, 59030, 0, -1090, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    Jump("loc_10DC")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C9C")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    Jump("loc_10DC")

    label("loc_C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CFE")
    SetChrPos(0xA, 17630, 0, -4730, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x45, 0x80)
    Jump("loc_10DC")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_D55")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    Jump("loc_10DC")

    label("loc_D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DA7")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6660, 0, -5660, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    Jump("loc_10DC")

    label("loc_DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E11")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 51570, 0, 57430, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 49240, 0, 59850, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 48750, 0, -59740, 180)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x43, 0x80)
    Jump("loc_10DC")

    label("loc_E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E90")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 56790, 0, 5200, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 54470, 0, -4240, 0)
    ClearChrFlags(0x44, 0x80)
    SetChrPos(0x44, 8160, 0, 400, 180)
    SetChrPos(0xA, 8160, 0, -630, 0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x42, 0x80)
    Jump("loc_10DC")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ED2")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_10DC")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F19")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_10DC")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F55")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_10DC")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FE3")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 16050, 0, -5480, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 48580, 0, -59600, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x41, 0x80)
    BeginChrThread(0x41, 0, 0, 3)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    SetChrPos(0xB, 49790, 0, 59830, 180)
    Jump("loc_10DC")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_101C")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 56870, 0, 2560, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_10DC")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1058")
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_10DC")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_10A4")
    SetChrPos(0xA, 9660, 0, 2050, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x40, 0x80)
    Jump("loc_10DC")

    label("loc_10A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10DC")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 17680, 0, -3850, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)

    label("loc_10DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F7")
    Event(0, 8)
    SetMapFlags(0x10000000)
    Jump("loc_110D")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110D")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_110D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1121")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)
    Jump("loc_1130")

    label("loc_1121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1130")
    ClearScenarioFlags(0x5C, 1)
    Event(1, 77)

    label("loc_1130")

    Return()

    # Function_5_B93 end

    def Function_6_1131(): pass

    label("Function_6_1131")

    Sound(160, 0, 100, 0)
    Return()

    # Function_6_1131 end

    def Function_7_1138(): pass

    label("Function_7_1138")

    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1151")
    Jump("loc_1169")

    label("loc_1151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1169")
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_1169")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118B")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_118B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_11DA")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_11DA")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_11DA")

    Return()

    # Function_7_1138 end

    def Function_8_11DB(): pass

    label("Function_8_11DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(20530, 1000, 0, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 2200, 0, -700, 90)
    SetChrPos(0x102, 2200, 0, 600, 90)
    SetChrPos(0x103, 900, 0, -700, 90)
    SetChrPos(0x104, 900, 0, 600, 90)
    OP_68(4000, 1000, 0, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(2520, 1000, -280, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21610, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1101058V#6P#0000FWe lucked out... Doesn't look like\x01",
            "it's too crowded today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101059V#0104F#5PYeah. The waiting room is usually packed\x01",
            "with people.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_134E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_134E)
    WaitChrThread(0x102, 1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1101060V#0100F#5PShould we try asking for her at the\x01",
            "front desk?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#1101061V#12P#0000FDefinitely. Let's have them call her.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 1500, 0, -100, 90)
    SetScenarioFlags(0x61, 7)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_8_11DB end

    def Function_9_1412(): pass

    label("Function_9_1412")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50014.itc", 0x3C)
    LoadChrToIndex("apl/ch50102.itc", 0x3D)
    OP_4B(0x8, 0xFF)
    OP_68(15690, 600, 7270, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 14410, 0, 6710, 90)
    SetChrPos(0x102, 14130, 0, 5550, 90)
    SetChrPos(0x103, 12820, 0, 5690, 90)
    SetChrPos(0x104, 13070, 0, 6870, 90)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    ClearChrFlags(0x44, 0x4)
    ClearChrFlags(0x44, 0x80)
    OP_4B(0x44, 0xFF)
    SetChrPos(0x44, 12000, 1050, 13300, 180)
    OP_A7(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(22630, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#1101062V#11PWelcome to St. Ursula Hospital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101063V#11PDo you need outpatient care or\x01",
            "did you have an appointment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101064V#0005F#6PAh, no...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x3C)
    SetChrSubChip(0x101, 0x3)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1101065V#0000F#6PI'm Lloyd Bannings of the Crossbell Police\x01",
            "Department, Special Support Section.\x02\x03",
            "#1101066VWe're here to conduct an investigation of the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1101067V#11PI see, so you're with the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101068V#11PThis investigation... Is it related to the\x01",
            "monster attack?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101069V#0003F#6PYes, ma'am. We received a request from\x01",
            "the CGF to investigate St. Ursula.\x02\x03",
            "#1101070V#0001FWe'd like to speak with everyone\x01",
            "involved in the incident, if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101071V#11PAll right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101072V#11PThe hospital director isn't here right now,\x01",
            "so I'll call the head nurse for you instead.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1101073V#0011F#6PA-Also...one other thing.\x02\x03",
            "#1101074VSomeone I know works here...\x02\x03",
            "#1101075V#0012F...and if she isn't busy at the moment, I'd\x01",
            "like to see if she could show us around.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0xFFFF)

    ChrTalk(
        0x103,
        "#1101076V#0202F#6P(He sounds somewhat nervous.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#1101077V#0301F(So am I! A beautiful nurse is a gift from Aidios!)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        "#1101078V#0106F#11P(Oh, please, grow up.)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x44,
        "Woman's Voice",
        "#1101079VLloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrFlags(0x1B, 0x80)

    def lambda_1AAA():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AAA)

    def lambda_1AB7():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AB7)
    Sleep(100)

    def lambda_1AC7():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AC7)

    def lambda_1AD4():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AD4)

    def lambda_1AE1():
        TurnDirection(0xFE, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AE1)
    OP_68(14050, 600, 9110, 3000)
    MoveCamera(30, 18, 0, 3000)

    def lambda_1B0A():
        OP_95(0xFE, 11970, 0, 10920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_1B0A)
    Sleep(200)

    def lambda_1B27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_1B27)
    WaitChrThread(0x44, 1)
    WaitChrThread(0x44, 2)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
    Sleep(500)

    NpcTalk(
        0x44,
        "Nurse",
        "#1101080V#1305F#5P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101081V#0005F#12PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101082V#0305F#6PHoly crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101083V#0105F#12PShe's so pretty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101084V#0205F#6PIs she an angel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101085V#2POh, Cecile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101086V#2PGood timing. These police officers just arrived.\x01",
            "They've come about some investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(13560, 600, 9860, 1500)

    def lambda_1CAB():
        OP_95(0xFE, 12960, 0, 8710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CAB)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)

    def lambda_1CCB():
        TurnDirection(0x102, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CCB)

    def lambda_1CD8():
        TurnDirection(0x103, 0x44, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CD8)
    Sleep(100)

    def lambda_1CE8():
        TurnDirection(0x104, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CE8)

    ChrTalk(
        0x101,
        (
            "#1101087V#0011F#12PUmm... Sorry for visiting all of a sudden...\x02\x03",
            "#1101088V#0009FI probably should've called first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x44,
        "#1101089V#1301F#5P...\x02",
    )

    CloseMessageWindow()
    OP_68(13660, 600, 9340, 500)
    SetChrFlags(0x44, 0x40)

    def lambda_1D9E():
        OP_95(0xFE, 12750, 0, 9200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_1D9E)
    WaitChrThread(0x44, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)

    def lambda_1DCD():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DCD)
    SetCameraDistance(22130, 0)
    SetChrChipByIndex(0x44, 0x3D)
    SetChrSubChip(0x44, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
        "#1101090V#0011F#12PWhoa, Cecile! Are you crying?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x44,
        (
            "#1101091V#1304F#5P#40WWelcome back, Lloyd...\x02\x03",
            "#1101092VIt's been a really long time. Too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101093V#0002F#12PY-Yeah...\x02\x03",
            "#1101094V#0004FI'm sorry for not visiting sooner, but\x01",
            "I've been caught up with work and...\x02\x03",
            "#1101095V#0011FM-More importantly, isn't this a little\x01",
            "much? You're embarrassing me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x44,
        (
            "#1101096V#1304F#5P#30WOh, who cares about that! Now, give\x01",
            "your big sister a hug!\x02\x03",
            "#1101097V#1302FHeehee... You've gotten so tall.\x02\x03",
            "#1101098VWe were about the same height when\x01",
            "you left for Calvard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101099V#0012F#12PH-Haha. Well, I HAVE had three years\x01",
            "to grow, Cecile.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x8,
        "#1101100V#2PU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101101V#0109F#4P(I-I don't know what to say...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101102V#0206F#12P(She is even sweeter than I imagined.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101103V#0307F#6P(Damn you Lloyd...! Shoulda told me you\x01",
            "had such a lovely sister from the get-go!)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(23130, 3000)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1412 end

    def Function_10_2274(): pass

    label("Function_10_2274")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(2200, 1000, -100, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24440, 0)
    OP_68(3670, 1000, 220, 3000)
    SetChrPos(0x136, 1800, 0, -100, 90)
    SetChrPos(0x101, 0, 0, -700, 90)
    SetChrPos(0x102, 0, 0, 600, 90)
    SetChrPos(0x103, 0, 0, -700, 90)
    SetChrPos(0x104, 0, 0, 600, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_234E():
        OP_96(0xFE, 0x1130, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_234E)
    Sleep(600)

    def lambda_236B():
        OP_96(0xFE, 0x898, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_236B)

    def lambda_2385():
        OP_96(0xFE, 0x898, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2385)

    def lambda_239F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_239F)

    def lambda_23B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_23B0)
    Sleep(1200)

    def lambda_23C4():
        OP_96(0xFE, 0x384, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23C4)

    def lambda_23DE():
        OP_96(0xFE, 0x384, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23DE)

    def lambda_23F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_23F8)

    def lambda_2409():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2409)
    WaitChrThread(0x136, 1)

    def lambda_241E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_241E)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x136,
        (
            "#1101174V#1300F#11PHere in the hospital, we maintain sickrooms\x01",
            "on the second and third floors.\x02\x03",
            "#1101175VThe intern you're looking for should be in\x01",
            "one on the second floor. I can lead you to\x01",
            "him, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101176V#0000F#6PAppreciate it, Cecile.\x02",
    )

    CloseMessageWindow()

    def lambda_2548():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_2548)
    WaitChrThread(0x136, 1)
    OP_68(11450, 1000, 7080, 12000)
    BeginChrThread(0x136, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x65, 6)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2274 end

    def Function_11_25AD(): pass

    label("Function_11_25AD")


    def lambda_25B2():
        OP_95(0xFE, 4400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25B2)
    WaitChrThread(0xFE, 1)

    def lambda_25D0():
        OP_95(0xFE, 11980, 0, 6820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25D0)
    WaitChrThread(0xFE, 1)

    def lambda_25EE():
        OP_95(0xFE, 11760, 0, 10650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25EE)
    WaitChrThread(0xFE, 1)

    def lambda_260C():
        OP_95(0xFE, 12190, 140, 12390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_260C)
    Sleep(500)

    def lambda_2629():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2629)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_25AD end

    def Function_12_263E(): pass

    label("Function_12_263E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17660, 1000, 7870, 0)
    MoveCamera(66, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26750, 0)
    SetChrPos(0x101, 14410, 0, 6710, 45)
    SetChrPos(0x153, 12450, 0, 6560, 45)
    SetChrPos(0xEF, 11920, 0, 5340, 45)
    OP_4B(0x44, 0xFF)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    SetChrPos(0x44, 13290, 0, 8050, 90)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 20770, 0, 9100, 45)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(25000, 2500)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x8,
        "#3600813V#5PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3600814V#5PYes, sir. I'll send them to the research ward, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_68(16430, 1000, 7320, 2500)

    def lambda_277B():
        OP_95(0xFE, 17210, 0, 7430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_277B)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#3600815V#5PDoctor Guenter says he can see you now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600816V#5PHe will meet you at his laboratory in\x01",
            "the research ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600817V#0004F#6PAwesome. Thank goodness he isn't busy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x44, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x44,
        "#3600818V#1302F#5PI'll excuse myself, then.\x02",
    )

    CloseMessageWindow()

    def lambda_2897():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2897)
    Sleep(50)

    def lambda_28A7():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_28A7)
    Sleep(50)

    def lambda_28B7():
        TurnDirection(0xFE, 0x44, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_28B7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x101,
        (
            "#3600819V#0002F#11PThanks for the help as always, Cecile. We'll\x01",
            "make sure to say bye before leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x44,
        (
            "#3600820V#1302F#5PI can't wait.\x02\x03",
            "#3600821V#1309FSee you soon, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600822V#1109F#12PSee ya!\x02",
    )

    CloseMessageWindow()
    OP_93(0x44, 0x0, 0x1F4)
    OP_68(15600, 1000, 9190, 3000)

    def lambda_29BA():

        label("loc_29BA")

        TurnDirection(0x101, 0x44, 500)
        Yield()
        Jump("loc_29BA")

    QueueWorkItem2(0x101, 1, lambda_29BA)

    def lambda_29CC():

        label("loc_29CC")

        TurnDirection(0xEF, 0x44, 500)
        Yield()
        Jump("loc_29CC")

    QueueWorkItem2(0xEF, 1, lambda_29CC)

    def lambda_29DE():

        label("loc_29DE")

        TurnDirection(0x153, 0x44, 500)
        Yield()
        Jump("loc_29DE")

    QueueWorkItem2(0x153, 1, lambda_29DE)

    def lambda_29F0():

        label("loc_29F0")

        TurnDirection(0x8, 0x44, 500)
        Yield()
        Jump("loc_29F0")

    QueueWorkItem2(0x8, 1, lambda_29F0)
    BeginChrThread(0x44, 3, 0, 13)
    WaitChrThread(0x44, 3)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x153, 0x1)
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2A61")

    ChrTalk(
        0x102,
        "#3600823V#0100FShe's really diligent about her work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2AA2")

    ChrTalk(
        0x103,
        "#3600824V#0200FWork keeps her busy, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2AE3")

    ChrTalk(
        0x104,
        "#3600825V#0300F*sigh* Always the workin' lady, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_2AE3")


    ChrTalk(
        0x8,
        (
            "#3600826V#11PI doubt there's anyone in this entire\x01",
            "hospital who works as hard as Cecile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600827V#11PSometimes, I wish she would take a page\x01",
            "out of Doctor Guenter's book and skip a\x01",
            "few shifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600828V#0012F#5PHaha...\x02\x03",
            "#3600829V#0000F(Try not to overwork yourself, Cecile.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16430, 1000, 7320, 1500)
    TurnDirection(0x8, 0x101, 500)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#3600830V#5PCome to think of it, do you even know\x01",
            "how to get to Doctor Guenter's lab?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3600831V#5PIt's on the fourth floor of the research ward.\x01",
            "I could take you there, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CFC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CFC)
    Sleep(50)

    def lambda_2D0C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D0C)
    Sleep(50)

    def lambda_2D1C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_2D1C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)

    ChrTalk(
        0x101,
        "#3600832V#0002F#6PI think we'll be all right. Thanks, though.\x02",
    )

    CloseMessageWindow()

    def lambda_2D78():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D78)
    Sleep(50)

    def lambda_2D88():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D88)
    Sleep(50)

    def lambda_2D98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_2D98)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3600833V#0000F#5PReady to see the doctor, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600834V#1110F#6PYep! To the research thingy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x44, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x0, 14000, 0, 6500, 90)
    SetScenarioFlags(0xA8, 5)
    OP_29(0x48, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_12_263E end

    def Function_13_2E4F(): pass

    label("Function_13_2E4F")


    def lambda_2E54():
        OP_95(0xFE, 11960, 0, 11140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E54)
    WaitChrThread(0xFE, 1)

    def lambda_2E72():
        OP_95(0xFE, 12060, 1030, 13280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E72)
    Sleep(250)

    def lambda_2E8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E8F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_13_2E4F end

    def Function_14_2EAE(): pass

    label("Function_14_2EAE")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(16430, 800, 7320, 0)
    MoveCamera(66, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 14410, 0, 6710, 45)
    SetChrPos(0x102, 12450, 0, 6560, 45)
    SetChrPos(0x103, 11920, 0, 5340, 45)
    SetChrPos(0x104, 13560, 0, 5070, 45)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#4200847V#5PWhy, hello there, everyone. Are you\x01",
            "here to visit Cecile today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200848V#0005F#6POh, not today.\x02\x03",
            "#4200849V#0000FWe're here to meet with Doctor Guenter again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200850V#0100F#6PCould you ask him if he's busy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200851V#5POf course.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    OP_68(17660, 800, 7870, 3000)

    def lambda_305B():
        OP_95(0xFE, 20770, 0, 9100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_305B)
    WaitChrThread(0x8, 1)
    Sound(807, 0, 100, 0)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#4200852V#5PAh, Doctor. I see you picked up the\x01",
            "phone today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200853V#5PYou have some visitors. If you have\x01",
            "some free time, would you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200854V#5POh? Bad timing? Do you have some\x01",
            "examination or research to do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200855V#5PI see what's going on here. Planning\x01",
            "to go fishing, Doctor Guenter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200856V#5PThat's no good. Try to do your job\x01",
            "while on the clock, all right?\x02",
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
        "#4200857V#0012F#6P(He's the same as always.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200858V#0211F#6P#N(Though he is exceptional in his field,\x01",
            "his dedication seems...lacking.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#4200859V#5PYes, it's Detective Bannings, from\x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200860V#5PYes. Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200861V#5PShould I have them meet you\x01",
            "in your laboratory, then?\x02",
        )
    )

    CloseMessageWindow()
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    OP_68(16430, 800, 7320, 2300)

    def lambda_33DF():
        OP_95(0xFE, 17210, 0, 7430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33DF)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#4200862V#5PWell, Doctor Guenter can see you now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200863V#5PIf you'll head up to the research ward, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200864V#0002F#6PTh-Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200865V#0309F#12PHaha, looks like we threw a wrench\x01",
            "in his plans.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 14000, 0, 6500, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC3, 3)
    OP_29(0x4C, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_14_2EAE end

    def Function_15_3512(): pass

    label("Function_15_3512")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FWe should go ask the receptionist\x01",
            "if Cecile's in.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11400, 0, 9830, 180)
    EventEnd(0x4)
    Return()

    # Function_15_3512 end

    def Function_16_3568(): pass

    label("Function_16_3568")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FWe should go ask the receptionist\x01",
            "if Cecile's in.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 21960, 0, -230, 270)
    EventEnd(0x4)
    Return()

    # Function_16_3568 end

    def Function_17_35BE(): pass

    label("Function_17_35BE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ICU (Intensive Care Unit)\x01",
            "Authorized Personnel Only\x01",
            "　Persons entering: Please follow the Level 2\x01",
            "　or higher sterilization protocol.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_35BE end

    SaveToFile()

Try(main)
