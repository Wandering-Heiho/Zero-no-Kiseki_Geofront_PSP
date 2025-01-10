from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0113.bin",                # FileName
        "m0113",                    # MapName
        "m0113",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0113",                  # 0
        "Monster",                # 1
        "Monster",                # 2
        "Monster",                # 3
        "Monster",                # 4
        "Monster",                # 5
        "Monster",                # 6
        "bm0112",                 # 7
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 14, 13, 180)
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
        "BattleInfo_E4", 0x0052, 50, 6, 0, 0, 1, 0, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71800.dat", "ms73300.dat", "ms73300.dat", "ms73101.dat", "ms73101.dat", "ms73101.dat", "ms73101.dat", 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7405", "ed7403", "ATBonus_94"),
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
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   0.0,                   -7.5,                  0.0,                   81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.5,                   -0.0,                  1.0])

    DeclActor(2000,    0,       -200000, 1200,    2500,    1000,    -200000, 0x007C, 0,  8,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  10, 0x0000)
    DeclActor(2500,    0,       -87250,  1200,    2500,    1500,    -87250,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_340",          # 01, 1
        "Function_2_35F",          # 02, 2
        "Function_3_3A7",          # 03, 3
        "Function_4_685",          # 04, 4
        "Function_5_E82",          # 05, 5
        "Function_6_1256",         # 06, 6
        "Function_7_131F",         # 07, 7
        "Function_8_141F",         # 08, 8
        "Function_9_15A6",         # 09, 9
        "Function_10_16ED",        # 0A, 10
        "Function_11_1874",        # 0B, 11
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_324")

    label("loc_33F")

    Return()

    # Function_0_324 end

    def Function_1_340(): pass

    label("Function_1_340")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_340")

    label("loc_35E")

    Return()

    # Function_1_340 end

    def Function_2_35F(): pass

    label("Function_2_35F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_3A6")

    label("loc_38C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_3A6")

    Return()

    # Function_2_35F end

    def Function_3_3A7(): pass

    label("Function_3_3A7")

    SetMapObjFrame(0x3, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x4, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_610")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C5")
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off_kp")
    Jump("loc_610")

    label("loc_4C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_570")
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off_kp")
    OP_1B(0x1, 0x0, 0x6)
    Jump("loc_610")

    label("loc_570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_610")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFrame(0x6, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "on_kp")

    label("loc_610")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    Return()

    # Function_3_3A7 end

    def Function_4_685(): pass

    label("Function_4_685")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch71850.itc", 0x22)
    LoadChrToIndex("monster/ch73350.itc", 0x23)
    LoadChrToIndex("monster/ch73150.itc", 0x24)
    OP_68(0, 1500, -8000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 500, 0, -7500, 0)
    SetChrPos(0x102, -500, 0, -7750, 0)
    SetChrPos(0x103, 750, 0, -9000, 0)
    SetChrPos(0x104, -750, 0, -9250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 7000, 0, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 1, 0, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrChipByIndex(0xA, 0x23)
    SetChrChipByIndex(0xB, 0x24)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0x9, 3500, 0, -1500, 225)
    SetChrPos(0xA, -3500, 0, -1500, 135)
    SetChrPos(0xB, 2000, 7000, 2000, 225)
    SetChrPos(0xC, -2500, 7000, 2000, 135)
    SetChrPos(0xD, 0, 7000, -1500, 180)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0x9, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xA, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xB, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xC, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xD, 1, 0, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    def lambda_8CF():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CF)
    Sleep(50)

    def lambda_8EC():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EC)
    Sleep(50)

    def lambda_909():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_909)
    Sleep(50)

    def lambda_926():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_926)
    OP_68(0, 1500, -3000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_95F():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95F)
    WaitChrThread(0x102, 1)

    def lambda_970():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_970)
    WaitChrThread(0x103, 1)

    def lambda_981():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_981)
    WaitChrThread(0x104, 1)

    def lambda_992():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_992)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#0005FWhoa, it's like this place was\x01",
            "hit by a blizzard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0106FI-It's a bit too cold for my liking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FIf I were to guess, the monster\x01",
            "we're lookin' for is usin' this frozen\x01",
            "wasteland to its advantage...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#0201FThat is correct! Everyone, we should\x01",
            "be cautious.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B03():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B03)

    def lambda_B10():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B10)

    def lambda_B1D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B1D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#11P#0007FDefinitely!\x02",
    )

    CloseMessageWindow()
    OP_68(-450, 1300, -3140, 3000)
    MoveCamera(34, 20, 0, 3000)
    SetCameraDistance(24160, 3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    def lambda_B7E():
        OP_98(0x8, 0x0, 0xFFFFE4A8, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B7E)
    Sleep(500)
    Sound(862, 0, 100, 0)

    def lambda_BA1():
        OP_98(0x104, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA1)
    Sleep(50)

    def lambda_BBE():
        OP_98(0x103, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BBE)
    Sleep(50)

    def lambda_BDB():
        OP_98(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BDB)
    Sleep(50)

    def lambda_BF8():
        OP_98(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF8)
    WaitChrThread(0x104, 1)
    Fade(500)
    SetChrChipByIndex(0x104, 0x21)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x20)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x1F)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sound(202, 0, 100, 0)

    def lambda_C4E():
        OP_A7(0x9, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C4E)
    Sleep(50)

    def lambda_C62():
        OP_A7(0xA, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C62)
    Sleep(50)

    def lambda_C76():
        OP_98(0xB, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C76)
    Sleep(150)

    def lambda_C93():
        OP_98(0xC, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C93)
    Sleep(150)

    def lambda_CB0():
        OP_98(0xD, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_CB0)
    WaitChrThread(0x9, 2)

    def lambda_CCE():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CCE)
    WaitChrThread(0xA, 2)

    def lambda_CE3():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CE3)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)

    ChrTalk(
        0x102,
        "#6P#0105FWh-What IS this thing...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0307FEyes open, guys! This guy's\x01",
            "gonna be a tough customer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0007FEveryone, let's give it our all!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 200)
    BlurSwitch(0xC8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x32, 0x32, 0xC8, 0x7D0)

    def lambda_DD3():
        OP_95(0x9, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DD3)
    Sleep(5)

    def lambda_DF0():
        OP_95(0xA, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DF0)
    Sleep(5)

    def lambda_E0D():
        OP_95(0xB, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E0D)
    Sleep(5)

    def lambda_E2A():
        OP_95(0xC, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E2A)
    Sleep(5)

    def lambda_E47():
        OP_95(0xD, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_E47)
    Sleep(200)
    CancelBlur(0)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 5)
    Return()

    # Function_4_685 end

    def Function_5_E82(): pass

    label("Function_5_E82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1500, 0, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30500, 0)
    SetChrPos(0x101, 0, 0, 1000, 0)
    SetChrPos(0x102, 1000, 0, 0, 90)
    SetChrPos(0x103, -1000, 0, 0, 270)
    SetChrPos(0x104, 0, 0, -1000, 180)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
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
    SetCameraDistance(35500, 3000)
    MoveCamera(45, 28, 0, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off")
    Sleep(2000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, 0, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0005FEverything's back to normal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FDoes that mean the Geofront\x01",
            "abnormality is all cleared up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FWell, my teeth aren't chatterin'\x01",
            "anymore, so that's a good sign.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10F7():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F7)
    Sleep(50)

    def lambda_1107():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1107)
    Sleep(50)

    def lambda_1117():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1117)
    Sleep(50)

    def lambda_1127():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1127)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        (
            "#6P#0200FThere should be an elevator in here that\x01",
            "can take us back up to ground level.\x02\x03",
            "I say we check it and see if it is still\x01",
            "operational or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FYeah, we can take that if it still works\x01",
            "and report back to the client.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 0, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x1, 0x0, 0x6)
    OP_29(0x34, 0x1, 0x2)
    OP_DE(0x23, 0x0)
    EventEnd(0x5)
    Return()

    # Function_5_E82 end

    def Function_6_1256(): pass

    label("Function_6_1256")

    EventBegin(0x1)

    ChrTalk(
        0x103,
        (
            "#0200FIf we go back into the inner section of the\x01",
            "Geofront, there should be an elevator that\x01",
            "takes us back up to the ground level.\x02\x03",
            "That would be our most efficient exit.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -110, 0, -123480, 0)
    EventEnd(0x4)
    Return()

    # Function_6_1256 end

    def Function_7_131F(): pass

    label("Function_7_131F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1402")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x5, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x5, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_141E")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_141E")

    Return()

    # Function_7_131F end

    def Function_8_141F(): pass

    label("Function_8_141F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159E")
    Fade(500)
    SetChrPos(0x0, 600, 0, -199400, 90)
    SetChrPos(0x1, 600, 0, -200600, 90)
    SetChrPos(0x2, -600, 0, -200600, 90)
    SetChrPos(0x3, -600, 0, -199400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FE")
    SetChrPos(0x4, -1800, 0, -200600, 90)
    SetChrPos(0x5, -1800, 0, -199400, 90)
    Jump("loc_151D")

    label("loc_14FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_151D")
    SetChrPos(0x4, -1800, 0, -200000, 90)

    label("loc_151D")

    OP_68(0, 1000, -200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, 6000, -200000, 3000)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0112", 0, 0, 0)
    IdleLoop()

    label("loc_159E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_141F end

    def Function_9_15A6(): pass

    label("Function_9_15A6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(0, 11000, -200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -199400, 90)
    OP_90(0x1, 600, 30000, -200600, 90)
    OP_90(0x2, -600, 30000, -200600, 90)
    OP_90(0x3, -600, 30000, -199400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1679")
    OP_90(0x4, -1800, 30000, -200600, 90)
    OP_90(0x5, -1800, 30000, -199400, 90)
    Jump("loc_1698")

    label("loc_1679")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1698")
    OP_90(0x4, -1800, 30000, -200000, 90)

    label("loc_1698")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, -200000, 3000)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x3)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_15A6 end

    def Function_10_16ED(): pass

    label("Function_10_16ED")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186C")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CC")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_17EB")

    label("loc_17CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17EB")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_17EB")

    OP_68(0, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, 6000, 100000, 3000)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_186C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_16ED end

    def Function_11_1874(): pass

    label("Function_11_1874")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(0, 11000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 100600, 0)
    OP_90(0x1, -600, 30000, 100600, 0)
    OP_90(0x2, -600, 30000, 99400, 0)
    OP_90(0x3, 600, 30000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1947")
    OP_90(0x4, -600, 30000, 98200, 0)
    OP_90(0x5, 600, 30000, 98200, 0)
    Jump("loc_1966")

    label("loc_1947")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1966")
    OP_90(0x4, 0, 30000, 98200, 0)

    label("loc_1966")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 100000, 3000)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x4)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1874 end

    SaveToFile()

Try(main)
