from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3021.bin",                # FileName
        "m3021",                    # MapName
        "m3021",                    # Location
        0x007D,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 2200, 238000, 0, 0, 1, 125, 0, 4, 0, 5],
    )

    BuildStringList((
        "m3021",                  # 0
        "Miner Gantz",            # 1
        "Citizen",                # 2
        "Citizen",                # 3
        "Dino",                   # 4
        "Nikolai",                # 5
        "Bond",                   # 6
        "Trader Rizero",          # 7
        "Engineer",               # 8
        "Ernest",                 # 9
        "Demon Ernest",           # 10
        "Pterosaur",              # 11
        "Pterosaur",              # 12
        "シームーン	",            # 13
        "SE制御",                 # 14
        "bm3090",                 # 15
        "bm3081",                 # 16
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_114", 0x0010, 40, 6, 60, 0, 1, 0, 0, "bm3081", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_158", 0x0042, 40, 6, 60, 0, 0, 0, 0, "bm3090", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67400.dat", "ms70000.dat", "ms70000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7405", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch37600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch06800.itc",                   # 03
        "chr/ch28900.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch27700.itc",                   # 06
        "apl/ch50523.itc",                   # 07
        "chr/ch26000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch68450.itc",               # 10
        "monster/ch68450.itc",               # 11
    ))

    DeclNpc(4500,    0,       235300,  270,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5800,    0,       236199,  270,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(5800,    0,       234399,  270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4610,    0,       188539,  270,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4500,    0,       223899,  270,  261,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4949,    0,       187440,  270,  261,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4500,    0,       176000,  270,  261,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5800,    0,       175100,  270,  261,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    277,  0x0, 0,   7,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28500,   -46500,  26250,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(2300,    0,       206000,  1500,    2300,    2000,    206000,  0x007C, 0,  22, 0x0000)
    DeclActor(2300,    0,       194000,  1500,    2300,    2000,    194000,  0x007C, 0,  23, 0x0000)
    DeclActor(28500,   -48000,  26250,   1200,    28500,   -47000,  26250,   0x007C, 0,  6,  0x0000)
    DeclActor(0,       -240000, 31400,   1200,    0,       -239000, 31400,   0x007C, 0,  7,  0x0000)
    DeclActor(10500,   0,       214750,  1200,    10500,   1000,    214750,  0x007C, 0,  8,  0x0000)
    DeclActor(22250,   -66000,  30000,   1200,    22250,   -65000,  30000,   0x007C, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_4D4",          # 00, 0
        "Function_1_58C",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_5C5",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_6F5",          # 05, 5
        "Function_6_86A",          # 06, 6
        "Function_7_AE4",          # 07, 7
        "Function_8_C46",          # 08, 8
        "Function_9_DEA",          # 09, 9
        "Function_10_F7A",         # 0A, 10
        "Function_11_11AA",        # 0B, 11
        "Function_12_13C6",        # 0C, 12
        "Function_13_1583",        # 0D, 13
        "Function_14_1712",        # 0E, 14
        "Function_15_186F",        # 0F, 15
        "Function_16_1A35",        # 10, 16
        "Function_17_1E05",        # 11, 17
        "Function_18_22BE",        # 12, 18
        "Function_19_2329",        # 13, 19
        "Function_20_2398",        # 14, 20
        "Function_21_23CD",        # 15, 21
        "Function_22_2B5C",        # 16, 22
        "Function_23_2C9B",        # 17, 23
        "Function_24_2DDA",        # 18, 24
        "Function_25_34D8",        # 19, 25
        "Function_26_4938",        # 1A, 26
        "Function_27_4998",        # 1B, 27
        "Function_28_49F8",        # 1C, 28
        "Function_29_5303",        # 1D, 29
        "Function_30_5320",        # 1E, 30
        "Function_31_5353",        # 1F, 31
        "Function_32_5386",        # 20, 32
        "Function_33_53B9",        # 21, 33
        "Function_34_53EC",        # 22, 34
        "Function_35_5467",        # 23, 35
    ))


    def Function_0_4D4(): pass

    label("Function_0_4D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_514"),
        (1, "loc_520"),
        (2, "loc_52C"),
        (3, "loc_538"),
        (4, "loc_544"),
        (5, "loc_550"),
        (6, "loc_55C"),
        (SWITCH_DEFAULT, "loc_568"),
    )


    label("loc_514")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_520")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_52C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_538")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_544")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_550")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_55C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_568")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_574")

    label("loc_58B")

    Return()

    # Function_0_4D4 end

    def Function_1_58C(): pass

    label("Function_1_58C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A7")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_58C")

    label("loc_5A7")

    Return()

    # Function_1_58C end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C4")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_5A8")

    label("loc_5C4")

    Return()

    # Function_2_5A8 end

    def Function_3_5C5(): pass

    label("Function_3_5C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_5C5")

    label("loc_5E1")

    Return()

    # Function_3_5C5 end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F8")
    Event(0, 21)
    Jump("loc_612")

    label("loc_5F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_612")
    Event(0, 25)

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_END)), "loc_62C")
    SetChrPos(0x10, 32500, -66000, 2000, 180)

    label("loc_62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E5")
    SetChrPos(0x8, 980, 0, 204950, 225)
    SetChrPos(0x9, 2390, 0, 196530, 225)
    SetChrPos(0xA, 740, 0, 195430, 45)
    SetChrPos(0xB, -5420, 0, 196800, 0)
    SetChrPos(0xC, -3950, 0, 202880, 180)
    SetChrPos(0xD, 3840, 0, 201430, 270)
    SetChrPos(0xE, 7860, 0, 177060, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_6CF")
    SetChrPos(0xF, 8560, 0, 175050, 270)
    Jump("loc_6E0")

    label("loc_6CF")

    SetChrPos(0xF, 8560, 0, 175050, 135)

    label("loc_6E0")

    SetChrFlags(0xA, 0x10)

    label("loc_6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_6F4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_6F4")

    Return()

    # Function_4_5E2 end

    def Function_5_6F5(): pass

    label("Function_5_6F5")

    ClearMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xB, 0x10)
    ClearMapObjFlags(0xC, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0xE, 0x10)
    ClearMapObjFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_END)), "loc_736")
    OP_65(0x0, 0x1)
    OP_70(0x10, 0x1E)
    OP_70(0xA, 0x32)
    OP_70(0xB, 0x32)
    OP_70(0xC, 0x32)

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_END)), "loc_753")
    OP_65(0x1, 0x1)
    OP_70(0x11, 0x1E)
    OP_70(0xD, 0x32)
    OP_70(0xE, 0x32)
    OP_70(0xF, 0x32)

    label("loc_753")

    ClearMapObjFlags(0x13, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_76B")
    OP_70(0x13, 0x1E)
    Jump("loc_76F")

    label("loc_76B")

    OP_70(0x13, 0x0)

    label("loc_76F")

    ClearMapObjFlags(0x14, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 5)), scpexpr(EXPR_END)), "loc_787")
    OP_70(0x14, 0x1E)
    Jump("loc_78B")

    label("loc_787")

    OP_70(0x14, 0x0)

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_798")
    OP_70(0x19, 0x1)

    label("loc_798")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CD")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_7D2")

    label("loc_7CD")

    ClearMapFlags(0x2000)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5")
    OP_70(0x0, 0x0)
    Jump("loc_7E9")

    label("loc_7E5")

    OP_70(0x0, 0x1E)

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC")
    OP_70(0x1, 0x0)
    Jump("loc_800")

    label("loc_7FC")

    OP_70(0x1, 0x1E)

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_813")
    OP_70(0x12, 0x0)
    Jump("loc_817")

    label("loc_813")

    OP_70(0x12, 0x1E)

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A")
    OP_70(0x18, 0x0)
    Jump("loc_82E")

    label("loc_82A")

    OP_70(0x18, 0x1E)

    label("loc_82E")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_869")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    OP_1B(0x2, 0x0, 0x20)
    OP_1B(0x3, 0x0, 0x21)

    label("loc_869")

    Return()

    # Function_5_6F5 end

    def Function_6_86A(): pass

    label("Function_6_86A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A29")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_969")
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x14, 0x0, 0)
    OP_98(0x14, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_8C3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8C3)

    def lambda_8DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8DD)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x14, 1)
    Battle("BattleInfo_114", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_94A"),
        (2, "loc_959"),
        (1, "loc_966"),
        (SWITCH_DEFAULT, "loc_969"),
    )


    label("loc_94A")

    SetScenarioFlags(0x76, 7)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_969")

    label("loc_959")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_966")

    OP_B7(0x0)
    Return()

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41B, 1)"), scpexpr(EXPR_END)), "loc_9C1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x41B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x109, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_A24")

    label("loc_9C1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x41B),
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

    label("loc_A24")

    Jump("loc_AD8")

    label("loc_A29")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Chief Roberts has been pulling strings to have\x01",
            "Crossbell rename the Geofront the 'Tiofront'.\x01",
            "Would the dev team have to change their name, too?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_AD8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_86A end

    def Function_7_AE4(): pass

    label("Function_7_AE4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x47, 1)"), scpexpr(EXPR_END)), "loc_B64")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_BC9")

    label("loc_B64")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x47),
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

    label("loc_BC9")

    Jump("loc_C3A")

    label("loc_BCE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You're going to love the sequel.\x01",
            "It's called Trails to ZX Advent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C3A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AE4 end

    def Function_8_C46(): pass

    label("Function_8_C46")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D81")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
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
    SetScenarioFlags(0x10D, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_DD8")

    label("loc_D81")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Someone stored Gnosis inside me and\x01",
            "next thing I knew, I was in this cell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_DD8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C46 end

    def Function_9_DEA(): pass

    label("Function_9_DEA")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED4")
    Sound(14, 0, 100, 0)
    OP_71(0x18, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x49, 1)"), scpexpr(EXPR_END)), "loc_E6A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x49),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_ECF")

    label("loc_E6A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x49),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x18, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ECF")

    Jump("loc_F6E")

    label("loc_ED4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As you gaze at the empty chest, you convince yourself\x01",
            "that your friends are the only treasure you'll ever need.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F6E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_DEA end

    def Function_10_F7A(): pass

    label("Function_10_F7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1007")

    ChrTalk(
        0xFE,
        "I just want to get back to Mainz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Listen, I just have one more request!\x01",
            "Get us outta here, please!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1146")

    label("loc_1007")


    ChrTalk(
        0xFE,
        (
            "Y-You guys, help will be here\x01",
            "soon, won't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I'm so sorry... I regret every second\x01",
            "of how I acted this past month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you take that drug, it's like you're\x01",
            "capable of anything...\x01",
            "Not to mention, you get a massive ego...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hate myself for causing so much\x01",
            "trouble for good ol' Mayor Bickson...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1146")

    Jump("loc_11A6")

    label("loc_114B")


    ChrTalk(
        0xFE,
        (
            "W-We're saved! Does this mean\x01",
            "we can go home now?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, hurry and save us!\x02",
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_11A6")

    TalkEnd(0xFE)
    Return()

    # Function_10_F7A end

    def Function_11_11AA(): pass

    label("Function_11_11AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1251")

    ChrTalk(
        0xFE,
        (
            "I was desperate, and I turned to that\x01",
            "blasted drug for help.\x01",
            "I know I'm an awful person, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to protect this girl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_136A")

    label("loc_1251")


    ChrTalk(
        0xFE,
        (
            "From what I've heard, she has no\x01",
            "recollection of taking the drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And apparently, she was on medicine prescribed\x01",
            "to her by the doctors at St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, I decided I would protect her.\x01",
            "In a place as hopeless as this, you need\x01",
            "someone to be there for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_136A")

    Jump("loc_13C2")

    label("loc_136F")


    ChrTalk(
        0xFE,
        (
            "Thank goodness... We're finally free.\x01",
            "And we can go back to the city soon!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_13C2")

    TalkEnd(0xFE)
    Return()

    # Function_11_11AA end

    def Function_12_13C6(): pass

    label("Function_12_13C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1462")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "This guy is being so kind to\x01",
            "a stranger like myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did I have to end up in\x01",
            "a place like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x0)
    Jump("loc_1532")

    label("loc_1462")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        (
            "D-Don't worry. If we believe hard\x01",
            "enough, help will definitely come...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Until then, we should all stay together.\x01",
            "This is probably the safest place to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Y-Yeah, you might be right.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_1532")

    Jump("loc_157F")

    label("loc_1537")


    ChrTalk(
        0xFE,
        (
            "W-We believed! And help arrived...!\x01",
            "Please, get us out of here!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_157F")

    TalkEnd(0xFE)
    Return()

    # Function_12_13C6 end

    def Function_13_1583(): pass

    label("Function_13_1583")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_161B")

    ChrTalk(
        0xFE,
        "Will they forgive me...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wald, Koki, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I just want to see and laugh\x01",
            "with all the Vipers again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B7")

    label("loc_161B")


    ChrTalk(
        0xFE,
        "Wald, I'm so sorry...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I...I just wanted to be strong like you.\x01",
            "But strength like that doesn't come easy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaahhh...!\x01",
            "Please forgive me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_16B7")

    Jump("loc_170E")

    label("loc_16BC")


    ChrTalk(
        0xFE,
        (
            "H-Hell yes! You guys are my heroes!\x01",
            "Crossbell City, I'll see you soon...!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 19)

    label("loc_170E")

    TalkEnd(0xFE)
    Return()

    # Function_13_1583 end

    def Function_14_1712(): pass

    label("Function_14_1712")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_182B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_177A")

    ChrTalk(
        0xFE,
        (
            "The troupe leader... Miss Ilya...\x01",
            "H-How can I ever face them again?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1826")

    label("loc_177A")


    ChrTalk(
        0xFE,
        "Oooh, my life is over!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I thought about being saved,\x01",
            "depression hit me like a tidal wave...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why did I turn to something as\x01",
            "nasty as that drug... Why?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1826")

    Jump("loc_186B")

    label("loc_182B")


    ChrTalk(
        0xFE,
        (
            "Th-This must be Aidios' will...\x01",
            "Everyone, we're saved!!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_186B")

    TalkEnd(0xFE)
    Return()

    # Function_14_1712 end

    def Function_15_186F(): pass

    label("Function_15_186F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_18DA")

    ChrTalk(
        0xFE,
        "Why am I here...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My family...! Creil, Sunita!\x01",
            "Are they safe...?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B0")

    label("loc_18DA")


    ChrTalk(
        0xFE,
        (
            "My memories of arriving here are fuzzy.\x01",
            "All I know is, before I even realized what\x01",
            "was happening, I was in that cell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just where the heck am I...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And my family... Are Creil and Sunita all right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_19B0")

    Jump("loc_1A31")

    label("loc_19B5")


    ChrTalk(
        0xFE,
        "You've come to help us...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, we can finally leave this Goddess-forsaken\x01",
            "place? Thank you! Thank you so much!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1A31")

    TalkEnd(0xFE)
    Return()

    # Function_15_186F end

    def Function_16_1A35(): pass

    label("Function_16_1A35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 2)), scpexpr(EXPR_END)), "loc_1C4D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C48")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B3F")

    ChrTalk(
        0xFE,
        (
            "Right now, I just want to leave\x01",
            "this place with my limbs intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to do that, you have my\x01",
            "full support, I assure you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEB")

    label("loc_1B3F")


    ChrTalk(
        0xFE,
        "I was too weak...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After suffering a heavy loss in my\x01",
            "investments, I just prayed for a way\x01",
            "to recover everything in one go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But the price was too great...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1BEB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C43")

    label("loc_1BFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1D")
    OP_60(0x0)
    OP_AF(0xBE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C43")

    label("loc_1C1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C43")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C43")

    Jump("loc_1A58")

    label("loc_1C48")

    Jump("loc_1D65")

    label("loc_1C4D")


    ChrTalk(
        0xFE,
        (
            "Thank you for releasing me from this\x01",
            "cell. I think I've finally gathered all of\x01",
            "my thoughts now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right... I have supplies on hand,\x01",
            "believe it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you ever need something while\x01",
            "exploring, give me a shout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, you can\x01",
            "count on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 2)

    label("loc_1D65")

    Jump("loc_1E01")

    label("loc_1D6A")


    ChrTalk(
        0xFE,
        (
            "I still can't believe someone came...\x01",
            "This has got to be Aidios' will!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, help us return to the surface\x01",
            "as soon as humanly possible!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1E01")

    TalkEnd(0xFE)
    Return()

    # Function_16_1A35 end

    def Function_17_1E05(): pass

    label("Function_17_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_20B9")
    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B1")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Upgrade/Synthesize\x01",      # 1
            "Leave\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAD")
    OP_C7(0x1, 0x80)
    OP_AF(0xBF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20AC")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC1")
    Jump("loc_20AC")

    label("loc_1EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(
        0xFE,
        (
            "In an ugly place like this, you never know\x01",
            "when you may need to tune your orbments.\x01",
            "When the time comes, give me a shout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You guys have my full support!\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AC")

    label("loc_1F8B")


    ChrTalk(
        0xFE,
        (
            "I was actually on my way to the Republic\x01",
            "when I was mugged and dragged here\x01",
            "by a swarm of black-suited men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess traveling on the highway\x01",
            "at night wasn't the best idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me, I want to get out of this\x01",
            "place as much as everyone else.\x01",
            "If you need help, let me know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_20AC")

    Jump("loc_1E28")

    label("loc_20B1")

    TalkEnd(0xFE)
    Jump("loc_221F")

    label("loc_20B9")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x87, 0x0)
    OP_70(0x19, 0x1)
    Sound(72, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Whew, that was a close call. I'd be\x01",
            "screwed if this was broken...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "You see, I work as an orbal engineer,\x01",
            "specializing in orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, my equipment made it\x01",
            "through the mugging intact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh, if you need your orbments tinkered\x01",
            "with, just let me know. I'll do what I can\x01",
            "to get them up to par.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 3)
    TalkEnd(0xFE)
    OP_93(0xFE, 0x10E, 0x0)

    label("loc_221F")

    Jump("loc_22BD")

    label("loc_2224")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh* I was getting pretty worried\x01",
            "for a second there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think that the police would rescue us...\x01",
            "Man, who would have guessed that?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    TalkEnd(0xFE)

    label("loc_22BD")

    Return()

    # Function_17_1E05 end

    def Function_18_22BE(): pass

    label("Function_18_22BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2328")

    ChrTalk(
        0x101,
        (
            "#0006FPlease try to remain calm.\x01",
            "We'll explain everything once\x01",
            "we open the other cells.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_2328")

    Return()

    # Function_18_22BE end

    def Function_19_2329(): pass

    label("Function_19_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2397")

    ChrTalk(
        0x101,
        (
            "#0006FPlease try to remain calm.\x01",
            "We'll explain everything once\x01",
            "we get the other cells open.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_2397")

    Return()

    # Function_19_2329 end

    def Function_20_2398(): pass

    label("Function_20_2398")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ernest is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_20_2398 end

    def Function_21_23CD(): pass

    label("Function_21_23CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 238100, 0)
    MoveCamera(55, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24750, 0)
    SetChrPos(0x101, 600, 0, 237500, 180)
    SetChrPos(0x102, -600, 0, 237500, 180)
    SetChrPos(0x103, -600, 0, 238800, 180)
    SetChrPos(0x104, 600, 0, 238800, 180)
    SetChrPos(0x107, 0, 0, 240100, 180)
    SetChrPos(0x108, 0, 0, 241400, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 4500, 0, 235300, 90)
    SetChrPos(0x9, 5800, 0, 236200, 180)
    SetChrPos(0xA, 5800, 0, 234400, 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_2553():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2553)

    def lambda_2560():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2560)
    Sleep(50)

    def lambda_2570():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2570)

    def lambda_257D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_257D)
    Sleep(50)

    def lambda_258D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_258D)

    def lambda_259A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_259A)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5300280V#5P#0011FLook!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300281V#5P#0205FCould these be our missing persons?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x19, 0x1000)
    Fade(500)
    OP_68(5000, 1100, 176000, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(5000, 1100, 188000, 4000)
    OP_6F(0x1)
    Fade(500)
    OP_68(5000, 900, 223900, 0)
    MoveCamera(70, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(5000, 900, 235300, 4000)
    OP_6F(0x1)
    ClearMapObjFlags(0x19, 0x1000)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x13B, 0x1F4)

    ChrTalk(
        0x8,
        "#5300282V#11PY-You guys! You came for us!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(3500, 900, 235300, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 1900, 0, 234700, 90)
    SetChrPos(0x102, 1900, 0, 235900, 90)
    SetChrPos(0x103, 600, 0, 234700, 90)
    SetChrPos(0x104, 600, 0, 235900, 90)
    SetChrPos(0x107, 1000, 0, 233000, 45)
    SetChrPos(0x108, 1000, 0, 232000, 45)
    SetChrPos(0x8, 4000, 0, 235300, 270)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 5800, 0, 236200, 270)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 5800, 0, 234400, 270)
    Sleep(500)
    SetCameraDistance(22500, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5300283V#6P#0002FGantz...? Thank goodness you're all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300284V#11POh, my police buddies! Did you come to\x01",
            "rescue us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5300285V#11PN-No way! Help actually came...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5300286V#11PHey! Can we get out of here now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300287V#6P#0008FAbout that...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#5300288V#0101F#5PLet's just open all of the cells first, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_93(0x108, 0xB4, 0x1F4)

    ChrTalk(
        0x108,
        (
            "#5300289V#5P#0901FI think that lever over there should\x01",
            "control the cell doors.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2700, 1700, 206000, 3000)
    MoveCamera(50, 25, 0, 3000)
    SetCameraDistance(20000, 3000)

    def lambda_29C8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_29C8)
    Sleep(50)

    def lambda_29D8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29D8)
    Sleep(50)

    def lambda_29E8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29E8)
    Sleep(50)

    def lambda_29F8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29F8)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x107,
        (
            "#5300290V#0801FI see another at the opposite end of\x01",
            "the room! Let's bust these people out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300291V#0001FRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 2250, 235300, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 0, 0, 235300, 90)
    SetChrPos(0x1, 0, 0, 235300, 90)
    SetChrPos(0x2, 0, 0, 235300, 90)
    SetChrPos(0x3, 0, 0, 235300, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 4500, 0, 235300, 270)
    SetChrPos(0x9, 5800, 0, 236200, 270)
    SetChrPos(0xA, 5800, 0, 234400, 270)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xE5, 6)
    OP_29(0x4F, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_21_23CD end

    def Function_22_2B5C(): pass

    label("Function_22_2B5C")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sturdy-looking lever.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pull it\x01",      # 0
            "Don't\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BD5"),
        (1, "loc_2C93"),
        (SWITCH_DEFAULT, "loc_2C98"),
    )


    label("loc_2BD5")

    Sound(143, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x10)
    Fade(250)
    OP_68(2500, 2300, 208500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    OP_68(2500, 2300, 218500, 3000)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xA, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xB, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xC, 0x0, 0x32, 0x0, 0x0)
    OP_79(0xA)
    OP_79(0xB)
    OP_79(0xC)
    OP_24(0x9B)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xE5, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C8E")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_2C8E")

    Jump("loc_2C98")

    label("loc_2C93")

    Jump("loc_2C98")

    label("loc_2C98")

    EventEnd(0x1)
    Return()

    # Function_22_2B5C end

    def Function_23_2C9B(): pass

    label("Function_23_2C9B")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sturdy-looking lever.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pull it\x01",      # 0
            "Don't\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D14"),
        (1, "loc_2DD2"),
        (SWITCH_DEFAULT, "loc_2DD7"),
    )


    label("loc_2D14")

    Sound(143, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x11)
    Fade(250)
    OP_68(2500, 2300, 191500, 0)
    MoveCamera(135, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    OP_68(2500, 2300, 181500, 3000)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xD, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xE, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xF, 0x0, 0x32, 0x0, 0x0)
    OP_79(0xD)
    OP_79(0xE)
    OP_79(0xF)
    OP_24(0x9B)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xE6, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DCD")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_2DCD")

    Jump("loc_2DD7")

    label("loc_2DD2")

    Jump("loc_2DD7")

    label("loc_2DD7")

    EventEnd(0x1)
    Return()

    # Function_23_2C9B end

    def Function_24_2DDA(): pass

    label("Function_24_2DDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-500, 900, 200000, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -2000, 0, 200600, 90)
    SetChrPos(0x102, -2000, 0, 199400, 90)
    SetChrPos(0x103, -3200, 0, 201400, 90)
    SetChrPos(0x104, -3200, 0, 198600, 90)
    SetChrPos(0x107, -4000, 0, 200600, 90)
    SetChrPos(0x108, -4000, 0, 199400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x8, 500, 0, 200000, 270)
    SetChrPos(0xB, 1100, 0, 198900, 270)
    SetChrPos(0xC, 1300, 0, 202500, 225)
    SetChrPos(0xD, 2300, 0, 201200, 270)
    SetChrPos(0xE, 1500, 0, 197500, 315)
    SetChrPos(0x9, -1500, 0, 203100, 225)
    SetChrPos(0xA, -200, 0, 203700, 225)
    SetChrPos(0xF, -1000, 0, 196900, 315)
    Sleep(500)
    SetCameraDistance(24500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        "#5300292VS-So we can't leave yet?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300293V#6P#0006FI'm sorry, Gantz. So far, we've avoided detection\x01",
            "during our infiltration of this place, but it's not\x01",
            "that simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300294V#12P#0303FNasty monsters and those brainwashed\x01",
            "mafiosos are crawling all over the place...\x02\x03",
            "#5300295V#0301FThere ain't a safe haven anywhere. Not\x01",
            "in these ruins and not in the city, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300296V#6P#0201FThe safest option is for you all to remain\x01",
            "here until help arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5300297V#11PA-Are you kidding me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300298V#5P*sigh* Just my luck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300299V#12P#0104FThe Guardian Force will be dispatched here\x01",
            "as soon as the chaos in the city is quelled.\x02\x03",
            "#5300300V#0100FPlease, we need you to endure this just a\x01",
            "little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300301V#0901F#12PThe Bracer Guild won't rest until this\x01",
            "entire incident is resolved. Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300302V#0800F#6PDon't worry, everyone! This place might\x01",
            "give you the creeps, but help is on its way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5300303V#5PI-I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5300304V#11PWe'll do everything in our power to\x01",
            "help you out! You deserve it!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1500, 2250, 200000, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, -1500, 0, 200000, 90)
    SetChrPos(0x1, -1500, 0, 200000, 90)
    SetChrPos(0x2, -1500, 0, 200000, 90)
    SetChrPos(0x3, -1500, 0, 200000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 980, 0, 204950, 225)
    SetChrPos(0x9, 2390, 0, 196530, 225)
    SetChrPos(0xA, 740, 0, 195430, 45)
    SetChrPos(0xB, -5420, 0, 196800, 0)
    SetChrPos(0xC, -3950, 0, 202880, 180)
    SetChrPos(0xD, 3840, 0, 201430, 270)
    SetChrPos(0xE, 7860, 0, 177060, 225)
    SetChrPos(0xF, 8560, 0, 175050, 135)
    SetChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0xE6, 1)
    OP_29(0x4F, 0x1, 0x7)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_2DDA end

    def Function_25_34D8(): pass

    label("Function_25_34D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00650.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00750.itc", 0x29)
    LoadChrToIndex("chr/ch02350.itc", 0x2A)
    LoadChrToIndex("monster/ch67450.itc", 0x2B)
    LoadChrToIndex("monster/ch70050.itc", 0x2C)
    LoadChrToIndex("monster/ch70051.itc", 0x2D)
    LoadChrToIndex("chr/ch02357.itc", 0x2E)
    LoadChrToIndex("monster/ch67452.itc", 0x2F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")
    SoundLoad(861)
    OP_68(28500, -65000, -26000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 27900, -66000, -26500, 0)
    SetChrPos(0x102, 29100, -66000, -26500, 0)
    SetChrPos(0x103, 27900, -66000, -27800, 0)
    SetChrPos(0x104, 29100, -66000, -27800, 0)
    SetChrPos(0x107, 31000, -66000, -27200, 0)
    SetChrPos(0x108, 31700, -66000, -27900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 28500, -66000, 3800, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 28500, -66000, 3800, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 42000, -61000, 14800, 120)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x2D)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 15500, -61000, 14800, 240)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(15500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sound(1905, 255, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x10,
        "Young Man's Voice",
        (
            "#5300387V\x07\x02",
            "Heh heh... Here at last.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5300388V\x07\x00",
            "#12P#0010FThat voice...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300389V#0107FErnest!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(28500, -65000, -10000, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 28300, -66000, -18000, 0)
    SetChrPos(0x102, 29400, -66000, -18500, 0)
    SetChrPos(0x103, 27500, -66000, -19500, 0)
    SetChrPos(0x104, 28600, -66000, -20000, 0)
    SetChrPos(0x107, 29600, -66000, -21200, 0)
    SetChrPos(0x108, 29000, -66000, -22400, 0)
    OP_68(28500, -65000, 1000, 4000)
    MoveCamera(43, 15, 0, 4000)
    SetCameraDistance(19000, 4000)

    def lambda_3955():
        OP_96(0xFE, 0x6E8C, 0xFFFEFE30, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3955)
    Sleep(50)

    def lambda_3972():
        OP_96(0xFE, 0x72D8, 0xFFFEFE30, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3972)
    Sleep(50)

    def lambda_398F():
        OP_96(0xFE, 0x6B6C, 0xFFFEFE30, 0xFFFFF63C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_398F)
    Sleep(50)

    def lambda_39AC():
        OP_96(0xFE, 0x6FB8, 0xFFFEFE30, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39AC)
    Sleep(50)

    def lambda_39C9():
        OP_96(0xFE, 0x73A0, 0xFFFEFE30, 0xFFFFEE6C, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_39C9)
    Sleep(50)

    def lambda_39E6():
        OP_96(0xFE, 0x7148, 0xFFFEFE30, 0xFFFFEA84, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_39E6)
    WaitChrThread(0x107, 1)

    def lambda_3A04():
        OP_95(0xFE, 31600, -66000, -1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3A04)
    WaitChrThread(0x108, 1)

    def lambda_3A22():
        OP_95(0xFE, 30900, -66000, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3A22)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_3A50():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3A50)
    WaitChrThread(0x108, 1)

    def lambda_3A61():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3A61)
    WaitChrThread(0x108, 2)
    OP_6F(0x79)

    ChrTalk(
        0x107,
        "#5300390V#0807FAh! I've definitely seen this creep before...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300391V#0901FThe would-be assassin of the mayor,\x01",
            "if the SSS didn't put a stop to him...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1902, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 43, 3)
    Sleep(500)

    AnonymousTalk(
        0x10,
        (
            "#5300393V\x07\x02",
            "Oh, you brought bracers?\x02\x03",
            "#5300394VAnd you cooperated with Yin earlier, too.\x01",
            "You have quite a lot of friends, don't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#5300395V\x07\x00",
            "#12P#0003FYou can cut the quips.\x02\x03",
            "#5300396V#0001FUnlike the mafia and the Guardian Force,\x01",
            "you're completely in control...\x02\x03",
            "#5300397VAiding and abetting willingly is just going\x01",
            "to add more time to your sentence. You\x01",
            "know that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5300398V\x07\x02",
            "#6613FHeh. What crime have I committed?\x01",
            "Laws are merely childish rules created\x01",
            "by mankind to rein in the weak.\x02\x03",
            "#5300399VFrom today onward, Crossbell shall\x01",
            "become a new, glorious holy ground...\x02\x03",
            "#5300400V#6600FKnowing that, why should I bore myself\x01",
            "with petty rules such as your 'laws'...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300401V\x07\x00",
            "#0101FErnest, please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300402V#12P#0211FOur words are useless...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300403V#4P#0306FLeaves us no choice, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300404V#12P#0008FHow you met Guenter, your motive\x01",
            "behind all of this madness...\x02\x03",
            "#5300405V#0003FWe'll find those answers when we\x01",
            "question you, after all of this\x01",
            "is said and done.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetCameraDistance(18500, 500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5300406V#12P#0007FBut for now... Stand aside\x01",
            "and let us pass!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()
    Sleep(500)
    Sound(1899, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#5300407V\x07\x02",
            "#6600FHaha, you wish to pass?! Very well!\x02\x03",
            "#5300408V#6613FMy holy comrade has bestowed upon me\x01",
            "the power to reach Wisdom!\x02\x03",
            "#5300409V#6610FFeast your eyes on the power of Gnosis!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(28500, -65000, 2800, 2000)
    MoveCamera(0, 19, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(16000, 4000)
    Sound(1904, 255, 100, 0)
    Sleep(500)
    OP_6F(0x41)
    PlayEffect(0x0, 0x0, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    StopBGM(0x1388)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x2)

    def lambda_41A3():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41A3)
    Sound(540, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x10, 0x3)
    Sleep(800)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#5300410V#0801F#12P#NTh-This again...?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300411V#0907F#12P#NStay on your toes!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    Sound(1906, 255, 100, 0)
    OP_6F(0x10)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x3)
    SetChrFlags(0x11, 0x800)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    def lambda_4312():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4312)

    def lambda_4323():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4323)
    Sound(202, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(315, 0, 100, 0)
    OP_24(0x35D)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(0, 15, 0, 1000)
    SetCameraDistance(18000, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)

    def lambda_43C3():
        OP_A6(0xFE, 0x0, 0x0, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_43C3)

    ChrTalk(
        0x11,
        (
            "#5300412V\x07\x02",
            "#6P#5S#24A#N#5POooooOOOOOHHHHHHH!\x02",
        )
    )

    SetChrSubChip(0x11, 0x4)
    Sleep(150)
    SetChrSubChip(0x11, 0x5)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    CancelBlur(0)
    EndChrThread(0x10, 0x1)
    ClearChrFlags(0x11, 0x800)

    ChrTalk(
        0x103,
        "#5300413V#0207F#6P#NDemonization...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#5300414V#0310F#12P#NThose mafia dudes were\x01",
            "nothing compared to this...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(300)
    Fade(500)
    OP_68(28500, -60000, 10000, 0)
    MoveCamera(33, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    OP_68(28500, -64500, 1000, 4500)
    MoveCamera(43, 15, 0, 4500)
    SetCameraDistance(18500, 4500)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x12, 3, 0, 26)
    BeginChrThread(0x15, 1, 0, 29)
    Sleep(700)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    BeginChrThread(0x13, 0, 0, 3)
    BeginChrThread(0x13, 3, 0, 27)
    WaitChrThread(0x12, 3)
    SetChrChipByIndex(0x12, 0x2C)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 2)
    WaitChrThread(0x13, 3)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 2)
    OP_6F(0x79)
    Sleep(500)
    SetMessageWindowPos(40, 5, -1, -1)
    Sound(965, 0, 100, 0)

    AnonymousTalk(
        0x11,
        (
            "#5300415V\x07\x02",
            "#5PHEH HEH... WHAT AN EXTRAORDINARY FEELING...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x11,
        (
            "#5300416V\x07\x02",
            "#5PWITH THE POWER OF A DEMON, I HAVE FINALLY\x01",
            "TRANSCENDED HUMANITY...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x11,
        (
            "#5300417V\x07\x02",
            "#5PTHIS IS THE PATH OF WISDOM--GNOSIS!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#5300418V\x07\x00",
            "#0106FErnest! How could you let this happen\x01",
            "to yourself?!\x02\x03",
            "#5300419V#0110FHow much lower must you sink until\x01",
            "you're finally satisfied...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300420V#0806FThis is too sad to watch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300421V#12P#0003FNo matter what form you may take...\x01",
            "No matter what wisdom you claim to possess...\x02\x03",
            "#5300422V#0013FErnest Reis.\x02\x03",
            "#5300423VWe will now place you under arrest on the\x01",
            "charge of interference of public duty!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x1)
    Sleep(300)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)
    Sound(1907, 255, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetMessageWindowPos(40, 5, -1, -1)

    AnonymousTalk(
        0x11,
        (
            "#5300424V\x07\x02",
            "#3P#4S#10AGYAHHHHHH!\x02",
        )
    )

    Sleep(700)
    SetMessageWindowPos(14, 280, 60, 3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15500, 300)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x6)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x11, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_48DE():
        OP_9D(0xFE, 0x6F54, 0xFFFEFE30, 0xFFFFFA24, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_48DE)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(200)
    OP_24(0x35D)
    Battle("BattleInfo_158", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x11, 0x0, 0x0)
    EndChrThread(0x11, 0xFF)
    Call(0, 28)
    Return()

    # Function_25_34D8 end

    def Function_26_4938(): pass

    label("Function_26_4938")


    def lambda_493D():
        OP_9E(0xFE, 0x8E94, 0x14B4, 0xFFFE2B40, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_493D)

    label("loc_4953")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4993")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_498B")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4993")

    label("loc_498B")

    Sleep(15)
    Jump("loc_4953")

    label("loc_4993")

    WaitChrThread(0x12, 1)
    Return()

    # Function_26_4938 end

    def Function_27_4998(): pass

    label("Function_27_4998")


    def lambda_499D():
        OP_9E(0xFE, 0x5014, 0x14B4, 0x1D4C0, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_499D)

    label("loc_49B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F3")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_49EB")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49F3")

    label("loc_49EB")

    Sleep(15)
    Jump("loc_49B3")

    label("loc_49F3")

    WaitChrThread(0x13, 1)
    Return()

    # Function_27_4998 end

    def Function_28_49F8(): pass

    label("Function_28_49F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch02353.itc", 0x24)
    LoadChrToIndex("monster/ch67453.itc", 0x25)
    LoadChrToIndex("chr/ch00156.itc", 0x26)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    OP_68(28500, -65000, 1000, 0)
    MoveCamera(43, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 28300, -66000, -1000, 0)
    SetChrPos(0x102, 29400, -66000, -1500, 0)
    SetChrPos(0x103, 27500, -66000, -2500, 0)
    SetChrPos(0x104, 28600, -66000, -3000, 0)
    SetChrPos(0x107, 31600, -66000, -1200, 315)
    SetChrPos(0x108, 30900, -66000, -2400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 28500, -66000, 2000, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x1)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 28500, -66000, 2000, 180)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    PlayEffect(0x0, 0x0, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4C30():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4C30)

    def lambda_4C49():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4C49)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    SetCameraDistance(19000, 4000)
    FadeToBright(2000, 0)
    Sound(903, 0, 100, 0)
    Sleep(1000)
    Sleep(500)
    Sound(965, 0, 100, 0)
    Sound(1908, 255, 100, 0)
    SetMessageWindowPos(100, 0, -1, -1)

    AnonymousTalk(
        0x11,
        (
            "#5300425V\x07\x02",
            "#3P#4S#20AGAAAAAHHHH...!\x02",
        )
    )

    Sleep(2000)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x10, 0x800)

    def lambda_4CDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4CDF)

    def lambda_4CF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4CF0)
    PlayEffect(0x1, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(500)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x11, 0x2)
    Sleep(200)
    SetChrSubChip(0x10, 0x3)
    SetChrSubChip(0x11, 0x3)
    Sleep(300)
    Fade(500)
    EndChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    Sound(514, 0, 100, 0)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x800)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5300426V#12P#0006F*pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300427V#0806FTh-That drug is no joke. Without it,\x01",
            "that wouldn't have been nearly as hard...\x02\x03",
            "#5300428V#0801FHe was as tough as a certain other\x01",
            "former mayor's secretary wishes he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300429V#0906FTo be fair, Ernest seems to have a proper\x01",
            "background in the martial arts.\x02\x03",
            "#5300430V#0908FThis Gnosis... Just how far can it push\x01",
            "people beyond human limits...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300431V#0108F...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(28700, -65000, 1290, 1500)

    def lambda_4F9B():
        OP_96(0xFE, 0x733C, 0xFFFEFE30, 0x76C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F9B)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x10E, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#5300432V#12P#0001FIs he still breathing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300433V#0106F#11PYes, somehow...\x02\x03",
            "#5300434V#0101FThe over-exhaustion will keep him\x01",
            "out of commission for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300435V#12P#0003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300436V#12P#0206FFor now, our best course of action\x01",
            "is to leave him here and move on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300437V#12P#0301FTrue... Our friend here can rest face-first\x01",
            "in the dirt, but we ain't stoppin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300438V#12P#0006FYeah, there's no point in loitering.\x02\x03",
            "#5300439V#0000FElie, time to move out.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#5300440V#0103F#11PI know.\x02\x03",
            "#5300441V#0108F(...Farewell, Ernest.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 32500, -66000, 2000, 180)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_37()
    OP_68(28500, -65000, -500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 28500, -66000, -500, 0)
    SetChrPos(0x1, 28500, -66000, -500, 0)
    SetChrPos(0x2, 28500, -66000, -500, 0)
    SetChrPos(0x3, 28500, -66000, -500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xE6, 3)
    OP_29(0x4F, 0x1, 0x9)
    OP_24(0x35D)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_28_49F8 end

    def Function_29_5303(): pass

    label("Function_29_5303")

    Sleep(400)

    label("loc_5306")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531F")
    Sound(966, 0, 100, 0)
    Sleep(650)
    Jump("loc_5306")

    label("loc_531F")

    Return()

    # Function_29_5303 end

    def Function_30_5320(): pass

    label("Function_30_5320")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5339")
    Call(0, 34)
    Jump("loc_533C")

    label("loc_5339")

    Call(0, 35)

    label("loc_533C")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 239660, 180)
    EventEnd(0x4)
    Return()

    # Function_30_5320 end

    def Function_31_5353(): pass

    label("Function_31_5353")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_536C")
    Call(0, 34)
    Jump("loc_536F")

    label("loc_536C")

    Call(0, 35)

    label("loc_536F")

    Sleep(50)
    SetChrPos(0x0, -11150, 0, 200000, 90)
    EventEnd(0x4)
    Return()

    # Function_31_5353 end

    def Function_32_5386(): pass

    label("Function_32_5386")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_539F")
    Call(0, 34)
    Jump("loc_53A2")

    label("loc_539F")

    Call(0, 35)

    label("loc_53A2")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    # Function_32_5386 end

    def Function_33_53B9(): pass

    label("Function_33_53B9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D2")
    Call(0, 34)
    Jump("loc_53D5")

    label("loc_53D2")

    Call(0, 35)

    label("loc_53D5")

    Sleep(50)
    SetChrPos(0x0, 9730, 0, 199950, 270)
    EventEnd(0x4)
    Return()

    # Function_33_53B9 end

    def Function_34_53EC(): pass

    label("Function_34_53EC")


    ChrTalk(
        0x101,
        (
            "#0001FIt looks like there are levers that will\x01",
            "open the cell doors.\x02\x03",
            "Let's go open those before we do\x01",
            "anything else.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_53EC end

    def Function_35_5467(): pass

    label("Function_35_5467")


    ChrTalk(
        0x101,
        (
            "#0005FWait. There's a second lever for the\x01",
            "cell doors.\x02\x03",
            "#0001FLet's pull that one, too.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_5467 end

    SaveToFile()

Try(main)
