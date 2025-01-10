from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1540.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("t1540", "t1540_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1540",                  # 0
        "Medical Intern Lytton",  # 1
        "Nurse Cirone",           # 2
        "Nurse Philia",           # 3
        "Head Nurse Martha",      # 4
        "Nurse Meifa",            # 5
        "Cecile",                 # 6
        "Doctor Belldine",        # 7
        "Inspector Donovan",      # 8
        "Detective Raymond",      # 9
        "Inpatient",              # 10
        "Inpatient",              # 11
        "Inpatient",              # 12
        "Inpatient",              # 13
        "Inpatient",              # 14
        "Girl",                   # 15
        "Inpatient",              # 16
        "Inpatient",              # 17
        "Inpatient",              # 18
        "Inpatient",              # 19
        "Inpatient",              # 20
        "Inpatient",              # 21
        "Inpatient",              # 22
        "Inpatient",              # 23
        "Inpatient",              # 24
        "Inpatient",              # 25
        "Inpatient",              # 26
        "Inpatient",              # 27
        "Inpatient",              # 28
        "Inpatient",              # 29
        "Inpatient",              # 30
        "Inpatient",              # 31
        "Inpatient",              # 32
        "Inpatient",              # 33
        "Inpatient",              # 34
        "Inpatient",              # 35
        "Inpatient",              # 36
        "Heiyue Member",          # 37
        "Visitor",                # 38
        "Visitor",                # 39
        "Tourist Varian",         # 40
        "Doctor Guenter",         # 41
    ))

    AddCharChip((
        "apl/ch50150.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "apl/ch50133.itc",                   # 02
        "apl/ch50137.itc",                   # 03
        "chr/ch29600.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch07100.itc",                   # 06
        "apl/ch50143.itc",                   # 07
        "chr/ch33100.itc",                   # 08
        "apl/ch50132.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch05300.itc",                   # 0C
        "chr/ch29300.itc",                   # 0D
        "apl/ch50135.itc",                   # 0E
        "apl/ch50141.itc",                   # 0F
        "apl/ch50139.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "apl/ch50152.itc",                   # 12
        "apl/ch50142.itc",                   # 13
        "chr/ch20500.itc",                   # 14
        "chr/ch30300.itc",                   # 15
        "chr/ch30200.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   0,   0,   255, 255, 1,   0,   255,  0)
    DeclNpc(110709,  0,       -5639,   0,    389,  0x0, 0,   1,   0,   0,   0,   1,   1,   255,  0)
    DeclNpc(24610,   0,       680,     225,  261,  0x0, 0,   1,   0,   0,   0,   1,   5,   255,  0)
    DeclNpc(108930,  0,       1450,    45,   261,  0x0, 0,   4,   0,   0,   0,   1,   6,   255,  0)
    DeclNpc(110709,  0,       -4320,   90,   389,  0x0, 0,   5,   0,   0,   0,   1,   7,   255,  0)
    DeclNpc(110709,  0,       -4320,   90,   389,  0x0, 0,   12,  0,   0,   0,   1,   8,   255,  0)
    DeclNpc(110720,  0,       -4239,   180,  389,  0x0, 0,   13,  0,   0,   0,   1,   9,   255,  0)
    DeclNpc(12779,   0,       1299,    270,  389,  0x0, 0,   21,  0,   0,   0,   1,   10,  255,  0)
    DeclNpc(11350,   0,       1299,    90,   389,  0x0, 0,   22,  0,   0,   0,   1,   11,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   2,   0,   255, 255, 1,   13,  255,  0)
    DeclNpc(4809,    400,     -51959,  0,    469,  0x0, 0,   9,   0,   255, 255, 1,   14,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   3,   0,   255, 255, 1,   15,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   7,   0,   255, 255, 1,   16,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   14,  0,   255, 255, 1,   17,  255,  0)
    DeclNpc(-3440,   0,       53919,   180,  389,  0x0, 0,   10,  0,   0,   0,   1,   20,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   21,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   22,  255,  0)
    DeclNpc(4829,    400,     57029,   0,    469,  0x0, 0,   9,   0,   255, 255, 1,   23,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   24,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   15,  0,   255, 255, 1,   25,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   26,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   27,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   28,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   29,  255,  0)
    DeclNpc(4949,    699,     57029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   30,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   3,   0,   255, 255, 1,   31,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   32,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   33,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   15,  0,   255, 255, 1,   34,  255,  0)
    DeclNpc(-4000,   699,     57029,   270,  469,  0x0, 0,   2,   0,   255, 255, 1,   37,  255,  0)
    DeclNpc(-4230,   400,     57029,   0,    469,  0x0, 0,   9,   0,   255, 255, 1,   38,  255,  0)
    DeclNpc(-4000,   699,     52029,   270,  469,  0x0, 0,   15,  0,   255, 255, 1,   39,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  469,  0x0, 0,   14,  0,   255, 255, 1,   41,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  469,  0x0, 0,   16,  0,   255, 255, 1,   42,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  469,  0x0, 0,   7,   0,   255, 255, 1,   43,  255,  0)
    DeclNpc(4809,    400,     -51959,  0,    469,  0x0, 0,   19,  0,   255, 255, 1,   44,  255,  0)
    DeclNpc(4949,    699,     52029,   270,  469,  0x0, 0,   18,  0,   255, 255, 1,   45,  255,  0)
    DeclNpc(-4800,   0,       -53659,  0,    389,  0x0, 0,   17,  0,   0,   0,   1,   35,  255,  0)
    DeclNpc(-4409,   0,       53549,   180,  389,  0x0, 0,   20,  0,   0,   0,   1,   40,  255,  0)
    DeclNpc(30569,   0,       -21719,  315,  385,  0x0, 0,   8,   0,   0,   0,   1,   48,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   1,   46,  255,  0)

    DeclActor(23500,   0,       -830,    1500,    24610,   1500,    680,     0x007E, 1,  4,  0x0000)
    DeclActor(3960,    0,       56230,   1500,    4950,    1700,    57030,   0x007E, 1,  26, 0x0000)

    ScpFunction((
        "Function_0_608",          # 00, 0
        "Function_1_6C0",          # 01, 1
        "Function_2_BCF",          # 02, 2
        "Function_3_BD6",          # 03, 3
        "Function_4_129A",         # 04, 4
        "Function_5_13EA",         # 05, 5
        "Function_6_151A",         # 06, 6
        "Function_7_154E",         # 07, 7
        "Function_8_2A38",         # 08, 8
        "Function_9_2AEB",         # 09, 9
        "Function_10_38D3",        # 0A, 10
        "Function_11_3B86",        # 0B, 11
        "Function_12_55E7",        # 0C, 12
        "Function_13_5C93",        # 0D, 13
    ))


    def Function_0_608(): pass

    label("Function_0_608")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_648"),
        (1, "loc_654"),
        (2, "loc_660"),
        (3, "loc_66C"),
        (4, "loc_678"),
        (5, "loc_684"),
        (6, "loc_690"),
        (SWITCH_DEFAULT, "loc_69C"),
    )


    label("loc_648")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_654")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_660")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_66C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_678")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_684")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_690")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_69C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_6A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A8")

    label("loc_6BF")

    Return()

    # Function_0_608 end

    def Function_1_6C0(): pass

    label("Function_1_6C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_730")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 5150, 0, -53670, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jump("loc_B4B")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_777")
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2E, 0x80)
    Jump("loc_B4B")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_B4B")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    Jump("loc_B4B")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_836")
    SetChrPos(0xE, 29100, 0, -20520, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2D, 0x80)
    Jump("loc_B4B")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_85D")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Jump("loc_B4B")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_884")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8ED")
    SetChrPos(0x30, -4130, 0, -55400, 180)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_925")
    SetChrPos(0x30, 4830, 0, 54990, 0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_962")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, 7320, 0, 4420, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_B4B")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9CB")
    SetChrPos(0x9, -4330, 0, -55480, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 102380, 0, -2210, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, -4630, 0, 53520, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B4B")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A1E")
    SetChrPos(0x9, -4330, 0, -55480, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -4630, 0, 53520, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B4B")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_A8C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -4010, 0, -53520, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 102380, 0, -2210, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, 29230, 0, -21560, 225)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_B4B")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_AD7")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_AD2")
    SetChrPos(0xA, 109200, 0, -8240, 180)

    label("loc_AD2")

    Jump("loc_B4B")

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_B3D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 110710, 0, -4320, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_B38")
    SetChrPos(0x30, -4700, 0, 53690, 180)
    ClearChrFlags(0x30, 0x80)

    label("loc_B38")

    Jump("loc_B4B")

    label("loc_B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B4B")
    SetChrFlags(0xB, 0x80)

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5E")
    ClearChrFlags(0x2F, 0x80)

    label("loc_B5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7D")
    Event(0, 10)
    Jump("loc_B97")

    label("loc_B7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B97")
    Event(0, 13)

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BAB")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_BCE")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BBF")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_BCE")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_BCE")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 9)

    label("loc_BCE")

    Return()

    # Function_1_6C0 end

    def Function_2_BCF(): pass

    label("Function_2_BCF")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_BCF end

    def Function_3_BD6(): pass

    label("Function_3_BD6")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DC1")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_E1D")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E79")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_EC8")
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_F17")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F66")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FA8")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FEA")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_102C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_106E")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_106E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10B0")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10F2")
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_114E")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_119D")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_11EC")
    SetMapObjFrame(0xFF, "BED08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x1, 0x1)
    Jump("loc_11F5")

    label("loc_11EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_11F5")

    label("loc_11F5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1207")
    Jump("loc_1214")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1214")
    OP_66(0x1, 0x1)

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1222")
    Jump("loc_124A")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1234")
    OP_65(0x0, 0x1)
    Jump("loc_124A")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_124A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_124A")
    OP_65(0x0, 0x1)

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1266")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1299")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1282")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_1299")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1299")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_1299")

    Return()

    # Function_3_BD6 end

    def Function_4_129A(): pass

    label("Function_4_129A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(4640, 1000, 2930, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 2750, 0, 2430, 90)
    SetChrPos(0x102, 2800, 0, 3550, 90)
    SetChrPos(0x103, 1240, 0, 2380, 90)
    SetChrPos(0x104, 1190, 0, 3580, 90)
    SetChrPos(0x136, 4680, 0, 2930, 90)
    FadeToBright(1000, 0)
    OP_68(10640, 1000, 2930, 5000)

    def lambda_1348():
        OP_95(0xFE, 11750, 0, 2430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1348)

    def lambda_1362():
        OP_95(0xFE, 11800, 0, 3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1362)

    def lambda_137C():
        OP_95(0xFE, 10240, 0, 2380, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_137C)

    def lambda_1396():
        OP_95(0xFE, 10190, 0, 3580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1396)

    def lambda_13B0():
        OP_95(0xFE, 13680, 0, 2930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_13B0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x136, 1)
    OP_6F(0x1)
    Call(0, 7)
    Return()

    # Function_4_129A end

    def Function_5_13EA(): pass

    label("Function_5_13EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(36760, 1000, -18000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 39350, 100, -18000, 270)
    SetChrPos(0x102, 39350, 100, -18000, 270)
    SetChrPos(0x103, 39350, 100, -18000, 270)
    SetChrPos(0x104, 39350, 100, -18000, 270)
    SetChrPos(0x136, 39350, 100, -18000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    BeginChrThread(0x136, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 6)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x136, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_0D()
    Call(0, 7)
    Return()

    # Function_5_13EA end

    def Function_6_151A(): pass

    label("Function_6_151A")


    def lambda_151F():
        OP_95(0xFE, 27690, 0, -18220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_151F)

    def lambda_1539():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1539)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_151A end

    def Function_7_154E(): pass

    label("Function_7_154E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(27000, 1300, -23530, 0)
    MoveCamera(49, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, 26200, 0, -20300, 180)
    SetChrPos(0x102, 27700, 0, -20300, 180)
    SetChrPos(0x103, 26200, 0, -18900, 180)
    SetChrPos(0x104, 27700, 0, -18900, 180)
    SetChrPos(0x136, 27000, 0, -22000, 180)
    OP_68(27000, 1300, -25030, 2000)

    def lambda_15F3():
        OP_95(0xFE, 27000, 0, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_15F3)

    def lambda_160D():
        OP_95(0xFE, 26200, 0, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_160D)
    Sleep(50)

    def lambda_162A():
        OP_95(0xFE, 27700, 0, -24300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_162A)
    Sleep(50)

    def lambda_1647():
        OP_95(0xFE, 26200, 0, -22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1647)
    Sleep(50)

    def lambda_1664():
        OP_95(0xFE, 27700, 0, -22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1664)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)

    def lambda_169B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_169B)
    WaitChrThread(0x136, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x136,
        (
            "#1101185V#1300F#12PThis should be the room.\x02\x03",
            "#1101186VThere are other patients here,\x01",
            "so try to keep it down, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101187V#0000F#5PWon't be a problem. We're just\x01",
            "here to listen to his account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#1101188V#1309F#12PShall we, then?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3410, 1000, -55120, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26050, 0)
    OP_4B(0x30, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x30, 0x80)
    SetChrPos(0x30, -4130, 0, -55510, 180)
    SetChrPos(0x136, 0, 0, -49400, 180)
    SetChrPos(0x101, -600, 0, -48200, 180)
    SetChrPos(0x102, 600, 0, -48200, 180)
    SetChrPos(0x103, -600, 0, -47000, 180)
    SetChrPos(0x104, 600, 0, -47000, 180)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101189V#2404F#5PHmm... Things seem to be progressing well.\x02\x03",
            "#1101190V#2400FIn fact, if things continue like this, I may\x01",
            "even be able to discharge you as soon\x01",
            "as tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101191V#4PS-Seriously?! You aren't pulling my leg?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101192V#2400F#5PI'm no liar.\x02\x03",
            "#1101193V#2409FHehe. Once you get out of here,\x01",
            "prepare yourself.\x02\x03",
            "#1101194VI have a hundred torims' worth of work\x01",
            "stacked on my desk, waiting for you\x01",
            "to tackle it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101195V#4PDoctor Guenter, c'mon!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101196V#4PWay to kick a man while he's down...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101197V#2403F#5PLacerations, bruises, and a sprain...\x01",
            "Hardly anything major. Be a man.\x02\x03",
            "#1101198V#2400FBesides, you've been resting quite a lot.\x01",
            "You must have a surplus of energy, if anything.\x02\x03",
            "#1101199V#2409FYes, oh, yes. I'd say you should be able to work\x01",
            "ten times harder than before.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101200V#4PDoctor, are you a sadist?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101201V#2403F#5PHmm, always considered myself a\x01",
            "masochist, to be quite honest.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    Sleep(300)

    NpcTalk(
        0x136,
        "Cecile's Voice",
        (
            "#1101202V#4PGood grief... What in Aidios' name are\x01",
            "you talking about, Doctor?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1940, 1000, -54350, 3000)

    def lambda_1D73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_1D73)
    WaitChrThread(0x30, 1)

    def lambda_1D84():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1D84)

    def lambda_1D99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_1D99)
    Sleep(200)

    def lambda_1DAD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAD)

    def lambda_1DC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DC2)
    Sleep(100)

    def lambda_1DD6():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DD6)

    def lambda_1DEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DEB)
    Sleep(150)

    def lambda_1DFF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DFF)

    def lambda_1E14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E14)
    Sleep(150)

    def lambda_1E28():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E28)

    def lambda_1E3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E3D)
    WaitChrThread(0x136, 1)

    def lambda_1E52():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1E52)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1E67():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E67)

    def lambda_1E74():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E74)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_1E89():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E89)

    def lambda_1E96():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E96)
    WaitChrThread(0x136, 1)

    def lambda_1EA7():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1EA7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(100)

    def lambda_1EC7():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EC7)
    Sleep(100)

    def lambda_1EDF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EDF)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(80)

    def lambda_1EFF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EFF)
    Sleep(80)

    def lambda_1F17():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F17)
    WaitChrThread(0x136, 1)

    def lambda_1F30():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1F30)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x136, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)

    NpcTalk(
        0x30,
        "Doctor",
        "#1101203V#2405F#6POh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101204V#6PAh, Miss Neues!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101205V#1306F#11PGeez, you two. You're going to talk about\x01",
            "those sorts of things HERE of all places?\x02\x03",
            "#1101206V#1301FWhat if a child heard you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Intern",
        "#1101207V#6PS-Sorry about that...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        "#1101208V#2406F#6PHaha. You've caught me red-handed.\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x30,
        "Doctor",
        "#1101209V#2405F#6POh, do we have visitors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101210V#1300F#11PThey're officers from the CPD.\x02\x03",
            "#1101211VThey wanted to speak to Mr. Lytton directly\x01",
            "about that incident, actually.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1101212V#6PO-Oh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101213V#2410F#6PThat would make sense, now, wouldn't it?\x02\x03",
            "#1101214V#2400FI suppose you don't need me here for that,\x01",
            "so I'll be on my way.\x02\x03",
            "#1101215VI can make my rounds and all that fun stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101216V#1302F#11PThank you, Doctor Guenter.\x02\x03",
            "#1101217V#1300FAnd don't even think about\x01",
            "sneaking out to go fishing.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x30,
        "Doctor",
        (
            "#1101218V#2405F#6P*gulp* Oh, I would never.\x02\x03",
            "#1101219V#2404FExcuse me, then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_238C():

        label("loc_238C")

        TurnDirection(0x101, 0x30, 500)
        Yield()
        Jump("loc_238C")

    QueueWorkItem2(0x101, 1, lambda_238C)

    def lambda_239E():

        label("loc_239E")

        TurnDirection(0x102, 0x30, 500)
        Yield()
        Jump("loc_239E")

    QueueWorkItem2(0x102, 1, lambda_239E)

    def lambda_23B0():

        label("loc_23B0")

        TurnDirection(0x103, 0x30, 500)
        Yield()
        Jump("loc_23B0")

    QueueWorkItem2(0x103, 1, lambda_23B0)

    def lambda_23C2():

        label("loc_23C2")

        TurnDirection(0x104, 0x30, 500)
        Yield()
        Jump("loc_23C2")

    QueueWorkItem2(0x104, 1, lambda_23C2)

    def lambda_23D4():

        label("loc_23D4")

        TurnDirection(0x136, 0x30, 500)
        Yield()
        Jump("loc_23D4")

    QueueWorkItem2(0x136, 1, lambda_23D4)

    def lambda_23E6():
        OP_96(0xFE, 0xFFFFF8DA, 0x0, 0xFFFF220C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_23E6)
    BeginChrThread(0x30, 3, 0, 8)
    WaitChrThread(0x30, 3)
    WaitChrThread(0x136, 2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x136, 0x1)
    SetChrFlags(0x30, 0x80)

    def lambda_2427():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2427)

    def lambda_2434():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2434)

    def lambda_2441():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2441)

    def lambda_244E():
        TurnDirection(0xFE, 0x136, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_244E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1101220V#0005F#5PUm, who was that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x136, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x136,
        (
            "#1101221V#1300F#12PThat was Doctor Guenter, one of our\x01",
            "associate professors.\x02\x03",
            "#1101222V#1306FThough he's an excellent doctor, his\x01",
            "priorities are rather...questionable.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(-2550, 1000, -54720, 3000)

    def lambda_2578():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2578)

    def lambda_2585():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2585)
    Sleep(100)

    def lambda_2595():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2595)

    def lambda_25A2():
        OP_93(0xFE, 0xD7, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25A2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_25BF():
        OP_95(0xFE, -3180, 0, -55730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_25BF)
    WaitChrThread(0x136, 1)

    def lambda_25DD():
        OP_95(0xFE, -4030, 0, -55490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_25DD)
    WaitChrThread(0x136, 1)

    def lambda_25FB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_25FB)
    WaitChrThread(0x136, 1)

    def lambda_260C():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_260C)
    Sleep(50)

    def lambda_2624():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2624)
    Sleep(100)

    def lambda_263C():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_263C)
    Sleep(80)

    def lambda_2654():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2654)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x136,
        (
            "#1101223V#1300F#5PNow, then, Lytton. Do you have time\x01",
            "to answer some of their questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101224V#6PS-Sure, I don't mind, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101225V#6P...didn't the CGF already conduct\x01",
            "an investigation of this mess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101226V#6PWhy are the CPD doing one now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101227V#0003F#5PWell, sadly, the CGF hit a dead end.\x02\x03",
            "#1101228V#0001FBecause of that, the SSS was asked\x01",
            "to perform an investigation of its own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101229V#6PGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101230V#6PHuh. Did they think I was dreaming\x01",
            "or something...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101231V#6PSleepwalking, maybe? No, I know\x01",
            "that's not what happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101232V#0103F#11PExcuse me, Lytton. If possible, could we\x01",
            "hear your story from the very beginning?\x02\x03",
            "#1101233V#0101FWhat exactly happened on that night\x01",
            "one week ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101234V#6PY-Yeah, no problem.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#1101235V#11PIt was late. I had been writing a research\x01",
            "paper all day and night.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_154E end

    def Function_8_2A38(): pass

    label("Function_8_2A38")


    def lambda_2A3D():
        OP_95(0xFE, 10, 0, -55640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A3D)
    WaitChrThread(0xFE, 1)

    def lambda_2A5B():
        OP_95(0xFE, 10, 0, -51540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A5B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_2A9B():
        OP_95(0xFE, 30, 0, -48960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A9B)
    Sleep(500)

    def lambda_2AB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AB8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    Return()

    # Function_8_2A38 end

    def Function_9_2AEB(): pass

    label("Function_9_2AEB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(0, 16777215, -1)
    OP_68(-3120, 2000, -54300, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26050, 0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x101, -3700, 0, -55250, 180)
    SetChrPos(0x102, -4600, 0, -55250, 180)
    SetChrPos(0x103, -3700, 0, -54150, 180)
    SetChrPos(0x104, -4600, 0, -54150, 180)
    SetChrPos(0x136, -2500, 0, -55250, 225)
    FadeToBright(0, -1)
    FadeToBright(1000, 16777215)
    OP_68(-3120, 500, -54300, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x8,
        "#1101240V#4P...And that's all I can remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101241V#4PThe next morning, the janitor found me\x01",
            "beaten to a bloody pulp on the roof...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101242V#4PAfter that, I was taken to one of the\x01",
            "hospital rooms and treated for my\x01",
            "wounds, which brings us here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#1101243V#0003F#5PThank you. I think I have a general\x01",
            "understanding of what happened now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101244V#0301F#5PYou get a good look at your attacker?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101245V#4PNot as good as I'd like. I'm embarrassed\x01",
            "to admit it, but I passed out due to shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101246V#4PWhat I can remember are blood-red eyes,\x01",
            "white fangs, and a coat of blackish fur\x01",
            "that keep replaying in my head...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101247V#4PWhich makes sense, because the CGF\x01",
            "confirmed that they were canines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101248V#0203F#5PThat lines up, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101249V#0101F#5PWhere exactly were you wounded?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101250V#4POh, right shoulder. The doctors told me that\x01",
            "the cuts came from fangs, no doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101251V#4PMy other injuries came from a blow to\x01",
            "the head and a sprained ankle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101252V#4PThey told me that the most likely scenario\x01",
            "was that I was dragged to the floor after\x01",
            "being chomped on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101253V#0003F#5PYou're wondering why the monsters\x01",
            "stopped there.\x02\x03",
            "#1101254V#0001FAm I right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101255V#4PYes, exactly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101256V#4PIsn't it strange that my head WASN'T\x01",
            "bitten off...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101257V#4POn top of that, it happened on the roof!\x01",
            "I swear, the CGF people thought I was\x01",
            "off my rocker when I told them that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101258V#4PThe only conclusion they could come to\x01",
            "was that I somehow staggered onto the\x01",
            "highway and was ambushed by monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101259V#0200F#5PBut you were discovered unconscious on\x01",
            "the hospital roof, were you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101260V#4PHmm, that's true. Maybe I panicked, ran\x01",
            "up to the roof, and then passed out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101261V#4PIt's not impossible, I guess.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#1101262V#0006F#5PYeah, I'm not too confident about that\x01",
            "theory, Lytton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101263V#1306F#11PTake a breath, Lytton.\x02\x03",
            "#1101264V#1301FYou're the victim here. How will they get\x01",
            "to the bottom of this if you don't have any\x01",
            "confidence in your own statement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101265V#4PI-I'm sorry... I just don't know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101266V#4PStill, is it really that big a deal if I don't\x01",
            "have a good explanation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101267V#4PIt's definitely easier on me, that's for sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101268V#4PI mean, if monsters legitimately appeared on\x01",
            "the roof...wouldn't that be a bit too freaky to\x01",
            "believe?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x136,
        (
            "#1101269V#1306F#11P*sigh* I know how you feel. I really do. But\x01",
            "think about it like this, Lytton.\x02\x03",
            "#1101270V#1301FIf you actually were attacked on the roof,\x01",
            "we need to make sure it doesn't happen\x01",
            "to anyone else ever again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101271V#0003F#5P...\x02\x03",
            "#1101272V#0000FWell, thanks for your help, Lytton.\x02\x03",
            "#1101273VFor now, we'll focus on investigating\x01",
            "the scene of the crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1101274V#4PUh, yeah. We're counting on you guys, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1101275V#4PIf you're able to figure out what happened,\x01",
            "we'll be able to keep it from happening again.\x01",
            "So, good luck.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x7D0)
    SetChrPos(0x0, -2910, 0, -54690, 90)
    SetScenarioFlags(0x62, 1)
    OP_29(0x3F, 0x1, 0xA)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0x8, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    EventEnd(0x5)
    Return()

    # Function_9_2AEB end

    def Function_10_38D3(): pass

    label("Function_10_38D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(26720, 1000, -24500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 26940, 0, -23600, 180)
    SetChrPos(0x102, 27970, 0, -24220, 270)
    SetChrPos(0x103, 28250, 0, -25380, 270)
    SetChrPos(0x104, 26030, 0, -25470, 0)
    SetChrPos(0x136, 25110, 0, -23850, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 7)), scpexpr(EXPR_END)), "loc_39A8")

    ChrTalk(
        0x104,
        "#1101276V#12P#0300FTo the roof, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_39F2")

    label("loc_39A8")


    ChrTalk(
        0x104,
        (
            "#1101277V#12P#0300FSo, we gotta head up to the\x01",
            "roof from here, yeah?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F2")


    ChrTalk(
        0x101,
        (
            "#1101278V#5P#0001FThat's right. Let's start off with trying to\x01",
            "pinpoint exactly where he was attacked.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101279V#0005F#11PCecile, do you still have some free time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1101280V#6P#1306FHmm, my break is probably going to\x01",
            "end relatively soon...\x02\x03",
            "#1101281V#1300FBut I can at least show you where\x01",
            "we found him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101282V#0000F#11PThat'd be great. Thanks.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 27000, 0, -26000, 0)
    SetScenarioFlags(0x62, 2)
    EventEnd(0x5)
    Return()

    # Function_10_38D3 end

    def Function_11_3B86(): pass

    label("Function_11_3B86")

    EventBegin(0x0)
    Fade(1000)
    OP_68(23570, 1000, -500, 0)
    MoveCamera(68, 15, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(26180, 0)
    SetChrPos(0x101, 22560, 0, -1490, 45)
    SetChrPos(0x102, 21620, 0, -3050, 45)
    SetChrPos(0x103, 21010, 0, -2400, 45)
    SetChrPos(0x104, 22860, 0, -3470, 45)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 24600, 0, 300, 225)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, 30540, 0, 20, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_3CB0")

    ChrTalk(
        0xA,
        "#1101357V#5PThanks for your hard work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101356V#5PHow's the investigation coming along?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D3E")

    label("loc_3CB0")


    ChrTalk(
        0xA,
        "#1101355V#5PKeep up the good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101358V#5PYou're those police officers, right? How's\x01",
            "the investigation coming along?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D3E")


    ChrTalk(
        0x101,
        (
            "#1101419V#0004F#6PWe're just about finished, actually.\x02\x03",
            "#1101360V#0000FAlso, I was hoping I could let Cecile know\x01",
            "what we found. Miss Neues, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101361V#5POh, is that right...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xA,
        "#1101362V#5PHeehee... It's just like Cecile said.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101363V#0005F#6PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101364V#5PI've heard loads of stories about you,\x01",
            "Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101365V#5PCecile hasn't been able to stop talking\x01",
            "about you since your dramatic return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101366V#5PAnd now I understand why. You're SO\x01",
            "cute!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1101367V#0011F#6PM-Me...? Cute?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101368V#0211F#6P(Quit ogling her.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101369V#0103F#12P(Can you save it for when we're\x01",
            "off duty, Lloyd?)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#1101370V#0013F#5P(Are you kidding me?! Whatever you\x01",
            "THINK I'm doing, I'm not!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4081():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4081)
    WaitChrThread(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1101371V#0304F#12P(Chillax, Lloyd.)\x02\x03",
            "#1101372V#0302F(Leave it to the master.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101373V#0005F#5P(What are you...?)\x02",
    )

    CloseMessageWindow()
    OP_68(23600, 1000, -700, 1000)

    def lambda_4124():
        OP_95(0xFE, 22880, 0, -1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4124)

    def lambda_413E():
        OP_96(0xFE, 0x5168, 0x0, 0xFFFFFA6A, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_413E)

    def lambda_4158():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4158)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1101374V#0309F#2PHaha. You know, babe, I think you're\x01",
            "the cute one here, not him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#1101375V#5PHuh? Me?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_END)), "loc_4268")

    ChrTalk(
        0x104,
        (
            "#1101376V#0304F#2PWell, sure, Lloyd has charm. But if\x01",
            "anyone here is cute, it'd be you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4371")

    label("loc_4268")


    ChrTalk(
        0x104,
        (
            "#1101377V#0302F#2PSorry 'bout that, I tend to get carried\x01",
            "away. The name's Randy.\x02\x03",
            "#1101378VAnd you are...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101379V#5PUmmm, Philia. I'm Philia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101380V#5PDo you work with Lloyd, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101381V#0304F#2PSure do. I'm a certified boy in blue.\x02",
    )

    CloseMessageWindow()

    label("loc_4371")

    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1101382V#0302F#2PTo celebrate our meeting, how 'bout you\x01",
            "come party with me this weekend?\x02\x03",
            "#1101383VThis guy'll be comin', of course, and you're\x01",
            "free to bring some girlfriends, too. C'mon,\x01",
            "doesn't that sound like a good time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4461():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4461)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#1101384V#0001F#6PW-Wait a second here, Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101385V#5PHmm, it's definitely tempting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101386V#5PI like to take a breather every so often,\x01",
            "so I'll try to invite some friends. Surely\x01",
            "some of them are free this weekend.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4562():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4562)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x104,
        (
            "#1101387V#0309F#2PHell yeah. Call 'em all up.\x02\x03",
            "#1101388V#0300FYou cool with Garante? That's my\x01",
            "go-to bar.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1101389V#0200F#6P(He has quite the silver tongue.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101390V#0106F#12P(I suppose his self-proclamation of being\x01",
            "a ladies' man wasn't all talk, after all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101391V#0006F#6P(I have no idea how things got to this point...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101392V#0309F#2PYou're too kind, lil' lady.\x02\x03",
            "#1101393VHavin' a few drinks with an angel like\x01",
            "yourself is more than I could ask for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101394V#5PAn angel, huh? I'm afraid I'm just\x01",
            "a regular nurse, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101395V#5PAre you okay with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101396V#0304F#2PNo problemo.\x02\x03",
            "#1101397V#0302FBesides, you rock that uniform. Hell,\x01",
            "every lady here ain't too bad if I'm\x01",
            "bein' honest with myself.\x02\x03",
            "#1101398V#0309FBut you, babe. You drive me crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101399V#5PO-Oh, Randy! *blush*\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    NpcTalk(
        0xB,
        "Old Lady's Voice",
        (
            "#1101400V'Ain't too bad,' hmm? Goodness me,\x01",
            "I think I'm going red in the face.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_49C6():
        OP_95(0xFE, 24940, 0, -190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_49C6)

    def lambda_49E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_49E0)

    def lambda_49F1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_49F1)
    WaitChrThread(0xA, 1)
    Sleep(500)

    def lambda_4A05():
        OP_96(0xFE, 0x5E10, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4A05)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xA, 2)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    ChrTalk(
        0x104,
        "#1101401V#0305F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101402V#5PAhaha... Hello there, Martha.\x02",
    )

    CloseMessageWindow()

    def lambda_4A91():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4A91)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xB,
        "#1101403V#2PDon't act all innocent, missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101404V#2PDid you remember to take temperatures\x01",
            "this afternoon? That was YOUR job, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#1101405V#5PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101406V#2POh, and this weekend? Did you somehow forget\x01",
            "that we're overseeing an INCREDIBLY complex\x01",
            "surgery?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101407V#5PWhoopsie-daisy. Ahaha...\x02",
    )

    CloseMessageWindow()

    def lambda_4C02():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4C02)
    WaitChrThread(0xA, 1)

    ChrTalk(
        0xA,
        (
            "#1101408V#5PI'm really sorry, Randy. Looks like we're\x01",
            "going to have to reschedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1101409V#5PSee you later, everyone!\x02",
    )

    CloseMessageWindow()

    def lambda_4C95():

        label("loc_4C95")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_4C95")

    QueueWorkItem2(0x104, 1, lambda_4C95)

    def lambda_4CA7():

        label("loc_4CA7")

        TurnDirection(0xB, 0xA, 500)
        Yield()
        Jump("loc_4CA7")

    QueueWorkItem2(0xB, 1, lambda_4CA7)

    def lambda_4CB9():
        OP_95(0xFE, 26210, 0, 1130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4CB9)
    WaitChrThread(0xA, 1)

    def lambda_4CD7():
        OP_95(0xFE, 28770, 0, -20, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4CD7)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_4D10():
        OP_95(0xFE, 31000, 0, 10, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4D10)
    Sleep(150)

    def lambda_4D2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4D2D)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xB, 0x1)

    ChrTalk(
        0x104,
        "#1101410V#0305F#2P...\x02",
    )

    CloseMessageWindow()

    def lambda_4D8E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4D8E)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xB,
        (
            "#1101411V#5PPerhaps you'd like to spend the weekend\x01",
            "with me instead? Hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101412V#5PSadly, I'm not the 'angel' you're looking\x01",
            "for, am I? Hmph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101413V#0309F#2PN-No, that's not true. Take a look in the\x01",
            "mirror. You're...beautiful. Haha...\x02\x03",
            "#1101414V#0306F(Tag in, Lloyd. You're up.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    def lambda_4ED2():
        OP_96(0xFE, 0x594C, 0x0, 0xFFFFF272, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4ED2)

    def lambda_4EEC():
        OP_93(0xFE, 0x2D, 0x64)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4EEC)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#1101415V#0001F#5P*sigh* Randy, zero percent of that was productive.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    OP_68(23820, 1000, -720, 1000)

    def lambda_4F63():
        OP_96(0xFE, 0x5492, 0x0, 0xFFFFFB14, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F63)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1101416V#0006F#6PI'm terribly sorry about him, ma'am.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_4FC7():
        OP_93(0xFE, 0x104, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4FC7)
    WaitChrThread(0xB, 1)
    Sleep(300)

    ChrTalk(
        0xB,
        "#1101417V#5PWell, what's done is done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101418V#5PSo, has your investigation yielded any\x01",
            "fruit? Must be, if you're here for Cecile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101359V#0000F#6PYes, ma'am. We just finished, actually.\x02\x03",
            "#1101420VWe found a few leads, so we wanted\x01",
            "to give her a rundown of everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101421V#5PI see. Around this time, Cecile should\x01",
            "be checking in on that girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101422V#5PHmm, and it would take a bit to make\x01",
            "an announcement on the intercom...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xB,
        "#1101423V#5PListen up, you four.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101424V#5PCecile should be in the farthest room on\x01",
            "the third floor right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101425V#5PWould you be against checking for me?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101426V#0005F#6PYou want us to just head up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101427V#0105F#12PAre you sure it's okay to interrupt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101428V#5POf course. The young child she's looking after is\x01",
            "hospitalized here under special circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101429V#5PIf possible, I'd like for you to say hello\x01",
            "to her as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101430V#0000F#6PI don't think that should be a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101431V#0300F#12PSo you want us to keep the kiddo\x01",
            "company for a lil' bit, that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101432V#5PWell, something like that. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101433V#5PIf you'll excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101434V#0200F#6P...\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_550D():
        OP_95(0xFE, 28870, 0, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_550D)
    WaitChrThread(0xB, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_5546():
        OP_95(0xFE, 30850, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5546)
    Sleep(200)

    def lambda_5563():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5563)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetChrPos(0xB, 108930, 0, 1450, 45)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 109200, 0, -8240, 180)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, 22400, 0, -1750, 45)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x63, 4)
    OP_29(0x3F, 0x1, 0x13)
    EventEnd(0x5)
    Return()

    # Function_11_3B86 end

    def Function_12_55E7(): pass

    label("Function_12_55E7")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    Fade(1000)
    OP_68(107900, 1000, 1500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0xB, 108930, 0, 1450, 270)
    SetChrPos(0x101, 107230, 0, 850, 90)
    SetChrPos(0x102, 107230, 0, 2180, 90)
    SetChrPos(0x103, 105980, 0, 850, 90)
    SetChrPos(0x104, 105980, 0, 2180, 90)
    OP_0D()

    ChrTalk(
        0xB,
        "#1101435V#11PYou guys again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101436V#11PI told you, you can find Cecile in the\x01",
            "farthest room on the third floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#1101437V#11PWait a minute... Are you...?\x02",
    )

    CloseMessageWindow()
    OP_68(106400, 1000, 1500, 3000)

    def lambda_574D():

        label("loc_574D")

        TurnDirection(0x101, 0xB, 500)
        Yield()
        Jump("loc_574D")

    QueueWorkItem2(0x101, 2, lambda_574D)

    def lambda_575F():

        label("loc_575F")

        TurnDirection(0x102, 0xB, 500)
        Yield()
        Jump("loc_575F")

    QueueWorkItem2(0x102, 2, lambda_575F)

    def lambda_5771():

        label("loc_5771")

        TurnDirection(0x104, 0xB, 500)
        Yield()
        Jump("loc_5771")

    QueueWorkItem2(0x104, 2, lambda_5771)

    def lambda_5783():
        OP_96(0xFE, 0x19DFC, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5783)
    Sleep(500)

    def lambda_57A0():
        OP_96(0xFE, 0x1A2DE, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57A0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_57CF():
        OP_96(0xFE, 0x19884, 0x0, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57CF)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_64(0x103)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#1101438V#0005F#11PMiss Martha? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101439V#0208F#6P#40WAre you looking...at me?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#1101440V#11POh, I knew it! It IS you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101441V#11PTio, right? You must be!\x02",
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
        0x101,
        "#1101442V#0011F#11PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101443V#0105F#5PYou know Tio...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101444V#0208F#6P#40W...\x02\x03",
            "#1101445V#0206F#40WI apologize for not staying in touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101446V#11PHaha, I thought it was you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101447V#11POh, my, look how you've grown!\x01",
            "Such a beautiful young lady!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101448V#11PI hardly recognized you!\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    OP_93(0xB, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#1101449V#5PHold on, why are you with these\x01",
            "police officers...?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)

    ChrTalk(
        0xB,
        "#1101450V#11PHmmm? Tell me everything, dear.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)

    ChrTalk(
        0x103,
        (
            "#1101451V#0208F#6P#40WUm...it's complicated.\x02\x03",
            "#1101452V#0203F#40WI intended to visit you earlier, but...\x02\x03",
            "#1101453V#0202F#40W...unfortunately, police work has kept\x01",
            "us quite busy today, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1101454V#11PI-I understand. It's fine, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101455V#11PNext time, I'll brew us some tea and\x01",
            "we can catch up, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 104070, 0, 940, 270)
    SetChrPos(0xB, 108930, 0, 1450, 45)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x63, 5)
    ClearScenarioFlags(0x0, 4)
    EventEnd(0x5)
    Return()

    # Function_12_55E7 end

    def Function_13_5C93(): pass

    label("Function_13_5C93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50104.itc", 0x1E)
    OP_68(27690, 1000, -9660, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 26000, 0, -6300, 180)
    SetChrPos(0x102, 27600, 0, -6000, 180)
    SetChrPos(0x103, 26800, 0, -8400, 180)
    SetChrPos(0x104, 26800, 0, -5000, 180)
    FadeToBright(1000, 0)
    SetCameraDistance(24000, 3000)

    def lambda_5D2E():
        OP_95(0xFE, 26000, 0, -8800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D2E)

    def lambda_5D48():
        OP_95(0xFE, 27600, 0, -8500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D48)

    def lambda_5D62():
        OP_95(0xFE, 26800, 0, -10400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D62)

    def lambda_5D7C():
        OP_95(0xFE, 26800, 0, -7500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D7C)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    ChrTalk(
        0x103,
        "#1101456V#0208F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101457V#0001F#5PTio, have you been here before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101458V#0208F#5P...Yes.\x02\x03",
            "#1101459VSix years ago, to be exact.\x02\x03",
            "#1101460V#0206FI did not intend to keep it a secret\x01",
            "from all of you. I apologize...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101461V#0303F#5PSecret, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101462V#0006F#5PThere's no need to apologize, Tio.\x02\x03",
            "#1101463V#0000FWe all have things that are hard to say\x01",
            "out loud. Heck, you'd be hard-pressed\x01",
            "to find someone who doesn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101464V#0208F#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(27590, 1000, -9860, 1000)
    SetCameraDistance(23500, 1000)
    OP_95(0x102, 26970, 0, -9830, 2000, 0x0)
    Fade(500)

    def lambda_5FCF():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5FCF)
    SetCameraDistance(22330, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#1101465V#0104F#5PIt's okay, Tio. Everything's okay...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1101466V#0205F#5PE-Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101467V#0102F#5PThere's no need to make that face, you know.\x02\x03",
            "#1101468VKeep that up and people might forget how\x01",
            "cute you really are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101469V#0205F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101470V#0304F#5PHey, each of us has led different lives\x01",
            "and experienced a hell of a lotta things.\x02\x03",
            "#1101471V#0300FOn top of that, we've only known each\x01",
            "other for a month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101472V#0004F#5POur age, genders, and even our\x01",
            "interests are all different.\x02\x03",
            "#1101473VAnd despite all that, we're still able to\x01",
            "come together and work as a team.\x02\x03",
            "#1101474V#0000FIsn't that enough for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101475V#0208F#5PLloyd, Randy...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#1101476V#0204F#5PYou may be right.\x02\x03",
            "#1101477V#0202FI'm afraid I was a bit nervous about\x01",
            "disclosing my past, that's all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x4)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    OP_93(0x103, 0xB4, 0x0)
    SetChrPos(0x102, 27070, 0, -9460, 180)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_93(0x103, 0x0, 0x12C)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1101478V#0204F#12PWell, it wasn't my intention to waste\x01",
            "valuable time. Should we find Cecile?\x02\x03",
            "#1101479V#0202FWe still need to give her our report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101480V#0000F#5PRight. Let's head to the third floor.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22580, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 26590, 0, -12170, 180)
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x63, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_5C93 end

    SaveToFile()

Try(main)
