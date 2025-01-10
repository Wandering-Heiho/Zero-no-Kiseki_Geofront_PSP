from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0120.bin",                # FileName
        "r0120",                    # MapName
        "r0120",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0120", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 3, 0, 4],
    )

    BuildStringList((
        "r0120",                  # 0
        "車",                     # 1
        "Alfred",                 # 2
        "Beetle Hunter",          # 3
        "bm0110",                 # 4
        "br0100",                 # 5
        "br0100",                 # 6
        "br0100",                 # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "To Crossbell City & Tangram Gate",# 12
        "To Armorica Village",    # 13
        "To Ancient Battlefield", # 14
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_B4", 0,   2,   0,   7,   3,   5,   0)
    Sepith("Sepith_C4", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_D4", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_E4", 1,   7,   0,   3,   0,   1,   5)
    Sepith("Sepith_F4", 34,  15,  25,  15,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_104", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_130", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_134", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_144", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 2, 13, 180)

    # monster count: 17

    BattleInfo(
        "BattleInfo_164", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms61800.dat", "ms62200.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_22C", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_B4", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2C8", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_C4", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_364", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_400", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_E4", 30, 45, 25, 5,
        (
            ("ms64500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms64500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4C8", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_564", 0x0000, 10, 6, 45, 0, 1, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch64550.itc",               # 18
        "monster/ch64551.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(11039,   3009,    77480,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-25709,  2000,    168059,  0,    484,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-31520,  37060,   3000,    0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-50480,  40250,   1000,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-6300,   63280,   3000,    0x1010000,    "BattleInfo_2C8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-10530,  85710,   3000,    0x1010000,    "BattleInfo_364", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-51040,  94660,   2000,    0x1010000,    "BattleInfo_400", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-56360,  74870,   2000,    0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-40900,  149790,  2009,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-17280,  116460,  2000,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21030,  137120,  1000,    0x1010000,    "BattleInfo_2C8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-60400,  152360,  2000,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-77600,  151590,  1500,    0x1010000,    "BattleInfo_400", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(40390,   71780,   5000,    0x1010000,    "BattleInfo_164", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(77400,   80820,   9000,    0x1010000,    "BattleInfo_22C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(72370,   108020,  9000,    0x1010000,    "BattleInfo_2C8", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-23200,  48960,   3000,    0x1010000,    "BattleInfo_4C8", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-46680,  101000,  2000,    0x1010000,    "BattleInfo_4C8", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-72140,  162220,  2710,    0x1010000,    "BattleInfo_4C8", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 15,  16.0,                  76.0,                  2.5,                   64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -8.0,                  -9.5,                  -0.5,                  1.0])

    DeclActor(-49820,  1000,    48270,   1200,    -49820,  2000,    48270,   0x007C, 0,  5,  0x0000)
    DeclActor(-55330,  2000,    72560,   1200,    -55330,  3000,    72560,   0x007C, 0,  6,  0x0000)
    DeclActor(-25710,  1000,    168060,  1200,    -25710,  2000,    168060,  0x007C, 0,  7,  0x0000)
    DeclActor(86490,   9000,    96960,   1200,    86490,   10000,   96960,   0x007C, 0,  8,  0x0000)
    DeclActor(39750,   5000,    90020,   1200,    39750,   6000,    90020,   0x007C, 0,  9,  0x0000)
    DeclActor(-79110,  1500,    147760,  1200,    -79110,  2500,    147760,  0x007C, 0,  10, 0x0000)
    DeclActor(7820,    3000,    74900,   1200,    7820,    4500,    74900,   0x007C, 0,  16, 0x0000)
    DeclActor(-41000,  1750,    29960,   1200,    -41000,  1750,    29960,   0x007C, 0,  11, 0x0000)
    DeclActor(-61320,  2040,    165270,  1500,    -61320,  3740,    165270,  0x007C, 0,  17, 0x0000)

    PlaceName(-2.0, 0.0, -22.0, 0x0000, 0x0000, "To Crossbell City & Tangram Gate")
    PlaceName(-95.0, 0.0, 210.0, 0x0000, 0x0000, "To Armorica Village")
    PlaceName(128.0, 0.0, 122.0, 0x0000, 0x0000, "To Ancient Battlefield")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_B60",          # 00, 0
        "Function_1_C18",          # 01, 1
        "Function_2_C34",          # 02, 2
        "Function_3_CA0",          # 03, 3
        "Function_4_D02",          # 04, 4
        "Function_5_173C",         # 05, 5
        "Function_6_189C",         # 06, 6
        "Function_7_1A1F",         # 07, 7
        "Function_8_1C54",         # 08, 8
        "Function_9_1DFE",         # 09, 9
        "Function_10_1F99",        # 0A, 10
        "Function_11_2118",        # 0B, 11
        "Function_12_212C",        # 0C, 12
        "Function_13_214A",        # 0D, 13
        "Function_14_22E8",        # 0E, 14
        "Function_15_24B1",        # 0F, 15
        "Function_16_25BE",        # 10, 16
        "Function_17_2680",        # 11, 17
    ))


    def Function_0_B60(): pass

    label("Function_0_B60")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BA0"),
        (1, "loc_BAC"),
        (2, "loc_BB8"),
        (3, "loc_BC4"),
        (4, "loc_BD0"),
        (5, "loc_BDC"),
        (6, "loc_BE8"),
        (SWITCH_DEFAULT, "loc_BF4"),
    )


    label("loc_BA0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BAC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BB8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BC4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BD0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BDC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BE8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_BF4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_C00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C17")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C00")

    label("loc_C17")

    Return()

    # Function_0_B60 end

    def Function_1_C18(): pass

    label("Function_1_C18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C33")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_C18")

    label("loc_C33")

    Return()

    # Function_1_C18 end

    def Function_2_C34(): pass

    label("Function_2_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_END)), "loc_C9F")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C9F")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sleep(2000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    ClearScenarioFlags(0xBA, 1)
    Jump("loc_C9F")

    label("loc_C9F")

    Return()

    # Function_2_C34 end

    def Function_3_CA0(): pass

    label("Function_3_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CB2")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 14)

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CD1")
    Jump("loc_CFE")

    label("loc_CD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_CE8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_CFE")

    label("loc_CE8")

    SetChrPos(0x9, 10370, 3000, 75310, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_CFE")

    Call(0, 12)
    Return()

    # Function_3_CA0 end

    def Function_4_D02(): pass

    label("Function_4_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D19")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D19")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 7800, 3010, 75130, 20000, 2000, 90000)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DCE")
    SetMapObjFrame(0xFF, "bridge_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bridge_after", 0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D93")
    ClearMapObjFlags(0x7, 0x4)
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x6, 0x1)

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DB2")
    Jump("loc_DC9")

    label("loc_DB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_DC4")
    Jump("loc_DC9")

    label("loc_DC4")

    ModifyEventFlags(1, 0, 0x80)

    label("loc_DC9")

    Jump("loc_DFB")

    label("loc_DCE")

    SetMapObjFrame(0xFF, "bridge_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bridge_after", 0x0, 0x1)
    SetBarrier(0x3, 0x0, 0x1)

    label("loc_DFB")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1320")
    OP_70(0x0, 0x0)
    Jump("loc_1324")

    label("loc_1320")

    OP_70(0x0, 0x1E)

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1337")
    OP_70(0x1, 0x0)
    Jump("loc_133B")

    label("loc_1337")

    OP_70(0x1, 0x1E)

    label("loc_133B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")
    OP_70(0x2, 0x0)
    Jump("loc_1352")

    label("loc_134E")

    OP_70(0x2, 0x1E)

    label("loc_1352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1365")
    OP_70(0x3, 0x0)
    Jump("loc_1369")

    label("loc_1365")

    OP_70(0x3, 0x1E)

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C")
    OP_70(0x4, 0x0)
    Jump("loc_1380")

    label("loc_137C")

    OP_70(0x4, 0x1E)

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1393")
    OP_70(0x5, 0x0)
    Jump("loc_1397")

    label("loc_1393")

    OP_70(0x5, 0x1E)

    label("loc_1397")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 4)), scpexpr(EXPR_END)), "loc_13F4")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -41000, 1750, 29960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_13F4")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0xB, 0, 0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_168A")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1469")
    SetScenarioFlags(0x7A, 0)

    label("loc_1469")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147F")
    SetScenarioFlags(0x7A, 1)

    label("loc_147F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1495")
    SetScenarioFlags(0x7A, 2)

    label("loc_1495")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB")
    SetScenarioFlags(0x7A, 3)

    label("loc_14AB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C1")
    SetScenarioFlags(0x7A, 4)

    label("loc_14C1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D7")
    SetScenarioFlags(0x7A, 5)

    label("loc_14D7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14ED")
    SetScenarioFlags(0x7A, 6)

    label("loc_14ED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1503")
    SetScenarioFlags(0x7A, 7)

    label("loc_1503")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1519")
    SetScenarioFlags(0x7B, 0)

    label("loc_1519")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152F")
    SetScenarioFlags(0x7B, 1)

    label("loc_152F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1545")
    SetScenarioFlags(0x7B, 2)

    label("loc_1545")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155B")
    SetScenarioFlags(0x7B, 3)

    label("loc_155B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1571")
    SetScenarioFlags(0x7B, 4)

    label("loc_1571")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1587")
    SetScenarioFlags(0x7B, 5)

    label("loc_1587")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")
    SetScenarioFlags(0x7B, 6)

    label("loc_159D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")
    SetScenarioFlags(0x7B, 7)

    label("loc_15B3")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_168A")

    label("loc_15EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1605")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_168A")

    label("loc_1605")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_168A")

    label("loc_161C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1633")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_168A")

    label("loc_1633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164A")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_168A")

    label("loc_164A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1661")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_168A")

    label("loc_1661")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1678")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_168A")

    label("loc_1678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168A")
    SetScenarioFlags(0x7C, 7)

    label("loc_168A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_169B")
    OP_24(0x7B)
    Jump("loc_172C")

    label("loc_169B")

    SoundDistance(0x7B, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E1(0xD8EA, 0x5DC, 0xFFFFC8F6)
    OP_E1(0x45D8, 0x5DC, 0x140DC)
    OP_E1(0xFFFFAAB0, 0x7D0, 0x190D2)
    OP_E1(0xFFFF633E, 0x5DC, 0x1C840)
    OP_E1(0xFFFF650A, 0x5DC, 0x20364)
    OP_E1(0xFFFF650A, 0x5DC, 0x20364)
    OP_E1(0xFFFF8BFC, 0x7D0, 0x23870)
    OP_E1(0xFFFF84F4, 0x7D0, 0x2698A)
    OP_E1(0xFFFE762C, 0x7D0, 0x38400)

    label("loc_172C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173B")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_173B")

    Return()

    # Function_4_D02 end

    def Function_5_173C(): pass

    label("Function_5_173C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1826")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_17BC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1821")

    label("loc_17BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1821")

    Jump("loc_1890")

    label("loc_1826")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What is Zemuria's favorite brand of popcorn?\x01",
            "Orbal Redenbacher.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1890")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_173C end

    def Function_6_189C(): pass

    label("Function_6_189C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x20\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x20.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x103, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1A0D")

    label("loc_19D0")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I hope your pockets are now Lloyded with sepith.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1A0D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_189C end

    def Function_7_1A1F(): pass

    label("Function_7_1A1F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDE")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1E")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A78():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A78)

    def lambda_1A92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A92)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_564", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1AFF"),
        (2, "loc_1B0E"),
        (1, "loc_1B1B"),
        (SWITCH_DEFAULT, "loc_1B1E"),
    )


    label("loc_1AFF")

    SetScenarioFlags(0x74, 0)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1B1E")

    label("loc_1B0E")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B1B")

    OP_B7(0x0)
    Return()

    label("loc_1B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6B, 1)"), scpexpr(EXPR_END)), "loc_1B76")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x6B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1BD9")

    label("loc_1B76")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x6B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BD9")

    Jump("loc_1C48")

    label("loc_1BDE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'd put a joke about law enforcement here,\x01",
            "but it'd be a bit of a cop-out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1C48")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1A1F end

    def Function_8_1C54(): pass

    label("Function_8_1C54")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3E")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1CD4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1D39")

    label("loc_1CD4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D39")

    Jump("loc_1DF2")

    label("loc_1D3E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Back in my day, we had to work HARD for our\x01",
            "curia balms. And we definitely wouldn't have 99\x01",
            "of them in our second playthrough. No, siree.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1DF2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1C54 end

    def Function_9_1DFE(): pass

    label("Function_9_1DFE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE8")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_1E7E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1EE3")

    label("loc_1E7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1EE3")

    Jump("loc_1F8D")

    label("loc_1EE8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are some...peculiar magazines inside the\x01",
            "chest. You decide to leave them where they are,\x01",
            "despite Randy's protests...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1F8D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1DFE end

    def Function_10_1F99(): pass

    label("Function_10_1F99")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2083")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_2019")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_207E")

    label("loc_2019")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_207E")

    Jump("loc_210C")

    label("loc_2083")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that string of chest thefts in Liberl, you\x01",
            "would think they'd have some locks installed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_210C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1F99 end

    def Function_11_2118(): pass

    label("Function_11_2118")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 4)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_11_2118 end

    def Function_12_212C(): pass

    label("Function_12_212C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2149")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_2149")

    Return()

    # Function_12_212C end

    def Function_13_214A(): pass

    label("Function_13_214A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_215E")
    Jump("loc_22E4")

    label("loc_215E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_22B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21CD")

    ChrTalk(
        0x9,
        (
            "Please assist that bracer in\x01",
            "finding those tourists!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm counting on you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B3")

    label("loc_21CD")


    ChrTalk(
        0x9,
        "Aren't you the Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A bracer just came here to look\x01",
            "for the missing tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You must have heard the news and\x01",
            "came to provide backup, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Can you please assist him in\x01",
            "locating them?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22B3")

    Jump("loc_22E4")

    label("loc_22B8")


    ChrTalk(
        0x9,
        (
            "Hmm... They must have gone\x01",
            "further in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E4")

    TalkEnd(0xFE)
    Return()

    # Function_13_214A end

    def Function_14_22E8(): pass

    label("Function_14_22E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-46600, 3000, 158700, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0x8)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -66000, 2000, 159000, 90)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x0, 0x20)
    Sound(457, 0, 100, 0)
    Sleep(1000)
    OP_6B(0x8)
    Sleep(200)

    def lambda_2394():
        OP_95(0xFE, -49200, 2000, 159000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2394)
    PlayBGM("ed7105", 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_23BF():
        OP_9E(0xFE, 0xFFFF3FD0, 0x24608, 0x1FBD0, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_23BF)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)
    Fade(1000)
    OP_6B(0xFF)
    OP_68(-45980, 3000, 133440, 0)
    MoveCamera(39, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36500, 0)
    OP_68(-45980, 0, 133440, 4000)
    Sound(458, 0, 100, 0)

    def lambda_242F():
        OP_95(0xFE, -48000, 2000, 135200, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_242F)
    Sleep(1260)

    def lambda_244C():
        OP_9E(0xFE, 0xFFFF6B90, 0x1E910, 0xFFFF5038, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_244C)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)

    def lambda_246F():
        OP_95(0xFE, -52000, 2000, 109000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_246F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x8, 0x1)
    Sleep(3000)
    ClearScenarioFlags(0x0, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("e0310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_22E8 end

    def Function_15_24B1(): pass

    label("Function_15_24B1")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        "Just a moment, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Beyond here is the Ancient Battlefield.\x01",
            "Monsters have turned it into their nest,\x01",
            "so it's currently off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I apologize, but unauthorized individuals\x01",
            "may not proceed any further.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_93(0x9, 0x10E, 0x0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 6820, 3010, 75770, 270)
    EventEnd(0x4)
    Return()

    # Function_15_24B1 end

    def Function_16_25BE(): pass

    label("Function_16_25BE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Danger: The ruins of the Ancient Battlefield\x01",
            "lie beyond here. Entry is strictly prohibited.\x01",
            "                          - Management Bureau\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_25BE end

    def Function_17_2680(): pass

    label("Function_17_2680")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Northwest: Armorica Village\x01",
            "South: Crossbell City - 274 selge\x01",
            "       Tangram Gate - 232 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2680 end

    SaveToFile()

Try(main)
