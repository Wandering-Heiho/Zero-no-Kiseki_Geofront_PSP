from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0050.bin",                # FileName
        "r0050",                    # MapName
        "r0050",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0050", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 2, 0, 3],
    )

    BuildStringList((
        "r0050",                  # 0
        "Purple Charlot",         # 1
        "Master Cryon",           # 2
        "br0000",                 # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "br0000",                 # 7
        "br0000",                 # 8
        "br0000",                 # 9
        "To Crossbell City & Armorica Village",# 10
        "To Tangram Gate",        # 11
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 6,   12,  0,   3,   0,   6,   2)
    Sepith("Sepith_B4", 0,   12,  6,   0,   7,   5,   0)
    Sepith("Sepith_C4", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_D4", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_E4", 12,  20,  10,  28,  11,  2,   5)

    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_118", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_120", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_124", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_128", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_12C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_174", 0x0000, 15, 6, 60, 6, 1, 15, 0, "br0000", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms69300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms66700.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", "ms66700.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 15, 6, 60, 6, 1, 25, 0, "br0000", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms66700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0010, 15, 6, 60, 0, 1, 5, 0, "br0000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms68900.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3CC", 0x0000, 15, 6, 60, 6, 1, 40, 0, "br0000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms69300.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_E4", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_530", 0x0000, 15, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", "ms69300.dat", "ms66700.dat", "ms66700.dat", 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0000, 30, 6, 0, 0, 1, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63100.dat", "ms63100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
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
        "monster/ch65550.itc",               # 10
        "monster/ch65551.itc",               # 11
        "monster/ch77450.itc",               # 12
        "monster/ch77450.itc",               # 13
        "monster/ch66750.itc",               # 14
        "monster/ch66750.itc",               # 15
        "monster/ch69350.itc",               # 16
        "monster/ch69351.itc",               # 17
        "monster/ch63150.itc",               # 18
        "monster/ch63150.itc",               # 19
        "monster/ch63750.itc",               # 1A
        "monster/ch63751.itc",               # 1B
    ))

    DeclNpc(85589,   4500,    20450,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(98000,   2750,    11000,   0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(12810,   -14760,  -4000,   0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(22410,   32450,   -2000,   0x1010000,    "BattleInfo_23C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(57420,   -5890,   -2000,   0x1010000,    "BattleInfo_304", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(81820,   8280,    4000,    0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(76670,   -19800,  850,     0x1010000,    "BattleInfo_3CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(104220,  -20140,  2009,    0x1010000,    "BattleInfo_23C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(95910,   800,     2009,    0x1010000,    "BattleInfo_304", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(20360,   21750,   -2000,   0x1010000,    "BattleInfo_494", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(49490,   -11630,  -2000,   0x1010000,    "BattleInfo_494", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(104110,  -1970,   2000,    0x1010000,    "BattleInfo_494", 0,   26,  0xFFFF, 8,  9)

    DeclActor(85590,   4000,    20450,   1200,    85590,   5000,    20450,   0x007C, 0,  4,  0x0000)
    DeclActor(82810,   4000,    20550,   1200,    82810,   5000,    20550,   0x007C, 0,  5,  0x0000)
    DeclActor(98000,   2000,    11000,   1200,    98000,   3000,    11000,   0x007C, 0,  6,  0x0000)
    DeclActor(84940,   4000,    2310,    1200,    84940,   4000,    2310,    0x007C, 0,  7,  0x0000)
    DeclActor(109990,  2009,    -27160,  1500,    109990,  3710,    -27160,  0x007C, 0,  9,  0x0000)

    PlaceName(-15.0, 0.0, -10.0, 0x0000, 0x0000, "To Crossbell City & Armorica Village")
    PlaceName(150.0, 0.0, -27.5, 0x0000, 0x0000, "To Tangram Gate")

    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9

    ScpFunction((
        "Function_0_91C",          # 00, 0
        "Function_1_93B",          # 01, 1
        "Function_2_958",          # 02, 2
        "Function_3_BDA",          # 03, 3
        "Function_4_ECF",          # 04, 4
        "Function_5_10FD",         # 05, 5
        "Function_6_1298",         # 06, 6
        "Function_7_1567",         # 07, 7
        "Function_8_157B",         # 08, 8
        "Function_9_1599",         # 09, 9
    ))


    def Function_0_91C(): pass

    label("Function_0_91C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93A")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_91C")

    label("loc_93A")

    Return()

    # Function_0_91C end

    def Function_1_93B(): pass

    label("Function_1_93B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_957")
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_93B")

    label("loc_957")

    Return()

    # Function_1_93B end

    def Function_2_958(): pass

    label("Function_2_958")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD6")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B5")
    SetScenarioFlags(0x7A, 0)

    label("loc_9B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CB")
    SetScenarioFlags(0x7A, 1)

    label("loc_9CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    SetScenarioFlags(0x7A, 2)

    label("loc_9E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7")
    SetScenarioFlags(0x7A, 3)

    label("loc_9F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D")
    SetScenarioFlags(0x7A, 4)

    label("loc_A0D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A23")
    SetScenarioFlags(0x7A, 5)

    label("loc_A23")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A39")
    SetScenarioFlags(0x7A, 6)

    label("loc_A39")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F")
    SetScenarioFlags(0x7A, 7)

    label("loc_A4F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A65")
    SetScenarioFlags(0x7B, 0)

    label("loc_A65")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7B")
    SetScenarioFlags(0x7B, 1)

    label("loc_A7B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A91")
    SetScenarioFlags(0x7B, 2)

    label("loc_A91")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    SetScenarioFlags(0x7B, 3)

    label("loc_AA7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABD")
    SetScenarioFlags(0x7B, 4)

    label("loc_ABD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD3")
    SetScenarioFlags(0x7B, 5)

    label("loc_AD3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE9")
    SetScenarioFlags(0x7B, 6)

    label("loc_AE9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFF")
    SetScenarioFlags(0x7B, 7)

    label("loc_AFF")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_BD6")

    label("loc_B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B51")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_BD6")

    label("loc_B51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_BD6")

    label("loc_B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_BD6")

    label("loc_B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_BD6")

    label("loc_B96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAD")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_BD6")

    label("loc_BAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC4")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_BD6")

    label("loc_BC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD6")
    SetScenarioFlags(0x7C, 7)

    label("loc_BD6")

    Call(0, 8)
    Return()

    # Function_2_958 end

    def Function_3_BDA(): pass

    label("Function_3_BDA")

    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3F")
    OP_70(0x0, 0x0)
    Jump("loc_E43")

    label("loc_E3F")

    OP_70(0x0, 0x1E)

    label("loc_E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E56")
    OP_70(0x1, 0x0)
    Jump("loc_E5A")

    label("loc_E56")

    OP_70(0x1, 0x1E)

    label("loc_E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")
    OP_70(0x2, 0x0)
    Jump("loc_E71")

    label("loc_E6D")

    OP_70(0x2, 0x1E)

    label("loc_E71")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_ECE")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 84940, 4000, 2310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_ECE")

    Return()

    # Function_3_BDA end

    def Function_4_ECF(): pass

    label("Function_4_ECF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108E")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCE")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F28():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F28)

    def lambda_F42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F42)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FAF"),
        (2, "loc_FBE"),
        (1, "loc_FCB"),
        (SWITCH_DEFAULT, "loc_FCE"),
    )


    label("loc_FAF")

    SetScenarioFlags(0x74, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FCE")

    label("loc_FBE")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FCB")

    OP_B7(0x0)
    Return()

    label("loc_FCE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA9, 1)"), scpexpr(EXPR_END)), "loc_1026")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1089")

    label("loc_1026")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
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

    label("loc_1089")

    Jump("loc_10F1")

    label("loc_108E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, well, my cousin's Erebonian and\x01",
            "he didn't even GET a message!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_ECF end

    def Function_5_10FD(): pass

    label("Function_5_10FD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x40\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x40.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x101, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1286")

    label("loc_1231")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "My buddy's from Liberl and he got his\x01",
            "message written by a professional.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1286")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10FD end

    def Function_6_1298(): pass

    label("Function_6_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1333")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sense powerful monsters in the chest.\x01",
            "Monster level: 30\x01",
            "Open and challenge?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1333")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1333")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F2")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1432")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_138C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_138C)

    def lambda_13A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13A6)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_574", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1413"),
        (2, "loc_1422"),
        (1, "loc_142F"),
        (SWITCH_DEFAULT, "loc_1432"),
    )


    label("loc_1413")

    SetScenarioFlags(0x72, 0)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1432")

    label("loc_1422")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_142F")

    OP_B7(0x0)
    Return()

    label("loc_1432")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x93, 1)"), scpexpr(EXPR_END)), "loc_148A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x93),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_14ED")

    label("loc_148A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x93),
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

    label("loc_14ED")

    Jump("loc_155B")

    label("loc_14F2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You are now breathing manually.\x01",
            "That's my revenge for taking that quartz.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_155B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1298 end

    def Function_7_1567(): pass

    label("Function_7_1567")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1567 end

    def Function_8_157B(): pass

    label("Function_8_157B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1598")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_1598")

    Return()

    # Function_8_157B end

    def Function_9_1599(): pass

    label("Function_9_1599")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East: Tangram Gate\x01",
            "West: Crossbell City - 206 selge\x01",
            "      Armorica Village - 232 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_1599 end

    SaveToFile()

Try(main)
