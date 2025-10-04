from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3013.bin",                # FileName
        "M3013",                    # MapName
        "M3013",                    # Location
        0x007C,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3013",                  # 0
        "bm3010",                 # 1
        "bm3010",                 # 2
        "bm3010",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 9,   12,  6,   16,  2,   13,  4)
    Sepith("Sepith_B4", 12,  6,   17,  9,   12,  4,   2)
    Sepith("Sepith_C4", 15,  9,   14,  5,   3,   0,   14)

    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_100", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_104", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_10C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_114", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_134", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_A4", 60, 25, 10, 5,
        (
            ("ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1FC", 0x0010, 38, 6, 60, 4, 1, 50, 0, "bm3010", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms67200.dat", 0, 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67200.dat", "ms72100.dat", 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2C4", 0x0000, 38, 6, 60, 4, 1, 30, 0, "bm3010", "Sepith_C4", 60, 25, 10, 5,
        (
            ("ms67500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67500.dat", "ms67500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67500.dat", "ms67500.dat", "ms67500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67500.dat", "ms67500.dat", "ms67500.dat", "ms67500.dat", 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch67250.itc",               # 10
        "monster/ch67251.itc",               # 11
        "monster/ch72150.itc",               # 12
        "monster/ch72151.itc",               # 13
        "monster/ch67550.itc",               # 14
        "monster/ch67551.itc",               # 15
    ))

    DeclMonster(-260,    14750,   -24000,  0x1010000,    "BattleInfo_134", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-33270,  14410,   -27000,  0x1010000,    "BattleInfo_1FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-54090,  -113940, -27000,  0x1010000,    "BattleInfo_2C4", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-45000,  -27000,  139000,  1500,    -45000,  -26000,  139000,  0x007C, 0,  3,  0x0000)
    DeclActor(-51000,  -27000,  -114000, 1200,    -51000,  -26000,  -114000, 0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_4E8",          # 00, 0
        "Function_1_4E9",          # 01, 1
        "Function_2_75B",          # 02, 2
        "Function_3_8AD",          # 03, 3
        "Function_4_1964",         # 04, 4
    ))


    def Function_0_4E8(): pass

    label("Function_0_4E8")

    Return()

    # Function_0_4E8 end

    def Function_1_4E9(): pass

    label("Function_1_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 4)), scpexpr(EXPR_END)), "loc_4FE")
    OP_71(0x2, 0x96, 0xD2, 0x0, 0x20)

    label("loc_4FE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_51F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_536")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_54D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B")
    OP_70(0x1, 0x5A)
    ClearMapObjFlags(0x1, 0x2)
    Jump("loc_5B1")

    label("loc_56B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")
    OP_70(0x1, 0x14)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_5B1")

    label("loc_589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_70(0x1, 0xA)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_5B1")

    label("loc_5A7")

    OP_70(0x1, 0x0)
    SetMapObjFlags(0x1, 0x2)

    label("loc_5B1")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A")
    OP_70(0x0, 0x0)
    Jump("loc_73E")

    label("loc_73A")

    OP_70(0x0, 0x1E)

    label("loc_73E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754")
    OP_24(0x85)
    Jump("loc_75A")

    label("loc_754")

    Sound(133, 1, 100, 0)

    label("loc_75A")

    Return()

    # Function_1_4E9 end

    def Function_2_75B(): pass

    label("Function_2_75B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x58, 1)"), scpexpr(EXPR_END)), "loc_7DB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_840")

    label("loc_7DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x58),
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

    label("loc_840")

    Jump("loc_8A1")

    label("loc_845")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To the guy who invented zero:\x01",
            "Thanks for nothing!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_8A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_75B end

    def Function_3_8AD(): pass

    label("Function_3_8AD")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(-44520, -26000, 137730, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21520, 0)
    SetChrPos(0x101, -44800, -27000, 136500, 0)
    SetChrPos(0x102, -43800, -27000, 136500, 0)
    SetChrPos(0x103, -44300, -27000, 138000, 0)
    SetChrPos(0x104, -44300, -27000, 135400, 0)
    SetChrPos(0x107, -46400, -27000, 137300, 45)
    SetChrPos(0x108, -46300, -27000, 136400, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AE")
    OP_71(0x2, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 4)

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")

    ChrTalk(
        0x107,
        "#5300232V#6P#0800FIt worked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300233V#11P#0203FThis is one of the foundation's older systems\x01",
            "used to store and process information.\x02\x03",
            "#5300234V#0201FMost scientists consider something like this a\x01",
            "relic now, but it was quite expensive in its prime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300235V#0106F#12PIf anything, Speaker Hartmann must have\x01",
            "provided the funds for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300236V#12P#0003FProbably. Either way, we should perform a\x01",
            "thorough sweep of the surrounding area.\x02\x03",
            "#5300237V#0001FTio, any luck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300238V#11P#0201FYes, actually.\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#5300239V#11P#0205FI was able to find details on how to\x01",
            "release the gate's locks. There are\x01",
            "also some data logs.\x02\x03",
            "#5300240V#0206FThough, only a portion of the data was\x01",
            "still accessible, I am sad to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300241V#12P#0000FWe can work with it. Let's have a look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_CE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1937")
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
            "#1KInformation Terminal 01\x07\x00\x02",
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
        (0, "loc_DA2"),
        (1, "loc_183A"),
        (2, "loc_1914"),
        (SWITCH_DEFAULT, "loc_1923"),
    )


    label("loc_DA2")

    FadeToDark(300, 0, 150)
    SetMessageWindowPos(-1, -1, 43, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S'On Our Order'\x01\x01",
            "My name is Joachim Guenter, high priest of D∴G.\x01",
            "Six years ago, our order was on the brink of\x01",
            "extinction due to the efforts of the authorities\x01",
            "and Bracer Guild. I alone escaped danger and\x01",
            "took refuge in this land of ------. It was the\x01",
            "guidance of the great - that helped me survive\x01",
            "so I could realize the ambitions of our order.\x01",
            "Since the time will surely come... I will record\x01",
            "data in each of these terminals, on which they\x01",
            "shall base the new Testaments.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2STo discuss the origins of our order, I will first\x01",
            "have to turn to the abominable history of the\x01",
            "Zemurian continent.\x01\x01",
            "The Great Collapse, approximately 1,200 years ago,\x01",
            "marked the end of an advanced civilization, and\x01",
            "with it the established order, giving rise to the\x01",
            "bloodshed and poverty of the Dark Ages. In their\x01",
            "fatigue, the people committed a grave sin.\x01\x01",
            "They led themselves to be deluded by the flattery\x01",
            "of pompous fools and accepted their invented,\x01",
            "self-centered cult with open arms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe foolish ------- ------ and their symbol, that\x01",
            "'------- of the ---.' The Dark Ages met its demise,\x01",
            "and this faith spread throughout the continent...\x01\x01",
            "Let us consider: If said ------- truly existed,\x01",
            "can we not assume that she would bestow equal\x01",
            "salvation upon all of us? However, disparity yet\x01",
            "exists, and people continue to perish in disasters\x01",
            "and misfortunes.\x01\x01",
            "Does that mean said ------- discriminates upon\x01",
            "whom she shall bestow salvation? This thought\x01",
            "alone is too ludicrous for words.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is merely an idol invented by the\x01",
            "------- ------ to amass power. A ------- as such\x01",
            "simply does not exist.\x01\x01",
            "Having reached that conclusion, our predecessors\x01",
            "embarked on a long journey to find a ---- ---.\x01\x01",
            "Their efforts were not in vain, for at the dawn\x01",
            "of the Middle Ages, in the depths of this land,\x01",
            "---- ----- --- --------- -- ----- ----- -- --\x01",
            "------- -------...\x01\x01",
            "She was known as...-.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1835")

    ChrTalk(
        0x101,
        "#5300242V#0008F#11PThis is Doctor Guenter's research?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300243V#0108F#12PIt seems to me more like an outline of the\x01",
            "entire cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300244V#0301F#12PReally? Bunch of mumbo jumbo to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300245V#0203F#5PI have a feeling that those bytes of\x01",
            "information were erased intentionally.\x02\x03",
            "#5300246V#0201FRestoring the data would be a feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300247V#0801F#6PI might be crazy, but I could have sworn that\x01",
            "'Septian Church' and 'Goddess of the Sky'\x01",
            "were two of the things missing.\x02\x03",
            "#5300248V#0806FIt's almost as if they're shouting to the\x01",
            "reader that Aidios isn't real...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300249V#0903F#6PAgreed. There's no mistake about it.\x02\x03",
            "#5300250V#0901FUnfortunately, it'll be difficult to dig any\x01",
            "more terms out of the data.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 1)

    label("loc_1835")

    Jump("loc_1932")

    label("loc_183A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")
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
    SetScenarioFlags(0xE5, 2)
    OP_29(0x4F, 0x1, 0x3)
    Call(0, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_190F")

    label("loc_188E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D1")
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
    Jump("loc_190F")

    label("loc_18D1")

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

    label("loc_190F")

    Jump("loc_1932")

    label("loc_1914")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1932")

    label("loc_1923")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1932")

    label("loc_1932")

    Jump("loc_CEF")

    label("loc_1937")

    SetChrPos(0x0, -45000, -27000, 136400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_8AD end

    def Function_4_1964(): pass

    label("Function_4_1964")

    Fade(500)
    OP_68(0, -23000, 18000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_19BC")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_19D3")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_19EA")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2C")
    OP_71(0x1, 0x14, 0x5A, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    Sleep(700)
    Sound(135, 0, 100, 0)
    OP_79(0x1)
    Sound(116, 0, 100, 0)
    OP_70(0x1, 0x5A)
    ClearMapObjFlags(0x1, 0x2)
    Jump("loc_1A9C")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5F")
    OP_71(0x1, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_1A9C")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A92")
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0xA)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_1A9C")

    label("loc_1A92")

    OP_70(0x1, 0x0)
    SetMapObjFlags(0x1, 0x2)

    label("loc_1A9C")

    Sleep(1000)
    Return()

    # Function_4_1964 end

    SaveToFile()

Try(main)
