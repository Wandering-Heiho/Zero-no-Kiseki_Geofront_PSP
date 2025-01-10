from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0040.bin",                # FileName
        "r0040",                    # MapName
        "r0040",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0040", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0040",                  # 0
        "列車",                   # 1
        "br0000",                 # 2
        "br0000",                 # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "br0000",                 # 7
        "To Crossbell City & Armorica Village",# 8
        "To Tangram Gate",        # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   12,  6,   0,   7,   5,   0)
    Sepith("Sepith_B4", 6,   12,  0,   3,   0,   6,   2)
    Sepith("Sepith_C4", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_D4", 10,  2,   0,   4,   0,   5,   2)
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
    MonsterBattlePostion("MonsterBattlePostion_154", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_174", 0x0000, 15, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms66700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms69300.dat", "ms66700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66700.dat", "ms66700.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 15, 6, 45, 6, 1, 15, 0, "br0000", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms69300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms66700.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69300.dat", "ms69300.dat", "ms66700.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0000, 15, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms69300.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", "ms69300.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3CC", 0x0010, 15, 6, 90, 6, 1, 5, 0, "br0000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms68900.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
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

    BattleInfo(
        "BattleInfo_530", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63700.dat", "ms63700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

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
        "monster/ch63750.itc",               # 18
        "monster/ch63751.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(400,     4090,    0,       0x1010000,    "BattleInfo_174", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(16300,   6830,    0,       0x1010000,    "BattleInfo_174", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(9480,    -15170,  0,       0x1010000,    "BattleInfo_23C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(71150,   -40180,  -6000,   0x1010000,    "BattleInfo_304", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(54700,   -53920,  -6000,   0x1010000,    "BattleInfo_3CC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(96330,   -71440,  -9250,   0x1010000,    "BattleInfo_3CC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(145270,  -47320,  -8170,   0x1010000,    "BattleInfo_23C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(83970,   -115500, -13000,  0x1010000,    "BattleInfo_174", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(126080,  -43730,  -9000,   0x1010000,    "BattleInfo_304", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(10940,   -4140,   0,       0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(42050,   -25350,  -2710,   0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(127590,  -64060,  -8000,   0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(145980,  -51720,  -7000,   0x18500B4,    "BattleInfo_530", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 8,   145.97999572753906,    -51.720001220703125,   -9.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -18.247499465942383,   6.465000152587891,     2.25,                  1.0])

    DeclActor(84240,   -13000,  -117840, 1200,    84240,   -12000,  -117840, 0x007C, 0,  3,  0x0000)
    DeclActor(84410,   -8000,   -71360,  1200,    84410,   -7000,   -71360,  0x007C, 0,  4,  0x0000)
    DeclActor(120310,  -9000,   -34770,  1200,    120310,  -8000,   -34770,  0x007C, 0,  5,  0x0000)
    DeclActor(10740,   0,       -13860,  1200,    10740,   0,       -13860,  0x007C, 0,  6,  0x0000)
    DeclActor(31610,   0,       -4490,   1200,    31610,   0,       -4490,   0x007C, 0,  7,  0x0000)

    PlaceName(-30.0, 0.0, 5.0, 0x0000, 0x0000, "To Crossbell City & Armorica Village")
    PlaceName(182.0, 0.0, -64.0, 0x0000, 0x0000, "To Tangram Gate")

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
        "Function_0_978",          # 00, 0
        "Function_1_997",          # 01, 1
        "Function_2_9AA",          # 02, 2
        "Function_3_D52",          # 03, 3
        "Function_4_E7C",          # 04, 4
        "Function_5_FCB",          # 05, 5
        "Function_6_1133",         # 06, 6
        "Function_7_1147",         # 07, 7
        "Function_8_115B",         # 08, 8
        "Function_9_13B3",         # 09, 9
        "Function_10_13D1",        # 0A, 10
    ))


    def Function_0_978(): pass

    label("Function_0_978")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_996")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_978")

    label("loc_996")

    Return()

    # Function_0_978 end

    def Function_1_997(): pass

    label("Function_1_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_9A6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_9A6")

    Call(0, 9)
    Return()

    # Function_1_997 end

    def Function_2_9AA(): pass

    label("Function_2_9AA")

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
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C1E")
    SetChrFlags(0x15, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_C32")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C32")
    ClearChrFlags(0x15, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C32")

    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x15, 0x100)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C60")
    OP_70(0x0, 0x0)
    Jump("loc_C64")

    label("loc_C60")

    OP_70(0x0, 0x1E)

    label("loc_C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C77")
    OP_70(0x1, 0x0)
    Jump("loc_C7B")

    label("loc_C77")

    OP_70(0x1, 0x1E)

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8E")
    OP_70(0x2, 0x0)
    Jump("loc_C92")

    label("loc_C8E")

    OP_70(0x2, 0x1E)

    label("loc_C92")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_CF8")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 10740, 0, -13860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_D51")

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_D51")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 31610, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_D51")

    Return()

    # Function_2_9AA end

    def Function_3_D52(): pass

    label("Function_3_D52")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA8, 1)"), scpexpr(EXPR_END)), "loc_DD2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_E37")

    label("loc_DD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
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

    label("loc_E37")

    Jump("loc_E70")

    label("loc_E3C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "NORVEMBER\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E70")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D52 end

    def Function_4_E7C(): pass

    label("Function_4_E7C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_EFC")
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
    SetScenarioFlags(0x100, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_F61")

    label("loc_EFC")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F61")

    Jump("loc_FBF")

    label("loc_F66")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sorry. No returns, exchanges, or chest credit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_FBF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_E7C end

    def Function_5_FCB(): pass

    label("Function_5_FCB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B5")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_104B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_10B0")

    label("loc_104B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
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

    label("loc_10B0")

    Jump("loc_1127")

    label("loc_10B5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hi, I'm Chest McClure. You may remember me\x01",
            "from such Falcom games as...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1127")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_FCB end

    def Function_6_1133(): pass

    label("Function_6_1133")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1133 end

    def Function_7_1147(): pass

    label("Function_7_1147")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1147 end

    def Function_8_115B(): pass

    label("Function_8_115B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 3)), scpexpr(EXPR_END)), "loc_1165")
    Return()

    label("loc_1165")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1248"),
        (SWITCH_DEFAULT, "loc_125F"),
    )


    label("loc_1248")

    Sleep(500)
    OP_90(0x0, 143780, -8000, -61010, 0)
    EventEnd(0x5)
    Return()

    label("loc_125F")

    Battle("BattleInfo_530", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(143780, -7000, -61010, 0)
    OP_90(0x0, 143780, -8000, -61010, 0)
    OP_90(0x1, 143780, -8000, -61010, 0)
    OP_90(0x2, 143780, -8000, -61010, 0)
    OP_90(0x3, 143780, -8000, -61010, 0)
    OP_90(0x4, 143780, -8000, -61010, 0)
    OP_90(0x5, 143780, -8000, -61010, 0)
    OP_90(0x6, 143780, -8000, -61010, 0)
    OP_90(0x7, 143780, -8000, -61010, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1321"),
        (1, "loc_1324"),
        (SWITCH_DEFAULT, "loc_1327"),
    )


    label("loc_1321")

    EventEnd(0x5)
    Return()

    label("loc_1324")

    OP_B7(0x0)
    Return()

    label("loc_1327")

    EventBegin(0x1)
    SetChrFlags(0x15, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster on East Crossbell Highway!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 3)
    OP_29(0x14, 0x4, 0x10)
    OP_29(0x14, 0x4, 0x2)
    OP_29(0x14, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_8_115B end

    def Function_9_13B3(): pass

    label("Function_9_13B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13D0")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_13D0")

    Return()

    # Function_9_13B3 end

    def Function_10_13D1(): pass

    label("Function_10_13D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x3, 0x8)
    OP_49()
    SetChrPos(0x8, 30300, -7000, -100000, 0)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    OP_68(66410, -770, -119610, 0)
    MoveCamera(27, 10, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(12060, 0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x1, 0x4)
    OP_11(0xAB, 0xE3, 0xEB, 0x28, 0xE6, 0x0)
    Sleep(500)
    SetCameraDistance(16059, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sound(451, 0, 100, 0)

    def lambda_14A6():
        OP_9B(0x1, 0xFE, 0x5A, 0x249F0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14A6)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_13D1 end

    SaveToFile()

Try(main)
