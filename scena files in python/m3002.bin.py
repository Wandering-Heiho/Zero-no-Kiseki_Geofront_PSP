from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3002.bin",                # FileName
        "m3002",                    # MapName
        "m3002",                    # Location
        0x007B,                     # MapIndex
        "ed7510",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -79500, 0, 0, 0, 0, 1, 123, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3002",                  # 0
        "SE制御",                 # 1
        "bm3080",                 # 2
        "bm3080",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_B4", 0,   29,  0,   0,   9,   3,   19)

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

    # monster count: 4

    BattleInfo(
        "BattleInfo_104", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3080", "Sepith_A4", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1CC", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3080", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch68650.itc",               # 10
        "monster/ch68651.itc",               # 11
        "monster/ch60650.itc",               # 12
        "monster/ch60650.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-7710,   26930,   10,      0x1010000,    "BattleInfo_104", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19430,   -70,     -12000,  0x1010000,    "BattleInfo_1CC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-35270,  -28040,  -228000, 0x1010000,    "BattleInfo_104", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-36100,  27760,   -228000, 0x1010000,    "BattleInfo_1CC", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 4,   -46.0,                 0.0,                   5.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.333333969116211,    -0.0,                  -1.0,                  1.0])
    DeclEvent(0x0000, 0, 5,   -46.0,                 0.0,                   5.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.333333969116211,    -0.0,                  -1.0,                  1.0])

    DeclActor(-7500,   -228000, 24500,   1200,    -7500,   -227000, 24500,   0x007C, 0,  2,  0x0000)
    DeclActor(-23250,  -228000, 28500,   1200,    -23250,  -227000, 28500,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_4D8",          # 00, 0
        "Function_1_4D9",          # 01, 1
        "Function_2_579",          # 02, 2
        "Function_3_768",          # 03, 3
        "Function_4_90B",          # 04, 4
        "Function_5_17E5",         # 05, 5
        "Function_6_24AA",         # 06, 6
        "Function_7_24F5",         # 07, 7
    ))


    def Function_0_4D8(): pass

    label("Function_0_4D8")

    Return()

    # Function_0_4D8 end

    def Function_1_4D9(): pass

    label("Function_1_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_END)), "loc_4EB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FE")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_52E")

    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557")
    OP_70(0x11, 0x0)
    Jump("loc_55B")

    label("loc_557")

    OP_70(0x11, 0x1E)

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E")
    OP_70(0x12, 0x0)
    Jump("loc_572")

    label("loc_56E")

    OP_70(0x12, 0x1E)

    label("loc_572")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_4D9 end

    def Function_2_579(): pass

    label("Function_2_579")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x11, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_756")

    label("loc_6B4")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Music trivia: The Sun Fort's music is a joint effort.\x01",
            "Momiyama composed it, while Sonoda and Unisuga\x01",
            "rearranged and fine-tuned it. Codename: XS065UP.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_756")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_579 end

    def Function_3_768(): pass

    label("Function_3_768")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_8F9")

    label("loc_8A3")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Is that a bulge of sepith in your pocket\x01",
            "or are you just happy to see me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8F9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_768 end

    def Function_4_90B(): pass

    label("Function_4_90B")

    EventBegin(0x0)
    OP_E0(0x1)
    SoundLoad(800)
    Fade(1000)
    OP_68(-38000, 7000, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -39800, 6000, 0, 90)
    SetChrPos(0x102, -41300, 6000, -900, 90)
    SetChrPos(0x103, -42200, 6000, 0, 90)
    SetChrPos(0x104, -41300, 6000, 900, 90)
    SetChrPos(0x107, -43300, 6000, -600, 90)
    SetChrPos(0x108, -43300, 6000, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-33000, 7000, 0, 3000)

    def lambda_9D5():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D5)

    def lambda_9EF():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EF)

    def lambda_A09():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A09)
    Sleep(50)

    def lambda_A26():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A26)
    Sleep(50)

    def lambda_A43():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A43)

    def lambda_A5D():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0x258, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A5D)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5300150V#0010F#5PWhat in the world...?\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 7000, 0, 3000)
    SetCameraDistance(42000, 3000)
    OP_6F(0x11)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 7)
    Fade(1000)
    OP_68(-10000, 5000, 0, 0)
    MoveCamera(100, 25, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(38000, 0)
    OP_68(-14000, -5000, 0, 10000)
    MoveCamera(55, 50, 0, 10000)
    SetCameraDistance(36000, 10000)
    OP_6F(0x79)
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0x107,
        "#5300151V#0813FWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300152V#0108FThis shaft looks never-ending.\x01",
            "Where could it lead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300153V#0901FWas all this built hundreds\x01",
            "of years ago, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300154V#0301FFrom up here, I'm guessin' it's at least\x01",
            "a good 500 arge deep.\x02\x03",
            "#5300155V#0306FMan... It's gonna be a pain in the ass\x01",
            "to get all the way down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300156V#0208F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-33000, 7100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -31800, 6000, 0, 90)
    SetChrPos(0x102, -33900, 6000, -900, 90)
    SetChrPos(0x103, -34800, 6000, 0, 90)
    SetChrPos(0x104, -33900, 6000, 900, 90)
    SetChrPos(0x107, -35900, 6000, -600, 90)
    SetChrPos(0x108, -35900, 6000, 600, 90)
    OP_0D()

    def lambda_DC3():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DC3)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E43():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E43)
    Sleep(100)

    def lambda_E53():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E53)

    def lambda_E60():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E60)
    Sleep(50)

    def lambda_E70():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_E70)
    TurnDirection(0x108, 0x103, 500)

    ChrTalk(
        0x101,
        "#5300157V#0011F#5PTio, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300158V#0101F#11PAre you all right?\x01",
            "You look so pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300159V#6P#0206FI am fine.\x02\x03",
            "#5300160V#0208FIt is just that this place triggered\x01",
            "some unpleasant memories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300161V#0003F#5POf that place you mentioned before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300162V#0301F#5PYou mean those bastards' hideout\x01",
            "at the Republic's western border?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300163V#6P#0203F...Yes.\x02\x03",
            "#5300164V#0208FMaybe this shaft was built to be\x01",
            "a staircase toward Gehenna.\x02\x03",
            "#5300165VWhere Aidios was renounced and\x01",
            "the devils were worshiped...\x02\x03",
            "#5300166V#0201FAnd to gain their trust, they sacrificed\x01",
            "humans under the veil of ceremonies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300167V#0106F#11PDisgusting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300168V#0310F#5PHmph... That explains the stench.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)

    ChrTalk(
        0x101,
        (
            "#5300169V#0008F#5PIn that case, I think our mission is clear.\x02\x03",
            "#5300170V#0003FFor the sake of those who helped us\x01",
            "come this far...\x02\x03",
            "#5300171V...and for the girl who's waiting for us\x01",
            "to come home.\x02\x03",
            "#5300172V#0013FIt's our duty to shatter these twisted\x01",
            "delusions and bring them to light.\x02\x03",
            "#5300173VWe'll put an end to all of the suffering\x01",
            "they've caused!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300174V#6P#0205FLloyd...\x02",
    )

    CloseMessageWindow()

    def lambda_130B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_130B)
    Sleep(50)

    def lambda_131B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_131B)
    Sleep(50)

    def lambda_132B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_132B)
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5300175V#6P#0304FSheesh, Lloyd. If it ain't the smell\x01",
            "here that's gonna off me, it'll be\x01",
            "one of your cheesy speeches...\x02\x03",
            "#5300176V#0300FBut, I'm with ya on this one.\x01",
            "Let's give 'em hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300177V#12P#0102FHeehee. Same here!\x02\x03",
            "#5300178V#0103FOur enemy is like a spider,\x01",
            "hiding in the shadows and\x01",
            "pulling the strings of its web.\x02\x03",
            "#5300179V#0100FBut we've come a long way.\x01",
            "We can bring them to justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300180V#6P#0204FIndeed.\x02\x03",
            "#5300181V#0201FWe cannot be defeated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300182V#0800F#12POur strength is yours!\x01",
            "One hundred percent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300183V#0901F#6PYou can count on us to back you up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300184V#0000F#5PAll right. Time to get going, then.\x02\x03",
            "#5300185V#0003FLet's make it official. Lloyd Bannings and\x01",
            "the four members of the Crossbell Police\x01",
            "Department's Special Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300186V#0801F#12P...and senior bracers of the Bracer Guild,\x01",
            "Estelle and Joshua Bright...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5300187V#0007F#5P...will now commence the infiltration and\x01",
            "settle this case once and for all!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-34800, 9000, 0, 0)
    MoveCamera(90, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37000, 0)
    SetChrPos(0x0, -34800, 6000, 0, 90)
    SetChrPos(0x1, -34800, 6000, 0, 90)
    SetChrPos(0x2, -34800, 6000, 0, 90)
    SetChrPos(0x3, -34800, 6000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE4, 7)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_4_90B end

    def Function_5_17E5(): pass

    label("Function_5_17E5")

    EventBegin(0x0)
    OP_E0(0x1)
    SoundLoad(800)
    Fade(1000)
    OP_68(-38000, 7000, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -39800, 6000, 0, 90)
    SetChrPos(0x102, -41300, 6000, -900, 90)
    SetChrPos(0x103, -42200, 6000, 0, 90)
    SetChrPos(0x104, -41300, 6000, 900, 90)
    OP_68(-33000, 7000, 0, 3000)

    def lambda_1879():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1879)
    Sleep(50)

    def lambda_1896():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1896)
    Sleep(50)

    def lambda_18B3():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18B3)
    Sleep(50)

    def lambda_18D0():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18D0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100015V#0010F#5PWhat in the world...?\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 7000, 0, 3000)
    SetCameraDistance(42000, 3000)
    OP_6F(0x11)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 7)
    Fade(1000)
    OP_68(-10000, 5000, 0, 0)
    MoveCamera(100, 25, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(38000, 0)
    OP_68(-14000, -5000, 0, 10000)
    MoveCamera(55, 50, 0, 10000)
    SetCameraDistance(36000, 10000)
    OP_6F(0x79)
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0x102,
        (
            "#0100016V#0108FThis shaft looks never-ending.\x01",
            "Where could it lead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100017V#0301FFrom up here, I'm guessin' it's at least\x01",
            "a good 500 arge deep.\x02\x03",
            "#0100018V#0306FMan... It's gonna be a pain in the ass\x01",
            "to get all the way down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100019V#0208F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-33000, 7100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -31800, 6000, 0, 90)
    SetChrPos(0x102, -33900, 6000, -900, 90)
    SetChrPos(0x103, -34800, 6000, 0, 90)
    SetChrPos(0x104, -33900, 6000, 900, 90)
    OP_0D()

    def lambda_1B9D():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B9D)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1BF9():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BF9)
    Sleep(100)

    def lambda_1C09():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C09)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x101,
        "#0100020V#0011F#5PTio, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100021V#0101F#11PAre you all right?\x01",
            "You look so pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100022V#6P#0206FI am fine.\x02\x03",
            "#0100023V#0208FIt is just that this place triggered\x01",
            "some unpleasant memories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100024V#0003F#5POf that place you mentioned before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100025V#0301F#5PYou mean those bastards' hideout\x01",
            "at the Republic's western border?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100026V#6P#0203F...Yes.\x02\x03",
            "#0100027V#0208FMaybe this shaft was built to be\x01",
            "a staircase toward Gehenna.\x02\x03",
            "#0100028VWhere Aidios was renounced and\x01",
            "the devils were worshiped...\x02\x03",
            "#0100029V#0201FAnd to gain their trust, they sacrificed\x01",
            "humans under the veil of ceremonies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100030V#0106F#11PDisgusting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100031V#0310F#5PHmph... That explains the stench.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0100032V#0008F#5PIn that case, I think our mission is clear.\x02\x03",
            "#0100033V#0003FFor the sake of those who helped us\x01",
            "come this far...\x02\x03",
            "#0100034V...and for the girl who's waiting for us\x01",
            "to come home.\x02\x03",
            "#0100035V#0013FIt's our duty to shatter these twisted\x01",
            "delusions and bring them to light.\x02\x03",
            "#0100036VWe'll put an end to all of the suffering\x01",
            "they've caused!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100037V#6P#0205FLloyd...\x02",
    )

    CloseMessageWindow()

    def lambda_209A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_209A)
    Sleep(50)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0100038V#6P#0304FSheesh, Lloyd. If it ain't the smell\x01",
            "here that's gonna off me, it'll be\x01",
            "one of your cheesy speeches...\x02\x03",
            "#0100039V#0300FBut, I'm with ya on this one.\x01",
            "Let's give 'em hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100040V#12P#0102FHeehee. Same here!\x02\x03",
            "#0100041V#0103FOur enemy is like a spider,\x01",
            "hiding in the shadows and\x01",
            "pulling the strings of its web.\x02\x03",
            "#0100042V#0100FBut we've come a long way.\x01",
            "We can bring them to justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100043V#6P#0204FIndeed.\x02\x03",
            "#0100044V#0201FWe cannot be defeated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100045V#0000F#5PAll right, time to get going then.\x02\x03",
            "#0100046V#0003FLet's make it official. Lloyd Bannings and\x01",
            "the four members of the Crossbell Police\x01",
            "Department's Special Support Section...\x02\x03",
            "#0100047V#0013F#5P...will now commence the infiltration and\x01",
            "settle this case once and for all!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 6)
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x8, 0x0)
    OP_32(0x0, 0x10, 0x3)
    OP_32(0x1, 0x10, 0x3)
    OP_32(0x2, 0x10, 0x3)
    OP_32(0x3, 0x10, 0x3)
    OP_BA(0x0)
    OP_BA(0x1)
    OP_BA(0x2)
    OP_BA(0x3)
    RemoveCraft(0x0, 0xFFFF)
    RemoveCraft(0x1, 0xFFFF)
    RemoveCraft(0x2, 0xFFFF)
    RemoveCraft(0x3, 0xFFFF)
    AddCraft(0x0, 0xFFFF)
    AddCraft(0x1, 0xFFFF)
    AddCraft(0x2, 0xFFFF)
    AddCraft(0x3, 0xFFFF)
    OP_38(0x0, 0x7F, 0x0)
    OP_38(0x1, 0x7F, 0x0)
    OP_38(0x2, 0x7F, 0x0)
    OP_38(0x3, 0x7F, 0x0)
    OP_38(0x0, 0x80, 0x1)
    OP_38(0x1, 0x80, 0x1)
    OP_38(0x2, 0x80, 0x1)
    OP_38(0x3, 0x80, 0x1)
    SubItemNumber(0x270F, 99)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_2468")
    MiniGame(0x2A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_2468")

    AddItemNumber(0x5, 1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_17E5 end

    def Function_6_24AA(): pass

    label("Function_6_24AA")

    OP_25(0x81, 0x64)
    Sleep(200)
    OP_25(0x81, 0x5A)
    Sleep(200)
    OP_25(0x81, 0x50)
    Sleep(200)
    OP_25(0x81, 0x46)
    Sleep(200)
    OP_25(0x81, 0x3C)
    Sleep(200)
    OP_25(0x81, 0x32)
    Sleep(200)
    OP_25(0x81, 0x28)
    Sleep(200)
    OP_25(0x81, 0x1E)
    Sleep(200)
    OP_25(0x81, 0x14)
    Sleep(200)
    OP_25(0x81, 0xA)
    Sleep(200)
    OP_25(0x81, 0x0)
    Return()

    # Function_6_24AA end

    def Function_7_24F5(): pass

    label("Function_7_24F5")

    Sleep(3000)
    Sound(800, 0, 100, 0)
    Return()

    # Function_7_24F5 end

    SaveToFile()

Try(main)
