from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0600.bin",                # FileName
        "t0600",                    # MapName
        "t0600",                    # Location
        0x0069,                     # MapIndex
        "ed7301",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 105, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0600",                  # 0
        "Mine Chief Hoffmann",    # 1
        "Miner Max",              # 2
        "Miner Marlow",           # 3
        "Miner Gantz",            # 4
        "Miner Logy",             # 5
        "Monster",                # 6
        "Monster",                # 7
        "Monster",                # 8
        "Monster",                # 9
        "Monster",                # 10
        "bt0600",                 # 11
        "bt0600",                 # 12
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 3,   3,   9,   3,   5,   4,   4)

    MonsterBattlePostion("MonsterBattlePostion_B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_114", 0x0000, 15, 6, 45, 6, 1, 30, 0, "bt0600", "Sepith_A4", 40, 30, 20, 10,
        (
            ("ms76400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76400.dat", "ms76400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76400.dat", "ms76400.dat", "ms76400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76400.dat", "ms76400.dat", "ms76400.dat", "ms76400.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1DC", 0x0002, 30, 6, 0, 0, 1, 40, 0, "bt0600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65101.dat", "ms65101.dat", "ms65101.dat", "ms65101.dat", "ms65101.dat", 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch26300.itc",                   # 00
        "chr/ch26200.itc",                   # 01
        "chr/ch30700.itc",                   # 02
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
        "monster/ch65150.itc",               # 10
        "monster/ch65150.itc",               # 11
        "monster/ch76450.itc",               # 12
        "monster/ch76451.itc",               # 13
    ))

    DeclNpc(-31850,  0,       32080,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-28860,  0,       56150,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4139,    0,       6690,    90,   385,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11470,  0,       15090,   19,   385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-17250,  50,      30370,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(109209,  -8949,   -9039,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(110739,  -8949,   -6610,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(106959,  -9000,   -9560,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(109220,  -8949,   -5909,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(107290,  -9000,   -11909,  135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-22150,  25270,   0,       0x1010000,    "BattleInfo_114", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(6200,    35950,   0,       0x1010000,    "BattleInfo_114", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(124120,  6350,    0,       0x1010000,    "BattleInfo_114", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(111590,  34990,   0,       0x1010000,    "BattleInfo_114", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(129789,  -23000,  -1950,   0x1010000,    "BattleInfo_114", 0,   18,  0xFFFF, 0,  1)

    DeclActor(129000,  0,       15000,   1200,    129000,  1000,    15000,   0x007C, 0,  9,  0x0000)
    DeclActor(130810,  0,       19250,   1200,    130810,  1000,    19250,   0x007C, 0,  10, 0x0000)
    DeclActor(119000,  -9000,   -26500,  1200,    119000,  -8000,   -26500,  0x007C, 0,  11, 0x0000)
    DeclActor(134600,  -2000,   -34220,  1200,    134600,  -1000,   -34220,  0x007C, 0,  12, 0x0000)
    DeclActor(-22540,  0,       54760,   1200,    -22540,  1500,    54760,   0x007C, 0,  17, 0x0000)
    DeclActor(117500,  -8950,   -15770,  1200,    117500,  -8000,   -15770,  0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1

    ScpFunction((
        "Function_0_560",          # 00, 0
        "Function_1_618",          # 01, 1
        "Function_2_643",          # 02, 2
        "Function_3_834",          # 03, 3
        "Function_4_D66",          # 04, 4
        "Function_5_158A",         # 05, 5
        "Function_6_19B0",         # 06, 6
        "Function_7_1DBF",         # 07, 7
        "Function_8_217B",         # 08, 8
        "Function_9_26C4",         # 09, 9
        "Function_10_2817",        # 0A, 10
        "Function_11_298B",        # 0B, 11
        "Function_12_2AF3",        # 0C, 12
        "Function_13_2C7B",        # 0D, 13
        "Function_14_354F",        # 0E, 14
        "Function_15_3C2E",        # 0F, 15
        "Function_16_4077",        # 10, 16
        "Function_17_4096",        # 11, 17
    ))


    def Function_0_560(): pass

    label("Function_0_560")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A0"),
        (1, "loc_5AC"),
        (2, "loc_5B8"),
        (3, "loc_5C4"),
        (4, "loc_5D0"),
        (5, "loc_5DC"),
        (6, "loc_5E8"),
        (SWITCH_DEFAULT, "loc_5F4"),
    )


    label("loc_5A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_5F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_600")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_617")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_600")

    label("loc_617")

    Return()

    # Function_0_560 end

    def Function_1_618(): pass

    label("Function_1_618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_642")
    OP_94(0xFE, 0xFFFFA7FE, 0x7F4E, 0xFFFFC3B0, 0x6AA4, 0x3E8)
    Sleep(300)
    Jump("Function_1_618")

    label("loc_642")

    Return()

    # Function_1_618 end

    def Function_2_643(): pass

    label("Function_2_643")

    BeginChrThread(0xC, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_693")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68E")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_68E")

    Jump("loc_833")

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6DD")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_6D8")

    Jump("loc_833")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_6EB")
    Jump("loc_833")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_73A")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_735")

    Jump("loc_833")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_784")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77F")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_77F")

    Jump("loc_833")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_792")
    Jump("loc_833")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7A0")
    Jump("loc_833")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7AE")
    Jump("loc_833")

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7BC")
    Jump("loc_833")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7CA")
    Jump("loc_833")

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7EC")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_833")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_80E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_833")

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_81C")
    Jump("loc_833")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_82A")
    Jump("loc_833")

    label("loc_82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_833")

    label("loc_833")

    Return()

    # Function_2_643 end

    def Function_3_834(): pass

    label("Function_3_834")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B")
    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")
    OP_E0(0x0)
    SetScenarioFlags(0x0, 5)

    label("loc_C00")

    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_C25")

    label("loc_C0B")

    SetMapFlags(0x2000)
    OP_E0(0x1)
    ClearScenarioFlags(0x0, 5)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_10(0x0, 0x1)
    OP_10(0x4, 0x0)

    label("loc_C25")

    Jump("loc_C3E")

    label("loc_C2A")

    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3E")
    OP_E0(0x0)
    SetScenarioFlags(0x0, 5)

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C51")
    OP_70(0x0, 0x0)
    Jump("loc_C55")

    label("loc_C51")

    OP_70(0x0, 0x1E)

    label("loc_C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C68")
    OP_70(0x1, 0x0)
    Jump("loc_C6C")

    label("loc_C68")

    OP_70(0x1, 0x1E)

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7F")
    OP_70(0x2, 0x0)
    Jump("loc_C83")

    label("loc_C7F")

    OP_70(0x2, 0x1E)

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C96")
    OP_70(0x3, 0x0)
    Jump("loc_C9A")

    label("loc_C96")

    OP_70(0x3, 0x1E)

    label("loc_C9A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -22700, 0, 54850, 10000, 2000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_END)), "loc_CE0")
    SetMapObjFrame(0xFF, "key00", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x10)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)
    Jump("loc_CFB")

    label("loc_CE0")

    SetMapObjFrame(0xFF, "key00", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x10)
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x4, 0x1)

    label("loc_CFB")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D65")
    OP_66(0x5, 0x1)
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 117500, -8750, -15770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_D65")

    Return()

    # Function_3_834 end

    def Function_4_D66(): pass

    label("Function_4_D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")

    ChrTalk(
        0xFE,
        "I heard about Gantz from the mayor's wife...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess that explains why Mayor Bickson\x01",
            "can't bring him home so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantz getting into drugs? I don't want to\x01",
            "believe it... I'll never forgive the guy who\x01",
            "dragged him into this mess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, now that I think about it, I kinda\x01",
            "want to sock Gantz in the face for falling\x01",
            "for such a stupid thing in the first place!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FFF")

    label("loc_F01")


    ChrTalk(
        0xFE,
        (
            "I'll never forgive the one who dragged\x01",
            "Gantz into that sort of life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though, the fact that Gantz let himself get\x01",
            "carried away like that is honestly pathetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that guy finally comes home, he's\x01",
            "getting a swift one to the jaw. Trust me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFF")

    Jump("loc_1586")

    label("loc_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(
        0xFE,
        (
            "Damn it, Gantz... I've heard that he just\x01",
            "keeps winning at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch. Is greed really enough to make someone\x01",
            "turn their back on everything they know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "When he comes back, I'll give him hell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1586")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_1586")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1176")

    ChrTalk(
        0xFE,
        "Where in the world has Gantz run off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, whatever. Nothing to do but mine and\x01",
            "mine and mine some more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1586")

    label("loc_1176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_121C")

    ChrTalk(
        0xFE,
        (
            "I can't wait for lunch. My wife always leaves\x01",
            "me goodies in there. Gah, I love that woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right. Last shift of the day!\x01",
            "Let's get to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1586")

    label("loc_121C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133A")

    ChrTalk(
        0xFE,
        (
            "Things have really come a long way,\x01",
            "even for us old-fashioned miners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Believe it or not, we didn't even have orbal lamps\x01",
            "when the previous mine chief was in charge!\x01",
            "Every day was just as perilous as the last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sure glad those days are gone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_141D")

    label("loc_133A")


    ChrTalk(
        0xFE,
        (
            "Nowadays, miners can worry less about getting\x01",
            "hurt and focus even more on their job. And the\x01",
            "crazy thing is, orbal tech is just beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heck, I don't know how much longer the world\x01",
            "is going to need miners like us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141D")

    Jump("loc_1586")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F1")

    ChrTalk(
        0xFE,
        "Max's injury finally healed, thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now we can finally get the mine back to\x01",
            "its standard pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I'm feeling it today! These rocks\x01",
            "can't stop my pickaxe!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_155C")

    label("loc_14F1")


    ChrTalk(
        0xFE,
        (
            "I'm glad Max is well enough to come back\x01",
            "to the mine... All right! Time to show this\x01",
            "mine who's boss!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155C")

    Jump("loc_1586")

    label("loc_1561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_156F")
    Jump("loc_1586")

    label("loc_156F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_157D")
    Jump("loc_1586")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1586")

    label("loc_1586")

    TalkEnd(0xFE)
    Return()

    # Function_4_D66 end

    def Function_5_158A(): pass

    label("Function_5_158A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1648")

    ChrTalk(
        0xFE,
        (
            "When that monster chewed me up real good,\x01",
            "everyone at the mine covered for my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I owe those guys a lot...so I can't let my\x01",
            "return go unnoticed! Let's do this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_170B")

    ChrTalk(
        0xFE,
        (
            "I've only heard rumors, but apparently, Gantz\x01",
            "is making a killing in the city's casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe we should have him throw us a party\x01",
            "in exchange for making us worry! Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_170B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1719")
    Jump("loc_19AC")

    label("loc_1719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17AB")

    ChrTalk(
        0xFE,
        (
            "Shoot... I just noticed a hole in this pipe.\x01",
            "Did some rats chew through it or something...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Gotta plug it up, either way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_17AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_182E")

    ChrTalk(
        0xFE,
        "Already been two weeks, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, Gantz is usually such a well-behaved\x01",
            "guy. What's been his deal lately...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18AA")

    ChrTalk(
        0xFE,
        (
            "Whew, I wouldn't be able to survive without\x01",
            "my wife's home-cooked lunches!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right! Back to work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1987")

    ChrTalk(
        0xFE,
        (
            "I was finally given the green light to\x01",
            "come back to work after my injuries\x01",
            "from the monster attack healed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I hated being confined to my bed.\x01",
            "I'm ready to burn off this energy in the mines!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AC")

    label("loc_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1995")
    Jump("loc_19AC")

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_19A3")
    Jump("loc_19AC")

    label("loc_19A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_19AC")

    label("loc_19AC")

    TalkEnd(0xFE)
    Return()

    # Function_5_158A end

    def Function_6_19B0(): pass

    label("Function_6_19B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_19C1")
    Jump("loc_1DBB")

    label("loc_19C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19CF")
    Jump("loc_1DBB")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_19DD")
    Jump("loc_1DBB")

    label("loc_19DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1A33")

    ChrTalk(
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without Gantz here, work just hasn't\x01",
            "been the same.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A41")
    Jump("loc_1DBB")

    label("loc_1A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B81")

    ChrTalk(
        0xFE,
        (
            "Apparently, Gantz plans on having fun\x01",
            "in the city, gambling the night away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy hits the slots ONCE, and\x01",
            "then he's hooked on the casino for\x01",
            "life. C'mon, Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I don't care if he's having fun\x01",
            "or not. I just wanna know when he'll\x01",
            "pay me back that mira I loaned him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C1C")

    label("loc_1B81")


    ChrTalk(
        0xFE,
        (
            "Gantz got himself hooked on the casino\x01",
            "and almost never makes a profit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I doubt that guy will ever manage to pay\x01",
            "back that mira I loaned him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C1C")

    Jump("loc_1DBB")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD6")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys are that group who helped\x01",
            "out the town...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The Special Support Section, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks, everyone. Gantz and I owe\x01",
            "you big time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D91")

    label("loc_1CD6")


    ChrTalk(
        0xFE,
        (
            "Thanks, everyone. I'm scared to imagine\x01",
            "what would have happened to us if you\x01",
            "hadn't stepped in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Special Support Section, I'll make sure to\x01",
            "raise a glass in your honor tonight!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D91")

    Jump("loc_1DBB")

    label("loc_1D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1DA4")
    Jump("loc_1DBB")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1DB2")
    Jump("loc_1DBB")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DBB")

    label("loc_1DBB")

    TalkEnd(0xFE)
    Return()

    # Function_6_19B0 end

    def Function_7_1DBF(): pass

    label("Function_7_1DBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1DD0")
    Jump("loc_2177")

    label("loc_1DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DDE")
    Jump("loc_2177")

    label("loc_1DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1DEC")
    Jump("loc_2177")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1DFA")
    Jump("loc_2177")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E08")
    Jump("loc_2177")

    label("loc_1E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F02")

    ChrTalk(
        0xFE,
        (
            "During next month's Anniversary Festival, all us\x01",
            "miners are going to get a well-deserved break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's going to be my chance to take back my\x01",
            "mira and win big at the casino!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe... It can't come soon enough.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FCC")

    label("loc_1F02")


    ChrTalk(
        0xFE,
        (
            "During next month's Anniversary Festival, all us\x01",
            "miners are going to get a well-deserved break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we got a few days off, I'm going to party all\x01",
            "night over at the city's casino! Hell yeah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCC")

    Jump("loc_2177")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D0")

    ChrTalk(
        0xFE,
        "Heave...ho...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it! Memories of yesterday's failures\x01",
            "at Barca are pissin' me off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta get back over there as soon as\x01",
            "possible! I wonder if Marlow would lend me\x01",
            "some mira again if I asked nice enough...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_214D")

    label("loc_20D0")


    ChrTalk(
        0xFE,
        "*sigh* Hurry up, weekend...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I may have lost a bunch recently, but I'm gonna\x01",
            "earn every mira back, just you wait...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214D")

    Jump("loc_2177")

    label("loc_2152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2160")
    Jump("loc_2177")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_216E")
    Jump("loc_2177")

    label("loc_216E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2177")

    label("loc_2177")

    TalkEnd(0xFE)
    Return()

    # Function_7_1DBF end

    def Function_8_217B(): pass

    label("Function_8_217B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_230E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227C")

    ChrTalk(
        0xFE,
        (
            "Huh? What about monsters?\x01",
            "Dang, that's unlucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, well, can't win 'em all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You recovered the book, so everything's\x01",
            "good to go, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(He's acting like he has nothing to do with this...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_230A")

    label("loc_227C")


    ChrTalk(
        0xFE,
        (
            "I can't believe you actually ran across monsters.\x01",
            "That's pretty unlucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You recovered the book, so everything's\x01",
            "good to go, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230A")

    TalkEnd(0xFE)
    Return()

    label("loc_230E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242E")

    ChrTalk(
        0xFE,
        (
            "I accidentally left the book down\x01",
            "in the mines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, but I'm swamped with work\x01",
            "right now. Mind heading down there\x01",
            "and grabbing it for me? Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pretty deep into the mine, but if you\x01",
            "take the stairs down, it shouldn't be too\x01",
            "hard to find.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_242E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_244B")
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    label("loc_244B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2522")

    ChrTalk(
        0xFE,
        "Gaaaaaaantz... Come baaaaack...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wasn't the mayor going to bring him\x01",
            "back from the city? Where are they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, no. Don't tell me Gantz dragged Mayor\x01",
            "Bickson into his gambling addiction...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C0")

    label("loc_2522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_25C2")

    ChrTalk(
        0xFE,
        (
            "Ow, owwww... I'm so sore from work\x01",
            "yesterday. Slacking off recently was\x01",
            "a bad idea, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Damn, all I can do is get back in shape!\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C0")

    label("loc_25C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_25D0")
    Jump("loc_26C0")

    label("loc_25D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2632")

    ChrTalk(
        0xFE,
        (
            "Since Gantz is who knows where,\x01",
            "I can't slack off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come back, you jerk.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C0")

    label("loc_2632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_267F")

    ChrTalk(
        0xFE,
        (
            "There's no time to be lazy 'cause\x01",
            "the crew is down a man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C0")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_268D")
    Jump("loc_26C0")

    label("loc_268D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_269B")
    Jump("loc_26C0")

    label("loc_269B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_26A9")
    Jump("loc_26C0")

    label("loc_26A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_26B7")
    Jump("loc_26C0")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26C0")

    label("loc_26C0")

    TalkEnd(0xFE)
    Return()

    # Function_8_217B end

    def Function_9_26C4(): pass

    label("Function_9_26C4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_2744")
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
    SetScenarioFlags(0x114, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_27A9")

    label("loc_2744")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_27A9")

    Jump("loc_280B")

    label("loc_27AE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is where I would put my item...\x01",
            "IF I HAD ONE!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_280B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_26C4 end

    def Function_10_2817(): pass

    label("Function_10_2817")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2901")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_2897")
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
    SetScenarioFlags(0x114, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_28FC")

    label("loc_2897")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_28FC")

    Jump("loc_297F")

    label("loc_2901")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The real treasure is buried underneath, but\x01",
            "you'll never be able to move me! NEVER!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_297F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2817 end

    def Function_11_298B(): pass

    label("Function_11_298B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A75")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_2A0B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_2A70")

    label("loc_2A0B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
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

    label("loc_2A70")

    Jump("loc_2AE7")

    label("loc_2A75")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Keep up the good work, and you're bound to be\x01",
            "a Mainz-stay around here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2AE7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_298B end

    def Function_12_2AF3(): pass

    label("Function_12_2AF3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDD")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x65, 1)"), scpexpr(EXPR_END)), "loc_2B73")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_2BD8")

    label("loc_2B73")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
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

    label("loc_2BD8")

    Jump("loc_2C6F")

    label("loc_2BDD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah HA! I'm actually an undercover chest\x01",
            "working for the Chest Police Department.\x01",
            "You're busted, buster!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_2C6F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_2AF3 end

    def Function_13_2C7B(): pass

    label("Function_13_2C7B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-19490, 1000, 21500, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20050, 0)
    SetChrPos(0x101, -20700, 50, 20900, 90)
    SetChrPos(0x102, -20700, 50, 22100, 90)
    SetChrPos(0x103, -21900, 50, 20900, 90)
    SetChrPos(0x104, -21900, 50, 22100, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D2F")
    SetChrPos(0x109, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_2D5A")

    label("loc_2D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D5A")
    SetChrPos(0x10A, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2D5A")

    OP_0D()

    ChrTalk(
        0x101,
        "#6P#0000FExcuse us. Are you Logy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PHuh? Yeah, who're you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FSpecial Support Section. You see, we had\x01",
            "a request from the library today...\x02\x03",
            "Logy, do you have a book checked out\x01",
            "from the library?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POhhh, it's about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PYeah, I still got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FAccording to the librarian, it is a few days\x01",
            "past its return date. Why did you not return\x01",
            "it on time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAh, 'cause going all the way into\x01",
            "the city is a pain.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FAF")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2FAF")

    Sleep(1000)

    ChrTalk(
        0x104,
        "#6P#0306F(Straight to the point, eh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWell, since you came all the way out here,\x01",
            "you might as well take it back for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI was actually finishing it up during my\x01",
            "break, just a little while ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0x102,
        "#5P#0105FIs something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI, uh, forgot to take it with me. So it's\x01",
            "down at the bottom of the mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A6")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_31A6")

    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#11PSorry, but I'm swamped with work\x01",
            "right now. Mind heading down there\x01",
            "and grabbing it for me? Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt's pretty deep into the mine, but if you\x01",
            "take the stairs down, it shouldn't be too\x01",
            "hard to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0206FDoes your laziness know no bounds...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3326")

    ChrTalk(
        0x109,
        (
            "#12P#0503FHe could give the CGF commander a run for\x01",
            "his money in terms of laziness...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3349")

    label("loc_3326")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3349")

    ChrTalk(
        0x10A,
        "#12P#0603F...\x02",
    )

    CloseMessageWindow()

    label("loc_3349")


    ChrTalk(
        0x101,
        (
            "#6P#0006FWell, it's not like it's a huge deal.\x01",
            "Let's go find it, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_END)), "loc_341E")

    ChrTalk(
        0xC,
        (
            "#11POh, by the way, don't try going into\x01",
            "the abandoned mine over to the left.\x01",
            "I didn't leave it in there, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_341E")


    ChrTalk(
        0xC,
        (
            "#11PYeah, the book isn't in the abandoned mine.\x01",
            "The gate is closed, so hopefully you could've\x01",
            "pieced that together yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A0")


    ChrTalk(
        0x101,
        "#6P#0001FR-Right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34DE")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_34DE")

    SetChrPos(0x0, -20750, 50, 20860, 90)
    OP_93(0xC, 0x5A, 0x0)
    OP_66(0x5, 0x1)
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 117500, -8750, -15770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_29(0x28, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_2C7B end

    def Function_14_354F(): pass

    label("Function_14_354F")

    TalkBegin(0xFF)
    StopEffect(0x9, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D9, 1)
    EventBegin(0x0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35DA")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_35F0")

    label("loc_35DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35F0")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_35F0")

    Fade(500)
    OP_68(116640, -7650, -15740, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19950, 0)
    SetChrPos(0x101, 115910, -8950, -14740, 135)
    SetChrPos(0x102, 117900, -8950, -14060, 180)
    SetChrPos(0x103, 118710, -8950, -15820, 270)
    SetChrPos(0x104, 116830, -8950, -17480, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36B0")
    SetChrPos(0x109, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_36DB")

    label("loc_36B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36DB")
    SetChrPos(0x10A, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_36DB")

    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0000FOh, finally found it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105FJudging by the title, this is no book\x01",
            "I'd want to read...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FA book that records strange phenomena\x01",
            "that have occurred in Crossbell State...\x02\x03",
            "#0203FDespite what the title says, it does not seem\x01",
            "as if the book confirms whether these events\x01",
            "actually happened or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FY'know, I could see myself readin'\x01",
            "somethin' like this to pass the time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_392C")

    ChrTalk(
        0x109,
        (
            "#6P#0500FI know similar things have been investigated\x01",
            "by the Guardian Force, but...\x02\x03",
            "I don't think any of that spooky stuff was\x01",
            "ever formally substantiated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_392C")


    ChrTalk(
        0x102,
        "#5P#0103F(I won't be reading it, that's for sure...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FWell, now that we successfully retrieved\x01",
            "the book, we should--\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39FB")
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        "#6P#0605FHey...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x13B, 0x1F4)

    label("loc_39FB")

    StopBGM(0xBB8)
    Sleep(200)
    Sound(835, 0, 100, 0)
    Sleep(700)
    BeginChrThread(0xD, 3, 0, 16)
    BeginChrThread(0xE, 3, 0, 16)
    BeginChrThread(0xF, 3, 0, 16)
    BeginChrThread(0x10, 3, 0, 16)
    BeginChrThread(0x11, 3, 0, 16)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_3A8F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A8F)

    def lambda_3A9C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A9C)

    def lambda_3AA9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AA9)

    def lambda_3AB6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AB6)
    OP_68(115510, -8000, -13560, 4000)
    MoveCamera(16, 17, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(20790, 4000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B21")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_3B19():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B19)

    label("loc_3B21")

    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)

    ChrTalk(
        0x101,
        "#12P#0005FMonsters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FTch, they've blocked our exit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0201FHere they come!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BF7")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_3C0F")

    label("loc_3BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C0F")
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_3C0F")

    OP_0D()
    Battle("BattleInfo_1DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    Return()

    # Function_14_354F end

    def Function_15_3C2E(): pass

    label("Function_15_3C2E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    StopEffect(0x9, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C90")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_3CA6")

    label("loc_3C90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CA6")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_3CA6")

    OP_68(115910, -8000, -14990, 0)
    MoveCamera(12, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21830, 0)
    SetChrPos(0x101, 115910, -8950, -14740, 315)
    SetChrPos(0x102, 117900, -8950, -14060, 315)
    SetChrPos(0x103, 118710, -8950, -15820, 315)
    SetChrPos(0x104, 116830, -8950, -17480, 315)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D70")
    SetChrPos(0x109, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_3DA3")

    label("loc_3D70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DA3")
    SetChrPos(0x10A, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_3DA3")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0006FPhew. They came out of nowhere.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E2A")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_3E42")

    label("loc_3E2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E42")
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    label("loc_3E42")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EAD")

    ChrTalk(
        0x10A,
        "#6P#0603FAre you idiots always this reckless?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0012FHaha. Sorry about that.\x02",
    )

    CloseMessageWindow()

    label("loc_3EAD")


    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, they weren't much of a\x01",
            "threat for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FMonsters always loiter along the path.\x01",
            "This was simply a case of bad timing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FGood thing the book wasn't scratched\x01",
            "up during the fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FRight. Let's head to the exit, everyone.\x02",
    )

    CloseMessageWindow()
    OP_29(0x28, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FEE")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_3FEE")

    SetChrPos(0x0, 115910, -8950, -14740, 315)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_401A")
    OP_D5(0x22)
    Jump("loc_402C")

    label("loc_401A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_402C")
    OP_D5(0x22)

    label("loc_402C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_404B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_4065")

    label("loc_404B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4065")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4065")

    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_15_3C2E end

    def Function_16_4077(): pass

    label("Function_16_4077")


    def lambda_407C():
        OP_98(0xFE, 0xFA0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_407C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_4077 end

    def Function_17_4096(): pass

    label("Function_17_4096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_416A")
    TalkBegin(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Use Abandoned Mine Key]\x01",      # 0
            "[Cancel]\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4162")
    Fade(500)
    SetMapObjFrame(0xFF, "key00", 0x0, 0x1)
    OP_0D()
    Sound(809, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The abandoned mine gate was opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4151")
    OP_29(0x1C, 0x1, 0x2)

    label("loc_4151")

    SetScenarioFlags(0xBF, 4)
    SetMapObjFlags(0x15, 0x10)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_4162")

    TalkEnd(0xFF)
    Jump("loc_41D1")

    label("loc_416A")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate leading to the abandoned mine\x01",
            "is locked up tight with a sturdy chain.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_41D1")

    Return()

    # Function_17_4096 end

    SaveToFile()

Try(main)
