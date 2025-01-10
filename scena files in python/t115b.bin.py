from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t115b.bin",                # FileName
        "t115b",                    # MapName
        "t115b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 2, 0, 3],
    )

    BuildStringList((
        "t115b",                  # 0
        "Invitee",                # 1
        "Lechter",                # 2
        "犬１",                   # 3
        "犬２",                   # 4
        "犬３",                   # 5
        "SE制御",                 # 6
        "bt114b",                 # 7
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 8, 14, 180)
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
        "BattleInfo_E4", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt114b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch33100.itc",                   # 00
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

    DeclNpc(-90,     0,       -270,    180,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   0.0,                   0.0,                   -1.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 12,  0.0,                   0.0,                   -1.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_42F",          # 02, 2
        "Function_3_46E",          # 03, 3
        "Function_4_4AE",          # 04, 4
        "Function_5_612",          # 05, 5
        "Function_6_1A8E",         # 06, 6
        "Function_7_1AE3",         # 07, 7
        "Function_8_1B38",         # 08, 8
        "Function_9_1B8D",         # 09, 9
        "Function_10_1BE2",        # 0A, 10
        "Function_11_1C3B",        # 0B, 11
        "Function_12_1C94",        # 0C, 12
        "Function_13_2392",        # 0D, 13
        "Function_14_23AE",        # 0E, 14
        "Function_15_23CD",        # 0F, 15
        "Function_16_23F2",        # 10, 16
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42E")
    OP_94(0xFE, 0xFFFFF7A4, 0xFFFFF40C, 0x8CA, 0x8C0, 0x3E8)
    Sleep(300)
    Jump("Function_1_404")

    label("loc_42E")

    Return()

    # Function_1_404 end

    def Function_2_42F(): pass

    label("Function_2_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_43D")
    Jump("loc_46D")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_46D")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_464")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_46D")

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_46D")

    label("loc_46D")

    Return()

    # Function_2_42F end

    def Function_3_46E(): pass

    label("Function_3_46E")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4A7")

    label("loc_4A7")

    Sound(124, 1, 100, 0)
    Return()

    # Function_3_46E end

    def Function_4_4AE(): pass

    label("Function_4_4AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597")

    ChrTalk(
        0xFE,
        (
            "There's still some time left before the\x01",
            "auction, so I'm taking my last look\x01",
            "around the mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "These decorations are mind-blowing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can really feel how much authority\x01",
            "Speaker Hartmann holds.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_60E")

    label("loc_597")


    ChrTalk(
        0xFE,
        "These decorations are mind-blowing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This mansion HAD to be designed by\x01",
            "some famous architect or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60E")

    TalkEnd(0xFE)
    Return()

    # Function_4_4AE end

    def Function_5_612(): pass

    label("Function_5_612")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("apl/ch50357.itc", 0x1F)
    LoadChrToIndex("apl/ch50358.itc", 0x20)
    LoadChrToIndex("apl/ch50359.itc", 0x21)
    LoadEffect(0x0, "eff\\mgm03_00.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    OP_68(-4460, 1750, -10210, 0)
    MoveCamera(30, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16910, 0)
    OP_68(-750, 1750, -5060, 6000)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0xEF, 3, 0, 7)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x1)
    Jump("loc_76B")

    label("loc_716")

    OP_68(4460, 1750, -10210, 0)
    MoveCamera(330, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16910, 0)
    OP_68(750, 1750, -5060, 6000)
    BeginChrThread(0x101, 3, 0, 8)
    BeginChrThread(0xEF, 3, 0, 9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x1)

    label("loc_76B")

    OP_0D()
    Fade(1000)
    OP_68(0, -450, -4840, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15190, 0)
    OP_68(0, 1750, -4840, 4000)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xEF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(
        0x101,
        (
            "#3501009V#5103F#5PHey, Elie.\x02\x03",
            "#3501018V#5108FAbout how much mira do you think it\x01",
            "took to build all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501011V#5306F#11PI'm not sure if I could even put a\x01",
            "price on it, honestly.\x02\x03",
            "#3501012V#5308FI doubt many castles would have\x01",
            "this sort of decor, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_8FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_9EB")

    ChrTalk(
        0x101,
        (
            "#3501013V#5103F#5PHey, Tio.\x02\x03",
            "#3501014V#5108FAbout how much mira do you think it\x01",
            "took to build all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3501015V#5406F#11PThere's not much use in asking me.\x02\x03",
            "#3501016V#5411FI just know it was an absurd amount.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_B00")

    ChrTalk(
        0x101,
        (
            "#3501017V#5103F#5PHey, Randy.\x02\x03",
            "#3501010V#5108FAbout how much mira do you think it\x01",
            "took to build all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501019V#5606F#11PDon't know and don't care.\x02\x03",
            "#3501020V#5601FStill, I bet you could build a small\x01",
            "castle with the mira spent on this\x01",
            "mansion alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B00")

    BeginChrThread(0x9, 3, 0, 10)

    ChrTalk(
        0x101,
        (
            "#3501021V#5106F#5P*sigh* What's with Speaker Hartmann?\x02\x03",
            "#3501022V#5113FI know he's from nobility, but is he really\x01",
            "THAT wealthy?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#3501023V#3507F#4SHey!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BF8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF8)

    def lambda_C05():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C05)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3501024V#5111F#6PWha...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_C91")

    ChrTalk(
        0x102,
        "#3501025V#5301F#12PA-Aren't you...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEE")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_CBF")

    ChrTalk(
        0x103,
        "#3501026V#5401F#12PYou...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEE")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_CEE")

    ChrTalk(
        0x104,
        "#3501027V#5601F#12PThe hell...?!\x02",
    )

    CloseMessageWindow()

    label("loc_CEE")

    OP_64(0x101)
    OP_64(0xEF)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x9,
        (
            "#3501028VOh, what's up, guys?\x02\x03",
            "#3501029VHey, those clothes don't look\x01",
            "too shabby on you.\x02\x03",
            "#3501030VLooks to me like you have some\x01",
            "taste in style after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501031V#5106F#6PYou're one to talk...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(
        0x102,
        "#3501032V#5311F#12PAren't you a bit TOO casual...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_EDB")

    ChrTalk(
        0x103,
        "#3501033V#5411F#12PThe irony is fascinating.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_F2F")

    ChrTalk(
        0x104,
        (
            "#3501034V#5605F#12PYou sure dressed in your Sunday\x01",
            "best, eh, Lechter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2F")


    ChrTalk(
        0x9,
        (
            "#3501035V#3504F#5PHave you heard what Hartmann's been\x01",
            "saying? He's telling guests to make\x01",
            "themselves at home. Don't mind if I do.\x02\x03",
            "#3501036V#3500FBut, enough about my clothes. You\x01",
            "guys look like you're having fun.\x02\x03",
            "#3501037V#3507FWell, you have a long way to go before\x01",
            "you're able to have as much fun as me!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1480, 1750, -4040, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14360, 0)
    SetChrPos(0x9, 0, 0, -1960, 180)
    OP_0D()
    Fade(250)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x5)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501038V#5111F#6PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_A1(0x9, 0x5DC, 0x2, 0x6, 0x7)
    Sleep(500)
    OP_A1(0x9, 0x5DC, 0x2, 0x0, 0x1)
    Sleep(500)
    OP_A1(0x9, 0x5DC, 0x2, 0x2, 0x3)

    ChrTalk(
        0x9,
        (
            "#3501039V#3500F#5PHmm, let's see here...\x02\x03",
            "#3501040V#3509FI think I found the sweet spot.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    SetChrSubChip(0x9, 0x5)
    OP_68(3440, 1950, -3240, 0)
    MoveCamera(29, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14360, 0)
    SetChrPos(0x9, 8330, 350, -1270, 180)
    SetChrPos(0x101, 4120, 0, -1320, 90)
    SetChrPos(0xEF, 2210, 0, -2180, 90)
    OP_68(5440, 1950, -3150, 3000)
    OP_6F(0x1)
    OP_0D()
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(541, 0, 100, 0)
    OP_A1(0x9, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Sleep(300)
    Sound(12, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8330, -1000, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#3501041V#5111F#6PWh-What are you doing?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_138B")

    ChrTalk(
        0x102,
        (
            "#3501042V#5306F#6P#NI'm just as lost as you, Lloyd.\x02\x03",
            "#3501043V#5301FYou know, if you're trying to catch fish\x01",
            "in a fake pond, you're going to be sta--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E0")

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_142B")

    ChrTalk(
        0x103,
        (
            "#3501044V#5406F#6P#NThis man is way too laid-back...\x02\x03",
            "#3501045V#5411FAnd the likelihood of you catching a fish\x01",
            "inside of a manmade pond is--\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E0")

    label("loc_142B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_14E0")

    ChrTalk(
        0x104,
        (
            "#3501046V#5606F#6P#NC'mon, man. I'm all for bein' lazy, but\x01",
            "there's gotta be a limit.\x02\x03",
            "#3501047V#5601FAnd, dude, I doubt you're gonna have\x01",
            "much luck in an indoor po--\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E0")

    Sleep(500)
    OP_A1(0x9, 0x3E8, 0x4, 0x3, 0x4, 0x5, 0x6)

    ChrTalk(
        0x9,
        (
            "#3501048V#40A#3505F#5P#20WHold on one second#1000W...\x01",
            "#20WOh#500W! #20WOh#500W! #20WYeah#500W!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#3501049V#3509F#4S#5P#10AHere we goooo!\x02",
    )

    Sleep(1100)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    Sound(11, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8330, -1000, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x9, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1654")

    ChrTalk(
        0x102,
        "#3501050V#5305F#6P#NDid he just...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C6")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1687")

    ChrTalk(
        0x103,
        "#3501051V#5405F#6P#NNever mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C6")

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_16C6")

    ChrTalk(
        0x104,
        "#3501052V#5605F#6P#NWell, would ya look at that.\x02",
    )

    CloseMessageWindow()

    label("loc_16C6")

    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#3501053V#3500F#5PWhew. I believe that's what the pros\x01",
            "call a 'beaut.'\x02\x03",
            "#3501054V#3504FHmm, I'm sure Noire would appreciate\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501055V#5106F#6PI think that's a kind of goldfish usually\x01",
            "bought for decoration...\x02\x03",
            "#3501056V#5113FWait, can't you see how messed up\x01",
            "this is?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    OP_93(0x9, 0x10E, 0x320)

    ChrTalk(
        0x9,
        (
            "#3501057V#3509F#11PHahaha! See ya later, guys!\x02\x03",
            "#3501058V#3502FI hope you all are able to fish up\x01",
            "something this great, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501059V#5105F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 11)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xEF)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Sleep(500)
    OP_68(2960, 1850, -3490, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3501060V#5112F#5P#40WUh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_19A6")

    ChrTalk(
        0x102,
        "#3501061V#5306F#6PLet's just pretend we didn't see anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A56")

    label("loc_19A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1A13")

    ChrTalk(
        0x103,
        (
            "#3501062V#5411F#6PTrying to understand what just happened\x01",
            "would be a waste of brainpower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A56")

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1A56")

    ChrTalk(
        0x104,
        "#3501063V#5606F#6PIf we let this bother us, he wins.\x02",
    )

    CloseMessageWindow()

    label("loc_1A56")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 0, 0, -1500, 180)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA5, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_612 end

    def Function_6_1A8E(): pass

    label("Function_6_1A8E")

    SetChrPos(0x101, -4000, 0, 10, 90)

    def lambda_1AA4():
        OP_95(0xFE, -1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA4)
    WaitChrThread(0x101, 1)

    def lambda_1AC2():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AC2)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_6_1A8E end

    def Function_7_1AE3(): pass

    label("Function_7_1AE3")

    SetChrPos(0xEF, -5540, 130, 10, 90)

    def lambda_1AF9():
        OP_95(0xFE, -2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1AF9)
    WaitChrThread(0xEF, 1)

    def lambda_1B17():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1B17)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_7_1AE3 end

    def Function_8_1B38(): pass

    label("Function_8_1B38")

    SetChrPos(0x101, 4000, 0, 10, 90)

    def lambda_1B4E():
        OP_95(0xFE, 1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B4E)
    WaitChrThread(0x101, 1)

    def lambda_1B6C():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B6C)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_8_1B38 end

    def Function_9_1B8D(): pass

    label("Function_9_1B8D")

    SetChrPos(0xEF, 5540, 130, 10, 90)

    def lambda_1BA3():
        OP_95(0xFE, 2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1BA3)
    WaitChrThread(0xEF, 1)

    def lambda_1BC1():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1BC1)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_9_1B8D end

    def Function_10_1BE2(): pass

    label("Function_10_1BE2")

    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -10310, 0, -20, 180)

    def lambda_1C03():
        OP_95(0xFE, 0, 0, -250, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C03)
    WaitChrThread(0xFE, 1)

    def lambda_1C21():
        OP_95(0xFE, 0, 0, -3100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C21)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1BE2 end

    def Function_11_1C3B(): pass

    label("Function_11_1C3B")

    OP_93(0xFE, 0x5A, 0x320)

    def lambda_1C47():
        OP_95(0xFE, 15120, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C47)
    WaitChrThread(0xFE, 1)

    def lambda_1C65():
        OP_95(0xFE, 16660, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C65)

    def lambda_1C7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C7F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_1C3B end

    def Function_12_1C94(): pass

    label("Function_12_1C94")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CE1")
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("monster/ch67152.itc", 0x25)
    Jump("loc_1CF3")

    label("loc_1CE1")

    LoadChrToIndex("monster/ch75650.itc", 0x23)
    LoadChrToIndex("monster/ch75651.itc", 0x24)
    LoadChrToIndex("monster/ch75652.itc", 0x25)

    label("loc_1CF3")

    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x4)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DE8")
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DE8")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xA, -14100, 0, -240, 90)
    SetChrPos(0xB, -15770, 0, 850, 90)
    SetChrPos(0xC, -17360, 0, -440, 90)
    SetChrPos(0x101, 6750, 0, -20, 270)
    SetChrPos(0xEF, 8800, 350, 860, 270)
    SetChrPos(0x105, 9500, 350, -880, 270)
    SetChrPos(0x133, 7200, 350, -340, 270)
    OP_68(3000, 1600, -190, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15250, 1500)

    def lambda_1EC2():
        OP_95(0xFE, 2620, 0, 210, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EC2)

    def lambda_1EDC():
        OP_95(0xFE, 3820, 0, 1420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1EDC)

    def lambda_1EF6():
        OP_95(0xFE, 4650, 0, -870, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1EF6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)
    OP_0D()
    Sound(836, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-8950, 1600, -1070, 0)
    MoveCamera(305, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11500, 0)
    SetCameraDistance(14000, 1500)
    BeginChrThread(0xA, 0, 0, 13)
    BeginChrThread(0xB, 0, 0, 13)
    BeginChrThread(0xC, 0, 0, 13)
    BeginChrThread(0xD, 1, 0, 16)

    def lambda_1FCD():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FCD)

    def lambda_1FE2():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FE2)

    def lambda_1FF7():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1FF7)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x133,
        "#3501596V#5805F#1POh, no! That's a lot of doggies!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501597V#0010F#1PNo way... They released the hounds\x01",
            "inside of the mansion?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    Fade(1000)
    OP_68(-2740, 1200, 170, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15230, 0)
    OP_68(1640, 1200, 170, 1200)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 14)
    BeginChrThread(0xB, 0, 0, 14)
    BeginChrThread(0xC, 0, 0, 14)
    SetChrPos(0xA, -610, 0, -20, 90)
    SetChrPos(0xB, -2100, 0, 1450, 90)
    SetChrPos(0xC, -3870, 0, -1040, 90)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_21B3")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_21DA")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_21C9")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_21DA")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_21DA")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_21DA")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2221")

    ChrTalk(
        0x102,
        "#3501598V#0107F#11PWe have to stop them!\x02",
    )

    CloseMessageWindow()
    Jump("loc_229D")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_225D")

    ChrTalk(
        0x103,
        "#3501599V#0207F#11PThey must be stopped!\x02",
    )

    CloseMessageWindow()
    Jump("loc_229D")

    label("loc_225D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_229D")

    ChrTalk(
        0x104,
        "#3501600V#0307F#11PLet's put 'em in the doghouse!\x02",
    )

    CloseMessageWindow()

    label("loc_229D")


    ChrTalk(
        0x105,
        "#3501601V#0407F#12PGet ready!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xA, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 15)
    BeginChrThread(0xC, 3, 0, 15)
    Sleep(200)
    Sound(814, 0, 100, 0)
    SetCameraDistance(12230, 400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x0, 0, 0, 0, 270)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA7, 0)
    EventEnd(0x5)
    Return()

    # Function_12_1C94 end

    def Function_13_2392(): pass

    label("Function_13_2392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23AD")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_13_2392")

    label("loc_23AD")

    Return()

    # Function_13_2392 end

    def Function_14_23AE(): pass

    label("Function_14_23AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23CC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_14_23AE")

    label("loc_23CC")

    Return()

    # Function_14_23AE end

    def Function_15_23CD(): pass

    label("Function_15_23CD")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_15_23CD end

    def Function_16_23F2(): pass

    label("Function_16_23F2")

    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Return()

    # Function_16_23F2 end

    SaveToFile()

Try(main)
