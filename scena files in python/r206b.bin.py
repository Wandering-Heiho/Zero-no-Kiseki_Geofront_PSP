from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r206b.bin",                # FileName
        "r206b",                    # MapName
        "r206b",                    # Location
        0x0062,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r206b",                  # 0
        "War Hound",              # 1
        "War Hound",              # 2
        "War Hound",              # 3
        "War Hound",              # 4
        "War Hound",              # 5
        "War Hound",              # 6
        "War Hound",              # 7
        "War Hound",              # 8
        "War Hound",              # 9
        "War Hound",              # 10
        "Mafioso",                # 11
        "Mafioso",                # 12
        "Zeit",                   # 13
        "White Wolf",             # 14
        "White Wolf",             # 15
        "White Wolf",             # 16
        "White Wolf",             # 17
        "White Wolf",             # 18
        "White Wolf",             # 19
        "Renne",                  # 20
        "Arios",                  # 21
        "車",                     # 22
        "SE制御",                 # 23
        "BR206b",                 # 24
        "To Crossbell City",      # 25
        "To Mainz Mining Village",# 26
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 9, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0002, 16, 6, 0, 0, 0, 0, 0, "BR206b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31001.dat", "ms31101.dat", "ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(18120,   10000,   151900,  1200,    18120,   11000,   151900,  0x007C, 0,  2,  0x0000)

    PlaceName(-3.0, 0.0, -15.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(87.0, 6.0, 122.0, 0x0000, 0x0000, "To Mainz Mining Village")

    ScpFunction((
        "Function_0_4D8",          # 00, 0
        "Function_1_4FC",          # 01, 1
        "Function_2_514",          # 02, 2
        "Function_3_6AB",          # 03, 3
        "Function_4_1943",         # 04, 4
        "Function_5_196A",         # 05, 5
        "Function_6_1994",         # 06, 6
        "Function_7_5065",         # 07, 7
        "Function_8_5096",         # 08, 8
        "Function_9_50C0",         # 09, 9
        "Function_10_50EA",        # 0A, 10
        "Function_11_5111",        # 0B, 11
        "Function_12_512E",        # 0C, 12
        "Function_13_5158",        # 0D, 13
        "Function_14_517F",        # 0E, 14
        "Function_15_519D",        # 0F, 15
        "Function_16_5229",        # 10, 16
        "Function_17_52BC",        # 11, 17
        "Function_18_52FD",        # 12, 18
        "Function_19_533E",        # 13, 19
        "Function_20_537F",        # 14, 20
        "Function_21_53C0",        # 15, 21
        "Function_22_5401",        # 16, 22
        "Function_23_5442",        # 17, 23
        "Function_24_545A",        # 18, 24
        "Function_25_5474",        # 19, 25
    ))


    def Function_0_4D8(): pass

    label("Function_0_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4EC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)
    Jump("loc_4FB")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_4FB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 6)

    label("loc_4FB")

    Return()

    # Function_0_4D8 end

    def Function_1_4FC(): pass

    label("Function_1_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F")
    OP_70(0x1, 0x0)
    Jump("loc_513")

    label("loc_50F")

    OP_70(0x1, 0x1E)

    label("loc_513")

    Return()

    # Function_1_4FC end

    def Function_2_514(): pass

    label("Function_2_514")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_594")
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
    SetScenarioFlags(0x105, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_5F9")

    label("loc_594")

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

    label("loc_5F9")

    Jump("loc_69F")

    label("loc_5FE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For your use of debug mode, your IP address has been logged.\x01",
            "You will be blocked from downloading Trails to ZX Advent.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_69F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_514 end

    def Function_3_6AB(): pass

    label("Function_3_6AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("monster/ch75650.itc", 0x2C)
    LoadChrToIndex("monster/ch75651.itc", 0x2D)
    LoadChrToIndex("apl/ch50121.itc", 0x2E)
    LoadChrToIndex("chr/ch31054.itc", 0x2F)
    LoadEffect(0x0, "battle\\mg128_00.eff")
    LoadEffect(0x1, "event\\ev101_00.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x12, 11530, 0, 138630, 180)
    SetChrPos(0x13, 12930, 0, 137890, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    OP_78(0x0, 0x1D)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, 18850, 0, 138470, 0)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(85720, 600, 134260, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40000, 0)
    OP_68(60560, -2600, 129789, 8000)
    SetCameraDistance(47000, 8000)
    SetChrPos(0x8, 88960, 6000, 118390, 270)
    SetChrPos(0x9, 87080, 6000, 116180, 270)
    SetChrPos(0xA, 91990, 6000, 116720, 270)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0x1E, 1, 0, 24)

    def lambda_940():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_940)

    def lambda_955():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_955)

    def lambda_96A():
        OP_9B(0x0, 0xFE, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_96A)
    Sleep(1500)
    OP_63(0x9, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_63(0x8, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_63(0xA, 0xFFFFFD44, 1600, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0x1E, 0x1)
    OP_0D()
    OP_6F(0x11)
    Fade(1000)
    OP_68(14370, 3400, 137860, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(14370, 900, 137860, 6000)
    OP_0D()
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(100)
    OP_63(0x8, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_63(0xA, 0xFFFFFC7C, 1800, 0x28, 0x2B, 0x64, 0x0)
    OP_6F(0x1)
    Sleep(500)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(13820, 900, 136010, 2500)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0x1E, 1, 0, 25)
    SetChrPos(0x8, 18050, 0, 125300, 270)
    SetChrPos(0x9, 19860, 0, 123430, 270)
    SetChrPos(0xA, 18390, 0, 121930, 270)

    def lambda_AFE():
        OP_95(0xFE, 11210, 0, 134270, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AFE)

    def lambda_B18():
        OP_95(0xFE, 13320, 0, 132200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B18)

    def lambda_B32():
        OP_95(0xFE, 10820, 0, 130550, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B32)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 5)
    OP_93(0x8, 0x0, 0x1F4)
    OP_64(0x8)
    OP_63(0x8, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 5)
    OP_93(0x9, 0x0, 0x1F4)
    OP_64(0x9)
    OP_63(0x9, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0xA, 1)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 5)
    OP_93(0xA, 0x0, 0x1F4)
    OP_64(0xA)
    OP_63(0xA, 0xFFFFFD44, 2100, 0x28, 0x2B, 0x64, 0x0)
    EndChrThread(0x1E, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#1200824V#11PGrrrrr!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200825V#11PWoof woof!\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    EndChrThread(0x8, 0x0)

    def lambda_C2C():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C2C)
    Sleep(250)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(500)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)

    def lambda_C76():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C76)

    def lambda_C8F():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C8F)
    Sleep(250)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2E)
    SetChrSubChip(0xA, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x12,
        "#1200826V#5PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200827V#5PWhy are you mutts back here\x01",
            "so soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200828V#5PI'm pretty sure we ordered you to\x01",
            "tear those townspeople to shreds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200829V#5PWhat's the matter with you?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 20720, 0, 128080, 270)
    SetChrPos(0x102, 20490, 0, 126430, 270)
    SetChrPos(0x103, 22480, 0, 127490, 270)
    SetChrPos(0x104, 22610, 0, 125580, 270)
    Sleep(300)
    Sound(1090, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1200830V#1PFreeze!\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)
    Sleep(50)
    TurnDirection(0x13, 0x101, 500)
    Fade(500)
    OP_68(12890, 0, 137590, 0)
    MoveCamera(330, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28010, 0)
    SetCameraDistance(26010, 2000)

    def lambda_EB8():
        OP_95(0xFE, 17030, 0, 132160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB8)

    def lambda_ED2():
        OP_95(0xFE, 16490, 0, 130310, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED2)

    def lambda_EEC():
        OP_95(0xFE, 19410, 0, 131940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EEC)

    def lambda_F06():
        OP_95(0xFE, 18620, 0, 129940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F06)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x13B, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x1F4)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x12,
        "#1200831V#5PWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200832V#11PWho the hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200833V#0013F#6PCrossbell Police Department,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200834V#0101F#6PYou're with Revache & Co. aren't you?\x02\x03",
            "#1200835VYou're under arrest on the charges\x01",
            "of property damage and assault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200836V#5PThe cops are here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200837V#11PHow'd they find us in a place like this?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#1200838V#5PThe Special Support Section, eh?\x01",
            "You're the guys who took down\x01",
            "Fabio and his men, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200839V#11PThese are the runts that messed up our\x01",
            "plans in the Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200840V#0302F#12PHow cute. They remembered us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200841V#0204F#12PShould I feel honored? Because honestly,\x01",
            "I could not care less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200842V#5PWell, not like it matters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200843V#5PWe gotta teach these junior detectives\x01",
            "a lesson.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#1200844V#11PYou took real good care of our friends, so it's\x01",
            "only natural for us to return the favor, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200845V#11PLooks like you dealt with our war hounds, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200846V#5PPerfect. We'll have you on your knees\x01",
            "begging for mercy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200847V#0013F#6PYou're resisting arrest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200848V#11PHahaha! Obviously, ya moron!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x8, 500)

    ChrTalk(
        0x12,
        "#1200849V#5PGet ready, 'cause it's clobberin' time!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_A1(0x12, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    PlayEffect(0x1, 0xFF, 0x12, 0x40, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(590, 0, 100, 0)
    OP_68(12020, 0, 137490, 1000)
    OP_A1(0x12, 0x3E8, 0x2, 0x3, 0x4)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0x8, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x9, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x12, 0x102, 500)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)

    def lambda_15F9():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15F9)

    def lambda_1612():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1612)

    def lambda_162B():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_162B)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 5)
    BeginChrThread(0xA, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)

    def lambda_16A4():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16A4)

    def lambda_16B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16B1)
    Sleep(100)

    def lambda_16C1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16C1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)

    def lambda_16DA():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16DA)

    def lambda_16E7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16E7)
    Sleep(100)

    def lambda_16F7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16F7)

    def lambda_1704():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1704)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1200850V#0010F#11PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200851V#0310F#12PCrap! They brought meds?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200852V#11PHahaha... You seriously think pros like\x01",
            "ourselves wouldn't come prepared?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x708)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x12,
        "#1200853V#5PSic 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200854V#5PYeah! Rip out their throats!\x02",
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x8,
        "#1200855V#5PGrrrrrr...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200856V#5PWoof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200857V#0101F#6PHere they come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200858V#0007F#2PDon't hold back!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetCameraDistance(24010, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    Call(0, 6)
    Return()

    # Function_3_6AB end

    def Function_4_1943(): pass

    label("Function_4_1943")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_194E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1969")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_194E")

    label("loc_1969")

    Return()

    # Function_4_1943 end

    def Function_5_196A(): pass

    label("Function_5_196A")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1975")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1993")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_1975")

    label("loc_1993")

    Return()

    # Function_5_196A end

    def Function_6_1994(): pass

    label("Function_6_1994")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31053.itc", 0x29)
    LoadChrToIndex("chr/ch31100.itc", 0x2A)
    LoadChrToIndex("chr/ch31150.itc", 0x2B)
    LoadChrToIndex("chr/ch31153.itc", 0x2C)
    LoadChrToIndex("chr/ch09500.itc", 0x2D)
    LoadChrToIndex("chr/ch02400.itc", 0x2E)
    LoadChrToIndex("chr/ch02600.itc", 0x2F)
    LoadChrToIndex("monster/ch75650.itc", 0x30)
    LoadChrToIndex("monster/ch75651.itc", 0x31)
    LoadChrToIndex("chr/ch02650.itc", 0x33)
    LoadChrToIndex("chr/ch02651.itc", 0x34)
    LoadChrToIndex("apl/ch50112.itc", 0x35)
    LoadChrToIndex("apl/ch50118.itc", 0x36)
    LoadChrToIndex("chr/ch02656.itc", 0x37)
    LoadChrToIndex("apl/ch50113.itc", 0x38)
    LoadChrToIndex("apl/ch50115.itc", 0x39)
    LoadChrToIndex("apl/ch50121.itc", 0x3A)
    LoadChrToIndex("chr/ch02602.itc", 0x3B)
    LoadChrToIndex("apl/ch50125.itc", 0x3C)
    OP_68(10560, 800, 129789, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17770, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 11220, 0, 132770, 0)
    SetChrPos(0x102, 10050, 0, 131260, 0)
    SetChrPos(0x103, 12170, 0, 131370, 0)
    SetChrPos(0x104, 10840, 0, 130060, 0)
    SetChrChipByIndex(0x8, 0x3A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x3A)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x30)
    SetChrSubChip(0xC, 0x1)
    SetChrChipByIndex(0xD, 0x30)
    SetChrSubChip(0xD, 0x1)
    SetChrChipByIndex(0xE, 0x30)
    SetChrSubChip(0xE, 0x1)
    SetChrChipByIndex(0xF, 0x30)
    SetChrSubChip(0xF, 0x1)
    SetChrChipByIndex(0x10, 0x30)
    SetChrSubChip(0x10, 0x1)
    SetChrChipByIndex(0x11, 0x30)
    SetChrSubChip(0x11, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 4250, 0, 130520, 90)
    SetChrPos(0x9, 5870, 0, 127000, 45)
    SetChrPos(0xA, 8119, 0, 123880, 0)
    SetChrPos(0xB, 13090, 0, 125630, 315)
    SetChrPos(0xC, 10600, 0, 142410, 180)
    SetChrPos(0xD, 9510, 0, 137200, 180)
    SetChrPos(0xE, 5740, 0, 137380, 180)
    SetChrPos(0xF, 17670, 0, 134980, 225)
    SetChrPos(0x10, 18840, 0, 132120, 270)
    SetChrPos(0x11, 18070, 0, 129470, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 9840, 0, 136620, 180)
    SetChrPos(0x12, 11740, 0, 135960, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    OP_78(0x0, 0x1D)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, 18850, 0, 138470, 0)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x35)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x35)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x35)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x1A, 0x20)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, -53820, 16000, 120750, 90)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -60750, 16000, 122310, 0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_68(11640, 800, 134270, 3000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_386F")

    ChrTalk(
        0x101,
        "#1200859V#0010F#2P*huff* *puff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200860V#0106F#12PI-It's a good thing we didn't\x01",
            "take them lightly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200861V#0208F#2PI cannot believe they are able to control\x01",
            "those war hounds in such a manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200862V#0301F#4PThey aren't some two-bit mobsters,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200863V#5PIs this for real?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200864V#1PHow the hell'd we get taken down\x01",
            "by a bunch of kids?!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(100)
    SetCameraDistance(16000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#1200865V#0003F#12PResistance is futile.\x02\x03",
            "#1200866V#0001FWe'll be handing you over to the CGF\x01",
            "first thing in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200867V#0304F#4PBut for tonight, we're gonna chuck\x01",
            "you boys in the warehouse.\x02\x03",
            "#1200868V#0300FOh, don't worry. We'll be keepin' watch.\x01",
            "See what happens if you try to pull anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200869V#5PHehehe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200870V#1PHahaha!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2B)
    SetChrSubChip(0x13, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(100)
    OP_68(13470, 300, 138160, 1500)
    MoveCamera(45, 16, 0, 1500)
    SetCameraDistance(20970, 1500)
    OP_93(0x12, 0xE1, 0x0)

    def lambda_2592():
        OP_9D(0xFE, 0x3692, 0x0, 0x21CDC, 0x258, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2592)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_93(0x13, 0xE1, 0x0)

    def lambda_25BF():
        OP_9D(0xFE, 0x303E, 0x0, 0x22132, 0x320, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_25BF)
    Sound(820, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_93(0x12, 0xB4, 0x0)
    WaitChrThread(0x13, 1)
    OP_93(0x13, 0xB4, 0x0)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#1200871V#0007F#6PDon't try to run!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200872V#0307FYou ain't gettin' away!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200873V#5POh, don't get the wrong idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200874V#1PSure, you may have caught us off guard,\x01",
            "but we still have a trick up our sleeves!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_68(15600, 600, 138500, 1500)
    SetCameraDistance(19000, 1500)
    OP_93(0x12, 0x5A, 0x1F4)
    OP_71(0x0, 0xF1, 0x10E, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_6F(0x79)
    OP_79(0x0)
    Sound(836, 0, 100, 0)
    OP_93(0x12, 0xB4, 0x0)

    def lambda_2742():
        OP_9D(0xFE, 0x3638, 0x0, 0x220E2, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2742)
    WaitChrThread(0x12, 1)
    Sound(42, 0, 100, 0)
    OP_93(0x12, 0xB4, 0x1F4)
    OP_68(14860, 600, 136990, 6000)
    MoveCamera(55, 16, 0, 6000)
    SetCameraDistance(24270, 6000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    BeginChrThread(0xE, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0xF, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 18)
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
    Sleep(350)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 22)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#1200875V#0205F#11P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200876V#0105F#11PThere were more?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200877V#0301F#11PThis ain't lookin' good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_2934():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2934)
    Sleep(50)

    def lambda_294C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_294C)
    Sleep(100)

    def lambda_2964():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2964)
    Sleep(50)

    def lambda_297C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_297C)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)

    def lambda_299D():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_299D)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_29B6():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29B6)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)

    def lambda_29CF():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29CF)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_29E8():
        OP_93(0xFE, 0xB4, 0x2EE)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29E8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_68(11630, 600, 132400, 1000)
    SetCameraDistance(23060, 1000)
    OP_6F(0x79)

    def lambda_2A2D():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2A2D)

    def lambda_2A46():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A46)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x1)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 5)
    SetChrChipByIndex(0xB, 0x30)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x9, 2)
    WaitChrThread(0xB, 2)

    def lambda_2AA2():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2AA2)

    def lambda_2ABB():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2ABB)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 5)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 5)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x101,
        "#1200878V#0013F#5POh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200879V#0310F#5PI don't like dogs nearly enough to play\x01",
            "with ten of 'em at the same time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200880V#5PHahaha! How's it feel to have\x01",
            "the tables turned?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200881V#1PWe're gonna pay you back double\x01",
            "for making us look like chumps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#1200882V#1PI'm going to enjoy taking my sweet time\x01",
            "torturing you brats...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200883V#0010F#5PWe'll see about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200884V#0108F#5PThis doesn't look good, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200885V#0206F#5PSituation: critical.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x104,
        "#1200886V#0308F#5P#30W(Damn... Guess I gotta bust it out...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#1200887V#1PYou punks say your prayers yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200888V#5PLet's get this party st--\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(842, 0, 100, 0)
    Sleep(1500)
    CancelBlur(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200889V#0005F#5PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#1200890V#5PWhat's going on?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x15, -6820, 4000, 146610, 180)
    SetChrPos(0x16, -2980, 4000, 147620, 180)
    SetChrPos(0x17, 6510, 6000, 145910, 180)
    SetChrPos(0x18, 13520, 6000, 144820, 180)
    SetChrPos(0x19, 17340, 6000, 141120, 225)
    SetChrPos(0x1A, 20260, 6000, 137750, 225)
    SetChrPos(0x14, 12860, 10000, 152980, 180)
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 0, 0, 8)
    BeginChrThread(0x16, 0, 0, 8)
    BeginChrThread(0x17, 0, 0, 8)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 8)
    BeginChrThread(0x1A, 0, 0, 8)
    BeginChrThread(0x14, 0, 0, 9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    Fade(1000)
    OP_68(250, 5000, 151050, 0)
    MoveCamera(25, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21730, 0)
    OP_68(20200, 5000, 141800, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(20800, 7900, 150250, 0)
    MoveCamera(65, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31530, 0)
    OP_68(22960, 7900, 157520, 2500)
    SetCameraDistance(29530, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sound(2047, 255, 100, 0)
    SetChrName("White Wolf")

    AnonymousTalk(
        0xFF,
        "#1200891V#1PGrrrrr...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetCameraDistance(27530, 1000)
    OP_6F(0x10)
    EndChrThread(0x14, 0x0)
    BeginChrThread(0x14, 0, 0, 11)
    Sound(846, 0, 100, 0)
    Sound(842, 0, 100, 0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    BeginChrThread(0x15, 0, 0, 14)
    BeginChrThread(0x16, 0, 0, 14)
    BeginChrThread(0x17, 0, 0, 14)
    BeginChrThread(0x18, 0, 0, 14)
    BeginChrThread(0x19, 0, 0, 14)
    BeginChrThread(0x1A, 0, 0, 14)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_68(1790, 7900, 135730, 750)
    SetCameraDistance(40740, 750)
    OP_6F(0x79)
    Sleep(1000)
    CancelBlur(500)
    Sleep(2000)
    Fade(1000)
    OP_68(11630, 600, 132400, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18690, 0)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x0, 0x0)
    SetChrPos(0x103, 11900, 0, 131330, 0)
    OP_93(0x104, 0x0, 0x0)
    SetCameraDistance(23060, 3000)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    Sleep(1000)
    SetCameraDistance(23060, 1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 7)
    BeginChrThread(0x9, 3, 0, 7)
    BeginChrThread(0xA, 3, 0, 7)
    BeginChrThread(0xB, 3, 0, 7)
    BeginChrThread(0xC, 3, 0, 7)
    BeginChrThread(0xD, 3, 0, 7)
    BeginChrThread(0xE, 3, 0, 7)
    BeginChrThread(0xF, 3, 0, 7)
    BeginChrThread(0x10, 3, 0, 7)
    BeginChrThread(0x11, 3, 0, 7)
    Sound(847, 0, 100, 0)
    Sound(514, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(1500)

    ChrTalk(
        0x103,
        "#1200892V#0205F#12PHim!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200893V#0105F#6PThe white wolf!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200894V#0309F#12PNice, he even brought backup.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x13,
        "#1200895V#1PWhat are you mutts scared for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200896V#5PThey're totally outnumbered, so\x01",
            "quit cowering!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#1200897V#5PStop hiding your tails between\x01",
            "your legs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200898V#0004F#6PThis is the difference between the\x01",
            "real deal and your fakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200899V#0302F#12PNo kiddin'. No way in hell I'd ever\x01",
            "pit a dog against a wolf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200900V#0204F#12PThey seem to be angry at the mafiosos\x01",
            "for having smeared their good name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200901V#0102F#6PHave they come for retribution, then?\x02",
    )

    CloseMessageWindow()
    OP_68(14080, 600, 137980, 2000)
    SetCameraDistance(18740, 2000)

    def lambda_36EC():
        OP_96(0xFE, 0x3372, 0x0, 0x21250, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36EC)
    Sleep(50)

    def lambda_3709():
        OP_95(0xFE, 11270, 0, 135430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3709)
    Sleep(100)

    def lambda_3726():
        OP_95(0xFE, 13600, 0, 133690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3726)
    Sleep(50)

    def lambda_3743():
        OP_95(0xFE, 11770, 0, 132800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3743)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x12,
        "#1200902V#5PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200903V#0003F#12PGive it up. It's over.\x02\x03",
            "#1200904V#0001FYou're under arrest on the charges of\x01",
            "property damage and assault, as well\x01",
            "as resisting arrest.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_386F")

    SetChrPos(0x101, 16970, 0, 135400, 180)
    SetChrPos(0x102, 19260, 0, 134710, 225)
    SetChrPos(0x12, 16800, 0, 133770, 180)
    SetChrPos(0x13, 18090, 0, 133340, 180)
    SetChrPos(0x104, 14260, 0, 140550, 180)
    SetChrPos(0x103, 10960, 0, 134320, 45)
    SetChrPos(0x8, 12970, 0, 138000, 90)
    SetChrPos(0x9, 10320, 0, 137530, 90)
    SetChrPos(0xA, 7500, 0, 135860, 45)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x10E, 0x10E, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x101, 0, 0, 23)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x103, 0, 0, 23)
    BeginChrThread(0x104, 0, 0, 23)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x3B)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 12)
    SetChrChipByIndex(0x15, 0x3C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x3C)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x3C)
    SetChrSubChip(0x17, 0x0)
    Sleep(100)
    BeginChrThread(0x15, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x17, 0, 0, 12)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x14, 13600, 10000, 151880, 180)
    SetChrPos(0x15, 12200, 10000, 154210, 180)
    SetChrPos(0x16, 15510, 10000, 154290, 180)
    SetChrPos(0x17, 13670, 10000, 156770, 180)
    FadeToBright(1000, 0)
    OP_68(-700, 8100, 125760, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12620, 0)
    OP_68(12620, 11400, 151020, 12000)
    SetCameraDistance(14540, 12000)
    OP_6F(0x11)
    OP_0D()
    Sleep(500)
    EndChrThread(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(500)
    Sound(2053, 255, 90, 0)
    BeginChrThread(0x14, 3, 0, 11)
    WaitChrThread(0x14, 3)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1E, 1, 0, 24)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x15, 0x10E, 0x1F4)
    BeginChrThread(0x15, 0, 0, 13)

    def lambda_3BE7():
        OP_95(0xFE, -1110, 9450, 159020, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3BE7)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x36)
    SetChrSubChip(0x16, 0x0)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x16, 0x10E, 0x1F4)
    BeginChrThread(0x16, 0, 0, 13)

    def lambda_3C24():
        OP_95(0xFE, 1170, 10000, 158500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3C24)
    Sleep(200)
    SetChrChipByIndex(0x17, 0x36)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x17, 0x10E, 0x1F4)
    BeginChrThread(0x17, 0, 0, 13)

    def lambda_3C61():
        OP_95(0xFE, 320, 10000, 160370, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C61)

    def lambda_3C7B():

        label("loc_3C7B")

        TurnDirection(0xFE, 0x15, 100)
        Yield()
        Jump("loc_3C7B")

    QueueWorkItem2(0x14, 3, lambda_3C7B)
    WaitChrThread(0x15, 1)
    EndChrThread(0x15, 0x0)
    SetChrChipByIndex(0x15, 0x35)
    SetChrSubChip(0x15, 0x0)
    WaitChrThread(0x16, 1)
    EndChrThread(0x16, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x1E, 0x1)
    WaitChrThread(0x17, 1)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x35)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x14, 0x3)
    OP_68(10390, 11400, 152400, 4000)
    MoveCamera(45, 13, 0, 4000)

    def lambda_3CE1():
        OP_95(0xFE, 11000, 10000, 153000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3CE1)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x14, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_93(0x14, 0x10E, 0x1F4)
    SetChrChipByIndex(0x14, 0x3B)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 12)
    Sleep(1000)

    NpcTalk(
        0x14,
        "White Wolf",
        "#1200905V#5412F#11P...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x14, 0x0)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_93(0x14, 0x13B, 0x12C)
    Sleep(300)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(19880, 2000)
    BeginChrThread(0x1E, 1, 0, 24)
    BeginChrThread(0x14, 0, 0, 10)
    OP_95(0x14, 1170, 10000, 158500, 7000, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x1E, 0x1)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_6F(0x10)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    OP_68(-43190, 16000, 121730, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22050, 0)
    OP_68(-49650, 16000, 122160, 5000)
    OP_6F(0x1)
    OP_0D()

    NpcTalk(
        0x1B,
        "Girl in Dress",
        "#1200906V#5PHeehee, so I've been caught, have I?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1B,
        (
            "#1200907V#1PThat little wolf has some impressive senses.\x01",
            "It's clear he's not just some regular old animal.\x02\x03",
            "#1200908VAnd those four... They really didn't\x01",
            "think this through, did they?\x02\x03",
            "#1200909VI would have probably gotten to hear their\x01",
            "blood-curdling screams right about now,\x01",
            "had the wolves not saved them.\x02\x03",
            "#1200910VA tumultuous road lies ahead of them.\x02",
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

    NpcTalk(
        0x1C,
        "Man's Voice",
        "#1200911V#2PTo be fair, they're only beginners.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#1200912V#3305F#5POh, my.\x02",
    )

    CloseMessageWindow()
    OP_68(-51770, 16000, 123370, 4000)

    def lambda_4119():
        OP_95(0xFE, -54170, 16000, 122860, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4119)
    WaitChrThread(0x1C, 1)
    OP_6F(0x1)
    SetCameraDistance(21050, 80000)
    Sleep(300)

    ChrTalk(
        0x1B,
        (
            "#1200913V#3304F#6PAre you here to enjoy the show as well?\x02\x03",
            "#1200914VOr were you waiting to make your heroic\x01",
            "entrance once they realized they were in\x01",
            "over their heads?\x02\x03",
            "#1200915V#3302FAm I right...Arios MacLaine? Or would you\x01",
            "prefer the Divine Blade of Wind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#1200916V#1403F#5P...I could say the same to you.\x02\x03",
            "#1200917V#1401FEnforcer No. XV of the Society of Ouroboros...\x02\x03",
            "#1200918V...the Angel of Slaughter, Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1200919V#3309F#6POh, you know me? I suppose I'll\x01",
            "spare you the introduction, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 400)
    Sleep(300)

    ChrTalk(
        0x1B,
        (
            "#1200920V#3302F#12PYou're everything I could expect from a bracer\x01",
            "who declined a promotion to S-rank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#1200921V#1403F#5PIt's honestly much more than I deserve.\x02\x03",
            "#1200922VThe expectations to become Cassius Bright's\x01",
            "successor were also too much for me to bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1200923V#3302F#12PReally, now?\x02\x03",
            "#1200924V#3304FI've only had the pleasure of\x01",
            "meeting Cassius Bright once...\x02\x03",
            "#1200925V...but I'm almost positive your\x01",
            "swordsmanship surpasses his.\x02\x03",
            "#1200926V#3300FYou might even be on par with the\x01",
            "strongest person I've ever known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#1200927V#1404F#5PHaha... Should I take that as a compliment?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 400)
    Sleep(500)

    ChrTalk(
        0x1C,
        (
            "#1200928V#1401F#5PI've found out that you've been staying\x01",
            "here in Crossbell these past few months.\x02\x03",
            "#1200929VI was convinced you were planning another\x01",
            "one of your tea parties at first.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0x1B,
        (
            "#1200930V#3304F#6PDon't be so quick to jump to conclusions.\x02\x03",
            "#1200931VCrossbell is plenty stimulating regardless\x01",
            "of whether I hold a tea party or not.\x02\x03",
            "#1200932V#3302FIt would be uncouth of me to start my own\x01",
            "entertainment in addition to everything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#1200933V#1403F#5PThat's reassuring to hear, at least.\x02\x03",
            "#1200934VI suppose you've come to Crossbell\x01",
            "for personal reasons, then.\x02\x03",
            "#1200935V#1400FAnswer this one question, if you will.\x01",
            "How much longer will you continue to\x01",
            "run away from them?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1B,
        "#1200936V#3308F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#1200937V#1403F#5PWell, it's not my place to interfere with\x01",
            "your fate.\x02\x03",
            "#1200938VI cannot deny that having them at the Crossbell\x01",
            "branch has been helpful.\x02\x03",
            "#1200939V#1400FHowever... You understand you cannot continue\x01",
            "running away from the answer that awaits, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1200940V#3306F#6P...Leave me alone.\x02\x03",
            "#1200941V#3300FI have plenty of reasons other than\x01",
            "Estelle and Joshua to be in Crossbell.\x02\x03",
            "#1200942VI'm getting him repaired, and...there's\x01",
            "something I need to find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#1200943V#1405F#5POh? And what exactly would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#1200944V#3304F#6PWouldn't you like to know?\x02\x03",
            "#1200945V#3302FI'll promise to be a good little girl, so\x01",
            "please leave me be.\x02\x03",
            "#1200946VAnd on that note... I presume you won't\x01",
            "be sharing any details with those two,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#1200947V#1404F#5PIndeed. You have nothing to worry about.\x02\x03",
            "#1200948V#1402FAs long as you leave this land be, I promise to\x01",
            "not interfere in your own personal matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#1200949V#3309F#6PThank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0x1B,
        (
            "#1200950V#3304F#5PNow, if you'll excuse me, I'll be taking my leave.\x02\x03",
            "#1200951V#3302FHave a wonderful evening, Mister Divine Blade.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x2)
    SetChrFlags(0x1B, 0x10)
    SetChrChipByIndex(0x1B, 0x39)
    SetChrSubChip(0x1B, 0x0)
    Sound(820, 0, 100, 0)
    OP_A1(0x1B, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    OP_A1(0x1B, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x2)
    ClearChrFlags(0x1B, 0x10)
    Sleep(200)

    def lambda_4D4F():

        label("loc_4D4F")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_4D4F")

    QueueWorkItem2(0x1C, 1, lambda_4D4F)
    OP_68(-51970, 16000, 121990, 5000)
    MoveCamera(68, 25, 0, 5000)
    SetCameraDistance(22500, 5000)

    def lambda_4D86():
        OP_96(0xFE, 0xFFFF1AA0, 0x3E80, 0x1B5B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4D86)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    EndChrThread(0x1C, 0x1)
    OP_6F(0x10)
    OP_63(0x1C, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1C)

    ChrTalk(
        0x1C,
        (
            "#1200952V#1403F#5PA lost kitten...\x02\x03",
            "#1200953VThe three of them will continue to wander\x01",
            "aimlessly with how things are going.\x02\x03",
            "#1200954V#1401FIf only there were a third party to create\x01",
            "an opportunity for them...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1C, 0x87, 0x190)
    Sleep(300)
    OP_63(0x1C, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1C)

    ChrTalk(
        0x1C,
        "#1200955V#1404F#5PHmph... But what are the odds of that?\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(22500, 2000)
    OP_6F(0x10)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(6000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
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
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    OP_D5(0x33)
    OP_D5(0x34)
    OP_D5(0x35)
    OP_D5(0x36)
    OP_D5(0x37)
    OP_D5(0x38)
    OP_D5(0x39)
    ClearMapObjFlags(0x1, 0x4)
    SetScenarioFlags(0x5C, 1)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1994 end

    def Function_7_5065(): pass

    label("Function_7_5065")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_507D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_507D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_5065 end

    def Function_8_5096(): pass

    label("Function_8_5096")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50BF")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_50A1")

    label("loc_50BF")

    Return()

    # Function_8_5096 end

    def Function_9_50C0(): pass

    label("Function_9_50C0")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50E9")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_50CB")

    label("loc_50E9")

    Return()

    # Function_9_50C0 end

    def Function_10_50EA(): pass

    label("Function_10_50EA")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5110")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_50F5")

    label("loc_5110")

    Return()

    # Function_10_50EA end

    def Function_11_5111(): pass

    label("Function_11_5111")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_11_5111 end

    def Function_12_512E(): pass

    label("Function_12_512E")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5139")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5157")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_5139")

    label("loc_5157")

    Return()

    # Function_12_512E end

    def Function_13_5158(): pass

    label("Function_13_5158")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5163")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517E")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_5163")

    label("loc_517E")

    Return()

    # Function_13_5158 end

    def Function_14_517F(): pass

    label("Function_14_517F")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_14_517F end

    def Function_15_519D(): pass

    label("Function_15_519D")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_51C1():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51C1)

    def lambda_51DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_51DB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_5201():
        OP_9D(0xFE, 0x2F08, 0x0, 0x219BC, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5201)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_15_519D end

    def Function_16_5229(): pass

    label("Function_16_5229")

    SetChrPos(0xFE, 17000, 450, 138450, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_524D():
        OP_95(0xFE, 15400, 450, 138450, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_524D)

    def lambda_5267():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5267)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_93(0xFE, 0xE1, 0x0)

    def lambda_5294():
        OP_9D(0xFE, 0x35AC, 0x0, 0x218AE, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5294)
    WaitChrThread(0xFE, 1)
    Sound(39, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_16_5229 end

    def Function_17_52BC(): pass

    label("Function_17_52BC")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_52CA():
        OP_95(0xFE, 8530, 0, 139830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52CA)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_17_52BC end

    def Function_18_52FD(): pass

    label("Function_18_52FD")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_530B():
        OP_95(0xFE, 8400, 0, 136320, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_530B)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_52FD end

    def Function_19_533E(): pass

    label("Function_19_533E")

    Call(0, 15)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_534C():
        OP_95(0xFE, 5740, 0, 137380, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_534C)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_533E end

    def Function_20_537F(): pass

    label("Function_20_537F")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_538D():
        OP_95(0xFE, 18070, 0, 129470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_538D)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_537F end

    def Function_21_53C0(): pass

    label("Function_21_53C0")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_53CE():
        OP_95(0xFE, 18840, 0, 132120, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53CE)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_53C0 end

    def Function_22_5401(): pass

    label("Function_22_5401")

    Call(0, 16)
    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_540F():
        OP_95(0xFE, 17670, 0, 134980, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_540F)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_22_5401 end

    def Function_23_5442(): pass

    label("Function_23_5442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5459")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("Function_23_5442")

    label("loc_5459")

    Return()

    # Function_23_5442 end

    def Function_24_545A(): pass

    label("Function_24_545A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5473")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_24_545A")

    label("loc_5473")

    Return()

    # Function_24_545A end

    def Function_25_5474(): pass

    label("Function_25_5474")

    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Return()

    # Function_25_5474 end

    SaveToFile()

Try(main)
