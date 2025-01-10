from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0630.bin",                # FileName
        "t0630",                    # MapName
        "t0630",                    # Location
        0x006A,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 106, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0630",                  # 0
        "Winged Ant",             # 1
        "bt0610",                 # 2
        "bt0610",                 # 3
        "bt0610",                 # 4
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 10,  7,   0,   7,   9,   6,   9)

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

    # monster count: 8

    BattleInfo(
        "BattleInfo_114", 0x0000, 23, 6, 60, 6, 1, 40, 0, "bt0610", "Sepith_A4", 75, 25, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_184", 0x0400, 23, 6, 60, 6, 1, 40, 0, "bt0610", "Sepith_A4", 75, 25, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1F4", 0x0000, 23, 6, 45, 0, 1, 0, 0, "bt0610", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch64850.itc",               # 10
        "monster/ch64851.itc",               # 11
    ))

    DeclNpc(20110,   1500,    -32299,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(100120,  29150,   8050,    0x1010000,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(58300,   29340,   3550,    0x1010000,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(71140,   -970,    800,     0x1010000,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(47150,   -13350,  -3950,   0x10100B4,    "BattleInfo_114", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(100120,  29150,   8050,    0x1810000,    "BattleInfo_184", 1504, 16,  0xFFFF, 0,  1)
    DeclMonster(58300,   29340,   3550,    0x1810000,    "BattleInfo_184", 1505, 16,  0xFFFF, 0,  1)
    DeclMonster(71140,   -970,    800,     0x1810000,    "BattleInfo_184", 1506, 16,  0xFFFF, 0,  1)
    DeclMonster(47150,   -13350,  -3950,   0x18100B4,    "BattleInfo_184", 1507, 16,  0xFFFF, 0,  1)

    DeclActor(105900,  8000,    24800,   1200,    105900,  9000,    24800,   0x007C, 0,  3,  0x0000)
    DeclActor(42580,   -1250,   580,     1200,    42580,   -250,    580,     0x007C, 0,  4,  0x0000)
    DeclActor(20110,   1000,    -32299,  1200,    20110,   2000,    -32299,  0x007C, 0,  5,  0x0000)
    DeclActor(55680,   -1750,   -41900,  1200,    52000,   -6150,   -45150,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_483",          # 01, 1
        "Function_2_4F0",          # 02, 2
        "Function_3_5DF",          # 03, 3
        "Function_4_76A",          # 04, 4
        "Function_5_904",          # 05, 5
        "Function_6_B49",          # 06, 6
        "Function_7_E39",          # 07, 7
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_482")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_464")

    label("loc_482")

    Return()

    # Function_0_464 end

    def Function_1_483(): pass

    label("Function_1_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_491")
    Jump("loc_4EF")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C2")
    ClearChrFlags(0xD, 0x80)

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1")
    ClearChrFlags(0xE, 0x80)

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0")
    ClearChrFlags(0xF, 0x80)

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF")
    ClearChrFlags(0x10, 0x80)

    label("loc_4EF")

    Return()

    # Function_1_483 end

    def Function_2_4F0(): pass

    label("Function_2_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_503")
    OP_70(0x0, 0x0)
    Jump("loc_507")

    label("loc_503")

    OP_70(0x0, 0x1E)

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A")
    OP_70(0x1, 0x0)
    Jump("loc_51E")

    label("loc_51A")

    OP_70(0x1, 0x1E)

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_531")
    OP_70(0x2, 0x0)
    Jump("loc_535")

    label("loc_531")

    OP_70(0x2, 0x1E)

    label("loc_535")

    Sound(124, 1, 100, 0)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 52000, -6150, -45150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DE")
    Event(0, 7)

    label("loc_5DE")

    Return()

    # Function_2_4F0 end

    def Function_3_5DF(): pass

    label("Function_3_5DF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C9")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_65F")
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
    SetScenarioFlags(0x115, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_6C4")

    label("loc_65F")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_6C4")

    Jump("loc_75E")

    label("loc_6C9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Just think. If you spent less time harassing chests, you\x01",
            "could have already finished this support request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_75E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5DF end

    def Function_4_76A(): pass

    label("Function_4_76A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_854")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4F, 1)"), scpexpr(EXPR_END)), "loc_7EA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_84F")

    label("loc_7EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
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

    label("loc_84F")

    Jump("loc_8F8")

    label("loc_854")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You peer deep inside the chest once again,\x01",
            "only to bump your head against the lid as\x01",
            "you stand back up. Serves you right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_8F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_76A end

    def Function_5_904(): pass

    label("Function_5_904")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC3")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A03")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_95D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_95D)

    def lambda_977():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_977)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_1F4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9E4"),
        (2, "loc_9F3"),
        (1, "loc_A00"),
        (SWITCH_DEFAULT, "loc_A03"),
    )


    label("loc_9E4")

    SetScenarioFlags(0x75, 3)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_A03")

    label("loc_9F3")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A00")

    OP_B7(0x0)
    Return()

    label("loc_A03")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64B, 1)"), scpexpr(EXPR_END)), "loc_A5B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x64B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_ABE")

    label("loc_A5B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x64B),
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

    label("loc_ABE")

    Jump("loc_B3D")

    label("loc_AC3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Remember when you didn't have to check the\x01",
            "treasure chests twice? Ah, those were the days.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B3D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_904 end

    def Function_6_B49(): pass

    label("Function_6_B49")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FFishing in a mine. This is the life.\x02",
    )

    CloseMessageWindow()
    OP_68(52750, -2850, -44000, 1500)
    MoveCamera(90, 27, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(26000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E34")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_END)), "loc_C29")
    MiniGame(0x6, 0x7, 0xD6D8, 0xFFFFF92A, 0xFFFF5AF6, 0xE1, 0xCB20, 0xFFFFE7FA, 0xFFFF4FA2)
    Jump("loc_E34")

    label("loc_C29")

    MiniGame(0x6, 0x8, 0xD6D8, 0xFFFFF92A, 0xFFFF5AF6, 0xE1, 0xCB20, 0xFFFFE7FA, 0xFFFF4FA2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E34")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(55000, -250, -42250, 0)
    MoveCamera(90, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("apl/ch50162.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, 55000, -1750, -42250, 225)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x0,
        "Lloyd",
        (
            "#0005FWh-What the heck is this...?\x02\x03",
            "#0003FWell, it's gorgeous, that's for sure.\x01",
            "Is this some kind of rare fish?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(55000, -250, -42250, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, 55000, -1750, -42250, 225)
    SetChrPos(0x2, 55000, -1750, -42250, 225)
    SetChrPos(0x3, 55000, -1750, -42250, 225)
    SetChrPos(0x4, 55000, -1750, -42250, 225)
    SetChrPos(0x5, 55000, -1750, -42250, 225)
    SetChrPos(0x6, 55000, -1750, -42250, 225)
    SetChrPos(0x7, 55000, -1750, -42250, 225)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x69, 2)

    label("loc_E34")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_6_B49 end

    def Function_7_E39(): pass

    label("Function_7_E39")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(63530, -200, -37770, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18690, 0)
    SetChrPos(0x101, 62960, -1700, -37310, 90)
    SetChrPos(0x102, 64590, -1700, -38050, 0)
    SetChrPos(0x103, 63900, -1700, -35830, 180)
    SetChrPos(0x104, 65170, -1700, -36660, 270)
    SetCameraDistance(17690, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#0000FThat's the last of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0203FYes, it should be.\x02\x03",
            "#0200FI can not detect any more monsters\x01",
            "within the abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FPhew, finally!\x02\x03",
            "Runnin' around this ugly place has\x01",
            "tuckered me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe've definitely worked hard.\x02\x03",
            "What do you say, Lloyd? Shall we head\x01",
            "back to Mayor Bickson's house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FUgh, I don't think I'm gonna make it...\x02\x03",
            "#0309FLloooooyd. Do a pal a solid and carry\x01",
            "me back to the entrance, pleeeease? ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#0003FNot gonna happen.\x02\x03",
            "#0000FStop messing around. It's time to head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306FTch, killjoy.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x1, 0x4)
    SetChrName("")
    SetMessageWindowPos(-1, 40, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Return to Mayor Bickson's house?\x07\x00",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Return]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11ED")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1200")

    label("loc_11ED")

    SetChrPos(0x0, 63730, -1700, -33940, 180)
    EventEnd(0x5)

    label("loc_1200")

    Return()

    # Function_7_E39 end

    SaveToFile()

Try(main)
