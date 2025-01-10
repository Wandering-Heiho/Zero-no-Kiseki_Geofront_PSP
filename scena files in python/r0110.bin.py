from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0110.bin",                # FileName
        "r0110",                    # MapName
        "r0110",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0110", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 4, 0, 5],
    )

    BuildStringList((
        "r0110",                  # 0
        "Tour Guide",             # 1
        "Tourist Qiulan",         # 2
        "Tourist Walt",           # 3
        "Tourist Seifer",         # 4
        "Tourist Aleut",          # 5
        "Tourist Teany",          # 6
        "Bus",                    # 7
        "飲み物",                 # 8
        "飲み物",                 # 9
        "飲み物",                 # 10
        "飲み物",                 # 11
        "SE制御",                 # 12
        "br0100",                 # 13
        "br0100",                 # 14
        "br0100",                 # 15
        "br0100",                 # 16
        "br0100",                 # 17
        "br0100",                 # 18
        "br0100",                 # 19
        "To Crossbell City & Tangram Gate",# 20
        "To Armorica Village",    # 21
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 1,   7,   0,   3,   0,   1,   5)
    Sepith("Sepith_B4", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_C4", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_D4", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_E4", 0,   2,   0,   7,   3,   5,   0)
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
    MonsterBattlePostion("MonsterBattlePostion_164", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_184", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms64500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms64500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_24C", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_B4", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2E8", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62200.dat", "ms61800.dat", "ms62200.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3B0", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_44C", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_E4", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4E8", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_584", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66801.dat", "ms66801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_164", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch32500.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch33102.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch23900.itc",                   # 05
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
        "monster/ch66850.itc",               # 1A
        "monster/ch66851.itc",               # 1B
        "monster/ch76250.itc",               # 1C
        "monster/ch76251.itc",               # 1D
    ))

    DeclNpc(-43049,  3000,    72669,   270,  385,  0x0, 0,   0,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-27329,  5000,    98910,   315,  385,  0x0, 0,   1,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(-34709,  5000,    83029,   270,  385,  0x0, 0,   2,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(-25319,  5199,    86550,   180,  405,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-29319,  5000,    79690,   225,  385,  0x0, 0,   4,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-16520,  5000,    87919,   45,   385,  0x0, 0,   5,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16030,  21390,   1050,    0x1010000,    "BattleInfo_184", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-650,    34640,   2009,    0x1010000,    "BattleInfo_24C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-43390,  58440,   3000,    0x1010000,    "BattleInfo_2E8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-33100,  91170,   3000,    0x1010000,    "BattleInfo_3B0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-50950,  128690,  1800,    0x1010000,    "BattleInfo_44C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-62740,  137000,  -410,    0x1010000,    "BattleInfo_184", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-67430,  109860,  40,      0x1010000,    "BattleInfo_24C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-90980,  120410,  -1000,   0x1010000,    "BattleInfo_2E8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-97230,  131570,  -1000,   0x1010000,    "BattleInfo_3B0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-13090,  34470,   2009,    0x1010000,    "BattleInfo_4E8", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-57690,  66190,   3000,    0x1010000,    "BattleInfo_4E8", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-58220,  121570,  860,     0x1010000,    "BattleInfo_4E8", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-66530,  110660,  840,     0x1850000,    "BattleInfo_584", 0,   26,  0xFFFF, 8,  9)

    DeclEvent(0x0000, 0, 20,  -56.0,                 67.5,                  2.0,                   1406.25,               [0.06666666269302368,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.733333110809326,     -13.5,                 -0.4000000059604645,   1.0])
    DeclEvent(0x0040, 0, 9,   -66.52999877929688,    110.66000366210938,    0.03999999910593033,   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   8.31624984741211,      -13.832500457763672,   -0.009999999776482582, 1.0])

    DeclActor(-35330,  3000,    58260,   1200,    -35330,  4000,    58260,   0x007C, 0,  6,  0x0000)
    DeclActor(-96800,  -1000,   121110,  1200,    -96800,  0,       121110,  0x007C, 0,  7,  0x0000)
    DeclActor(-98580,  1000,    157750,  1200,    -98580,  2000,    157750,  0x007C, 0,  8,  0x0000)
    DeclActor(-15380,  5000,    78030,   1200,    -11760,  1000,    74380,   0x007C, 0,  19, 0x0000)
    DeclActor(-30440,  5000,    73410,   1200,    -30440,  6500,    73410,   0x007C, 0,  22, 0x0000)
    DeclActor(-47130,  2040,    113100,  1200,    -47130,  2040,    113100,  0x007C, 0,  10, 0x0000)
    DeclActor(-12680,  10,      9680,    1200,    -12680,  10,      9680,    0x007C, 0,  11, 0x0000)
    DeclActor(-16850,  5000,    89750,   1000,    -16850,  6500,    89750,   0x007C, 0,  23, 0x0000)
    DeclActor(-15850,  5000,    88750,   1000,    -15850,  6500,    88750,   0x007C, 0,  23, 0x0000)

    PlaceName(-1.3899999856948853, 0.0, -33.0, 0x0000, 0x0000, "To Crossbell City & Tangram Gate")
    PlaceName(-88.0, 0.0, 178.0, 0x0000, 0x0000, "To Armorica Village")

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
        "Function_0_C4C",          # 00, 0
        "Function_1_C6B",          # 01, 1
        "Function_2_D23",          # 02, 2
        "Function_3_D4E",          # 03, 3
        "Function_4_D79",          # 04, 4
        "Function_5_DCE",          # 05, 5
        "Function_6_152C",         # 06, 6
        "Function_7_1689",         # 07, 7
        "Function_8_17F4",         # 08, 8
        "Function_9_199C",         # 09, 9
        "Function_10_1BF4",        # 0A, 10
        "Function_11_1C08",        # 0B, 11
        "Function_12_1C1C",        # 0C, 12
        "Function_13_1C3A",        # 0D, 13
        "Function_14_1D80",        # 0E, 14
        "Function_15_1F41",        # 0F, 15
        "Function_16_206E",        # 10, 16
        "Function_17_22C7",        # 11, 17
        "Function_18_23FF",        # 12, 18
        "Function_19_2598",        # 13, 19
        "Function_20_2869",        # 14, 20
        "Function_21_4207",        # 15, 21
        "Function_22_4220",        # 16, 22
        "Function_23_42B7",        # 17, 23
    ))


    def Function_0_C4C(): pass

    label("Function_0_C4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C6A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_C4C")

    label("loc_C6A")

    Return()

    # Function_0_C4C end

    def Function_1_C6B(): pass

    label("Function_1_C6B")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_CAB"),
        (1, "loc_CB7"),
        (2, "loc_CC3"),
        (3, "loc_CCF"),
        (4, "loc_CDB"),
        (5, "loc_CE7"),
        (6, "loc_CF3"),
        (SWITCH_DEFAULT, "loc_CFF"),
    )


    label("loc_CAB")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CB7")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CC3")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CCF")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CDB")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CE7")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CF3")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_CFF")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_D0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D22")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D0B")

    label("loc_D22")

    Return()

    # Function_1_C6B end

    def Function_2_D23(): pass

    label("Function_2_D23")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4D")
    OP_94(0xFE, 0xFFFF9598, 0x18DB2, 0xFFFF9372, 0x175CA, 0x3E8)
    Sleep(300)
    Jump("Function_2_D23")

    label("loc_D4D")

    Return()

    # Function_2_D23 end

    def Function_3_D4E(): pass

    label("Function_3_D4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D78")
    OP_94(0xFE, 0xFFFF8D82, 0x12A52, 0xFFFF8BC0, 0x14546, 0x3E8)
    Sleep(300)
    Jump("Function_3_D4E")

    label("loc_D78")

    Return()

    # Function_3_D4E end

    def Function_4_D79(): pass

    label("Function_4_D79")

    Call(0, 12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D97")
    SetChrFlags(0x1A, 0x8)

    label("loc_D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCD")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_DCD")

    Return()

    # Function_4_D79 end

    def Function_5_DCE(): pass

    label("Function_5_DCE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE6")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DE6")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_131A")
    SetChrFlags(0x20, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_132E")

    label("loc_131A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")
    ClearChrFlags(0x20, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_132E")

    OP_52(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x20, 0x100)
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139A")
    OP_65(0x3, 0x1)

    label("loc_139A")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -11760, 1000, 74380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7")
    OP_70(0x0, 0x0)
    Jump("loc_13FB")

    label("loc_13F7")

    OP_70(0x0, 0x1E)

    label("loc_13FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140E")
    OP_70(0x1, 0x0)
    Jump("loc_1412")

    label("loc_140E")

    OP_70(0x1, 0x1E)

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1425")
    OP_70(0x2, 0x0)
    Jump("loc_1429")

    label("loc_1425")

    OP_70(0x2, 0x1E)

    label("loc_1429")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 2)), scpexpr(EXPR_END)), "loc_148F")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -47130, 2040, 113100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_14E8")

    label("loc_148F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 3)), scpexpr(EXPR_END)), "loc_14E8")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -12680, 10, 9680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_14E8")

    SoundDistance(0x7B, 0xFFFFCD1A, 0x1388, 0x10946, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E1(0xFFFFDE0E, 0x1388, 0x14712)
    OP_E1(0xFFFFEBBA, 0x1388, 0x25B48)
    OP_E1(0xFFFE3EDC, 0x1388, 0x28EC4)
    Return()

    # Function_5_DCE end

    def Function_6_152C(): pass

    label("Function_6_152C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1616")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x40, 1)"), scpexpr(EXPR_END)), "loc_15AC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1611")

    label("loc_15AC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x40),
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

    label("loc_1611")

    Jump("loc_167D")

    label("loc_1616")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty and exercises its right to remain silent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_167D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_152C end

    def Function_7_1689(): pass

    label("Function_7_1689")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1773")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_1709")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_176E")

    label("loc_1709")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
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

    label("loc_176E")

    Jump("loc_17E8")

    label("loc_1773")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A bracer assaulting a chest, I can understand.\x01",
            "But a cop? That's low, man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_17E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1689 end

    def Function_8_17F4(): pass

    label("Function_8_17F4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DE")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8A, 1)"), scpexpr(EXPR_END)), "loc_1874")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_18D9")

    label("loc_1874")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
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

    label("loc_18D9")

    Jump("loc_1990")

    label("loc_18DE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If my wish comes true, I want to become a bird.\x01",
            "Even if I lose everything else, someday I want\x01",
            "to go to the place of memories with him.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1990")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17F4 end

    def Function_9_199C(): pass

    label("Function_9_199C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 5)), scpexpr(EXPR_END)), "loc_19A6")
    Return()

    label("loc_19A6")

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
        (1, "loc_1A89"),
        (SWITCH_DEFAULT, "loc_1AA0"),
    )


    label("loc_1A89")

    Sleep(500)
    OP_90(0x0, -63920, 350, 114420, 45)
    EventEnd(0x5)
    Return()

    label("loc_1AA0")

    Battle("BattleInfo_584", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-63920, 1350, 114420, 0)
    OP_90(0x0, -63920, 350, 114420, 45)
    OP_90(0x1, -63920, 350, 114420, 45)
    OP_90(0x2, -63920, 350, 114420, 45)
    OP_90(0x3, -63920, 350, 114420, 45)
    OP_90(0x4, -63920, 350, 114420, 45)
    OP_90(0x5, -63920, 350, 114420, 45)
    OP_90(0x6, -63920, 350, 114420, 45)
    OP_90(0x7, -63920, 350, 114420, 45)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1B62"),
        (1, "loc_1B65"),
        (SWITCH_DEFAULT, "loc_1B68"),
    )


    label("loc_1B62")

    EventEnd(0x5)
    Return()

    label("loc_1B65")

    OP_B7(0x0)
    Return()

    label("loc_1B68")

    SetChrFlags(0x1A, 0x8)
    EventBegin(0x1)
    SetChrFlags(0x20, 0x80)
    ModifyEventFlags(0, 1, 0x80)
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
            "Exterminated monster on Old Armorica Road!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 5)
    OP_29(0x1E, 0x4, 0x10)
    OP_29(0x1E, 0x4, 0x2)
    OP_29(0x1E, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_9_199C end

    def Function_10_1BF4(): pass

    label("Function_10_1BF4")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 2)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_10_1BF4 end

    def Function_11_1C08(): pass

    label("Function_11_1C08")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 3)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_11_1C08 end

    def Function_12_1C1C(): pass

    label("Function_12_1C1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C39")
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    label("loc_1C39")

    Return()

    # Function_12_1C1C end

    def Function_13_1C3A(): pass

    label("Function_13_1C3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")

    ChrTalk(
        0xFE,
        (
            "This is one of the destinations along the\x01",
            "Crossbellan sightseeing tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody at the tour's been having a\x01",
            "great time. Myself included.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D7C")

    label("loc_1CE4")


    ChrTalk(
        0xFE,
        (
            "The spot is especially popular during the\x01",
            "Crossbellan sightseeing tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think everybody's been looking forward\x01",
            "to the tour for a while now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7C")

    TalkEnd(0xFE)
    Return()

    # Function_13_1C3A end

    def Function_14_1D80(): pass

    label("Function_14_1D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8F")

    ChrTalk(
        0xFE,
        (
            "This is great. There's nothing but the\x01",
            "great outdoors around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd only heard Crossbell was a technological\x01",
            "metropolis, so I wasn't expecting such a treat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as I found out, I just had to splurge\x01",
            "on a brand new orbal camera.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F3D")

    label("loc_1E8F")


    ChrTalk(
        0xFE,
        (
            "The scenery out here is gorgeous! It's making it\x01",
            "difficult to decide what kind of photograph to take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad I decided to go all out on a\x01",
            "brand new orbal camera.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3D")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D80 end

    def Function_15_1F41(): pass

    label("Function_15_1F41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFE")

    ChrTalk(
        0xFE,
        (
            "Huh. What do you suppose they're growing\x01",
            "in that field over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Probably fruits, right? Or maybe it's vegetables...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm more of a fruity guy, myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_206A")

    label("loc_1FFE")


    ChrTalk(
        0xFE,
        (
            "Are they growing fruits or vegetables\x01",
            "in that field over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm more of a fruity guy, myself.\x02",
    )

    CloseMessageWindow()

    label("loc_206A")

    TalkEnd(0xFE)
    Return()

    # Function_15_1F41 end

    def Function_16_206E(): pass

    label("Function_16_206E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2102")
    Jump("loc_214C")

    label("loc_2102")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2122")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214C")

    label("loc_2122")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2142")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214C")

    label("loc_2142")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_214C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223A")

    ChrTalk(
        0xFE,
        (
            "Whoops! Accidentally dozed off for a second.\x01",
            "Can you blame me, though? Look at how\x01",
            "perfect the weather is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I love how warm it is... I might accidentally\x01",
            "take a small nap...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22BF")

    label("loc_223A")


    ChrTalk(
        0xFE,
        (
            "No, no! I can't go wasting away a special trip\x01",
            "napping outdoors like I'm some cat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, still... This weather IS gorgeous.\x02",
    )

    CloseMessageWindow()

    label("loc_22BF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_206E end

    def Function_17_22C7(): pass

    label("Function_17_22C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234F")

    ChrTalk(
        0xFE,
        "This is one beautifully built rest area.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anybody unaccustomed to traveling would\x01",
            "deeply appreciate this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23FB")

    label("loc_234F")


    ChrTalk(
        0xFE,
        (
            "You should never take these highway\x01",
            "rest areas for granted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City sure knows how to give\x01",
            "tourists all-star treatment. Credit's given\x01",
            "where credit's due.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FB")

    TalkEnd(0xFE)
    Return()

    # Function_17_22C7 end

    def Function_18_23FF(): pass

    label("Function_18_23FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FB")

    ChrTalk(
        0xFE,
        (
            "I heard this big hunk of metal is\x01",
            "called a vending machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, if you feed this thing mira\x01",
            "and push a button, a drink will come out.\x01",
            "Wow... The future is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't tell me somebody's hiding in that thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2594")

    label("loc_24FB")


    ChrTalk(
        0xFE,
        (
            "This hunk of metal is called a vending machine.\x01",
            "Don't tell me somebody's hiding in that thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If there is, then they're one dedicated worker.\x02",
    )

    CloseMessageWindow()

    label("loc_2594")

    TalkEnd(0xFE)
    Return()

    # Function_18_23FF end

    def Function_19_2598(): pass

    label("Function_19_2598")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FWhat kind of rest area would be complete\x01",
            "without a fishing spot?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-14450, 3800, 76450, 1500)
    MoveCamera(12, 27, 0, 1500)
    OP_6E(500, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2864")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 3)), scpexpr(EXPR_END)), "loc_2694")
    MiniGame(0x6, 0x15, 0xFFFFBFFA, 0x1388, 0x134B6, 0x87, 0xFFFFD210, 0x3E8, 0x1228C)
    Jump("loc_2864")

    label("loc_2694")

    MiniGame(0x6, 0x16, 0xFFFFBFFA, 0x1388, 0x134B6, 0x87, 0xFFFFD210, 0x3E8, 0x1228C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2864")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2864")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-16390, 6500, 79030, 0)
    MoveCamera(25, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    LoadChrToIndex("apl/ch50162.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -16390, 5000, 79030, 135)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x0,
        "Lloyd",
        (
            "#0011FWh-What the heck did I just catch?\x02\x03",
            "#0003FI've never seen a fish so beautiful before.\x01",
            "I feel like it might be kind of rare...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -16390, 5000, 79030, 135)
    SetChrPos(0x2, -16390, 5000, 79030, 135)
    SetChrPos(0x3, -16390, 5000, 79030, 135)
    SetChrPos(0x4, -16390, 5000, 79030, 135)
    SetChrPos(0x5, -16390, 5000, 79030, 135)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x69, 3)

    label("loc_2864")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_19_2598 end

    def Function_20_2869(): pass

    label("Function_20_2869")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x8)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_78(0x3, 0xE)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xE, -41000, 3000, 100200, 190)
    OP_D3(0xE, 0x0, 0xBE, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-37910, 7300, 75370, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30840, 0)
    SetChrPos(0x101, -51380, 3000, 66930, 45)
    SetChrPos(0x104, -53080, 3000, 67090, 45)
    SetChrPos(0x102, -52120, 3000, 66570, 45)
    SetChrPos(0x103, -53840, 3000, 67420, 45)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-37910, 2400, 75370, 5000)
    Sleep(1500)

    def lambda_29C3():
        OP_95(0xFE, -45660, 3000, 71330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29C3)

    def lambda_29DD():
        OP_95(0xFE, -47170, 3000, 71910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29DD)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(-40710, 2400, 74790, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30460, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100326V#0005F#5POh, good timing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100327V#0300F#5PA rest area, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100328V#5P#50WTh-There's a rest area?\x02",
    )

    CloseMessageWindow()
    OP_68(-43440, 2400, 73320, 3000)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_2B07():
        OP_95(0xFE, -48700, 3000, 69060, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B07)
    Sleep(500)

    def lambda_2B24():
        OP_95(0xFE, -49800, 3000, 69800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B24)

    def lambda_2B3E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B3E)

    def lambda_2B4B():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B4B)
    Sound(1176, 255, 100, 0)
    Sleep(1000)
    Sound(1272, 255, 100, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#1100331V#0002F#5PWhy don't we take a break here\x01",
            "before your legs fall off?\x02\x03",
            "#1100332VWe can even admire the view while\x01",
            "we catch our breath. Sound good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100333V#0106F#12P#40WY-Yes, I would love that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100334V#0206F#6P#40WMuch...appreciated...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100335V#0300F#5PWhy not? I'm always game for\x01",
            "a lil' kick back and chill.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50092.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -19300, 5200, 86600, 180)
    SetChrPos(0x102, -17800, 5200, 83300, 0)
    SetChrPos(0x103, -19300, 5200, 83300, 0)
    SetChrPos(0x104, -17800, 5200, 86600, 180)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x3)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0xF, -19300, 5700, 85400, 0)
    SetChrPos(0x10, -17800, 5700, 84500, 0)
    SetChrPos(0x11, -19300, 5700, 84500, 0)
    SetChrPos(0x12, -17800, 5700, 85400, 0)
    FadeToBright(1000, 0)
    OP_68(-73140, 5600, 97250, 0)
    MoveCamera(48, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(43060, 0)
    OP_68(-75530, 5600, 71880, 12000)
    Sleep(10000)
    OP_0D()
    Fade(1000)
    OP_68(-16760, 5300, 86730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21780, 0)
    SetCameraDistance(20280, 3000)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#1100336V#0104F#4P#40WThe breeze is so nice...\x02\x03",
            "#1100337V#0102F#30WAaaahhh... Just what I needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100338V#0202F#12P#40WI completely agree.\x02\x03",
            "#1100339V#0203F#30WI may even fall asleep at this rate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_3144")

    ChrTalk(
        0x101,
        (
            "#1100345V#0009F#5PHaha. But we're almost there.\x02\x03",
            "#1100341V#0000FOh, hold on a second. I almost forgot\x01",
            "about our lemonade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100342V#0309F#5PHeh, check it out. Ice is just about finished\x01",
            "meltin'. Perfect time to chug 'em down, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100343V#0204F#12PI concur. A cold drink is proven to taste better\x01",
            "on a hot day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100344V#0102F#4PWe should really go back and thank her\x01",
            "when we have the opportunity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3185")

    label("loc_3144")


    ChrTalk(
        0x101,
        "#1100340V#0009F#5PI know it's hard, but we're almost there.\x02",
    )

    CloseMessageWindow()

    label("loc_3185")

    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100346V#0000F#5PThe countryside is really breathtaking\x01",
            "out this way.\x02\x03",
            "#1100347VIt almost feels as if it were taken straight\x01",
            "out of a fairy tale.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1100348V#0305F#5PNow that I think about it, it looks like\x01",
            "there are a buncha ruins scattered\x01",
            "around over here.\x02\x03",
            "#1100349VI bet history buffs would have a field\x01",
            "day here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100350V#0100F#11PIndeed. I believe most of them were\x01",
            "constructed during the Middle Ages\x01",
            "and have long since been forgotten.\x02\x03",
            "#1100351V#0103FI actually seem to remember being told\x01",
            "this area once served as a battlefield.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    ChrTalk(
        0x103,
        "#1100352V#0205F#6PThere were battles...? Here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100353V#0108F#11PYes. Between Erebonia and Calvard.\x02\x03",
            "#1100354V#0101FThe Ancient Battlefield is close by,\x01",
            "so it makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100355V#0001F#5PThe Ancient...Battlefield...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100356V#0300F#5PHeh. Sounds pretty interestin'.\x02\x03",
            "#1100357VWe don't come out here too often, so\x01",
            "you guys wanna go check it out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100358V#0006F#6PAs much as I'd love to, I think we should\x01",
            "save it for some other time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100359V#0106F#4PYes... I have to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100360V#0211F#12PThere is a time and location for everything,\x01",
            "Randy, and right now happens to be neither.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100361V#0306F#5PYou guys for real?! How can ya be so young,\x01",
            "yet so devoid of passion?\x02\x03",
            "#1100362V#0300F#5PYou're tellin' me the both of you grew up in\x01",
            "Crossbell, yet you never bothered to explore\x01",
            "outside the city?\x02\x03",
            "#1100363VI mean, ain't it natural to wanna ditch town\x01",
            "and spread your wings a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100364V#0006F#6PNot really. We never had much reason to\x01",
            "leave the city when we were kids.\x02\x03",
            "#1100365V#0000FEverything I could ever need was available\x01",
            "right there in the city, so I never thought\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100366V#0103F#4PCrossbell's commercial centrality encouraged\x01",
            "merchants to carry non-domestically produced\x01",
            "goods.\x02\x03",
            "#1100367V#0100FFurthermore, most people prefer to travel by\x01",
            "airship or by train.\x02\x03",
            "#1100368VAnd with the introduction of orbal cars and\x01",
            "buses, trekking the road like this, for all\x01",
            "intents and purposes, is a thing of the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100369V#0203F#12PWhile I was not raised in Crossbell,\x01",
            "I can relate.\x02\x03",
            "#1100370V#0200FI was living in one of the foundation's\x01",
            "research labs for the past few months,\x01",
            "so I never had the chance to hike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100371V#0303F#5PModern conveniences really are turning\x01",
            "us into a bunch of lazy bums, huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    ChrTalk(
        0x104,
        (
            "#1100372V#0305F#5PBut anyway, Lloyd. You look like you\x01",
            "still have plenty of energy to spare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100373V#0012F#6PWell, I owe that to the police academy's\x01",
            "survival and fitness training.\x02\x03",
            "#1100374V#0000FStill, my stamina doesn't hold a candle\x01",
            "to yours, Randy. All that training with\x01",
            "the CGF must have really paid off.\x02\x03",
            "#1100375VYou haven't even broken a sweat yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100376V#0304F#5PHeh. Probably just used to runnin'\x01",
            "everywhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1100377V#0305F#5PHey! Check it out, you guys.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x1)
    Fade(1000)
    OP_68(-46500, 5000, 80300, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24000, 0)
    OP_68(-46500, 2800, 80300, 7000)
    BeginChrThread(0x13, 1, 0, 21)
    ClearMapObjFlags(0x3, 0x4)

    def lambda_3DE8():
        OP_95(0xFE, -52200, 3000, 59200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3DE8)
    WaitChrThread(0xE, 1)
    SetChrPos(0xE, -93540, 3000, 51290, 0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    ClearMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    OP_6F(0x1)
    OP_0D()
    Fade(500)
    OP_68(-16760, 5300, 86730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20280, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#1100378V#0108F#2PThat must be the bus making its\x01",
            "return trip to the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100379V#0208F#11PFor a moment I considered signaling to the\x01",
            "driver to stop so I could return home.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100380V#0006F#5PC'mon. Wouldn't it be a total waste if\x01",
            "we took the bus back now?\x02\x03",
            "#1100381V#0000FWe're in the final stretch, you guys.\x02\x03",
            "#1100382VYou won't have to push yourselves\x01",
            "for much longer.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    ChrTalk(
        0x102,
        "#1100383V#0102F#4PI hope so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100384V#0203F#12P*sigh* Fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100385V#0302F#5PLet's get this show on the road, ladies!\x01",
            "I believe in ya!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20780, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    OP_68(-22900, 5600, 82800, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, -21900, 5000, 82800, 225)
    SetChrPos(0x1, -21900, 5000, 82800, 225)
    SetChrPos(0x2, -21900, 5000, 82800, 225)
    SetChrPos(0x3, -21900, 5000, 82800, 225)
    ModifyEventFlags(0, 0, 0x80)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0x60, 3)
    EndChrThread(0x13, 0x1)
    ClearMapFlags(0x8000000)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x1C, 0x8)
    Call(0, 12)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_2869 end

    def Function_21_4207(): pass

    label("Function_21_4207")

    Sound(465, 0, 100, 0)
    Sleep(3000)
    Sound(467, 0, 100, 0)
    Sleep(2000)
    Sound(470, 0, 100, 0)
    Return()

    # Function_21_4207 end

    def Function_22_4220(): pass

    label("Function_22_4220")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Old Armorica Road - Rest Area\x01",
            "　This is a public location, so\x01",
            "　please pick up after yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_4220 end

    def Function_23_42B7(): pass

    label("Function_23_42B7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C3")

    ChrTalk(
        0x101,
        (
            "#0005FYou know, this has been bothering\x01",
            "me for a while now...\x02\x03",
            "#0001FWhat exactly is this thing supposed to be?\x01",
            "It looks like that weird metal box back at\x01",
            "headquarters, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYeah, I've been eyein' it, too.\x02\x03",
            "#0300FThere's a bunch of juice and coffee\x01",
            "on display... What gives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FThis would be an orbal vending machine.\x01",
            "Is this the first time you have seen one?\x02\x03",
            "#0204FIf you insert mira coins into this slot, you\x01",
            "can choose the drink you want, and the\x01",
            "machine dispenses it accordingly.\x02\x03",
            "Since they were originally developed by\x01",
            "the Epstein Foundation, you would often\x01",
            "find them all over their research facilities...\x02\x03",
            "#0202FApparently, they are being tested out in\x01",
            "Crossbell as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWow, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FWere ya aware of these gadgets,\x01",
            "Mademois-Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FNo, this is my first time seeing one, too.\x02\x03",
            "#0100FIt's hard to believe that all these inventions\x01",
            "by the Epstein Foundation are starting to\x01",
            "pop up all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FGranted, I have heard that they have some\x01",
            "incredibly influential and wealthy sponsors...\x02\x03",
            "#0200FPlease resort to coins if you intend on using it.\x01",
            "Bills are incompatible with this model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThanks for the heads-up.\x01",
            "(I'm curious... I should try it\x01",
            "out at least once, right?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE0")

    label("loc_47C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbal vending machine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0005FI think Tio said I could insert a coin\x01",
            "to buy a drink.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48FA")

    ChrTalk(
        0x103,
        (
            "#0200FYes. This is a vending machine developed\x01",
            "by the Epstein Foundation.\x02\x03",
            "I believe Crossbell is one of the regions\x01",
            "designated to experiment with them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8C")

    label("loc_48FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D2")

    ChrTalk(
        0x102,
        (
            "#0100FThis is a vending machine developed\x01",
            "by the Epstein Foundation, isn't it?\x02\x03",
            "If I remember correctly, Tio said that\x01",
            "they've been placed all around Crossbell\x01",
            "for their experimental stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8C")

    label("loc_49D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A8C")

    ChrTalk(
        0x104,
        (
            "#0300FA vending machine created by the\x01",
            "Epstein Foundation, eh?\x02\x03",
            "Accordin' to Tio Tot, the foundation has\x01",
            "been using Crossbell as a testing\x01",
            "ground for these suckers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8C")


    ChrTalk(
        0x101,
        (
            "#0000FLeave it to Crossbell to incorporate\x01",
            "a broad spectrum of new technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE0")

    SetScenarioFlags(0x95, 3)
    Jump("loc_4AFF")

    label("loc_4AE8")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4AFF")

    TalkEnd(0xFF)
    Return()

    # Function_23_42B7 end

    SaveToFile()

Try(main)
