from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r308b.bin",                # FileName
        "r308b",                    # MapName
        "r308b",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r308b",                  # 0
        "Chief Sergei",           # 1
        "Zeit",                   # 2
        "車１",                   # 3
        "To Old Armorica Road",   # 4
        "Sun Fort",               # 5
    ))

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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "To Old Armorica Road")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "Sun Fort")

    ScpFunction((
        "Function_0_1A0",          # 00, 0
        "Function_1_1BD",          # 01, 1
        "Function_2_1CD",          # 02, 2
        "Function_3_1DD",          # 03, 3
        "Function_4_1B44",         # 04, 4
        "Function_5_1BC5",         # 05, 5
    ))


    def Function_0_1A0(): pass

    label("Function_0_1A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BC")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_0_1A0")

    label("loc_1BC")

    Return()

    # Function_0_1A0 end

    def Function_1_1BD(): pass

    label("Function_1_1BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1CC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)

    label("loc_1CC")

    Return()

    # Function_1_1BD end

    def Function_2_1CD(): pass

    label("Function_2_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_1DC")

    Return()

    # Function_2_1CD end

    def Function_3_1DD(): pass

    label("Function_3_1DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02700.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch50520.itc", 0x20)
    LoadChrToIndex("apl/ch50521.itc", 0x21)
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_32(0x6, 0x0, 0x26)
    RemoveCraft(0x6, 0xFFFF)
    OP_38(0x6, 0x80, 0x2)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x442, 0xFF)
    OP_42(0x6, 0x5EC, 0xFF)
    OP_42(0x6, 0x650, 0xFF)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0xD5)
    AddCraft(0x6, 0xD6)
    AddCraft(0x6, 0x118)
    SetChrChipPat(0x6, 0x6, 0x118)
    AddCraft(0x6, 0x13E)
    AddCraft(0x6, 0x150)
    OP_42(0x6, 0x87, 0x0)
    OP_42(0x6, 0x6C, 0x1)
    OP_42(0x6, 0x8D, 0x2)
    OP_42(0x6, 0x7E, 0x3)
    OP_42(0x6, 0x66, 0x4)
    OP_42(0x6, 0x6F, 0x5)
    OP_42(0x6, 0x81, 0x6)
    OP_32(0x7, 0x0, 0x26)
    RemoveCraft(0x7, 0xFFFF)
    OP_38(0x7, 0x80, 0x2)
    OP_38(0x7, 0x81, 0x2)
    OP_38(0x7, 0x82, 0x2)
    OP_38(0x7, 0x83, 0x2)
    OP_38(0x7, 0x84, 0x2)
    OP_38(0x7, 0x85, 0x2)
    OP_38(0x7, 0x86, 0x2)
    OP_42(0x7, 0x447, 0xFF)
    OP_42(0x7, 0x5EC, 0xFF)
    OP_42(0x7, 0x650, 0xFF)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x11D)
    SetChrChipPat(0x7, 0x6, 0x11D)
    AddCraft(0x7, 0x141)
    AddCraft(0x7, 0x150)
    OP_42(0x7, 0x81, 0x0)
    OP_42(0x7, 0x6C, 0x1)
    OP_42(0x7, 0x99, 0x2)
    OP_42(0x7, 0xA3, 0x3)
    OP_42(0x7, 0x7E, 0x4)
    OP_42(0x7, 0x8B, 0x5)
    OP_42(0x7, 0x7B, 0x6)
    OP_68(-70000, 900, 1000, 0)
    MoveCamera(67, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x101, -51300, 0, -2500, 90)
    SetChrPos(0x102, -51800, 0, -1500, 90)
    SetChrPos(0x103, -52800, 0, -3300, 90)
    SetChrPos(0x104, -53300, 0, -2300, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrPos(0x107, -29000, 0, -3100, 270)
    SetChrPos(0x108, -28700, 0, -1900, 270)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -54000, 250, 1400, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x5, 0xA)
    OP_49()
    SetChrPos(0xA, -84000, 100, 1000, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    Sound(485, 0, 100, 0)
    Sleep(300)
    OP_68(-59000, 900, 1000, 5000)
    MoveCamera(67, 17, 0, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_4B7():
        OP_96(0xFE, 0xFFFF2D10, 0x64, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4B7)
    FadeToBright(2000, 0)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x5, 0x20)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    OP_71(0x5, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_79(0x5)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_68(-52000, 1000, -2300, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0xA, -54000, 100, 1500, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5300051V#0013F#5PI can't believe the Ancient Battlefield was\x01",
            "the key all along...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300052V#0101F#5PI never would have thought it was hiding\x01",
            "one of the cult's lodges...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    Sleep(300)
    Sound(1708, 255, 100, 0)
    Sleep(150)

    NpcTalk(
        0x107,
        "Girl's Voice",
        "#5300053V#8AHey, you guys made it!\x02",
    )

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(-50200, 900, -2300, 3500)
    MoveCamera(40, 23, 0, 3500)
    SetCameraDistance(17000, 3500)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)

    def lambda_71D():
        OP_96(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFF3E4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_71D)
    Sleep(200)

    def lambda_73A():
        OP_96(0xFE, 0xFFFF40FC, 0x0, 0xFFFFF894, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_73A)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300054V#6P#0002FEstelle, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300055V#6P#0300FFancy meetin' the two of you here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300056V#0903F#11PYeah, for sure. It sounds like you had\x01",
            "a difficult time getting here, too.\x02\x03",
            "#5300057V#0900FWe just heard all the details from Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300058V#11P#0800FWhile you guys were on your way, we\x01",
            "went ahead and busted that door down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300059V#6P#0205F...\x02",
    )

    CloseMessageWindow()
    OP_68(-24000, 3000, -2000, 3000)
    MoveCamera(75, 5, 0, 3000)
    SetCameraDistance(26500, 3000)

    def lambda_8FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8FF)
    Sleep(100)

    def lambda_90F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_90F)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#5300060V#0201FThat door was previously sealed.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300061V#0806FIt took forever, but we eventually managed\x01",
            "to figure out that weirdo mechanism thingy\x01",
            "keeping us out.\x02\x03",
            "#5300062V#0800FBut anyway, you're good to infiltrate\x01",
            "their lodge now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-50200, 900, -2300, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300063V#6P#0004FThanks, you two. We owe you one.\x02\x03",
            "#5300064V#0001FAs things stand, we plan to corner and\x01",
            "arrest the mastermind, but...\x02\x03",
            "#5300065V...what do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B01():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B01)
    Sleep(50)

    def lambda_B11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B11)
    Sleep(300)

    ChrTalk(
        0x107,
        (
            "#5300066V#11P#0809FHelp you out, duh!\x02\x03",
            "#5300067V#0800FWhy do you think we were waiting\x01",
            "here in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300068V#0900F#11PIt wouldn't feel right to sit here and do nothing\x01",
            "while people are missing, so let us help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300069V#6P#0004FThanks, you guys. The operation will go much\x01",
            "more smoothly with the two of you around.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#5300070V#6P#0001FOh, right. I just remembered that\x01",
            "we have a message for you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd relayed Renne's message from the hospital.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7001", 0)

    ChrTalk(
        0x108,
        "#5300071V#0908F#11PGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300072V#11P#0808FI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300073V#0103F#6PShe's giving you one last chance to\x01",
            "capture her...\x02\x03",
            "#5300074V#0101FDo you know what she means by that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300075V#11P#0804FYeah.\x02\x03",
            "#5300076V#0800FI'm pretty sure it's one of Renne's\x01",
            "elaborate tests to see if we're\x01",
            "willing to accept every part of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300077V#0903F#11PAnd in order to do that, we'll have to\x01",
            "drag the truth out of that vile man...\x02\x03",
            "#5300078V#0901FHe's largely responsible for that poor\x01",
            "girl's tragic past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300079V#6P#0001FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300080V#6P#0206FI would also like to question him, too.\x02\x03",
            "#5300081V#0208FWhy was he conducting those experiments?\x02\x03",
            "#5300082VFor what purpose did he flee to Crossbell\x01",
            "and complete his Gnosis research?\x02\x03",
            "#5300083V#0201FAnd lastly, what is KeA's true identity, and\x01",
            "what does he have planned for her?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10D1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D1)
    Sleep(100)

    def lambda_10E1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10E1)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x102,
        "#5300084V#0101F#5PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300085V#5P#0303FIn any case, get the handcuffs ready,\x01",
            "'cause this dude is going down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300086V#11P#0003FYeah, we have no choice but to arrest him.\x02\x03",
            "#5300087V#0013FHow else would we free the brainwashed\x01",
            "Guardian Force and secure KeA's safety?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#5300088V#40WSo you're going in, huh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_12CE():

        label("loc_12CE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12CE")

    QueueWorkItem2(0x101, 2, lambda_12CE)
    Sleep(50)

    def lambda_12E3():

        label("loc_12E3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12E3")

    QueueWorkItem2(0x102, 2, lambda_12E3)
    Sleep(50)

    def lambda_12F8():

        label("loc_12F8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12F8")

    QueueWorkItem2(0x103, 2, lambda_12F8)
    Sleep(50)

    def lambda_130D():

        label("loc_130D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_130D")

    QueueWorkItem2(0x104, 2, lambda_130D)

    def lambda_131F():

        label("loc_131F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_131F")

    QueueWorkItem2(0x9, 2, lambda_131F)
    OP_68(-52700, 1000, -1000, 2500)
    MoveCamera(47, 25, 0, 2500)
    SetCameraDistance(16500, 2500)
    BeginChrThread(0x8, 3, 0, 4)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300089V#0005F#11PChief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300090V#11P#0101FYou only just stopped bleeding, so you\x01",
            "shouldn't be moving around yet, Chief!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300091V#5P#1002F#30WHeh. You afraid I'll follow you in?\x01",
            "Not like I can with my leg like this.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)

    ChrTalk(
        0x8,
        (
            "#5300092V#1004F#5P#30WBut at the very least, let me send\x01",
            "you off to your final battle.\x02\x03",
            "#5300093VMy subordinates are finally about to\x01",
            "stand on their own two feet, and I\x01",
            "couldn't be prouder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300094V#0008F#11PChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300095V#12P#0306FGood grief, man. You're gonna make\x01",
            "me all teary-eyed if you keep it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300096V#1002F#5P#30WWhat can I say? I've aged like\x01",
            "a fine wine.\x02\x03",
            "#5300097V#1003FLloyd, Elie, Tio, Randy...\x02\x03",
            "#5300098VIt's been a short four months since you were\x01",
            "assigned to the Special Support Section, but\x01",
            "you've come a long way.\x02\x03",
            "#5300099VIf you end up cracking this case, I'll have to\x01",
            "acknowledge you all as halfway decent cops.\x02\x03",
            "#5300100V#1001FThat's why...as chief of the SSS,\x01",
            "I order you to return safely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300101V#0001F#11PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300102V#11P#0100FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300103V#12P#0202FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300104V#12P#0309FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_E5()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    OP_6F(0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)
    ReplaceBGM("ed7510", "ed7305")
    Sleep(1600)
    OP_68(-29000, 1000, -2000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    OP_90(0x101, -40000, 0, -2000, 90)
    OP_90(0x102, -41300, 0, -2900, 90)
    OP_90(0x103, -41700, 0, -1500, 90)
    OP_90(0x104, -40600, 0, -900, 90)
    OP_90(0x107, -43500, 0, -2500, 90)
    OP_90(0x108, -44000, 0, -1500, 90)
    OP_90(0x9, -53400, 0, -2300, 90)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x8, 0x1)

    def lambda_18C1():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18C1)
    Sleep(50)

    def lambda_18D9():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18D9)
    Sleep(50)

    def lambda_18F1():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18F1)
    Sleep(50)

    def lambda_1909():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1909)
    Sleep(50)

    def lambda_1921():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1921)
    Sleep(50)

    def lambda_1939():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1939)
    SetCameraDistance(17000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)
    OP_4B(0x107, 0xFF)
    OP_4B(0x108, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    Fade(500)
    OP_68(-53500, 2000, -1800, 0)
    MoveCamera(63, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(-53500, 1300, -1800, 5000)
    OP_6F(0x1)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x104, 0xFF)
    OP_4C(0x107, 0xFF)
    OP_4C(0x108, 0xFF)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)
    PlaceName2(340, 200, "c_plac30", 0x0, 2500)
    Fade(500)
    OP_68(-7500, 6200, -2000, 0)
    MoveCamera(50, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(12500, 17200, -2000, 6000)
    MoveCamera(60, 15, 0, 6000)
    SetCameraDistance(25000, 6000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(38500, 21000, -2000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(30000, 0)
    OP_68(51500, 21000, -2000, 4000)
    MoveCamera(60, 27, 0, 4000)
    SetCameraDistance(17000, 4000)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x107, 0xFF)
    EndChrThread(0x108, 0xFF)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("m3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1DD end

    def Function_4_1B44(): pass

    label("Function_4_1B44")

    BeginChrThread(0x8, 0, 0, 0)

    def lambda_1B4F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B4F)

    def lambda_1B60():
        OP_96(0xFE, 0xFFFF2D10, 0xFA, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B60)
    WaitChrThread(0x8, 1)

    def lambda_1B7E():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B7E)
    WaitChrThread(0x8, 1)

    def lambda_1B9C():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B9C)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)
    Return()

    # Function_4_1B44 end

    def Function_5_1BC5(): pass

    label("Function_5_1BC5")

    OP_92(0x8, 0xFFFF3224, 0xFFFFFCE0, 0x1F4)
    BeginChrThread(0x8, 0, 0, 0)

    def lambda_1BDD():
        OP_96(0xFE, 0xFFFF3224, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BDD)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Return()

    # Function_5_1BC5 end

    SaveToFile()

Try(main)
