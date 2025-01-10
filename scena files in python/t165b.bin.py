from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t165b.bin",                # FileName
        "t165b",                    # MapName
        "t165b",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 88, 0, 0, 0, 2],
    )

    BuildStringList((
        "t165b",                  # 0
        "Ernest",                 # 1
        "Angel of Slaughter, Renne",# 2
        "Pater-Mater",            # 3
        "Ernest's Companion",     # 4
        "Ernest's Companion",     # 5
        "SE制御",                 # 6
        "bt162b",                 # 7
        "bt162b",                 # 8
        "bt163b",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_C4", 3,   14,  4,   4,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_100", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_104", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_10C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_114", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_154", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_21C", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2E4", 0x0042, 34, 6, 0, 0, 0, 0, 0, "bt163b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02300.dat", "ms67201.dat", "ms67201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_F4", "ed7405", "ed7000", "ATBonus_A4"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-50170,  39240,   0,       0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-60420,  106890,  0,       0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(95760,   109010,  0,       0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)

    DeclActor(109500,  0,       56500,   1500,    109500,  900,     56500,   0x007C, 0,  15, 0x0000)
    DeclActor(95000,   0,       113500,  1200,    95000,   1000,    113500,  0x007C, 0,  4,  0x0000)
    DeclActor(-50000,  0,       36500,   1200,    -50000,  1000,    36500,   0x007C, 0,  5,  0x0000)
    DeclActor(-62000,  0,       110000,  1200,    -62000,  1000,    110000,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_598",          # 00, 0
        "Function_1_605",          # 01, 1
        "Function_2_60C",          # 02, 2
        "Function_3_79D",          # 03, 3
        "Function_4_819",          # 04, 4
        "Function_5_968",          # 05, 5
        "Function_6_AD9",          # 06, 6
        "Function_7_C4B",          # 07, 7
        "Function_8_C67",          # 08, 8
        "Function_9_C86",          # 09, 9
        "Function_10_2013",        # 0A, 10
        "Function_11_205C",        # 0B, 11
        "Function_12_20A5",        # 0C, 12
        "Function_13_2D5E",        # 0D, 13
        "Function_14_2DA1",        # 0E, 14
        "Function_15_317A",        # 0F, 15
        "Function_16_3458",        # 10, 16
        "Function_17_64BB",        # 11, 17
        "Function_18_64E0",        # 12, 18
        "Function_19_6533",        # 13, 19
        "Function_20_6576",        # 14, 20
        "Function_21_6E10",        # 15, 21
    ))


    def Function_0_598(): pass

    label("Function_0_598")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B0")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 1)

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CA")
    Event(0, 9)

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5DE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)
    Jump("loc_604")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_5F5")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_604")

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_604")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 20)

    label("loc_604")

    Return()

    # Function_0_598 end

    def Function_1_605(): pass

    label("Function_1_605")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_605 end

    def Function_2_60C(): pass

    label("Function_2_60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_621")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_621")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_END)), "loc_632")
    OP_66(0x0, 0x1)

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_68C")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_754")
    OP_1B(0x1, 0x0, 0x15)

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_767")
    OP_70(0x8, 0x0)
    Jump("loc_76B")

    label("loc_767")

    OP_70(0x8, 0x1E)

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E")
    OP_70(0x9, 0x0)
    Jump("loc_782")

    label("loc_77E")

    OP_70(0x9, 0x1E)

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    OP_70(0xA, 0x0)
    Jump("loc_799")

    label("loc_795")

    OP_70(0xA, 0x1E)

    label("loc_799")

    Call(0, 3)
    Return()

    # Function_2_60C end

    def Function_3_79D(): pass

    label("Function_3_79D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0xA, 0x4)
    Jump("loc_7C6")

    label("loc_7BB")

    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0xA, 0x4)

    label("loc_7C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E4")
    SetChrFlags(0x10, 0x8)
    SetMapObjFlags(0x8, 0x4)
    Jump("loc_7EF")

    label("loc_7E4")

    ClearChrFlags(0x10, 0x8)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_7EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D")
    SetChrFlags(0xE, 0x8)
    SetMapObjFlags(0x9, 0x4)
    Jump("loc_818")

    label("loc_80D")

    ClearChrFlags(0xE, 0x8)
    ClearMapObjFlags(0x9, 0x4)

    label("loc_818")

    Return()

    # Function_3_79D end

    def Function_4_819(): pass

    label("Function_4_819")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_903")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4A, 1)"), scpexpr(EXPR_END)), "loc_899")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_8FE")

    label("loc_899")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8FE")

    Jump("loc_95C")

    label("loc_903")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Maybe she's born with it.\x01",
            "Maybe it's Ursuline.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_95C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_819 end

    def Function_5_968(): pass

    label("Function_5_968")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A52")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x87, 1)"), scpexpr(EXPR_END)), "loc_9E8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_A4D")

    label("loc_9E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A4D")

    Jump("loc_ACD")

    label("loc_A52")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After reexamining the chest, you find something else...\x01",
            "IT'S THE BUG OF LEGENDS!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_ACD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_968 end

    def Function_6_AD9(): pass

    label("Function_6_AD9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC3")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B59")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_BBE")

    label("loc_B59")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BBE")

    Jump("loc_C3F")

    label("loc_BC3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "*cough* *cough*...*COUGH* *cough*\x01",
            "Sorry about that. I'm feeling a bit conchested.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C3F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_AD9 end

    def Function_7_C4B(): pass

    label("Function_7_C4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C66")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_7_C4B")

    label("loc_C66")

    Return()

    # Function_7_C4B end

    def Function_8_C67(): pass

    label("Function_8_C67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C85")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_C67")

    label("loc_C85")

    Return()

    # Function_8_C67 end

    def Function_9_C86(): pass

    label("Function_9_C86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch02300.itc", 0x23)
    LoadChrToIndex("chr/ch02350.itc", 0x24)
    LoadChrToIndex("chr/ch02351.itc", 0x25)
    LoadChrToIndex("monster/ch67250.itc", 0x26)
    LoadChrToIndex("monster/ch67251.itc", 0x27)
    LoadChrToIndex("chr/ch00051.itc", 0x28)
    LoadChrToIndex("chr/ch00151.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00351.itc", 0x2B)
    LoadChrToIndex("chr/ch00551.itc", 0x2C)
    SoundLoad(861)
    OP_68(110910, 400, 58340, 0)
    OP_6E(440, 0)
    MoveCamera(38, 26, 0, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, 99000, 0, 50600, 90)
    SetChrPos(0x102, 99000, 0, 49400, 90)
    SetChrPos(0x103, 97800, 0, 49400, 90)
    SetChrPos(0x104, 97800, 0, 50600, 90)
    SetChrPos(0x106, 96600, 0, 50000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 113800, 0, 50000, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 112500, 0, 51300, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, 112500, 0, 48700, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xB, 0, 0, 8)
    BeginChrThread(0xC, 0, 0, 8)
    SetMapFlags(0x2000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x2, "event\\ev605_00.eff")
    FadeToBright(1000, 0)
    OP_68(102940, 400, 51730, 4000)
    MoveCamera(38, 26, 0, 4000)
    SetCameraDistance(23750, 4000)
    Sleep(2000)

    def lambda_F48():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F48)
    Sleep(50)

    def lambda_F60():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F60)
    Sleep(50)

    def lambda_F78():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F78)
    Sleep(50)

    def lambda_F90():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F90)
    Sleep(50)

    def lambda_FA8():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_FA8)
    Sleep(200)

    def lambda_FC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC0)
    Sleep(50)

    def lambda_FD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FD4)
    Sleep(500)

    def lambda_FE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FE8)
    Sleep(50)

    def lambda_FFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FFC)
    Sleep(500)

    def lambda_1010():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1010)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x79)
    OP_0D()
    Sound(1902, 255, 100, 0)
    Sleep(800)

    NpcTalk(
        0x8,
        "Young Man's Voice",
        "#5100803V#3PEarlier than I expected.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(111800, 1200, 50000, 2500)
    MoveCamera(60, 16, 0, 2500)
    SetCameraDistance(19500, 2500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5100804V#0007FYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100805V#0101FErnest?!\x02",
    )

    CloseMessageWindow()
    Sound(1899, 255, 100, 0)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(600)
    OP_68(109660, 1100, 50060, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(20420, 2500)

    def lambda_11A7():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11A7)
    Sleep(500)

    def lambda_11BF():
        OP_95(0xFE, 108000, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11BF)
    Sleep(50)

    def lambda_11DC():
        OP_95(0xFE, 108000, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11DC)
    Sleep(50)

    def lambda_11F9():
        OP_95(0xFE, 106750, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11F9)
    Sleep(50)

    def lambda_1216():
        OP_95(0xFE, 106750, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1216)
    Sleep(50)

    def lambda_1233():
        OP_95(0xFE, 105500, 0, 50000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1233)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#5100806V#30WHello, Elie. It's been about two months now,\x01",
            "hasn't it?\x02\x03",
            "#5100807VThe night is young, yet the moon looks\x01",
            "positively gorgeous.\x02",
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
        0x102,
        "#5100808V#0101F#6PErnest... Your eyes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100809V\x07\x03",
            "#0700F#6PHmph. He's already given himself\x01",
            "over to demonization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100810V\x07\x00",
            "#6610F#11POh, the legendary Yin has graced\x01",
            "us with his presence, has he?\x02\x03",
            "#5100811V#6613FMy future would have been secure--if\x01",
            "only you kept your damn mouths shut.\x02\x03",
            "#5100812V#6611FAllow me this opportunity to sincerely\x01",
            "express my gratitude towards you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100813V\x07\x03",
            "#0702F#6PThe shadows are my domain...and I won't\x01",
            "allow anyone to assume my name.\x02\x03",
            "#5100814VEven if they have obtained a demon's strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100815V\x07\x00",
            "#6610F#11PHeh. You're one to talk, Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100816V#0201F#6PSo you are the one responsible for\x01",
            "manipulating the monsters here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100817V#0010F#6PWhy are you here? HOW are you here?\x02\x03",
            "#5100818V#0007FAren't you supposed to be in prison?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100819V#6613F#11PHeh heh. Prison?\x02\x03",
            "#5100820V#6610FThat pathetic building, just like this hospital,\x01",
            "has already fallen into our hands.\x02",
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
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5100821V#0005F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100822V#0310F#6PThe prison guards should all be members\x01",
            "of the CGF stationed at Bellguard Gate...\x02\x03",
            "#5100823VAre you sayin' the mafia attacked the gate,\x01",
            "too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100824V#6613F#11PHeh. Not exactly.\x02\x03",
            "#5100825V#6610FAlso, don't mix us up with those\x01",
            "pieces of filth, Revache.\x02\x03",
            "#5100826VThey're nothing more than puppets\x01",
            "to help us achieve our goals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100827V#0006F#6PI knew it...\x02\x03",
            "#5100828V#0013FYou're using some trick to manipulate\x01",
            "the people who've consumed Gnosis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100829V#6600F#11PRight you are, Bannings.\x02\x03",
            "#5100830V#6604FEverything is going exactly according\x01",
            "to our great comrade's plan.\x02\x03",
            "#5100831V#6610FPawns! Revache are mere pawns to aid us\x01",
            "in the execution of our grand ceremony!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100832V#0101F#6PYour great comrade...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100833V#0003F#6PA remnant of the D∴G cult and the\x01",
            "mastermind hiding behind the mafia...\x02\x03",
            "#5100834V#0013FIn other words...the resident of this office.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(111600, 1000, 50000, 2500)
    MoveCamera(60, 26, 0, 2500)
    SetCameraDistance(19500, 2500)
    Sleep(300)
    Sound(1903, 255, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    Sound(1904, 255, 100, 0)

    ChrTalk(
        0x8,
        "#5100836V#4S#11P#20AHAHAHAHAHAHA!\x02",
    )

    Sleep(2000)
    StopBGM(0xFA0)
    Fade(500)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(540, 0, 80, 0)
    Sound(531, 0, 100, 0)
    SetCameraDistance(21500, 800)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0xC, 3, 0, 11)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    OP_68(109660, 1100, 50060, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(20420, 2500)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    Sleep(250)
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
    Sleep(200)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x2C)
    SetChrSubChip(0x106, 0x0)

    def lambda_1D98():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D98)
    Sleep(50)

    def lambda_1DB0():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DB0)
    Sleep(50)

    def lambda_1DC8():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DC8)
    Sleep(50)

    def lambda_1DE0():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DE0)
    Sleep(50)

    def lambda_1DF8():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DF8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
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
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5100837V#0007F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100838V\x07\x03",
            "#0707F#6P#NThis demonic aura...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#5100839V#0207F#6P#NThe three higher elements have surfaced...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5100840V\x07\x02",
            "#6613F#11P#30WIf you wish to know the answer you seek,\x01",
            "try to defeat me.\x02\x03",
            "#5100841V#6610F#30WI, who has received the blessing of Gnosis\x01",
            "from my great comrade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100842V#0101F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100843V#0307F#6PGet ready!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0x35D)
    Battle("BattleInfo_2E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Call(0, 12)
    Return()

    # Function_9_C86 end

    def Function_10_2013(): pass

    label("Function_10_2013")

    PlayEffect(0x0, 0x5, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_10_2013 end

    def Function_11_205C(): pass

    label("Function_11_205C")

    PlayEffect(0x0, 0x6, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_11_205C end

    def Function_12_20A5(): pass

    label("Function_12_20A5")

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
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    LoadChrToIndex("chr/ch00551.itc", 0x27)
    LoadChrToIndex("chr/ch02300.itc", 0x28)
    LoadChrToIndex("chr/ch02350.itc", 0x29)
    LoadChrToIndex("chr/ch02351.itc", 0x2A)
    LoadChrToIndex("chr/ch02353.itc", 0x2B)
    LoadChrToIndex("chr/ch02352.itc", 0x2C)
    SoundLoad(861)
    OP_68(109660, 1100, 50060, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18420, 0)
    SetChrPos(0x101, 107540, 0, 50360, 90)
    SetChrPos(0x102, 106840, 0, 48670, 90)
    SetChrPos(0x103, 105610, 0, 49480, 90)
    SetChrPos(0x104, 104460, 0, 50510, 90)
    SetChrPos(0x106, 105970, 0, 51390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, 111000, 0, 50000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetMapFlags(0x2000)
    StopEffect(0x7, 0x0)
    LoadEffect(0x0, "event\\ev602_00.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20420, 2000)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2400")

    ChrTalk(
        0x8,
        (
            "#5100844V\x07\x02",
            "#6613F#11P#30WHeh. I expected nothing less of you, Yin...\x02\x03",
            "#5100845V#6610FBeing able to fend me off in that state\x01",
            "means you're just as much a monster as\x01",
            "the rumors have said...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100846V\x07\x03",
            "#0700F#6PHmph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100847V\x07\x02",
            "#6600F#11P#30WAnd I won't forget about you four. The\x01",
            "CPD's most annoying division.\x02\x03",
            "#5100849V#6604FYou've exceeded all my expectations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2499")

    label("loc_2400")


    ChrTalk(
        0x8,
        (
            "#5100848V\x07\x02",
            "#6613F#11P#30WHeh. You four truly are the CPD's\x01",
            "most annoying division, aren't you?\x02\x03",
            "#5100849V#6600FYou've exceeded all my expectations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2499")


    ChrTalk(
        0x102,
        (
            "#5100850V\x07\x00",
            "#0108F#6PErnest, why are you doing this?!\x02\x03",
            "#5100851V#0103FBetraying Grandfather and becoming\x01",
            "a lapdog of this monstrous cult...\x02\x03",
            "#5100852V#0107FHow did you fall this low?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100853V\x07\x02",
            "#6605F#11PMe? Fallen? No, Elie, I've simply\x01",
            "come to realize the truth.\x02\x03",
            "#5100854V#6613FOh, yes...\x02\x03",
            "#5100855VI understand the true meaning\x01",
            "behind this land of Crossbell...\x02\x03",
            "#5100856V#6610FI can see everything for what it\x01",
            "really is now!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100857V#0101F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100858V#0206F#6P#NUtter nonsense.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#5100859V#0301F#6P#NThis guy's out of his mind.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5100860V#0003F#6PI've heard enough.\x02\x03",
            "#5100861V#0013FFormer First Secretary, Ernest Reis...\x02\x03",
            "#5100862VUnder state law, you are hereby under arrest on the\x01",
            "charges of assault, incitement of a riot, unlawful\x01",
            "seizure of property, drug use, jailbreak, and more.\x02\x03",
            "#5100863V#0007FSurrender and come quietly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100864V\x07\x02",
            "#6613F#11PWhy the rush, Bannings?\x02\x03",
            "#5100865VThe night has just begun...and the show\x01",
            "our comrade has written is just starting.\x02\x03",
            "#5100866V#6610FYour personal invitation is right over there.\x01",
            "Be sure to give it a thorough examination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100867V\x07\x00",
            "#0011F#6PWhat?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(111440, 400, 58730, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17580, 2000)

    def lambda_2941():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2941)

    def lambda_294E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_294E)
    Sleep(100)

    def lambda_295E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_295E)

    def lambda_296B():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_296B)
    Sleep(100)

    def lambda_297B():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_297B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#5100868V#0105F#1PAre those...files?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(109660, 1100, 50060, 0)
    MoveCamera(50, 19, 0, 0)
    SetCameraDistance(20420, 0)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 13)
    StopEffect(0x0, 0x0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 80, 0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5100869V\x07\x02",
            "#6610F#11PHaha! We'll meet again, SSS!\x02\x03",
            "#5100870VAfter you cross the land of death\x01",
            "standing in your way, that is...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2B1D():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B1D)

    def lambda_2B2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B2A)
    Sleep(50)

    def lambda_2B3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B3A)
    Sleep(50)

    def lambda_2B4A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B4A)
    Sleep(50)

    def lambda_2B5A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B5A)
    Sleep(50)

    def lambda_2B6A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2B6A)
    WaitChrThread(0x8, 1)
    OP_68(115300, 1200, 50000, 1000)
    MoveCamera(65, 13, 0, 1000)
    SetCameraDistance(15500, 1000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_2BAC():
        OP_9B(0x0, 0xFE, 0x0, 0x8FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BAC)
    WaitChrThread(0x8, 1)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_2BCF():
        OP_9D(0xFE, 0x1C138, 0x2EE, 0xC350, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BCF)
    WaitChrThread(0x8, 1)
    Sound(854, 0, 100, 0)

    def lambda_2BF6():
        OP_9D(0xFE, 0x1F338, 0xFFFFD8F0, 0xC350, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BF6)
    WaitChrThread(0x8, 1)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    ChrTalk(
        0x101,
        (
            "#5100871V\x07\x00",
            "#0010FNo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100872V\x07\x03",
            "#0707FThere's no escape!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(113000, 1200, 50000, 1500)
    MoveCamera(60, 26, 0, 1500)
    SetCameraDistance(21420, 1500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)

    def lambda_2CB9():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CB9)

    def lambda_2CCE():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CCE)

    def lambda_2CE3():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CE3)

    def lambda_2CF8():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CF8)

    def lambda_2D0D():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2D0D)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x35D)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_20A5 end

    def Function_13_2D5E(): pass

    label("Function_13_2D5E")

    OP_25(0x35D, 0x5A)
    Sleep(100)
    OP_25(0x35D, 0x50)
    Sleep(100)
    OP_25(0x35D, 0x46)
    Sleep(100)
    OP_25(0x35D, 0x3C)
    Sleep(100)
    OP_25(0x35D, 0x32)
    Sleep(100)
    OP_25(0x35D, 0x28)
    Sleep(100)
    OP_25(0x35D, 0x1E)
    Sleep(100)
    OP_25(0x35D, 0x14)
    Sleep(100)
    OP_25(0x35D, 0xA)
    Sleep(100)
    OP_24(0x35D)
    Return()

    # Function_13_2D5E end

    def Function_14_2DA1(): pass

    label("Function_14_2DA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(114540, 900, 50290, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24200, 0)
    SetChrPos(0x101, 112980, 0, 50210, 90)
    SetChrPos(0x102, 112670, 0, 48780, 90)
    SetChrPos(0x103, 111040, 0, 48560, 90)
    SetChrPos(0x104, 111900, 0, 50560, 90)
    SetChrPos(0x106, 109870, 0, 49310, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapFlags(0x2000)
    StopEffect(0x7, 0x0)
    FadeToBright(1000, 0)
    OP_68(113040, 900, 50290, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100873V#0011F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100874V#0101F#5PTh-That thing that he grabbed on to...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_END)), "loc_2F1F")

    ChrTalk(
        0x103,
        (
            "#5100875V#0206F#6PIt appeared to be the dragon we\x01",
            "encountered at Stargazer's Tower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F64")

    label("loc_2F1F")


    ChrTalk(
        0x103,
        "#5100876V#0206F#6PIt appeared to be an Ancient Winged Dragon...\x02",
    )

    CloseMessageWindow()

    label("loc_2F64")


    ChrTalk(
        0x104,
        "#5100877V#0307FThat's so not fair, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100878V\x07\x03",
            "#0700F#6PHmph. I suppose it's impossible\x01",
            "for us to pursue him now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x106, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#5100879V\x07\x03",
            "#0700F#11PTime is of the essence. Hurry and\x01",
            "take a look at his 'invitation.'\x02\x03",
            "#5100880VAfter all, it must have been prepared\x01",
            "by Reis' so-called comrade.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_309C():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_309C)

    def lambda_30A9():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30A9)
    Sleep(100)

    def lambda_30B9():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30B9)

    def lambda_30C6():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30C6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#5100881V\x07\x00",
            "#0005F#11PThat's right...\x02\x03",
            "#5100882V#0013FLet's check it out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(24700, 2000)
    Sleep(2000)
    SetChrPos(0x0, 106500, 0, 50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x0, 0x1)
    SetScenarioFlags(0xE3, 5)
    OP_29(0x4D, 0x1, 0xE)
    PlayBGM("ed7526", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_14_2DA1 end

    def Function_15_317A(): pass

    label("Function_15_317A")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis176.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Two files, one black and one white, are placed\x01",
            "neatly on the desk.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D0")

    AnonymousTalk(
        0x101,
        "#5100883V#0005FLook at the emblem!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#5100884V#0201FCould this be the official crest of D∴G...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#5100885V#0101FIt's extremely similar to the one we found in the temple.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#5100886V#0301FSame place we had to fight off a bunch of fiends.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x106,
        (
            "#5100887V\x07\x03",
            "#0700FSuch a place exists?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#5100888V#0006FYeah. It's similar to the tower you had us go to.\x02\x03",
            "#5100889V#0013FNow, as for these files...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE3, 6)

    label("loc_33D0")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Look through the files]\x01",      # 0
            "[Not yet]\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3439"),
        (1, "loc_3450"),
        (SWITCH_DEFAULT, "loc_3455"),
    )


    label("loc_3439")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x0, 0x1)
    Call(0, 16)
    Jump("loc_3455")

    label("loc_3450")

    Jump("loc_3455")

    label("loc_3455")

    EventEnd(0x3)
    Return()

    # Function_15_317A end

    def Function_16_3458(): pass

    label("Function_16_3458")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("apl/ch50505.itc", 0x1F)
    LoadChrToIndex("chr/ch09501.itc", 0x20)
    LoadChrToIndex("apl/ch50115.itc", 0x21)
    SoundLoad(953)
    OP_68(109250, 1000, 56760, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25250, 0)
    SetChrPos(0x101, 107800, 0, 56800, 90)
    SetChrPos(0x102, 106700, 0, 56800, 90)
    SetChrPos(0x103, 107800, 0, 55700, 45)
    SetChrPos(0x104, 106700, 0, 58000, 135)
    SetChrPos(0x106, 108800, 0, 54400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 114900, 600, 50000, 270)
    ClearChrFlags(0x9, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis100.itp")
    LoadEffect(0x0, "event\\ev600_01.eff")
    LoadEffect(0x1, "event\\ev601_01.eff")
    FadeToBright(1000, 0)
    SetCameraDistance(24250, 4000)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D25")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x102,
        "#5100890V#0108FHow horrible...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x106,
        (
            "#5100891V\x07\x03",
            "#0702FThere truly is no decency left in this world.\x02\x03",
            "#5100892VThough, it's a surprise that Speaker Hartmann himself\x01",
            "was subject to blackmail.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#5100893V\x07\x00",
            "#0303FSomeone must have found out one of Hartmann's\x01",
            "secrets and blackmailed him into cooperating.\x02\x03",
            "#5100894V#0301FWhat the hell is this 'Paradise'?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#5100895V#0208FI am not sure.\x02\x03",
            "#5100896VIt was probably one of the cult's lodges,\x01",
            "if I were to guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#5100897V#0003FRegardless of what it was, he was able to find one\x01",
            "of the speaker's vulnerabilities and then exploited it.\x02\x03",
            "#5100898V#0013FWhat's more, he lent Revache a helping hand in\x01",
            "order to guarantee the cult refuge in Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#5100899V#0110FAbsolutely unforgivable. He's Speaker of the\x01",
            "Diet. How could he do something as foolish\x01",
            "as getting caught up in all this...?\x02\x03",
            "#5100900V#0108FBecause of people like Hartmann, Grandfather has\x01",
            "been toiling with his work all these years, and\x01",
            "Father was forced to abandon us and Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#5100901V#0008FElie...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#5100902V#0208F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x0, 0x0)

    ChrTalk(
        0x106,
        (
            "#5100903V\x07\x03",
            "#0700F#11PIt's not time to get emotional, yet.\x02\x03",
            "#5100904VThat black notebook indicates that St. Ursula\x01",
            "Medical College isn't actually the place where\x01",
            "Gnosis is being manufactured.\x02\x03",
            "#5100905VPlus, the shipment list in there suggests that\x01",
            "the mafia isn't the only organization that the\x01",
            "drug has wormed its way into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100906V\x07\x00",
            "#0003F#5PGood catch. He must have another\x01",
            "base of operations in Crossbell...\x02\x03",
            "#5100907V#0013FMaybe that's where the missing\x01",
            "people are being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100908V#0203F#12PMost likely.\x02\x03",
            "#5100909V#0201FBut where could that be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100910V#0306F#1PI just wanna know who else they could've\x01",
            "shipped this crap to, 'sides the mafia.\x02\x03",
            "#5100911V#0301FYou don't think they got Heiyue, do ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100912V\x07\x03",
            "#0702F#11PHmph. Cao is not naive enough to try his\x01",
            "luck with this foolishness.\x02\x03",
            "#5100913V#0700FI'd say possible candidates include some\x01",
            "sort of pharmaceutical company...\x02\x03",
            "#5100914V...terrorist cells, jaeger corps, or even\x01",
            "national intelligence agencies.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100915V#0303F#1PThat's a relief, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100916V#0106F#6PThe grotesque reality of Crossbell's situation\x01",
            "is becoming more and more apparent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100917V#0006F#6PYeah...\x02\x03",
            "#5100918V#0001FWe should see what's in the white\x01",
            "file, too.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis101.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis115.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis127.itp")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x103,
        "#5100919V#0208F...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#5100920V#0110FN-No...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x106,
        (
            "#5100921V\x07\x03",
            "#0700FHmm... It seems to record the victims of their\x01",
            "'ceremonies,' six years ago.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#5100922V#0311FThose sick bastards... How could they do something\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#5100944V#0003F...\x02\x03",
            "#5100924V#0008FI'm sorry, Tio. We have to see what's inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#5100925V#0204F#30WPlease, do not apologize.\x02\x03",
            "#5100926V#0202FJust continue with your investigation, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#5100927V#0003FOkay.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    CreatePortrait(2, 112, 65520, 368, 240, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis102.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4235")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_4235")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#5100928V#0013FUgh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#5100929V#0213F#30WHaha...\x02\x03",
            "#5100930V#0212F...I think my looks have improved over the years.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#5100931V#0008FTio...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#5100932V#0102FOf course they have...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#5100933V#0304FHaha... You're so cute now, I can hardly recognize ya.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#5100934V#0212FI know you are simply trying to cheer me up,\x01",
            "but...thank you.\x02\x03",
            "#5100935V#0213FLloyd. Please continue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#5100936V#0003F...Right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0x2, 0x0)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    CreatePortrait(2, 112, 65520, 368, 240, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis103.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_44F6")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    Jump("loc_4514")

    label("loc_44F6")

    OP_C9(0x2, 0x0, 0x1F400, 0x0, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_4514")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#5100937V#0005FOh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#5100938V#0301FThat who I think it is?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#5100939V#0208FRenne...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#5100940V#0103FIt must be. So she's connected to all of this,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x106,
        (
            "#5100941V\x07\x03",
            "#0700FThat girl is an acquaintance of yours, is that right?\x02\x03",
            "#5100942VAround that time, I had heard rumors of kidnappings\x01",
            "taking place in the Eastern Quarter...\x02\x03",
            "#5100943VThese cultists must be guilty of those crimes.\x01",
            "I'm certain.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#5100923V#0003F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0x2, 0x0)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis104.itp")
    OP_C9(0x2, 0x1, 0x190, 0x190, 0x0)
    OP_C9(0x2, 0x0, 0x36B00, 0xBB80, 0x0)
    OP_C9(0x2, 0x2, 0xFFFF9E58, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a photograph stuck in the file.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_C9(0x2, 0x0, 0x0, 0xFFFF5420, 0x3E8)
    OP_C9(0x2, 0x2, 0x0, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x1)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#5100945V#0013F...?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#5100946V#0107FKeA?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#5100947V#0201FImpossible...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#5100948V#0310FThat son of a bitch...! Was it too much to ask\x01",
            "for her to be left outta this shit?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x106,
        (
            "#5100949V\x07\x03",
            "#0700FThe girl you rescued from the Schwarze Auction,\x01",
            "hmm?\x02\x03",
            "#5100950VThis looks like a newer photo than the others.\x01",
            "Could it have been taken recently?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#5100951V\x07\x00",
            "#0006FYeah, probably so.\x02\x03",
            "#5100952V#0010FDamn it! He knew everything from the very beginning!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4AF6")

    AnonymousTalk(
        0x102,
        (
            "#5100953V#0108FWhen we brought KeA here...\x02\x03",
            "#5100954V#0101F...he innocently suggested we have her stay at the\x01",
            "hospital for tests.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C6C")

    label("loc_4AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4BAB")

    AnonymousTalk(
        0x103,
        (
            "#5100955V#0203FRemember when we brought KeA here, Lloyd?\x02\x03",
            "#5100956V#0201FHe innocently suggested that we should have her\x01",
            "hospitalized in order to run tests...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4C6C")

    label("loc_4BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4C6C")

    AnonymousTalk(
        0x104,
        (
            "#5100957V#0303FWe brought KeDo here to ask about her memories.\x02\x03",
            "#5100958V#0310FThat slimy bastard wanted her to stay at the hospital\x01",
            "so he could run a bunch of tests on her...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4C6C")

    StopBGM(0xFA0)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        "#5100959V#3PTeehee. I'd say you're on the right track, now.\x02",
    )

    CloseMessageWindow()
    OP_68(109250, 1000, 56760, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21890, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x2, 0x0)

    label("loc_4D25")

    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#5100960V\x07\x03",
            "#0707F#11PWho goes there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100961V\x07\x00",
            "#0005F#5PI know that voice...\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    OP_68(115330, 1000, 50270, 2500)
    MoveCamera(67, 17, 0, 2500)

    def lambda_4E32():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4E32)
    Sleep(50)

    def lambda_4E42():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E42)
    Sleep(50)

    def lambda_4E52():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E52)
    Sleep(50)

    def lambda_4E62():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4E62)
    Sleep(50)

    def lambda_4E72():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4E72)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#5100962V#0205FLook...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100963V#0105FRenne?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100964V#0301FSeriously?!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(112510, 1000, 51940, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26200, 0)
    SetChrPos(0x101, 108890, 0, 53750, 90)
    SetChrPos(0x102, 108080, 0, 52250, 90)
    SetChrPos(0x103, 107910, 0, 54870, 90)
    SetChrPos(0x104, 107150, 0, 53720, 90)
    SetChrPos(0x106, 107240, 0, 56080, 90)
    OP_68(112890, 1000, 51950, 2500)
    MoveCamera(57, 15, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(23650, 2500)

    def lambda_4FA0():
        OP_95(0xFE, 109970, 0, 51460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FA0)

    def lambda_4FBA():
        OP_95(0xFE, 109180, 0, 50270, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FBA)

    def lambda_4FD4():
        OP_95(0xFE, 108860, 0, 52330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FD4)

    def lambda_4FEE():
        OP_95(0xFE, 107860, 0, 51050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4FEE)

    def lambda_5008():
        OP_95(0xFE, 107760, 0, 52680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5008)
    WaitChrThread(0x102, 1)

    def lambda_5026():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5026)
    WaitChrThread(0x101, 1)

    def lambda_5037():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5037)
    WaitChrThread(0x103, 1)

    def lambda_5048():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5048)
    WaitChrThread(0x104, 1)

    def lambda_5059():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5059)
    WaitChrThread(0x106, 1)

    def lambda_506A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_506A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)
    SetCameraDistance(23150, 80000)

    ChrTalk(
        0x101,
        "#5100965V#0001F#6PHow long have you been sitting there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100966V\x07\x03",
            "#0700F#6PI wasn't able to sense your presence...\x02\x03",
            "#5100967VYou aren't an ordinary girl, are you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Renne",
        (
            "#5100968V\x07\x00",
            "#3304F#11PI'd say I'm about as ordinary as you.\x02",
        )
    )

    CloseMessageWindow()
    OP_CA(0x1, 0x3, 0x0)
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#5100969VAllow me to formally introduce myself:\x02\x03",
            "#5100970VI am Renne. Ouroboros Enforcer No. XV,\x01",
            "the Angel of Slaughter.\x02\x03",
            "#5100971VIt's a pleasure to officially make your\x01",
            "acquaintance, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    ChrTalk(
        0x101,
        "#5100972V#0006F#6PJust like Estelle and Joshua said...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100973V\x07\x03",
            "#0700F#6POuroboros... You work alongside the\x01",
            "Direwolf, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100974V\x07\x00",
            "#3305F#11POh, you know of Walter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100975V\x07\x03",
            "#0702F#6PI've met him in battle once before.\x02\x03",
            "#5100976VIn the end, he ran away, leaving\x01",
            "things unresolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100977V\x07\x00",
            "#3304F#11PFunny. I'm sure he probably thinks\x01",
            "the same thing about you.\x02\x03",
            "#5100978V#3302FPerhaps I should ask him to join\x01",
            "me when I return to the society...\x02\x03",
            "#5100979V#3309FOr would Bleublanc be the better\x01",
            "choice, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100980V\x07\x03",
            "#0702F#6PHeh. And now the phantom thief's\x01",
            "true name comes out into the open.\x02\x03",
            "#5100981VYou Ouroboros people are quite the\x01",
            "interesting bunch, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100982V\x07\x00",
            "#3302F#11PYou think so? Honestly, it's strange\x01",
            "that someone like you hasn't been\x01",
            "scouted to join yet.\x02\x03",
            "#5100983V#3309FPerhaps there's a reason for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100984V\x07\x03",
            "#0700F#6PEnough of your nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100985V\x07\x00",
            "#0003F#6PRenne, is it possible Ouroboros\x01",
            "has a part in all of this?\x02\x03",
            "#5100986V#0013FAre they helping with what this\x01",
            "lab's owner is trying to cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100987V#3304F#11PI'm afraid not.\x02\x03",
            "#5100988VYou see, I have personal reasons\x01",
            "for staying in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#5100989V#3308F#11PJoachim Guenter...\x02\x03",
            "#5100990V...associate professor of St. Ursula Medical\x01",
            "College and high priest of the D∴G cult.\x02\x03",
            "#5100991V#3303FIt seems he collected all the results of their\x01",
            "ceremonies and put the finishing touches\x01",
            "on his Gnosis, all while hiding in plain sight.\x02\x03",
            "#5100992V#3300FAnd with this, I finally have every piece of\x01",
            "information I wanted to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100993V#0008F#6PSo you were looking for...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100994V#0208F#6P...this white file, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100995V#3304F#11PI've always had my suspicions, but\x01",
            "I lacked decisive evidence...\x02\x03",
            "#5100996V#3300FAs of now, 'his' injuries have been\x01",
            "fixed, and you helped me overcome\x01",
            "what I couldn't myself.\x02\x03",
            "#5100997V#3309FFinally...my reasons for coming to\x01",
            "Crossbell State have been narrowed\x01",
            "down to one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100998V#0005F#6PHuh?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(112890, 1200, 51950, 800)
    Fade(500)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 114900, 800, 50000, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5100999V#3300F#11PNext time you see Estelle and Joshua,\x01",
            "could you please tell them this?\x02\x03",
            "#5101000V'I will give you one final chance to\x01",
            "capture me.'\x02\x03",
            "#5101001V#3304FHeehee. Something tells me that\x01",
            "their efforts will amount to nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101002V#0013F#6PRenne...what are you planning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5101003V#3300F#11PIn this land, I'm a stray kitten...a mere\x01",
            "observer in all of this.\x02\x03",
            "#5101004VI have no intention of giving you\x01",
            "assistance or interfering.\x02\x03",
            "#5101005V#3303FBut, I can at least offer you one\x01",
            "word of warning.\x02\x03",
            "#5101006V#3301FThat girl is the key to everything.\x01",
            "Be careful to not let her be taken\x01",
            "away from you.\x02\x03",
            "#5101007V#3302FThough, you hardly need me to tell\x01",
            "you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101008V#0005F#6PThe key to everything...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5101009V#0101F#6P#NDo you mean KeA?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#5101010V#3309F#11PI believe it's about time for me to be\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x4)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    Sound(820, 0, 100, 0)
    OP_A1(0x9, 0x384, 0x4, 0x4, 0x5, 0x6, 0x7)
    Sleep(300)

    ChrTalk(
        0x9,
        "#5101011V#3304F#11PEveryone, have a pleasant evening.\x02",
    )

    CloseMessageWindow()
    OP_A1(0x9, 0x384, 0x3, 0x6, 0x5, 0x4)
    Sleep(300)
    StopBGM(0x1770)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x4)
    Sound(854, 0, 100, 0)
    Fade(500)
    OP_68(113940, 1000, 51950, 1000)
    MoveCamera(57, 15, 0, 1000)
    SetCameraDistance(22130, 1000)
    SetChrChip(0x0, 0x9, 0x1E, 0x12C)

    def lambda_5F3C():
        OP_9D(0xFE, 0x1D45C, 0xFFFFD8F0, 0xC350, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F3C)
    Sleep(800)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    EndChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5101012V#0007F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5101013V#0307F#6P#NThe hell?!\x02",
    )

    CloseMessageWindow()
    OP_68(114250, 1000, 51350, 1500)

    def lambda_6046():
        OP_95(0xFE, 113120, 0, 50450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6046)
    Sleep(50)

    def lambda_6063():
        OP_95(0xFE, 112260, 0, 49260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6063)
    Sleep(50)

    def lambda_6080():
        OP_95(0xFE, 112030, 0, 51400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6080)
    Sleep(50)

    def lambda_609D():
        OP_95(0xFE, 110940, 0, 49890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_609D)
    Sleep(50)

    def lambda_60BA():
        OP_95(0xFE, 110470, 0, 51110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_60BA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x11)
    BeginChrThread(0xD, 1, 0, 18)
    BeginChrThread(0xA, 3, 0, 17)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x7, 0x1000)
    OP_78(0x7, 0xA)
    OP_49()
    OP_74(0x7, 0xF)
    OP_71(0x7, 0xF1, 0x104, 0x0, 0x20)
    SetChrPos(0xA, 118500, -8150, 47300, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_D1(0x9, 0x7, "Null_ren(52)")
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x8000)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_r0(63)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_r2(64)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_l0(66)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_l2(65)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_S_jet_r1(61)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_S_jet_l1(62)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_kata_jet_r(53)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_kata_jet_l(54)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_63A3():
        OP_96(0xFE, 0x1CEE4, 0xFFFFF704, 0xB8C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_63A3)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0xA, 1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x4)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    OP_0D()
    OP_A1(0x9, 0x384, 0x7, 0x4, 0x5, 0x6, 0x7, 0x6, 0x5, 0x4)
    Sleep(500)
    Sleep(500)

    def lambda_6470():
        OP_96(0xFE, 0x1CEE4, 0x10CC, 0xB8C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6470)
    WaitChrThread(0xA, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0xD, 2, 0, 19)
    EndChrThread(0xD, 0x1)
    WaitChrThread(0xD, 2)
    EndChrThread(0xA, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x3B9)
    SetScenarioFlags(0x5C, 1)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3458 end

    def Function_17_64BB(): pass

    label("Function_17_64BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64DF")
    OP_82(0x46, 0x46, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_17_64BB")

    label("loc_64DF")

    Return()

    # Function_17_64BB end

    def Function_18_64E0(): pass

    label("Function_18_64E0")

    Sound(954, 0, 70, 0)
    Sound(953, 2, 0, 0)
    Sleep(80)
    OP_25(0x3B9, 0xA)
    Sleep(80)
    OP_25(0x3B9, 0x14)
    Sleep(80)
    OP_25(0x3B9, 0x1E)
    Sleep(80)
    OP_25(0x3B9, 0x28)
    Sleep(80)
    OP_25(0x3B9, 0x32)
    Sleep(80)
    OP_25(0x3B9, 0x3C)
    Sleep(80)
    OP_25(0x3B9, 0x46)
    Sleep(80)
    OP_25(0x3B9, 0x50)
    Sleep(80)
    OP_25(0x3B9, 0x5A)
    Sleep(80)
    OP_25(0x3B9, 0x64)
    Return()

    # Function_18_64E0 end

    def Function_19_6533(): pass

    label("Function_19_6533")

    OP_25(0x3B9, 0x5A)
    Sleep(150)
    OP_25(0x3B9, 0x50)
    Sleep(150)
    OP_25(0x3B9, 0x46)
    Sleep(150)
    OP_25(0x3B9, 0x3C)
    Sleep(150)
    OP_25(0x3B9, 0x32)
    Sleep(150)
    OP_25(0x3B9, 0x28)
    Sleep(150)
    OP_25(0x3B9, 0x1E)
    Sleep(150)
    OP_25(0x3B9, 0x14)
    Sleep(150)
    OP_25(0x3B9, 0xA)
    Sleep(150)
    OP_24(0x3B9)
    Return()

    # Function_19_6533 end

    def Function_20_6576(): pass

    label("Function_20_6576")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(114540, 900, 50290, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24200, 0)
    SetChrPos(0x101, 113630, 0, 49990, 90)
    SetChrPos(0x102, 112940, 0, 48520, 90)
    SetChrPos(0x103, 111480, 0, 48550, 90)
    SetChrPos(0x104, 112430, 0, 50730, 90)
    SetChrPos(0x106, 110760, 0, 49390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapFlags(0x2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_68(113040, 900, 50290, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x106)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#5101014V#0106F#5PA part of me wishes that all\x01",
            "of that was just a dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5101015V#0201F#6PThe level of technology Ouroboros\x01",
            "possesses must be monumental.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5101016V\x07\x03",
            "#0700F#6PYes. It appears we need to reassess\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5101017V\x07\x00",
            "#0306F#5PDamn it. That Ernest guy was bad\x01",
            "enough, but this is even crazier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101018V#0006F#5PTrue.\x02\x03",
            "#5101019V#0008FHowever, at least we know Renne isn't\x01",
            "connected to this particular incident.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68A5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68A5)
    Sleep(50)

    def lambda_68B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68B5)
    Sleep(50)

    def lambda_68C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_68C5)
    Sleep(50)

    def lambda_68D5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68D5)
    Sleep(50)

    def lambda_68E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_68E5)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5101020V#0003F#11PWe've uncovered the true mastermind\x01",
            "behind all of this and can start to piece\x01",
            "together his intentions, albeit vaguely.\x02\x03",
            "#5101021V#0013FWith that being the case, we need to\x01",
            "hurry and get back to Crossbell City--\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5101022V#0005F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5101023V#0101F#11PGood timing.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#5101024V#0013FThis is Lloyd Bannings, Special Support Section!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5101025V\x07\x05",
            "Thank goodness you're safe.\x02\x03",
            "#5101026VIt's me, Deputy Commander Baelz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5101027V\x07\x00",
            "#0005FDeputy Commander...?!\x02\x03",
            "#5101028V#0000FWhat's your location?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5101029V\x07\x05",
            "I'm almost at St. Ursula.\x02\x03",
            "#5101030VI hope you have no issues with\x01",
            "my unit storming the premises.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5101031V\x07\x00",
            "#0004FN-Not really.\x02\x03",
            "#5101032V#0000FWe've already dealt with the mafia here.\x02\x03",
            "#5101033VIf you could check on the hospital staff we\x01",
            "rescued and take them somewhere safe,\x01",
            "I would appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sonya's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5101034V\x07\x05",
            "Understood. We'll rendezvous later.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 2)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_6576 end

    def Function_21_6E10(): pass

    label("Function_21_6E10")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0008FTime is precious. Let's have a\x01",
            "look at the 'invitation' that's on\x01",
            "the desk for now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x4)
    Return()

    # Function_21_6E10 end

    SaveToFile()

Try(main)
