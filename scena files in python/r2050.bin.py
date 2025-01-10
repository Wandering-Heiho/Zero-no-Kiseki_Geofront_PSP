from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2050.bin",                # FileName
        "r2050",                    # MapName
        "r2050",                    # Location
        0x0063,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2050", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 99, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2050",                  # 0
        "Bus",                    # 1
        "車１",                   # 2
        "Red Mottled Murder",     # 3
        "SE制御",                 # 4
        "br2040",                 # 5
        "br2050",                 # 6
        "br2050",                 # 7
        "br2050",                 # 8
        "br2040",                 # 9
        "br2040",                 # 10
        "br2040",                 # 11
        "br2050",                 # 12
        "To Crossbell City",      # 13
        "To Mainz Mining Village",# 14
        "To Moon Temple",         # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   9,   2,   0,   5,   4,   5)
    Sepith("Sepith_B4", 7,   4,   0,   1,   4,   6,   3)
    Sepith("Sepith_C4", 9,   0,   4,   0,   4,   2,   6)
    Sepith("Sepith_D4", 0,   0,   0,   6,   6,   6,   6)
    Sepith("Sepith_E4", 14,  4,   9,   5,   7,   12,  9)

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
    MonsterBattlePostion("MonsterBattlePostion_154", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_174", 0x0000, 14, 6, 60, 10, 1, 40, 0, "br2050", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms69100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 14, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms68100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms68100.dat", "ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0000, 14, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms72800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms72800.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3CC", 0x0000, 14, 6, 60, 10, 1, 30, 0, "br2040", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71700.dat", "ms71700.dat", "ms65500.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2050", "Sepith_E4", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_114", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0C10, 255, 6, 0, 0, 0, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76000.dat", "ms77700.dat", "ms77700.dat", "ms77700.dat", "ms77700.dat", 0, "ms77700.dat", 0, "MonsterBattlePostion_154", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_574", 0x0000, 14, 6, 60, 0, 1, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72800.dat", "ms68100.dat", "ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_114", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch68150.itc",               # 12
        "monster/ch68151.itc",               # 13
        "monster/ch72850.itc",               # 14
        "monster/ch72851.itc",               # 15
        "monster/ch69150.itc",               # 16
        "monster/ch69151.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-12930,  8500,    127330,  0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-11790,  32470,   0,       0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-48260,  51700,   0,       0x1010000,    "BattleInfo_23C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-58330,  102750,  0,       0x1010000,    "BattleInfo_304", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-103440, 89080,   -14000,  0x1010000,    "BattleInfo_3CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-57310,  146680,  0,       0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-25730,  141040,  8000,    0x1010000,    "BattleInfo_3CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-83270,  179260,  0,       0x1010000,    "BattleInfo_23C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-33350,  41540,   0,       0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-62470,  119400,  0,       0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-82940,  170350,  0,       0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-74490,  81330,   -5980,   0x1010000,    "BattleInfo_494", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-26820,  143860,  7990,    0x185010E,    "BattleInfo_530", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0000, 0, 16,  -67.5,                 101.0,                 -1.0,                  324.0,                 [0.05892555043101311,  0.23570235073566437,   -0.0,                  0.0,                   -0.05892558768391609,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.928958892822266,     -7.8960137367248535,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 17,  -67.5,                 101.0,                 -1.0,                  324.0,                 [0.05892555043101311,  0.23570235073566437,   -0.0,                  0.0,                   -0.05892558768391609,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.928958892822266,     -7.8960137367248535,   0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 8,   -26.81999969482422,    143.86000061035156,    6.989999771118164,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   3.3524999618530273,    -17.982500076293945,   -1.747499942779541,    1.0])
    DeclEvent(0x0000, 0, 20,  -55.97999954223633,    98.30000305175781,     -0.5,                  729.0,                 [0.23570217192173004,  0.03928372263908386,   -0.0,                  0.0,                   -0.23570233583450317,  0.039283692836761475,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   36.3641471862793,      -1.6624844074249268,   0.09999999403953552,   1.0])
    DeclEvent(0x0000, 0, 21,  -62.279998779296875,   123.3499984741211,     -0.5,                  729.0,                 [-2.132526049081207e-07, 0.0555555559694767,    0.0,                   0.0,                   -0.3333333134651184,   -3.554210081802012e-08, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   41.11664962768555,     3.4600043296813965,    0.10000000149011612,   1.0])

    DeclActor(-21100,  8000,    145620,  1200,    -21100,  9000,    145620,  0x007C, 0,  4,  0x0000)
    DeclActor(-12930,  8000,    127330,  1200,    -12930,  9000,    127330,  0x007C, 0,  5,  0x0000)
    DeclActor(-54270,  0,       137790,  1200,    -54270,  1000,    137790,  0x007C, 0,  13, 0x0000)
    DeclActor(-56750,  0,       105830,  1200,    -56750,  2000,    105830,  0x007C, 0,  12, 0x0000)
    DeclActor(-51520,  0,       60360,   1200,    -51520,  0,       60360,   0x007C, 0,  6,  0x0000)
    DeclActor(-80100,  0,       181140,  1200,    -80100,  0,       181140,  0x007C, 0,  7,  0x0000)

    PlaceName(-6.0, 0.0, -16.989999771118164, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-86.0, 0.0, 229.97999572753906, 0x0000, 0x0000, "To Mainz Mining Village")
    PlaceName(-151.4199981689453, 0.0, 100.58000183105469, 0x0000, 0x0000, "To Moon Temple")
    PlaceName(-55.5, 0.0, 107.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9

    ScpFunction((
        "Function_0_BEC",          # 00, 0
        "Function_1_C0B",          # 01, 1
        "Function_2_C2A",          # 02, 2
        "Function_3_C72",          # 03, 3
        "Function_4_12CF",         # 04, 4
        "Function_5_140D",         # 05, 5
        "Function_6_1609",         # 06, 6
        "Function_7_161D",         # 07, 7
        "Function_8_1631",         # 08, 8
        "Function_9_1886",         # 09, 9
        "Function_10_18A9",        # 0A, 10
        "Function_11_1E82",        # 0B, 11
        "Function_12_1F6F",        # 0C, 12
        "Function_13_1F93",        # 0D, 13
        "Function_14_1F94",        # 0E, 14
        "Function_15_288C",        # 0F, 15
        "Function_16_28CF",        # 10, 16
        "Function_17_2F68",        # 11, 17
        "Function_18_3FC7",        # 12, 18
        "Function_19_4058",        # 13, 19
        "Function_20_4191",        # 14, 20
        "Function_21_41AD",        # 15, 21
        "Function_22_41C9",        # 16, 22
    ))


    def Function_0_BEC(): pass

    label("Function_0_BEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_BEC")

    label("loc_C0A")

    Return()

    # Function_0_BEC end

    def Function_1_C0B(): pass

    label("Function_1_C0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C29")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_C0B")

    label("loc_C29")

    Return()

    # Function_1_C0B end

    def Function_2_C2A(): pass

    label("Function_2_C2A")

    OP_16(0x2, 2000, 0, 0, 386, 452, 557974784)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C56")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_C6E")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_C6E")

    Call(0, 9)
    Return()

    # Function_2_C2A end

    def Function_3_C72(): pass

    label("Function_3_C72")

    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBA")
    ModifyEventFlags(1, 1, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)

    label("loc_CBA")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D34")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_66(0x3, 0x1)

    label("loc_D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB8")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_66(0x3, 0x1)
    Jump("loc_DBD")

    label("loc_DB8")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_DBD")

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
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10EC")
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_1100")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1100")
    ClearChrFlags(0x17, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1100")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C3")
    OP_70(0x0, 0x0)
    Jump("loc_11C7")

    label("loc_11C3")

    OP_70(0x0, 0x1E)

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    OP_70(0x1, 0x0)
    Jump("loc_11DE")

    label("loc_11DA")

    OP_70(0x1, 0x1E)

    label("loc_11DE")

    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_1244")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -51520, 0, 60360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)
    Jump("loc_129D")

    label("loc_1244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 2)), scpexpr(EXPR_END)), "loc_129D")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -80100, 0, 181140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_129D")

    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12BF")
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_12CE")

    Return()

    # Function_3_C72 end

    def Function_4_12CF(): pass

    label("Function_4_12CF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AC")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 50)
    AddSepith(0x1, 50)
    AddSepith(0x2, 50)
    AddSepith(0x3, 50)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x50\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x50\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x50\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x50.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x104, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_13FB")

    label("loc_13AC")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I guess you could say the contents of this\x01",
            "chest add up to...zero.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_13FB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12CF end

    def Function_5_140D(): pass

    label("Function_5_140D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CC")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150C")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1466():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1466)

    def lambda_1480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1480)
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
    Battle("BattleInfo_574", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_14ED"),
        (2, "loc_14FC"),
        (1, "loc_1509"),
        (SWITCH_DEFAULT, "loc_150C"),
    )


    label("loc_14ED")

    SetScenarioFlags(0x74, 3)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_150C")

    label("loc_14FC")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1509")

    OP_B7(0x0)
    Return()

    label("loc_150C")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x645, 1)"), scpexpr(EXPR_END)), "loc_1564")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x645),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_15C7")

    label("loc_1564")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x645),
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

    label("loc_15C7")

    Jump("loc_15FD")

    label("loc_15CC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Police brutality!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_15FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_140D end

    def Function_6_1609(): pass

    label("Function_6_1609")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1609 end

    def Function_7_161D(): pass

    label("Function_7_161D")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 2)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_161D end

    def Function_8_1631(): pass

    label("Function_8_1631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 7)), scpexpr(EXPR_END)), "loc_163B")
    Return()

    label("loc_163B")

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
        (1, "loc_171E"),
        (SWITCH_DEFAULT, "loc_1735"),
    )


    label("loc_171E")

    Sleep(500)
    OP_90(0x0, -35110, 7990, 143660, 89)
    EventEnd(0x5)
    Return()

    label("loc_1735")

    Battle("BattleInfo_530", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-35110, 8990, 143660, 0)
    OP_90(0x0, -35110, 7990, 143660, 89)
    OP_90(0x1, -35110, 7990, 143660, 89)
    OP_90(0x2, -35110, 7990, 143660, 89)
    OP_90(0x3, -35110, 7990, 143660, 89)
    OP_90(0x4, -35110, 7990, 143660, 89)
    OP_90(0x5, -35110, 7990, 143660, 89)
    OP_90(0x6, -35110, 7990, 143660, 89)
    OP_90(0x7, -35110, 7990, 143660, 89)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_17F7"),
        (1, "loc_17FA"),
        (SWITCH_DEFAULT, "loc_17FD"),
    )


    label("loc_17F7")

    EventEnd(0x5)
    Return()

    label("loc_17FA")

    OP_B7(0x0)
    Return()

    label("loc_17FD")

    EventBegin(0x1)
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 2, 0x80)
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
            "Exterminated monster on Mainz Mountain Path!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 7)
    OP_29(0x23, 0x4, 0x10)
    OP_29(0x23, 0x4, 0x2)
    OP_29(0x23, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_8_1631 end

    def Function_9_1886(): pass

    label("Function_9_1886")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18A8")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_18A8")

    Return()

    # Function_9_1886 end

    def Function_10_18A9(): pass

    label("Function_10_18A9")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7A")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E17")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_194F")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_196A")

    label("loc_194F")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_196A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1998")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_19AE")

    label("loc_1998")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_19AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DC")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_19F2")

    label("loc_19DC")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_19F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A21")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1A38")

    label("loc_1A21")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_1A38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A67")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1A7E")

    label("loc_1A67")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA8")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1ABA")

    label("loc_1AA8")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_1ABA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE6")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1AFA")

    label("loc_1AE6")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B32")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1B52")

    label("loc_1B32")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_1B52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B80")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1B96")

    label("loc_1B80")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1B96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC8")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1BE2")

    label("loc_1BC8")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1C")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1C3E")

    label("loc_1C1C")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1C3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6D")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1C84")

    label("loc_1C6D")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_1C84")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E08")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D5B"),
        (1, "loc_1D69"),
        (2, "loc_1D77"),
        (3, "loc_1D85"),
        (4, "loc_1D93"),
        (5, "loc_1DA1"),
        (6, "loc_1DAF"),
        (7, "loc_1DBD"),
        (8, "loc_1DCB"),
        (9, "loc_1DD9"),
        (10, "loc_1DE7"),
        (11, "loc_1DF5"),
        (SWITCH_DEFAULT, "loc_1E03"),
    )


    label("loc_1D5B")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1D69")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1D77")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1D85")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1D93")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DA1")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DAF")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DBD")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DCB")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DD9")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DE7")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1DF5")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E03")

    label("loc_1E03")

    Jump("loc_1E12")

    label("loc_1E08")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E12")

    Jump("loc_1E75")

    label("loc_1E17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E62")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1E75")

    label("loc_1E62")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E75")

    Jump("loc_18C3")

    label("loc_1E7A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_18A9 end

    def Function_11_1E82(): pass

    label("Function_11_1E82")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -57660, 0, 105090, 225)
    SetChrPos(0x1, -57660, 0, 105090, 225)
    SetChrPos(0x2, -57660, 0, 105090, 225)
    SetChrPos(0x3, -57660, 0, 105090, 225)
    SetChrPos(0x4, -57660, 0, 105090, 225)
    SetChrPos(0x5, -57660, 0, 105090, 225)
    Sleep(1)
    OP_68(-57660, 2500, 105090, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F54")
    Sound(1502, 255, 100, 0)
    Jump("loc_1F5A")

    label("loc_1F54")

    Sound(1503, 255, 100, 0)

    label("loc_1F5A")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1E82 end

    def Function_12_1F6F(): pass

    label("Function_12_1F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F85")
    Call(0, 18)
    Jump("loc_1F92")

    label("loc_1F85")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)

    label("loc_1F92")

    Return()

    # Function_12_1F6F end

    def Function_13_1F93(): pass

    label("Function_13_1F93")

    Return()

    # Function_13_1F93 end

    def Function_14_1F94(): pass

    label("Function_14_1F94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(-3690, 2500, 9580, 0)
    MoveCamera(31, 12, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17280, 0)
    OP_68(-3690, 2500, 580, 6000)
    SetChrPos(0x101, -1740, 0, -2640, 0)
    SetChrPos(0x102, -620, 0, -3750, 0)
    SetChrPos(0x103, -2390, 0, -4560, 0)
    SetChrPos(0x104, -1370, 0, -5530, 0)
    FadeToBright(1000, 0)
    Sleep(2000)

    def lambda_206F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_206F)

    def lambda_2084():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2084)

    def lambda_2099():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2099)

    def lambda_20AE():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20AE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#1200352V#0300FA tunnel, eh? Thing looks sturdy enough\x01",
            "to not collapse on us, so that's good.\x02\x03",
            "#1200353VThough, I get the feelin' this place was\x01",
            "used to mine septium, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#1200354V#0004F#5PYeah, I'd be surprised if it wasn't.\x02\x03",
            "#1200355V#0000FIf I remember my history, these tunnels\x01",
            "were constructed just before Crossbell\x01",
            "became an autonomous state.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1200356V#0203F#6P#NIn that case, this tunnel dates back\x01",
            "70 years ago...\x02\x03",
            "#1200357V#0200FThen again, Crossbell has a reputation\x01",
            "for being rich in septium, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1200358V#0103FCorrect. So rich that the Empire and\x01",
            "the Republic would have wars over it.\x02\x03",
            "#1200359V#0100FSeptium yields are still bountiful to\x01",
            "this day, making it one of Crossbell's\x01",
            "most valuable resources.\x02\x03",
            "#1200360VBut given the advancements in mining\x01",
            "technology and the discovery of septium\x01",
            "veins, it's not as alluring as it once was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200361V#0003F#5PHuh, I wasn't aware of that...\x02\x03",
            "#1200362VCommerce really is the backbone\x01",
            "of modern Crossbell, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Sound(842, 0, 100, 0)
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

    def lambda_2557():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2557)

    def lambda_2564():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2564)

    def lambda_2571():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2571)

    def lambda_257E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_257E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1200363V#0001F#5PThere it is again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200364V#0301FThing must be real close, judgin'\x01",
            "by the echo...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_260A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_260A)
    Sleep(50)

    def lambda_261A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_261A)
    Sleep(50)

    def lambda_262A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_262A)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#1200365V#0101FCan you pinpoint its location, Tio?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#1200366V#0201F#5POf course!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1203, 255, 100, 0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 15)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#1200367V#0203F#5PI have got it.\x02\x03",
            "#1200368V#0201FI traced the sound waves to\x01",
            "the exit of this tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200369V#0001F#5PGood work. Let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    SetChrPos(0x0, -1200, 0, -1100, 0)
    SetScenarioFlags(0x64, 6)
    OP_29(0x40, 0x1, 0x5)
    OP_E0(0x2)
    Call(0, 9)
    EndChrThread(0xB, 0x1)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_1F94 end

    def Function_15_288C(): pass

    label("Function_15_288C")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_15_288C end

    def Function_16_28CF(): pass

    label("Function_16_28CF")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-69470, 1100, 96030, 0)
    MoveCamera(30, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(19500, 2500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -67560, 0, 98480, 180)
    SetChrPos(0x102, -68860, 0, 97180, 180)
    SetChrPos(0x103, -66110, 0, 98530, 180)
    SetChrPos(0x104, -69340, 0, 98740, 180)
    SetChrPos(0x109, -67000, 0, 100640, 180)

    def lambda_2973():
        OP_95(0xFE, -69630, 0, 96020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2973)

    def lambda_298D():
        OP_95(0xFE, -71190, 0, 94710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_298D)

    def lambda_29A7():
        OP_95(0xFE, -68070, 0, 96430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29A7)

    def lambda_29C1():
        OP_95(0xFE, -70710, 0, 97390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29C1)

    def lambda_29DB():
        OP_95(0xFE, -68650, 0, 99180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_29DB)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x12C)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xB4, 0x12C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xB4, 0x12C)
    OP_0D()
    OP_6F(0x10)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_2AD4")

    ChrTalk(
        0x101,
        (
            "#4100274V#0003F#5PWell, that was much quicker\x01",
            "than I thought it'd be.\x02\x03",
            "#4100279V#0001FI'm pretty sure this road leads\x01",
            "down to the ruins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C16")

    label("loc_2AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_2B78")

    ChrTalk(
        0x101,
        (
            "#4100274V#0003F#5PWell, that was much quicker\x01",
            "than I thought it'd be.\x02\x03",
            "#4100280V#0001FThis must be the road that leads\x01",
            "down to the ruins, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C16")

    label("loc_2B78")


    ChrTalk(
        0x101,
        (
            "#4100274V#0003F#5PWell, that was much quicker\x01",
            "than I thought it'd be.\x02\x03",
            "#4100281V#0001FYou think this is the road that leads\x01",
            "down to the ruins near here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C16")

    Jump("loc_2DFC")

    label("loc_2C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_2CB8")

    ChrTalk(
        0x101,
        (
            "#4100278V#0006F#5PMan, I didn't realize how far we've\x01",
            "walked already.\x02\x03",
            "#4100275V#0001FIsn't that the way to get to\x01",
            "those ruins near here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFC")

    label("loc_2CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(
        0x101,
        (
            "#4100278V#0006F#5PMan, I didn't realize how far we've\x01",
            "walked already.\x02\x03",
            "#4100276V#0001FThis must be the road that leads\x01",
            "down to the ruins, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFC")

    label("loc_2D5C")


    ChrTalk(
        0x101,
        (
            "#4100278V#0006F#5PMan, I didn't realize how far we've\x01",
            "walked already...\x02\x03",
            "#4100277V#0001FYou think this is the road that leads\x01",
            "down to the ruins near here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFC")


    ChrTalk(
        0x109,
        (
            "#4100282V#0503F#5PYou are correct.\x02\x03",
            "#4100283V#0500FWe'll have to continue on foot\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100284V#0300F#5PLet's get a move on if we're ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100285V#0204F#5PIndeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100286V#0108F#5P(*sigh* Could these ruins truly be\x01",
            "haunted...?)\x02\x03",
            "#4100287V#0113F(N-No, of course not. Ghosts aren't\x01",
            "real!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -70200, 0, 98000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC0, 2)
    OP_E0(0x2)
    Call(0, 9)
    EventEnd(0x5)
    Return()

    # Function_16_28CF end

    def Function_17_2F68(): pass

    label("Function_17_2F68")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("apl/ch50109.itc", 0x1F)
    SoundLoad(806)
    OP_68(-61260, 2300, 105970, 0)
    MoveCamera(76, 9, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, -64190, 0, 101320, 45)
    SetChrPos(0x102, -65650, 0, 102220, 45)
    SetChrPos(0x103, -66810, 0, 100330, 45)
    SetChrPos(0x104, -64840, 0, 100030, 45)
    SetChrPos(0x109, -62860, 0, 103720, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_302B():
        OP_95(0xFE, -61100, 0, 104820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_302B)

    def lambda_3045():
        OP_95(0xFE, -62740, 0, 105360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3045)

    def lambda_305F():
        OP_95(0xFE, -63850, 0, 103990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_305F)

    def lambda_3079():
        OP_95(0xFE, -62330, 0, 103250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3079)

    def lambda_3093():
        OP_95(0xFE, -59960, 0, 107020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3093)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    OP_68(-61260, 1300, 105970, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0xE1, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x109,
        (
            "#4100467V#0502F#5PSo, what do you all plan to do after\x01",
            "this?\x02\x03",
            "#4100468VI still have a bit of time before I need\x01",
            "to be back. Need a ride anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100469V#0002F#12PHmm, let me think...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4100470V#0109F#6PIf you're offering, we might\x01",
            "as well take you up on it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4100471V#0005F#11PA call? Sorry, give me a minute.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#4100472V#0300F#12PHaha. Kinda weird time for\x01",
            "someone to ring.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x190)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(400)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1084, 255, 90, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100473V#0000FHello. This is Lloyd Bannings,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2083, 255, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100475V\x07\x05",
            "Umm, it's Fran. Where are\x01",
            "you guys right now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_END)), "loc_35D8")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100476V\x07\x00",
            "#0005FOh, we're in the tunnel on Mainz\x01",
            "Mountain Path right now.\x02\x03",
            "#4100477V#0002FWe just finished investigating some ruins\x01",
            "in the area with your sister.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100478V\x07\x05",
            "How's everyone doing?\x02\x03",
            "#4100482VWere you able to safely complete your\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_372A")

    label("loc_35D8")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100479V\x07\x00",
            "#0005FOh, we're actually in the tunnel on\x01",
            "Mainz Mountain path right now.\x02\x03",
            "#4100480V#0000FWe just finished investigating some ruins\x01",
            "in the area with your sister.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100481V\x07\x05",
            "Oh, Noey was telling me about that earlier.\x02\x03",
            "#4100482VWere you able to safely complete your\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_372A")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100483V\x07\x00",
            "#0004FYeah... At least, for now, anyway.\x02\x03",
            "#4100484V#0000FDid you want me to hand her the\x01",
            "phone? She's right here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100485V\x07\x05",
            "Ahaha. No, that's okay!\x02\x03",
            "#4100486VIf I needed to talk to her, I would\x01",
            "have just called her Enigma!\x02\x03",
            "#4100487VActually, there's someone who'd like to\x01",
            "ask the SSS a question or two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100488V\x07\x00",
            "#0005FOh, sure. Who is it? A citizen?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100489V\x07\x05",
            "Not quite. It's the mayor of Mainz.\x02\x03",
            "#4100490VIt sounds like he needs a consultation\x01",
            "with your team.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100491V\x07\x00",
            "#0000FOh, really? This doesn't happen very\x01",
            "often.\x02\x03",
            "#4100492VDid he give you any details?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100493V\x07\x05",
            "Apparently, one of the locals from Mainz\x01",
            "went to visit Crossbell City, but he hasn't\x01",
            "returned for several days.\x02\x03",
            "#4100494VAt least, that's what I gathered from\x01",
            "everything he told me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4100495V\x07\x00",
            "#0008FThat sounds a little concerning...\x02\x03",
            "#4100496V#0000FAll right, we're already near Mainz, so\x01",
            "we'll pay Mayor Bickson a visit.\x02\x03",
            "#4100497VFortunately for us, your sister can\x01",
            "give us a ride there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100498V\x07\x05",
            "Heehee. Don't be afraid to work her\x01",
            "to the bone!\x02\x03",
            "#4100499VI'll go ahead and contact the mayor to\x01",
            "let him know you're coming in advance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#4100500V\x07\x00",
            "#0500F#5PWas that Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100501V#0012F#11PYeah. She called to tell us about\x01",
            "a new request.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D1C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D1C)
    Sleep(50)
    TurnDirection(0x101, 0x103, 500)
    WaitChrThread(0x103, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave a short summary of what Fran said.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#4100502V#0105F#6PHmm, I see... Mayor Bickson submitted\x01",
            "a support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100503V#0203F#12PSomeone visited the city and has\x01",
            "yet to return home...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100504V#0300F#12PMay as well head on over and hear the\x01",
            "story straight from the man himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100505V#0000F#5PYeah, I was thinking the same.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100506V#0002F#11PAll right, Sergeant Major. Could you\x01",
            "take us to Mainz?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#4100507V#0502F#5PLeave it to me!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_37()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrPos(0x0, -64000, 0, 105500, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_E0(0x2)
    OP_66(0x3, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xC1, 0)
    OP_29(0x49, 0x4, 0x10)
    OP_29(0x4A, 0x4, 0x2)
    OP_29(0x4A, 0x1, 0x0)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    Sleep(500)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_17_2F68 end

    def Function_18_3FC7(): pass

    label("Function_18_3FC7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ride in Guardian Force car?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mainz Mining Village\x01",      # 0
            "Cancel\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4050")
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 19)
    ClearMapFlags(0x8000000)
    SetScenarioFlags(0x5C, 2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_4050")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_3FC7 end

    def Function_19_4058(): pass

    label("Function_19_4058")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-63070, 1200, 112420, 0)
    MoveCamera(28, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16140, 0)
    OP_68(-63070, 3800, 112420, 4000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -61970, 0, 110190, 0)
    OP_D3(0x9, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_E0(0x1)
    FadeToBright(1000, 0)
    Sound(469, 0, 100, 0)
    Sound(488, 0, 70, 0)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_4165():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4165)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    EndChrThread(0x9, 0x1)
    OP_6F(0x1)
    Return()

    # Function_19_4058 end

    def Function_20_4191(): pass

    label("Function_20_4191")

    EventBegin(0x1)
    Call(0, 22)
    Sleep(50)
    SetChrPos(0x0, -58910, 0, 103870, 316)
    EventEnd(0x4)
    Return()

    # Function_20_4191 end

    def Function_21_41AD(): pass

    label("Function_21_41AD")

    EventBegin(0x1)
    Call(0, 22)
    Sleep(50)
    SetChrPos(0x0, -62130, 0, 119470, 181)
    EventEnd(0x4)
    Return()

    # Function_21_41AD end

    def Function_22_41C9(): pass

    label("Function_22_41C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4241")

    ChrTalk(
        0x101,
        (
            "#0005FWhoops...\x02\x03",
            "#0000FLet's get a ride from the Sergeant Major.\x01",
            "That'll save us a lot of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4351")

    label("loc_4241")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D8")

    ChrTalk(
        0x101,
        (
            "#0005FWhoops...\x02\x03",
            "#0000FYou mind giving us a ride, Sergeant\x01",
            "Major Seeker? That'll save us a lot\x01",
            "of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0500FNo problem!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4351")

    label("loc_42D8")


    ChrTalk(
        0x101,
        (
            "#0005FWhoops...\x02\x03",
            "#0000FWe're hitching a ride with Sergeant Major\x01",
            "Seeker, aren't we? That'll save us plenty\x01",
            "of time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4351")

    Return()

    # Function_22_41C9 end

    SaveToFile()

Try(main)
