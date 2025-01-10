from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t050b.bin",                # FileName
        "t050B",                    # MapName
        "t050B",                    # Location
        0x003C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 3, 0, 4],
    )

    BuildStringList((
        "t050b",                  # 0
        "Mine Chief Hoffmann",    # 1
        "Miner Marlow",           # 2
        "Miner Gantz",            # 3
        "Monster",                # 4
        "Monster",                # 5
        "Monster",                # 6
        "SE制御",                 # 7
        "BT050b",                 # 8
        "Mainz Mountain Path",    # 9
        "Mainz Mine",             # 10
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 2, 13, 180)
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
        "BattleInfo_E4", 0x0002, 16, 6, 0, 0, 0, 0, 0, "BT050b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch26300.itc",                   # 01
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

    DeclNpc(-24969,  11439,   56069,   270,  401,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-4600,   -2000,   28700,   1500,    -4600,   -500,    28700,   0x007C, 0,  6,  0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "Mainz Mine")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_348",          # 00, 0
        "Function_1_400",          # 01, 1
        "Function_2_451",          # 02, 2
        "Function_3_46C",          # 03, 3
        "Function_4_49F",          # 04, 4
        "Function_5_4E4",          # 05, 5
        "Function_6_FDF",          # 06, 6
        "Function_7_1009",         # 07, 7
        "Function_8_1FD0",         # 08, 8
        "Function_9_200C",         # 09, 9
        "Function_10_202A",        # 0A, 10
        "Function_11_2069",        # 0B, 11
        "Function_12_209A",        # 0C, 12
        "Function_13_20B6",        # 0D, 13
        "Function_14_20D5",        # 0E, 14
        "Function_15_211B",        # 0F, 15
        "Function_16_216D",        # 10, 16
        "Function_17_21BF",        # 11, 17
        "Function_18_2211",        # 12, 18
        "Function_19_2277",        # 13, 19
        "Function_20_22BA",        # 14, 20
        "Function_21_299F",        # 15, 21
        "Function_22_29F7",        # 16, 22
    ))


    def Function_0_348(): pass

    label("Function_0_348")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_388"),
        (1, "loc_394"),
        (2, "loc_3A0"),
        (3, "loc_3AC"),
        (4, "loc_3B8"),
        (5, "loc_3C4"),
        (6, "loc_3D0"),
        (SWITCH_DEFAULT, "loc_3DC"),
    )


    label("loc_388")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_394")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E8")

    label("loc_3FF")

    Return()

    # Function_0_348 end

    def Function_1_400(): pass

    label("Function_1_400")

    OP_95(0xFE, -23810, 11440, 54160, 3000, 0x0)
    OP_95(0xFE, -20240, 11440, 54160, 3000, 0x0)
    OP_95(0xFE, -18970, 11440, 55670, 3000, 0x0)
    OP_95(0xFE, -14930, 9560, 55670, 3000, 0x0)
    Return()

    # Function_1_400 end

    def Function_2_451(): pass

    label("Function_2_451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    TurnDirection(0xFE, 0x8, 100)
    Sleep(10)
    Jump("Function_2_451")

    label("loc_46B")

    Return()

    # Function_2_451 end

    def Function_3_46C(): pass

    label("Function_3_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_480")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)
    Jump("loc_48F")

    label("loc_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_48F")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 20)

    label("loc_48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E")
    ClearChrFlags(0x8, 0x80)

    label("loc_49E")

    Return()

    # Function_3_46C end

    def Function_4_49F(): pass

    label("Function_4_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF")
    ClearMapObjFlags(0x6, 0x10)

    label("loc_4AF")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C7")
    OP_1B(0x0, 0x0, 0x16)

    label("loc_4C7")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Return()

    # Function_4_49F end

    def Function_5_4E4(): pass

    label("Function_5_4E4")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-22000, 13400, 56100, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -22770, 11440, 55720, 270)
    SetChrPos(0x102, -22770, 11440, 57320, 270)
    SetChrPos(0x103, -21040, 11440, 55740, 270)
    SetChrPos(0x104, -21040, 11440, 57320, 270)
    FadeToBright(500, 0)
    OP_0D()
    Sound(810, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "There we go. That's\x01",
            "everyone, by my count.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it looks like Gantz and Marlow\x01",
            "already snuck away to the bar... Oh, well.\x01",
            "As long as they're indoors, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUmm, excuse me...\x01",
            "What exactly are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Oh, I'm just closing the mine's gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Monsters like to show up every once\x01",
            "in a while, so I've got to make sure\x01",
            "no one's left inside with those suckers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FMonsters...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x102, 0xB4, 0x12C)

    ChrTalk(
        0x102,
        (
            "#0105FLloyd, what's the matter?\x02\x03",
            "Something's bothering you, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77F)

    def lambda_78C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#0001FOh, I was just thinking...\x02\x03",
            "#0000FWe still have time before the operation,\x01",
            "so why not train here for a bit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#0300FHuh, might be on to\x01",
            "somethin' there, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FIt is true that we do not have enough\x01",
            "time to head back onto the highway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh, what are you kids talkin' about?\x02",
    )

    CloseMessageWindow()

    def lambda_917():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_917)

    def lambda_924():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_924)

    def lambda_931():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_931)

    def lambda_93E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#0000FUhm, you see...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the situation and asked if\x01",
            "they could be allowed to train in the mine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "Huh, that's it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sorry, can't usually do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If outsiders went inside and got hurt, as the\x01",
            "mine chief, that'd fall onto my shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FO-Oh, is that the case...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103FNothing we can do, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hey, now, I didn't refuse just yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Judgin' by what's in front of me, you look about\x01",
            "as tough as any miner I've ever seen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If y'all promise not to go crazy in there,\x01",
            "I'll make a special exception for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309FHaha, mighty generous of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y'know, I want to give some payback\x01",
            "to those mutts who tore up Max, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you promise to get them good,\x01",
            "I'd be happy to lend a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "All right, give me a sec.\x02",
    )

    CloseMessageWindow()

    def lambda_C9B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C9B)
    WaitChrThread(0x8, 1)
    Sound(809, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hoffman unlocked the mine's gate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_CE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE2)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "Okay, then, y'all try not to\x01",
            "get too worn out in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right... The left gate inside there leads to the\x01",
            "abandoned mine. Stay away from there, y'hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FLoud and clear. Thanks for the help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No sweat. Well, then, I'll leave our\x01",
            "wolf infestation in your hands.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 1)

    def lambda_E18():

        label("loc_E18")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E18")

    QueueWorkItem2(0x101, 1, lambda_E18)

    def lambda_E2A():

        label("loc_E2A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E2A")

    QueueWorkItem2(0x102, 1, lambda_E2A)

    def lambda_E3C():

        label("loc_E3C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E3C")

    QueueWorkItem2(0x103, 1, lambda_E3C)

    def lambda_E4E():

        label("loc_E4E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_E4E")

    QueueWorkItem2(0x104, 1, lambda_E4E)
    Sleep(6000)

    def lambda_E63():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E63)

    def lambda_E70():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E70)

    def lambda_E7D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E7D)

    def lambda_E8A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E8A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        (
            "#0200FAt any rate, we can enter and\x01",
            "exit the mine freely now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FRight, let's use this as a warmup\x01",
            "for our operation later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(-21980, 13440, 56060, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, -21980, 11440, 56060, 270)
    SetChrPos(0x102, -21980, 11440, 56060, 270)
    SetChrPos(0x103, -21980, 11440, 56060, 270)
    SetChrPos(0x104, -21980, 11440, 56060, 270)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0x6, 0x10)
    SetScenarioFlags(0x68, 2)
    EventEnd(0x5)
    Return()

    # Function_5_4E4 end

    def Function_6_FDF(): pass

    label("Function_6_FDF")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_6_FDF end

    def Function_7_1009(): pass

    label("Function_7_1009")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26200.itc", 0x1E)
    LoadChrToIndex("chr/ch30700.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("monster/ch75650.itc", 0x28)
    LoadChrToIndex("monster/ch75651.itc", 0x29)
    LoadChrToIndex("monster/ch75653.itc", 0x2A)
    LoadChrToIndex("apl/ch50121.itc", 0x2B)
    LoadEffect(0x0, "event\\ev100_00.eff")
    SoundLoad(843)
    SetChrPos(0x101, 8700, 0, 56240, 90)
    SetChrPos(0x102, 9160, 0, 41110, 90)
    SetChrPos(0x103, 10870, 0, 41130, 90)
    SetChrPos(0x104, -4490, 2920, 44010, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0xA, -1950, 440, 54350, 90)
    SetChrPos(0x9, -1950, 440, 54350, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(843, 2, 100, 0)
    OP_68(-1910, 3550, 66890, 0)
    MoveCamera(326, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(110410, 0)
    OP_68(-1910, -550, 66890, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(0, 750, 54400, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29280, 0)
    SetCameraDistance(27780, 3000)
    OP_6F(0x10)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    Sleep(700)

    def lambda_128D():
        OP_97(0xFE, 0x1964, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_128D)

    def lambda_12A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_12A7)
    Sleep(800)

    def lambda_12BB():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12BB)

    def lambda_12D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12D5)
    Sleep(1000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    TurnDirection(0xA, 0x9, 500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sleep(500)
    OP_93(0xA, 0xB4, 0x1F4)

    def lambda_131F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_131F)
    Sleep(300)

    def lambda_133C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_133C)
    Sleep(2000)
    BeginChrThread(0xE, 1, 0, 19)
    Fade(1000)
    OP_68(3730, 1050, 46330, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20800, 0)
    SetCameraDistance(19000, 2000)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xE, 0x1)
    TurnDirection(0xA, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#1200781V#11P*hic*...Maybe I had a lil'\x01",
            "too mush ta drink...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#1200782V#5PIt's already gotten this late, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1200783V#5PMayor told us to head back\x01",
            "home early, y'know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1200784V#11POh, worried 'bout a few shmall monshters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200785V#11PPft, I put ashide visitin' the casino to keep\x01",
            "shlavin' away in those damn mines, man. *hic*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200786V#11PCut me shome slack and lemme\x01",
            "have a couple of drinks, damn it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1200787V#5PDude, every weekend you go to that\x01",
            "casino and bleed yourself dry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1200788V#5PYou must be their best regular, huh? Y'know,\x01",
            "given how much mira they milk outta you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200789V#11PSh-Shuddup...*hic*\x01",
            "I'm savin' my money for my next trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1200790V#11PJust ya watch... I'll score big at roulette\x01",
            "next time and win everything back!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(836, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xA,
        "#1200791V#11PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200792V#5PDid you hear that?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_176E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_176E)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetCameraDistance(20500, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xB, 13370, 0, 47650, 270)
    SetChrPos(0xC, 3460, 0, 55100, 180)
    SetChrPos(0xD, 3200, 0, 39330, 0)
    BeginChrThread(0xB, 3, 0, 15)
    BeginChrThread(0xC, 3, 0, 16)
    BeginChrThread(0xD, 3, 0, 17)
    Sleep(100)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        "#1200793V#5PEek! The hell?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0xD, 500)

    ChrTalk(
        0x9,
        "#1200794V#11PN-No way... The wolves?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetCameraDistance(17580, 1000)
    BeginChrThread(0xB, 3, 0, 14)
    BeginChrThread(0xC, 3, 0, 14)
    BeginChrThread(0xD, 3, 0, 14)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 8)
    BeginChrThread(0x9, 3, 0, 9)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0xA,
        "#1200795V#5PP-P-Please, stay away from me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200796V#11PH-Help us, Aidios!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Young Man's Voice",
        (
            "#1200797V#4PYo, you two. Might\x01",
            "wanna cover your eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x104, 500)
    TurnDirection(0x9, 0x104, 500)
    Sound(1298, 255, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 4310, 0, 47660, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(814, 0, 100, 0)
    Sleep(1800)
    Sound(555, 0, 100, 0)
    Sleep(700)
    Sound(555, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 10)
    Sound(556, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(250)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 11)
    Sleep(100)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 11)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#1200799V#11PWoof?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#1200800V#11PWoof...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)

    ChrTalk(
        0xA,
        "#1200801V#11PWhat the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200802V#5PWh-What WAS that?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetCameraDistance(21000, 1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1BCF():
        OP_95(0xFE, 5960, 0, 50660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BCF)

    def lambda_1BE9():
        OP_95(0xFE, 5990, 0, 43230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BE9)

    def lambda_1C03():
        OP_95(0xFE, 7630, 0, 43280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C03)

    def lambda_1C1D():
        OP_95(0xFE, -790, 0, 44080, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C1D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#1200803V#0304F#1PA flashbang.\x02\x03",
            "#1200804V#0302FThese babies are pretty useful\x01",
            "against mutts like these.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0xA,
        "#1200805V#11PY-You guys...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "#1200806V#5PF-From earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200807V#0007F#2PSave the talking for later! For\x01",
            "now, go take shelter in the inn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1200808V#5PY-Yeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#1200809V#11PUgh, what is GOING ON?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 18)
    Sleep(2100)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x9, 3)
    OP_64(0x9)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    WaitChrThread(0xA, 3)
    OP_64(0xA)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Sleep(200)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Fade(250)
    EndChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 13)
    OP_0D()
    TurnDirection(0xB, 0x103, 0)

    ChrTalk(
        0xB,
        "#1200810V#11PGrrrrrrr...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 0, 0, 13)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 13)
    OP_0D()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x104, 500)

    ChrTalk(
        0xC,
        "#1200811V#5PWoof!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200812V#0301F#1PDamn, they recovered pretty quickly.\x01",
            "This is gonna be a real pain in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200813V#0007FAll right, everyone...\x01",
            "Let's take them out!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    StopBGM(0x7D0)
    OP_24(0x34B)
    Battle("BattleInfo_E4", 0x30200011, 0x0, 0x0, 0xD, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Call(0, 20)
    Return()

    # Function_7_1009 end

    def Function_8_1FD0(): pass

    label("Function_8_1FD0")


    def lambda_1FD5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FD5)
    WaitChrThread(0xA, 1)

    def lambda_1FF2():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1FF2)
    WaitChrThread(0xA, 2)
    Return()

    # Function_8_1FD0 end

    def Function_9_200C(): pass

    label("Function_9_200C")


    def lambda_2011():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2011)
    WaitChrThread(0x9, 1)
    Return()

    # Function_9_200C end

    def Function_10_202A(): pass

    label("Function_10_202A")

    OP_82(0x0, 0x12C, 0x1770, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(19580, 150)
    OP_6F(0x79)
    CancelBlur(1000)
    SetCameraDistance(17580, 1000)
    OP_6F(0x79)
    Return()

    # Function_10_202A end

    def Function_11_2069(): pass

    label("Function_11_2069")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2085():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2085)
    Return()

    # Function_11_2069 end

    def Function_12_209A(): pass

    label("Function_12_209A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B5")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_12_209A")

    label("loc_20B5")

    Return()

    # Function_12_209A end

    def Function_13_20B6(): pass

    label("Function_13_20B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20D4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_13_20B6")

    label("loc_20D4")

    Return()

    # Function_13_20B6 end

    def Function_14_20D5(): pass

    label("Function_14_20D5")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    Return()

    # Function_14_20D5 end

    def Function_15_211B(): pass

    label("Function_15_211B")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 8670, 0, 47200, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_211B end

    def Function_16_216D(): pass

    label("Function_16_216D")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 3260, 0, 50500, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_16_216D end

    def Function_17_21BF(): pass

    label("Function_17_21BF")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 3200, 0, 42450, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_21BF end

    def Function_18_2211(): pass

    label("Function_18_2211")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, 1190, 0, 49990, 4000, 0x0)
    OP_95(0xFE, 860, 0, 54460, 4000, 0x0)

    def lambda_2245():
        OP_95(0xFE, -1950, 440, 54350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2245)
    Sleep(500)

    def lambda_2262():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2262)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2211 end

    def Function_19_2277(): pass

    label("Function_19_2277")

    OP_25(0x34B, 0x5A)
    Sleep(100)
    OP_25(0x34B, 0x50)
    Sleep(100)
    OP_25(0x34B, 0x46)
    Sleep(100)
    OP_25(0x34B, 0x3C)
    Sleep(100)
    OP_25(0x34B, 0x32)
    Sleep(100)
    OP_25(0x34B, 0x28)
    Sleep(100)
    OP_25(0x34B, 0x1E)
    Sleep(100)
    OP_25(0x34B, 0x14)
    Sleep(100)
    OP_25(0x34B, 0xA)
    Sleep(100)
    OP_24(0x34B)
    Return()

    # Function_19_2277 end

    def Function_20_22BA(): pass

    label("Function_20_22BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("monster/ch75650.itc", 0x28)
    LoadChrToIndex("monster/ch75651.itc", 0x29)
    LoadChrToIndex("apl/ch50121.itc", 0x2A)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 4200, 0, 48980, 180)
    SetChrPos(0x102, 6050, 0, 49360, 180)
    SetChrPos(0x103, 5020, 0, 50820, 180)
    SetChrPos(0x104, 3410, 0, 50610, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2580, 0, 45100, 0)
    SetChrPos(0xC, 4270, 0, 42920, 0)
    SetChrPos(0xD, 5490, 0, 44910, 0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(1350, 150, 47770, 0)
    MoveCamera(301, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23200, 0)
    OP_68(1350, 150, 49270, 2000)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#1200814V#0003F#2PPhew, they definitely\x01",
            "were a handful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200815V#0101F#4PNow that I take a closer look...\x01",
            "they look like dogs, not wolves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200816V#0201F#2PSo these were trained\x01",
            "war hounds after all...?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1350, 150, 47770, 3000)
    OP_6F(0x1)

    def lambda_2576():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2576)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0xC, 2)
    Sound(836, 0, 100, 0)

    NpcTalk(
        0xC,
        "War Hound",
        "#1200817VGrrrr...\x02",
    )

    CloseMessageWindow()

    def lambda_25D6():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_25D6)

    def lambda_25EF():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_25EF)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)

    NpcTalk(
        0xD,
        "War Hound",
        "#1200818V#5PArf...!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 21)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xC, 0xE1, 0x1F4)
    OP_63(0xC, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xC, 0, 0, 12)

    def lambda_269A():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_269A)
    Sleep(750)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xD, 0xE1, 0x1F4)
    OP_63(0xD, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xD, 0, 0, 12)

    def lambda_26E9():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_26E9)
    Sleep(750)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xB, 0xE1, 0x1F4)
    OP_63(0xB, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xB, 0, 0, 12)

    def lambda_2738():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2738)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1200819V#0205FAh...!\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_64(0xC)
    WaitChrThread(0xC, 1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_64(0xD)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    ChrTalk(
        0x104,
        "#1200820V#0301F#2PDang... Still kickin', huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200821V#0007FIt's fine! Just follow them\x01",
            "for now!\x02\x03",
            "#1200822VThey'll probably lead us back\x01",
            "to where the mobsters are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200823V#0107F#4PRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)

    def lambda_28FB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28FB)

    def lambda_2910():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2910)

    def lambda_2925():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2925)

    def lambda_293A():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_293A)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    EndChrThread(0xE, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_22BA end

    def Function_21_299F(): pass

    label("Function_21_299F")

    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Return()

    # Function_21_299F end

    def Function_22_29F7(): pass

    label("Function_22_29F7")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThe sun's already set.\x02\x03",
            "#0003FOdds are, they'll assault the village tonight.\x01",
            "Let's avoid going out onto the highway.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_22_29F7 end

    SaveToFile()

Try(main)
