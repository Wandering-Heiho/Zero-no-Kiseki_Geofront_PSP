from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2099.bin",                # FileName
        "M2099",                    # MapName
        "M2099",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 1, 0, 2],
    )

    BuildStringList((
        "m2099",                  # 0
        "Boss 1",                 # 1
        "bm2099",                 # 2
        "bm2099",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 8, 14, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_114", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72201.dat", "ms72201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_158", 0x0052, 30, 6, 45, 0, 1, 0, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75100.dat", "ms74100.dat", "ms74100.dat", 0, 0, 0, "ms74100.dat", 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7405", "ed7403", "ATBonus_A4"),
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
        "monster/ch75150.itc",               # 10
        "monster/ch75150.itc",               # 11
        "monster/ch74150.itc",               # 12
        "monster/ch74150.itc",               # 13
        "monster/ch72250.itc",               # 14
        "monster/ch72250.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(49520,   -10,     1100,    0x185010E,    "BattleInfo_114", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 9,   49.52000045776367,     -0.009999999776482582, 0.25,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.190000057220459,    0.0012499999720603228, -0.0625,               1.0])

    DeclActor(-83500,  0,       -5000,   1200,    -83500,  1500,    -5000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 2, 1])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_343",          # 01, 1
        "Function_2_36D",          # 02, 2
        "Function_3_467",          # 03, 3
        "Function_4_567",          # 04, 4
        "Function_5_119E",         # 05, 5
        "Function_6_11C3",         # 06, 6
        "Function_7_11E0",         # 07, 7
        "Function_8_1219",         # 08, 8
        "Function_9_1626",         # 09, 9
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_342")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_324")

    label("loc_342")

    Return()

    # Function_0_324 end

    def Function_1_343(): pass

    label("Function_1_343")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D")
    Event(0, 4)

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_36C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 8)

    label("loc_36C")

    Return()

    # Function_1_343 end

    def Function_2_36D(): pass

    label("Function_2_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_37F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_38E")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_3EF")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_40E")
    SetMapObjFrame(0xFF, "model05_mark_2", 0x0, 0x1)

    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427")
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_43B")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x9, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_43B")

    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x9, 0x100)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466")
    Sound(129, 1, 100, 0)

    label("loc_466")

    Return()

    # Function_2_36D end

    def Function_3_467(): pass

    label("Function_3_467")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_54A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_566")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_566")

    Return()

    # Function_3_467 end

    def Function_4_567(): pass

    label("Function_4_567")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    LoadChrToIndex("monster/ch75150.itc", 0x23)
    LoadChrToIndex("monster/ch75150.itc", 0x24)
    LoadEffect(0x0, "event\\ev501_00.eff")
    SetChrPos(0x101, 13330, 0, 10, 90)
    SetChrPos(0x109, 12590, 0, 1200, 90)
    SetChrPos(0x103, 11580, 0, -830, 90)
    SetChrPos(0x104, 9960, 250, -1360, 90)
    SetChrPos(0x102, 10920, 0, 560, 90)

    def lambda_60E():
        OP_95(0xFE, 43330, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60E)
    Sleep(50)

    def lambda_62B():
        OP_95(0xFE, 42590, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62B)
    Sleep(50)

    def lambda_648():
        OP_95(0xFE, 41580, 0, -830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_648)
    Sleep(50)

    def lambda_665():
        OP_95(0xFE, 39960, 250, -1360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_665)
    Sleep(50)

    def lambda_682():
        OP_95(0xFE, 40920, 0, 560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_682)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 50000, -2500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 6)
    FadeToBright(1000, 0)
    OP_68(16390, 1850, 0, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17140, 0)
    OP_68(42880, 1850, 0, 12000)
    SetCameraDistance(25140, 12000)
    Sleep(9000)
    OP_0D()
    Fade(1000)
    OP_68(49940, 200, 0, 0)
    MoveCamera(90, 45, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29320, 0)
    OP_68(49940, -450, 0, 7000)
    MoveCamera(90, 16, 0, 7000)
    SetCameraDistance(26460, 7000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#0501F#6PThis place keeps getting stranger and stranger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F#12PYeeeeah. It's rubbin' me the\x01",
            "wrong way.\x02\x03",
            "#0301FWhy the hell is there a place\x01",
            "like this behind a chapel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008F#6PIt's not normal, that's for sure.\x02\x03",
            "These ruins are way too bizarre to have\x01",
            "belonged to the Septian Church...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F#6PI'm curious about the meaning of\x01",
            "that floor pattern there...\x02\x03",
            "It resembles an eye, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201F#12P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9CA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9CA)
    Sleep(50)

    def lambda_9DA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DA)
    Sleep(50)

    def lambda_9EA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9EA)
    Sleep(50)

    def lambda_9FA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9FA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        "#0005F#5PWhat's wrong, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0501F#5PDid you notice something?\x02",
    )

    CloseMessageWindow()
    OP_64(0x103)
    Sleep(800)

    ChrTalk(
        0x103,
        (
            "#0208F#12POdds are this place served as some sort\x01",
            "of ritual chamber.\x02\x03",
            "A horrid place, used to offer live sacrifices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0107F#6PS-Sacrifices?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F#12PYes... I imagine those dark, red stains on the\x01",
            "floor are from the victims' spilled blood.\x02\x03",
            "#0201FOf course, I would not know for sure without\x01",
            "a proper composition test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F#12PWell, this conversation sure got dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0013F#5PBut why would a place like this be behind\x01",
            "the ruins of an old church...?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(935, 0, 100, 0)
    Sleep(500)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_CDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CDC)
    Sleep(50)

    def lambda_CEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CEC)
    Sleep(50)

    def lambda_CFC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CFC)
    Sleep(50)

    def lambda_D0C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D0C)
    Sleep(50)

    def lambda_D1C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D1C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#0507F#6PAgain?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0007F#6PWhat are we up against this time?!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1500)
    OP_68(49940, 1150, 0, 1500)
    SetCameraDistance(16020, 1500)
    OP_6F(0x11)
    Fade(1000)
    SetCameraDistance(15520, 0)
    Sound(934, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    BeginChrThread(0x101, 3, 0, 5)
    OP_68(49940, 1550, 0, 2500)
    SetCameraDistance(12520, 2500)
    Sleep(1500)
    BeginChrThread(0x8, 3, 0, 7)
    OP_6F(0x79)
    Fade(2000)
    Sound(868, 0, 100, 0)
    WaitChrThread(0x8, 3)
    OP_0D()
    Sleep(1000)
    OP_68(49940, 550, 0, 1000)
    MoveCamera(90, 12, 0, 1000)
    SetCameraDistance(19480, 1000)
    OP_6F(0x79)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(47940, 550, 0, 1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F62():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F62)
    Sleep(50)

    def lambda_F7A():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F7A)
    Sleep(50)

    def lambda_F92():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F92)
    Sleep(50)

    def lambda_FAA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FAA)
    Sleep(50)

    def lambda_FC2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FC2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0007F#6PNo way, is that thing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0110F#6P#NA devil?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#0207F#12P#NPlease, be careful! I am detecting massive\x01",
            "amounts of spiritual energy from it!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#0310F#12P#NHey, I don't remember signin'\x01",
            "up to be a CPD exorcist!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#0507F#6PHere it comes!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15980, 500)
    OP_68(50940, 1050, 0, 500)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    Battle("BattleInfo_158", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 8)
    Return()

    # Function_4_567 end

    def Function_5_119E(): pass

    label("Function_5_119E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11C2")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_5_119E")

    label("loc_11C2")

    Return()

    # Function_5_119E end

    def Function_6_11C3(): pass

    label("Function_6_11C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DF")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_6_11C3")

    label("loc_11DF")

    Return()

    # Function_6_11C3 end

    def Function_7_11E0(): pass

    label("Function_7_11E0")

    ClearChrFlags(0xFE, 0x1)

    def lambda_11EA():
        OP_98(0xFE, 0x0, 0xAF0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EA)

    def lambda_1204():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1204)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_11E0 end

    def Function_8_1219(): pass

    label("Function_8_1219")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    OP_68(53090, 850, 0, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21650, 0)
    SetMapObjFrame(0xFF, "model05_mark_2", 0x0, 0x1)
    SetChrPos(0x101, 46890, 0, -70, 90)
    SetChrPos(0x109, 45620, 0, 1750, 90)
    SetChrPos(0x103, 45140, 0, -1890, 90)
    SetChrPos(0x102, 43000, 0, 620, 90)
    SetChrPos(0x104, 44170, 0, -680, 90)
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
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_68(53090, -450, 0, 3000)
    OP_6F(0x1)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#0006F#6P*pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0506F#6PWe managed to take it down...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
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
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#0106F#6P#NWh-What in Aidios' name was that?\x02\x03",
            "#0101FIt looked like a devil straight from\x01",
            "the church's Testaments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0206F#12PRegardless of its origin, it was\x01",
            "emitting a terrifying amount of\x01",
            "spiritual energy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F#12PGhosts, skeletons, monsters...\x01",
            "and now we're fightin' devils?\x02\x03",
            "#0301FThis place is messed up, man.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(61640, 1250, -50, 2000)
    MoveCamera(90, 16, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(26460, 2000)
    Sleep(2500)

    ChrTalk(
        0x101,
        (
            "#0001F#5PGiven our current position, I'm\x01",
            "pretty sure the bell's right above us.\x02\x03",
            "Let's take a look, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0501F#5PLet's...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 43000, 250, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 5)
    OP_29(0x49, 0x1, 0x3)
    Sleep(500)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_1219 end

    def Function_9_1626(): pass

    label("Function_9_1626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 1)), scpexpr(EXPR_END)), "loc_1630")
    Return()

    label("loc_1630")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1713"),
        (SWITCH_DEFAULT, "loc_172A"),
    )


    label("loc_1713")

    Sleep(500)
    OP_90(0x0, 44860, 250, -10, 270)
    EventEnd(0x5)
    Return()

    label("loc_172A")

    Battle("BattleInfo_114", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(44860, 1250, -10, 0)
    OP_90(0x0, 44860, 250, -10, 270)
    OP_90(0x1, 44860, 250, -10, 270)
    OP_90(0x2, 44860, 250, -10, 270)
    OP_90(0x3, 44860, 250, -10, 270)
    OP_90(0x4, 44860, 250, -10, 270)
    OP_90(0x5, 44860, 250, -10, 270)
    OP_90(0x6, 44860, 250, -10, 270)
    OP_90(0x7, 44860, 250, -10, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_17EC"),
        (1, "loc_17EF"),
        (SWITCH_DEFAULT, "loc_17F2"),
    )


    label("loc_17EC")

    EventEnd(0x5)
    Return()

    label("loc_17EF")

    OP_B7(0x0)
    Return()

    label("loc_17F2")

    FadeToDark(0, 0, -1)
    OP_68(49680, 1550, -270, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster in the Moon Temple!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xB, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_194E")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 49520, 250, 1990, 180)
    SetChrPos(0x102, 51420, 250, 610, 252)
    SetChrPos(0x103, 50700, 250, -1620, 324)
    SetChrPos(0x104, 48340, 250, -1620, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1938")
    SetChrPos(0x10A, 47620, 250, 610, 108)
    Jump("loc_1949")

    label("loc_1938")

    SetChrPos(0x109, 47620, 250, 610, 108)

    label("loc_1949")

    Jump("loc_1992")

    label("loc_194E")

    SetChrPos(0x101, 49520, 250, 2009, 180)
    SetChrPos(0x102, 51520, 250, -10, 270)
    SetChrPos(0x103, 49520, 250, -2009, 0)
    SetChrPos(0x104, 47520, 250, -10, 90)

    label("loc_1992")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E3")

    ChrTalk(
        0x101,
        "#5P#0005FA craft book? It looks pretty beat up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A1F")

    label("loc_19E3")


    ChrTalk(
        0x101,
        "#5P#0000FThis craft book looks as old as the last one.\x02",
    )

    CloseMessageWindow()

    label("loc_1A1F")


    ChrTalk(
        0x104,
        (
            "#6P#0303FLooks like it's about combinin' crafts\x01",
            "during battle.\x02\x03",
            "#0300FMademois-Elie and Tio Tot might get\x01",
            "a kick outta tryin' the stuff in here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#11P#0105FOh, we could probably use this.\x02\x03",
            "#0100FWant to give it a try, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0202FYes, we should test it out.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B8C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1B8C")

    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x14D)
    AddCraft(0x2, 0x14D)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio and Elie learned \x07\x02",
            "[Cold Gehenna]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x79, 1)
    SetScenarioFlags(0xD8, 7)
    OP_29(0x2B, 0x4, 0x10)
    OP_29(0x2B, 0x4, 0x2)
    OP_29(0x2B, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE(0x21, 0x0)
    EventEnd(0x5)
    Return()

    # Function_9_1626 end

    SaveToFile()

Try(main)
