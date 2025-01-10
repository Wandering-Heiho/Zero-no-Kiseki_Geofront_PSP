from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2060.bin",                # FileName
        "r2060",                    # MapName
        "r2060",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2060", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2060",                  # 0
        "Zeit",                   # 1
        "br2060",                 # 2
        "br2060",                 # 3
        "br2060",                 # 4
        "br2060",                 # 5
        "To Crossbell City",      # 6
        "To Mainz Mining Village",# 7
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   9,   3,   1,   5,   5,   0)
    Sepith("Sepith_B4", 0,   0,   0,   6,   6,   6,   6)
    Sepith("Sepith_C4", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_D4", 14,  4,   9,   5,   7,   12,  9)

    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_110", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_114", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_11C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 2, 13, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_144", 0x0000, 14, 6, 45, 10, 1, 50, 0, "br2060", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms64400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64400.dat", "ms64400.dat", "ms64400.dat", "ms64400.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_20C", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2060", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2D4", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2060", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_39C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2060", "Sepith_D4", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch64450.itc",               # 14
        "monster/ch64450.itc",               # 15
        "monster/ch76050.itc",               # 16
        "monster/ch76051.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(690,     27940,   0,       0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-39910,  61380,   0,       0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-42170,  79460,   0,       0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(350,     141340,  0,       0x1010000,    "BattleInfo_20C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5600,    124460,  0,       0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(23790,   135160,  0,       0x1010000,    "BattleInfo_2D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-23150,  170010,  7400,    0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(15210,   144180,  6000,    0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(12090,   156500,  10000,   0x1010000,    "BattleInfo_20C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-39940,  194050,  8000,    0x1010000,    "BattleInfo_20C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-13710,  39330,   0,       0x1010000,    "BattleInfo_39C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-32470,  88800,   0,       0x1010000,    "BattleInfo_39C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-20640,  138730,  0,       0x1010000,    "BattleInfo_39C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(14120,   125230,  0,       0x1010000,    "BattleInfo_39C", 0,   22,  0xFFFF, 6,  7)

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  2,  0x0000)
    DeclActor(-20040,  8000,    199730,  1200,    -20040,  9500,    199730,  0x007C, 0,  12, 0x0000)
    DeclActor(-44060,  0,       71300,   1200,    -44060,  0,       71300,   0x007C, 0,  3,  0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "To Mainz Mining Village")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_A34",          # 01, 1
        "Function_2_DAD",          # 02, 2
        "Function_3_F62",          # 03, 3
        "Function_4_F76",          # 04, 4
        "Function_5_F99",          # 05, 5
        "Function_6_3155",         # 06, 6
        "Function_7_3200",         # 07, 7
        "Function_8_3230",         # 08, 8
        "Function_9_324C",         # 09, 9
        "Function_10_32B7",        # 0A, 10
        "Function_11_33D7",        # 0B, 11
        "Function_12_3401",        # 0C, 12
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B2")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_7B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A30")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F")
    SetScenarioFlags(0x7A, 0)

    label("loc_80F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825")
    SetScenarioFlags(0x7A, 1)

    label("loc_825")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    SetScenarioFlags(0x7A, 2)

    label("loc_83B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    SetScenarioFlags(0x7A, 3)

    label("loc_851")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_867")
    SetScenarioFlags(0x7A, 4)

    label("loc_867")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87D")
    SetScenarioFlags(0x7A, 5)

    label("loc_87D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_893")
    SetScenarioFlags(0x7A, 6)

    label("loc_893")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9")
    SetScenarioFlags(0x7A, 7)

    label("loc_8A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF")
    SetScenarioFlags(0x7B, 0)

    label("loc_8BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D5")
    SetScenarioFlags(0x7B, 1)

    label("loc_8D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EB")
    SetScenarioFlags(0x7B, 2)

    label("loc_8EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_901")
    SetScenarioFlags(0x7B, 3)

    label("loc_901")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_917")
    SetScenarioFlags(0x7B, 4)

    label("loc_917")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    SetScenarioFlags(0x7B, 5)

    label("loc_92D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943")
    SetScenarioFlags(0x7B, 6)

    label("loc_943")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_959")
    SetScenarioFlags(0x7B, 7)

    label("loc_959")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_A30")

    label("loc_994")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AB")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_A30")

    label("loc_9AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_A30")

    label("loc_9C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D9")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_A30")

    label("loc_9D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F0")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_A30")

    label("loc_9F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A07")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_A30")

    label("loc_A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1E")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_A30")

    label("loc_A1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    SetScenarioFlags(0x7C, 7)

    label("loc_A30")

    Call(0, 4)
    Return()

    # Function_0_79C end

    def Function_1_A34(): pass

    label("Function_1_A34")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4B")
    OP_70(0x0, 0x0)
    Jump("loc_D4F")

    label("loc_D4B")

    OP_70(0x0, 0x1E)

    label("loc_D4F")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 3)), scpexpr(EXPR_END)), "loc_DAC")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -44060, 0, 71300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_DAC")

    Return()

    # Function_1_A34 end

    def Function_2_DAD(): pass

    label("Function_2_DAD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E97")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E2D")
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
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_E92")

    label("loc_E2D")

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

    label("loc_E92")

    Jump("loc_F56")

    label("loc_E97")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Your investigation into the theft of this chest comes\x01",
            "up empty, much like the chest itself. You conveniently\x01",
            "ignore the fact that you are the thief.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F56")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_DAD end

    def Function_3_F62(): pass

    label("Function_3_F62")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_F62 end

    def Function_4_F76(): pass

    label("Function_4_F76")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F98")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_F98")

    Return()

    # Function_4_F76 end

    def Function_5_F99(): pass

    label("Function_5_F99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch02600.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00351.itc", 0x22)
    LoadChrToIndex("chr/ch02651.itc", 0x23)
    LoadChrToIndex("chr/ch02602.itc", 0x24)
    OP_68(340, 1000, 3460, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23550, 0)
    SetChrPos(0x101, -60, 0, 2870, 0)
    SetChrPos(0x102, 1300, 0, 2029, 0)
    SetChrPos(0x103, -630, 0, 1060, 0)
    SetChrPos(0x104, 220, 0, 180, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    FadeToBright(1000, 0)
    OP_68(-60, 1000, 6310, 4000)

    def lambda_108D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_108D)

    def lambda_10A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A2)

    def lambda_10B7():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10B7)

    def lambda_10CC():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10CC)
    Sleep(3000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(1500, 900, 17380, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24640, 0)
    OP_68(1680, 900, 20780, 3000)
    SetChrPos(0x101, -650, 0, 12520, 0)
    SetChrPos(0x102, 830, 0, 10910, 0)
    SetChrPos(0x103, -720, 0, 10890, 0)
    SetChrPos(0x104, 830, 0, 12550, 0)

    def lambda_117D():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117D)

    def lambda_1197():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1197)

    def lambda_11B1():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11B1)

    def lambda_11CB():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11CB)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 11)
    SetChrPos(0x8, 7000, 3900, 32000, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200376V#0007F#11PHey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200377V#0101FThere it is!\x02",
    )

    CloseMessageWindow()
    OP_68(6950, 4600, 31420, 2000)
    SetCameraDistance(18070, 2000)
    OP_6F(0x11)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("White Wolf")
    Sound(2055, 255, 90, 0)

    AnonymousTalk(
        0xFF,
        "#1200378VGrrrr...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    EndChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 3, 0, 6)
    Sleep(650)
    Fade(1000)
    OP_68(-360, 600, 25160, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)

    def lambda_13FB():
        OP_95(0xFE, -1720, 0, 23100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13FB)

    def lambda_1415():
        OP_95(0xFE, 260, 0, 21430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1415)

    def lambda_142F():
        OP_95(0xFE, -1490, 0, 21240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_142F)

    def lambda_1449():
        OP_95(0xFE, 70, 0, 23420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1449)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 3)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#1200379V#0013F#12PStay on guard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200380V#0101F#11PThat streak of white fur... It's just\x01",
            "like the legendary divine wolf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200381V#0304F#11PWhoa... Finally decided to\x01",
            "come out and play, eh?!\x02\x03",
            "#1200382V#0307FNo way you're getting away now!\x01",
            "C'mon, let's hurry and neutr--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200383V#0205F#12PWait a moment, please.\x02\x03",
            "#1200384VI do not sense any hostility.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_164E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_164E)

    def lambda_165B():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_165B)
    Sleep(50)

    def lambda_166B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_166B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#1200385V#0305F#5PYeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200386V#0201F#12PI will handle this.\x02",
    )

    CloseMessageWindow()

    def lambda_16CD():

        label("loc_16CD")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_16CD")

    QueueWorkItem2(0x101, 1, lambda_16CD)

    def lambda_16DF():

        label("loc_16DF")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_16DF")

    QueueWorkItem2(0x102, 1, lambda_16DF)

    def lambda_16F1():

        label("loc_16F1")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_16F1")

    QueueWorkItem2(0x104, 1, lambda_16F1)
    OP_68(-480, 600, 26430, 4000)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1200387V#0007F#5PW-Wait, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200388V#0307F#11PYou outta your mind?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    ChrTalk(
        0x103,
        "#1200389V#0204F#5PCalm down. I will be fine.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White Wolf",
        "#1200390V#5412F#5P#30W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200391V#0204F#12PWe finally meet.\x02\x03",
            "#1200392V#0202FI feel as though you have been\x01",
            "seeking us.\x02\x03",
            "#1200393VIs there perhaps a message\x01",
            "you wished to relay?\x02",
        )
    )

    CloseMessageWindow()
    Sound(2053, 255, 90, 0)

    NpcTalk(
        0x8,
        "White Wolf",
        "#1200394V#5412F#5P#30WGrrrrr...grrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200395V#0203F#12PIs that so? My hypothesis\x01",
            "was essentially correct, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200396V#0105FT-Tio?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200397V#0005F#12PYou can UNDERSTAND it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200398V#0204F#12PMore or less.\x02\x03",
            "#1200399V#0201FWhat is your message?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "White Wolf",
        (
            "#1200400V#5412F#5P#30WGrrrrrrr... Woof...\x02\x03",
            "#1200401VGrrr...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1200402V#0205F#12POh, that means...\x02",
    )

    CloseMessageWindow()

    def lambda_1A35():

        label("loc_1A35")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_1A35")

    QueueWorkItem2(0x101, 1, lambda_1A35)

    def lambda_1A47():

        label("loc_1A47")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_1A47")

    QueueWorkItem2(0x102, 1, lambda_1A47)

    def lambda_1A59():

        label("loc_1A59")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_1A59")

    QueueWorkItem2(0x103, 1, lambda_1A59)

    def lambda_1A6B():

        label("loc_1A6B")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_1A6B")

    QueueWorkItem2(0x104, 1, lambda_1A6B)
    EndChrThread(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    Sound(2060, 255, 100, 0)
    Sleep(1700)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    Sleep(800)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    BeginChrThread(0x8, 3, 0, 10)
    Fade(500)
    OP_68(-4830, 5800, 20720, 0)
    MoveCamera(54, 10, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21420, 0)
    OP_68(-4830, 12100, 20720, 5000)

    ChrTalk(
        0x102,
        "#1200404V#0105F#5P#10ANo...!\x02",
    )

    Sleep(2000)

    ChrTalk(
        0x101,
        "#1200405V#0011F#5P#12ACrap, he's escaping!\x02",
    )

    Sleep(2400)

    ChrTalk(
        0x104,
        (
            "#1200406V#0307F#5P#14ASheesh. He's like a friggin'\x01",
            "mountain goat!\x02",
        )
    )

    Sleep(2800)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    OP_5A()
    Fade(1000)
    OP_68(-480, 600, 26430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(390, 600, 25160, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x103,
        "#1200407V#0205F#6P...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()

    def lambda_1CB8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CB8)

    def lambda_1CC5():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CC5)
    Sleep(50)

    def lambda_1CD5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CD5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200408V#0001F#12PWhat did he say, Tio?\x02\x03",
            "#1200409VIt definitely seemed like he was\x01",
            "trying to tell us something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1200410V#0206F#5PUmm... I could only piece it together\x01",
            "from his nuances...\x02\x03",
            "#1200411V#0201F'The final fragment lies ahead...'\x02\x03",
            "#1200412V'The rest is in your hands...'\x02\x03",
            "#1200413V...That should be it.\x02",
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
        0x101,
        "#1200414V#0005F#12PThe final fragment...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200415V#0203F#5PIndeed. That is as much as\x01",
            "I could understand.\x02\x03",
            "#1200416V#0200FWhether we decide to believe him\x01",
            "or not is our decision, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200417V#0006F#12PWell, yeah. That goes without saying.\x02\x03",
            "#1200418V#0008F'The final fragment lies ahead...'\x02\x03",
            "#1200419V#0001FIn other words, are we near the\x01",
            "last piece of info we need about\x01",
            "the attacks?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#1200420V#0105F#11PW-Wait a minute.\x02\x03",
            "#1200421V#0101FLet's assume Tio's interpretation\x01",
            "is, in fact, true...\x02\x03",
            "#1200422V...is it really fine to believe that wolf\x01",
            "without any supporting evidence?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#1200423V#0301F#11PFair point. He and his friends are the\x01",
            "perps behind the attack, yeah?\x02\x03",
            "#1200424VWho gives a hoot if they're intelligent?\x01",
            "They're probably tryin' to throw us for\x01",
            "a loop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200425V#0003F#6PNo, I disagree.\x02\x03",
            "#1200426V#0000FI'm fairly positive that wolf isn't\x01",
            "one of our culprits.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1200427V#0105F#11PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200428V#0305F#11PYou serious?! What makes\x01",
            "you think that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200429V#0000F#6PWell, something stood out to me...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhy was that wolf not the culprit?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The howl]\x01",                      # 0
            "[The appearance]\x01",                # 1
            "[Both howl and appearance]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23C8"),
        (1, "loc_259B"),
        (2, "loc_2794"),
        (SWITCH_DEFAULT, "loc_290E"),
    )


    label("loc_23C8")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200430V#0000F#6PAccording to testimonies at Armorica\x01",
            "and St. Ursula...\x02\x03",
            "#1200431V...there were no mentions of any\x01",
            "howling on the night of the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200444V#0101F#11PN-Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200433V#0203F#5PFurthermore, according to Lytton's\x01",
            "statement...\x02\x03",
            "#1200434V#0201F...the wolf-like monster responsible\x01",
            "for the attack looked pitch-black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200435V#0301F#11PHuh, yeah. I guess they were\x01",
            "totally different colors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290E")

    label("loc_259B")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200436V#0000F#6PAccording to Lytton, who was\x01",
            "ambushed on the hospital roof...\x02\x03",
            "#1200437V...the wolf-like monster that attacked\x01",
            "him had a pitch-black appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200438V#0101F#11PN-Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200439V#0203F#5PFurthermore, according to the testimonies\x01",
            "at Armorica and St. Ursula...\x02\x03",
            "#1200440V#0201F...on the night of the attacks, no one\x01",
            "recalled any howling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200441V#0301F#11PHuh, yeah. I guess that IS kinda\x01",
            "strange, now that I think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290E")

    label("loc_2794")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#1200442V#0003F#6PAccording to testimonies at Armorica\x01",
            "and St. Ursula, there were no mentions\x01",
            "of howling.\x02\x03",
            "#1200443V#0000FAlso, Lytton claims the wolf-like monsters\x01",
            "that ambushed him on the hospital roof\x01",
            "had a pitch-black appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200432V#0101F#11PN-Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200445V#0301F#11PLots of inconsistencies with\x01",
            "our wolf pal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290E")

    label("loc_290E")


    ChrTalk(
        0x101,
        (
            "#1200446V#0006F#6PRight. But that doesn't necessarily\x01",
            "mean we can cross him off our list\x01",
            "of suspects.\x02\x03",
            "#1200447V#0001FIt's possible he's their leader and is\x01",
            "commanding the black wolves to\x01",
            "do his dirty work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200448V#0208F#5PPacks tend to have an alpha, so\x01",
            "you may be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200449V#0103F#11PStill, if he isn't responsible for the attacks,\x01",
            "we'll need to adjust our thought process.\x02\x03",
            "#1200450V#0101FThere are now two different groups of\x01",
            "wolves acting on their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200451V#0004F#6PYeah, that's a safe assumption.\x02\x03",
            "#1200452V#0001FNot only that, but he may very well\x01",
            "have been a divine wolf--like the\x01",
            "one from the legends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200453V#0303F#11PAnd in that case, those black wolves,\x01",
            "which we know squat about, are causin'\x01",
            "this whole mess.\x02\x03",
            "#1200454V#0302FYep. Sure makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200455V#0204F#5PI also feel like that is a likely scenario.\x02\x03",
            "#1200456V#0202FAnd like I previously mentioned, I\x01",
            "sensed no hostility from the wolf.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1200457V#0000F#12PYeah, I think I'm on board.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200458V#0103F#11P'The final fragment lies ahead...'\x02\x03",
            "#1200459V#0101FBy 'ahead,' do you think he was\x01",
            "referring to Mainz?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D8A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D8A)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200460V#0004F#6PYeah, I can't see what else it'd be.\x02\x03",
            "#1200461V#0000FWe're almost there, so let's keep\x01",
            "pushing for a little longer, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200462V#0104F#11PI'm okay with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200463V#0306F#11PAin't we forgetting somethin'?\x01",
            "'The rest is in your hands...'\x02\x03",
            "#1200464V#0301FKinda pretentious, isn't it? He\x01",
            "too good to give us a paw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200465V#0203F#5PThat may be true, actually.\x02\x03",
            "#1200466V#0200FI did get the impression he was\x01",
            "being condescending.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200467V#0006F#12PW-Well, nothing we can do about that...\x02\x03",
            "#1200468V#0001FLet's get back on track and put an\x01",
            "end to this investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200469V#0101F#11PRight. I feel like we're on the cusp\x01",
            "of making a breakthrough.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_37()
    OP_68(-800, 600, 22500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, -800, 0, 22500, 0)
    SetChrPos(0x1, -800, 0, 22500, 0)
    SetChrPos(0x2, -800, 0, 22500, 0)
    SetChrPos(0x3, -800, 0, 22500, 0)
    SetScenarioFlags(0x65, 0)
    OP_29(0x40, 0x1, 0x6)
    OP_E0(0x0)
    Call(0, 4)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_5_F99 end

    def Function_6_3155(): pass

    label("Function_6_3155")

    OP_93(0x8, 0xE1, 0x12C)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_3179():
        OP_9D(0xFE, 0xFFFFFA10, 0x0, 0x6E5A, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3179)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(820, 0, 100, 0)
    Sound(832, 0, 100, 0)
    Sound(38, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 11)
    Return()

    # Function_6_3155 end

    def Function_7_3200(): pass

    label("Function_7_3200")

    OP_95(0xFE, -3510, 0, 23390, 2000, 0x0)
    OP_95(0xFE, -980, 0, 25900, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_7_3200 end

    def Function_8_3230(): pass

    label("Function_8_3230")

    OP_97(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_3230 end

    def Function_9_324C(): pass

    label("Function_9_324C")

    OP_93(0x8, 0x2D, 0x1F4)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x1)

    def lambda_3270():
        OP_9D(0xFE, 0x1194, 0xF3C, 0x84D0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3270)
    Sound(814, 0, 100, 0)
    Sound(38, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_9_324C end

    def Function_10_32B7(): pass

    label("Function_10_32B7")

    OP_95(0xFE, 8000, 3900, 30000, 6000, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_32D5():
        OP_9D(0xFE, 0x3C8C, 0x1EDC, 0x61A8, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32D5)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    OP_95(0xFE, 18180, 8000, 23720, 6000, 0x0)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_3340():
        OP_9D(0xFE, 0x45D8, 0x2EE0, 0x7602, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3340)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x1)

    def lambda_3390():
        OP_9D(0xFE, 0x4132, 0x3EE4, 0x95B0, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3390)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x1)
    Sound(39, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_10_32B7 end

    def Function_11_33D7(): pass

    label("Function_11_33D7")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3400")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_33E2")

    label("loc_3400")

    Return()

    # Function_11_33D7 end

    def Function_12_3401(): pass

    label("Function_12_3401")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There a gate to an old mine.\x01",
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_3401 end

    SaveToFile()

Try(main)
