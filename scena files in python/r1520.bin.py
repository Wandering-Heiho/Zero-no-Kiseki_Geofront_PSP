from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1520.bin",                # FileName
        "r1520",                    # MapName
        "r1520",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1520", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 12500, 0, 0, 1, 96, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1520",                  # 0
        "Bus",                    # 1
        "Driver",                 # 2
        "Estelle",                # 3
        "Joshua",                 # 4
        "Boss 1",                 # 5
        "Boss 2",                 # 6
        "Boss 3",                 # 7
        "br1500",                 # 8
        "br1500",                 # 9
        "br1500",                 # 10
        "br1500",                 # 11
        "br1500",                 # 12
        "br1500",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "To Crossbell City",      # 16
        "To St. Ursula Medical College",# 17
        "To Stargazer's Tower",   # 18
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_B4", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_C4", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_D4", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_E4", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_F4", 9,   7,   18,  6,   7,   6,   3)

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

    # monster count: 10

    BattleInfo(
        "BattleInfo_184", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_24C", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_314", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3DC", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_D4", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4A4", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_E4", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_56C", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br1500", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_608", 0x0012, 12, 6, 45, 0, 1, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68501.dat", "ms68501.dat", 0, 0, 0, 0, "ms66600.dat", 0, "MonsterBattlePostion_164", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch00600.itc",                   # 01
        "chr/ch00700.itc",                   # 02
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
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch66650.itc",               # 12
        "monster/ch66651.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch65850.itc",               # 16
        "monster/ch65851.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "monster/ch70250.itc",               # 1C
        "monster/ch70251.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(60,      -21740,  0,       0x1010000,    "BattleInfo_184", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(13280,   -29310,  0,       0x1010000,    "BattleInfo_24C", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-14000,  -53580,  0,       0x1010000,    "BattleInfo_314", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-17670,  -78600,  0,       0x1010000,    "BattleInfo_3DC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-41730,  -84600,  0,       0x1010000,    "BattleInfo_4A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-41630,  -87100,  0,       0x1010000,    "BattleInfo_4A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-56290,  -101340, 0,       0x1010000,    "BattleInfo_314", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44280,  -104010, 0,       0x1010000,    "BattleInfo_184", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-2950,   -34030,  0,       0x1010000,    "BattleInfo_56C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-42660,  -94360,  10,      0x1010000,    "BattleInfo_56C", 0,   28,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 17,  -28.0,                 -82.0,                 -1.0,                  625.0,                 [0.07071065902709961,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142131805419922,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.8183791637420654,   15.556347846984863,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 27,  -2.5,                  9.0,                   -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.1666666716337204,    -3.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 28,  0.0,                   -1.5,                  -1.0,                  506.25,                [0.04714055731892586,  -0.23570173978805542,  0.0,                   0.0,                   0.047140348702669144,  0.23570279777050018,   -0.0,                  0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   0.0,                   0.07071052491664886,   0.3535541892051697,    0.20000000298023224,   1.0])

    DeclActor(-14600,  -1400,   -10500,  1200,    -14600,  -400,    -10500,  0x007C, 0,  4,  0x0000)
    DeclActor(-33050,  0,       -69250,  1200,    -33050,  1000,    -69250,  0x007C, 0,  5,  0x0000)
    DeclActor(4920,    0,       -11820,  1200,    4920,    0,       -11820,  0x007C, 0,  6,  0x0000)
    DeclActor(-1270,   0,       -59940,  1200,    -1270,   0,       -59940,  0x007C, 0,  7,  0x0000)
    DeclActor(-57680,  0,       -116430, 1200,    -57680,  0,       -116430, 0x007C, 0,  8,  0x0000)

    PlaceName(2.0, 0.4300000071525574, 40.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-59.900001525878906, 0.0, -142.27999877929688, 0x0000, 0x0000, "To St. Ursula Medical College")
    PlaceName(-51.7400016784668, -1.399999976158142, -3.7799999713897705, 0x0000, 0x0000, "To Stargazer's Tower")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_BE0",          # 00, 0
        "Function_1_C98",          # 01, 1
        "Function_2_CB7",          # 02, 2
        "Function_3_D40",          # 03, 3
        "Function_4_110A",         # 04, 4
        "Function_5_1267",         # 05, 5
        "Function_6_13FA",         # 06, 6
        "Function_7_140E",         # 07, 7
        "Function_8_1422",         # 08, 8
        "Function_9_1436",         # 09, 9
        "Function_10_144F",        # 0A, 10
        "Function_11_1478",        # 0B, 11
        "Function_12_1643",        # 0C, 12
        "Function_13_177A",        # 0D, 13
        "Function_14_1910",        # 0E, 14
        "Function_15_1A53",        # 0F, 15
        "Function_16_205D",        # 10, 16
        "Function_17_20C2",        # 11, 17
        "Function_18_274E",        # 12, 18
        "Function_19_3AFE",        # 13, 19
        "Function_20_5462",        # 14, 20
        "Function_21_5487",        # 15, 21
        "Function_22_5586",        # 16, 22
        "Function_23_55A1",        # 17, 23
        "Function_24_560A",        # 18, 24
        "Function_25_562E",        # 19, 25
        "Function_26_56A2",        # 1A, 26
        "Function_27_5C19",        # 1B, 27
        "Function_28_606B",        # 1C, 28
        "Function_29_6079",        # 1D, 29
    ))


    def Function_0_BE0(): pass

    label("Function_0_BE0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_C20"),
        (1, "loc_C2C"),
        (2, "loc_C38"),
        (3, "loc_C44"),
        (4, "loc_C50"),
        (5, "loc_C5C"),
        (6, "loc_C68"),
        (SWITCH_DEFAULT, "loc_C74"),
    )


    label("loc_C20")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C2C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C38")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C44")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C50")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C5C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C68")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C74")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C97")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C80")

    label("loc_C97")

    Return()

    # Function_0_BE0 end

    def Function_1_C98(): pass

    label("Function_1_C98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB6")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_1_C98")

    label("loc_CB6")

    Return()

    # Function_1_C98 end

    def Function_2_CB7(): pass

    label("Function_2_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CC6")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 18)

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D32")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -51450, 0, -96010, 315)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, -52810, 0, -95050, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -53470, 0, -94190, 45)
    Call(0, 10)

    label("loc_D32")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_2_CB7 end

    def Function_3_D40(): pass

    label("Function_3_D40")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D62")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7A")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_D7A")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")
    OP_70(0x1, 0x0)
    Jump("loc_F1D")

    label("loc_F19")

    OP_70(0x1, 0x1E)

    label("loc_F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F30")
    OP_70(0x2, 0x0)
    Jump("loc_F34")

    label("loc_F30")

    OP_70(0x2, 0x1E)

    label("loc_F34")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 1)), scpexpr(EXPR_END)), "loc_F9E")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 4920, 0, -11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_1055")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 2)), scpexpr(EXPR_END)), "loc_FFC")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -1270, 0, -59940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_1055")

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 3)), scpexpr(EXPR_END)), "loc_1055")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -57680, 0, -116430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10A0")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B1")
    Call(0, 16)

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C4")
    OP_1B(0x2, 0x0, 0x1D)

    label("loc_10C4")

    SoundDistance(0x7D, 0xFFFFAD4E, 0x0, 0xFFFDDD7A, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0xB50E, 0x0, 0xFFFEEE0E)
    OP_E1(0xBA86, 0x0, 0xD0D4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1109")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_1109")

    Return()

    # Function_3_D40 end

    def Function_4_110A(): pass

    label("Function_4_110A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F4")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_118A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_11EF")

    label("loc_118A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
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

    label("loc_11EF")

    Jump("loc_125B")

    label("loc_11F4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If the CPD found out who stole from me,\x01",
            "you'd be unempLloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_125B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_110A end

    def Function_5_1267(): pass

    label("Function_5_1267")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1351")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_12E7")
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
    SetScenarioFlags(0x116, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_134C")

    label("loc_12E7")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_134C")

    Jump("loc_13EE")

    label("loc_1351")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As you walk away with a mediocre item, you fail to notice\x01",
            "that the chest itself is made of priceless Zemurian Ore.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_13EE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1267 end

    def Function_6_13FA(): pass

    label("Function_6_13FA")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_13FA end

    def Function_7_140E(): pass

    label("Function_7_140E")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_140E end

    def Function_8_1422(): pass

    label("Function_8_1422")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 3)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1422 end

    def Function_9_1436(): pass

    label("Function_9_1436")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_144E")
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_144E")

    Return()

    # Function_9_1436 end

    def Function_10_144F(): pass

    label("Function_10_144F")

    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Return()

    # Function_10_144F end

    def Function_11_1478(): pass

    label("Function_11_1478")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1602")

    ChrTalk(
        0xFE,
        (
            "Hey there, officers. I just wanted\x01",
            "to thank you for your help earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those bracers definitely impressed\x01",
            "me, too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that had you guys not shown up,\x01",
            "we would have been in a world of trouble.\x01",
            "Once again, I thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're welcome to take a quick rest\x01",
            "inside my bus if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to hunker down in any\x01",
            "of the open seats.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    SetScenarioFlags(0x70, 7)
    Jump("loc_163F")

    label("loc_1602")


    ChrTalk(
        0xFE,
        (
            "Well? Would you like to take a break\x01",
            "inside the bus?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_163F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1478 end

    def Function_12_1643(): pass

    label("Function_12_1643")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Take a quick break\x01",      # 0
            "Cancel\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C8")
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
    Jump("loc_1779")

    label("loc_16C8")

    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "No worries. You can always come back and\x01",
            "give me a shout if you change your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, I don't think we'll be able to get\x01",
            "back on the road for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1779")

    Return()

    # Function_12_1643 end

    def Function_13_177A(): pass

    label("Function_13_177A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1790")
    Call(0, 26)
    Jump("loc_190F")

    label("loc_1790")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A5")
    Call(0, 15)
    Jump("loc_190C")

    label("loc_17A5")


    ChrTalk(
        0xA,
        (
            "#0800FOh, hey guys.\x02\x03",
            "Don't you worry about a thing.\x01",
            "We've got you covered!\x02\x03",
            "#0804FWe only need to keep watch for monsters,\x01",
            "explain the situation to the passengers, and\x01",
            "give our report to City Hall, right?\x02\x03",
            "#0800FPiece of cake! We won't even break\x01",
            "a sweat, so feel free to get back to\x01",
            "doing your own thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks. We'll leave it to you, then.\x02",
    )

    CloseMessageWindow()

    label("loc_190C")

    TalkEnd(0xA)

    label("loc_190F")

    Return()

    # Function_13_177A end

    def Function_14_1910(): pass

    label("Function_14_1910")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1925")
    Call(0, 15)
    Jump("loc_1A4F")

    label("loc_1925")


    ChrTalk(
        0xB,
        (
            "#0904FI've actually heard about the SSS,\x01",
            "but I never expected I'd be able to\x01",
            "meet you so quickly.\x02\x03",
            "#0900FIt's going to be a while before the engine\x01",
            "is repaired. We can handle things from\x01",
            "here, so feel free to get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FSorry for dumpin' it all on you,\x01",
            "but we appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4F")

    TalkEnd(0xB)
    Return()

    # Function_14_1910 end

    def Function_15_1A53(): pass

    label("Function_15_1A53")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "#1100995V#0804F#11PWowza, between all these orbal cars\x01",
            "and that big network thingy, Crossbell\x01",
            "sure is ahead of the game.\x02\x03",
            "#1100996V#0800FIt's all neat, but I still think Liberl's\x01",
            "the leader in everything orbal!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "#1100997V#0904F#5PI wouldn't jump to conclusions so quickly.\x01",
            "Liberl may be advanced, but most of its\x01",
            "citizens still live an old-fashioned lifestyle.\x02\x03",
            "#1100998V#0900FAnd speaking of the orbal network, it sounds\x01",
            "like Crossbell's major partners with the\x01",
            "Epstein Foundation.\x02\x03",
            "#1100999VSo, all things considered, Crossbell might\x01",
            "very well be the most technologically\x01",
            "advanced place on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101000V#0805F#11POh, yeah?\x02\x03",
            "#1101001V#0809FWell, I bet if we dragged Tita along with us\x01",
            "sometime, she'd totally have a field day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101002V#0909F#5PHaha. Yeah, I could see that.\x02\x03",
            "#1101003V#0902F...Do you miss them, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1101004V#0802F#11PA...hahaha... You caught me red-handed.\x02\x03",
            "#1101005V#0804FIt hardly feels like that long ago that we\x01",
            "were reunited with everyone, y'know?\x02\x03",
            "#1101006V#0808FBut it's already been three months...\x01",
            "Sometimes I just wonder how everyone's\x01",
            "doing. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101007V#0904F#5PI wouldn't worry if I were you, Estelle.\x01",
            "I'm sure everybody's doing fine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F67")

    ChrTalk(
        0x101,
        "#1101008V#0005F(Reunited...? With who?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2040")

    label("loc_1F67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB7")

    ChrTalk(
        0x102,
        "#1101009V#0105F(Who do you think they're referring to?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2040")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FFC")

    ChrTalk(
        0x103,
        "#1101010V#0200F(That was strangely vague...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2040")

    label("loc_1FFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2040")

    ChrTalk(
        0x104,
        "#1101011V#0300F(You think they miss their pals?)\x02",
    )

    CloseMessageWindow()

    label("loc_2040")

    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x2D, 0x0)
    Return()

    # Function_15_1A53 end

    def Function_16_205D(): pass

    label("Function_16_205D")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x2)
    SetMapObjFlags(0x0, 0x400)
    SetChrFlags(0x8, 0x8000)
    OP_78(0x0, 0x8)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetChrPos(0x8, -49600, 0, -91600, 230)
    OP_D3(0x8, 0x0, 0x38270, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x14A)
    Return()

    # Function_16_205D end

    def Function_17_20C2(): pass

    label("Function_17_20C2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x9D, 0xFF, 0xFF)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch68550.itc", 0x26)
    LoadChrToIndex("monster/ch68551.itc", 0x27)
    SetChrFlags(0x19E, 0x80)
    SetChrBattleFlags(0x19E, 0x8000)
    OP_68(-30410, 600, -82830, 0)
    MoveCamera(15, 18, 0, 0)
    OP_6E(410, 0)
    SetCameraDistance(25080, 0)
    SetChrPos(0x101, -32800, 0, -85500, 225)
    SetChrPos(0x102, -31800, 0, -86500, 225)
    SetChrPos(0x103, -30800, 0, -85500, 225)
    SetChrPos(0x104, -31800, 0, -84500, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -48090, 300, -93440, 135)
    BeginChrThread(0x9, 3, 0, 20)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xC, -44270, 0, -94740, 315)
    SetChrPos(0xD, -47430, 0, -98660, 0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    OP_70(0x0, 0x1E)
    SetMapObjFlags(0x2, 0x4)
    StopBGM(0x7D0)
    FadeToBright(1000, 0)
    OP_68(-32830, 600, -84230, 1500)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100860V#0013F#11PLook over there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100861V#0307F#11PDamn... Looks like our worst fears\x01",
            "came true!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_237C():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_237C)
    OP_68(-45100, 600, -91970, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21660, 0)
    OP_68(-48150, 600, -93080, 1500)
    OP_6F(0x1)
    OP_0D()
    Sound(835, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#1100862V#5PSomebody help us! Where'd these\x01",
            "monsters even come from?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100863V#5PO-Oh... Aidios, take the wheel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100864V#0007F#1PAre you okay?!\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Fade(1000)
    OP_68(-44300, 1100, -93460, 0)
    MoveCamera(359, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23150, 0)
    SetCameraDistance(19150, 1500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -34490, 0, -89160, 225)
    SetChrPos(0x102, -33270, 0, -86290, 225)
    SetChrPos(0x103, -33260, 0, -89550, 225)
    SetChrPos(0x104, -31970, 0, -87360, 225)

    def lambda_2561():
        OP_95(0xFE, -41650, 0, -93000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2561)

    def lambda_257B():
        OP_95(0xFE, -40590, 0, -90960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_257B)

    def lambda_2595():
        OP_95(0xFE, -40140, 0, -93680, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2595)

    def lambda_25AF():
        OP_95(0xFE, -39140, 0, -91570, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25AF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    def lambda_25DB():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_25DB)

    def lambda_25E8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_25E8)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0x9,
        "#1100865V#5PWh-Who are you guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100866V#0013F#11PCPD, Special Support Section!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100867V#0307F#2PWe'll take it from here, so get\x01",
            "back in the bus!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_68(-43010, 1100, -92990, 1500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_26BD():
        OP_95(0xFE, -48840, 500, -92450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26BD)
    Sleep(300)

    def lambda_26DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26DA)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)
    OP_6F(0x1)
    Battle("BattleInfo_608", 0x30200011, 0x0, 0x0, 0xC, 0xFF)
    FadeToDark(0, 0, -1)
    RemoveParty(0x9D, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_20C2 end

    def Function_18_274E(): pass

    label("Function_18_274E")

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
    LoadChrToIndex("monster/ch68550.itc", 0x26)
    LoadChrToIndex("monster/ch68551.itc", 0x27)
    LoadChrToIndex("chr/ch00651.itc", 0x29)
    LoadChrToIndex("chr/ch00652.itc", 0x2A)
    LoadChrToIndex("chr/ch00751.itc", 0x2B)
    LoadChrToIndex("chr/ch00650.itc", 0x2C)
    LoadChrToIndex("chr/ch00750.itc", 0x2D)
    LoadEffect(0x0, "battle\\cr006201.eff")
    OP_68(-47720, 200, -93920, 0)
    MoveCamera(335, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -45410, 0, -97050, 135)
    SetChrPos(0x102, -46960, 0, -96830, 135)
    SetChrPos(0x103, -48540, 0, -96760, 180)
    SetChrPos(0x104, -45330, 0, -94950, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -48840, 500, -92450, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xC, -58010, 0, -97980, 45)
    SetChrPos(0xD, -55680, 0, -100660, 45)
    SetChrPos(0xE, -55780, 0, -104760, 45)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    BeginChrThread(0xE, 3, 0, 1)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 16)
    OP_70(0x0, 0x0)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -41590, 0, -97730, 225)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -43200, 0, -98240, 225)
    SetChrFlags(0xB, 0x8000)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(21400, 1500)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(100)
    OP_93(0x101, 0x10E, 0x12C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100868V#0006F#12P*sigh* That was a little too close\x01",
            "for comfort.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A84():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A84)

    def lambda_2A91():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A91)
    Sleep(100)

    def lambda_2AA1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2AA1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        (
            "#1100869V#0106F#5PYou can say that again...\x02\x03",
            "#1100870V#0101FI can't begin to imagine where monsters\x01",
            "that massive came from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100871V#0206F#5PI suspect they are forest dwellers...\x02\x03",
            "#1100872V#0200FHowever, for what reason would they\x01",
            "venture out onto the highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100873V#0305F#11PI dunno, but that sounds weird.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-48290, 200, -93170, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x0)

    def lambda_2C36():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C36)

    def lambda_2C43():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C43)

    def lambda_2C50():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C50)

    def lambda_2C5D():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C5D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_2C7A():
        OP_95(0xFE, -48090, 300, -93440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C7A)

    def lambda_2C94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2C94)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#1100874V#5PMy heroes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100875V#5PI thought I was a goner back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100876V#0004F#6PI'm just glad you weren't hurt.\x02\x03",
            "#1100877V#0000FIs it safe to assume the bus was immobilized\x01",
            "because of those monsters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100878V#5PWell, sort of, but not really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100879V#5PThe engine on this thing broke down\x01",
            "before the monsters showed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100880V#5PIt happens occasionally, so I popped\x01",
            "the hood to take a look at it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100881V#0300F#12PAnd that's when the baddies popped\x01",
            "outta the woods, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100882V#0200F#6PDid the engine failure also cause your\x01",
            "communication device to stop working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100883V#5PYup. The communications also\x01",
            "gets its power from the engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100884V#5PI'm going to have to run some\x01",
            "tests to see if it can be fixed.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-49330, 200, -94050, 3000)

    def lambda_2FCF():

        label("loc_2FCF")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_2FCF")

    QueueWorkItem2(0x101, 1, lambda_2FCF)

    def lambda_2FE1():

        label("loc_2FE1")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_2FE1")

    QueueWorkItem2(0x102, 1, lambda_2FE1)

    def lambda_2FF3():

        label("loc_2FF3")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_2FF3")

    QueueWorkItem2(0x103, 1, lambda_2FF3)

    def lambda_3005():

        label("loc_3005")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_3005")

    QueueWorkItem2(0x104, 1, lambda_3005)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(10000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x1)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x103)

    def lambda_308C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_308C)
    Sleep(50)

    def lambda_309C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_309C)

    def lambda_30A9():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30A9)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#1100885V#0103F#5PI'm afraid this might take some time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100886V#0001F#12PWe should probably return to the city and let\x01",
            "the Transportation Division know about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100887V#0206F#5P*sigh* Typical.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100888V#0306F#11PI ain't a fan of it, either, but it doesn't\x01",
            "look like we have much choi--\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0xE1, 0x1F4)

    ChrTalk(
        0x104,
        "#1100889V#0307F#11PHeads-up!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x9, 0x3)

    def lambda_3295():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3295)

    def lambda_32A2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32A2)
    Sleep(100)

    def lambda_32B2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32B2)

    def lambda_32BF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32BF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    OP_68(-50900, 1600, -98850, 0)
    MoveCamera(7, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22200, 0)
    OP_68(-51930, 1600, -99720, 1500)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#1100890V#5PA-AHHHH!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100891V#0005F#2P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100892V#0201F#11PNot good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100893V#0107F#2PThere's still more of them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100894V#0303F#11PThis isn't lookin' too hot...\x02\x03",
            "#1100895V#0307FHey, Lloyd! I don't think we can take\x01",
            "all of 'em at once!\x02\x03",
            "#1100896VLet's team up on one before we worry\x01",
            "about the rest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100897V#0007F#11PNo, that won't work!\x02\x03",
            "#1100898VIt'll be over if one gets near the bus!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100899V#0310F#11PDamn, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100900V#0101F#2PBut we have to do something!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1500)
    EndChrThread(0xC, 0x3)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(835, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 22)

    def lambda_3621():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3621)
    Sleep(300)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 3, 0, 22)

    def lambda_365B():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_365B)
    Sleep(200)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 3, 0, 22)

    def lambda_3695():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3695)
    WaitChrThread(0xC, 1)
    EndChrThread(0xC, 0x3)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    WaitChrThread(0xD, 1)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 3, 0, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 3, 0, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#1100901V#0207F#2PIncoming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100902V#0010F#2P(...!)\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1701, 255, 100, 0)
    StopBGM(0x4B0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x192), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(22500, 1250)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xA, 3, 0, 23)
    BeginChrThread(0xB, 3, 0, 24)

    def lambda_37A0():
        OP_95(0xFE, -50690, 0, -99150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_37A0)
    Sleep(750)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x96, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x0, 0xFF, 0xA, 0x140, 0, -300, 1250, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 22)
    BeginChrThread(0xD, 3, 0, 22)
    BeginChrThread(0xE, 3, 0, 22)

    def lambda_3874():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3874)

    def lambda_388E():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_388E)

    def lambda_38A8():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_38A8)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    BeginChrThread(0xE, 3, 0, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0xB, 0x3)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    TurnDirection(0xB, 0xD, 500)
    WaitChrThread(0xA, 3)
    OP_6F(0x10)
    CancelBlur(0)
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
        "#1100904V#0005F#2P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100905V#0305F#2PThe hell?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Girl With Twintails",
        "#1100906V#0807F#5PJoshua!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Black-Haired Boy",
        "#1100907V#0903F#11PRight!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle(0xFFFFFFFF, 0x30200003, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30068501, 0x30068501, 0x30068501, 0x0, 0x0, 0x0, 0x0, 0x0, 0x192, 0x8)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 19)
    Return()

    # Function_18_274E end

    def Function_19_3AFE(): pass

    label("Function_19_3AFE")

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
    LoadChrToIndex("monster/ch68553.itc", 0x28)
    LoadChrToIndex("chr/ch00650.itc", 0x2C)
    LoadChrToIndex("chr/ch00750.itc", 0x2D)
    LoadEffect(0x0, "battle\\ms00001.eff")
    OP_68(-53870, 800, -99910, 0)
    MoveCamera(6, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24120, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -48420, 0, -95970, 225)
    SetChrPos(0x102, -47190, 0, -95080, 225)
    SetChrPos(0x103, -45450, 0, -95570, 225)
    SetChrPos(0x104, -46730, 0, -96390, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -53630, 0, -94960, 180)
    Call(0, 16)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -51980, 0, -98210, 225)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -50720, 0, -98630, 225)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xC, -58010, 0, -97980, 45)
    SetChrPos(0xD, -55680, 0, -100660, 45)
    SetChrPos(0xE, -55780, 0, -104760, 45)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(22620, 1500)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x0, 0x96, 0x1770, 0x3E8)
    BeginChrThread(0xC, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xE, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sound(816, 0, 100, 0)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    Sleep(500)
    OP_68(-51040, 800, -95930, 2500)
    OP_6F(0x79)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1100908V#0005F#11PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100909V#0105F#11PA-Amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100910V#0205F#11PThey are incredible.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0xB,
        "Black-Haired Boy",
        (
            "#1100911V#0903F#11PPhew... Looks like we made it just\x01",
            "in the nick of time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(300)

    NpcTalk(
        0xB,
        "Black-Haired Boy",
        "#1100912V#0900F#11PAre you okay, Estelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)
    Sleep(300)

    NpcTalk(
        0xA,
        "Girl With Twintails",
        (
            "#1100913V#0804F#5PYep. That was nothing!\x02\x03",
            "#1100914V#0800FBoy, I'm sure glad I got the timing right\x01",
            "on that, Joshua. I would have died of\x01",
            "embarrassment if I tripped.\x02\x03",
            "#1100915V#0805FBut, uh, enough about me.\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7519", 0)
    OP_68(-49690, 800, -95970, 2000)

    def lambda_40AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40AB)
    TurnDirection(0xB, 0x101, 500)
    OP_93(0x9, 0x87, 0x1F4)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    NpcTalk(
        0xA,
        "Girl With Twintails",
        (
            "#1100916V#0800F#6PAre you guys with the Crossbell police?\x02\x03",
            "#1100917VSomeone from the Transportation Division\x01",
            "near the south exit told us about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100974V#0011F#11PY-Yeah, we are.\x02\x03",
            "#1100919V#0001FAnd who are you two?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Girl With Twintails",
        (
            "#1100920V#0809F#6PWhoops! We totally forgot to\x01",
            "introduce ourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(1702, 255, 100, 0)
    SetChrName("Girl With Twintails")

    AnonymousTalk(
        0xFF,
        (
            "#1100921VI'm Estelle Bright!\x02\x03",
            "#1100922VNice to meet'cha, officers!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    Sound(1770, 255, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Black-Haired Boy")

    AnonymousTalk(
        0xFF,
        (
            "#1100923VAnd I'm Joshua.\x02\x03",
            "#1100924VWe recently transferred over to the\x01",
            "Bracer Guild's Crossbell branch.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#1100925V#0006F#11P(It figures it'd be bracers. Can't say I'm surprised...)\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-49950, 800, -96090, 800)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1100926V#0003F#11PNice to meet you two. We're members of\x01",
            "the CPD's Special Support Section.\x02\x03",
            "#1100927V#0000FThanks a lot, by the way. You really\x01",
            "helped us get out of that jam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100928V#0809F#6PHahaha... I don't deserve that much credit.\x02\x03",
            "#1100929V#0800FAnd besides, the four of you put up a\x01",
            "pretty good fight. I almost considered\x01",
            "sitting back and enjoying the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100930V#0006F#11PNo, that isn't true. Things could have taken\x01",
            "a turn for the worse if you hadn't shown up.\x02\x03",
            "#1100931V#0000FI'm Lloyd. Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100932V#0100F#11PMy name's Elie MacDowell.\x01",
            "It's a pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100933V#0302F#11PName's Randy Orlando.\x01",
            "How's it hangin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100934V#0203F#11PTio Plato.\x01",
            "Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100935V#0800F#6PI gotta remember those.\x01",
            "Lloyd, Elie, Randy, and Tio...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#1100936V#0805F#6PWait... Tio and Lloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1100937V#0909F#6PHaha. What are the odds?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100938V#0005F#11PAm I missing something, or...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100939V#0205F#11PDo you find our names amusing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100940V#0809F#6PHahaha... Sorry about that!\x02\x03",
            "#1100941V#0802FI just thought it was funny because\x01",
            "I have two friends named Tio and\x01",
            "Lloyd.\x02\x03",
            "#1100942VYou obviously look nothing alike,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100943V#0000F#11PO-Okay, then...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x9, 500)

    ChrTalk(
        0xB,
        (
            "#1100944V#0901F#12PGetting back to the topic at hand.\x01",
            "How's the orbal bus doing?\x02\x03",
            "#1100945VIt was having some problems with\x01",
            "its engine, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x9, 500)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1100946V#5PY-Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100947V#5PI think there might be a weak connection\x01",
            "with the quartz, but I'm not sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100948V#5PMan, if I knew this was going to\x01",
            "happen, I would've paid more\x01",
            "attention in maintenance class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1100949V#0903F#12PIf you don't mind, could I take a look\x01",
            "at it?\x02\x03",
            "#1100950V#0900FI might be able to get it up and running\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1100951V#5PS-Seriously?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#1100952V#0802F#5PY'know, Joshua is pretty darn good\x01",
            "at handling airships.\x02\x03",
            "#1100953VMaybe maintenance is his true calling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100954V#5POh, bless the Bracer Guild! You guys\x01",
            "always know what to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1100955V#0904F#12PNo, I think you just got lucky.\x02",
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
        0x104,
        (
            "#1100956V#0301F#11P(Yo, Tio Tot... You a maintenance\x01",
            "guru, too?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100957V#0206F#11P(That is unfortunately outside of\x01",
            "my area of expertise...)\x02\x03",
            "#1100958V(I am fairly proficient with orbal\x01",
            "network equipment, however.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    def lambda_4E63():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4E63)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#1100959V#0805F#6PSo anyway, what are you guys all\x01",
            "up to out here?\x02\x03",
            "#1100960V#0800FDid you have a monster extermination\x01",
            "to take care of or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100961V#0011F#11PNo, not exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100962V#0103F#11PWe were actually heading to the\x01",
            "hospital on police business.\x02\x03",
            "#1100963V#0100FThis whole situation wasn't\x01",
            "a part of the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1100964V#0900F#6PSt. Ursula Medical College, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100965V#0805F#6POh, hey! I've heard of that place before!\x02\x03",
            "#1100966V#0800FWe'd be happy to take it from here,\x01",
            "since you guys are busy.\x02\x03",
            "#1100967VAfter all, we wouldn't want you guys to\x01",
            "get held up on your own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100968V#0105F#11PA-Are you sure?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#1100969V#0003F#11PThank you. We'll take you up on that offer.\x02\x03",
            "#1100970V#0000FYou said your names are Estelle\x01",
            "and Joshua, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100971V#0809F#6PYep, that's us!\x02\x03",
            "#1100972V#0802FAnd don't go getting all formal on us just\x01",
            "because we're all professionals here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1100973V#0902F#6PYeah, she's right. I'd like it if we could all\x01",
            "treat each other as friends, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100918V#0005F#11PY-Yeah, sounds good.\x02\x03",
            "#1100975V#0004FWell, then, Estelle and Joshua...\x02\x03",
            "#1100976V#0000FPlease take care of this bus and\x01",
            "its passengers in our stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1100977V#0809F#6PSure thing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1100978V#0900F#6PTake care of yourselves out there.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(1775, 255, 90, 0)
    SetCameraDistance(23120, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7200", 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x28)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_37()
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -51350, 0, -96010, 315)
    SetChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xB, -52810, 0, -95050, 45)
    SetChrFlags(0xB, 0x10)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -53470, 0, -94190, 45)
    ClearMapObjFlags(0x2, 0x4)
    SetChrPos(0x0, -47400, 0, -96310, 225)
    SetScenarioFlags(0x61, 3)
    OP_29(0x3F, 0x1, 0x7)
    ModifyEventFlags(0, 0, 0x80)
    OP_E0(0x0)
    Call(0, 9)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_19_3AFE end

    def Function_20_5462(): pass

    label("Function_20_5462")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5486")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_20_5462")

    label("loc_5486")

    Return()

    # Function_20_5462 end

    def Function_21_5487(): pass

    label("Function_21_5487")

    OP_95(0xFE, -47450, 0, -94270, 2000, 0x0)
    OP_95(0xFE, -48230, 0, -94830, 2000, 0x0)
    OP_95(0xFE, -50330, 0, -94830, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sound(822, 0, 100, 0)
    Sleep(1000)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_71(0x0, 0x12D, 0x14A, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_95(0xFE, -51890, 0, -96080, 2000, 0x0)
    OP_95(0xFE, -53450, 0, -94190, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sound(833, 0, 100, 0)
    Sleep(2000)

    label("loc_553B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5585")
    OP_96(0xFE, 0xFFFF3152, 0x0, 0xFFFE8D74, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    OP_96(0xFE, 0xFFFF2F36, 0x0, 0xFFFE9012, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    Jump("loc_553B")

    label("loc_5585")

    Return()

    # Function_21_5487 end

    def Function_22_5586(): pass

    label("Function_22_5586")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55A0")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_22_5586")

    label("loc_55A0")

    Return()

    # Function_22_5586 end

    def Function_23_55A1(): pass

    label("Function_23_55A1")


    def lambda_55A6():
        OP_9D(0xFE, 0xFFFF35A8, 0x0, 0xFFFE8018, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55A6)
    Sound(814, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    Sleep(600)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_A1(0xFE, 0x3E8, 0x6, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_55A1 end

    def Function_24_560A(): pass

    label("Function_24_560A")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_5612")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_562D")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_5612")

    label("loc_562D")

    Return()

    # Function_24_560A end

    def Function_25_562E(): pass

    label("Function_25_562E")

    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 1500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_566A():
        OP_A6(0xFE, 0x96, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_566A)

    def lambda_5683():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5683)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_25_562E end

    def Function_26_56A2(): pass

    label("Function_26_56A2")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-50910, 800, -96660, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18850, 0)
    SetCameraDistance(17850, 2500)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -51450, 0, -96010, 135)
    SetChrPos(0x101, -50470, 0, -97180, 315)
    SetChrPos(0x102, -49360, 0, -97230, 315)
    SetChrPos(0x103, -50060, 0, -99050, 315)
    SetChrPos(0x104, -48830, 0, -98720, 315)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#1100979V#0805F#5PHey, so you guys said you were the\x01",
            "Special Support Section, right?\x02\x03",
            "#1100980V#0800FI think I heard it's pretty similar to\x01",
            "the Bracer Guild... Is that true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100981V#0011F#11PAbout that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100982V#0108F#11PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100983V#0206F#12PWell, you are not technically wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100984V#0809F#5POh, yeah? It kinda makes\x01",
            "me happy to hear that!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100985V#0005F#11PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100986V#0305F#12PDunno why that'd make you happy,\x01",
            "but you do you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1100987V#0802F#5PWell, the way I see it, we're kinda in\x01",
            "the same line of work, aren't we?\x02\x03",
            "#1100988VSo in my eyes, we're basically\x01",
            "friends already!\x02\x03",
            "#1100989V#0809FLet's do our best, everyone!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x104,
        "#1100990V#0302F#12P(This girl...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100991V#0204F#12P(Her heart may be even larger than\x01",
            "Lloyd's... I never thought I would\x01",
            "see the day.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100992V#0102F#11P(I've never met somebody as bright as her...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100993V#0012F#11PThanks, haha.\x02\x03",
            "#1100994V#0002FI'm also looking forward to working\x01",
            "with you, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -51450, 0, -96010, 315)
    SetChrPos(0x0, -50600, 0, -97410, 225)
    SetScenarioFlags(0x61, 4)
    OP_E0(0x2)
    Call(0, 9)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_26_56A2 end

    def Function_27_5C19(): pass

    label("Function_27_5C19")

    EventBegin(0x0)
    OP_E0(0x3)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Fade(1000)
    OP_68(-5760, 1000, 3900, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAD")
    SetChrPos(0x101, -2660, 0, 8920, 210)
    SetChrPos(0x102, -1580, 0, 8109, 210)
    SetChrPos(0x103, -80, 0, 9090, 210)
    SetChrPos(0x104, -1280, 0, 9660, 210)
    Jump("loc_5CF1")

    label("loc_5CAD")

    SetChrPos(0x101, -310, 0, -500, 315)
    SetChrPos(0x102, -70, 0, -1700, 315)
    SetChrPos(0x103, 1340, 0, -1430, 315)
    SetChrPos(0x104, 1070, 0, -350, 315)

    label("loc_5CF1")


    def lambda_5CF6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CF6)

    def lambda_5D0B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D0B)

    def lambda_5D20():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D20)

    def lambda_5D35():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D35)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(19500, 2500)

    def lambda_5DAF():
        OP_95(0xFE, -5470, 0, 4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DAF)

    def lambda_5DC9():
        OP_95(0xFE, -4680, 0, 3270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DC9)

    def lambda_5DE3():
        OP_95(0xFE, -3230, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DE3)

    def lambda_5DFD():
        OP_95(0xFE, -4160, 0, 5120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DFD)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E75")
    WaitChrThread(0x104, 1)

    def lambda_5E25():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E25)
    WaitChrThread(0x101, 1)

    def lambda_5E36():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E36)
    WaitChrThread(0x103, 1)

    def lambda_5E47():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E47)
    WaitChrThread(0x102, 1)

    def lambda_5E58():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E58)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_5EC9")

    label("loc_5E75")

    WaitChrThread(0x102, 1)

    def lambda_5E7E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E7E)
    WaitChrThread(0x101, 1)

    def lambda_5E8F():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E8F)
    WaitChrThread(0x104, 1)

    def lambda_5EA0():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EA0)
    WaitChrThread(0x103, 1)

    def lambda_5EB1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EB1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    label("loc_5EC9")

    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_5F6B")

    ChrTalk(
        0x101,
        (
            "#2201042V#0001F#11PStargazer's Tower should\x01",
            "be right past here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201043V#0101F#11PIndeed. But the CGF has it barricaded\x01",
            "off, remember?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FF4")

    label("loc_5F6B")


    ChrTalk(
        0x101,
        "#2201044V#0001F#11PStargazer's Tower is this way...right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201045V#0101F#11PConsidering the landmarks,\x01",
            "I'm inclined to agree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF4")


    ChrTalk(
        0x104,
        "#2201046V#0300F#11PWell, no way to go but forward.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201047V#0202F#11PIndeed.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -6520, 0, 4300, 270)
    SetScenarioFlags(0x84, 0)
    OP_E0(0x2)
    Call(0, 9)
    EventEnd(0x5)
    Return()

    # Function_27_5C19 end

    def Function_28_606B(): pass

    label("Function_28_606B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 27)
    Return()

    # Function_28_606B end

    def Function_29_6079(): pass

    label("Function_29_6079")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_613F")

    ChrTalk(
        0x104,
        "#0300FRoad leads into the forest, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah. I've actually heard there are\x01",
            "ruins hidden somewhere in there.\x02\x03",
            "Though, we don't have any\x01",
            "reason to check it out now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_618C")

    label("loc_613F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The road leads into the forest.\x01",
            "There's no need to enter it now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_618C")

    Sleep(50)
    SetChrPos(0x0, -39950, -1400, -1490, 90)
    EventEnd(0x4)
    Return()

    # Function_29_6079 end

    SaveToFile()

Try(main)
