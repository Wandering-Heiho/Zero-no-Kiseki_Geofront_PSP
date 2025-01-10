from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0020.bin",                # FileName
        "r0020",                    # MapName
        "r0020",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0020",                  # 0
        "br0000",                 # 1
        "br0000",                 # 2
        "br0000",                 # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "To Crossbell City",      # 7
        "To Armorica Village & Tangram Gate",# 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 4,   4,   4,   4,   0,   0,   0)
    Sepith("Sepith_B4", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_C4", 1,   6,   0,   3,   2,   1,   1)
    Sepith("Sepith_D4", 3,   0,   2,   6,   0,   0,   2)
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

    # monster count: 18

    BattleInfo(
        "BattleInfo_174", 0x0000, 8, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_A4", 30, 45, 25, 0,
        (
            ("ms63000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63000.dat", "ms63000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63000.dat", "ms61000.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_210", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_B4", 30, 45, 25, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66500.dat", "ms63000.dat", "ms66500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2AC", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_C4", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_348", 0x0000, 8, 6, 45, 6, 1, 75, 0, "br0000", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms61000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61000.dat", "ms61000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61000.dat", "ms61000.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3E4", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_E4", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_480", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77500.dat", "ms77500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch63050.itc",               # 12
        "monster/ch63050.itc",               # 13
        "monster/ch61050.itc",               # 14
        "monster/ch61050.itc",               # 15
        "monster/ch69950.itc",               # 16
        "monster/ch69950.itc",               # 17
        "monster/ch77550.itc",               # 18
        "monster/ch77550.itc",               # 19
        "monster/ch63750.itc",               # 1A
        "monster/ch63751.itc",               # 1B
    ))

    DeclMonster(6590,    11560,   0,       0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19770,   -540,    -1790,   0x1010000,    "BattleInfo_210", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(32340,   -13180,  -2000,   0x1010000,    "BattleInfo_2AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(34430,   22750,   0,       0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(59270,   42550,   0,       0x1010000,    "BattleInfo_210", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(16120,   34420,   0,       0x1010000,    "BattleInfo_348", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(60950,   19410,   -4000,   0x1010000,    "BattleInfo_348", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(62620,   -1500,   -3610,   0x1010000,    "BattleInfo_210", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(86970,   1440,    -4000,   0x1010000,    "BattleInfo_2AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(60450,   -360,    3000,    0x1010000,    "BattleInfo_348", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(38070,   48570,   1130,    0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(131240,  60350,   4000,    0x1010000,    "BattleInfo_210", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(147670,  22420,   1000,    0x1010000,    "BattleInfo_2AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(145080,  62620,   3860,    0x1010000,    "BattleInfo_348", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(106730,  12830,   -3080,   0x1010000,    "BattleInfo_174", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33820,   32880,   10,      0x1010000,    "BattleInfo_3E4", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(110030,  47740,   1000,    0x1010000,    "BattleInfo_3E4", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(83470,   -2040,   -3000,   0x185010E,    "BattleInfo_480", 0,   24,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 7,   83.47000122070312,     -2.0399999618530273,   -5.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -10.43375015258789,    0.2549999952316284,    1.25,                  1.0])

    DeclActor(65950,   3000,    61070,   1200,    65950,   4000,    61070,   0x007C, 0,  3,  0x0000)
    DeclActor(151530,  1000,    22610,   1200,    151530,  2000,    22610,   0x007C, 0,  4,  0x0000)
    DeclActor(92870,   -5000,   34660,   1200,    90050,   -7000,   39730,   0x007C, 0,  9,  0x0000)
    DeclActor(72570,   0,       29130,   1200,    72570,   0,       29130,   0x007C, 0,  5,  0x0000)
    DeclActor(142060,  1500,    63090,   1200,    142060,  1500,    63090,   0x007C, 0,  6,  0x0000)

    PlaceName(-19.5, 0.0, -18.5, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(187.0, 0.0, 39.0, 0x0000, 0x0000, "To Armorica Village & Tangram Gate")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9

    ScpFunction((
        "Function_0_950",          # 00, 0
        "Function_1_96C",          # 01, 1
        "Function_2_970",          # 02, 2
        "Function_3_F96",          # 03, 3
        "Function_4_10E7",         # 04, 4
        "Function_5_12B7",         # 05, 5
        "Function_6_12CB",         # 06, 6
        "Function_7_12DF",         # 07, 7
        "Function_8_1537",         # 08, 8
        "Function_9_1550",         # 09, 9
    ))


    def Function_0_950(): pass

    label("Function_0_950")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_950")

    label("loc_96B")

    Return()

    # Function_0_950 end

    def Function_1_96C(): pass

    label("Function_1_96C")

    Call(0, 8)
    Return()

    # Function_1_96C end

    def Function_2_970(): pass

    label("Function_2_970")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DDE")
    SetChrFlags(0x19, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_DF2")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF2")
    ClearChrFlags(0x19, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DF2")

    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x19, 0x100)
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E")
    OP_65(0x2, 0x1)

    label("loc_E5E")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 90050, -7000, 39730, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")
    OP_70(0x0, 0x0)
    Jump("loc_EBF")

    label("loc_EBB")

    OP_70(0x0, 0x1E)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")
    OP_70(0x1, 0x0)
    Jump("loc_ED6")

    label("loc_ED2")

    OP_70(0x1, 0x1E)

    label("loc_ED6")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 1)), scpexpr(EXPR_END)), "loc_F3C")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 72570, 0, 29130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_F95")

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 2)), scpexpr(EXPR_END)), "loc_F95")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 142060, 1500, 63090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_F95")

    Return()

    # Function_2_970 end

    def Function_3_F96(): pass

    label("Function_3_F96")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1080")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3C, 1)"), scpexpr(EXPR_END)), "loc_1016")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_107B")

    label("loc_1016")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
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

    label("loc_107B")

    Jump("loc_10DB")

    label("loc_1080")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I thought you were supposed to serve the people!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10DB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_F96 end

    def Function_4_10E7(): pass

    label("Function_4_10E7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121B")
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
    SetScenarioFlags(0x100, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_12A5")

    label("loc_121B")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The contents of this chest brought to you\x01",
            "by the International Bank of Crossbell.\x01",
            "Visit us for premium sepith exchange rates.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_12A5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_10E7 end

    def Function_5_12B7(): pass

    label("Function_5_12B7")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_12B7 end

    def Function_6_12CB(): pass

    label("Function_6_12CB")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_12CB end

    def Function_7_12DF(): pass

    label("Function_7_12DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 6)), scpexpr(EXPR_END)), "loc_12E9")
    Return()

    label("loc_12E9")

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
        (1, "loc_13CC"),
        (SWITCH_DEFAULT, "loc_13E3"),
    )


    label("loc_13CC")

    Sleep(500)
    OP_90(0x0, 76760, -4000, 920, 135)
    EventEnd(0x5)
    Return()

    label("loc_13E3")

    Battle("BattleInfo_480", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(76760, -3000, 920, 0)
    OP_90(0x0, 76760, -4000, 920, 135)
    OP_90(0x1, 76760, -4000, 920, 135)
    OP_90(0x2, 76760, -4000, 920, 135)
    OP_90(0x3, 76760, -4000, 920, 135)
    OP_90(0x4, 76760, -4000, 920, 135)
    OP_90(0x5, 76760, -4000, 920, 135)
    OP_90(0x6, 76760, -4000, 920, 135)
    OP_90(0x7, 76760, -4000, 920, 135)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_14A5"),
        (1, "loc_14A8"),
        (SWITCH_DEFAULT, "loc_14AB"),
    )


    label("loc_14A5")

    EventEnd(0x5)
    Return()

    label("loc_14A8")

    OP_B7(0x0)
    Return()

    label("loc_14AB")

    EventBegin(0x1)
    SetChrFlags(0x19, 0x80)
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
    SetScenarioFlags(0x78, 6)
    OP_29(0x21, 0x4, 0x10)
    OP_29(0x21, 0x4, 0x2)
    OP_29(0x21, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_7_12DF end

    def Function_8_1537(): pass

    label("Function_8_1537")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_154F")

    Return()

    # Function_8_1537 end

    def Function_9_1550(): pass

    label("Function_9_1550")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FSure, I'm on duty, but what the chief\x01",
            "doesn't know won't hurt him, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(90520, -4400, 36960, 1500)
    MoveCamera(26, 41, 0, 1500)
    OP_6E(470, 1500)
    SetCameraDistance(23000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1647")
    OP_E0(0x2)
    MiniGame(0x6, 0x14, 0x16A8A, 0xFFFFEC78, 0x8214, 0x0, 0x15FC2, 0xFFFFE4A8, 0x9B32)

    label("loc_1647")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_9_1550 end

    SaveToFile()

Try(main)
