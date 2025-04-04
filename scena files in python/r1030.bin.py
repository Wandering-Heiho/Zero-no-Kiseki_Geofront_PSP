from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1030.bin",                # FileName
        "r1030",                    # MapName
        "r1030",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1030", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 1000, 9000, 0, 0, 1, 95, 0, 3, 0, 4],
    )

    BuildStringList((
        "r1030",                  # 0
        "Colin",                  # 1
        "Boss 1",                 # 2
        "Boss 2",                 # 3
        "Boss 3",                 # 4
        "Boss 4",                 # 5
        "Boss 5",                 # 6
        "Boss 6",                 # 7
        "Kettle",                 # 8
        "Butterfly",              # 9
        "Bus",                    # 10
        "Flaming Ginu",           # 11
        "br1000",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "br1000",                 # 17
        "br1000",                 # 18
        "br1000",                 # 19
        "br1000",                 # 20
        "To Crossbell City",      # 21
        "To Bellguard Gate",      # 22
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   0,   13,  1,   5,   7,   4)
    Sepith("Sepith_B4", 2,   1,   0,   0,   9,   9,   9)
    Sepith("Sepith_C4", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_D4", 4,   2,   11,  0,   0,   8,   5)
    Sepith("Sepith_E4", 0,   8,   0,   12,  4,   8,   0)
    Sepith("Sepith_F4", 12,  7,   4,   3,   6,   14,  7)

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
    MonsterBattlePostion("MonsterBattlePostion_164", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 12, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 4, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_198", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_19C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_1A4", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms71300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71300.dat", "ms71300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71300.dat", "ms71300.dat", "ms70400.dat", "ms71300.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_26C", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms64200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64200.dat", "ms64200.dat", "ms64200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64200.dat", "ms66900.dat", "ms64200.dat", "ms66900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_334", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms70400.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 17, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_628", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65100.dat", "ms65100.dat", "ms65100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_164", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_66C", 0x0000, 17, 6, 60, 0, 1, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", "ms71300.dat", 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6B0", 0x0002, 26, 6, 0, 0, 1, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62900.dat", "ms62900.dat", "ms62900.dat", "ms62900.dat", 0, 0, 0, 0, "MonsterBattlePostion_184", "MonsterBattlePostion_124", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch71350.itc",               # 12
        "monster/ch71351.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch64250.itc",               # 16
        "monster/ch64251.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch65150.itc",               # 1A
        "monster/ch65150.itc",               # 1B
        "monster/ch60750.itc",               # 1C
        "monster/ch60750.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-59919,  500,     32990,   0,    484,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-17880,  910,     0,       0x1010000,    "BattleInfo_1A4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44410,  -7750,   0,       0x1010000,    "BattleInfo_26C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-60650,  27380,   0,       0x1010000,    "BattleInfo_334", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-16440,  44520,   0,       0x1010000,    "BattleInfo_3FC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-39150,  60950,   0,       0x1010000,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-74290,  -25740,  -2000,   0x1010000,    "BattleInfo_3FC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-34710,  -42590,  -4000,   0x1010000,    "BattleInfo_1A4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-62760,  -62500,  -6000,   0x1010000,    "BattleInfo_334", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-19130,  6440,    0,       0x1010000,    "BattleInfo_58C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-59570,  -9280,   0,       0x1010000,    "BattleInfo_58C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-56370,  -76140,  -6000,   0x1010000,    "BattleInfo_58C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-27490,  31330,   0,       0x1010000,    "BattleInfo_58C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-38170,  2140,    1000,    0x185005A,    "BattleInfo_628", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 19,  -36.0,                 2.0,                   -1.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666666269302368,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   7.200000286102295,     -0.13333332538604736,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 20,  -38.0,                 -50.0,                 -5.5,                  506.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.222222328186035,     10.0,                  1.100000023841858,     1.0])
    DeclEvent(0x0000, 0, 11,  -37.56999969482422,    2.0,                   -1.0,                  3600.0,                [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.696249961853027,     -0.13333334028720856,  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 48,  -28.690000534057617,   29.889999389648438,    -0.5,                  144.0,                 [0.05892554670572281,  0.35355350375175476,   -0.0,                  0.0,                   -0.05892558768391609,  0.35355326533317566,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.451859712600708,     -0.42425668239593506,  0.10000000149011612,   1.0])

    DeclActor(-59920,  0,       32990,   1200,    -59920,  1000,    32990,   0x007C, 0,  5,  0x0000)
    DeclActor(-82750,  -2000,   -27760,  1200,    -82750,  -1000,   -27760,  0x007C, 0,  6,  0x0000)
    DeclActor(-27210,  -3900,   -44030,  1200,    -27210,  -2900,   -44030,  0x007C, 0,  7,  0x0000)
    DeclActor(-37700,  0,       8150,    1200,    -37700,  1000,    8150,    0x007C, 0,  18, 0x0000)
    DeclActor(-62570,  0,       36330,   1200,    -62770,  -1000,   40340,   0x007C, 0,  17, 0x0000)
    DeclActor(-49450,  -6000,   -76260,  1200,    -49360,  -3000,   -76640,  0x007C, 0,  49, 0x0000)
    DeclActor(-12560,  0,       12190,   1200,    -12560,  0,       12190,   0x007C, 0,  8,  0x0000)
    DeclActor(-51750,  0,       -9060,   1200,    -51750,  0,       -9060,   0x007C, 0,  9,  0x0000)
    DeclActor(-23570,  0,       48090,   1200,    -23570,  0,       48090,   0x007C, 0,  10, 0x0000)
    DeclActor(-59500,  -6000,   -63000,  1200,    -59500,  -5000,   -63000,  0x007C, 0,  47, 0x0000)
    DeclActor(-37790,  0,       10900,   1500,    -37790,  1700,    10900,   0x007C, 0,  50, 0x0000)

    PlaceName(29.0, 0.0, 19.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-95.0, 0.0, 84.0, 0x0000, 0x0000, "To Bellguard Gate")
    PlaceName(-37.5, 0.0, 8.449999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_EE4",          # 00, 0
        "Function_1_F00",          # 01, 1
        "Function_2_F1F",          # 02, 2
        "Function_3_F3E",          # 03, 3
        "Function_4_F60",          # 04, 4
        "Function_5_193C",         # 05, 5
        "Function_6_1B5B",         # 06, 6
        "Function_7_1CD6",         # 07, 7
        "Function_8_1E59",         # 08, 8
        "Function_9_1E6D",         # 09, 9
        "Function_10_1E81",        # 0A, 10
        "Function_11_1E95",        # 0B, 11
        "Function_12_260A",        # 0C, 12
        "Function_13_262D",        # 0D, 13
        "Function_14_26EA",        # 0E, 14
        "Function_15_280E",        # 0F, 15
        "Function_16_292F",        # 10, 16
        "Function_17_29C4",        # 11, 17
        "Function_18_2AE2",        # 12, 18
        "Function_19_2C11",        # 13, 19
        "Function_20_2F4E",        # 14, 20
        "Function_21_4152",        # 15, 21
        "Function_22_4178",        # 16, 22
        "Function_23_419E",        # 17, 23
        "Function_24_41C4",        # 18, 24
        "Function_25_41EA",        # 19, 25
        "Function_26_4210",        # 1A, 26
        "Function_27_422C",        # 1B, 27
        "Function_28_424B",        # 1C, 28
        "Function_29_42C1",        # 1D, 29
        "Function_30_437A",        # 1E, 30
        "Function_31_4427",        # 1F, 31
        "Function_32_449E",        # 20, 32
        "Function_33_4558",        # 21, 33
        "Function_34_45B3",        # 22, 34
        "Function_35_51B5",        # 23, 35
        "Function_36_526A",        # 24, 36
        "Function_37_52CB",        # 25, 37
        "Function_38_52E7",        # 26, 38
        "Function_39_5370",        # 27, 39
        "Function_40_53D4",        # 28, 40
        "Function_41_54C2",        # 29, 41
        "Function_42_5574",        # 2A, 42
        "Function_43_5593",        # 2B, 43
        "Function_44_55C8",        # 2C, 44
        "Function_45_5633",        # 2D, 45
        "Function_46_5652",        # 2E, 46
        "Function_47_5670",        # 2F, 47
        "Function_48_5ACD",        # 30, 48
        "Function_49_5B35",        # 31, 49
        "Function_50_63D0",        # 32, 50
    ))


    def Function_0_EE4(): pass

    label("Function_0_EE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EFF")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_EE4")

    label("loc_EFF")

    Return()

    # Function_0_EE4 end

    def Function_1_F00(): pass

    label("Function_1_F00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_F00")

    label("loc_F1E")

    Return()

    # Function_1_F00 end

    def Function_2_F1F(): pass

    label("Function_2_F1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F3D")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_F1F")

    label("loc_F3D")

    Return()

    # Function_2_F1F end

    def Function_3_F3E(): pass

    label("Function_3_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_F4D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 34)

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_F5C")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 16)

    label("loc_F5C")

    Call(0, 12)
    Return()

    # Function_3_F3E end

    def Function_4_F60(): pass

    label("Function_4_F60")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F90")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1711")
    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_1725")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1725")
    ClearChrFlags(0x1F, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1725")

    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x1F, 0x100)
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x9, 0x1)
    SetMapObjFlags(0x5, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1764")
    OP_66(0x9, 0x1)

    label("loc_1764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1773")
    ClearMapObjFlags(0x5, 0x4)

    label("loc_1773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1786")
    OP_70(0x0, 0x0)
    Jump("loc_178A")

    label("loc_1786")

    OP_70(0x0, 0x1E)

    label("loc_178A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179D")
    OP_70(0x1, 0x0)
    Jump("loc_17A1")

    label("loc_179D")

    OP_70(0x1, 0x1E)

    label("loc_17A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B4")
    OP_70(0x2, 0x0)
    Jump("loc_17B8")

    label("loc_17B4")

    OP_70(0x2, 0x1E)

    label("loc_17B8")

    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_1822")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -12560, 0, 12190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)
    Jump("loc_18D9")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_1880")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -51750, 0, -9060, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)
    Jump("loc_18D9")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_18D9")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -23570, 0, 48090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x8, 0x1)

    label("loc_18D9")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -62770, -1000, 40340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193B")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_193B")

    Return()

    # Function_4_F60 end

    def Function_5_193C(): pass

    label("Function_5_193C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3B")
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x12, 0x0, 0)
    OP_98(0x12, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1995():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1995)

    def lambda_19AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_19AF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x12, 1)
    Battle("BattleInfo_66C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1A1C"),
        (2, "loc_1A2B"),
        (1, "loc_1A38"),
        (SWITCH_DEFAULT, "loc_1A3B"),
    )


    label("loc_1A1C")

    SetScenarioFlags(0x74, 5)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_1A3B")

    label("loc_1A2B")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A38")

    OP_B7(0x0)
    Return()

    label("loc_1A3B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x647, 1)"), scpexpr(EXPR_END)), "loc_1A93")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x647),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1AF6")

    label("loc_1A93")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x647),
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

    label("loc_1AF6")

    Jump("loc_1B4F")

    label("loc_1AFB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ahhh, I get it. Fish prints.\x01",
            "Of course. Fish prints.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1B4F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_193C end

    def Function_6_1B5B(): pass

    label("Function_6_1B5B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1D")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x60\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x60\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x60.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x119, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1CC4")

    label("loc_1C1D")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The true result of the Non-Aggression Pact is not\x01",
            "technological exchange, but the spread of talkative\x01",
            "treasure chests that previously were only in Liberl.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1CC4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1B5B end

    def Function_7_1CD6(): pass

    label("Function_7_1CD6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC0")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1D56")
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
    SetScenarioFlags(0x119, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1DBB")

    label("loc_1D56")

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

    label("loc_1DBB")

    Jump("loc_1E4D")

    label("loc_1DC0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Disappointed with the chest's contents, you close it.\x01",
            "One could call this...an open-and-shut case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1E4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1CD6 end

    def Function_8_1E59(): pass

    label("Function_8_1E59")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1E59 end

    def Function_9_1E6D(): pass

    label("Function_9_1E6D")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_1E6D end

    def Function_10_1E81(): pass

    label("Function_10_1E81")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x8, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_10_1E81 end

    def Function_11_1E95(): pass

    label("Function_11_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 2)), scpexpr(EXPR_END)), "loc_1E9F")
    Return()

    label("loc_1E9F")

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
        (1, "loc_1F82"),
        (SWITCH_DEFAULT, "loc_1F99"),
    )


    label("loc_1F82")

    Sleep(500)
    OP_90(0x0, -32290, 0, 1830, 270)
    EventEnd(0x5)
    Return()

    label("loc_1F99")

    Battle("BattleInfo_628", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-32290, 1000, 1830, 0)
    OP_90(0x0, -32290, 0, 1830, 270)
    OP_90(0x1, -32290, 0, 1830, 270)
    OP_90(0x2, -32290, 0, 1830, 270)
    OP_90(0x3, -32290, 0, 1830, 270)
    OP_90(0x4, -32290, 0, 1830, 270)
    OP_90(0x5, -32290, 0, 1830, 270)
    OP_90(0x6, -32290, 0, 1830, 270)
    OP_90(0x7, -32290, 0, 1830, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_205B"),
        (1, "loc_205E"),
        (SWITCH_DEFAULT, "loc_2061"),
    )


    label("loc_205B")

    EventEnd(0x5)
    Return()

    label("loc_205E")

    OP_B7(0x0)
    Return()

    label("loc_2061")

    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(-38360, 600, 1950, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    EventBegin(0x0)
    SetChrFlags(0x1F, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster on West Crossbell Highway!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrPos(0x101, -38400, 0, 3980, 180)
    SetChrPos(0x102, -36700, 0, 1980, 270)
    SetChrPos(0x103, -38400, 0, -20, 0)
    SetChrPos(0x104, -40400, 0, 1980, 90)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x102,
        "#0106FPhew... That was harder than I had anticipated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FKinda surprised, to be honest.\x02\x03",
            "I've patrolled these parts a bunch of times\x01",
            "back during my CGF days, but I'd never\x01",
            "seen anythin' that tough before.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 2)), scpexpr(EXPR_END)), "loc_22DC")

    ChrTalk(
        0x103,
        "#0202FHowever, the bus may now resume service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, fortunately. We should report\x01",
            "the good news to City Hall.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2428")

    label("loc_22DC")


    ChrTalk(
        0x101,
        (
            "#0008FYou know, I'm actually a bit worried it was\x01",
            "roaming around the middle of the highway.\x02\x03",
            "That bus stop is right there, so it could\x01",
            "have put people in danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt was likely interrupting the bus service\x01",
            "in this direction.\x02\x03",
            "We should contact City Hall to inform them\x01",
            "of our success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSounds like a plan.\x02",
    )

    CloseMessageWindow()

    label("loc_2428")

    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd contacted City Hall to inform them that\x01",
            "they'd disposed of the monster on the highway.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bus service will resume immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_64(0x101)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Buses traveling on West Crossbell Highway\x01",
            "are up and running again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x78, 2)
    OP_29(0x10, 0x4, 0x10)
    OP_29(0x10, 0x4, 0x2)
    OP_29(0x10, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_1E95 end

    def Function_12_260A(): pass

    label("Function_12_260A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_262C")
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    label("loc_262C")

    Return()

    # Function_12_260A end

    def Function_13_262D(): pass

    label("Function_13_262D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City - West Exit\x01",      # 0
            "Bellguard Gate\x01",                  # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C2")
    Call(0, 14)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_26E2")

    label("loc_26C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E2")
    Call(0, 15)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()

    label("loc_26E2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_262D end

    def Function_14_26EA(): pass

    label("Function_14_26EA")

    Fade(1000)
    OP_68(-40030, 600, 12630, 0)
    MoveCamera(38, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(24000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 270)
    SetChrPos(0x1, -39500, 0, 8500, 270)
    SetChrPos(0x2, -39500, 0, 9700, 270)
    SetChrPos(0x3, -39500, 0, 10900, 270)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x11)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -27810, 0, 29700, 225)
    OP_D3(0x11, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_27C5():
        OP_95(0xFE, -43990, 0, 13530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_27C5)
    Sleep(500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_14_26EA end

    def Function_15_280E(): pass

    label("Function_15_280E")

    Fade(1000)
    OP_68(-38160, 600, 3480, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -39500, 0, 7300, 180)
    SetChrPos(0x1, -39500, 0, 8500, 180)
    SetChrPos(0x2, -39500, 0, 9700, 180)
    SetChrPos(0x3, -39500, 0, 10900, 180)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x11)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -27200, 0, 1290, 270)
    OP_D3(0x11, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_28E9():
        OP_95(0xFE, -39660, 0, 1670, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_28E9)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_15_280E end

    def Function_16_292F(): pass

    label("Function_16_292F")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -36870, 0, 7430, 225)
    SetChrPos(0x1, -36870, 0, 7430, 225)
    SetChrPos(0x2, -36870, 0, 7430, 225)
    SetChrPos(0x3, -36870, 0, 7430, 225)
    OP_68(-36870, 600, 7430, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_292F end

    def Function_17_29C4(): pass

    label("Function_17_29C4")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FHad I known there was such a perfect\x01",
            "fishing spot so close to the academy,\x01",
            "I might not have ever graduated.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-62940, 600, 37620, 1500)
    MoveCamera(45, 45, 0, 1500)
    OP_6E(470, 1500)
    SetCameraDistance(23500, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADD")
    OP_E0(0x2)
    MiniGame(0x6, 0x12, 0xFFFF0D4E, 0x0, 0x8804, 0x0, 0xFFFF0ACE, 0xFFFFFC18, 0x9D94)

    label("loc_2ADD")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_29C4 end

    def Function_18_2AE2(): pass

    label("Function_18_2AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BA7")
    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the ongoing monster infestation, the\x01",
            "bus service has been temporarily suspended.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_2C10")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0D")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#0001FWe don't have time to wait for the bus!\x01",
            "Let's go find Colin ASAP!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_2C10")

    label("loc_2C0D")

    Call(0, 13)

    label("loc_2C10")

    Return()

    # Function_18_2AE2 end

    def Function_19_2C11(): pass

    label("Function_19_2C11")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-37910, 400, 3210, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21640, 0)
    SetCameraDistance(20640, 2000)
    SetChrPos(0x101, -40270, 0, 1690, 270)
    SetChrPos(0x102, -39010, 0, 3170, 270)
    SetChrPos(0x103, -39370, 0, 1230, 270)
    SetChrPos(0x104, -37130, 0, 3090, 270)
    SetChrPos(0x160, -36970, 0, 1730, 270)
    SetChrPos(0x8, -46500, -2000, -6500, 0)
    OP_0D()
    SetMessageWindowPos(220, 170, -1, -1)
    SetChrName("Child's Voice")

    AnonymousTalk(
        0xFF,
        "#3400619V#2SHehehe! Come back!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
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
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400620V#0005F#11PDid you hear that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400621V#0108F#11PWhich way did it come from?\x02",
    )

    CloseMessageWindow()

    def lambda_2DE2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DE2)
    Sleep(50)

    def lambda_2DF2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DF2)
    Sleep(50)

    def lambda_2E02():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2E02)
    Sleep(300)

    ChrTalk(
        0x103,
        "#3400622V#0202F#5PSouth!\x02",
    )

    CloseMessageWindow()

    def lambda_2E30():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E30)
    Sleep(50)

    def lambda_2E40():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E40)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#3400623V#0300F#5PYeah! Sounded like it was comin' from the\x01",
            "direction of the police academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400624V#0000F#5PAll right. Let's hurry and check it out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400625V#3308F#11P#40W(So he's safe, then?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -41600, 0, 2050, 270)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA3, 2)
    OP_29(0x46, 0x1, 0xE)
    OP_E0(0x2)
    Call(0, 12)
    EventEnd(0x5)
    Return()

    # Function_19_2C11 end

    def Function_20_2F4E(): pass

    label("Function_20_2F4E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch07200.itc", 0x26)
    LoadChrToIndex("monster/ch62950.itc", 0x27)
    LoadChrToIndex("monster/ch62951.itc", 0x28)
    LoadChrToIndex("monster/ch62952.itc", 0x29)
    LoadChrToIndex("apl/ch50338.itc", 0x2A)
    LoadChrToIndex("apl/ch50339.itc", 0x2B)
    LoadChrToIndex("apl/ch50340.itc", 0x2C)
    LoadChrToIndex("apl/ch50341.itc", 0x2D)
    LoadChrToIndex("apl/ch50337.itc", 0x2F)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "event\\ev312_00.eff")
    LoadEffect(0x2, "event\\ev313_00.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307D")
    SetChrPos(0x101, -38330, -4000, -48020, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_31B0")

    label("loc_307D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E5")
    SetChrPos(0x101, -39320, -4000, -47210, 180)
    SetChrPos(0x102, -38330, -4000, -48020, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_31B0")

    label("loc_30E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314D")
    SetChrPos(0x101, -37450, -4000, -46640, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -38330, -4000, -48020, 180)
    SetChrPos(0x104, -37440, -4000, -45160, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)
    Jump("loc_31B0")

    label("loc_314D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B0")
    SetChrPos(0x101, -37440, -4000, -45160, 180)
    SetChrPos(0x102, -39320, -4000, -47210, 180)
    SetChrPos(0x103, -37450, -4000, -46640, 180)
    SetChrPos(0x104, -38330, -4000, -48020, 180)
    SetChrPos(0x160, -38600, -4000, -44830, 180)

    label("loc_31B0")

    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -40040, -6000, -60700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x10, 0x2F)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x1000)
    SetChrPos(0x10, -39960, -6000, -63090, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x1, 0x0, 0x10, 0x140, 0, 700, 0, 0, 0, 0, 1750, 1750, 1750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -56560, -6000, -76920, 0)
    SetChrPos(0xA, -54610, -6000, -78160, 0)
    SetChrPos(0xB, -53190, -6000, -76380, 0)
    SetChrPos(0xC, -58360, -6000, -77640, 0)
    SetChrPos(0xD, -62210, -6000, -69920, 0)
    SetChrPos(0xE, -61950, -6000, -64470, 0)
    ModifyEventFlags(0, 1, 0x80)
    OP_68(-37980, -3400, -45910, 0)
    MoveCamera(51, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    OP_68(-37980, -3400, -47410, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E4")

    ChrTalk(
        0x101,
        "#3400626V#0002F#5PThere he is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B4")

    label("loc_34E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351B")

    ChrTalk(
        0x102,
        "#3400627V#0102F#5POh, finally!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B4")

    label("loc_351B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3563")

    ChrTalk(
        0x103,
        "#3400628V#0202F#5PTarget located and confirmed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B4")

    label("loc_3563")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B4")

    ChrTalk(
        0x104,
        "#3400629V#0302F#5PLet's get this kid home to his parents, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_35B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3918")
    OP_68(-40310, -5300, -61630, 2500)
    MoveCamera(45, 20, 0, 2500)
    SetCameraDistance(19360, 2500)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3400630V#3809F#5PAhahaha!\x02\x03",
            "#3400631V#3802FWaaaaait! Don't go!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-42080, -5300, -61840, 9000)
    BeginChrThread(0x8, 3, 0, 35)
    BeginChrThread(0x10, 3, 0, 36)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x10, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(-40200, -5300, -60040, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21180, 0)
    SetCameraDistance(20180, 3000)
    SetChrPos(0x101, -40200, -6000, -58030, 180)
    SetChrPos(0x102, -38920, -6000, -57280, 180)
    SetChrPos(0x103, -38930, -5770, -55090, 180)
    SetChrPos(0x104, -37290, -5600, -54400, 180)
    SetChrPos(0x160, -37390, -6000, -56350, 180)
    BeginChrThread(0x103, 3, 0, 21)
    BeginChrThread(0x104, 3, 0, 22)
    BeginChrThread(0x101, 3, 0, 23)
    BeginChrThread(0x102, 3, 0, 24)
    BeginChrThread(0x160, 3, 0, 25)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3400632V#0012F#11PHe was chasing a butterfly this\x01",
            "entire time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400633V#0309F#11PSure is an adventurer, ain't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400634V#3308F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400635V#0102F#11PWell, we should probably put an end to this\x01",
            "particular adventure, wouldn't you say?\x02",
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
    Sleep(50)
    OP_63(0x160, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3400636V#0105F#11PAidios, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400637V#0201F#11PMonsters sighted!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)

    label("loc_3918")

    Fade(500)
    OP_68(-56670, -4900, -65600, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21710, 0)
    SetCameraDistance(20710, 2500)
    SetChrPos(0x8, -49720, -6000, -62980, 270)
    SetChrPos(0x10, -52640, -6000, -64410, 270)

    def lambda_397B():
        OP_95(0xFE, -56570, -6000, -65650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_397B)

    def lambda_3995():
        OP_95(0xFE, -56570, -6000, -65650, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3995)
    WaitChrThread(0x10, 1)

    def lambda_39B3():
        OP_95(0xFE, -56810, -6000, -74480, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_39B3)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x12C)
    WaitChrThread(0x10, 1)
    StopEffect(0x0, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Sound(836, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-58670, -4900, -65600, 1000)
    SetCameraDistance(23500, 1000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    BeginChrThread(0x9, 3, 0, 29)
    Sleep(150)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0xA, 3, 0, 30)
    Sleep(50)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xB, 3, 0, 31)
    Sleep(100)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 3, 0, 32)
    Sleep(150)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 3, 0, 33)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x12C)

    ChrTalk(
        0x8,
        "#3400638V#3800F#11PHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    OP_68(-43050, -5300, -60890, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20080, 0)
    OP_68(-41050, -5300, -60890, 1500)
    SetChrPos(0x101, -42730, -6000, -61720, 270)
    SetChrPos(0x102, -40700, -6000, -59430, 270)
    SetChrPos(0x103, -41600, -6000, -62430, 270)
    SetChrPos(0x104, -39410, -6000, -60380, 270)
    SetChrPos(0x160, -39980, -6000, -62730, 270)
    OP_6F(0x79)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#3400639V#0007F#11PThis is bad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400640V#0301F#11PNo time to think! Just go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400641V#0110F#11PWe have to keep them away from Colin!\x02",
    )

    CloseMessageWindow()
    OP_68(-39730, -5300, -62460, 1000)
    OP_6F(0x79)

    ChrTalk(
        0x160,
        "#3400642V#3307F#11PNo!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(19080, 0)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(-43050, -5300, -60890, 3000)
    SetCameraDistance(22080, 3000)
    BeginChrThread(0x160, 3, 0, 38)
    Sleep(1000)
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
        "#3400643V#0011F#11PWait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400644V#0205F#11PRenne!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-57200, -5400, -67220, 0)
    MoveCamera(325, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24800, 0)
    MoveCamera(335, 25, 0, 2000)
    SetCameraDistance(22300, 2000)
    SetChrPos(0x8, -57200, -6000, -67220, 180)
    SetChrPos(0x160, -44270, -6000, -64030, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 27)
    SetChrPos(0x9, -59130, -6000, -62650, 135)
    SetChrPos(0xA, -61560, -6000, -66330, 90)
    SetChrPos(0xB, -60830, -6000, -70180, 45)
    SetChrPos(0xC, -58140, -6000, -72810, 0)
    SetChrPos(0xD, -55020, -6000, -71640, 315)
    SetChrPos(0xE, -53670, -6000, -69290, 315)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        "#3400645V#3805F#11PWh-Whaaaaaaah...! Mamaaaaa!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x160,
        "#3400646V#3307F#4S#1PI said, STAY AWAY FROM HIM!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-52990, -5200, -63660, 2000)
    MoveCamera(13, 22, 0, 2000)
    SetCameraDistance(18000, 2000)
    BeginChrThread(0x160, 3, 0, 39)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0xF, 0x2C)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x160, 3, 0, 40)
    WaitChrThread(0x160, 3)

    ChrTalk(
        0x8,
        "#3400647V#3805F...\x02",
    )

    CloseMessageWindow()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-57360, -4800, -67530, 1200)
    MoveCamera(19, 19, 0, 1200)
    OP_6E(510, 1200)
    SetCameraDistance(16309, 1200)
    BeginChrThread(0x160, 3, 0, 43)

    def lambda_3FE3():
        OP_95(0xFE, -54950, -6000, -66690, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FE3)
    Sleep(100)

    def lambda_4000():
        OP_95(0xFE, -53310, -6000, -64470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4000)
    Sleep(100)

    def lambda_401D():
        OP_95(0xFE, -53510, -6000, -66840, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_401D)
    Sleep(100)

    def lambda_403A():
        OP_95(0xFE, -51780, -6000, -64870, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_403A)
    WaitChrThread(0x160, 3)
    BeginChrThread(0x160, 3, 0, 44)
    OP_6F(0x79)
    OP_68(-56410, -4800, -67290, 1500)
    SetCameraDistance(20280, 1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 3)
    OP_6F(0x79)

    ChrTalk(
        0x160,
        "#3400648V#3308F#12PEveryone, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400649V#0007F#11PLeave it to us, Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400650V#0307F#11PTime to clean house!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17280, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetChrBattleFlags(0x160, 0x8)
    Battle("BattleInfo_6B0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 34)
    Return()

    # Function_20_2F4E end

    def Function_21_4152(): pass

    label("Function_21_4152")


    def lambda_4157():
        OP_95(0xFE, -41310, -6000, -59840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4157)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_4152 end

    def Function_22_4178(): pass

    label("Function_22_4178")


    def lambda_417D():
        OP_95(0xFE, -39470, -6000, -59420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_417D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_4178 end

    def Function_23_419E(): pass

    label("Function_23_419E")


    def lambda_41A3():
        OP_95(0xFE, -42730, -6000, -61720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41A3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_419E end

    def Function_24_41C4(): pass

    label("Function_24_41C4")


    def lambda_41C9():
        OP_95(0xFE, -41410, -6000, -61870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41C9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_41C4 end

    def Function_25_41EA(): pass

    label("Function_25_41EA")


    def lambda_41EF():
        OP_95(0xFE, -39610, -6000, -61340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41EF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_25_41EA end

    def Function_26_4210(): pass

    label("Function_26_4210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_422B")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_26_4210")

    label("loc_422B")

    Return()

    # Function_26_4210 end

    def Function_27_422C(): pass

    label("Function_27_422C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_424A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_27_422C")

    label("loc_424A")

    Return()

    # Function_27_422C end

    def Function_28_424B(): pass

    label("Function_28_424B")

    EndChrThread(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4293():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4293)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_28_424B end

    def Function_29_42C1(): pass

    label("Function_29_42C1")

    SetChrPos(0xFE, -72040, -2800, -70380, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_42EF():
        OP_9D(0xFE, 0xFFFEF8F4, 0xFFFFECDC, 0xFFFEEC9C, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42EF)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_4332():
        OP_9D(0xFE, 0xFFFF0D26, 0xFFFFE890, 0xFFFEF642, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4332)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_29_42C1 end

    def Function_30_437A(): pass

    label("Function_30_437A")

    SetChrPos(0xFE, -74740, -2800, -62070, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_43A8():
        OP_9D(0xFE, 0xFFFEF16A, 0xFFFFECDC, 0xFFFF09FC, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43A8)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_43E5():
        OP_9D(0xFE, 0xFFFF0998, 0xFFFFE890, 0xFFFF0718, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E5)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_30_437A end

    def Function_31_4427(): pass

    label("Function_31_4427")

    SetChrPos(0xFE, -69850, -2800, -57770, 90)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_4455():
        OP_9D(0xFE, 0xFFFF1BC2, 0xFFFFE890, 0xFFFF13B6, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4455)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_31_4427 end

    def Function_32_449E(): pass

    label("Function_32_449E")

    SetChrPos(0xFE, -71660, -2900, -73300, 135)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)

    def lambda_44CC():
        OP_9D(0xFE, 0xFFFF03B2, 0xFFFFECDC, 0xFFFEDC98, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44CC)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_4509():
        OP_9D(0xFE, 0xFFFF19CE, 0xFFFFE890, 0xFFFEEB8E, 0x2BC, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4509)
    WaitChrThread(0xFE, 1)
    Sound(832, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    OP_93(0xFE, 0x2D, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_32_449E end

    def Function_33_4558(): pass

    label("Function_33_4558")

    SetChrPos(0xFE, -55440, -6000, -76280, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_457C():
        OP_95(0xFE, -54700, -6000, -70010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_457C)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_33_4558 end

    def Function_34_45B3(): pass

    label("Function_34_45B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch07200.itc", 0x26)
    LoadChrToIndex("apl/ch50341.itc", 0x2D)
    LoadChrToIndex("apl/ch50364.itc", 0x30)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    ClearChrBattleFlags(0x160, 0x8)
    OP_52(0x160, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-54870, -4600, -64980, 0)
    MoveCamera(356, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21020, 0)
    SetChrPos(0x101, -53640, -6000, -65700, 270)
    SetChrPos(0x102, -52260, -6000, -66520, 270)
    SetChrPos(0x103, -51370, -6000, -64550, 270)
    SetChrPos(0x104, -49730, -6000, -65160, 270)
    SetChrPos(0x160, -55310, -6000, -77360, 270)
    SetChrChipByIndex(0x160, 0x2D)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0x160, 0, 0, 45)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -55310, -6000, -77360, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(19020, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3400651V#0006F#11PPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400652V#0306F#2PThat could've turned out reeeeeal bad.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#3400653V#0101F#11PYou're right. But, wait... What about\x01",
            "Renne and Colin?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    def lambda_486D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_486D)

    def lambda_487A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_487A)
    Sleep(100)

    def lambda_488A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_488A)

    def lambda_4897():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4897)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(1000)
    SetChrPos(0x101, -55430, -6000, -70010, 180)
    SetChrPos(0x102, -56590, -6000, -69430, 180)
    SetChrPos(0x103, -55010, -6000, -68390, 180)
    SetChrPos(0x104, -55580, -6000, -67260, 180)
    OP_68(-55580, -4500, -75880, 0)
    MoveCamera(36, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16870, 0)
    OP_68(-55580, -5200, -75880, 3000)

    def lambda_493C():
        OP_95(0xFE, -55430, -6000, -75010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_493C)

    def lambda_4956():
        OP_95(0xFE, -56590, -6000, -74430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4956)

    def lambda_4970():
        OP_95(0xFE, -55010, -6000, -73390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4970)

    def lambda_498A():
        OP_95(0xFE, -55580, -6000, -72260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_498A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x8,
        "#3400654V#3805F#12P#40W*sniff*\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0x160,
        (
            "#3400655V#3308F#5P#30WIt's okay. Everything will be all right now.\x02\x03",
            "#3400656V#3306FThese nice people took care of all those\x01",
            "big, scary monsters for you.\x02\x03",
            "#3400657V#3300FYou can relax now, okay? Please don't cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3400658V#3810F#60W#12P*sniff*... *hic*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400659V#3305F#5PW-Wait, why are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3400660V#3810F#60W#12PB-B-But, I j-just wanted... *sniff*\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x8,
        "#3400661V#3811F#4S#12PWh-Whaaaaaaaaah!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    BeginChrThread(0x160, 0, 0, 46)
    Sleep(500)

    ChrTalk(
        0x160,
        (
            "#3400662V#3311F#5P#30WWh-Why are you crying?! I already said\x01",
            "nothing is going to hurt you anymore...\x02\x03",
            "#3400663V#3308F#40WYou... You're...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x160,
        "#3400664V#3310F#5P#4SI never meant to save you...!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x160, 0x0)
    SetChrSubChip(0x160, 0xB)

    ChrTalk(
        0x101,
        "#3400665V#0008F#5PYou did the right thing, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400666V#0208F#5PRenne, are you...?\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x160, 0x5DC, 0x4, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x160,
        (
            "#3400667V#3310F#5PMoronic! How utterly, completely moronic!\x02\x03",
            "#3400668V#30WI just wanted to observe him...!\x01",
            "I never wanted to get involved, and yet...!\x02\x03",
            "#3400669V#3313F#30WWhy...? Why did I do it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3400670V#0108F#5PRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400671V#0003F#5P...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15370, 3000)
    OP_68(-54730, -5200, -76500, 3000)

    def lambda_4E2C():
        OP_96(0xFE, 0xFFFF2D1A, 0xFFFFE890, 0xFFFED220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E2C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x12C)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x5)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3400672V#0004F#11PI can't pretend to know or understand your\x01",
            "circumstances, Renne.\x02\x03",
            "#3400673V#0000FBut, I think it's clear that you acted\x01",
            "to save someone you care about.\x02\x03",
            "#3400674VWith your own two hands.\x02\x03",
            "#3400675V#0004FAnd if you don't believe me, look no further\x01",
            "than the boy crying in your arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3400676V#3312F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400677V#0006F#11PYou pulled most of the weight here.\x01",
            "We were basically your backup.\x02\x03",
            "#3400678V#0000FBut, still... I'm glad we were here.\x02\x03",
            "#3400679V#0002FIt was an honor to help you, Renne... To help\x01",
            "you protect what's important to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x160, 0x708, 0x4, 0x15, 0x16, 0x15, 0x14)
    Sleep(150)
    OP_A1(0x160, 0x4B0, 0x8, 0x15, 0x16, 0x15, 0x14, 0x15, 0x16, 0x15, 0x14)
    Sleep(300)

    ChrTalk(
        0x160,
        "#3400680V#3313F#60W#5PWh-What's important...? I-I...I don't...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(20000, 4000)
    Sound(804, 0, 100, 0)
    OP_A1(0x160, 0x7D0, 0x3, 0x5, 0x6, 0x7)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x160,
        "#3400681V#3310F#4S#5P#70W#25AWaaaaaaaaah!\x02",
    )


    ChrTalk(
        0x8,
        "#3811F#4S#12P#70W#25AWaaaaaaaaah!\x02",
    )

    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_45B3 end

    def Function_35_51B5(): pass

    label("Function_35_51B5")


    def lambda_51BA():
        OP_95(0xFE, -39960, -6000, -63090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51BA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(100)

    def lambda_51EC():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51EC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(100)

    def lambda_521E():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_521E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(200)

    def lambda_5250():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5250)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_35_51B5 end

    def Function_36_526A(): pass

    label("Function_36_526A")


    def lambda_526F():
        OP_95(0xFE, -42950, -6000, -63260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_526F)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_5290():
        OP_95(0xFE, -45050, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5290)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_52B1():
        OP_95(0xFE, -51480, -6000, -61950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52B1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_526A end

    def Function_37_52CB(): pass

    label("Function_37_52CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52E6")
    OP_A1(0xFE, 0x1388, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_37_52CB")

    label("loc_52E6")

    Return()

    # Function_37_52CB end

    def Function_38_52E7(): pass

    label("Function_38_52E7")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x4)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_5306():
        OP_9D(0xFE, 0xFFFF54B6, 0xFFFFE890, 0xFFFF0178, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5306)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)

    def lambda_533A():
        OP_95(0xFE, -53880, -6000, -64819, 15000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_533A)
    Sound(250, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_38_52E7 end

    def Function_39_5370(): pass

    label("Function_39_5370")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)
    BeginChrThread(0xFE, 0, 0, 37)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_5395():
        OP_95(0xFE, -52890, -6000, -63420, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5395)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0x160, 0xB4, 0x320)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0x160, 0x2B)
    SetChrSubChip(0x160, 0x0)
    Return()

    # Function_39_5370 end

    def Function_40_53D4(): pass

    label("Function_40_53D4")

    SetChrChipByIndex(0x160, 0x2B)
    SetChrSubChip(0x160, 0x0)
    Sound(540, 0, 100, 0)
    Sound(804, 0, 100, 0)
    SetCameraDistance(15500, 1000)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    OP_6F(0x79)
    OP_A1(0xFE, 0xFA0, 0x1, 0x3)
    OP_68(-54280, -4700, -69480, 750)
    MoveCamera(13, 18, 0, 750)
    SetCameraDistance(21840, 750)
    Sound(912, 0, 100, 0)
    OP_82(0x96, 0x0, 0x1B58, 0x5DC)
    BeginChrThread(0xF, 3, 0, 41)
    OP_A1(0xFE, 0x7D0, 0x1, 0x4)
    Sleep(400)
    BeginChrThread(0xE, 3, 0, 28)
    Sound(502, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 28)
    Sound(502, 0, 100, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-52990, -5200, -63660, 2000)
    MoveCamera(13, 22, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sleep(1500)
    OP_A1(0xFE, 0x7D0, 0x3, 0x5, 0x6, 0x7)
    WaitChrThread(0xF, 3)
    OP_82(0x64, 0x0, 0x1B58, 0x12C)
    Fade(250)
    SetChrSubChip(0x160, 0x0)
    OP_0D()
    OP_6F(0x79)
    Return()

    # Function_40_53D4 end

    def Function_41_54C2(): pass

    label("Function_41_54C2")

    PlayEffect(0x2, 0x1, 0xFE, 0x40, 0, -800, 0, 0, 0, 0, 1750, 1000, 1750, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x800)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xFE, 0, 0, 42)
    SetChrPos(0xFE, -52890, -6000, -63420, 270)

    def lambda_5525():
        OP_96(0xFE, 0xFFFF2644, 0xFFFFE890, 0xFFFED626, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5525)
    WaitChrThread(0xFE, 1)

    def lambda_5543():
        OP_96(0xFE, 0xFFFF3166, 0xFFFFE890, 0xFFFF0844, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5543)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    StopEffect(0x1, 0x2)
    Return()

    # Function_41_54C2 end

    def Function_42_5574(): pass

    label("Function_42_5574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5592")
    OP_A1(0xFE, 0x1B58, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_42_5574")

    label("loc_5592")

    Return()

    # Function_42_5574 end

    def Function_43_5593(): pass

    label("Function_43_5593")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0x160, 0x2A)
    SetChrSubChip(0x160, 0x0)

    def lambda_55A5():
        OP_95(0xFE, -57200, -6000, -67220, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55A5)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_43_5593 end

    def Function_44_55C8(): pass

    label("Function_44_55C8")

    Fade(250)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x12)
    Sound(804, 0, 100, 0)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sound(854, 0, 100, 0)

    def lambda_5606():
        OP_9D(0xFE, 0xFFFF3576, 0xFFFFE890, 0xFFFEF2BE, 0x2BC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5606)
    WaitChrThread(0xFE, 1)
    Sound(31, 0, 100, 0)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_44_55C8 end

    def Function_45_5633(): pass

    label("Function_45_5633")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5651")
    OP_A1(0xFE, 0x3E8, 0x5, 0x8, 0x9, 0xA, 0x9, 0x0)
    Sleep(4000)
    Jump("Function_45_5633")

    label("loc_5651")

    Return()

    # Function_45_5633 end

    def Function_46_5652(): pass

    label("Function_46_5652")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_566F")
    OP_A1(0xFE, 0x5DC, 0x4, 0xB, 0xC, 0xD, 0xC)
    Sleep(3000)
    Jump("Function_46_5652")

    label("loc_566F")

    Return()

    # Function_46_5652 end

    def Function_47_5670(): pass

    label("Function_47_5670")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_68(-57720, -5200, -61820, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, -57910, -6000, -62950, 270)
    SetChrPos(0x102, -58320, -6000, -61520, 225)
    SetChrPos(0x103, -57190, -6000, -63960, 270)
    SetChrPos(0x104, -56700, -6000, -61250, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5725")
    SetChrPos(0x10A, -56130, -6000, -61940, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5725")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x349),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x349, 1)

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, aren't these yellow ones the\x01",
            "Leevus Flowers we've been\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FProbably a real pain for regular folk to\x01",
            "pick 'em 'cause of the location, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FIt IS right in front of the police academy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FConsidering how far apart these flowerbeds\x01",
            "are scattered throughout Crossbell, it's fairly\x01",
            "difficult to gather a three-color bouquet.\x02\x03",
            "#0100FAnd that's why most graves today are\x01",
            "decorated with a single type of flower.\x02\x03",
            "Three-color bouquets are usually\x01",
            "saved for funeral services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0305FHuh. Learn somethin' new everyday.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A07")

    ChrTalk(
        0x10A,
        "#11P#0603FI suppose it's a sign of the changing times.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A3F")

    label("loc_5A07")


    ChrTalk(
        0x103,
        "#12P#0200FTraditions must face reality eventually.\x02",
    )

    CloseMessageWindow()

    label("loc_5A3F")


    ChrTalk(
        0x101,
        "#12P#0003FYeah, I guess that's true.\x02",
    )

    CloseMessageWindow()
    OP_65(0x9, 0x1)
    OP_29(0x2E, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A96")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_5A96")

    ClearMapFlags(0x8000000)
    OP_37()
    Call(0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AB9")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5AB9")

    SetChrPos(0x0, -57910, -6000, -62950, 270)
    EventEnd(0x5)
    Return()

    # Function_47_5670 end

    def Function_48_5ACD(): pass

    label("Function_48_5ACD")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThe voice wasn't coming from this direction.\x01",
            "We need to head south!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -32500, 0, 26090, 225)
    EventEnd(0x4)
    Return()

    # Function_48_5ACD end

    def Function_49_5B35(): pass

    label("Function_49_5B35")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　CPA\x01",
            "Crossbell Police Academy\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63CC")
    EventBegin(0x0)
    SetChrFlags(0x1D, 0x80)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    Fade(500)
    OP_68(-49100, -5400, -95960, 0)
    MoveCamera(123, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24710, 0)
    SetChrPos(0x101, -53560, -6000, -80120, 180)
    SetChrPos(0x102, -54580, -6000, -78550, 180)
    SetChrPos(0x103, -51530, -6000, -79120, 180)
    SetChrPos(0x104, -52490, -6000, -77690, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C48")
    SetChrPos(0x10A, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5C48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C73")
    SetChrPos(0x109, -51490, -6000, -76540, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5C73")

    OP_0D()
    OP_68(-50470, -5400, -82530, 6000)
    MoveCamera(134, 26, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(24710, 6000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#0100FThe police academy is just beyond\x01",
            "this road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FI believe Lloyd enrolled at this academy\x01",
            "to earn his detective's license.\x02\x03",
            "#0202FI have heard it is fully fitted with a\x01",
            "plethora of training equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FYeah. Not only that, but it also functions as a\x01",
            "joint training facility for the CPD and CGF.\x02\x03",
            "#0000FThere's a long winding path through the forest,\x01",
            "along with various training grounds just past\x01",
            "the gate.\x02\x03",
            "#0012FActually, I've never made the trip on foot before.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F2D")

    def lambda_5EA5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EA5)
    Sleep(60)

    def lambda_5EB5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EB5)
    Sleep(60)

    def lambda_5EC5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EC5)
    Sleep(60)

    def lambda_5ED5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5ED5)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_5FCD")

    label("loc_5F2D")


    def lambda_5F32():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F32)
    Sleep(60)

    def lambda_5F42():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F42)
    Sleep(60)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FCA")

    def lambda_5FAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FAA)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_5FCA")

    Sleep(1000)

    label("loc_5FCD")


    ChrTalk(
        0x102,
        "#0105FYou haven't?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0000F#11PWell, when I first arrived at the academy, I hitched\x01",
            "a ride with a freighter that was headed there.\x02\x03",
            "And I'd trapped myself in the dorms for the\x01",
            "following months after.\x02\x03",
            "#0006FI had no choice but to spend my entire\x01",
            "time studying for the detective exam.\x01",
            "I even had to give up my holidays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOh, I never realized it was that difficult...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYou're yankin' my chain, right, Lloyd?\x01",
            "That's no way for a guy to live!\x02\x03",
            "#0309FYou gotta ditch the textbooks during the\x01",
            "weekend, my man. What better time to\x01",
            "experience the nightlife at its fullest?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206FI believe those crude standards apply\x01",
            "only to a certain redheaded man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F#11PH-Haha...\x02\x03",
            "#0008F(I'd kept telling myself I couldn't return\x01",
            "to Crossbell City until I'd passed the\x01",
            "exam and earned my license.)\x02\x03",
            "#0006F(And the more I think back on it,\x01",
            "the more childish it sounds...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6396")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_6396")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63B0")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_63B0")

    SetScenarioFlags(0x95, 4)
    SetChrPos(0x0, -52380, -6000, -78750, 180)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)

    label("loc_63CC")

    TalkEnd(0xFF)
    Return()

    # Function_49_5B35 end

    def Function_50_63D0(): pass

    label("Function_50_63D0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "East: Crossbell City - 137 selge\x01",
            "West: Bellguard Gate - 61 selge\x01",
            "South: Crossbell Police Academy - 31 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_50_63D0 end

    SaveToFile()

Try(main)
