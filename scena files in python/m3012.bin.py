from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3012.bin",                # FileName
        "m3012",                    # MapName
        "m3012",                    # Location
        0x007C,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 2, 0, 3],
    )

    BuildStringList((
        "m3012",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Demon Mafioso",          # 3
        "Demon Mafioso",          # 4
        "Hellhound",              # 5
        "bm3010",                 # 6
        "bm3010",                 # 7
        "bm3010",                 # 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 9,   12,  6,   16,  2,   13,  4)

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
    MonsterBattlePostion("MonsterBattlePostion_124", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_144", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_20C", 0x0010, 38, 6, 60, 0, 1, 0, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67200.dat", "ms67200.dat", "ms67200.dat", "ms67200.dat", 0, 0, "ms72100.dat", 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_250", 0x0040, 38, 6, 45, 0, 1, 0, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67300.dat", "ms67300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_E4", "ed7405", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
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
        "monster/ch67250.itc",               # 10
        "monster/ch67251.itc",               # 11
        "monster/ch72150.itc",               # 12
        "monster/ch72151.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-111000, -23000,  5500,    0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-236920, -4059,   -24000,  0x1010000,    "BattleInfo_144", 0,   18,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 7,   0.0,                   22.0,                  -25.0,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -7.333333492279053,    5.0,                   1.0])

    DeclActor(-108700, -24000,  0,       1500,    -108700, -23000,  0,       0x007C, 0,  10, 0x0000)
    DeclActor(8000,    -24000,  -118400, 1500,    8000,    -23000,  -118400, 0x007C, 0,  11, 0x0000)
    DeclActor(-111000, -24000,  5500,    1200,    -111000, -24000,  5500,    0x007C, 0,  4,  0x0000)
    DeclActor(6250,    -24000,  -108250, 1200,    6250,    -24000,  -108250, 0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_4CC",          # 00, 0
        "Function_1_4EB",          # 01, 1
        "Function_2_50A",          # 02, 2
        "Function_3_596",          # 03, 3
        "Function_4_805",          # 04, 4
        "Function_5_A54",          # 05, 5
        "Function_6_BDC",          # 06, 6
        "Function_7_C0D",          # 07, 7
        "Function_8_1ABD",         # 08, 8
        "Function_9_1B21",         # 09, 9
        "Function_10_2894",        # 0A, 10
        "Function_11_38E6",        # 0B, 11
        "Function_12_46D0",        # 0C, 12
    ))


    def Function_0_4CC(): pass

    label("Function_0_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EA")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_4CC")

    label("loc_4EA")

    Return()

    # Function_0_4CC end

    def Function_1_4EB(): pass

    label("Function_1_4EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_509")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_4EB")

    label("loc_509")

    Return()

    # Function_1_4EB end

    def Function_2_50A(): pass

    label("Function_2_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_END)), "loc_595")
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 3600, -24000, 31500, 135)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 3800, -24000, 29600, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_595")

    Return()

    # Function_2_50A end

    def Function_3_596(): pass

    label("Function_3_596")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 5)), scpexpr(EXPR_END)), "loc_5C3")
    OP_71(0x7, 0x96, 0xD2, 0x0, 0x20)

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 6)), scpexpr(EXPR_END)), "loc_5D8")
    OP_71(0x6, 0x96, 0xD2, 0x0, 0x20)

    label("loc_5D8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_5F9")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_610")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_627")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659")
    OP_70(0x3, 0x5A)
    OP_70(0x4, 0x5A)
    OP_70(0x5, 0x5A)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_6DB")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68B")
    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)
    OP_70(0x5, 0x14)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_6DB")

    label("loc_68B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BD")
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_6DB")

    label("loc_6BD")

    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)

    label("loc_6DB")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_END)), "loc_7D6")
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    OP_70(0x1, 0x0)
    Jump("loc_7ED")

    label("loc_7E9")

    OP_70(0x1, 0x1E)

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800")
    OP_70(0x2, 0x0)
    Jump("loc_804")

    label("loc_800")

    OP_70(0x2, 0x1E)

    label("loc_804")

    Return()

    # Function_3_596 end

    def Function_4_805(): pass

    label("Function_4_805")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C4")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_904")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_85E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_85E)

    def lambda_878():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_878)
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
    Battle("BattleInfo_20C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8E5"),
        (2, "loc_8F4"),
        (1, "loc_901"),
        (SWITCH_DEFAULT, "loc_904"),
    )


    label("loc_8E5")

    SetScenarioFlags(0x76, 4)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_904")

    label("loc_8F4")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_901")

    OP_B7(0x0)
    Return()

    label("loc_904")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x652, 1)"), scpexpr(EXPR_END)), "loc_95C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_9BF")

    label("loc_95C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
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

    label("loc_9BF")

    Jump("loc_A48")

    label("loc_9C4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and friends can get over barriers, but they sure\x01",
            "can't get over stealing from treasure chests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_A48")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_805 end

    def Function_5_A54(): pass

    label("Function_5_A54")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3E")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_AD4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_B39")

    label("loc_AD4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
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

    label("loc_B39")

    Jump("loc_BD0")

    label("loc_B3E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Just how badly do you have to screw up cooking a\x01",
            "Sincere Lunchbox for it to become a Prank Box, anyway?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_BD0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A54 end

    def Function_6_BDC(): pass

    label("Function_6_BDC")

    TalkBegin(0xFE)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafioso is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_6_BDC end

    def Function_7_C0D(): pass

    label("Function_7_C0D")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch36000.itc", 0x24)
    LoadChrToIndex("chr/ch36100.itc", 0x25)
    LoadChrToIndex("monster/ch67350.itc", 0x26)
    LoadChrToIndex("monster/ch67352.itc", 0x27)
    LoadChrToIndex("monster/ch67353.itc", 0x28)
    LoadChrToIndex("apl/ch50522.itc", 0x29)
    LoadChrToIndex("apl/ch50522.itc", 0x2A)
    SoundLoad(861)
    OP_68(0, -22900, 25000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -1300, -24000, 22100, 0)
    SetChrPos(0x102, -300, -24000, 21800, 0)
    SetChrPos(0x103, -1800, -24000, 20500, 0)
    SetChrPos(0x104, -800, -24000, 20200, 0)
    SetChrPos(0x107, 1500, -24000, 21900, 0)
    SetChrPos(0x108, 1900, -24000, 20900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -700, -24000, 40600, 180)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xA, 0x0)
    SetChrPos(0xA, -1200, -24000, 30900, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 700, -24000, 40600, 180)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, 1200, -24000, 31200, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0x0, 0x80, 0x80, 0x14, 0x32, 0x0)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")

    def lambda_E35():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E35)
    Sleep(50)

    def lambda_E52():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E52)

    def lambda_E6C():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E6C)
    Sleep(50)

    def lambda_E89():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E89)

    def lambda_EA3():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_EA3)
    Sleep(50)

    def lambda_EC0():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EC0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(500)
    OP_6F(0x10)

    ChrTalk(
        0x102,
        (
            "#5300188V#0108F#12PAll the modern technology in this ancient\x01",
            "fort is throwing me off...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x107,
        (
            "#5300189V#11P#0801FI wonder if Joachim modified all\x01",
            "these contraptions himself?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FE0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FE0)
    Sleep(50)

    def lambda_FF0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FF0)

    def lambda_FFD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FFD)
    Sleep(50)

    def lambda_100D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_100D)

    def lambda_101A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_101A)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#5300190V#6P#0003F...I'd say so.\x02\x03",
            "#5300191V#0001FIf I were to guess, this equipment was\x01",
            "used to complete his Gnosis research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300192V#0903F#11PA rational deduction...\x02\x03",
            "#5300193V#0900FAlso, I don't remember the hospital\x01",
            "having any equipment like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1168():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1168)

    def lambda_1175():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1175)
    WaitChrThread(0x108, 2)
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    OP_0D()

    ChrTalk(
        0x108,
        "#5300194V#0901F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300195V#12P#0201FWe have been found...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -23100, 38000, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_68(0, -23100, 28000, 5000)
    SetCameraDistance(22000, 5000)

    def lambda_124C():
        OP_96(0xFE, 0xFFFFFB50, 0xFFFFA240, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_124C)
    Sleep(50)

    def lambda_1269():
        OP_96(0xFE, 0x4B0, 0xFFFFA240, 0x79E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1269)

    def lambda_1283():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1283)

    def lambda_1290():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1290)

    def lambda_129D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_129D)

    def lambda_12AA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_12AA)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5300196V#12P#0013FMore of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300197V#12P#0301FTsk, tsk. Managed to find your\x01",
            "way inside this maze, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300198V#0807FC'mon, just surrender and you won't\x01",
            "receive a pummeling!\x02\x03",
            "#5300199VThat drug may have made you stronger,\x01",
            "but we outnumber y--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300200V#12P#0205FP-Please, hold on...!\x02\x03",
            "#5300201V#0201F#40WThere is...something off about them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300202V#0805FWhat?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(340, -23100, 28730, 3000)
    SetCameraDistance(20900, 3000)

    def lambda_14A5():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14A5)
    Fade(500)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5300203V\x07\x02",
            "#5P#100W#18AAaaaahhhhhhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x8, 2)

    def lambda_1542():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1542)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#5300204V\x07\x02",
            "#5P#100W#18AGuuuuuhhhhhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    ChrTalk(
        0x102,
        "#5300205V#0105FWh-What's wrong with them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300206V#0905FThis again...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -23000, 30600, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(17000, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    def lambda_168B():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_168B)

    def lambda_16A4():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16A4)

    def lambda_16BD():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16BD)

    def lambda_16D6():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16D6)
    Sleep(500)

    def lambda_16F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_16F2)

    def lambda_1703():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1703)

    def lambda_1714():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1714)

    def lambda_1725():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1725)
    Sound(202, 0, 100, 0)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x10)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(22000, 500)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(315, 0, 100, 0)
    OP_24(0x35D)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)

    def lambda_1842():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1842)

    def lambda_185B():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_185B)

    ChrTalk(
        0x8,
        (
            "#5300207V\x07\x02",
            "#6P#5S#15AGaaaaAAAAAHHHHH!\x02",
        )
    )


    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#5S#15AAaaaaAAAAHHHHH!\x02",
        )
    )

    OP_5A()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    CancelBlur(0)
    Fade(250)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 1)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 1)
    OP_68(0, -23100, 28000, 1500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x107,
        "#5300209V#0813F#4SWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300210V#12P#0207FMetamorphosis...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300211V#12P#0007FWe can figure that out later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300212V#12P#0307FFor now, we gotta knock 'em silly!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(814, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 8)
    Sleep(450)
    OP_24(0x35D)
    Battle("BattleInfo_250", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 9)
    Return()

    # Function_7_C0D end

    def Function_8_1ABD(): pass

    label("Function_8_1ABD")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1AF2():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFF060, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AF2)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(130)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_1ABD end

    def Function_9_1B21(): pass

    label("Function_9_1B21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("apl/ch50546.itc", 0x24)
    LoadChrToIndex("monster/ch67350.itc", 0x26)
    LoadChrToIndex("monster/ch67352.itc", 0x27)
    LoadChrToIndex("monster/ch67353.itc", 0x28)
    LoadChrToIndex("chr/ch00056.itc", 0x29)
    SoundLoad(861)
    OP_68(-20, -23100, 30300, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
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
    SetChrPos(0x101, -1300, -24000, 26100, 0)
    SetChrPos(0x102, -300, -24000, 25800, 0)
    SetChrPos(0x103, -1800, -24000, 24500, 0)
    SetChrPos(0x104, -800, -24000, 24200, 0)
    SetChrPos(0x107, 1500, -24000, 25900, 0)
    SetChrPos(0x108, 1900, -24000, 24900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1200, -24000, 30900, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -1200, -24000, 30900, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 1200, -24000, 31200, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x800)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 1200, -24000, 31200, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_11(0x0, 0x80, 0x80, 0x14, 0x32, 0x0)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)
    SetCameraDistance(20000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sound(965, 0, 100, 0)

    def lambda_1E10():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E10)

    ChrTalk(
        0xA,
        (
            "#5300213V\x07\x02",
            "#5P#15A#50WGAaaAAaaHHH...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    Sound(965, 0, 100, 0)

    def lambda_1E5D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E5D)

    ChrTalk(
        0xB,
        (
            "#5300214V\x07\x02",
            "#5P#15A#50WOoooOOOHHH...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(202, 0, 100, 0)

    def lambda_1EA6():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1EA6)

    def lambda_1EBF():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EBF)

    def lambda_1ED8():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ED8)

    def lambda_1EF1():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EF1)

    def lambda_1F0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F0A)

    def lambda_1F1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F1B)

    def lambda_1F2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F2C)

    def lambda_1F3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F3D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    OP_24(0x35D)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_68(0, -23100, 28000, 3000)
    MoveCamera(55, 19, 0, 3000)
    OP_6E(450, 3000)
    SetCameraDistance(23000, 3000)
    Fade(1000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x87, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x1)
    Sound(514, 0, 100, 0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    ClearChrFlags(0x8, 0x800)
    ClearChrFlags(0x9, 0x800)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x107, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x108, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x107)
    OP_64(0x108)
    OP_6F(0x79)

    ChrTalk(
        0x107,
        "#5300215V#0808FThis is horrifying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300216V#0106FIt's like watching a nightmare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300217V#0903FDemonization...\x02\x03",
            "#5300218V#0908FI've heard of things like this, but this\x01",
            "is the first time I've seen it myself....\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(540, -23100, 28800, 1500)

    def lambda_220E():
        OP_96(0xFE, 0xFFFFFCE0, 0xFFFFA240, 0x73A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_220E)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5300219V#0006F#11PThey've lost consciousness.\x02\x03",
            "#5300220V#0008FThey'll be out for a while, but their\x01",
            "lives shouldn't be in danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
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

    ChrTalk(
        0x107,
        "#5300221V#0806FPhew... That's a relief.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21800, 1500)
    OP_68(410, -23100, 29290, 1500)

    def lambda_236C():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_236C)
    Sleep(50)

    def lambda_2389():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2389)
    Sleep(50)

    def lambda_23A6():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23A6)
    Sleep(50)

    def lambda_23C3():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_23C3)
    Sleep(50)

    def lambda_23E0():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23E0)
    WaitChrThread(0x107, 1)

    def lambda_23FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_23FE)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)

    def lambda_2417():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2417)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        (
            "#5300222V#12P#0203FI am afraid that this is another power\x01",
            "of the doctor's Gnosis.\x02\x03",
            "#5300223V#0201FThe transformation occurring in the user's\x01",
            "mind can become so potent that it alters\x01",
            "their body, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300224V#12P#0306FWhoa, Tio Tot... You aren't jokin', are you?\x01",
            "That's freakin' ridiculous.\x02\x03",
            "#5300225V#0310FThey might've been some good-for-nothin'\x01",
            "grunts, but they didn't deserve this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300226V#0807FThis Joachim... I'm going to rearrange his\x01",
            "ugly mug with my staff, just you wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300227V#0003F#11PLet's go.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300228V#0013F#5PWe should comb the surrounding area\x01",
            "for clues.\x02\x03",
            "#5300229VThere may be valuable information on\x01",
            "the cult hidden somewhere nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300230V#0101F#12PUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300231V#0901F#11PLet's do it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 3800, -24000, 31500, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 3800, -24000, 29600, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_37()
    OP_68(0, -23000, 28600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 0, -24000, 28600, 0)
    SetChrPos(0x1, 0, -24000, 28600, 0)
    SetChrPos(0x2, 0, -24000, 28600, 0)
    SetChrPos(0x3, 0, -24000, 28600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_11(0x0, 0x80, 0x80, 0x19, 0x3C, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE5, 0)
    OP_29(0x4F, 0x1, 0x2)
    Sleep(500)
    OP_24(0x35D)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_9_1B21 end

    def Function_10_2894(): pass

    label("Function_10_2894")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(-109170, -23000, -760, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21950, 0)
    SetChrPos(0x101, -111000, -24000, -1500, 90)
    SetChrPos(0x102, -111000, -24000, -500, 90)
    SetChrPos(0x103, -109500, -24000, -1000, 90)
    SetChrPos(0x104, -112100, -24000, -1000, 90)
    SetChrPos(0x107, -110400, -24000, 1500, 135)
    SetChrPos(0x108, -111300, -24000, 1600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2995")
    OP_71(0x7, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x7)
    OP_71(0x7, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 5)

    label("loc_2995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA6")

    ChrTalk(
        0x107,
        "#5300232V#5P#0800FIt worked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300233V#0203F#5PThis is one of the foundation's older systems\x01",
            "used to store and process information.\x02\x03",
            "#5300234V#0201FMost scientists consider something like this a\x01",
            "relic now, but it was quite expensive in its prime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300235V#0106F#6PIf anything, Speaker Hartmann must have\x01",
            "provided the funds for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300236V#6P#0003FProbably. Either way, we should search it for\x01",
            "any potential evidence.\x02\x03",
            "#5300237V#0001FTio, any luck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300238V#5P#0201FYes.\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#5300239V#5P#0205FI was able to find details on how to\x01",
            "release the gate's locks. There are\x01",
            "also some data logs.\x02\x03",
            "#5300240V#0206FOnly a portion of the data was\x01",
            "still accessible, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300241V#6P#0000FWe can work with it.\x01",
            "Let's have a look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_2CA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B9")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KInformation Terminal 02\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[View information]\x01",      # 0
            "[Release lock]\x01",          # 1
            "[Done]\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D63"),
        (1, "loc_37BC"),
        (2, "loc_3896"),
        (SWITCH_DEFAULT, "loc_38A5"),
    )


    label("loc_2D63")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S'On Gnosis'\x01\x01",
            "Gnosis is a secret remedy made from a ---------\x01",
            "----- which grows directly on top of ------- -----\x01",
            "known as Pleroma Grass.\x01\x01",
            "The way it is prepared, -------- ---- -, gives\x01",
            "the user enhanced physical abilities and sensory\x01",
            "receptivity and draws out their latent powers.\x01",
            "----- -------, -------, --- ---- ------------;\x01",
            "--- ---- --------- ---- ---------. Gnosis allows\x01",
            "----- to ---- their ---- to the revered ------\x01",
            "of -.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy doing so, - can draw --------- from the\x01",
            "--------- ----- and thereupon stimulate Her\x01",
            "------. When enough --------- is amassed to\x01",
            "achieve ------, - will be -----------. \x01",
            " \x01",
            "Moreover, Gnosis left room for improvement.\x01",
            "-- ------- --- ------------ -- --- ---- -- -----\x01",
            "------, the ------ of --------- to - would\x01",
            "-------- --------. \x01",
            " \x01",
            "After --- ----- of research, our order has\x01",
            "increased the effects of Gnosis...and repeated\x01",
            "the so-called 'ceremonies.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SAt a ----- ---- --- unfathomable five centuries\x01",
            "prior, the completion of Gnosis lay within reach,\x01",
            "when we hit an unforeseen obstacle.\x01\x01",
            "Due to the scale of our experiments, we were\x01",
            "detected by the authorities and the Bracer Guild.\x01",
            "They led coordinated assaults on our lodges and,\x01",
            "ultimately, our order.\x01\x01",
            "Foolish beyond words, indeed. After all, what\x01",
            "are a few sacrifices at the cost of ------------\x01",
            "a ---- ---?\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn secrecy, I collected the data from the\x01",
            "destroyed lodges and arrived in Crossbell,\x01",
            "the land of ------.\x01\x01",
            "As Pleroma Grass, the foremost ingredient for\x01",
            "Gnosis, ----- in abundance in the --------\x01",
            "-------- of ---------, there would never be\x01",
            "a -------- -- --- ---------. In addition to\x01",
            "the highly advanced facilities once ---------\x01",
            "by the ---------- from the ------ ---- in the\x01",
            "depths of this Sun Fort, I was blessed with an\x01",
            "environment to continue my research...and\x01",
            "finish the secret remedy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B7")

    ChrTalk(
        0x101,
        "#5300251V#0013F#6PIt looks like a lot of details were deleted...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300252V#0101F#6PUnfortunately so. I think we still have enough\x01",
            "information to create a report on that drug, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300253V#0908F#5PIt seems almost certain that Joachim\x01",
            "was using this place as a research facility.\x02\x03",
            "#5300254V#0903FAnd after working these past several years,\x01",
            "he's finally hit the mass production stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300255V#0801F#5PYeah, but what's the deal with\x01",
            "this Pleroma Grass?\x02\x03",
            "#5300256VHe said it was an ingredient, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300257V#0301F#6PPleroma Grass? That's not ringin' any bells.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300258V#0206F#5PI do not remember anything like that, either.\x02\x03",
            "#5300259V#0201FWhen we return home, I should run a full-\x01",
            "scale database search for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 2)

    label("loc_37B7")

    Jump("loc_38B4")

    label("loc_37BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3810")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Activating lock override sequence.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 3)
    OP_29(0x4F, 0x1, 0x4)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3891")

    label("loc_3810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3853")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The barrier has already been opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3891")

    label("loc_3853")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The corresponding lock has already been released.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3891")

    Jump("loc_38B4")

    label("loc_3896")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38B4")

    label("loc_38A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38B4")

    label("loc_38B4")

    Jump("loc_2CB0")

    label("loc_38B9")

    SetChrPos(0x0, -111400, -24000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_2894 end

    def Function_11_38E6(): pass

    label("Function_11_38E6")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(7660, -23000, -119310, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrPos(0x101, 6000, -24000, -120000, 90)
    SetChrPos(0x102, 6000, -24000, -119000, 90)
    SetChrPos(0x103, 7500, -24000, -119500, 90)
    SetChrPos(0x104, 4900, -24000, -119500, 90)
    SetChrPos(0x107, 6600, -24000, -117000, 135)
    SetChrPos(0x108, 5700, -24000, -116900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E7")
    OP_71(0x6, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x6, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 6)

    label("loc_39E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D18")

    ChrTalk(
        0x107,
        "#5300232V#5P#0800FIt worked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300233V#0203F#5PThis is one of the foundation's older systems\x01",
            "used to store and process information.\x02\x03",
            "#5300234V#0201FMost scientists consider something like this a\x01",
            "relic now, but it was quite expensive in its prime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300235V#0106F#6PIf anything, Speaker Hartmann must have\x01",
            "provided the funds for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300236V#6P#0003FProbably. Either way, we should perform a\x01",
            "thorough sweep of the surrounding area.\x02\x03",
            "#5300237V#0001FTio, any luck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300238V#5P#0201FYes, actually.\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#5300239V#5P#0205FI was able to find details on how to\x01",
            "release the gate's locks. There are\x01",
            "also some data logs.\x02\x03",
            "#5300240V#0206FThough, only a portion of the data was\x01",
            "still accessible, I am sad to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300241V#6P#0000FWe can work with it. Let's have a look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_3D18")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A3")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KInformation Terminal 03\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[View information]\x01",      # 0
            "[Release lock]\x01",          # 1
            "[Done]\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DD5"),
        (1, "loc_45A6"),
        (2, "loc_4680"),
        (SWITCH_DEFAULT, "loc_468F"),
    )


    label("loc_3DD5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S'On the Divine Child'\x01\x01",
            "Crossbell is the ---- of D∴G and the ---- --\x01",
            "------, as it is this very place where our sect\x01",
            "--------- the Divine Child ---- --- --------.\x01\x01",
            "The Divine Child ---------- --- ---- --- and\x01",
            "Her --------- is the ------ -- D∴G. ----------\x01",
            "--- Sun Fort -------- ---- ------- -- -- -\x01",
            "----- ---- -- ----------. -- -------, --- ------\x01",
            "--- ------ -- --- --------- -- --- -- ---\x01",
            "----- -- --- Sun Fort.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor ------- to ---- ---- ---- might be hard to\x01",
            "believe for us mortals.\x01\x01",
            "However, I have seen Her with my own eyes.\x01",
            "Within the ------ (referred to as the '------\x01",
            "------') -------- - ------ ----... A ------ --------.\x01\x01",
            "The ------ ------ was ------- by the ------------\x01",
            "-- --- ----, based on the ---------- ----------\x01",
            "had ------- by -------- artifacts, meaning that\x01",
            "like ----- --------- --------- -- --------,\x01",
            "there is nothing ---------- to be found here.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFrom --- --- -- --------- --, the Divine Child,\x01",
            "--- Gnosis, --- ---- --------- ---- ---------,\x01",
            "----- --- -- ---- --------- -- --------.\x01\x01",
            "Once ------ is --------, the Divine Child will\x01",
            "------ and She will ------ the ---- ---, -.\x01",
            "And the ----- and ----- of --- will be --------\x01",
            "within -, releasing the people from the -------'\x01",
            "spell.\x01\x01",
            "That is the prophecy left by the predecessors\x01",
            "of D∴G and the ambition we shall fulfill.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A1")

    ChrTalk(
        0x104,
        (
            "#5300260V#0305F#6PThe hell's this terminal's deal? Pack\x01",
            "of moths eat at it or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300261V#0901F#5PI'm thinking that this might be confidential\x01",
            "information held by the cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300262V#0808F#5PUm, so this 'Divine Child' has gotta\x01",
            "be KeA, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300263V#0106F#6PY-Yes, most likely.\x02\x03",
            "#5300264V#0101FConsidering Doctor Guenter addressed\x01",
            "her as such in front of the IBC...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300265V#0211F#6PHonestly, that just sounded like nothing more\x01",
            "than the delusions of a madman to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300266V#0003F#6PMaybe so. Still, the only way to find\x01",
            "out for sure is to ask the man himself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 3)

    label("loc_45A1")

    Jump("loc_469E")

    label("loc_45A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45FA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Activating lock override sequence.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 4)
    OP_29(0x4F, 0x1, 0x5)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_467B")

    label("loc_45FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_463D")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The barrier has already been opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_467B")

    label("loc_463D")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The corresponding lock has already been released.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_467B")

    Jump("loc_469E")

    label("loc_4680")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469E")

    label("loc_468F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469E")

    label("loc_469E")

    Jump("loc_3D22")

    label("loc_46A3")

    SetChrPos(0x0, 6000, -24000, -118400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_38E6 end

    def Function_12_46D0(): pass

    label("Function_12_46D0")

    Fade(500)
    OP_68(0, -23000, 218000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_4728")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_473F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_473F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_4756")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4756")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47AC")
    OP_71(0x5, 0x14, 0x5A, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    Sleep(700)
    Sound(135, 0, 100, 0)
    OP_79(0x5)
    Sound(116, 0, 100, 0)
    OP_70(0x3, 0x5A)
    OP_70(0x4, 0x5A)
    OP_70(0x5, 0x5A)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_4858")

    label("loc_47AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F3")
    OP_71(0x5, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)
    OP_70(0x5, 0x14)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_4858")

    label("loc_47F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_483A")
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_4858")

    label("loc_483A")

    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)

    label("loc_4858")

    Sleep(1000)
    Return()

    # Function_12_46D0 end

    SaveToFile()

Try(main)
