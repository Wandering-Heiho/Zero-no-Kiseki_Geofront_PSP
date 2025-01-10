from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t162b.bin",                # FileName
        "t162b",                    # MapName
        "t162b",                    # Location
        0x0055,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 85, 0, 0, 0, 2],
    )

    BuildStringList((
        "t162b",                  # 0
        "Event Monster",          # 1
        "Event Monster",          # 2
        "bt162b",                 # 3
        "bt162b",                 # 4
        "bt162b",                 # 5
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_B4", 3,   14,  4,   4,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_F0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_F4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_FC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 12, 45)
    MonsterBattlePostion("MonsterBattlePostion_130", 12, 12, 315)
    MonsterBattlePostion("MonsterBattlePostion_134", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_144", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_20C", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2D4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt162b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch67550.itc",               # 10
        "monster/ch67551.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-3610,   62420,   0,       0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(9070,    61620,   0,       0x1010000,    "BattleInfo_20C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6590,    -63750,  0,       0x1010000,    "BattleInfo_20C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(9500,    0,       -63750,  1200,    9500,    1000,    -63750,  0x007C, 0,  4,  0x0000)
    DeclActor(7600,    0,       3000,    1200,    7600,    1500,    3000,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_4B0",          # 00, 0
        "Function_1_52F",          # 01, 1
        "Function_2_536",          # 02, 2
        "Function_3_706",          # 03, 3
        "Function_4_757",          # 04, 4
        "Function_5_8A3",          # 05, 5
        "Function_6_9A3",          # 06, 6
        "Function_7_F3E",          # 07, 7
        "Function_8_F56",          # 08, 8
        "Function_9_14A7",         # 09, 9
        "Function_10_1505",        # 0A, 10
        "Function_11_1563",        # 0B, 11
        "Function_12_15C1",        # 0C, 12
        "Function_13_161F",        # 0D, 13
    ))


    def Function_0_4B0(): pass

    label("Function_0_4B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C8")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 1)

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DE")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_52E")
    ClearScenarioFlags(0x5C, 0)
    SetChrPos(0x0, 7190, 0, -90, 270)
    SetChrPos(0x1, 7190, 0, -90, 270)
    SetChrPos(0x2, 7190, 0, -90, 270)
    SetChrPos(0x3, 7190, 0, -90, 270)

    label("loc_52E")

    Return()

    # Function_0_4B0 end

    def Function_1_52F(): pass

    label("Function_1_52F")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_52F end

    def Function_2_536(): pass

    label("Function_2_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_58B")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_58B")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")
    OP_70(0x3, 0x0)
    Jump("loc_702")

    label("loc_6FE")

    OP_70(0x3, 0x1E)

    label("loc_702")

    Call(0, 3)
    Return()

    # Function_2_536 end

    def Function_3_706(): pass

    label("Function_3_706")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_723")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    Jump("loc_72D")

    label("loc_723")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)

    label("loc_72D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74B")
    SetChrFlags(0xC, 0x8)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_756")

    label("loc_74B")

    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_756")

    Return()

    # Function_3_706 end

    def Function_4_757(): pass

    label("Function_4_757")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_841")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_7D7")
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
    SetScenarioFlags(0x10B, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_83C")

    label("loc_7D7")

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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_83C")

    Jump("loc_897")

    label("loc_841")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I swear I was just holding it for a friend.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_897")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_757 end

    def Function_5_8A3(): pass

    label("Function_5_8A3")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_986")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x4, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x4, 0x0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x4, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_986")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_9A2")

    Return()

    # Function_5_8A3 end

    def Function_6_9A3(): pass

    label("Function_6_9A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("monster/ch75750.itc", 0x23)
    LoadChrToIndex("monster/ch75750.itc", 0x24)
    OP_68(12250, 500, -7480, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -1000, 0, 0, 90)
    SetChrPos(0x102, -1000, 0, 0, 90)
    SetChrPos(0x103, -1000, 0, 0, 90)
    SetChrPos(0x104, -1000, 0, 0, 90)
    SetChrPos(0x106, -1000, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x8, 7880, 0, 8370, 0)
    SetChrPos(0x9, 9020, 0, -7350, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x8, 0, 0, 7)
    BeginChrThread(0x9, 0, 0, 7)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(4190, 500, 580, 7000)
    SetCameraDistance(23500, 7000)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(750)
    BeginChrThread(0x102, 3, 0, 10)
    Sleep(750)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(750)
    BeginChrThread(0x104, 3, 0, 12)
    Sleep(750)
    BeginChrThread(0x106, 3, 0, 13)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100712V#0011F#6PWh-What's with this fog?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100713V#0108F#6PIt's as if the air has stagnated...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100714V#0301F#6PWhoa, hold up. Couldn't this be\x01",
            "some kinda dangerous gas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100715V#0203F#6PI do not believe so. At least, it will not\x01",
            "have any lasting impact on the body.\x02\x03",
            "#5100716V#0208FThe soul, on the other hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100717V\x07\x03",
            "#0700F#6PIt's likely some sort of miasma.\x02\x03",
            "#5100718V#0702FHeh. Our opponent here may be more\x01",
            "troublesome than I presumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100719V\x07\x00",
            "#0010F#6PDamn them...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(835, 0, 100, 0)
    Fade(1000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    def lambda_DA5():
        OP_95(0xFE, 3970, 0, 4370, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DA5)

    def lambda_DBF():
        OP_95(0xFE, 4000, 0, -4140, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DBF)
    OP_93(0x101, 0x2D, 0x0)
    SetChrPos(0x102, 2230, 0, -960, 90)
    SetChrPos(0x106, 1010, 0, 260, 45)
    OP_68(3930, 800, 30, 0)
    MoveCamera(65, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(25000, 1500)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x102,
        "#5100720V#0101F#6PAgain?!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#5100721V\x07\x03",
            "#0700F#6PThey've met their end.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ED5)

    def lambda_EEA():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EEA)
    SetCameraDistance(20000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    Battle("BattleInfo_2D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 8)
    Return()

    # Function_6_9A3 end

    def Function_7_F3E(): pass

    label("Function_7_F3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F55")
    OP_A0(0xFE, 1250, 0x0, 0xFB)
    Jump("Function_7_F3E")

    label("loc_F55")

    Return()

    # Function_7_F3E end

    def Function_8_F56(): pass

    label("Function_8_F56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    OP_68(4000, 1800, 120, 0)
    MoveCamera(65, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22060, 0)
    SetChrPos(0x101, 4790, 0, 1050, 45)
    SetChrPos(0x102, 4090, 0, -350, 135)
    SetChrPos(0x103, 3780, 0, 1890, 0)
    SetChrPos(0x104, 2880, 0, -1690, 180)
    SetChrPos(0x106, 2020, 0, 280, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_68(4000, 1000, 120, 2000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5100722V#0003F#5PThose were no ordinary monsters...\x02\x03",
            "#5100723V#0008FThey reminded me of the ones we fought\x01",
            "in the tower and temple...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100724V#0208F#5PDespite the higher elements not being\x01",
            "present, I am inclined to agree.\x02\x03",
            "#5100725V#0201FWhat if...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100726V\x07\x03",
            "#0700F#12PThere's the possibility that they are\x01",
            "under the influence of Gnosis, the\x01",
            "same as those mafiosos.\x02\x03",
            "#5100727V#0702FIs that what you wanted to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100728V\x07\x00",
            "#0206F#5PYes. Exactly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100729V#0303F#5PThat'd explain it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100730V#0101F#5PThey certainly were abnormally strong.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    def lambda_12ED():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12ED)
    Sleep(50)

    def lambda_12FD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12FD)
    Sleep(50)

    def lambda_130D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_130D)
    Sleep(50)

    def lambda_131D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_131D)
    Sleep(50)

    def lambda_132D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_132D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0x101,
        (
            "#5100731V#0003F#5PLet's begin our search.\x02\x03",
            "#5100732V#0013FAccording to Cecile, the doctors and the\x01",
            "rest of the staff should still be in here.\x02\x03",
            "#5100733VWe should find Doctor Guenter, while we're\x01",
            "at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100734V#0101F#2PUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100735V#0301F#12PLet's hurry before time runs out!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 4500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE3, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_8_F56 end

    def Function_9_14A7(): pass

    label("Function_9_14A7")


    def lambda_14AC():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14AC)

    def lambda_14C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_14DA():
        OP_95(0xFE, 2600, 0, 580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14DA)
    WaitChrThread(0x101, 1)

    def lambda_14F8():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14F8)
    WaitChrThread(0x101, 1)
    Return()

    # Function_9_14A7 end

    def Function_10_1505(): pass

    label("Function_10_1505")


    def lambda_150A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_150A)

    def lambda_151F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_151F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1538():
        OP_95(0xFE, 2700, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1538)
    WaitChrThread(0xFE, 1)

    def lambda_1556():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1556)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1505 end

    def Function_11_1563(): pass

    label("Function_11_1563")


    def lambda_1568():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1568)

    def lambda_157D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_157D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1596():
        OP_95(0xFE, 1380, 0, -1820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1596)
    WaitChrThread(0xFE, 1)

    def lambda_15B4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15B4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1563 end

    def Function_12_15C1(): pass

    label("Function_12_15C1")


    def lambda_15C6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15C6)

    def lambda_15DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15DB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_15F4():
        OP_95(0xFE, 1420, 0, 1670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15F4)
    WaitChrThread(0xFE, 1)

    def lambda_1612():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1612)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_15C1 end

    def Function_13_161F(): pass

    label("Function_13_161F")


    def lambda_1624():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1624)

    def lambda_1639():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1639)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1652():
        OP_95(0xFE, 950, 0, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1652)
    WaitChrThread(0xFE, 1)

    def lambda_1670():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1670)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_161F end

    SaveToFile()

Try(main)
