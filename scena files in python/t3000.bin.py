from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3000.bin",                # FileName
        "t3000",                    # MapName
        "t3000",                    # Location
        0x005B,                     # MapIndex
        "ed7202",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3000",                  # 0
        "Renne",                  # 1
        "Estelle",                # 2
        "Joshua",                 # 3
        "Meister Joerg",          # 4
        "Monster",                # 5
        "Monster",                # 6
        "Monster",                # 7
        "Monster",                # 8
        "Monster",                # 9
        "Monster",                # 10
        "SE制御",                 # 11
        "bt3000",                 # 12
        "Mainz Mountain Path",    # 13
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 12, 9, 180)
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

    # event battle count: 2

    BattleInfo(
        "BattleInfo_E4", 0x0062, 32, 6, 0, 0, 1, 0, 0, "bt3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75400.dat", "ms75400.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7405", "ed7403", "ATBonus_94"),
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
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  2.0,                   26.5,                  0.0,                   225.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.3333333432674408,   -5.300000190734863,    -0.0,                  1.0])

    DeclActor(-7090,   0,       24320,   1200,    -7090,   2500,    24320,   0x007C, 0,  19, 0x0000)
    DeclActor(2070,    250,     26860,   1200,    2070,    1500,    26860,   0x007C, 0,  20, 0x0000)
    DeclActor(2000,    2500,    47300,   1200,    2000,    4000,    47300,   0x007C, 0,  21, 0x0000)

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "Mainz Mountain Path")

    ScpFunction((
        "Function_0_40C",          # 00, 0
        "Function_1_428",          # 01, 1
        "Function_2_445",          # 02, 2
        "Function_3_477",          # 03, 3
        "Function_4_4DE",          # 04, 4
        "Function_5_115B",         # 05, 5
        "Function_6_1180",         # 06, 6
        "Function_7_11A5",         # 07, 7
        "Function_8_11CA",         # 08, 8
        "Function_9_11EF",         # 09, 9
        "Function_10_18AD",        # 0A, 10
        "Function_11_1A1C",        # 0B, 11
        "Function_12_1A3E",        # 0C, 12
        "Function_13_1EA2",        # 0D, 13
        "Function_14_3DB5",        # 0E, 14
        "Function_15_42D6",        # 0F, 15
        "Function_16_641C",        # 10, 16
        "Function_17_730D",        # 11, 17
        "Function_18_7336",        # 12, 18
        "Function_19_7362",        # 13, 19
        "Function_20_73B8",        # 14, 20
        "Function_21_7444",        # 15, 21
    ))


    def Function_0_40C(): pass

    label("Function_0_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_427")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_40C")

    label("loc_427")

    Return()

    # Function_0_40C end

    def Function_1_428(): pass

    label("Function_1_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_444")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_428")

    label("loc_444")

    Return()

    # Function_1_428 end

    def Function_2_445(): pass

    label("Function_2_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_476")

    Return()

    # Function_2_445 end

    def Function_3_477(): pass

    label("Function_3_477")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49A")
    Jump("loc_4DD")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 4)), scpexpr(EXPR_END)), "loc_4B1")
    Jump("loc_4DD")

    label("loc_4B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4D0")
    ModifyEventFlags(1, 0, 0x80)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    Jump("loc_4DD")

    label("loc_4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4DD")

    label("loc_4DD")

    Return()

    # Function_3_477 end

    def Function_4_4DE(): pass

    label("Function_4_4DE")

    EventBegin(0x0)
    Fade(500)
    OP_68(17500, 600, 38730, 0)
    MoveCamera(49, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28710, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetMapObjFlags(0x0, 0x1000)
    OP_68(1770, 3090, 45860, 10000)
    MoveCamera(45, 14, 0, 10000)
    SetCameraDistance(59000, 10000)
    PlaceName2(100, 200, "c_plac16", 0x0, 5000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(2020, 1500, 25360, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17600, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0001FNo sign of anyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FHow odd. It sounded like Imelda was in contact\x01",
            "with someone here...\x02\x03",
            "#0100FRenne was staying here, too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FAlbeit faint, I detect a presence coming from\x01",
            "within the building.\x02\x03",
            "#0200FAs to whether it is human or not, I am not sure,\x01",
            "but it is definitely there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FYou really can't tell what it is, Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#12P#0303FHey, Lloyd.\x02\x03",
            "#0301FIf what Estelle and Joshua told us about that\x01",
            "society is legit, then...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D3():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D3)
    Sleep(50)

    def lambda_7E3():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E3)
    Sleep(50)

    def lambda_7F3():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        (
            "#5P#0006FYeah, I'm thinking the same thing.\x02\x03",
            "#0001FThis doll studio must be connected to it,\x01",
            "in some way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0303FBingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FI suppose that IS a possibility...\x02\x03",
            "#0108FHonestly, I didn't take them seriously at first,\x01",
            "given the absurdity of the story, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0201F...considering everything that happened with Renne,\x01",
            "there is no choice but to accept it as the truth.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "So that's what's going on here. You're\x01",
            "that young police squad Renne was\x01",
            "telling me about, hmm?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    Sleep(1000)
    Fade(500)
    MoveCamera(0, 27, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x101, 1, 0, 5)
    BeginChrThread(0x102, 1, 0, 6)
    BeginChrThread(0x103, 1, 0, 7)
    BeginChrThread(0x104, 1, 0, 8)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x101, 0x1)

    def lambda_B0D():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0D)
    EndChrThread(0x102, 0x1)

    def lambda_B1E():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1E)
    EndChrThread(0x103, 0x1)

    def lambda_B2F():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2F)
    EndChrThread(0x104, 0x1)

    def lambda_B40():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B40)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#5P#0005FWho's there?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105FWhere's that voice coming from?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You were sent here by Imelda, I presume.\x02\x03",
            "You're out of luck, though. My works aren't\x01",
            "mere second-rate antiques to be handled\x01",
            "and pawned off by a broker like her.\x02\x03",
            "Leave at once.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#5P#0008FSir, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FWell, when you put it like that,\x01",
            "what's a guy s'posed to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#0203FConsider me speechless.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm, still...\x02\x03",
            "I suppose you did make a long trek to\x01",
            "get here. Turning you away at the door\x01",
            "would no doubt be unsatisfactory.\x02\x03",
            "Besides, I owe you a debt for all you did\x01",
            "for Renne, so I'll give you one chance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#0105FA chance...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What I mean is that I'd like to test the\x01",
            "extent of your strength.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(809, 0, 100, 0)
    Sleep(600)

    def lambda_F0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F0C)
    Sleep(50)

    def lambda_F1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F1C)
    Sleep(50)

    def lambda_F2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F2C)
    Sleep(50)

    def lambda_F3C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F3C)
    Sleep(300)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is unlocked.\x02\x03",
            "If you so wish, open it and enter.\x02\x03",
            "However...are you prepared?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(35, 27, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_0D()
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#6P#0108FShould we go inside...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FFrom what he said, something's bound\x01",
            "to happen when we open that gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FDon't tell me he went and set a bunch\x01",
            "of booby traps for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0206FPerhaps it's something even nastier.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2000, 0, 25250, 0)
    ClearMapObjFlags(0x0, 0x1000)
    OP_29(0x30, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_4_4DE end

    def Function_5_115B(): pass

    label("Function_5_115B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_117F")
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    Jump("Function_5_115B")

    label("loc_117F")

    Return()

    # Function_5_115B end

    def Function_6_1180(): pass

    label("Function_6_1180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11A4")
    OP_93(0x102, 0xE1, 0x1C2)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x1C2)
    Sleep(500)
    Jump("Function_6_1180")

    label("loc_11A4")

    Return()

    # Function_6_1180 end

    def Function_7_11A5(): pass

    label("Function_7_11A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11C9")
    OP_93(0x103, 0x87, 0x1C2)
    Sleep(550)
    OP_93(0x103, 0x2D, 0x1C2)
    Sleep(550)
    Jump("Function_7_11A5")

    label("loc_11C9")

    Return()

    # Function_7_11A5 end

    def Function_8_11CA(): pass

    label("Function_8_11CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11EE")
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(450)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(450)
    Jump("Function_8_11CA")

    label("loc_11EE")

    Return()

    # Function_8_11CA end

    def Function_9_11EF(): pass

    label("Function_9_11EF")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Open the gate.\x01",      # 0
            "Turn away.\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123B")
    Return()

    label("loc_123B")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("monster/ch76352.itc", 0x24)
    OP_68(2000, 1500, 25500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 5000, 33250, 45)
    SetChrPos(0xD, -1000, 5250, 37250, 135)
    SetChrPos(0xE, 5000, 5500, 33250, 315)
    SetChrPos(0xF, 5000, 5750, 37250, 225)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 28750, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)

    def lambda_149D():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149D)
    Sleep(50)

    def lambda_14BA():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BA)
    Sleep(50)

    def lambda_14D7():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14D7)
    Sleep(50)

    def lambda_14F4():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14F4)
    OP_68(2000, 1500, 34500, 5000)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#12P#0207FEveryone!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    WaitChrThread(0x101, 1)

    def lambda_1571():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1571)
    WaitChrThread(0x102, 1)

    def lambda_1582():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1582)
    WaitChrThread(0x104, 1)

    def lambda_1593():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1593)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(320, 1500, 37700, 0)
    MoveCamera(269, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18870, 0)
    Sleep(500)
    BeginChrThread(0x12, 1, 0, 11)
    Sleep(1000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 10)
    OP_68(1060, 1500, 34190, 7000)
    MoveCamera(53, 30, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(20000, 7000)

    def lambda_166A():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_166A)
    WaitChrThread(0x103, 1)

    def lambda_1688():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1688)

    def lambda_1695():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1695)

    def lambda_16A2():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16A2)

    def lambda_16AF():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16AF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    WaitChrThread(0xB, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#11P#0007FLook out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0107FA-Are those...angels?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0310FFor real, old man?! This is your freakin' test?!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 8000)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)

    ChrTalk(
        0x101,
        "#11P#0010FBrace yourselves!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0307FThey're chargin'!\x02",
    )

    CloseMessageWindow()
    Fade(200)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    Sleep(400)
    CancelBlur(0)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 13)
    Return()

    # Function_9_11EF end

    def Function_10_18AD(): pass

    label("Function_10_18AD")


    def lambda_18B2():
        OP_97(0xC, 0x0, 0xFFFFEC78, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_18B2)

    def lambda_18CC():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_18CC)
    Sleep(50)

    def lambda_18E0():
        OP_97(0xD, 0x0, 0xFFFFEB7E, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_18E0)

    def lambda_18FA():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_18FA)
    Sleep(50)

    def lambda_190E():
        OP_97(0xE, 0x0, 0xFFFFEA84, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_190E)

    def lambda_1928():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_1928)
    Sleep(50)

    def lambda_193C():
        OP_97(0xF, 0x0, 0xFFFFE98A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_193C)

    def lambda_1956():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_1956)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xF, 3)
    Sound(868, 0, 100, 0)

    def lambda_198D():
        OP_97(0x10, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_198D)

    def lambda_19A7():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_19A7)
    Sleep(50)

    def lambda_19BB():
        OP_97(0x11, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_19BB)

    def lambda_19D5():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_19D5)
    WaitChrThread(0x10, 3)

    def lambda_19EA():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_19EA)
    WaitChrThread(0x11, 3)

    def lambda_19FF():
        OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_19FF)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x11, 3)
    Return()

    # Function_10_18AD end

    def Function_11_1A1C(): pass

    label("Function_11_1A1C")

    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Return()

    # Function_11_1A1C end

    def Function_12_1A3E(): pass

    label("Function_12_1A3E")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Open the door.\x01",      # 0
            "Turn away.\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8A")
    Return()

    label("loc_1A8A")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("monster/ch76352.itc", 0x24)
    OP_68(2000, 1500, 25500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 5000, 33250, 45)
    SetChrPos(0xD, -1000, 5250, 37250, 135)
    SetChrPos(0xE, 5000, 5500, 33250, 315)
    SetChrPos(0xF, 5000, 5750, 37250, 225)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 28750, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)

    def lambda_1CDB():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CDB)
    Sleep(50)

    def lambda_1CF8():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF8)
    Sleep(50)

    def lambda_1D15():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D15)
    Sleep(50)

    def lambda_1D32():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D32)
    OP_68(2000, 1500, 35500, 5000)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(1060, 1500, 34190, 6000)
    MoveCamera(53, 30, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(20000, 7000)
    BeginChrThread(0x12, 1, 0, 11)
    BeginChrThread(0xB, 1, 0, 10)

    def lambda_1D9E():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D9E)

    def lambda_1DAB():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DAB)

    def lambda_1DB8():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DB8)

    def lambda_1DC5():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DC5)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xB, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Fade(200)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    Sleep(400)
    CancelBlur(0)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 13)
    Return()

    # Function_12_1A3E end

    def Function_13_1EA2(): pass

    label("Function_13_1EA2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3748")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("chr/ch06600.itc", 0x24)
    LoadEffect(0x0, "event\\ev503_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    OP_68(1350, 1500, 34720, 0)
    MoveCamera(53, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16870, 0)
    SetCameraDistance(18870, 5000)
    SetChrPos(0x101, 2000, 0, 36250, 315)
    SetChrPos(0x102, 1000, 0, 35000, 225)
    SetChrPos(0x103, 3000, 0, 35500, 45)
    SetChrPos(0x104, 2000, 0, 34000, 135)
    SetChrPos(0xB, 2000, 2500, 46500, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 0, 33250, 45)
    SetChrPos(0xD, -1000, 0, 37250, 135)
    SetChrPos(0xE, 5000, 0, 33250, 315)
    SetChrPos(0xF, 5000, 0, 37250, 225)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 30750, 0)
    SetChrPos(0x11, 3000, 0, 39250, 180)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_2114():
        OP_A6(0xC, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2114)
    PlayEffect(0x0, 0x0, 0xC, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2167():
        OP_A6(0xD, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2167)
    PlayEffect(0x0, 0x1, 0xD, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_21BA():
        OP_A6(0xE, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_21BA)
    PlayEffect(0x0, 0x2, 0xE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_220D():
        OP_A6(0xF, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_220D)
    PlayEffect(0x0, 0x3, 0xF, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2260():
        OP_A6(0x10, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2260)
    PlayEffect(0x0, 0x4, 0x10, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_22B3():
        OP_A6(0x11, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_22B3)
    PlayEffect(0x0, 0x5, 0x11, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(868, 0, 100, 0)

    def lambda_2313():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2313)
    Sleep(50)

    def lambda_2327():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2327)
    Sleep(50)

    def lambda_233B():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_233B)
    Sleep(50)

    def lambda_234F():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_234F)
    Sleep(50)

    def lambda_2363():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2363)
    Sleep(50)

    def lambda_2377():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2377)
    WaitChrThread(0xC, 3)
    StopEffect(0x0, 0x2)

    def lambda_238F():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_238F)
    WaitChrThread(0xD, 3)
    StopEffect(0x1, 0x2)

    def lambda_23A7():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_23A7)
    WaitChrThread(0xE, 3)
    StopEffect(0x2, 0x2)

    def lambda_23BF():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_23BF)
    WaitChrThread(0xF, 3)
    StopEffect(0x3, 0x2)

    def lambda_23D7():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_23D7)
    WaitChrThread(0x10, 3)
    StopEffect(0x4, 0x2)

    def lambda_23EF():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_23EF)
    WaitChrThread(0x11, 3)
    StopEffect(0x5, 0x2)

    def lambda_2407():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2407)
    WaitChrThread(0xC, 3)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    WaitChrThread(0xD, 3)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0xE, 3)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    WaitChrThread(0xF, 3)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    WaitChrThread(0x10, 3)
    EndChrThread(0x10, 0x2)
    EndChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    WaitChrThread(0x11, 3)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    CancelBlur(0)
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0x101,
        "#11P#0010FThose weren't your normal monsters...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101FAre those springs...and gears?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0201F'Dolls,' I presume.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FDolls? What kinda dolls have you\x01",
            "been playin' with...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_25BB")

    NpcTalk(
        0xB,
        "Old Man's Voice",
        (
            "Hmph. This has been a fine waste\x01",
            "of my time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_25BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_25F9")

    NpcTalk(
        0xB,
        "Old Man's Voice",
        "That's all you're made of?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_25F9")


    NpcTalk(
        0xB,
        "Old Man's Voice",
        (
            "Hmm, it looks like you four aren't entirely\x01",
            "useless, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2649")

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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0005FSir...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)

    def lambda_26F7():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26F7)

    def lambda_2704():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2704)

    def lambda_2711():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2711)

    def lambda_271E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_271E)
    OP_68(6130, 1500, 47630, 0)
    MoveCamera(53, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(1580, 1500, 36060, 4500)
    MoveCamera(53, 24, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(15880, 4500)
    ClearChrFlags(0xB, 0x4)
    OP_97(0xB, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrFlags(0xB, 0x4)
    OP_6F(0x79)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Wipe away the shock. I'm Joerg,\x01",
            "owner of the Rosenberg Doll Studio.\x02\x03",
            "You four are the youngsters of the\x01",
            "Special Support Section, I presume?\x02",
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
        "#12P#0001FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FYou mentioned that Renne told you\x01",
            "about us, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FIndeed. And even if that girl hadn't told me,\x01",
            "word of you folks would have eventually\x01",
            "made it to the ears of a recluse like me.\x02\x03",
            "#3900FYour performance wasn't anything too\x01",
            "great, but a promise is a promise.\x02\x03",
            "Take this.\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0xB, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x359),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x359, 1)
    OP_98(0xB, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#12P#0005FTh-Thank you, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0205FI was not expecting you to hand it over this\x01",
            "quickly, considering your objection earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FHah. Every doll has its own destiny.\x02\x03",
            "This particular doll's destiny involves meeting\x01",
            "a group of individuals tasked with handing it\x01",
            "over to a boorish broker.\x02\x03",
            "#3900FIt's the same with people. Each and every\x01",
            "one of our destinies rest in the hands of\x01",
            "the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FWise words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FThings do make a bit more sense\x01",
            "when you phrase it like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0013FW-Wait just a second!\x02\x03",
            "#0007FWhat were those angels just now?\x02\x03",
            "And does this mean that Renne really\x01",
            "is a part of that society?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FDetective Bannings.\x02\x03",
            "#3901FDo you really have the time to be\x01",
            "worrying about things like that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0011FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FI am a humble doll maker. Nothing more,\x01",
            "nothing less.\x02\x03",
            "You are attempting to confront the many\x01",
            "illnesses plaguing this land...\x02\x03",
            "However, you will find it impossible to find\x01",
            "a cure for all of them.\x02\x03",
            "#3901FAnd despite all that, I hear that you intend\x01",
            "to gaze into the bottomless abyss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0010FI-I know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FThe same goes for Renne.\x02\x03",
            "Her destiny is not entwined\x01",
            "with yours.\x02\x03",
            "#3900FBefore you worry yourselves with Renne,\x01",
            "isn't there someone else who should be\x01",
            "taking priority?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FYou mean KeA, right?\x02\x03",
            "#0101FLloyd found her in a suitcase that was\x01",
            "meant to contain one of your dolls, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0201F...it appears you already know that, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FIf you know somethin' about KeDo,\x01",
            "now's the time to spill the beans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FDid you forget what I just told you?\x01",
            "Every doll has its own destiny.\x02\x03",
            "#3900FPerhaps I made a doll with an unfortunate\x01",
            "destiny, one which led it to forgoing its life\x01",
            "as a doll, and instead becoming human.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0205FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0011FWhat are you even trying to say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FTo be clear, no dolls of that particular nature\x01",
            "have been crafted by these hands, as far\x01",
            "as I'm aware.\x02\x03",
            "#3900FThe entire incident was likely someone\x01",
            "appropriating the Rosenberg name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0106FPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FThat was in bad taste, sir.\x02\x03",
            "#0001FSo, you really don't know anything\x01",
            "about KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3901FAt the very least, I am not aware of\x01",
            "how she became involved in that auction.\x02\x03",
            "I assume neither is Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0008FThere goes my second question...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0308FDamn. And here I was hopin' that you'd\x01",
            "have some kinda clue for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FThat reminds me... Is Renne inside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#3903FNo. She just left, actually.\x02\x03",
            "#3900FShe's quite the fickle child. If you came to\x01",
            "see her, I recommend you give up now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0011FW-Wait...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#3903FI have no more to say to you four.\x02\x03",
            "Go on, take that doll to Imelda.\x02\x03",
            "#3900FAnd tell her to deposit the mira in\x01",
            "the usual account.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2000, 4000, 46500, 5000)
    ClearChrFlags(0xB, 0x4)
    OP_97(0xB, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x4)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x1)

    def lambda_363C():
        OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_363C)

    def lambda_3656():
        OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3656)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x1)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(2000, 600, 36250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 36250, 0)
    SetChrPos(0x1, 2000, 0, 36250, 0)
    SetChrPos(0x2, 2000, 0, 36250, 0)
    SetChrPos(0x3, 2000, 0, 36250, 0)
    ModifyEventFlags(1, 0, 0x80)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_29(0x30, 0x1, 0x5)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Jump("loc_3DB4")

    label("loc_3748")

    LoadChrToIndex("chr/ch00053.itc", 0x1E)
    LoadChrToIndex("chr/ch00153.itc", 0x1F)
    LoadChrToIndex("chr/ch00253.itc", 0x20)
    LoadChrToIndex("chr/ch00353.itc", 0x21)
    OP_68(2200, 800, 25700, 0)
    MoveCamera(34, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19460, 0)
    SetChrPos(0x101, 2000, 0, 25250, 0)
    SetChrPos(0x102, 1000, 0, 24000, 0)
    SetChrPos(0x103, 3000, 0, 24500, 0)
    SetChrPos(0x104, 2000, 0, 23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x3)
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
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_32(0xFF, 0xFE, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_39E9")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Brute force will get you nowhere.\x02\x03",
            "Tildawns reflect physical attacks, but if you\x01",
            "leave them alone, you will find yourselves in\x01",
            "a world of pain.\x02\x03",
            "Cooperating with those angels, who can impede\x01",
            "arts, one could say they're an unstoppable team.\x02\x03",
            "How to break down that fearsome combination...?\x01",
            "Try using your heads as you face them down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x30, 0x1, 0x4)
    Jump("loc_3D02")

    label("loc_39E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_3B05")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I haven't been that unentertained in a while.\x02\x03",
            "Those angels ruthlessly impede arts, so trying\x01",
            "to cast them is a waste of energy.\x02\x03",
            "Try shifting your strategy around your crafts.\x01",
            "That should produce better results next time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD3, 2)
    OP_29(0x30, 0x1, 0x3)
    Jump("loc_3D02")

    label("loc_3B05")

    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This isn't going anywhere. Try again\x01",
            "later, if you feel up to the task.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2140, 800, 24900, 1500)
    MoveCamera(34, 22, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(18490, 1500)
    OP_6F(0x79)
    OP_A6(0x101, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0010F#30WHarsh...\x02",
    )

    CloseMessageWindow()
    OP_A6(0x102, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#0108F#30WJ-Just what were those things...?\x02",
    )

    CloseMessageWindow()
    OP_A6(0x103, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#0206F#30WIt's obvious that they were no ordinary\x01",
            "monsters. Let alone like anything we\x01",
            "have faced before...\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x104, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    ChrTalk(
        0x104,
        "#12P#0301F#30WEither way, this ain't gonna be easy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 1)
    OP_29(0x30, 0x1, 0x2)

    label("loc_3D02")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_68(2000, 600, 25250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 25250, 0)
    SetChrPos(0x1, 2000, 0, 25250, 0)
    SetChrPos(0x2, 2000, 0, 25250, 0)
    SetChrPos(0x3, 2000, 0, 25250, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)

    label("loc_3DB4")

    Return()

    # Function_13_1EA2 end

    def Function_14_3DB5(): pass

    label("Function_14_3DB5")

    EventBegin(0x0)
    Fade(500)
    OP_68(2000, 1500, 29500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17600, 0)
    SetChrPos(0x101, 2000, 0, 30250, 180)
    SetChrPos(0x102, 1000, 0, 29000, 180)
    SetChrPos(0x103, 3000, 0, 29500, 180)
    SetChrPos(0x104, 2000, 0, 28000, 180)
    OP_68(2000, 1500, 24500, 3000)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)

    def lambda_3E56():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E56)
    Sleep(50)

    def lambda_3E73():
        OP_97(0x103, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E73)
    Sleep(50)

    def lambda_3E90():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E90)
    Sleep(50)

    def lambda_3EAD():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EAD)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)

    def lambda_3EEA():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EEA)
    Sleep(50)

    def lambda_3EFA():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EFA)
    Sleep(50)

    def lambda_3F0A():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F0A)
    Sleep(50)

    def lambda_3F1A():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F1A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_79(0x0)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#11P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FThe Society of Ouroboros, eh?\x02\x03",
            "#0301FDunno if that old man is a part of it,\x01",
            "but one thing's for sure: Those guys\x01",
            "are anything but normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0206FI am curious about those dolls... Even the\x01",
            "Epstein Foundation is still incapable of\x01",
            "creating things of that nature.\x02\x03",
            "#0201FAnd Liberl's ZCF has only just begun\x01",
            "their research into them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FThe Rosenberg Studio is becoming more\x01",
            "and more mysterious with every visit...\x02\x03",
            "#0108FThis might be too much for us to handle\x01",
            "at this point in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FI think you might be right there.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x101, 0x104, 500)

    def lambda_41F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41F8)
    Sleep(50)

    def lambda_4208():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4208)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FWell, we still have a job to do. Let's take\x01",
            "this doll back to the antique shop.\x02\x03",
            "I'm sure Imelda is waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FSounds good.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2000, 0, 25250, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x1, 0x1)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0xD3, 4)
    EventEnd(0x5)
    Return()

    # Function_14_3DB5 end

    def Function_15_42D6(): pass

    label("Function_15_42D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_68(11740, 600, 78670, 0)
    MoveCamera(21, 13, 0, 0)
    MoveCamera(21, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(103740, 0)
    SetChrPos(0x101, 680, 0, 12320, 0)
    SetChrPos(0x102, 1760, 0, 10960, 0)
    SetChrPos(0x103, -290, 0, 11070, 0)
    SetChrPos(0x104, 540, 0, 9730, 0)
    OP_68(12220, 600, 58030, 10000)
    PlaceName2(100, 200, "c_plac16", 0x0, 5000)
    FadeToBright(1000, 0)
    Sleep(4000)

    def lambda_43C3():
        OP_95(0xFE, 950, 0, 20480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43C3)

    def lambda_43DD():
        OP_95(0xFE, 2040, 0, 19440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43DD)

    def lambda_43F7():
        OP_95(0xFE, -300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43F7)

    def lambda_4411():
        OP_95(0xFE, 620, 0, 18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4411)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(1210, 3000, 27080, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26530, 0)
    OP_68(1210, 600, 27080, 6000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#1200260V#0005F#11PWhat is this place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200261V#0105FSomething certainly feels...off about it.\x02\x03",
            "#1200262V#0101FIt almost strikes me as abandoned, but\x01",
            "it looks like someone's living here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x104, 0x13B, 0x1F4)

    ChrTalk(
        0x104,
        "#1200263V#0305FOh, check it out.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetCameraDistance(22690, 0)
    OP_68(-5310, 800, 24820, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21610, 2500)
    SetChrPos(0x101, -6340, 120, 21700, 0)
    SetChrPos(0x102, -7980, 0, 21620, 0)
    SetChrPos(0x103, -8050, 0, 20110, 0)
    SetChrPos(0x104, -6570, 120, 19980, 0)
    OP_6F(0x10)
    OP_0D()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Rosenberg Studio\x01",
            "　  Keep Out\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1200264V#0102F#6PRosenberg...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1200265V#0005F#2PDoes that ring any bells, Elie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#1200266V#0100F#6PYes, it does. It's a very famous doll studio\x01",
            "known for making many valuable antiques.\x02\x03",
            "#1200267VI've been told there's an extremely\x01",
            "talented doll maker living here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#1200268V#0300F#2PDang. Who knew a place like that would\x01",
            "be all the way out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200269V#0203F#12PI have actually heard of that name before...\x02\x03",
            "#1200270V#0200FIf I am not mistaken, his dolls are usually sold\x01",
            "at auctions for extraordinarily high prices.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#1200271V#0104F#5PThat's true. I've only seen a few pieces of his\x01",
            "work, and the price is certainly warranted.\x02\x03",
            "#1200272V#0100FI can't help but agree with Randy. I knew he\x01",
            "operated around Crossbell, but I'd never\x01",
            "have guessed it'd be from such a remote place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200273V#0003F#5PA talented doll maker, you said?\x02\x03",
            "#1200274V#0001FIf the sign is any indication, he's not very open\x01",
            "to strangers. Would he even be willing to speak\x01",
            "to us in the first place?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1650, 0, 20130, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(100)

    NpcTalk(
        0x8,
        "Girl's Voice",
        "#1200275V#1PIf you're looking for Grandpa, he's not here.\x02",
    )

    CloseMessageWindow()
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
    Sleep(1000)

    def lambda_4B9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4B9D)
    OP_68(-2610, 800, 21420, 4000)
    MoveCamera(55, 14, 0, 4000)

    def lambda_4BCA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BCA)

    def lambda_4BD7():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BD7)
    Sleep(50)

    def lambda_4BE7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BE7)

    def lambda_4BF4():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4BF4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1200276V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200277V#0105F#3P(A girl? Where'd she come from...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200278V#0200F#3P(Could she be living at the studio?)\x02",
    )

    CloseMessageWindow()
    OP_68(-3240, 800, 21630, 2000)
    OP_97(0x8, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
    OP_6F(0x1)

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200279V#3309F#11PTeehee. Good day, everyone.\x02\x03",
            "#1200280V#3300FWho might you four be?\x02\x03",
            "#1200281VHave you some business with the studio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200282V#0005F#6PUmm, about that...\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 800, 21080, 2000)
    OP_95(0x101, -4470, 0, 20870, 1600, 0x0)
    TurnDirection(0x101, 0x8, 500)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#1200283V#0004F#6PThere's no need to be suspicious of us.\x02\x03",
            "#1200284V#0000FWe're with the Crossbell Police Department.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200285V#3305F#11POh, you're police officers?\x02\x03",
            "#1200286V#3304FFunny. I've never seen the police wander\x01",
            "outside of the city before...\x02\x03",
            "#1200287V#3300FAre you patrolling this area now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200288V#0005F#6PNot exactly. You see, we didn't come\x01",
            "here on an official patrol.\x02\x03",
            "#1200289V#0000FActually, we were hoping to ask someone\x01",
            "about the local monsters.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200290V#3305F#11PMonsters? What kind of monsters are\x01",
            "you curious about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200291V#0106F#6PThey're canines. Wolves, we think.\x02\x03",
            "#1200292V#0101FHas your grandfather talked about\x01",
            "monsters like that before?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200293V#3303F#11PI'm afraid not, miss.\x02\x03",
            "#1200294V#3308FBut...I do think I heard some\x01",
            "howling in the distance earlier.\x02\x03",
            "#1200295V#3300FCould that have been the wolves\x01",
            "you were looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200296V#0001F#6PIt's definitely possible.\x02\x03",
            "#1200297VYou said your grandfather is away, so\x01",
            "does that mean the studio is empty?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200298V#3300F#11PYes, that's correct.\x02\x03",
            "#1200299VHe did tell me that he would return\x01",
            "late in the evening, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200300V#0003F#6PReally? We can't stay to wait on him...\x02\x03",
            "#1200301V#0001FI know we already told you, but I want to\x01",
            "stress this. There are extremely dangerous\x01",
            "monsters running around here.\x02\x03",
            "#1200302VWould you mind staying inside until your\x01",
            "grandfather comes back? It would give us\x01",
            "some peace of mind, at least.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200303V#3305F#11PI don't mind, but...\x02\x03",
            "#1200304V#3304F...I think following you all would be\x01",
            "much more entertaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200305V#0005F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200306V#3302F#11PYou're playing tag with that big wolf, aren't you?\x02\x03",
            "#1200307V#3309FOr is hide-and-seek a better description? Either\x01",
            "way, it looks quite fun. I'm almost jealous of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1200308V#0204F#3PI suppose that is one way of putting it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200309V#0302F#6PHaha. You've got spunk, kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200310V#0011F#6PHold on! We're still not 100 percent sure of\x01",
            "what we're chasing down, so taking you along\x01",
            "is completely out of the question.\x02\x03",
            "#1200311V#0006FI'm sorry. Again, would you mind staying\x01",
            "inside for us?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200312V#3301F#11PHow boring.\x02\x03",
            "#1200313VIf only he was repaired... Then I\x01",
            "wouldn't be so bored.\x02\x03",
            "#1200314V#3304FOh, well. Perhaps I should leave it at that\x01",
            "for today and go mess with Freckles a bit\x01",
            "more...\x02\x03",
            "#1200315VOr maybe playing in the glass castle\x01",
            "would be a better choice...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#1200316V#0005F#6PMess with who...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200317V#0105F#3PWhat is the glass castle?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Girl in Dress",
        (
            "#1200318V#3309F#11PHeehee. I'm simply talking to myself.\x02\x03",
            "#1200319V#3302FOh, silly me. I haven't even introduced\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Girl in Dress")

    AnonymousTalk(
        0xFF,
        (
            "#1200320VPlease, call me Renne.\x02\x03",
            "#1200321VIn truth, there's someone else I\x01",
            "would love to introduce you to...\x02\x03",
            "#1200322V...but, unfortunately, his right\x01",
            "leg was broken and is being patched\x01",
            "up by Grandpa right now.\x02",
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
            "#1200323V#0000F#6PI-I'm sorry to hear that. (Is she talking\x01",
            "about one of her dolls or something?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200324V#3304F#11PThis wolf seems to be quite the smarty-pants.\x02\x03",
            "#1200325VI wanted to play with him for a bit, but\x01",
            "I'm already a grown-up. I won't be too\x01",
            "selfish this time.\x02\x03",
            "#1200326V#3302FSpecial Support Section, keep up the\x01",
            "hard work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200327V#0012F#6PThanks?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200328V#0102F#3PYou be careful now, Renne.\x02",
    )

    CloseMessageWindow()

    def lambda_5C4B():

        label("loc_5C4B")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_5C4B")

    QueueWorkItem2(0x101, 1, lambda_5C4B)

    def lambda_5C5D():

        label("loc_5C5D")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_5C5D")

    QueueWorkItem2(0x102, 1, lambda_5C5D)

    def lambda_5C6F():

        label("loc_5C6F")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_5C6F")

    QueueWorkItem2(0x103, 1, lambda_5C6F)

    def lambda_5C81():

        label("loc_5C81")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_5C81")

    QueueWorkItem2(0x104, 1, lambda_5C81)
    OP_93(0x8, 0x0, 0x190)
    OP_95(0x8, 1950, 0, 25620, 2000, 0x0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    OP_68(-4220, 600, 23220, 4000)
    MoveCamera(45, 14, 0, 4000)

    def lambda_5CDF():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CDF)
    Sleep(1000)

    def lambda_5CFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5CFC)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        (
            "#1200329V#0204F#6PShe was quite the unique one.\x02\x03",
            "#1200330V#0202FIs she actually the granddaughter of the\x01",
            "famous Rosenberg doll maker?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#1200331V#0304F#11PGuess so.\x02\x03",
            "#1200332V#0302FShe was strangely mature for her\x01",
            "age, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#1200333V#0109F#5PI thought she was simply adorable.\x02\x03",
            "#1200334V#0102FHer ambiguous way of speaking might just\x01",
            "be a part of her charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200335V#0001F#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#1200336V#0105F#6PLloyd? Did I say something wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_5F38():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F38)
    Sleep(50)

    def lambda_5F48():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F48)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        "#1200337V#0305F#6PWhat's with that look on your face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200338V#0200F#6PAre you worried about Renne's safety?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200339V#0003F#5PNo... That's not it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200340V#0001F#11PRight before she left... Didn't she refer to\x01",
            "us as the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#1200341V#0101F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200342V#0205F#6PNow that you mention it...we did not\x01",
            "introduce ourselves as such, did we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200343V#0301F#6PHow the hell would a lil' girl like her\x01",
            "know about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200344V#0006F#11PWell, it's possible that she recognized us\x01",
            "through the Crossbell Times.\x02\x03",
            "#1200345VAnd if that's the case, it's not unlikely she'd\x01",
            "know who we are.\x02\x03",
            "#1200346V#0000FStill, I think there's more to her than\x01",
            "meets the eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200347V#0300F#6PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200348V#0203F#6P...I concur.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200349V#0003F#11PAnyway, it doesn't look like the wolves\x01",
            "have made their way up here.\x02\x03",
            "#1200350V#0000FLet's head back for now and keep making\x01",
            "our way towards Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200351V#0100F#6PYes, let's.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(21860, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -8080, 0, 19380, 180)
    SetScenarioFlags(0x64, 5)
    OP_29(0x40, 0x1, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_42D6 end

    def Function_16_641C(): pass

    label("Function_16_641C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(2050, 3100, 45140, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 2750, 0, 23000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 1250, 0, 23080, 0)
    SetChrPos(0x101, 2000, 0, 10250, 0)
    SetChrPos(0x102, 1000, 0, 9000, 0)
    SetChrPos(0x103, 3000, 0, 9500, 0)
    SetChrPos(0x104, 2000, 0, 8000, 0)
    OP_68(2910, 600, 25220, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6F(0x1)
    Fade(500)
    OP_68(2000, 1200, 23000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    OP_64(0x9)
    OP_64(0xA)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#0808FNo one home?\x02\x03",
            "#0801FJoshua, are you positive this\x01",
            "is the place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0903FI don't have definitive proof, but everything\x01",
            "we've found out up until now points here.\x02\x03",
            "#0908FThere's just too much information about the\x01",
            "Thirteen Factories I wasn't told.\x02\x03",
            "All we know is that it's a network of twelve\x01",
            "workshops that has passed down ancient\x01",
            "technology...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0803FAnd supposedly this doll studio is one of them.\x02\x03",
            "#0801FThis is definitely the kind of place\x01",
            "she'd stay at.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_674B():
        OP_93(0xA, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_674B)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0xA,
        (
            "#0901FWhat's the plan, Estelle?\x02\x03",
            "Should I go in and investigate?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67A2():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_67A2)
    WaitChrThread(0x9, 2)

    ChrTalk(
        0x9,
        (
            "#0804FNo, it's okay.\x02\x03",
            "Lucky for us, we aren't directly butting\x01",
            "heads with the society this time.\x02\x03",
            "#0802FIf I'm going to catch her, I'll have to\x01",
            "play by the rules!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0904FIf that's what you think is best, I'm with you.\x02\x03",
            "#0900FBesides, we still have that auction to worry\x01",
            "about. Should we focus on that for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0800FSounds good to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FEstelle? Joshua?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(2000, 1200, 21750, 5000)
    SetCameraDistance(19500, 5000)

    def lambda_6979():
        OP_95(0xFE, 2000, 0, 20250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6979)
    Sleep(50)

    def lambda_6996():
        OP_95(0xFE, 1000, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6996)
    Sleep(50)

    def lambda_69B3():
        OP_95(0xFE, 3000, 0, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69B3)
    Sleep(50)

    def lambda_69D0():
        OP_95(0xFE, 2000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69D0)

    def lambda_69EA():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_69EA)

    def lambda_69F7():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_69F7)

    ChrTalk(
        0x9,
        "#0805F#5PWhat the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0905FThe SSS?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    WaitChrThread(0xA, 2)
    OP_6F(0x51)

    ChrTalk(
        0x104,
        "#0305FHey, what a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FI thought I was detecting a familiar presence,\x01",
            "but I could not quite pinpoint who it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0813F#5PWh-Why the heck are you guys here?\x02\x03",
            "#0801FDoes the Special Support Section\x01",
            "have some business with the studio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWe were just stretching our legs for\x01",
            "a bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FWhat about you? Did the Bracer Guild\x01",
            "have a request here or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0809F#5PA-Actually, we're here on personal\x01",
            "business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0904FWe were, but it looks like the meister\x01",
            "isn't in right now.\x02\x03",
            "#0900FOn a lighter note, you guys put up a good\x01",
            "fight yesterday. How are you feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FI'm a little sore, but fine overall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWho cares 'bout us? You two were the\x01",
            "ones who gave us a run for our mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0802F#5PHaha, you think? I guess these two years\x01",
            "of walking everywhere has finally started\x01",
            "to pay off.\x02\x03",
            "#0806FSorry to cut our conversation short, but\x01",
            "it's about time for us to start heading back\x01",
            "to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#0902FI'm sure we'll run into each other again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FBe careful on your way back, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0809FOf course! You stay safe, too!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0xA, 2, 0, 18)

    def lambda_6E9F():

        label("loc_6E9F")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6E9F")

    QueueWorkItem2(0x101, 2, lambda_6E9F)

    def lambda_6EB1():

        label("loc_6EB1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6EB1")

    QueueWorkItem2(0x102, 2, lambda_6EB1)

    def lambda_6EC3():

        label("loc_6EC3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6EC3")

    QueueWorkItem2(0x103, 2, lambda_6EC3)

    def lambda_6ED5():

        label("loc_6ED5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6ED5")

    QueueWorkItem2(0x104, 2, lambda_6ED5)
    Sleep(2000)
    OP_68(1000, 1200, 18000, 3000)
    Sleep(4000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    Sleep(500)
    OP_68(2000, 1200, 19000, 3500)
    MoveCamera(51, 23, 0, 3500)
    SetCameraDistance(17500, 3500)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    def lambda_6FAB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FAB)

    def lambda_6FB8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FB8)

    def lambda_6FC5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6FC5)

    def lambda_6FD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6FD2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        (
            "#0301FEven a moron could tell that they\x01",
            "were hidin' something from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThat may be true, but I did not sense\x01",
            "any guilt coming from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F#3PI don't think it's our place to stick our\x01",
            "noses into their private matters.\x02\x03",
            "#0100FJoshua mentioned that the owner of the\x01",
            "doll studio isn't home. Shall we head on\x01",
            "back as well, then?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_71E1")

    ChrTalk(
        0x101,
        (
            "#0003FYeah, might as well.\x02\x03",
            "#0008F(We all met Renne for the first time\x01",
            "when we were here before...)\x02\x03",
            "(Do those two know her somehow?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725F")

    label("loc_71E1")


    ChrTalk(
        0x101,
        (
            "#0003FYeah, might as well.\x02\x03",
            "#0008F(We met that strange girl here last\x01",
            "time, didn't we?)\x02\x03",
            "(Do those two know who she is?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_725F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(2000, 600, 20250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 20250, 0)
    SetChrPos(0x1, 2000, 0, 20250, 0)
    SetChrPos(0x2, 2000, 0, 20250, 0)
    SetChrPos(0x3, 2000, 0, 20250, 0)
    SetScenarioFlags(0xB7, 2)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_641C end

    def Function_17_730D(): pass

    label("Function_17_730D")

    OP_95(0xFE, 5000, 0, 20750, 2000, 0x0)
    OP_95(0xFE, 1000, 0, 0, 2000, 0x0)
    Return()

    # Function_17_730D end

    def Function_18_7336(): pass

    label("Function_18_7336")

    Sleep(50)
    OP_95(0xFE, 4750, 0, 21000, 2000, 0x0)
    OP_95(0xFE, 750, 0, 0, 2000, 0x0)
    Return()

    # Function_18_7336 end

    def Function_19_7362(): pass

    label("Function_19_7362")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Rosenberg Studio\x01",
            "　  Keep Out\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_7362 end

    def Function_20_73B8(): pass

    label("Function_20_73B8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_73C9")
    Jump("loc_741B")

    label("loc_73C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_741B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_73E4")
    Jump("loc_741B")

    label("loc_73E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_73F4")
    Call(0, 12)
    TalkEnd(0xFF)
    Return()

    label("loc_73F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7408")
    Call(0, 9)
    TalkEnd(0xFF)
    Return()

    label("loc_7408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_741B")
    Call(0, 4)
    TalkEnd(0xFF)
    Return()

    label("loc_741B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_20_73B8 end

    def Function_21_7444(): pass

    label("Function_21_7444")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked, and there is no sign of the old man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_7444 end

    SaveToFile()

Try(main)
