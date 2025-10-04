from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3023.bin",                # FileName
        "m3023",                    # MapName
        "m3023",                    # Location
        0x007D,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 2, 0, 3],
    )

    BuildStringList((
        "m3023",                  # 0
        "Don Marconi",            # 1
        "Mafioso",                # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Sea Moon",               # 5
        "Sea Moon",               # 6
        "bm3020",                 # 7
        "bm3020",                 # 8
        "bm3020",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   4,   12,  0,   24,  8,   16)
    Sepith("Sepith_B4", 2,   0,   4,   14,  16,  9,   18)

    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_F0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_F4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_FC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 8, 14, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_124", 0x0000, 40, 6, 60, 4, 1, 40, 0, "bm3020", "Sepith_A4", 60, 25, 10, 5,
        (
            ("ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", "ms71100.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1EC", 0x0000, 40, 6, 60, 4, 1, 50, 0, "bm3020", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms77100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms77100.dat", "ms77100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms77100.dat", "ms77100.dat", "ms71100.dat", "ms77100.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2B4", 0x0010, 40, 6, 60, 4, 1, 0, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06200.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "chr/ch36100.itc",                   # 02
        "chr/ch36200.itc",                   # 03
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
        "monster/ch77150.itc",               # 10
        "monster/ch77150.itc",               # 11
        "monster/ch71150.itc",               # 12
        "monster/ch71151.itc",               # 13
        "monster/ch68450.itc",               # 14
        "monster/ch68450.itc",               # 15
    ))

    DeclNpc(-10899,  -54000,  -104500, 180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-12000,  -54000,  -103599, 180,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-9800,   -54000,  -103599, 180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-10899,  -54000,  -102699, 180,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-10250,  -52500,  -116500, 0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-148250, -55500,  -46250,  0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(14110,   2110,    -54000,  0x1010000,    "BattleInfo_124", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-161850, -18710,  -54000,  0x1010000,    "BattleInfo_1EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(161530,  -121810, -54000,  0x1010000,    "BattleInfo_1EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(205280,  -121920, -60000,  0x1010000,    "BattleInfo_124", 0,   18,  0xFFFF, 2,  3)

    DeclActor(31500,   -54000,  1500,    1200,    31500,   -53000,  1500,    0x007C, 0,  4,  0x0000)
    DeclActor(-161500, -54000,  -47750,  1200,    -161500, -53000,  -47750,  0x007C, 0,  5,  0x0000)
    DeclActor(-10250,  -54000,  -116500, 1200,    -10250,  -53000,  -116500, 0x007C, 0,  6,  0x0000)
    DeclActor(28000,   -54000,  -101500, 1200,    28000,   -53000,  -101500, 0x007C, 0,  7,  0x0000)
    DeclActor(-148250, -57000,  -46250,  1200,    -148250, -56000,  -46250,  0x007C, 0,  8,  0x0000)
    DeclActor(19500,   -54000,  -106400, 1200,    19500,   -53000,  -106400, 0x007C, 0,  15, 0x0000)
    DeclActor(6750,    -54000,  -114350, 1200,    6750,    -53000,  -114350, 0x007C, 0,  16, 0x0000)
    DeclActor(-16500,  -54000,  -106400, 1200,    -16500,  -53000,  -106400, 0x007C, 0,  17, 0x0000)
    DeclActor(158250,  -54000,  -98400,  1200,    158250,  -53000,  -98400,  0x007C, 0,  18, 0x0000)
    DeclActor(233500,  -60000,  -121500, 1200,    233500,  -58500,  -121500, 0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3

    ScpFunction((
        "Function_0_660",          # 00, 0
        "Function_1_718",          # 01, 1
        "Function_2_734",          # 02, 2
        "Function_3_79C",          # 03, 3
        "Function_4_BFB",          # 04, 4
        "Function_5_D4B",          # 05, 5
        "Function_6_EA2",          # 06, 6
        "Function_7_10E7",         # 07, 7
        "Function_8_1274",         # 08, 8
        "Function_9_14A1",         # 09, 9
        "Function_10_1556",        # 0A, 10
        "Function_11_1ECA",        # 0B, 11
        "Function_12_2004",        # 0C, 12
        "Function_13_2076",        # 0D, 13
        "Function_14_217F",        # 0E, 14
        "Function_15_227F",        # 0F, 15
        "Function_16_23CD",        # 10, 16
        "Function_17_251B",        # 11, 17
        "Function_18_255B",        # 12, 18
        "Function_19_26A9",        # 13, 19
    ))


    def Function_0_660(): pass

    label("Function_0_660")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6A0"),
        (1, "loc_6AC"),
        (2, "loc_6B8"),
        (3, "loc_6C4"),
        (4, "loc_6D0"),
        (5, "loc_6DC"),
        (6, "loc_6E8"),
        (SWITCH_DEFAULT, "loc_6F4"),
    )


    label("loc_6A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_6F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_700")

    label("loc_717")

    Return()

    # Function_0_660 end

    def Function_1_718(): pass

    label("Function_1_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_718")

    label("loc_733")

    Return()

    # Function_1_718 end

    def Function_2_734(): pass

    label("Function_2_734")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74E")
    Event(0, 19)

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_END)), "loc_79B")
    SetChrPos(0x8, 4300, -54000, -106450, 225)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)

    label("loc_79B")

    Return()

    # Function_2_734 end

    def Function_3_79C(): pass

    label("Function_3_79C")

    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 0)), scpexpr(EXPR_END)), "loc_7B8")
    OP_70(0x7, 0x1E)
    OP_70(0x6, 0x1E)
    Jump("loc_7C0")

    label("loc_7B8")

    OP_70(0x7, 0x0)
    OP_70(0x6, 0x0)

    label("loc_7C0")

    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 1)), scpexpr(EXPR_END)), "loc_7DC")
    OP_70(0x8, 0x1E)
    OP_70(0x4, 0x1E)
    Jump("loc_7E4")

    label("loc_7DC")

    OP_70(0x8, 0x0)
    OP_70(0x4, 0x0)

    label("loc_7E4")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_END)), "loc_800")
    OP_70(0x9, 0x1E)
    OP_70(0x5, 0x32)
    Jump("loc_808")

    label("loc_800")

    OP_70(0x9, 0x0)
    OP_70(0x5, 0x0)

    label("loc_808")

    ClearMapObjFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_824")
    OP_70(0xA, 0x1E)
    OP_70(0xB, 0x1E)
    Jump("loc_82C")

    label("loc_824")

    OP_70(0xA, 0x0)
    OP_70(0xB, 0x0)

    label("loc_82C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84F")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_854")

    label("loc_84F")

    ClearMapFlags(0x2000)

    label("loc_854")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -150000, -55000, -4000, 5000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -150000, -55000, -17000, 5000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 7)), scpexpr(EXPR_END)), "loc_8B1")
    SetMapObjFrame(0xFF, "mizu1", 0x2, "low")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    Jump("loc_8C7")

    label("loc_8B1")

    SetMapObjFrame(0xFF, "mizu1", 0x2, "high")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_8C7")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9A")
    OP_70(0x0, 0x0)
    Jump("loc_B9E")

    label("loc_B9A")

    OP_70(0x0, 0x1E)

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB1")
    OP_70(0x1, 0x0)
    Jump("loc_BB5")

    label("loc_BB1")

    OP_70(0x1, 0x1E)

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC8")
    OP_70(0x2, 0x0)
    Jump("loc_BCC")

    label("loc_BC8")

    OP_70(0x2, 0x1E)

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDF")
    OP_70(0x3, 0x0)
    Jump("loc_BE3")

    label("loc_BDF")

    OP_70(0x3, 0x1E)

    label("loc_BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF6")
    OP_70(0xC, 0x0)
    Jump("loc_BFA")

    label("loc_BF6")

    OP_70(0xC, 0x1E)

    label("loc_BFA")

    Return()

    # Function_3_79C end

    def Function_4_BFB(): pass

    label("Function_4_BFB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_C7B")
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
    SetScenarioFlags(0x11B, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_CE0")

    label("loc_C7B")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CE0")

    Jump("loc_D3F")

    label("loc_CE5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I expected nothing, and I'm still disappointed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D3F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_BFB end

    def Function_5_D4B(): pass

    label("Function_5_D4B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E35")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_DCB")
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
    SetScenarioFlags(0x11B, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_E30")

    label("loc_DCB")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E30")

    Jump("loc_E96")

    label("loc_E35")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found nothing.\x01",
            "Can't hold any more, so left it behind.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E96")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_D4B end

    def Function_6_EA2(): pass

    label("Function_6_EA2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1061")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA1")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_EFB():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EFB)

    def lambda_F15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F15)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_2B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F82"),
        (2, "loc_F91"),
        (1, "loc_F9E"),
        (SWITCH_DEFAULT, "loc_FA1"),
    )


    label("loc_F82")

    SetScenarioFlags(0x77, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_FA1")

    label("loc_F91")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_F9E")

    OP_B7(0x0)
    Return()

    label("loc_FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EE, 1)"), scpexpr(EXPR_END)), "loc_FF9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_105C")

    label("loc_FF9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5EE),
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

    label("loc_105C")

    Jump("loc_10DB")

    label("loc_1061")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can argue over who best boy is, but I think\x01",
            "we can all agree that Zeit is goodest boy.\x07\x00\x02",
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

    # Function_6_EA2 end

    def Function_7_10E7(): pass

    label("Function_7_10E7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1222")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11D, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1262")

    label("loc_1222")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is what I get for opening myself up to others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1262")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_10E7 end

    def Function_8_1274(): pass

    label("Function_8_1274")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1433")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_12CD():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12CD)

    def lambda_12E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_12E7)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_2B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1354"),
        (2, "loc_1363"),
        (1, "loc_1370"),
        (SWITCH_DEFAULT, "loc_1373"),
    )


    label("loc_1354")

    SetScenarioFlags(0x77, 2)
    OP_70(0xC, 0x1E)
    Sleep(500)
    Jump("loc_1373")

    label("loc_1363")

    OP_70(0xC, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1370")

    OP_B7(0x0)
    Return()

    label("loc_1373")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x443, 1)"), scpexpr(EXPR_END)), "loc_13CB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x443),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11D, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_142E")

    label("loc_13CB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x443),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_142E")

    Jump("loc_1495")

    label("loc_1433")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "How can Estelle spin her staff so fast?\x01",
            "Because it's a hurry-cane!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1495")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1274 end

    def Function_9_14A1(): pass

    label("Function_9_14A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 4)), scpexpr(EXPR_END)), "loc_154F")

    ChrTalk(
        0x8,
        (
            "#3005FP-Please believe me... We weren't the\x01",
            "ones who killed that irritating detective!\x02\x03",
            "#3007FIt was Joachim! All of this mess is that\x01",
            "bastard's fault!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1552")

    label("loc_154F")

    Call(0, 10)

    label("loc_1552")

    TalkEnd(0xFE)
    Return()

    # Function_9_14A1 end

    def Function_10_1556(): pass

    label("Function_10_1556")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis093.itp")
    OP_68(3080, -52600, -107620, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13750, 0)
    SetChrPos(0x101, 2950, -54000, -107770, 45)
    SetChrPos(0x102, 3750, -54000, -108770, 0)
    SetChrPos(0x103, 2500, -54000, -106500, 90)
    SetChrPos(0x104, 2100, -54000, -107980, 45)
    SetChrPos(0x107, 1500, -54000, -108750, 45)
    SetChrPos(0x108, 600, -54000, -108790, 45)
    SetChrPos(0x9, 6080, -54000, -108260, 180)
    SetChrPos(0xA, 7480, -54000, -109660, 315)
    SetChrPos(0xB, 5250, -54000, -110050, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0003F...Don Marconi. Answer me.\x02\x03",
            "#0001FDo you recognize this?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#3005F#11PA police badge...? I feel like I've seen this\x01",
            "one before...\x02\x03",
            "#3001F...!\x02\x03",
            "#3007FTh-That's the badge of that insufferable\x01",
            "detective...!\x02\x03",
            "How did you get your hands on that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    ChrTalk(
        0x101,
        (
            "#0006FFunny. I was going to ask you the same thing.\x02\x03",
            "#0001FYou killed the owner of this badge, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3002F#11PI-I don't know what you're talking about.\x02\x03",
            "#3004FBesides, you might meet the same fate\x01",
            "as him if you get carried away.\x02\x03",
            "#3002FBetter learn your place quick and make\x01",
            "sure to keep us happy, or else...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#0010F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3005F#11P*gulp* Fine! I'll talk, okay?!\x02\x03",
            "That pest was named Guy, right? Well, sorry,\x01",
            "'cause we weren't the ones who killed him!\x02\x03",
            "#3003FY-Yeah, we might have been planning on taking\x01",
            "him out since he was such a pain in the ass to\x01",
            "deal with...but still!\x02\x03",
            "#3007FBefore we could act, some other guy did the\x01",
            "job for us!\x02\x03",
            "That badge was just some piece of junk that\x01",
            "my men took from the scene of the crime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F#6PIs that really the whole truth?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F#5PHe does not seem to be lying, at least.\x02\x03",
            "#0211FThough, it is possible that he's simply\x01",
            "an incredibly good liar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F#5PIf everything he said was true, removin' key\x01",
            "evidence from the victim and hidin' it like a\x01",
            "treasure...\x02\x03",
            "#0301FYou got quite a strange hobby there, don'tcha,\x01",
            "Marconi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3001F#11PUgh, shut it.\x02\x03",
            "#3003FA-Anyway, we didn't kill him!\x02\x03",
            "#3005FYeah, he was probably... No, absolutely\x01",
            "killed by Joachim!\x02\x03",
            "#3000FAfter all, that detective was conducting\x01",
            "an investigation into Joachim while\x01",
            "annoying us, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FMy brother knew...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#0903FSo he had the mastermind pinned down\x01",
            "long before we found out about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#0802FLloyd's brother really sounds like he was\x01",
            "an amazing man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008F...\x02\x03",
            "#0006FIt doesn't matter. We'll learn the truth once\x01",
            "we capture Joachim.\x02\x03",
            "#0000FWe've spent enough time here. Everyone,\x01",
            "let's move out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#6PRight!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 3390, -54000, -105640, 135)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xEF, 4)
    EventEnd(0x5)
    Return()

    # Function_10_1556 end

    def Function_11_1ECA(): pass

    label("Function_11_1ECA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F2A")

    ChrTalk(
        0xFE,
        (
            "All our buddies, brainwashed... Th-The boss\x01",
            "must be okay, though, right?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F2A")


    ChrTalk(
        0xFE,
        "Why is this happening?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We should've destroyed Heiyue without\x01",
            "breaking a sweat with that drug.\x01",
            "We should be raking in mounds of mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And yet...damn it! Some things really\x01",
            "are too good to be true.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2000")

    TalkEnd(0xFE)
    Return()

    # Function_11_1ECA end

    def Function_12_2004(): pass

    label("Function_12_2004")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I guess Revache can't take on the\x01",
            "world, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once we get outta here...\x01",
            "what will we do?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2004 end

    def Function_13_2076(): pass

    label("Function_13_2076")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20BD")

    ChrTalk(
        0xFE,
        (
            "Boss... What the hell are we\x01",
            "supposed to do now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217B")

    label("loc_20BD")


    ChrTalk(
        0xFE,
        (
            "Garcia was opposed to using\x01",
            "that drug from the very beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said that once we went down that\x01",
            "slope, there'd be no getting back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He was right... About everything...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_217B")

    TalkEnd(0xFE)
    Return()

    # Function_13_2076 end

    def Function_14_217F(): pass

    label("Function_14_217F")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2262")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xD, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xD, 0x0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xD)
    OP_71(0xD, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0xD, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227E")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_227E")

    Return()

    # Function_14_217F end

    def Function_15_227F(): pass

    label("Function_15_227F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 0)), scpexpr(EXPR_END)), "loc_22CC")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever has already been pulled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_23CC")

    label("loc_22CC")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Pull it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C5")
    Fade(500)
    SetChrPos(0x0, 19740, -53940, -108080, 0)
    SetChrPos(0x1, 21500, -53990, -108010, 270)
    SetChrPos(0x2, 21500, -53990, -109380, 270)
    SetChrPos(0x3, 22680, -53990, -108600, 270)
    OP_68(16410, -52910, -107880, 0)
    MoveCamera(45, 37, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x6)
    Sleep(500)
    SetScenarioFlags(0xF5, 0)

    label("loc_23C5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_23CC")

    Return()

    # Function_15_227F end

    def Function_16_23CD(): pass

    label("Function_16_23CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 1)), scpexpr(EXPR_END)), "loc_241A")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever has already been pulled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_251A")

    label("loc_241A")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Pull it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2513")
    Fade(500)
    SetChrPos(0x0, 5090, -54000, -114250, 89)
    SetChrPos(0x1, 3700, -54000, -115420, 89)
    SetChrPos(0x2, 3700, -54000, -113640, 89)
    SetChrPos(0x3, 2700, -54000, -114250, 89)
    OP_68(6060, -53000, -116870, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x8)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetScenarioFlags(0xF5, 1)

    label("loc_2513")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_251A")

    Return()

    # Function_16_23CD end

    def Function_17_251B(): pass

    label("Function_17_251B")

    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever has already been pulled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    # Function_17_251B end

    def Function_18_255B(): pass

    label("Function_18_255B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_25A8")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever has already been pulled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_26A8")

    label("loc_25A8")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Pull it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A1")
    Fade(500)
    SetChrPos(0x0, 158000, -54000, -100000, 0)
    SetChrPos(0x1, 158900, -54000, -102000, 0)
    SetChrPos(0x2, 156840, -54000, -102000, 0)
    SetChrPos(0x3, 158000, -54000, -103560, 0)
    OP_68(160990, -53000, -99920, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xA)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    Sleep(500)
    SetScenarioFlags(0xF5, 2)

    label("loc_26A1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_26A8")

    Return()

    # Function_18_255B end

    def Function_19_26A9(): pass

    label("Function_19_26A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1500, -52900, -102000, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 900, -54000, -100200, 180)
    SetChrPos(0x102, 2100, -54000, -100200, 180)
    SetChrPos(0x103, 900, -54000, -98900, 180)
    SetChrPos(0x104, 2100, -54000, -98900, 180)
    SetChrPos(0x107, 4200, -54000, -99700, 180)
    SetChrPos(0x108, 3500, -54000, -99000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0x8, -10900, -54000, -104500, 90)
    SetChrPos(0x9, -12000, -54000, -103600, 90)
    SetChrPos(0xA, -9800, -54000, -103600, 90)
    SetChrPos(0xB, -10900, -54000, -102700, 90)
    OP_68(1500, -52900, -100000, 4000)
    MoveCamera(35, 35, 0, 4000)
    SetCameraDistance(20500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300305V#5P#0001FMore cells...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300306V#5P#0108FIt doesn't look like anyone's\x01",
            "in here, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    ChrTalk(
        0x103,
        "#5300307V#0211F#11PI wish.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#5300308VI-Is anyone there?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-10900, -52900, -103500, 3000)
    MoveCamera(35, 30, 0, 3000)
    SetCameraDistance(17500, 3000)

    def lambda_2964():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2964)
    Sleep(50)

    def lambda_2974():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2974)
    Sleep(50)

    def lambda_2984():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2984)
    Sleep(50)

    def lambda_2994():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2994)
    Sleep(50)

    def lambda_29A4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_29A4)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300309V#3P#0011FDon Marconi?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300310V#0805FWait... The don of Revache?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-10900, -53100, -105500, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -11500, -54000, -106700, 0)
    SetChrPos(0x102, -10300, -54000, -106700, 0)
    SetChrPos(0x103, -11500, -54000, -108000, 0)
    SetChrPos(0x104, -10300, -54000, -108000, 0)
    SetChrPos(0x107, -8500, -54000, -106800, 315)
    SetChrPos(0x108, -8400, -54000, -107800, 315)
    SetChrPos(0x8, -10900, -54000, -104500, 180)
    SetChrPos(0x9, -12000, -54000, -103600, 180)
    SetChrPos(0xA, -9800, -54000, -103600, 180)
    SetChrPos(0xB, -10900, -54000, -102700, 180)
    Sleep(500)
    SetCameraDistance(20000, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5300311V#3005F#5PH-Haven't I seen you before? Your\x01",
            "faces are rubbing me the wrong way...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5300312V#5PN-No way...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5300313V#5PIt's the Special Support Section brats!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5300314V#3007F#5PWhat?!\x02\x03",
            "#5300315VThose brats who ruined this\x01",
            "year's Schwarze Auction?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300316V#12P#0006FYou know, it wasn't exactly our intention to\x01",
            "send the entirety of Mishelam into a panic...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2D49")

    ChrTalk(
        0x102,
        (
            "#5300317V#0101F#12PRegardless, you all got what\x01",
            "was coming to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC3")

    label("loc_2D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2D8D")

    ChrTalk(
        0x103,
        "#5300318V#12P#0211FAs if you did not deserve it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC3")

    label("loc_2D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2DC3")

    ChrTalk(
        0x104,
        "#5300319V#12P#0309FKarma's a bitch, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_2DC3")


    ChrTalk(
        0x8,
        (
            "#5300320V#3001F#5PShut your mouths, you ingrates!\x02\x03",
            "#5300321V#3003FThis is all your fault! If that hadn't infuriated\x01",
            "the speaker, I would've never had to turn\x01",
            "to these drastic measures!\x02\x03",
            "#5300322V#3007FThis is all on you, punks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300323V#0806F#11PTalk about dodging the blame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300324V#0901F#11PAre you trying to say you AREN'T one\x01",
            "of Joachim's accomplices?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300325V#3007F#5PO-Of course I'm not!\x02\x03",
            "#5300326V#3003FHow was I supposed to know how\x01",
            "horrifying Gnosis could be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5300327V#5PO-Originally, we just thought it would\x01",
            "make everyone stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5300328V#5PEveryone in Revache started downing\x01",
            "it after the raid on Heiyue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5300329V#5PBut last night, every person who took\x01",
            "the drug started acting differently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5300330V#5PA-And then this happened...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5300331V#5PScarier than that, some of them began\x01",
            "to transform into disgusting creatures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5300332V#5POh, Aidios! Please forgive us for the\x01",
            "sins we've committed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300333V#12P#0303FSo that's how it went down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300334V#12P#0201FIt checks out with everything\x01",
            "we have presumed so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300335V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300336V#3002F#5PN-Now you know the real story!\x01",
            "I'm a victim in all this!\x02\x03",
            "#5300337VHurry up, let us out, and lead us\x01",
            "to somewhere safe...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#5300338V#12P#0010F#4SDon't push your luck!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5300339V#3005F#5PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300340V#12P#0010FJoachim Guenter is the mastermind!\x02\x03",
            "#5300341VHow can you claim no responsibility in this,\x01",
            "knowing that?!\x02\x03",
            "#5300342VRevache was the SOLE provider of Gnosis\x01",
            "to the citizenry, right?! Tell me I'm wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5300343V#5PW-Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300344V#12P#0003FI know your plan.\x02\x03",
            "#5300345VYou used Crossbell's citizens as lab rats\x01",
            "to evaluate the safety of Gnosis.\x02\x03",
            "#5300346V#0013FIf things went smoothly, you would have begun\x01",
            "to market the drug to potential buyers, expanding\x01",
            "its reach all over Zemuria...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#5300347V#12P#0007F#4SAm I wrong?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5300348V#3001F#5PTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5300349V#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5300350V#5PWe may have gone too far in\x01",
            "some places...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300351V#0103F#12PI doubt any diet member will attempt\x01",
            "to sweep this under the rug for you.\x02\x03",
            "#5300352V#0101FAs for Speaker Hartmann, he's under\x01",
            "investigation for multiple ties to Guenter.\x02\x03",
            "#5300353VKnow full well that nobody will be able\x01",
            "to shield you from the law now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5300354V#3007F#5PGrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300355V#12P#0306FWell, now that they know that...\x02\x03",
            "#5300356V#0301FWhat happened to Garcia?\x02\x03",
            "#5300357VWasn't he caught alongside\x01",
            "you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5300358V#5PThe boss fought Joachim until\x01",
            "the bitter end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5300359V#5PUnfortunately, the raw power of all those\x01",
            "monsters was too much for him to handle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5300360V#5PAnd we haven't seen him since...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300361V#12P#0303FThat so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300362V#12P#0208FThat is bad news.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    ChrTalk(
        0x107,
        (
            "#5300363V#0806F#11PYeah, it is.\x02\x03",
            "#5300364V#0801FHey, Lloyd.\x02\x03",
            "#5300365VWhat are you planning to do with them?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3A15():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3A15)
    Sleep(50)

    def lambda_3A25():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A25)
    Sleep(50)

    def lambda_3A35():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A35)
    Sleep(50)

    def lambda_3A45():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A45)
    Sleep(50)

    def lambda_3A55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A55)
    Sleep(50)

    def lambda_3A65():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A65)
    Sleep(50)

    def lambda_3A75():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3A75)

    ChrTalk(
        0x8,
        "#5300366V#3005F#5PEep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300367V#0806F#11PI think it'd be dangerous to leave them\x01",
            "in a place like this all alone...\x02\x03",
            "#5300368V#0808FBut if we free them, they might just take\x01",
            "the opportunity to run away, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300369V#6P#0008FTrue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300370V#0903F#11PIt's not an easy call.\x02\x03",
            "#5300371V#0901FWe'll trust your judgment, Lloyd.\x02\x03",
            "#5300372VBecause honestly, I'm not sure if the\x01",
            "guild's sworn duty to protect civilians\x01",
            "applies to Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300373V#6P#0003F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_92(0x101, 0xFFFFC0B8, 0xFFFE5A20, 0x1F4)
    OP_68(-15000, -53100, -106500, 2500)

    def lambda_3C9A():
        OP_95(0xFE, -16500, -54000, -108000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C9A)
    Sleep(50)

    def lambda_3CB7():

        label("loc_3CB7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3CB7")

    QueueWorkItem2(0x102, 2, lambda_3CB7)

    def lambda_3CC9():

        label("loc_3CC9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3CC9")

    QueueWorkItem2(0x8, 2, lambda_3CC9)
    Sleep(50)

    def lambda_3CDE():

        label("loc_3CDE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3CDE")

    QueueWorkItem2(0x103, 2, lambda_3CDE)
    Sleep(50)

    def lambda_3CF3():

        label("loc_3CF3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3CF3")

    QueueWorkItem2(0x104, 2, lambda_3CF3)

    def lambda_3D05():

        label("loc_3D05")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3D05")

    QueueWorkItem2(0x9, 2, lambda_3D05)

    def lambda_3D17():

        label("loc_3D17")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3D17")

    QueueWorkItem2(0xA, 2, lambda_3D17)

    def lambda_3D29():

        label("loc_3D29")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3D29")

    QueueWorkItem2(0xB, 2, lambda_3D29)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x1F4)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd pulled the lever.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-21500, -53100, -105000, 0)
    MoveCamera(0, 36, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(21500, 3000)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x9)
    Sound(155, 0, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0x5, 0x0, 0x32, 0x0, 0x0)
    OP_79(0x5)
    OP_6F(0x10)
    Fade(500)
    OP_68(-15000, -53100, -106500, 0)
    MoveCamera(43, 29, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5300374V#3002F#12PHah...hahaha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5300375VOh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5300376VW-We owe you one, kid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300377V#0205FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300378V#0304FGeez, ever the good cop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300379V#0102FWould you expect anything else?\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFFFFD314, 0xFFFE5F34, 0x1F4)
    OP_68(-10900, -53100, -105500, 2500)

    def lambda_3F95():

        label("loc_3F95")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3F95")

    QueueWorkItem2(0x102, 2, lambda_3F95)

    def lambda_3FA7():

        label("loc_3FA7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3FA7")

    QueueWorkItem2(0x103, 2, lambda_3FA7)

    def lambda_3FB9():

        label("loc_3FB9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3FB9")

    QueueWorkItem2(0x104, 2, lambda_3FB9)

    def lambda_3FCB():

        label("loc_3FCB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3FCB")

    QueueWorkItem2(0x8, 2, lambda_3FCB)

    def lambda_3FDD():

        label("loc_3FDD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3FDD")

    QueueWorkItem2(0x9, 2, lambda_3FDD)

    def lambda_3FEF():

        label("loc_3FEF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3FEF")

    QueueWorkItem2(0xA, 2, lambda_3FEF)

    def lambda_4001():

        label("loc_4001")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4001")

    QueueWorkItem2(0xB, 2, lambda_4001)

    def lambda_4013():
        OP_95(0xFE, -11500, -54000, -106700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4013)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)

    def lambda_4049():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4049)
    EndChrThread(0xB, 0x2)
    OP_6F(0x1)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5300380V#12P#0006FThis is only because it's an emergency.\x02\x03",
            "#5300381V#0001FIncredibly strong monsters wander around\x01",
            "this place like it's their home. Trying to\x01",
            "escape is tantamount to suicide.\x02\x03",
            "#5300382VMy advice is to stay put and wait for the\x01",
            "police to start their rescue mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300383V#3001F#5PHmph. Don't go barking orders\x01",
            "at me, brat!\x02\x03",
            "#5300384V#3007FYour job here is done! Scram!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300385V#0103F#11PWe should go.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5300386V#6P#0013FYeah. Let's press on!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1000, -53000, -108000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 1000, -54000, -108000, 90)
    SetChrPos(0x1, 1000, -54000, -108000, 90)
    SetChrPos(0x2, 1000, -54000, -108000, 90)
    SetChrPos(0x3, 1000, -54000, -108000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0x8, 4300, -54000, -106450, 225)
    SetChrPos(0x9, 5080, -54000, -108260, 180)
    SetChrPos(0xA, 6480, -54000, -109660, 315)
    SetChrPos(0xB, 4250, -54000, -110050, 45)
    SetScenarioFlags(0xE6, 2)
    OP_29(0x4F, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_26A9 end

    SaveToFile()

Try(main)
