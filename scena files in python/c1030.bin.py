from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1030.bin",                # FileName
        "c1030",                    # MapName
        "c1030",                    # Location
        0x0012,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 18, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1030",                  # 0
        "Zhang Hui",              # 1
        "Finn",                   # 2
        "Shanshan",               # 3
        "Gryd",                   # 4
        "Puck",                   # 5
        "Puck",                   # 6
        "Roose",                  # 7
        "Roose",                  # 8
        "Purple-Haired Girl",     # 9
        "Chief Sergei",           # 10
        "Grace",                  # 11
        "Reins",                  # 12
        "Felicia",                # 13
        "Letina",                 # 14
        "Anton",                  # 15
        "Ricky",                  # 16
        "Wald",                   # 17
        "Luganov",                # 18
        "Lars",                   # 19
        "Kurt",                   # 20
        "イス",                   # 21
        "イス",                   # 22
        "Tableware",              # 23
        "Tableware",              # 24
        "Tableware",              # 25
        "Tableware",              # 26
        "Tableware",              # 27
        "Tableware",              # 28
        "Tableware",              # 29
        "Tableware",              # 30
        "Tableware",              # 31
        "Tableware",              # 32
        "Tableware",              # 33
        "SE制御",                 # 34
    ))

    AddCharChip((
        "chr/ch31600.itc",                   # 00
        "chr/ch25100.itc",                   # 01
        "chr/ch32500.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch05202.itc",                   # 06
        "chr/ch20402.itc",                   # 07
        "chr/ch21202.itc",                   # 08
        "chr/ch06002.itc",                   # 09
        "chr/ch28102.itc",                   # 0A
        "chr/ch02502.itc",                   # 0B
        "chr/ch33300.itc",                   # 0C
        "chr/ch34500.itc",                   # 0D
        "chr/ch33302.itc",                   # 0E
        "chr/ch37300.itc",                   # 0F
        "chr/ch37400.itc",                   # 10
        "apl/ch50018.itc",                   # 11
        "chr/ch30802.itc",                   # 12
        "chr/ch23400.itc",                   # 13
        "chr/ch21400.itc",                   # 14
        "apl/ch50092.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(16000,   0,       15989,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(16030,   0,       6050,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(12310,   0,       -1990,   225,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(7130,    150,     -1480,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(16030,   0,       6050,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10689,   150,     3170,    270,  341,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(17909,   0,       8399,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(7300,    150,     3230,    90,   341,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(13949,   150,     2900,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(13810,   150,     5909,    90,   469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4900,    100,     7099,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1299,    100,     7099,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-49830,  29,      -54020,  180,  389,  0x0, 0,   12,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-49830,  29,      -55880,  0,    389,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-100000, 19,      -54500,  270,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-103849, 0,       -53459,  180,  389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4849,    0,       7099,    270,  389,  0x0, 0,   17,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(3200,    0,       8899,    180,  389,  0x0, 0,   18,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-50970,  29,      -56450,  180,  389,  0x0, 0,   19,  0,   0,   2,   0,   34,  255,  0)
    DeclNpc(-53849,  0,       -55180,  180,  389,  0x0, 0,   20,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14590,   0,       4630,    1000,    16030,   1500,    6050,    0x007E, 0,  5,  0x0000)

    ScpFunction((
        "Function_0_598",          # 00, 0
        "Function_1_650",          # 01, 1
        "Function_2_7A4",          # 02, 2
        "Function_3_7CC",          # 03, 3
        "Function_4_B3F",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_BC8",          # 06, 6
        "Function_7_CBF",          # 07, 7
        "Function_8_1BDB",         # 08, 8
        "Function_9_1CD2",         # 09, 9
        "Function_10_331B",        # 0A, 10
        "Function_11_4B8E",        # 0B, 11
        "Function_12_5E48",        # 0C, 12
        "Function_13_5F3F",        # 0D, 13
        "Function_14_6103",        # 0E, 14
        "Function_15_6AF6",        # 0F, 15
        "Function_16_6B82",        # 10, 16
        "Function_17_8049",        # 11, 17
        "Function_18_81EE",        # 12, 18
        "Function_19_81F2",        # 13, 19
        "Function_20_86E3",        # 14, 20
        "Function_21_8A0C",        # 15, 21
        "Function_22_8FB3",        # 16, 22
        "Function_23_914D",        # 17, 23
        "Function_24_95CB",        # 18, 24
        "Function_25_9B18",        # 19, 25
        "Function_26_A0F7",        # 1A, 26
        "Function_27_A4AF",        # 1B, 27
        "Function_28_C26E",        # 1C, 28
        "Function_29_C861",        # 1D, 29
        "Function_30_D0DF",        # 1E, 30
        "Function_31_104CB",       # 1F, 31
        "Function_32_110F2",       # 20, 32
        "Function_33_11324",       # 21, 33
        "Function_34_1195D",       # 22, 34
        "Function_35_11F38",       # 23, 35
        "Function_36_12123",       # 24, 36
        "Function_37_12BCB",       # 25, 37
        "Function_38_13505",       # 26, 38
        "Function_39_137B0",       # 27, 39
        "Function_40_1474F",       # 28, 40
        "Function_41_1498B",       # 29, 41
        "Function_42_14BDF",       # 2A, 42
        "Function_43_14C2A",       # 2B, 43
    ))


    def Function_0_598(): pass

    label("Function_0_598")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5D8"),
        (1, "loc_5E4"),
        (2, "loc_5F0"),
        (3, "loc_5FC"),
        (4, "loc_608"),
        (5, "loc_614"),
        (6, "loc_620"),
        (SWITCH_DEFAULT, "loc_62C"),
    )


    label("loc_5D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_5FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_608")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_614")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_620")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_62C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_638")

    label("loc_64F")

    Return()

    # Function_0_598 end

    def Function_1_650(): pass

    label("Function_1_650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A3")
    OP_95(0xFE, 7200, 0, 370, 1000, 0x0)
    OP_95(0xFE, 7280, 30, 1390, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_95(0xFE, 5850, 0, 1930, 1000, 0x0)
    OP_95(0xFE, 4730, 0, 3700, 1000, 0x0)
    OP_95(0xFE, 4840, 0, 5570, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 5660, 0, 5540, 1000, 0x0)
    OP_95(0xFE, 10470, 0, 10350, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1200)
    OP_95(0xFE, 12980, 0, 7230, 1000, 0x0)
    OP_95(0xFE, 12730, 0, 2100, 1000, 0x0)
    OP_95(0xFE, 13200, 0, 1420, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1600)
    OP_95(0xFE, 12280, 0, 680, 1000, 0x0)
    OP_95(0xFE, 11230, 0, 110, 1000, 0x0)
    OP_95(0xFE, 8930, 30, -1570, 1000, 0x0)
    Sleep(1400)
    OP_95(0xFE, 8720, 0, -510, 1000, 0x0)
    Jump("Function_1_650")

    label("loc_7A3")

    Return()

    # Function_1_650 end

    def Function_2_7A4(): pass

    label("Function_2_7A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CB")
    OP_94(0xFE, 0xFFFF3D96, 0xFFFF29BE, 0xFFFF381E, 0xFFFF2126, 0x3E8)
    Jump("Function_2_7A4")

    label("loc_7CB")

    Return()

    # Function_2_7A4 end

    def Function_3_7CC(): pass

    label("Function_3_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7FA")
    SetChrPos(0x9, 11180, 0, 15810, 0)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B14")

    label("loc_7FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_84A")
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, -103790, 0, -55180, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_B14")

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_85D")
    SetChrFlags(0x8, 0x10)
    Jump("loc_B14")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AD")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8A8")
    SetChrPos(0x16, -100320, 30, -56530, 180)
    SetChrPos(0x17, -101160, 30, -55430, 180)
    SetChrFlags(0x17, 0x10)

    label("loc_8A8")

    Jump("loc_B14")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_925")
    SetChrPos(0x8, 16030, 0, 6050, 270)
    SetChrPos(0x9, 12310, 0, -1990, 225)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x80)
    Jump("loc_920")

    label("loc_909")

    SetChrPos(0xA, 13950, 0, 6940, 135)
    BeginChrThread(0xA, 0, 0, 0)

    label("loc_920")

    Jump("loc_B14")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_99E")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x19, 0x1)
    SetChrChipByIndex(0x1E, 0x15)
    SetChrSubChip(0x1E, 0xF)
    SetChrPos(0x1E, 4000, 600, 7100, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x15)
    SetChrSubChip(0x1F, 0xF)
    SetChrPos(0x1F, 3300, 600, 8000, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    Jump("loc_B14")

    label("loc_99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9B6")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_B14")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9C4")
    Jump("loc_B14")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9D2")
    Jump("loc_B14")

    label("loc_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A41")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A1E")
    SetChrPos(0x1A, -49440, 30, -56190, 270)
    SetChrPos(0x1B, -51000, 30, -56190, 90)
    BeginChrThread(0x1A, 0, 0, 0)
    Jump("loc_A3C")

    label("loc_A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A35")
    SetChrFlags(0x1B, 0x10)
    Jump("loc_A3C")

    label("loc_A35")

    OP_93(0x1B, 0x2D, 0x0)

    label("loc_A3C")

    Jump("loc_B14")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A90")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1A, -49800, 20, -53530, 180)
    SetChrPos(0x1B, -50200, 20, -55110, 0)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1B, 0x10)
    BeginChrThread(0x1A, 0, 0, 0)
    Jump("loc_B14")

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AE7")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x40)
    SetChrChipByIndex(0x14, 0xE)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 3230, 150, 9000, 180)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrPos(0x15, 2020, 0, 9600, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_B14")

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_B0B")
    ClearChrFlags(0x14, 0x80)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x15, 0x80)
    BeginChrThread(0x15, 0, 0, 0)
    Jump("loc_B14")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B14")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearChrFlags(0x10, 0x80)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3E")
    ClearChrFlags(0x12, 0x80)

    label("loc_B3E")

    Return()

    # Function_3_7CC end

    def Function_4_B3F(): pass

    label("Function_4_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B50")
    SetScenarioFlags(0x1, 0)
    Jump("loc_B69")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B66")
    SetScenarioFlags(0x0, 6)
    Jump("loc_B69")

    label("loc_B66")

    SetScenarioFlags(0x0, 7)

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B85")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B9C")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B9C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B9C")

    label("loc_B9C")

    Return()

    # Function_4_B3F end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BAE")
    Call(0, 12)
    Jump("loc_BC7")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC4")
    Call(0, 6)
    Jump("loc_BC7")

    label("loc_BC4")

    Call(0, 8)

    label("loc_BC7")

    Return()

    # Function_5_B9D end

    def Function_6_BC8(): pass

    label("Function_6_BC8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CB8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5E")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAE")

    label("loc_C5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7E")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAE")

    label("loc_C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C92")
    Jump("loc_CAE")

    label("loc_C92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_CAE")

    Jump("loc_BDE")

    label("loc_CB3")

    Jump("loc_CBB")

    label("loc_CB8")

    Call(0, 7)

    label("loc_CBB")

    TalkEnd(0x8)
    Return()

    # Function_6_BC8 end

    def Function_7_CBF(): pass

    label("Function_7_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D74")

    ChrTalk(
        0x8,
        (
            "That part-timer keeps bumping into Shanshan\x01",
            "while she's carrying plates whenever I put him\x01",
            "in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "He isn't doing it on purpose, is he?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DEB")

    label("loc_D74")


    ChrTalk(
        0x8,
        "I put the part-timer outside to attract customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no chance in hell I'd let him\x01",
            "in the kitchen now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEB")

    Jump("loc_1BDA")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E2A")

    ChrTalk(
        0x8,
        "Part-timers just need to work swiftly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BDA")

    label("loc_E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7E")

    ChrTalk(
        0x8,
        "*slurp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yup. Soup came out well today.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF2")

    label("loc_E7E")


    ChrTalk(
        0x8,
        (
            "I've been making this soup ever since\x01",
            "I was out in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Don't ask for the recipe. It's a secret.\x02",
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_1BDA")

    label("loc_EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_104F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FEB")

    ChrTalk(
        0x8,
        "I don't run this store to please customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm not really doing it for the money, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "As long as we have a modest amount of both, it's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "We're not exactly a popular establishment, anyway.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104A")

    label("loc_FEB")


    ChrTalk(
        0x8,
        "Running a modest business is fine with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I like it better when it's quiet, anyway.\x02",
    )

    CloseMessageWindow()

    label("loc_104A")

    Jump("loc_1BDA")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10CB")

    ChrTalk(
        0x8,
        (
            "Now that the festival's over, it's finally\x01",
            "quiet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's calm now, so I've opened up\x01",
            "the store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDA")

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1191")

    ChrTalk(
        0x8,
        (
            "I'll turn those delinquents into chopped liver\x01",
            "if they ever touch my Shanshan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Shanshan's my precious daughter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't allow her to deal with\x01",
            "those kinds of customers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDA")

    label("loc_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12AA")

    ChrTalk(
        0x8,
        "So THOSE guys have come back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll give them a swift boot from the restaurant\x01",
            "if they try anything funny.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A5")

    ChrTalk(
        0x101,
        (
            "#0000F(Sounds like Wald comes here\x01",
            "pretty often.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(It also sounds like the workers are\x01",
            "already used to dealing with him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12A5")

    Jump("loc_1BDA")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A7")

    ChrTalk(
        0x8,
        (
            "Shanshan was still a little girl\x01",
            "when we first moved here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She never had any girls around her\x01",
            "age to be friends with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But finally, after all this time, she's\x01",
            "found herself a good friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm happy for her.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1439")

    label("loc_13A7")


    ChrTalk(
        0x8,
        (
            "I'm happy to see that Shanshan's found herself\x01",
            "a good friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...However.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If her friend is a man, then he'll have\x01",
            "me to answer to!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1439")

    Jump("loc_1BDA")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(
        0x8,
        (
            "I overheard some of\x01",
            "the customers talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I didn't know THEY had come to this\x01",
            "city as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I used to live in the Eastern Quarter, so I've\x01",
            "seen how slimy they are for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would recommend that you don't\x01",
            "get involved with them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15E9")

    label("loc_1556")


    ChrTalk(
        0x8,
        (
            "I'm trying to prepare for the festival,\x01",
            "but I got distracted by a rumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heiyue is slimy, so make sure you\x01",
            "don't get involved with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E9")

    Jump("loc_1BDA")

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_16E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168D")

    ChrTalk(
        0x8,
        "Those two over there talk for hours everyday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they plan to stay here any longer,\x01",
            "then they had better order more food.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E0")

    label("loc_168D")


    ChrTalk(
        0x8,
        (
            "I swear, I'm going to beat those two with\x01",
            "a ladle if they don't shut up soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E0")

    Jump("loc_1BDA")

    label("loc_16E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_17DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1790")

    ChrTalk(
        0x8,
        "*sigh* Shanshan is one stubborn girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've told her many times before to not\x01",
            "bother helping me around the store,\x01",
            "and yet... *grumble*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D7")

    label("loc_1790")


    ChrTalk(
        0x8,
        (
            "Never mind. Did you want to order something?\x01",
            "Go do it over there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D7")

    Jump("loc_1BDA")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E9")

    ChrTalk(
        0x8,
        (
            "I haven't seen those brats from the\x01",
            "Downtown District around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I can finally relax...or so I thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I still have to deal with people getting off\x01",
            "work that come here to get drunk.\x01",
            "I can never seem to catch a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1952")

    label("loc_18E9")


    ChrTalk(
        0x8,
        (
            "Is there something wrong with eating\x01",
            "more quietly? I can never find a\x01",
            "moment of silence for myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1952")

    Jump("loc_1BDA")

    label("loc_1957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A24")

    ChrTalk(
        0x8,
        (
            "Those brats from the Downtown\x01",
            "District piss me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They've fought right in the middle of my\x01",
            "humble little shop before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I obviously threw their asses to the curb.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AD9")

    label("loc_1A24")


    ChrTalk(
        0x8,
        (
            "Those hoodlums from the Downtown District\x01",
            "broke out into a huge fight in here earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't start problems in my establishment,\x01",
            "or I won't let you off so easy next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD9")

    Jump("loc_1BDA")

    label("loc_1ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B80")

    ChrTalk(
        0x8,
        "You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...are aware this is the kitchen, yes?\x01",
            "You're not allowed back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you need to order, do it at the counter!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDA")

    label("loc_1B80")


    ChrTalk(
        0x8,
        (
            "If you have working eyes, you can tell\x01",
            "this is the kitchen. Go order at the counter!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDA")

    Return()

    # Function_7_CBF end

    def Function_8_1BDB(): pass

    label("Function_8_1BDB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1CCB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C71")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CC1")

    label("loc_1C71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C91")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CC1")

    label("loc_1C91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA5")
    Jump("loc_1CC1")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_1CC1")

    Jump("loc_1BF1")

    label("loc_1CC6")

    Jump("loc_1CCE")

    label("loc_1CCB")

    Call(0, 9)

    label("loc_1CCE")

    TalkEnd(0x9)
    Return()

    # Function_8_1BDB end

    def Function_9_1CD2(): pass

    label("Function_9_1CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1D11")

    ChrTalk(
        0x9,
        (
            "The master sure loves to worry,\x01",
            "doesn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_1D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D9D")

    ChrTalk(
        0x9,
        (
            "Puck and Roose started working\x01",
            "here part-time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They've racked up some hefty tabs, so\x01",
            "we're going to work them hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_1D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(
        0x9,
        "Come on in! Need something to eat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're looking pretty worried there.\x01",
            "Something going on outside?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ED1")

    label("loc_1E26")


    ChrTalk(
        0x9,
        (
            "Speaking of 'something' going on, Puck\x01",
            "and Roose look like they might be\x01",
            "breaking up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly, might be better for them than\x01",
            "wasting their time here every day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED1")

    Jump("loc_331A")

    label("loc_1ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA2")

    ChrTalk(
        0x9,
        "Welcome to our humble little inn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The Anniversary Festival's over, so we're\x01",
            "back to serving our regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What a darn shame. We should be raking\x01",
            "in the cash now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2061")

    label("loc_1FA2")


    ChrTalk(
        0x9,
        (
            "I'm a bit of a merchant myself, so I bet'cha\x01",
            "I could run this store better than it currently is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It'd be really nice if we had more festivals,\x01",
            "because we'd have way more customers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2061")

    Jump("loc_331A")

    label("loc_2066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_21A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2104")

    ChrTalk(
        0x9,
        (
            "Shanshan said she's going to go shopping\x01",
            "for western-style clothing with Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Maaan, I sure wish I could go with them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21A0")

    label("loc_2104")


    ChrTalk(
        0x9,
        (
            "Who knows? If I play my cards right,\x01",
            "I might even score a date with Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shopping with women can get pricey,\x01",
            "so I'm sparing my wallet the pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A0")

    Jump("loc_331A")

    label("loc_21A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_231F")

    ChrTalk(
        0x9,
        "Oh, you got some fish for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, thanks. I owe ya one. I should\x01",
            "be able to make it through the night now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some guys are staying here up until\x01",
            "Arc en Ciel's private performance, so I\x01",
            "guess that means they're hotshots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I oughta serve up some sashimi or something,\x01",
            "or else our menu is going to look like a lie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231A")
    SetScenarioFlags(0x0, 1)

    label("loc_231A")

    Jump("loc_331A")

    label("loc_231F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_256F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D0")

    ChrTalk(
        0x9,
        (
            "I come from Calvard, and it sounds like they've\x01",
            "had their fair share of terrorism and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At first glance, it looks like a relaxing place to live,\x01",
            "but once you get past the fluff, there's a lot of\x01",
            "shady stuff going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At least they've got a powerful military,\x01",
            "unlike Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those guys are pretty amazing. I think they're\x01",
            "some unit for 'maintaining public order' or whatever.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_256A")

    label("loc_24D0")


    ChrTalk(
        0x9,
        (
            "Compared to Crossbell, you can't expect\x01",
            "to rely on the police at all, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, oops. Those badges mean that\x01",
            "you're police officers, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256A")

    Jump("loc_331A")

    label("loc_256F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_288C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267A")

    ChrTalk(
        0x9,
        (
            "Man, I'm beat. We had some last second\x01",
            "reservations come in today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd make you some sashimi if it were\x01",
            "any other time, but we're out of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I gotta find myself five of them, and they don't\x01",
            "have to be high-quality, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2887")

    label("loc_267A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(
        0x9,
        "Oh, you got some fish for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, thanks. I owe ya one. I should\x01",
            "be able to make it through the night now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some guys are staying here up until\x01",
            "Arc en Ciel's private performance, so I\x01",
            "guess that means they're hotshots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I oughta serve up some sashimi or something,\x01",
            "or else our menu is going to look like a lie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2887")

    label("loc_27D7")


    ChrTalk(
        0x9,
        (
            "Anyway, you really saved my butt. I should\x01",
            "be able to make it through the night now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So long as those tracksuit-wearing punks\x01",
            "don't cause trouble, we'll be all good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2887")

    Jump("loc_331A")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2983")

    ChrTalk(
        0x9,
        (
            "Shanshan's been getting all friendly with\x01",
            "some girl named Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She was actually here this morning, too.\x01",
            "Man, what a cutie. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She's totally my type...plus, she gets\x01",
            "extra points for being Calvardian! ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A03")

    label("loc_2983")


    ChrTalk(
        0x9,
        (
            "It turns out Rixia's Calvardian, so we'll\x01",
            "have pleeeeenty to talk about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Think I'll go on the offensive next time! ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_2A03")

    Jump("loc_331A")

    label("loc_2A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF6")

    ChrTalk(
        0x9,
        "Hey, hey! Listen to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, there's been a few customers who have reserved\x01",
            "a room here for the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Normally you wouldn't think to get a place\x01",
            "right on the edge of town, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B76")

    label("loc_2AF6")


    ChrTalk(
        0x9,
        (
            "Maybe if we were an actual hotel,\x01",
            "but why would you want to stay\x01",
            "at this tiny inn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Were the hotels just fully booked?\x02",
    )

    CloseMessageWindow()

    label("loc_2B76")

    Jump("loc_331A")

    label("loc_2B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C97")

    ChrTalk(
        0x9,
        (
            "We call those two over there the\x01",
            "Eternal Losers, Roose and Puck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shanshan went to Sunday School with them,\x01",
            "and it sounds like they've always been like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. They're trying to start a business, but\x01",
            "I'm wondering if they can pull it off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D11")

    label("loc_2C97")


    ChrTalk(
        0x9,
        (
            "We call those two over there the\x01",
            "Eternal Losers, Roose and Puck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, when I say 'we,' I actually mean\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D11")

    Jump("loc_331A")

    label("loc_2D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2DA5")

    ChrTalk(
        0x9,
        "Heh. This customer really gets it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our master's from the Eastern Quarter,\x01",
            "so the roasted pork is the best you'll find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_2DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F1C")

    ChrTalk(
        0x9,
        "Man, Shanshan is cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She's hardworking, beautiful, and has\x01",
            "a sexy voice. She's my number one\x01",
            "self-proclaimed wife candidate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though, Master always watches her\x01",
            "like a hawk. Doesn't want anyone making\x01",
            "a move on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can always see him snooping around\x01",
            "while he pretends to work the pan.\x01",
            "I won't lie. It's amusing to watch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F92")

    label("loc_2F1C")


    ChrTalk(
        0x9,
        (
            "Shanshan's looks always turn our\x01",
            "customers' heads towards her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. You can bet Master's\x01",
            "on edge about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F92")

    Jump("loc_331A")

    label("loc_2F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B3")

    ChrTalk(
        0x9,
        (
            "Ohhh, we're on the edge of town,\x01",
            "and there's delinquents all around... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Basically, those guys like to come\x01",
            "and mess the place up real good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those tracksuit-wearing jackasses come here\x01",
            "every couple of days. They're so annoying\x01",
            "to deal with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3133")

    label("loc_30B3")


    ChrTalk(
        0x9,
        (
            "Those guys are pretty infamous\x01",
            "around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, just stay away from those\x01",
            "alley punks, and you'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3133")

    Jump("loc_331A")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_331A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32CD")

    ChrTalk(
        0x9,
        (
            "Welcome to the best combination bar\x01",
            "and inn in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't you think the landscape around\x01",
            "here is kind of a mess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Back when Crossbell was Calvardian territory,\x01",
            "a bunch of immigrants came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After mixing in with all of the other immigrants,\x01",
            "everybody's nationality is a total mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This sorta melting pot environment\x01",
            "has its upsides, too, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_331A")

    label("loc_32CD")


    ChrTalk(
        0x9,
        "You guys tourists? Or locals?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, either way, wanna take\x01",
            "a seat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331A")

    Return()

    # Function_9_1CD2 end

    def Function_10_331B(): pass

    label("Function_10_331B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_333C")
    Call(0, 36)
    Return()

    label("loc_333C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A35")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A31")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",           # 0
            "Give Fish\x01",      # 1
            "Leave\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_33AF"),
        (1, "loc_34BE"),
        (SWITCH_DEFAULT, "loc_3A1D"),
    )


    label("loc_33AF")


    ChrTalk(
        0xFE,
        (
            "Hi there, odd jobbers! Did you\x01",
            "bring me any fish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember, I asked for five\x01",
            "long and slender fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't worry. We can cook all kinds\x01",
            "of fish, but five of the same type of fish\x01",
            "would be ideal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The reservation was for five people, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A2C")

    label("loc_34BE")

    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3594")

    ChrTalk(
        0xA,
        "Ohhhh, you didn't bring me enough fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sorry, but all five of the fish have\x01",
            "to be the same type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have a five person reservation all\x01",
            "ordering the same thing, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A18")

    label("loc_3594")

    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3609")

    ChrTalk(
        0xA,
        "Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The customers are coming tonight, so\x01",
            "it'd be nice if we could get them ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2C")

    label("loc_3609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36CE")

    ChrTalk(
        0xA,
        (
            "Oh, these are the long and slender\x01",
            "ones we need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "These would go great with a rice dish!\x01",
            "Wow, you even brought me five of them.\x01",
            "Is it really okay for me to have these?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3927")

    label("loc_36CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F0")

    ChrTalk(
        0xA,
        (
            "What's this...? They're long and slender,\x01",
            "but also kind of shiny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm... We don't really serve this,\x01",
            "buuuut...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "They're close enough, so it should be fine.\x01",
            "You've even brought five of them, too.\x01",
            "Are you really giving them to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3927")

    label("loc_37F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(
        0xA,
        "What's this supposed to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huh? This isn't even a fish! Why'd\x01",
            "you even bring this to me?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3927")

    label("loc_3886")


    ChrTalk(
        0xA,
        "This...is not a long and slender fish, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well... There are five of them, at least.\x01",
            "Maybe we can still use them.\x01",
            "Are you really giving them to me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3927")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_393B")
    Jump("loc_3A2C")

    label("loc_393B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "[Give]\x01",         # 0
            "[Not yet]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3987")
    Call(0, 37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A2C")

    label("loc_3987")


    ChrTalk(
        0xA,
        (
            "Oh, okay... No point getting upset. I'm sure\x01",
            "you odd jobbers have your reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, feel free to come back if you\x01",
            "change your minds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A18")

    Jump("loc_3A2C")

    label("loc_3A1D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A2C")

    label("loc_3A2C")

    Jump("loc_3366")

    label("loc_3A31")

    TalkEnd(0xFE)
    Return()

    label("loc_3A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3AA1")

    ChrTalk(
        0xA,
        (
            "Great! Surely our customers will\x01",
            "be happy tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You odd jobbers were\x01",
            "a big help!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_3AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5C")

    ChrTalk(
        0xFE,
        "I think something's up with Rixia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We talked for a bit at noon today, but\x01",
            "she wasn't being too responsive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Something must be worrying her again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BBE")

    label("loc_3B5C")


    ChrTalk(
        0xFE,
        (
            "I can easily tell when she's trying to\x01",
            "hide her worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what's up with her...\x02",
    )

    CloseMessageWindow()

    label("loc_3BBE")

    Jump("loc_4B8A")

    label("loc_3BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C77")

    ChrTalk(
        0xFE,
        (
            "Puck and Roose said they wanted to\x01",
            "help out with the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heehee. Daddy immediately gave\x01",
            "them the okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My daddy's super nice like that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CEE")

    label("loc_3C77")


    ChrTalk(
        0xFE,
        (
            "Work's going to be so much easier with\x01",
            "Puck and Roose helping out now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now we can serve even more customers!\x02",
    )

    CloseMessageWindow()

    label("loc_3CEE")

    Jump("loc_4B8A")

    label("loc_3CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9A")

    ChrTalk(
        0xFE,
        (
            "Puck and Roose are always\x01",
            "so energetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used to go to Sunday School\x01",
            "with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a little jealous of their friendship...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DC7")

    label("loc_3D9A")


    ChrTalk(
        0xFE,
        (
            "Puck and Roose are always\x01",
            "so energetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC7")

    Jump("loc_4B8A")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EC3")

    ChrTalk(
        0xFE,
        (
            "It's already been four months since I\x01",
            "started helping here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between waiting tables, washing dishes, and making\x01",
            "the beds, I just love making everything sparkle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Cause you know, a happy customer\x01",
            "means a happy Shanshan!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_3EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3FF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA5")

    ChrTalk(
        0xFE,
        (
            "Hey, listen to this! Rixia said she'd go\x01",
            "to Times with me today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She finally has a day off today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We couldn't hang out at all during the festival,\x01",
            "but we'll have tons of fun today. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FF0")

    label("loc_3FA5")


    ChrTalk(
        0xFE,
        (
            "Oooh, it's almost time for our meetup!\x01",
            "I'm so excited to hang out! ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF0")

    Jump("loc_4B8A")

    label("loc_3FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_411A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C7")

    ChrTalk(
        0xFE,
        (
            "Work's been busy, since the Anniversary\x01",
            "Festival is so close. I need to step it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And for some reason, Daddy's been glaring\x01",
            "at me all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did I mess something up?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4115")

    label("loc_40C7")


    ChrTalk(
        0xFE,
        (
            "I feel like Daddy's been staring at me...\x01",
            "Did I break some plates today?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4115")

    Jump("loc_4B8A")

    label("loc_411A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_422F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4192")

    ChrTalk(
        0xFE,
        (
            "Daddy's always on edge when a certain\x01",
            "customer comes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why, though? Is he scary?\x02",
    )

    CloseMessageWindow()
    Jump("loc_422A")

    label("loc_4192")


    ChrTalk(
        0xFE,
        (
            "I've been working hard all day to make sure\x01",
            "there aren't any problems at the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm having so much fun talking to all kinds\x01",
            "of people! ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422A")

    Jump("loc_4B8A")

    label("loc_422F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_438B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4310")

    ChrTalk(
        0xFE,
        (
            "You know, Rixia looks like she's had a lot\x01",
            "to worry about lately. I keep noticing her\x01",
            "spacing out when we're together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure working for Arc en Ciel comes\x01",
            "with its own set of problems.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4386")

    label("loc_4310")


    ChrTalk(
        0xFE,
        (
            "Rixia looks like she's had a lot to worry\x01",
            "about lately. I wish there was something\x01",
            "I could do to help her out...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4386")

    Jump("loc_4B8A")

    label("loc_438B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_44BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4441")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0xFE,
        "Hey, listen to this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, Rixia is a performer for\x01",
            "Arc en Ciel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooooh, that's so amazing!\x01",
            "I totally admire her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44B6")

    label("loc_4441")


    ChrTalk(
        0xFE,
        (
            "So apparently, my friend, Rixia, performs\x01",
            "for Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooooh, that's so amazing!\x01",
            "I totally admire her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B6")

    Jump("loc_4B8A")

    label("loc_44BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4664")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0xFE,
        "Hey, guys! Listen to this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This absolute cutie of a customer\x01",
            "has been coming by these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her name's Rixia, and she apparently\x01",
            "just moved here recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the best part is, we're the same age!\x01",
            "I hope we can become friends. ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_465F")

    label("loc_45E5")


    ChrTalk(
        0xFE,
        "Rixia moved in around here recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the best part is, we're the same age!\x01",
            "I hope we can become friends. ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_465F")

    Jump("loc_4B8A")

    label("loc_4664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_485B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A4")

    ChrTalk(
        0xFE,
        (
            "I just graduated from Sunday School\x01",
            "earlier this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been thinking about what I should do,\x01",
            "but I think I should help with the business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, look at Daddy. He's got a mean face,\x01",
            "and he's always glaring at customers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I doubt I could leave him to run things alone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4856")

    label("loc_47A4")


    ChrTalk(
        0xFE,
        (
            "We'd be broke if I left the store to my dad,\x01",
            "so I help out as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've had trouble getting used to it, but I'm sure\x01",
            "it'll all work out if I keep smiling! ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4856")

    Jump("loc_4B8A")

    label("loc_485B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_49F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4979")

    ChrTalk(
        0xFE,
        (
            "Many members of the CGF come here\x01",
            "to eat on weekends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so interesting to talk to so many\x01",
            "different kinds of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their jobs must be really hard, though.\x01",
            "They always look so tired after work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Maybe I'll try to encourage them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49F2")

    label("loc_4979")


    ChrTalk(
        0xFE,
        (
            "Members of the CGF like to come\x01",
            "here often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their jobs look really hard, so maybe I'll\x01",
            "try and encourage them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F2")

    Jump("loc_4B8A")

    label("loc_49F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4A59")

    ChrTalk(
        0xFE,
        "So, how was your food?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's great stuff, right?\x01",
            "Daddy's such a good cook.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_4A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1D")

    ChrTalk(
        0xFE,
        "Oooh, what a cute customer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will you be dining in, or are you renting a room?\x01",
            "We have spots open for either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Place your order when you're ready, okay? ㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B8A")

    label("loc_4B1D")


    ChrTalk(
        0xFE,
        (
            "Not only do we serve food, but we also\x01",
            "offer lodging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Place your order when you're ready, okay? ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_4B8A")

    TalkEnd(0xFE)
    Return()

    # Function_10_331B end

    def Function_11_4B8E(): pass

    label("Function_11_4B8E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C22")
    Jump("loc_4C6C")

    label("loc_4C22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C42")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C6C")

    label("loc_4C42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C62")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C6C")

    label("loc_4C62")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C6C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4DF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D59")

    ChrTalk(
        0xFE,
        "Oh, wow. Time flew by in an instant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*munch* *crunch*\x01",
            "I'd better quickly finish up this meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just got one more delivery out to Calvard\x01",
            "to finish up the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DEF")

    label("loc_4D59")


    ChrTalk(
        0xFE,
        (
            "Just got one more delivery out to Calvard\x01",
            "to finish up the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's become more commonplace to use\x01",
            "orbal trucks for deliveries these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DEF")

    Jump("loc_5E40")

    label("loc_4DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F07")

    ChrTalk(
        0xFE,
        (
            "I was delivering some stuff to the\x01",
            "Rizero Trading Company yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their employees were freaking out because\x01",
            "their president had gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't hear much about it, but the guy signing\x01",
            "the papers seemed pretty stressed out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F62")

    label("loc_4F07")


    ChrTalk(
        0xFE,
        (
            "Where the heck did their president even go?\x01",
            "Does he like to spontaneously take trips?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F62")

    Jump("loc_5E40")

    label("loc_4F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_510E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505B")

    ChrTalk(
        0xFE,
        (
            "I've been seeing a bunch of black vans\x01",
            "whenever I drive on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are usually guys wearing shades\x01",
            "behind the wheel. They don't seem too\x01",
            "friendly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I get the creeps whenever I drive past 'em.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5109")

    label("loc_505B")


    ChrTalk(
        0xFE,
        (
            "And if I'm not mistaken, I'm pretty sure those\x01",
            "vans are made in the Empire. They're pretty\x01",
            "expensive, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was there always a trading company\x01",
            "that used those vans?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5109")

    Jump("loc_5E40")

    label("loc_510E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5210")

    ChrTalk(
        0xFE,
        (
            "Been noticing a lot more delivery trucks\x01",
            "on the highway recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I make four whole trips to the Republic daily...\x01",
            "Even with a truck, it's still a huge pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well... I did get a raise, so I\x01",
            "shouldn't be complaining.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_527D")

    label("loc_5210")


    ChrTalk(
        0xFE,
        (
            "Been noticing a lot more trucks going through\x01",
            "the highway to make deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This job ain't easy.\x02",
    )

    CloseMessageWindow()

    label("loc_527D")

    Jump("loc_5E40")

    label("loc_5282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_52EB")

    ChrTalk(
        0xFE,
        "*chew* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Ack!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wh-Whew, that was a close call.\x01",
            "Almost choked there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E40")

    label("loc_52EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_538B")

    ChrTalk(
        0xFE,
        (
            "They finally reopened the road out to Calvard,\x01",
            "so we can start up our deliveries again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*munch* *chew*...\x01",
            "Better eat while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E40")

    label("loc_538B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54D6")

    ChrTalk(
        0xFE,
        (
            "Some truck got into an accident near Calvard, and\x01",
            "it was supposedly holding some smuggled goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like it was one of those newer models\x01",
            "from the Reinford Company, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What if...it was more than just a simple 'accident'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Aidios... Please don't let me\x01",
            "get dragged into this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_557E")

    label("loc_54D6")


    ChrTalk(
        0xFE,
        (
            "That truck that got into an accident near Calvard\x01",
            "was supposedly holding some smuggled goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if...it was more than just a simple 'accident'?\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_557E")

    Jump("loc_5E40")

    label("loc_5583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5675")

    ChrTalk(
        0xFE,
        (
            "The company I work for told me that deliveries\x01",
            "to Calvard are suspended until the accident's\x01",
            "been cleaned up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on what I've heard, it sounds like\x01",
            "a pretty terrible accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Dunno the details myself, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E40")

    label("loc_5675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AF")

    ChrTalk(
        0xFE,
        (
            "*munch* *munch*... Sounds like another truck\x01",
            "got into an accident near Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't been keeping up with it, but apparently\x01",
            "the Calvardian army has started to handle\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The highways are fiercely regulated now, so\x01",
            "you don't see many people going through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57FB")

    label("loc_57AF")


    ChrTalk(
        0xFE,
        (
            "*chew*... Doubt you'd get through today,\x01",
            "no matter how much you hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57FB")

    Jump("loc_5E40")

    label("loc_5800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_589B")

    ChrTalk(
        0xFE,
        "*chew* *chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, that reminds me... Noticed the\x01",
            "CGF's been mobilizing these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They doing military drills, or what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E40")

    label("loc_589B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_59E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595D")

    ChrTalk(
        0xFE,
        "*chew* *chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of my good buds drives a delivery\x01",
            "route through the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Imperial border sounds like a pain\x01",
            "in the ass to get through, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_59E2")

    label("loc_595D")


    ChrTalk(
        0xFE,
        (
            "The procedures necessary for entering\x01",
            "Erebonia sure seem strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Makes sense, I guess. They're a\x01",
            "huge militarized country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E2")

    Jump("loc_5E40")

    label("loc_59E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF4")

    ChrTalk(
        0xFE,
        (
            "There's a town right past the Calvardian\x01",
            "border called Altair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not exactly big, but it's been a hub\x01",
            "for people to leave and enter Crossbell\x01",
            "for decades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Crossbellan side of Tangram Gate's\x01",
            "always packed with travelers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B99")

    label("loc_5AF4")


    ChrTalk(
        0xFE,
        (
            "There's a town right past the Calvardian\x01",
            "border called Altair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you keep going down the East Highway into\x01",
            "Tangram Gate, you'll get there pretty quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B99")

    Jump("loc_5E40")

    label("loc_5B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9E")

    ChrTalk(
        0xFE,
        "*chew* *crunch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orbal trucks cost a heck\x01",
            "of a lot of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, the government's giving out\x01",
            "subsidies to help purchase 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And thanks to that, my company's been steadily\x01",
            "building up our fleet of trucks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5D3A")

    label("loc_5C9E")


    ChrTalk(
        0xFE,
        (
            "Whenever you buy an orbal truck, the government\x01",
            "will subsidize your purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, every company's able\x01",
            "to get their hands on one now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D3A")

    Jump("loc_5E40")

    label("loc_5D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E05")

    ChrTalk(
        0xFE,
        "*chew* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I work as a delivery truck driver, and I gotta\x01",
            "make round trips out to Calvard daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, it can get pretty taxing.\x01",
            "*chew* *munch*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E40")

    label("loc_5E05")


    ChrTalk(
        0xFE,
        (
            "*chew*... Gotta take every opportunity\x01",
            "I have to eat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E40")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_4B8E end

    def Function_12_5E48(): pass

    label("Function_12_5E48")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5F38")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F33")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EBE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5EBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EDE")
    OP_AF(0x34)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F2E")

    label("loc_5EDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EFE")
    OP_AF(0x32)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F2E")

    label("loc_5EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F12")
    Jump("loc_5F2E")

    label("loc_5F12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_5F2E")

    Jump("loc_5E5E")

    label("loc_5F33")

    Jump("loc_5F3B")

    label("loc_5F38")

    Call(0, 13)

    label("loc_5F3B")

    TalkEnd(0xC)
    Return()

    # Function_12_5E48 end

    def Function_13_5F3F(): pass

    label("Function_13_5F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FCE")

    ChrTalk(
        0xC,
        "Welcome. Anything you want to eat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You know, I'm starting to feel like I'm\x01",
            "pretty talented at working at a\x01",
            "restaurant!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6102")

    label("loc_5FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6102")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6083")

    ChrTalk(
        0xC,
        (
            "My buddy Roose and I are thinking about\x01",
            "opening up our own store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're in the planning stages right now.\x01",
            "The early days, as you might call it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6102")

    label("loc_6083")


    ChrTalk(
        0xC,
        (
            "Everybody who's ever made it big had to\x01",
            "start SOMEWHERE, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nothing's gonna stop me from reaching\x01",
            "for the stars!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6102")

    Return()

    # Function_13_5F3F end

    def Function_14_6103(): pass

    label("Function_14_6103")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6197")
    Jump("loc_61E1")

    label("loc_6197")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61B7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61E1")

    label("loc_61B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61D7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61E1")

    label("loc_61D7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61E1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6217")
    Call(0, 16)
    Jump("loc_6AEE")

    label("loc_6217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_62CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6232")
    Call(0, 16)
    Jump("loc_62C8")

    label("loc_6232")


    ChrTalk(
        0xFE,
        (
            "I'm meeting up with the chairman of the\x01",
            "Business Owners' Association tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is gonna be huge! I'm way too\x01",
            "excited to sleep tonight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C8")

    Jump("loc_6AEE")

    label("loc_62CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C5")

    ChrTalk(
        0xFE,
        (
            "After I saw all those insane crowds during the\x01",
            "festival, I've been overflowing with ideas on\x01",
            "what to sell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Heh. Yep, I'm definitely talented at this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being a merchant is all about debuting\x01",
            "with a big bang!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6431")

    label("loc_63C5")


    ChrTalk(
        0xFE,
        "Heh. Yep, I'm definitely talented at this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll show everyone the biggest bang\x01",
            "they've ever seen!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6431")

    Jump("loc_6AEE")

    label("loc_6436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_650D")

    ChrTalk(
        0xFE,
        (
            "I'm thinking about just dropping\x01",
            "this business talk with my bud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Cause Roose just never stops\x01",
            "obsessing over details, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Running a business should be more\x01",
            "carefree and fun, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_650D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_657A")
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xFE,
        "Roose just doesn't get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might have inherited my pro skills\x01",
            "from my grandpa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_657A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_65EB")

    ChrTalk(
        0xFE,
        (
            "I think I might even be suited for a\x01",
            "managerial position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys think so, too, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_65EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6692")

    ChrTalk(
        0xFE,
        (
            "Roose's always too busy talking about\x01",
            "the theoretical side of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too bad that's all useless to talk about\x01",
            "before you actually own a shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_6692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6792")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6726")

    ChrTalk(
        0xFE,
        "Man, Roose is way too argumentative.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You ain't starting a business with such an\x01",
            "inflexible mindset these days.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_678D")

    label("loc_6726")


    ChrTalk(
        0xFE,
        (
            "Damn, Roose. He's gotta take some notes from\x01",
            "more open-minded individuals. You know,\x01",
            "like myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678D")

    Jump("loc_6AEE")

    label("loc_6792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6834")
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xFE,
        (
            "*chew* *crunch*\x01",
            "She may only be helping out, but even Shanshan's\x01",
            "managing to work for a business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There's no way we can't do it, too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_6834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_69A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6950")

    ChrTalk(
        0xFE,
        (
            "I wasn't getting anywhere talking\x01",
            "to my bud, so I decided to consult\x01",
            "the Grimwood Law Office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could see how shocked he looked\x01",
            "as he explained to me that I needed to\x01",
            "decide on a business before starting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess that was kind of obvious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69A2")

    label("loc_6950")


    ChrTalk(
        0xFE,
        (
            "You need to decide on what to sell if you're\x01",
            "planning on starting a company.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A2")

    Jump("loc_6AEE")

    label("loc_69A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6A57")
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xFE,
        (
            "So on that note, the president is obviously\x01",
            "going to be the one, the only, the amazingly\x01",
            "talented yours truly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, Roose! Are you even listening?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AEE")

    label("loc_6A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6AEE")

    ChrTalk(
        0xFE,
        "Me and my bud are going to start a business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're aiming to make the best company in\x01",
            "all of Crossbell! Us men gotta dream big, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AEE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_6103 end

    def Function_15_6AF6(): pass

    label("Function_15_6AF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B7E")

    ChrTalk(
        0xFE,
        (
            "I got a part-time job so I could earn funds\x01",
            "to start my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My wages are so low that\x01",
            "it makes me wanna cry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B7E")

    TalkEnd(0xFE)
    Return()

    # Function_15_6AF6 end

    def Function_16_6B82(): pass

    label("Function_16_6B82")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C16")
    Jump("loc_6C60")

    label("loc_6C16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C60")

    label("loc_6C36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C60")

    label("loc_6C56")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C60")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6DC9")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D46")

    ChrTalk(
        0xF,
        (
            "Uh-oh, I think we're forgetting\x01",
            "something important, Puck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Don't we need money if we're\x01",
            "going to open a store?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Crap. You're right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6DC4")

    label("loc_6D46")


    ChrTalk(
        0xF,
        (
            "Grrrr! How could you forget\x01",
            "something so important?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Wh-What the hell, Roose! You only\x01",
            "just remembered it yourself!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC4")

    Jump("loc_8041")

    label("loc_6DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F28")
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xF,
        "All right, it's perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We've finally decided on a name for our\x01",
            "store and what wares we'll be selling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "We've also decided on a president!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Are you ready? We're calling it\x01",
            "Puck & Roose Company, and\x01",
            "we'll be dealing in sundries!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "As of tomorrow, we'll be starting\x01",
            "our new lives as merchants!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_701E")

    label("loc_6F28")


    ChrTalk(
        0xFE,
        (
            "We managed to meet the Business Owners'\x01",
            "Association's chairman in a sheer stroke of\x01",
            "luck as he passed by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We got him to introduce us to some suppliers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's good to know that Aidios has not abandoned\x01",
            "those who believe in Her!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701E")

    Jump("loc_8041")

    label("loc_7023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_71F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FA")

    ChrTalk(
        0xFE,
        (
            "Heh. All of these jerks kept telling us\x01",
            "that we weren't going to accomplish\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who's the stupid one now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha! Look at what we can pull off\x01",
            "when we get serious!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71F2")

    label("loc_70FA")


    ChrTalk(
        0xFE,
        (
            "Have you seen those two guys that've\x01",
            "stayed here since the festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They keep wasting away talking about a bunch\x01",
            "of pointless stuff. What a bunch of losers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bunch of losers like them won't ever\x01",
            "accomplish anything in their lives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71F2")

    Jump("loc_8041")

    label("loc_71F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_73F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737E")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xFE,
        "Damn it! Why can't we agree on anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's try this from the top again, Puck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "When you think ramen, you think shoyu, right?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xD,
        "Yeah, no. This ain't it, Roose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Miso ramen is WAY better than shoyu!\x01",
            "Why can't you acknowledge that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "What'd you say?! You'd better take\x01",
            "that back!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_73F4")

    label("loc_737E")


    ChrTalk(
        0xFE,
        "Damn it! Why can't we agree on ANYTHING?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Starting a business with Puck might be\x01",
            "a horrible, horrible idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F4")

    Jump("loc_8041")

    label("loc_73F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_754C")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xFE,
        (
            "I've read through Mr. Crois' autobiography\x01",
            "front to back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He says, in order to start a business, you'll\x01",
            "need to effectively calculate the expenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So what? I don't need to hear any of that.\x01",
            "I've already read my grandpa's diary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "'Business is all about having spirit!'\x01",
            "...Or so he claims.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7591")

    label("loc_754C")

    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xFE,
        "This isn't going anywhere, is it...?\x02",
    )

    CloseMessageWindow()

    label("loc_7591")

    Jump("loc_8041")

    label("loc_7596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_76F4")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76CC")

    ChrTalk(
        0xFE,
        (
            "Confidence is the most important quality\x01",
            "of any seasoned businessman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, one of us is going to have to decide\x01",
            "what our company's going to deal in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Probably best leave that to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uh, no? Shouldn't it be me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Your face is just going to scare people away.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_76EF")

    label("loc_76CC")


    ChrTalk(
        0xFE,
        "My face isn't important here!\x02",
    )

    CloseMessageWindow()

    label("loc_76EF")

    Jump("loc_8041")

    label("loc_76F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_78F3")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7860")

    ChrTalk(
        0xFE,
        (
            "*munch* *chew* *crunch* *slurp*\x01",
            "All right. Listen up, Puck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All products have a buying and a selling price,\x01",
            "so when you make the sale price higher than\x01",
            "the buying price--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Pfft! What are you blabbering about, Roose?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "None of that stuff matters if you've got spirit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Your 'spirit' will BANKRUPT US IN MINUTES!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_78EE")

    label("loc_7860")


    ChrTalk(
        0xFE,
        (
            "How the hell can you not understand something\x01",
            "THIS basic...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hell, your entire concept of common sense\x01",
            "seems to have sprung a leak.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78EE")

    Jump("loc_8041")

    label("loc_78F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4F")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xFE,
        (
            "Everybody probably thinks we're a pair\x01",
            "of worthless idiots who waste the day\x01",
            "away chatting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You saw how those tourists from earlier\x01",
            "were laughing at us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is probably all your fault, Puck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "No! It's obviously yours, Roose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "They probably thought your wicked case\x01",
            "of bedhead was hilarious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7ABC")

    label("loc_7A4F")


    ChrTalk(
        0xFE,
        "My buddy Puck and I can't ever agree on anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does he actually care about starting\x01",
            "a business?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ABC")

    Jump("loc_8041")

    label("loc_7AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7C6B")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BDC")

    ChrTalk(
        0xFE,
        "*munch* *munch* *crunch* *chew*\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "What the fudge, Puck?! Don't\x01",
            "eat that dumpling. It's mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "*crunch* *gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, maybe you should lay off the dumplings, then.\x01",
            "You're going to have some real stinky breath.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7C66")

    label("loc_7BDC")


    ChrTalk(
        0xFE,
        (
            "Maaan, Shanshan is so attractive...she might\x01",
            "just be the perfect waitress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Enough about her, though.\x01",
            "More importantly... *chew*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C66")

    Jump("loc_8041")

    label("loc_7C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D8A")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xFE,
        (
            "The best selling product\x01",
            "in all of Crossbell is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Orbal cars!\x02",
    )


    ChrTalk(
        0xD,
        "Arc en Ciel tickets!\x02",
    )

    OP_57(0x1)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xFE,
        (
            "Come on, Puck. Are you\x01",
            "trying to be a scalper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Arc en Ciel tickets are crazy popular, man!\x01",
            "We'd totally make a killing!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7E05")

    label("loc_7D8A")


    ChrTalk(
        0xFE,
        (
            "The business world's all about\x01",
            "orbal cars right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every man dreams of owning one...\x01",
            "Aren't you guys the same?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E05")

    Jump("loc_8041")

    label("loc_7E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7ED6")
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xFE,
        (
            "(That lady sitting behind us earlier\x01",
            "was pretty cute, wasn't she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hey, Roose! Are you even paying attention?!\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Huh? Oh, yeah... What were you saying?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8041")

    label("loc_7ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8041")
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF8")

    ChrTalk(
        0xFE,
        (
            "#1PThere's one thing we'll need to decide on before\x01",
            "we start our business, and that's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2PThe president!\x02",
    )


    ChrTalk(
        0xFE,
        "#1PThe company's name!\x02",
    )

    OP_57(0x1)

    ChrTalk(
        0xFE,
        "#1POh, come on. The name's totally important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2POh, yeah? Who decides the name?\x01",
            "The president, right?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8041")

    label("loc_7FF8")


    ChrTalk(
        0xFE,
        (
            "You're only saying that because\x01",
            "you wanna be president, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8041")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_6B82 end

    def Function_17_8049(): pass

    label("Function_17_8049")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80DD")
    Jump("loc_8127")

    label("loc_80DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80FD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8127")

    label("loc_80FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_811D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8127")

    label("loc_811D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8127")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "#1806F*sigh* Isn't there any place around here\x01",
            "that has cheap rent?\x02\x03",
            "#1802FCity Hall told me to look in this area,\x01",
            "but I haven't found anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_8049 end

    def Function_18_81EE(): pass

    label("Function_18_81EE")

    Call(0, 19)
    Return()

    # Function_18_81EE end

    def Function_19_81F2(): pass

    label("Function_19_81F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_86D1")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_836D")

    ChrTalk(
        0x13,
        (
            "Hey, Grace. Why'd you decide to become\x01",
            "a reporter for the Crossbell Times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#2102FMmm, let me think about it. It's probably\x01",
            "'cause of my unquenchable curiosity.\x02\x03",
            "#2109FIsn't gossiping about political scandals,\x01",
            "celebrities, and the like totally interesting?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "Wow. You're awfully honest when\x01",
            "you're in a good mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86C9")

    label("loc_836D")


    ChrTalk(
        0x12,
        (
            "#2105F*munch* *munch*\x01",
            "Whoa! You've got an older twin brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Haha, yeah... He's a farmer up\x01",
            "in Ored State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I came to Crossbell on my own,\x01",
            "in hopes of becoming a reporter.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84F9")

    ChrTalk(
        0x102,
        (
            "#0100F(I see Grace sharing a meal with\x01",
            "her coworker.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Let's avoid her. She'd sink her fangs\x01",
            "right into KeA's innocent little neck.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(Y-You can say that again.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C6")

    label("loc_84F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85ED")

    ChrTalk(
        0x103,
        (
            "#0200F(I believe Grace is enjoying a meal\x01",
            "with her coworker.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Let's avoid her. She'd probably sink her\x01",
            "teeth right into poor little KeA and never\x01",
            "let go.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Your imagination is certainly active.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C6")

    label("loc_85ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86C6")

    ChrTalk(
        0x104,
        (
            "#0300F(Yo, that Grace chick is eatin' a meal\x01",
            "with her coworker.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Let's avoid her. She'd sink her vampirous\x01",
            "teeth right into KeA's innocent little\x01",
            "neck.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F(You said it, bud.)\x02",
    )

    CloseMessageWindow()

    label("loc_86C6")

    SetScenarioFlags(0x1, 1)

    label("loc_86C9")

    TalkEnd(0xFE)
    Jump("loc_86E2")

    label("loc_86D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86E2")
    Call(0, 30)

    label("loc_86E2")

    Return()

    # Function_19_81F2 end

    def Function_20_86E3(): pass

    label("Function_20_86E3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8777")
    Jump("loc_87C1")

    label("loc_8777")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8797")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87C1")

    label("loc_8797")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87B7")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87C1")

    label("loc_87B7")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87C1")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8953")

    ChrTalk(
        0x103,
        "#0205FWhy is our chief at such an establishment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#1000FYo, everyone.\x02\x03",
            "How's the investigation? Progressing smoothly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI suppose you could say that, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe're going to head to St. Ursula\x01",
            "Medical College from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#1000FHeh. Enthusiastic, aren't we?\x02\x03",
            "#1003FWell, good luck with that.\x01",
            "Give me your report later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8A04")

    label("loc_8953")


    ChrTalk(
        0x11,
        (
            "#1000FThe grub here is pretty good, so you should\x01",
            "eat some lunch if you haven't yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FActually, we did already eat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FChief's as cool as a cucumber, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_8A04")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_20_86E3 end

    def Function_21_8A0C(): pass

    label("Function_21_8A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8D43")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AA9")
    Jump("loc_8AF3")

    label("loc_8AA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AC9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8AF3")

    label("loc_8AC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8AF3")

    label("loc_8AE9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8AF3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8BB2")

    ChrTalk(
        0xFE,
        (
            "This is the first step towards bonding with\x01",
            "my septium trading father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had plenty of fun sightseeing, but it's\x01",
            "time I head out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D37")

    label("loc_8BB2")


    ChrTalk(
        0xFE,
        (
            "I very much enjoyed seeing all the sights\x01",
            "Crossbell had to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's about time I went and purchased\x01",
            "that septium crystal I had my eyes\x01",
            "on earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty easy to get to Mainz now that\x01",
            "they've established a bus route there\x01",
            "from the northern exit of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the first step towards bonding with\x01",
            "my septium trading father! Okay, it's\x01",
            "time I head out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_8D37")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_8FB2")

    label("loc_8D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8DD2")

    ChrTalk(
        0xFE,
        (
            "I seem to remember seeing a huge department\x01",
            "store when I came here from the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll head there first.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FAF")

    label("loc_8DD2")

    OP_4B(0x15, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)

    ChrTalk(
        0x14,
        (
            "The first thing I need to do is conduct\x01",
            "a month-long preliminary investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "I'll start by checking out the city...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Excuse me, my lady. Did we not come here\x01",
            "to purchase septium? Have you forgotten\x01",
            "about that already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Huh? What are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Why would I come to Crossbell JUST\x01",
            "to buy some shiny rock? That's a total\x01",
            "waste of an opportunity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "(It's quite obvious she wants to see the sights...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    OP_4C(0x15, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_8FAF")

    TalkEnd(0xFE)

    label("loc_8FB2")

    Return()

    # Function_21_8A0C end

    def Function_22_8FB3(): pass

    label("Function_22_8FB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_908C")

    ChrTalk(
        0xFE,
        (
            "We came to Crossbell with the intention of\x01",
            "purchasing goods, but we ended up spending\x01",
            "the whole month sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do wonder what's happening back at\x01",
            "the Imperial mansion right about now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9149")

    label("loc_908C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9138")

    ChrTalk(
        0xFE,
        (
            "I was hoping to buy the septium as quickly as\x01",
            "possible, so we could return immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Excuse me, my lady. Did we not come here\x01",
            "to see the sights?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9149")

    label("loc_9138")

    TurnDirection(0x14, 0x15, 0)
    TurnDirection(0x15, 0x14, 0)
    Call(0, 21)

    label("loc_9149")

    TalkEnd(0xFE)
    Return()

    # Function_22_8FB3 end

    def Function_23_914D(): pass

    label("Function_23_914D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_94B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_92FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_9214")

    ChrTalk(
        0x16,
        (
            "Going down the path of a poet...\x01",
            "That doesn't sound too bad, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I lost all my motivation since I got here,\x01",
            "but maybe I'll give it another shot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92F5")

    label("loc_9214")


    ChrTalk(
        0x16,
        (
            "I fear my heart will shatter into pieces if\x01",
            "I suffer another unrequited love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hey, Ricky. What should I have\x01",
            "done differently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I feel a little bad for him, but I think\x01",
            "we should give him some space.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_92F5")

    Jump("loc_94AE")

    label("loc_92FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_930F")
    Call(0, 29)
    Jump("loc_94AE")

    label("loc_930F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_93EA")

    ChrTalk(
        0x16,
        (
            "I can't believe it... I somehow\x01",
            "ran into her sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "There's no mistaking it, Ricky. This is fate.\x01",
            "Fate, I tell ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It's our destiny to be together! I'm so\x01",
            "frickin' happy I could die!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94AE")

    label("loc_93EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_93FF")
    Call(0, 28)
    Jump("loc_94AE")

    label("loc_93FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9413")
    Call(0, 27)
    Jump("loc_94AE")

    label("loc_9413")


    ChrTalk(
        0x16,
        (
            "I'm going to do it this time, Ricky. I'm finally\x01",
            "going to make my wish come true!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I wonder about her every day. Where is she?\x01",
            "What is she doing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94AE")

    Jump("loc_95C7")

    label("loc_94B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_9522")

    ChrTalk(
        0xFE,
        (
            "I know nothing of that girl, not even her name...\x01",
            "And yet I do wonder where and how she is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95C7")

    label("loc_9522")


    ChrTalk(
        0xFE,
        (
            "The whole world had forsaken me, but an angel\x01",
            "descended from the heavens and blessed me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder about her every day. Where is she?\x01",
            "What is she doing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_95C7")

    TalkEnd(0xFE)
    Return()

    # Function_23_914D end

    def Function_24_95CB(): pass

    label("Function_24_95CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_996D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96AA")

    ChrTalk(
        0x17,
        "Cheer up, buddy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "If you really think it suits you, then why\x01",
            "don't you give this whole poet deal\x01",
            "another shot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Who knows? You might even be able to write\x01",
            "really angsty poetry now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9968")

    label("loc_96AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9748")

    ChrTalk(
        0x17,
        (
            "Hey, guys. Anton's been eagerly\x01",
            "awaiting your report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "If he wants to meet her that badly, then\x01",
            "why doesn't he go see her himself?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9968")

    label("loc_9748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_9836")

    ChrTalk(
        0x17,
        (
            "Anton has a bad habit of leaving these\x01",
            "kinds of things in the hands of 'fate.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "But if you ask me, if they were REALLY fated\x01",
            "to be with each other, he would have met her\x01",
            "when he went down to the police station.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9968")

    label("loc_9836")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_98DB")

    ChrTalk(
        0x17,
        (
            "He's been here for THREE whole weeks already.\x01",
            "Give it a rest, man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Every day is an adventure with Anton...\x01",
            "Who knows what'll happen next?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9968")

    label("loc_98DB")


    ChrTalk(
        0x17,
        (
            "He submitted a support request, but I\x01",
            "don't know if it'll get accepted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "You might wanna wait until he's\x01",
            "calmed down a bit, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9968")

    Jump("loc_9B14")

    label("loc_996D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_9A08")

    ChrTalk(
        0xFE,
        (
            "Anton's trying to find the lady that helped\x01",
            "him find his wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a total Anton move to leave\x01",
            "without asking for their name.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B14")

    label("loc_9A08")


    ChrTalk(
        0xFE,
        (
            "Anton dropped his wallet, and a lady passing\x01",
            "by happened to notice, so she helped him\x01",
            "look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's all it took for Anton to think they\x01",
            "were fated to meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And thanks to that, he decided to postpone\x01",
            "our return home so he could search for her.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_9B14")

    TalkEnd(0xFE)
    Return()

    # Function_24_95CB end

    def Function_25_9B18(): pass

    label("Function_25_9B18")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BAC")
    Jump("loc_9BF6")

    label("loc_9BAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9BCC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BF6")

    label("loc_9BCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BEC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BF6")

    label("loc_9BEC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BF6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9CB4")

    ChrTalk(
        0x18,
        (
            "#1602FA legendary assassin, eh? You've\x01",
            "definitely got my attention.\x02\x03",
            "I'd love to have a go at 'em if he comes\x01",
            "onto our turf.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E98")

    label("loc_9CB4")


    ChrTalk(
        0x18,
        (
            "#1603FAnd while we're on the topic of Easterners...\x02\x03",
            "#1600FThose Heiyue guys have been pushin'\x01",
            "their damn luck lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FH-How'd you hear about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FDamn, dude. Already? These friggin'\x01",
            "rumors keep spreadin' like wildfire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1602FWhy ya actin' all surprised? All sorts of rumors\x01",
            "spread about the Downtown District.\x02\x03",
            "#1604FI heard they hired some 'legendary' assassin...\x01",
            "Haha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FCould you please not try to pick fights\x01",
            "with everyone? Thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_9E98")

    Jump("loc_A0EF")

    label("loc_9E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9F2F")

    ChrTalk(
        0x18,
        (
            "#1603FDamn, I'm starved. Mornin' practice with\x01",
            "the boys did a number on me.\x02\x03",
            "#1600FWish they'd hurry up with the food already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0EF")

    label("loc_9F2F")


    ChrTalk(
        0x18,
        "#1600FOh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHey, Wald... Do you come here often?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1603FPretty much. Owner's some annoyin'\x01",
            "old dude, but the grub's decent.\x02\x03",
            "#1602FAnd not to mention, their waitress is pretty\x01",
            "friggin' sexy, y'know what I'm saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FOh, dude. I totally feel you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    ChrTalk(
        0x102,
        "#0106FSeriously, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FYour lack of integrity is concerning, Randy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)

    label("loc_A0EF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_9B18 end

    def Function_26_A0F7(): pass

    label("Function_26_A0F7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A18B")
    Jump("loc_A1D5")

    label("loc_A18B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1D5")

    label("loc_A1AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1CB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1D5")

    label("loc_A1CB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1D5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A39E")

    ChrTalk(
        0x19,
        (
            "Yeah, get 'em with the nail bat!\x01",
            "It's a Testament bloodbath! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "*munch* *munch* *gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Kinda feelin' like I'm up for some\x01",
            "pudding...or am I?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A393")
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
            "#0006F(Is he actually singing, eating, and ordering\x01",
            "all at the same time? Maybe he should try\x01",
            "sticking to one thing at a time...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A393")

    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x19, 0x1)
    TalkEnd(0xFE)
    Return()

    label("loc_A39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_A414")

    ChrTalk(
        0x19,
        "I'm still huuuuuungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh, yeah! I'm hella hungry! Hurry, hurry,\x01",
            "bring me all the foooood! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4A7")

    label("loc_A414")


    ChrTalk(
        0x19,
        "The hell are a bunch of COPPERS doin' here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, whatever. Don't get in the way of my\x01",
            "eatin' if you know what's good for ya. Got it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_A4A7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_A0F7 end

    def Function_27_A4AF(): pass

    label("Function_27_A4AF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x102, -100750, 20, -53000, 180)
    SetChrPos(0x103, -99250, 20, -52000, 180)
    SetChrPos(0x104, -101000, 20, -52000, 180)
    SetChrPos(0x109, -99500, 20, -51000, 180)
    OP_93(0x16, 0x10E, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    ChrTalk(
        0x16,
        "#12PI'm begging you, Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PPlease let me meet with that\x01",
            "beautiful angel again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FExcuse me... Are you Anton?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    ChrTalk(
        0x16,
        "#12PYep, that's me. Who are you, though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FWe're with the Crossbell Police Department's\x01",
            "Special Support Section. We're here to consult\x01",
            "you about a support request.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#12POh! I've been waiting for you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PThere's a huge favor I need from you,\x01",
            "and I'm kinda in a hurry. Will you hear\x01",
            "me out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FYeah, we will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FThe request stated that you're trying\x01",
            "to locate a woman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PYeah. I really need to find her so I can\x01",
            "give her my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PShe pulled me out of the darkness when\x01",
            "no one else could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FCare to elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PSure. My best friend Ricky and I came\x01",
            "here from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PTo be honest, my life stinks. I figured visiting\x01",
            "somewhere a little more exciting might help\x01",
            "turn it around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0003FF-Fair enough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PNothing changed, though. I still got slapped\x01",
            "across the face by the cold, cruel reality of\x01",
            "my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PTo make matters worse, I managed to lose\x01",
            "my wallet...along with my travel expenses.\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#0006FOuch. That sounds unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWell, yeah. Leave it to someone as dull and\x01",
            "hopeless as myself to screw up that badly.\x01",
            "I really am my own worst enemy, aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PRicky already tried to help me find my wallet,\x01",
            "but it was to no avail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PI had no choice but to start borrowing\x01",
            "money from him. I also considered\x01",
            "cutting our trip short...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12P...however, that was when it all began.\x01",
            "Just when all hope was lost, that kind\x01",
            "lady gave me the helping hand I needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FMan, I'm jealous. Not a lotta gals out there\x01",
            "are that nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PSeriously... It was all thanks to her\x01",
            "efforts that I was able to get my\x01",
            "wallet back in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PAs you can imagine, I thought our\x01",
            "meeting had to have been fated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PShe held out her hand for me when I was\x01",
            "trapped in an endless pit of darkness, so\x01",
            "to me, she's nothing short of an angel.\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0006FSo...to make an unnecessarily long story\x01",
            "short, you want us to find this girl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PExactamundo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PThe problem is, I've been searching for\x01",
            "her for the last three weeks, but I haven't\x01",
            "found a single lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PI asked the Bracer Guild to help a poor guy\x01",
            "out, but they turned me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PThey claimed that it'd be a low priority case,\x01",
            "since she isn't exactly missing. They had far\x01",
            "more important work they needed to focus on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PHell, if this were Liberl, I'd be able to get help\x01",
            "with something as mundane as a drinking\x01",
            "con...test...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0x16)

    ChrTalk(
        0x101,
        "#5P#0005FAre you okay...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12P...I'm fine. Just reopened an old wound.\x01",
            "A-Anyway, moving along...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PRicky heard about your team while he was\x01",
            "out on the town, so he submitted a request\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PYour team's pretty much like the Bracer\x01",
            "Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PC'mon, help a poor guy out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0006FW-Well... Sure, why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0505FHuh. I didn't know the SSS handled\x01",
            "requests of this nature.\x02\x03",
            "#0500FYour work has a much wider scope\x01",
            "than I thought it did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FTo be fair, something like this\x01",
            "is quite rare...\x02\x03",
            "#0100FSo, what's the plan, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0203FI do not know how I feel about the CPD\x01",
            "involving themselves in other people's\x01",
            "personal affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0003F(She makes a good point.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0304FGotta be honest with you guys.\x01",
            "I kinda wanna scope out this chick.\x02\x03",
            "#0300FWhat'd she look like, anyway?\x02\x03",
            "#0309FBet she's cute as heck, yeah? ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PCute as heck doesn't even BEGIN to\x01",
            "describe her. I still have her burned\x01",
            "into my memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PHer gentle aura soothes the most\x01",
            "dissolute of men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PHer calm voice oozes with kindness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PAnd don't even get me started on her\x01",
            "utterly adorable, auburn pigtails...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0005FHuh? I can't help but shake the feeling\x01",
            "that I know someone like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0103FI agree. That sounds awfully familiar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI, too, seem to recall encountering someone\x01",
            "of a similar description frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FWell, he's clearly talkin' about our\x01",
            "Fran, ain't he?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#5P#0505FOh! I think you're right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PW-Wait a second! You guys KNOW HER?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0503FThere's a strong chance we do...\x02\x03",
            "#0500FYou said she had auburn-colored hair...\x01",
            "Was it roughly the same color as mine?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x16, 0x109, 500)
    Sleep(500)

    ChrTalk(
        0x16,
        "#12PY-YEAH!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PIt is! It totally is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PNo way... Don't tell me...\x01",
            "Are you related to each other?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#5P#0503FAs long as this isn't the world's biggest\x01",
            "coincidence, I'm actually her older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12POh, sweet Aidios! You've done it again!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 500)

    ChrTalk(
        0x16,
        "#12PYou hear that, Ricky?! Fate strikes again!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    ChrTalk(
        0x17,
        (
            "#5PSure, Anton. If that's what your heart\x01",
            "believes, then maybe you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PThough, you're kinda ignoring the possibility\x01",
            "that she might not actually be 'the one.'\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(500)
    TurnDirection(0x16, 0x109, 500)

    ChrTalk(
        0x16,
        "#12PE-E-Excuse me, dear sister!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#0505FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PDoes she have...you know...\x01",
            "A romantic partner already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0505FH-Huh?!\x02\x03",
            "#0503FU-Um... Not that I've heard of...\x02\x03",
            "#0508FWe don't live together, but she's never\x01",
            "told me anything of the sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PI see... A-Anyway, I'd like to really show\x01",
            "her my most heartfelt thanks before I\x01",
            "head back to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWould you do me the great honor\x01",
            "of asking her to meet with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#0503FHmm...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#0500FWell, I suppose I don't mind.\x01",
            "Is that all right with you, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2A, 0x1, 0x0)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF92")

    ChrTalk(
        0x101,
        "#5P#0000FAll right. We'll accept your request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PYes! Thank you so, so, SO much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PO-Okay, then. I'm counting on you guys.\x01",
            "Please get her to promise to meet with\x01",
            "me again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FNow that it's settled, we should head over\x01",
            "to the department and see if we can get a\x01",
            "hold of her.\x02\x03",
            "#0000FI bet she's manning the reception desk\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#0500FGood idea. I'll come along with you.\x02",
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
            "[A Sincere Favor]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_C23E")

    label("loc_BF92")


    ChrTalk(
        0x101,
        (
            "#5P#0006FI hate to leave you hanging, but we're kind of\x01",
            "in the middle of an important case, so I don't\x01",
            "think we can help you right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12P...I see. I guess this is the end, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PThis is how it's always been.\x01",
            "No one takes me seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWell, I suppose you did hear me out, but\x01",
            "I understand why you'd think that no good\x01",
            "could ever come of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0012FH-Hey, come on, now. You don't need to\x01",
            "be so hard on yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0505FHe's right, you know. It's not like we've\x01",
            "completely refused you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PNo, it's okay. You don't need to\x01",
            "try to make me feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PI'll keep my expectations in check,\x01",
            "but I'll be waiting here, regardless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C23E")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_27_A4AF end

    def Function_28_C26E(): pass

    label("Function_28_C26E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x102, -100750, 20, -53000, 180)
    SetChrPos(0x103, -99250, 20, -52000, 180)
    SetChrPos(0x104, -101000, 20, -52000, 180)
    SetChrPos(0x109, -99500, 20, -51000, 180)
    OP_93(0x16, 0x0, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    ChrTalk(
        0x16,
        "#12POh, you're those police officers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PYou really came back for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FY-Yeah, we did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PSo, about that lady... Fran, I believe\x01",
            "her name was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWill you help me? Can you get\x01",
            "her to meet with me again?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C68C")

    ChrTalk(
        0x101,
        "#5P#0000FAll right. We'll accept your request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PWhoa. For real?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PLike, for really real? You're not messing with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FYeah, of course not.\x02\x03",
            "#0003F(With a face like that, you'd think the world\x01",
            "was ending before his very eyes.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PO-Okay, then. I'm counting on you guys.\x01",
            "Please get her to promise to meet with\x01",
            "me again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FNow that it's settled, we should head over\x01",
            "to the department and see if we can get a\x01",
            "hold of her.\x02\x03",
            "I bet she's manning the reception desk\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#0500FGood idea. I'll come along with you.\x02",
    )

    CloseMessageWindow()
    OP_29(0x2A, 0x1, 0x1)
    Jump("loc_C831")

    label("loc_C68C")


    ChrTalk(
        0x101,
        (
            "#5P#0006FS-Sorry, but we're still kind of in the\x01",
            "middle of something important right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PIt's fine. I'm already used to this type\x01",
            "of treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWhy do I even try? Nothing EVER goes\x01",
            "the way I want it to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(Th-This guy's more childish than Ryu...)\x02\x03",
            "#0000FI-I hate to leave you like this, but we'll\x01",
            "come back if we find the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PI'll be waiting but won't get my\x01",
            "hopes up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C831")

    SetChrPos(0x0, -100000, 20, -53500, 180)
    OP_93(0x16, 0x10E, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_C26E end

    def Function_29_C861(): pass

    label("Function_29_C861")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x17, 0xFF)
    OP_68(-100600, 1420, -53410, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -100000, 20, -53500, 180)
    SetChrPos(0x109, -100750, 20, -53000, 180)
    SetChrPos(0x102, -99250, 20, -52000, 180)
    SetChrPos(0x103, -101000, 20, -52000, 180)
    SetChrPos(0x104, -99500, 20, -51000, 180)
    OP_93(0x16, 0x0, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0000FHello again, Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12POh, you guys are back already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PH-How'd it go? Did you get Fran\x01",
            "to agree to meet with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FSurprisingly enough, yes. She seemed\x01",
            "receptive to the whole idea.\x02\x03",
            "#0000FShe'll be on break soon, so she'd\x01",
            "like to meet you at the restaurant in\x01",
            "Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PO-Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PTh-Thank you so much. I don't know\x01",
            "how I'll ever repay you for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PMan, oh, man. I didn't think a bum like\x01",
            "myself would ever get a lucky break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#0200FHe seems a little overly thrilled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FI'm glad it's working out for you, Anton.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#12POh, right! I need to find her an appropriate\x01",
            "gift to thank her for her help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PI don't actually have anything prepared for her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FDude... Seriously? Shoulda had that planned\x01",
            "well in advance. The date's already knockin'\x01",
            "on your damn door!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PH-Hey, can you blame me?! I didn't think I'd\x01",
            "be meeting her this quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12POh, I know just the thing!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x109, 500)

    ChrTalk(
        0x16,
        (
            "#12PP-Pardon me, dear sister. Would you\x01",
            "be willing to accompany me to Times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#0505FTimes...? Why do you want to go there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#12PIt's the perfect place to find a present for Fran!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PYou're sisters, so I figure you have all kinds of\x01",
            "insider knowledge on her tastes and hobbies.\x01",
            "I could find her the perfect gift!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#0508FR-Right...\x02\x03",
            "#0506FOn that note, I'd really rather you\x01",
            "didn't call me 'dear sister.'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)

    ChrTalk(
        0x16,
        (
            "#12POh, by the way, the rest of you will\x01",
            "also help me pick out a present...right?\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0006FUh...\x01",
            "(Don't look at me with those\x01",
            "puppy-dog eyes!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0203FThis is becoming more bothersome\x01",
            "by the second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(Well, we've come this far, so we may as well\x01",
            "see it through to the end.)\x02\x03",
            "#0000FAll right. Shall we go to Times, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PSir, yes, sir! Thanks a bunch,\x01",
            "you guys!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5E, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_C861 end

    def Function_30_D0DF(): pass

    label("Function_30_D0DF")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch06000.itc", 0x22)
    LoadChrToIndex("apl/ch50090.itc", 0x23)
    SoundLoad(827)
    OP_68(4900, 1000, 6400, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 4800, 0, 5400, 0)
    SetChrPos(0x102, 6100, 0, 4800, 315)
    SetChrPos(0x103, 4400, 0, 4100, 0)
    SetChrPos(0x104, 6600, 0, 6200, 270)
    SetChrPos(0x12, 4900, 100, 7100, 270)
    SetChrSubChip(0x12, 0x1)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x12,
        (
            "#0400620VHeh heh.  I knew you'd come crawling. ♪\x02\x03",
            "#0400621VDon't be shy, now! Have a seat, I'll treat you all\x01",
            "to a nice dinner. ♪\x02",
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
        (
            "#0400622V#12P#0006FWhile that's awfully kind of you, we'll have to\x01",
            "respectfully decline the dinner.\x02\x03",
            "#0400623V#0001FHow about we stick to exchanging information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400624V#2101F#5PBoo. You're no fun.\x02\x03",
            "#0400625V#2102FOr are you trying to make a statement that\x01",
            "you're impervious to bribes, unlike the\x01",
            "upper echelons of the CPD?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400626V#12P#0005F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400627V#0303FLet's not get ahead of ourselves.\x02\x03",
            "#0400628V#0302FI'll gladly scope out that free meal, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400629V#2P#0204FI would also accept, so long as you are\x01",
            "not scheming to make us owe you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400630V#0103FIt's...probably okay?\x02\x03",
            "#0400631V#0100FI don't see the harm in sharing\x01",
            "a casual meal together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400632V#12P#0011F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400633V#2102F#5PHahaha. You're the only one worried\x01",
            "about some kinda moral conflict.\x02\x03",
            "#0400634V#2109FHow are you going to become a pro\x01",
            "detective if you act like such a prude\x01",
            "all the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400635V#12P#0013FAll right, I get it already!\x02\x03",
            "#0400636V#0003FBut I'm forbidding you all from drinking!\x01",
            "As long as you abide by this one rule,\x01",
            "we'll accept your offer.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x7D0)
    OP_68(3200, 1000, 7100, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 1500, 100, 6500, 90)
    SetChrPos(0x102, 1500, 100, 7600, 90)
    SetChrPos(0x103, 3200, 100, 5500, 0)
    SetChrPos(0x104, 3200, 100, 8900, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x12, 4900, 100, 7100, 270)
    SetChrSubChip(0x12, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x3, 0x1C)
    OP_78(0x4, 0x1D)
    SetChrPos(0x1C, 1400, 0, 6500, 0)
    OP_D3(0x1C, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1D, 1400, 0, 7700, 0)
    OP_D3(0x1D, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetChrChipByIndex(0x1E, 0x15)
    SetChrSubChip(0x1E, 0x2)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 2400, 600, 6600, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x23)
    SetChrSubChip(0x1F, 0xE)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 2100, 500, 6600, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x15)
    SetChrSubChip(0x20, 0x1)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 3300, 600, 6400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x14)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 3300, 500, 6100, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x2)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 2400, 600, 7700, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0xE)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 2100, 500, 7700, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x15)
    SetChrSubChip(0x24, 0x1)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 3300, 600, 8000, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x14)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 3300, 500, 8300, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x15)
    SetChrSubChip(0x26, 0x2)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 4000, 600, 7100, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0xE)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 4400, 500, 7100, 0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x6)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 3200, 600, 7100, 0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    Sound(827, 2, 0, 0)
    BeginChrThread(0x29, 0, 0, 42)
    SetCameraDistance(18500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x102,
        (
            "#0400637V#6P#0109FThis is delectable...\x02\x03",
            "#0400638V#0102FThe chef here is highly skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400639V#12P#0204F*munch* *munch*\x01",
            "This food is most satisfying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400640V#5P#0306FThough it's kinda hard to savor somethin'\x01",
            "this tasty without a good drink.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#0400641V#5P#0302FC'mon, Lloyd. Don't be such a hard-ass.\x01",
            "One sip ain't gonna kill me, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0400642V#6P#0003FAbsolutely not. You know we're still\x01",
            "technically on duty, right?\x02\x03",
            "#0400643V#0001FWe have to keep our wits about us\x01",
            "at all times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400644V#5P#0306FYeah, yeah. Whatever. Our leader's\x01",
            "as stubborn as a damn mule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400645V#12P#0211FOn the contrary, Randy. Are you not the\x01",
            "one who is far too nonchalant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400646V#6P#0101FI'm going to have to agree with them.\x01",
            "Drinking on the job is highly inappropriate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400733V#11P#2104FHeehee.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#0400648V#11P#2109FYou guys are so much fun.\x02\x03",
            "#0400649V#2100FYour personalities are wildly different,\x01",
            "yet you fit together perfectly, almost\x01",
            "like a jigsaw puzzle.\x02\x03",
            "#0400650VHeck, you're basically a well-oiled\x01",
            "machine now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400651V#6P#0006FFlattery will get you nowhere.\x02\x03",
            "#0400652V#0001FBack to the topic at hand. We've told you\x01",
            "everything we know about the incident\x01",
            "that occurred in the Downtown District.\x02\x03",
            "#0400653VI seem to recall you mentioning that you\x01",
            "had the 'missing piece to the puzzle' earlier.\x02\x03",
            "#0400654VIsn't it about time you filled us in on it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400655V#11P#2102FAnd what if I told you that I don't wanna?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400656V#6P#0003FGood luck ever getting us to trust\x01",
            "you again, Grace.\x02\x03",
            "#0400657V#0001FNot only that, but it'd be the last\x01",
            "time we'd talk. Ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400658V#11P#2105FOh, calm down! I was just messing with you.\x02\x03",
            "#0400659V#2109FThough, I gotta say. You can be pret-ty\x01",
            "charming when you're serious.\x02\x03",
            "#0400660V#2102FIt's a nice contrast to your boyish looks.\x01",
            "I hate to admit it, but you've caught my\x01",
            "attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400661V#6P#0004FOkay, guys. How about we get back to work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400662V#6P#0102FYes, that sounds fine by me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400663V#12P#0204FI appreciate the meal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400664V#11P#2106FWhoa, whoa! Hold your horses, people!\x02\x03",
            "#0400665V#2101FYou want your missing piece of the\x01",
            "puzzle, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400666V#6P#0006F*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400667V#11P#2103FHmm, where do I begin?\x02\x03",
            "#0400668V#2100FOkay. Have you guys ever heard\x01",
            "of a group named 'Revache'?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400669V#6P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400670V#6P#0101FI've heard the name.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0400671V#5P#0305FGuys? What's with the blank look\x01",
            "on your faces?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400672V#12P#0205F'Revache & Co...'\x02\x03",
            "#0400673V#0203FI believe there is a business in Crossbell\x01",
            "registered under that name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400674V#11P#2104FHeh. That's all they appear to be on a quick\x01",
            "surface-level examination.\x02\x03",
            "#0400675V#2101FThe truth of the matter is that they're actually\x01",
            "Crossbell's mafia. They've been controlling our\x01",
            "dark underworld for a long time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x104, 0x1)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x2)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0400676V#12P#0201FBy mafia, do you mean that they are\x01",
            "a criminal organization?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400677V#5P#0301FMakes sense. I've definitely heard rumors\x01",
            "about there bein' a mafia in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#0400678V#5P#0301FI'm guessin' you already know a thing\x01",
            "or two about that, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0400679V#6P#0003FI do.\x02\x03",
            "#0400680V#0001FIt's pretty hard to be in the dark\x01",
            "about them if you're Crossbellan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400681V#6P#0108FTheir organization has a vast network\x01",
            "of connections with important people.\x02\x03",
            "#0400682V#0101FI've heard that they've got strong ties deep\x01",
            "within the government, so the police can't\x01",
            "take any actions against them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400683V#5P#0303FInteresting. The underbelly of society's\x01",
            "pretty much identical no matter where\x01",
            "you go, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400684V#12P#0200FSo, why the mention of Revache?\x01",
            "Are they involved with the incident?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#0400685V#11P#2103FOh, you bet'cha.\x02\x03",
            "#0400686V#2101FRevache's members have been engaged\x01",
            "in some rather...shady business lately.\x02\x03",
            "#0400687VThey've been working their behinds off,\x01",
            "almost as if they're anxious to complete\x01",
            "some kind of plan.\x02\x03",
            "#0400688VSo, being the investigative guru I am,\x01",
            "I decided to spend some time sinking\x01",
            "my teeth into this potential scoop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400689V#6P#0005FWhat do you mean by the mafia working\x01",
            "harder than usual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400690V#6P#0103FThis certainly sounds ominous...\x01",
            "I have a terrible feeling about this.\x02\x03",
            "#0400691V#0101FIs that why you decided to visit the\x01",
            "Downtown District, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400692V#6P#0013FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400693V#11P#2100FBingo, my friend.\x02\x03",
            "#0400694V#2103FAbout two weeks ago, one of my sources\x01",
            "provided me with some intel on members\x01",
            "of the mafia snooping around downtown.\x02\x03",
            "#0400695VThey were dressed like civilians, probably\x01",
            "to try to conceal their identities.\x02\x03",
            "#0400696V#2102FDoesn't that smell awfully fishy to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x104,
        "#0400697V#5P#0301FIt reeks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400698V#6P#0003FAgreed. Something feels out of place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400699V#6P#0103FIt's unlikely that each gang would simultaneously\x01",
            "and independently choose to attack one another.\x02\x03",
            "#0400700V#0101FRevache orchestrating things from the shadows\x01",
            "would explain how that happened.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#0400701V#12P#0201FI am confused about something, though.\x02\x03",
            "#0400702VFor what reason does a criminal organization\x01",
            "require delinquent groups to antagonize\x01",
            "each other?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0400703V#6P#0001FRight. That's the million mira question.\x02\x03",
            "#0400704VIt'd make sense if they already harbored\x01",
            "a grudge against one another.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x12,
        (
            "#0400705V#11P#2106FUh-huh. And as far as I know, they don't\x01",
            "have a rocky relationship, and I've never\x01",
            "heard of any serious conflicts between them.\x02\x03",
            "#0400706V#2101FQuite frankly, all three groups are savages.\x01",
            "Those mafia dudes are way more threatening\x01",
            "than the others, though.\x02\x03",
            "#0400707VThe weird part is, Revache doesn't have any\x01",
            "conflicts of interest with the other two groups.\x01",
            "I don't see the need for them to be fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400708V#5P#0300FWhat if one of 'em formed an alliance with\x01",
            "the mafia to off their rival group, once and\x01",
            "for all?\x02\x03",
            "#0400709VGoin' by this assumption, then it's not exactly\x01",
            "surprising that the culprits would play the role\x01",
            "of the victim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400710V#6P#0106FBut do they really need to take it that far?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400711V#6P#0001FI didn't get the impression that Wazy and\x01",
            "Wald were on bad terms with each other.\x02\x03",
            "#0400712VIf anything, I felt like they held each other\x01",
            "in high regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400713V#11P#2105FHey, that's what I was gonna say.\x02\x03",
            "#0400714V#2104FFrom what I've gathered, Wazy and Wald ARE\x01",
            "rivals, but they hold a mutual respect for one\x01",
            "another.\x02\x03",
            "#0400715V#2100FSo at first, Wald and the Saber Vipers were\x01",
            "the only gang in the Downtown District...\x02\x03",
            "#0400716V...but then that all changed two years ago.\x01",
            "Wazy showed up out of nowhere and\x01",
            "established the Testaments.\x02\x03",
            "#0400717V#2106FAnd we all know how Wald is, so he obviously\x01",
            "went to go put Wazy in his place, but, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400718V#6P#0005FWazy took him down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400719V#11P#2109FYeppers, he sure did!\x02\x03",
            "#0400720V#2110FDespite his charming looks and small frame,\x01",
            "Wazy's a skilled martial artist.\x02\x03",
            "#0400721VI'd heard he managed to take Wald by\x01",
            "surprise with his lightning quick moves,\x01",
            "and pinned him to the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400722V#6P#0105FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400723V#12P#0205FI was not expecting that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400724V#5P#0305FThat cute little dude's freakishly strong?\x01",
            "Color me surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400725V#6P#0006FNo kidding, but I don't think Wald's\x01",
            "a pushover, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400726V#11P#2104FHe was a little too careless that one time.\x01",
            "They've fought a number of times since,\x01",
            "but they're at a stalemate, supposedly.\x02\x03",
            "#0400727V#2100FI think that's precisely why they respect\x01",
            "each other, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400728V#6P#0100FThat makes perfect sense. I see why\x01",
            "they consider each other rivals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400729V#5P#0301FS'pose that rules out any likelihood that\x01",
            "either of them formed an alliance with\x01",
            "the mafia to crush each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400730V#6P#0008FAgreed.\x02\x03",
            "#0400731VThey're both worshiped by their respective\x01",
            "gangs, so I doubt their subordinates were\x01",
            "acting independently.\x02\x03",
            "#0400732V#0006FHmm... This can really only mean one thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400647V#11P#2104FHeehee...\x02\x03",
            "#0400734V#2102FI may have divulged a little more\x01",
            "information than I should have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400735V#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 5100, 0, 6200, 270)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#0400736V#11P#2110FAnyway. I've got other interviews to conduct,\x01",
            "so I'm going to take off.\x02\x03",
            "#0400737VKick some butt with that investigation so\x01",
            "I can write me a good story later.\x02\x03",
            "#0400738V#2109FToodles. ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1500, 1000, 0, 3000)
    OP_92(0x12, 0x5DC, 0x0, 0x1F4)

    def lambda_FCFC():
        OP_95(0xFE, 1500, 0, 0, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_FCFC)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x101, 0x2)
    Sleep(1500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x12, 1)

    def lambda_FD36():
        OP_95(0xFE, -2000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_FD36)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_FD5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_FD5C)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x12, 2)
    Sound(104, 0, 100, 0)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(3200, 1000, 7100, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0400739V#6P#0006F*sigh*...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#0400740V#3P#0102FShe sure has an interesting way of\x01",
            "handling things.\x02\x03",
            "#0400741V#0100FBut regardless, we were able to obtain\x01",
            "some highly valuable information.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#0400742V#6P#0000FYeah, knowing that the mafia is likely involved\x01",
            "with this mess is a huge leap forward in our\x01",
            "investigation.\x02\x03",
            "#0400743V#0003FNow, the real question is, why did the mafia\x01",
            "get themselves involved with their affairs?\x02\x03",
            "#0400744V#0008FThis is going to be a tough one to figure out\x01",
            "with the limited evidence we have right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#0400745V#11P#0203FThe police database does not appear to have\x01",
            "any relevant information, either.\x02\x03",
            "#0400746V#0201FI believe it is locked behind multiple levels\x01",
            "of authorization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400747V#5P#0306FSo it's classified info, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400748V#3P#0108FIt makes sense, considering whose pockets\x01",
            "the mafia has their hands in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400749V#6P#0003F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearChrFlags(0x101, 0x4)
    OP_68(3100, 1000, 6720, 0)
    SetChrPos(0x101, 1500, 0, 5300, 45)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400750V#0001F#12PAll right, let's head back to the SSS and see\x01",
            "what Chief Sergei has to say about everything.\x02\x03",
            "#0400751VAs much as I'd love for us to solve the case,\x01",
            "the situation is starting to become larger\x01",
            "than what we can handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400752V#3P#0100FYou're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400753V#1P#0300FYeah, let's head back and see what\x01",
            "the old man has to say for himself.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 43)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 21000, 0, 19000, 0)
    SetChrPos(0x1D, 21000, 0, 19000, 0)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(1500, 1400, 5300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 1500, 0, 5300, 180)
    SetChrPos(0x1, 1500, 0, 5300, 180)
    SetChrPos(0x2, 1500, 0, 5300, 180)
    SetChrPos(0x3, 1500, 0, 5300, 180)
    SetScenarioFlags(0x42, 5)
    OP_29(0x3E, 0x1, 0x5)
    ReplaceBGM("ed7100", "ed7000")
    ReplaceBGM("ed7101", "ed7000")
    ReplaceBGM("ed7100", "ed7102")
    EndChrThread(0x29, 0x0)
    OP_24(0x33B)
    EventEnd(0x5)
    Return()

    # Function_30_D0DF end

    def Function_31_104CB(): pass

    label("Function_31_104CB")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 90)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#12PThis is bad... Who would have\x01",
            "thought they'd sell out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x1A, 0x0, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x1A,
        "#12PWait, don't you guys work for...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PAnyway, did you happen to purchase one\x01",
            "of those Mishy plushes that were being\x01",
            "sold earlier this month?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PAnd if so, would you be okay\x01",
            "with selling it to me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FHmm... I can't say I've ever heard\x01",
            "of this 'Mishy' you're talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FMishy is the official mascot of Mishelam.\x02\x03",
            "I seem to remember Tio being an avid\x01",
            "collector of his goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou are correct. I have not purchased the\x01",
            "new Mishy plush yet, unfortunately.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x1A,
        "#12POh, you're a fan, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PHahaha. Truth be told, my son is\x01",
            "especially fond of him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PAnd thus, I'm traveling from afar to\x01",
            "collect the new plush for him. There's\x01",
            "just one problem, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)

    ChrTalk(
        0x1A,
        (
            "#12PBy the time I went to the department store\x01",
            "in Central Square, it was already sold out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FWow, they managed to sell out at the\x01",
            "department store? Are they that popular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FIndeed they are.\x02\x03",
            "#0200FA campaign to sell limited time merchandise\x01",
            "began recently. A new item is offered each\x01",
            "month, and some are exceedingly popular.\x02\x03",
            "#0202FThis month's item is the Mishy plush.\x01",
            "Its charm lies in its size, as it fits in\x01",
            "the palm of your hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FWithout skippin' a beat, Tio Tot manages to pull\x01",
            "the goods from her database of a brain.\x02\x03",
            "...\x02\x03",
            "#0303FY'know, now that you mention it, I remember\x01",
            "seeing our feline friend being offered as a\x01",
            "prize at the casino.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10B9E():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10B9E)

    def lambda_10BAB():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10BAB)

    def lambda_10BB8():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10BB8)

    def lambda_10BC5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10BC5)
    Sleep(600)
    OP_93(0x104, 0xE1, 0x12C)

    ChrTalk(
        0x104,
        (
            "#0303FNot really interested in plushes, so I ended\x01",
            "up ignorin' it.\x02\x03",
            "#0300FDidn't seem like it was anythin' special when\x01",
            "lined up alongside the other prizes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#12PReally?!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x13B, 0x12C)
    Sleep(300)

    ChrTalk(
        0x1A,
        (
            "#12PWell, I'm not one to gamble. So, going to the\x01",
            "casino would be a little conflicting for me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10CFE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10CFE)

    def lambda_10D0B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_10D0B)

    def lambda_10D18():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_10D18)

    def lambda_10D25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_10D25)
    OP_63(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A)
    Sleep(300)
    OP_93(0x1A, 0x0, 0x12C)

    ChrTalk(
        0x1A,
        (
            "#12PI hate to ask this of you, but would you be\x01",
            "willing to go and win the plush for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PI'll be sure to pay you for your efforts!\x01",
            "Please, help me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(I don't know about you guys, but it feels\x01",
            "off-brand to hit the casino for a support\x01",
            "request.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100F(This technically isn't an official request. As\x01",
            "long as we're doing it as a favor of kindness,\x01",
            "we're unlikely to have any issues.)\x02\x03",
            "#0106F(As long as you-know-who doesn't go overboard.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309FHell yeah, let's do this! Come on, guys!\x01",
            "We're off to the casino!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    def lambda_10FC5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10FC5)

    def lambda_10FD2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10FD2)

    def lambda_10FDF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10FDF)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0200FSomebody is impatient.\x02\x03",
            "#0211FPlease do not tell us you fabricated your claims\x01",
            "as an excuse to visit the casino.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[We Long for Mishy]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50510, 30, -53790, 180)
    OP_4C(0x1A, 0xFF)
    BeginChrThread(0x1A, 0, 0, 2)
    ClearChrFlags(0x1B, 0x10)
    OP_29(0xC, 0x4, 0x2)
    OP_29(0xC, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_104CB end

    def Function_32_110F2(): pass

    label("Function_32_110F2")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#12PN-No way, is that what I think it is?!\x01",
            "You actually managed to get the Mishy\x01",
            "plush?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PI can't believe you got one! C-Could\x01",
            "I please have it? Pretty please?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Give]\x01",         # 0
            "[Not yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11275"),
        (1, "loc_11279"),
        (SWITCH_DEFAULT, "loc_11323"),
    )


    label("loc_11275")

    Call(0, 33)
    Return()

    label("loc_11279")


    ChrTalk(
        0x1A,
        "#12PW-Wait, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PLet me know if you change your mind, please.\x01",
            "I can't go home empty-handed. My son would\x01",
            "be crushed.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -50510, 30, -53790, 180)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    EventEnd(0x5)
    Jump("loc_11323")

    label("loc_11323")

    Return()

    # Function_32_110F2 end

    def Function_33_11324(): pass

    label("Function_33_11324")

    ClearChrFlags(0x1B, 0x4)

    ChrTalk(
        0x101,
        (
            "#5P#0000FYeah, it's all yours. Fortunately enough,\x01",
            "it wasn't too difficult to get.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave the Mishy plush toy to Lars.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SubItemNumber(0x5D, 1)

    ChrTalk(
        0x1A,
        "#12POh, so this is Mishy.\x02",
    )

    CloseMessageWindow()
    OP_68(-53210, 1400, -55140, 2000)

    def lambda_11402():

        label("loc_11402")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_11402")

    QueueWorkItem2(0x0, 1, lambda_11402)

    def lambda_11414():

        label("loc_11414")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_11414")

    QueueWorkItem2(0x1, 1, lambda_11414)

    def lambda_11426():

        label("loc_11426")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_11426")

    QueueWorkItem2(0x2, 1, lambda_11426)

    def lambda_11438():

        label("loc_11438")

        TurnDirection(0xFE, 0x1A, 300)
        Yield()
        Jump("loc_11438")

    QueueWorkItem2(0x3, 1, lambda_11438)
    OP_95(0x1A, -52950, 0, -54800, 4000, 0x0)
    OP_93(0x1A, 0xE1, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#11PYou see that, Kurt? Your dad went and\x01",
            "got your beloved Mishy!\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
    Sleep(600)
    TurnDirection(0x1B, 0x1A, 500)

    ChrTalk(
        0x1B,
        "#6PWoow, it's Mishy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#6PIt's really him, I can't believe it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_68(-50420, 1400, -54190, 2000)
    OP_95(0x1A, -50570, 30, -55800, 4000, 0x0)
    OP_93(0x1A, 0x0, 0x1F4)
    Sleep(300)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#12PThank you, everyone. You've made\x01",
            "my boy as happy as can be.\x01",
            "I have to think about how I'm going to repay you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#12PLet's see... Oh, I've got it. It's not much, but\x01",
            "I hope you'll accept it.\x02",
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
            "Received \x07\x02",
            "120 mira\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(120)

    ChrTalk(
        0x101,
        (
            "#5P#0000FThanks, haha. Really, though, it wasn't\x01",
            "a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0304FYeah, doin' a request of that caliber is\x01",
            "a piece of cake.\x02\x03",
            "I woulda been able to score enough cash to\x01",
            "build an art gallery had I been given enough\x01",
            "time. But, a certain missy put a stop to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0103FAhem! Well, shall we return to our duties?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FUnderstood. I expect Randy will expend an\x01",
            "equal amount of energy the next time a similar\x01",
            "opportunity arises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0306FJust you try and stop me.\x02",
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
            "[We Long for Mishy]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -50110, 30, -52370, 180)
    SetChrPos(0x1A, -49440, 30, -56190, 270)
    SetChrPos(0x1B, -51000, 30, -56190, 90)
    SetChrFlags(0x1B, 0x4)
    BeginChrThread(0x1A, 0, 0, 0)
    TalkBegin(0x1A)
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_29(0xC, 0x4, 0x10)
    OP_29(0xC, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_11324 end

    def Function_34_1195D(): pass

    label("Function_34_1195D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11DF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11AF5")

    ChrTalk(
        0xFE,
        (
            "Thank you, everyone. My boy is enjoying\x01",
            "every second of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank Aidios we came to Crossbell. Thank\x01",
            "Mishy for putting a smile on my son's\x01",
            "precious face!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AED")

    ChrTalk(
        0x104,
        (
            "#0300F(Tourists come out here for the craziest\x01",
            "of reasons, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(I can relate. I would do the same for Mishy.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_11AED")

    SetScenarioFlags(0x2, 1)
    Jump("loc_11DEE")

    label("loc_11AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x5D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B27")
    Call(0, 32)
    Jump("loc_11D07")

    label("loc_11B27")


    ChrTalk(
        0x1A,
        (
            "You actually managed to get the Mishy plush?!\x01",
            "I can't believe you got one! C-Could\x01",
            "I please have it? Pretty please?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Give]\x01",         # 0
            "[Not yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11BE3"),
        (1, "loc_11C81"),
        (SWITCH_DEFAULT, "loc_11D07"),
    )


    label("loc_11BE3")

    TalkEnd(0x1A)
    EventBegin(0x0)
    EndChrThread(0x1A, 0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    Fade(800)
    OP_68(-50420, 1400, -54190, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20940, 0)
    SetChrPos(0x101, -51120, 30, -54260, 180)
    SetChrPos(0x102, -51120, 30, -52840, 180)
    SetChrPos(0x103, -50000, 30, -54260, 180)
    SetChrPos(0x104, -50000, 30, -52840, 180)
    SetChrPos(0x1A, -50570, 30, -55800, 0)
    OP_0D()
    Call(0, 33)
    Return()

    label("loc_11C81")


    ChrTalk(
        0x1A,
        "W-Wait, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Let me know if you change your mind, please.\x01",
            "I can't go home empty-handed. My son would\x01",
            "be crushed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D07")

    label("loc_11D07")

    Jump("loc_11DEE")

    label("loc_11D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_11DEB")

    ChrTalk(
        0xFE,
        (
            "Why'd it have to go and be a prize at\x01",
            "the casino, of all places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm not a gambler in the slightest bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like for you guys to get it for me, but\x01",
            "I can't help but feel selfish for asking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DEE")

    label("loc_11DEB")

    Call(0, 31)

    label("loc_11DEE")

    Jump("loc_11F34")

    label("loc_11DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_11EAB")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1A,
        "Okay, we've finished eating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It's time for us to go and buy what we\x01",
            "came for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Yay! I'm excited!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Haha. You sure love Mishy, don't you?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    Jump("loc_11F34")

    label("loc_11EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_11F34")

    ChrTalk(
        0xFE,
        (
            "I took a long trip out to Crossbell for\x01",
            "my boy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd do anything for my son. I'm not\x01",
            "afraid of working overtime!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F34")

    TalkEnd(0xFE)
    Return()

    # Function_34_1195D end

    def Function_35_11F38(): pass

    label("Function_35_11F38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_12044")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11F9D")

    ChrTalk(
        0xFE,
        "Wow, it's really Mishy! He's soooo cute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1203F")

    label("loc_11F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_12001")

    ChrTalk(
        0xFE,
        (
            "You guys are going to get Mishy\x01",
            "for me, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yaaay! Thank you so much!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1203F")

    label("loc_12001")


    ChrTalk(
        0xFE,
        (
            "Waaaaah... I thought I was going to get to\x01",
            "meet Mishy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1203F")

    Jump("loc_1211F")

    label("loc_12044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_12055")
    Call(0, 34)
    Jump("loc_1211F")

    label("loc_12055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1211F")

    ChrTalk(
        0xFE,
        "Wooow, this bed is so soft and fluffy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you guys know that Daddy promised\x01",
            "me he'd buy me something I wanted?!\x01",
            "I told him I wanted the Mishy plush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sooo excited to get it!\x02",
    )

    CloseMessageWindow()

    label("loc_1211F")

    TalkEnd(0xFE)
    Return()

    # Function_35_11F38 end

    def Function_36_12123(): pass

    label("Function_36_12123")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x0, 0xA, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10960, 1400, -1150, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(25660, 0)
    SetChrPos(0x101, 11270, 0, -600, 90)
    SetChrPos(0x102, 11270, 0, -2110, 90)
    SetChrPos(0x103, 9810, 0, -600, 90)
    SetChrPos(0x104, 9810, 0, -2110, 90)
    SetChrPos(0xA, 12840, 0, -1050, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "#11PWelcome to, Long Lao!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FShanshan, I presume? We're here to\x01",
            "discuss your support request.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PWow, you're here already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11POh, thank goodness!\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#6P#0309F(Ain't she a cutie?)\x02\x03",
            "#0300FI think 'Fishing for Ingredients!' was the\x01",
            "name of your request?\x02\x03",
            "#0306FWork's work, but is it me, or does the SSS\x01",
            "get saddled with a lot of fetch requests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FYou're not wrong, but it really is\x01",
            "out of our control.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11PI dunno what you guys are talking about,\x01",
            "but I need this done as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe had a customer suddenly come in this morning\x01",
            "and make a reservation bigger than our stock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe tried to buy some fish from the marketplace,\x01",
            "but even they were running low on the good stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe're going to need odd jobbers to\x01",
            "tackle this one for us!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x101,
        "#5P#0003FSorry, what was that now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200F'Odd jobber' is an inadequate\x01",
            "description of our work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAll I know is, I spoke with the Bracer Guild\x01",
            "receptionist, and he told me he'd set\x01",
            "something up for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThere weren't any bracers available, but\x01",
            "he mentioned a group of odd jobbers\x01",
            "that would be willing to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PAren't you the ones he was referring to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306F(So it's that damn receptionist's fault, eh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F(The worst part is he's not completely\x01",
            "mistaken...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0106F(It still feels bad to hear it, though.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FHowever, Lloyd is a proficient fisherman, so\x01",
            "shall we assist her with her request?\x02\x03",
            "She appears to be in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FYeah, I think we can help you out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PReally? That's such a relief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThis dish calls for a fish that's\x01",
            "both slender and long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PThe reservation is for five people, so\x01",
            "we'll need five of the same type of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHmm... If you have trouble catching it,\x01",
            "then we could settle for something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PHowever, it definitely needs to be\x01",
            "five of the same type of fish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FTo recap, you want five long and slender fish.\x01",
            "If we fail to catch them, then you'll settle for\x01",
            "another fish, as long as they are identical.\x02\x03",
            "#0000FOkay, I think we've got it. We'll fish them up\x01",
            "and bring them to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PThank you so much! I'm counting on you!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Fishing for Ingredients!]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 9670, 30, -2060, 90)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12BC2")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_12BC2")

    OP_29(0x11, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_12123 end

    def Function_37_12BCB(): pass

    label("Function_37_12BCB")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(800)
    OP_68(10960, 1400, -1150, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(25660, 0)
    SetChrPos(0x101, 11270, 0, -600, 90)
    SetChrPos(0x102, 11270, 0, -2110, 90)
    SetChrPos(0x103, 9810, 0, -600, 90)
    SetChrPos(0x104, 9810, 0, -2110, 90)
    SetChrPos(0xA, 12840, 0, -1050, 270)
    OP_0D()
    Call(0, 41)

    ChrTalk(
        0xA,
        (
            "#11PThank you! Now we'll be able to make\x01",
            "it through the day!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D1B")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x2)

    ChrTalk(
        0xA,
        (
            "#11PYou were able to bring our usual fish, so\x01",
            "I'm sure our customers will be delighted!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E84")

    label("loc_12D1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E00")
    OP_2C(0x11, 0x5)
    OP_29(0x11, 0x1, 0x3)

    ChrTalk(
        0xA,
        (
            "#11PHmm, these aren't the usual fish we use. It's\x01",
            "a bit of a rare one, so I think Daddy will be\x01",
            "able to make an interesting dish out of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI'm sure our customers will be satisfied!\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E84")

    label("loc_12E00")

    OP_2C(0x11, 0x2)
    OP_29(0x11, 0x1, 0x4)

    ChrTalk(
        0xA,
        (
            "#11PThese fish don't fit the description I was\x01",
            "looking for, but I think Daddy can make\x01",
            "a nice sashimi out of these.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E84")


    ChrTalk(
        0xA,
        (
            "#11PHere, I'd like to give you these\x01",
            "as a thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F21")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 2)
    Jump("loc_12FD3")

    label("loc_12F21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F84")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 3)
    Jump("loc_12FD3")

    label("loc_12F84")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F4, 2)

    label("loc_12FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131BC")

    ChrTalk(
        0xA,
        (
            "#11PActually...there's a recipe I want to give you.\x01",
            "Are you interested?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x197),
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
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x3)

    ChrTalk(
        0xA,
        (
            "#11PThis is the secret recipe to our delicious fried\x01",
            "rice. We plan to make this alongside the fish\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI hope you guys use it, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FSounds good to me. We'll gladly\x01",
            "accept your offer, then.\x02\x03",
            "Good luck with tonight. We're rooting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13343")

    label("loc_131BC")


    ChrTalk(
        0xA,
        "#11POh, wait. I have one more thing to give you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x197),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x197, 1)

    ChrTalk(
        0xA,
        (
            "#11PWe have an extra one because we made\x01",
            "a mistake on someone's order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PI figured there's no point in wasting it,\x01",
            "so I'll give it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FOh, thank you. We'll take you up\x01",
            "on that offer.\x02\x03",
            "Good luck with tonight. We're rooting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13343")


    ChrTalk(
        0xA,
        "#11PYep! Thanks for your help, odd jobbers!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#5P#0012FHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106F(We weren't able to clear the misunderstanding,\x01",
            "by the looks of it...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Fishing for Ingredients!]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9670, 30, -2060, 90)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_134F7")
    SetChrPos(0xA, 4960, 0, 9080, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x10)

    label("loc_134F7")

    OP_29(0x11, 0x4, 0x10)
    SetScenarioFlags(0x2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_12BCB end

    def Function_38_13505(): pass

    label("Function_38_13505")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1352B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1352B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13547")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13547")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13563")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13563")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1357F")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1357F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1359B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1359B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_135B7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_135B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_135D3")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_135D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_135EF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_135EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1360B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1360B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13627")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13627")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13643")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13643")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1365F")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1365F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1367B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1367B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13697")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13697")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136B3")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_136B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136CF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_136CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136EB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_136EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13707")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13707")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13723")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13723")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1373F")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1373F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1375B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1375B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13777")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13777")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13793")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_13793")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_137AF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_137AF")

    Return()

    # Function_38_13505 end

    def Function_39_137B0(): pass

    label("Function_39_137B0")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13817")
    MenuCmd(1, 1, "Snow Crab")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1380D")
    Call(0, 40)

    label("loc_1380D")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13817")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13876")
    MenuCmd(1, 1, "Armorican Carp")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1386C")
    Call(0, 40)

    label("loc_1386C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13876")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_138D5")
    MenuCmd(1, 1, "Tiger Rockfish")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_138CB")
    Call(0, 40)

    label("loc_138CB")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_138D5")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1392F")
    MenuCmd(1, 1, "Rockeater")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13925")
    Call(0, 40)

    label("loc_13925")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1392F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13984")
    MenuCmd(1, 1, "Carp")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1397A")
    Call(0, 40)

    label("loc_1397A")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13984")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_139DE")
    MenuCmd(1, 1, "Raineater")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_139D4")
    Call(0, 40)

    label("loc_139D4")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_139DE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A37")
    MenuCmd(1, 1, "Azelfish")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13A2D")
    Call(0, 40)

    label("loc_13A2D")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13A37")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A8F")
    MenuCmd(1, 1, "Kasagin")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13A85")
    Call(0, 40)

    label("loc_13A85")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AED")
    MenuCmd(1, 1, "Rainbow Trout")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13AE3")
    Call(0, 40)

    label("loc_13AE3")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13AED")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B43")
    MenuCmd(1, 1, "Trout")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13B39")
    Call(0, 40)

    label("loc_13B39")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13B43")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B9A")
    MenuCmd(1, 1, "Salmon")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13B90")
    Call(0, 40)

    label("loc_13B90")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13BEE")
    MenuCmd(1, 1, "Eel")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13BE4")
    Call(0, 40)

    label("loc_13BE4")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13BEE")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13C49")
    MenuCmd(1, 1, "Pearlglass")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13C3F")
    Call(0, 40)

    label("loc_13C3F")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13C49")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13CA9")
    MenuCmd(1, 1, "Gluttonous Bass")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13C9F")
    Call(0, 40)

    label("loc_13C9F")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13CA9")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13D03")
    MenuCmd(1, 1, "Viperhead")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13CF9")
    Call(0, 40)

    label("loc_13CF9")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13D03")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13D5E")
    MenuCmd(1, 1, "Pythonhead")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13D54")
    Call(0, 40)

    label("loc_13D54")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13DB6")
    MenuCmd(1, 1, "Catfish")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13DAC")
    Call(0, 40)

    label("loc_13DAC")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E11")
    MenuCmd(1, 1, "Queen Crab")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13E07")
    Call(0, 40)

    label("loc_13E07")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13E11")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E6E")
    MenuCmd(1, 1, "Electric Eel")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13E64")
    Call(0, 40)

    label("loc_13E64")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13ECC")
    MenuCmd(1, 1, "Demon Catfish")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13EC2")
    Call(0, 40)

    label("loc_13EC2")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F26")
    MenuCmd(1, 1, "Arch Crab")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13F1C")
    Call(0, 40)

    label("loc_13F1C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13F26")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F82")
    MenuCmd(1, 1, "Gold Salmon")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13F78")
    Call(0, 40)

    label("loc_13F78")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13F82")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13FDD")
    MenuCmd(1, 1, "Noble Carp")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13FD3")
    Call(0, 40)

    label("loc_13FD3")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14039")
    MenuCmd(1, 1, "Serpenthead")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1402F")
    Call(0, 40)

    label("loc_1402F")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14039")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x1)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14080")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_14080")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_140C8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_140C8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14110")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14110")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14158")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14158")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141A0")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_141A0")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141E8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_141E8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14230")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14230")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14278")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14278")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142C0")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_142C0")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14308")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14308")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14350")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14350")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14398")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14398")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_143E0")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_143E0")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14428")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14428")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14470")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14470")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144B8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_144B8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14500")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14500")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14548")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14548")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14590")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14590")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145D8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145D8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14620")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14620")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14668")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14668")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_146B0")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_146B0")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_146F8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_146F8")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14740")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14740")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_137B0 end

    def Function_40_1474F(): pass

    label("Function_40_1474F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14767")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1498A")

    label("loc_14767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1477F")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1498A")

    label("loc_1477F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14797")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1498A")

    label("loc_14797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147AF")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1498A")

    label("loc_147AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147C7")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1498A")

    label("loc_147C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147DF")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1498A")

    label("loc_147DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147F7")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1498A")

    label("loc_147F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1480F")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1498A")

    label("loc_1480F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14827")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1498A")

    label("loc_14827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1483F")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1498A")

    label("loc_1483F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14857")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1498A")

    label("loc_14857")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1486F")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1498A")

    label("loc_1486F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14887")
    MenuCmd(3, 1, 0xC)
    Jump("loc_1498A")

    label("loc_14887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1489F")
    MenuCmd(3, 1, 0xD)
    Jump("loc_1498A")

    label("loc_1489F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148B7")
    MenuCmd(3, 1, 0xE)
    Jump("loc_1498A")

    label("loc_148B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148CF")
    MenuCmd(3, 1, 0xF)
    Jump("loc_1498A")

    label("loc_148CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148E7")
    MenuCmd(3, 1, 0x10)
    Jump("loc_1498A")

    label("loc_148E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148FF")
    MenuCmd(3, 1, 0x11)
    Jump("loc_1498A")

    label("loc_148FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14917")
    MenuCmd(3, 1, 0x12)
    Jump("loc_1498A")

    label("loc_14917")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1492F")
    MenuCmd(3, 1, 0x13)
    Jump("loc_1498A")

    label("loc_1492F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14947")
    MenuCmd(3, 1, 0x14)
    Jump("loc_1498A")

    label("loc_14947")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1495F")
    MenuCmd(3, 1, 0x15)
    Jump("loc_1498A")

    label("loc_1495F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14977")
    MenuCmd(3, 1, 0x16)
    Jump("loc_1498A")

    label("loc_14977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1498A")
    MenuCmd(3, 1, 0x17)

    label("loc_1498A")

    Return()

    # Function_40_1474F end

    def Function_41_1498B(): pass

    label("Function_41_1498B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x175), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149A4")
    SubItemNumber(0x175, 5)
    Jump("loc_14BDE")

    label("loc_149A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x174), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149BD")
    SubItemNumber(0x174, 5)
    Jump("loc_14BDE")

    label("loc_149BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x173), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149D6")
    SubItemNumber(0x173, 5)
    Jump("loc_14BDE")

    label("loc_149D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x172), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149EF")
    SubItemNumber(0x172, 5)
    Jump("loc_14BDE")

    label("loc_149EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x171), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A08")
    SubItemNumber(0x171, 5)
    Jump("loc_14BDE")

    label("loc_14A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A21")
    SubItemNumber(0x170, 5)
    Jump("loc_14BDE")

    label("loc_14A21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A3A")
    SubItemNumber(0x16F, 5)
    Jump("loc_14BDE")

    label("loc_14A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A53")
    SubItemNumber(0x16E, 5)
    Jump("loc_14BDE")

    label("loc_14A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A6C")
    SubItemNumber(0x16D, 5)
    Jump("loc_14BDE")

    label("loc_14A6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A85")
    SubItemNumber(0x16C, 5)
    Jump("loc_14BDE")

    label("loc_14A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A9E")
    SubItemNumber(0x16B, 5)
    Jump("loc_14BDE")

    label("loc_14A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB7")
    SubItemNumber(0x16A, 5)
    Jump("loc_14BDE")

    label("loc_14AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x169), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AD0")
    SubItemNumber(0x169, 5)
    Jump("loc_14BDE")

    label("loc_14AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE9")
    SubItemNumber(0x168, 5)
    Jump("loc_14BDE")

    label("loc_14AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x167), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B02")
    SubItemNumber(0x167, 5)
    Jump("loc_14BDE")

    label("loc_14B02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x166), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B1B")
    SubItemNumber(0x166, 5)
    Jump("loc_14BDE")

    label("loc_14B1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x165), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B34")
    SubItemNumber(0x165, 5)
    Jump("loc_14BDE")

    label("loc_14B34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B4D")
    SubItemNumber(0x164, 5)
    Jump("loc_14BDE")

    label("loc_14B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x163), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B66")
    SubItemNumber(0x163, 5)
    Jump("loc_14BDE")

    label("loc_14B66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B7F")
    SubItemNumber(0x162, 5)
    Jump("loc_14BDE")

    label("loc_14B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B98")
    SubItemNumber(0x161, 5)
    Jump("loc_14BDE")

    label("loc_14B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BB1")
    SubItemNumber(0x160, 5)
    Jump("loc_14BDE")

    label("loc_14BB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BCA")
    SubItemNumber(0x15F, 5)
    Jump("loc_14BDE")

    label("loc_14BCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BDE")
    SubItemNumber(0x15E, 5)

    label("loc_14BDE")

    Return()

    # Function_41_1498B end

    def Function_42_14BDF(): pass

    label("Function_42_14BDF")

    OP_25(0x33B, 0x0)
    Sleep(80)
    OP_25(0x33B, 0xA)
    Sleep(80)
    OP_25(0x33B, 0x14)
    Sleep(80)
    OP_25(0x33B, 0x1E)
    Sleep(80)
    OP_25(0x33B, 0x28)
    Sleep(80)
    OP_25(0x33B, 0x32)
    Sleep(80)
    OP_25(0x33B, 0x3C)
    Sleep(80)
    OP_25(0x33B, 0x46)
    Sleep(80)
    OP_25(0x33B, 0x50)
    Sleep(80)
    OP_25(0x33B, 0x5A)
    Sleep(80)
    OP_25(0x33B, 0x64)
    Return()

    # Function_42_14BDF end

    def Function_43_14C2A(): pass

    label("Function_43_14C2A")

    OP_25(0x33B, 0x64)
    Sleep(80)
    OP_25(0x33B, 0x5A)
    Sleep(80)
    OP_25(0x33B, 0x50)
    Sleep(80)
    OP_25(0x33B, 0x46)
    Sleep(80)
    OP_25(0x33B, 0x3C)
    Sleep(80)
    OP_25(0x33B, 0x32)
    Sleep(80)
    OP_25(0x33B, 0x28)
    Sleep(80)
    OP_25(0x33B, 0x1E)
    Sleep(80)
    OP_25(0x33B, 0x14)
    Sleep(80)
    OP_25(0x33B, 0xA)
    Sleep(80)
    OP_25(0x33B, 0x0)
    OP_24(0x33B)
    Return()

    # Function_43_14C2A end

    SaveToFile()

Try(main)
