from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1100",                  # 0
        "Man in Suit",            # 1
        "Man in Suit",            # 2
        "Man in Suit",            # 3
        "Man in Suit",            # 4
        "Garcia",                 # 5
        "To Hotel Delphinia",     # 6
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
    ))

    DeclNpc(-2299,   0,       18149,   180,  453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2299,    0,       18149,   180,  453,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_284",          # 01, 1
        "Function_2_2B3",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_16D5",         # 04, 4
        "Function_5_1713",         # 05, 5
        "Function_6_1758",         # 06, 6
        "Function_7_179D",         # 07, 7
        "Function_8_17B3",         # 08, 8
        "Function_9_17C9",         # 09, 9
        "Function_10_17DF",        # 0A, 10
        "Function_11_17F5",        # 0B, 11
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_20C"),
        (1, "loc_218"),
        (2, "loc_224"),
        (3, "loc_230"),
        (4, "loc_23C"),
        (5, "loc_248"),
        (6, "loc_254"),
        (SWITCH_DEFAULT, "loc_260"),
    )


    label("loc_20C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_218")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_224")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_230")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_23C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_248")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_260")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_283")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_283")

    Return()

    # Function_0_1CC end

    def Function_1_284(): pass

    label("Function_1_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    Event(0, 3)

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)

    label("loc_2B2")

    Return()

    # Function_1_284 end

    def Function_2_2B3(): pass

    label("Function_2_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F3")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1100_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x1, 0x1)
    Jump("loc_317")

    label("loc_2F3")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)

    label("loc_317")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_342")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_342")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_2B3 end

    def Function_3_349(): pass

    label("Function_3_349")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36000.itc", 0x1E)
    LoadChrToIndex("chr/ch36100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    OP_68(0, 1600, -23850, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    SetChrPos(0x101, 0, 0, -21970, 0)
    SetChrPos(0x102, -780, 0, -22750, 0)
    SetChrPos(0x103, 850, 0, -23240, 0)
    SetChrPos(0x104, 180, 0, -24710, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, -22350, 1700)
    Sleep(1500)
    OP_0D()
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
        "#3500343V#0013F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500344V#0301F#11PBigger than I was expectin'...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 200, "c_plac21", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)
    Fade(500)
    OP_68(0, 1600, -22350, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500345V#0001F#5PSo, this is Speaker Hartmann's mansion.\x02\x03",
            "#3500346V#0003FLooking at it... It's more like a castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500347V#0103F#5PWell, his family has been prominent in the\x01",
            "Crossbell social sphere for a long time now.\x02\x03",
            "#3500348V#0100FIt's said this mansion was built as the\x01",
            "governor general's residence during\x01",
            "Imperial reign nearly 100 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500349V#0306F#11PSure, but this is just overkill.\x02\x03",
            "#3500350V#0301FIt ain't like he's some Erebonian noble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500351V#0203F#11PI can see why he holds the auction\x01",
            "in a place like this...\x02\x03",
            "#3500352V#0200FAn estate this large can hold an incredible\x01",
            "amount of people and goods alike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500353V#0008F#5PThat's for su--\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3500354V#0013F#5PThat man...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1500, 26500, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20210, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1500, 25000, 5000)
    SetChrPos(0xC, -10, 800, 29110, 0)
    SetChrPos(0xA, -10, 800, 29110, 0)
    SetChrPos(0xB, -10, 800, 29110, 0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 3, 0, 5)
    Sleep(1000)
    BeginChrThread(0xB, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0xC, 3, 0, 4)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    ChrTalk(
        0xC,
        (
            "#3500355V#3103F#5PSecurity detail is going to be the same as usual.\x02\x03",
            "#3500356V#3101FThough, we're expecting those Heiyue pests\x01",
            "to try and interfere this year.\x02\x03",
            "#3500357VListen up! If someone doesn't have an invitation,\x01",
            "they aren't allowed in. And that's final.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3500358V#12PUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3500359V#6PWhere will you be, Boss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500360V#3104F#5PI'll be watching over things from inside.\x02\x03",
            "#3500361VOne of our enemies is an elusive guy.\x01",
            "Can never be too careful around him.\x02\x03",
            "#3500362V#3100FWhile I'm here, were all the auction\x01",
            "items brought in already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3500363V#6PGot 'em all this morning, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3500364V#6PThat doll or whatever was the last one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500365V#3104F#5PSo that's our centerpiece, is it?\x01",
            "I wonder how much mira that'll go for.\x02\x03",
            "#3500366V#3101FWell, whatever. There's only a few hours until\x01",
            "the doors open.\x02\x03",
            "#3500367VDon't lose focus, boys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3500368V#6PYou got it, Boss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#3500369V#12PYou can count on us!\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_D54():
        OP_95(0xFE, -10, 800, 29110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D54)
    Sleep(1200)

    def lambda_D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D71)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(30)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(1000)
    SetChrPos(0x101, -3000, 0, -28000, 0)
    SetChrPos(0x102, -3570, 0, -29080, 0)
    SetChrPos(0x103, -2930, 0, -30390, 0)
    SetChrPos(0x104, -2350, 0, -28980, 0)
    OP_68(-2890, 3000, -29150, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(15440, 0)
    OP_68(-2890, 1500, -29150, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#3500370V#0301F#6PDamn. I was hoping he would skip.\x02\x03",
            "#3500371VGuess that geezer is focusin' on the\x01",
            "mansion's interior. Fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500372V#0201F#6PA former jaeger will make things more\x01",
            "difficult, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500373V#0103F#6PIf I remember correctly, the party starts\x01",
            "at 7PM tonight.\x02\x03",
            "#3500374V#0101FEven this early, security is already in full swing.\x01",
            "They aren't taking this lightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3500375V#0001F#5PAgreed. That alone shows that they're on guard.\x02\x03",
            "#3500376V#0008FThis is going to be a tough job.\x02\x03",
            "#3500377VEven with the invitation, getting inside the\x01",
            "mansion is going to take some extra effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500378V#0306F#6PThose guys probably know our faces pretty well,\x01",
            "too, given how much trouble we cause 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500379V#0206F#6PWe will need to devise a plan in order\x01",
            "to deceive them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500380V#0003F#5P...\x02\x03",
            "#3500381V#0000FLet's retreat for now.\x02\x03",
            "#3500382VIf we get caught, our entire operation\x01",
            "will be over before it could even start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500383V#0100F#6PRight.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_122B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_122B)
    Sleep(100)

    def lambda_123B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_123B)

    def lambda_1248():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1248)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(-2860, 1500, -32040, 3000)

    def lambda_128E():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_128E)
    Sleep(200)

    def lambda_12A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A6)
    Sleep(200)

    def lambda_12BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12BE)
    Sleep(400)

    def lambda_12D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D6)
    Sleep(1000)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x101, 0x1)
    OP_C7(0x0, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 65, 0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C7(0x1, 0x800)
    FadeToBright(500, 0)
    OP_68(-2860, 1500, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x104, 3, 0, 10)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3500385V#0005F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)

    def lambda_13F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13F0)
    Sleep(100)

    def lambda_1400():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1400)

    def lambda_140D():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_140D)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Fade(1000)
    OP_68(7430, 7600, 6620, 0)
    MoveCamera(329, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(54410, 0)
    OP_68(2020, 7600, 3200, 8000)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(5, 250, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3500386V#0005F#5P#40W(What was that, just now?)\x02\x03",
            "#3500387V#0001F#40W(Was I just hearing things, or...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-2860, 3000, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    OP_68(-2860, 1500, -32040, 4000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x103,
        "#3500388V#0205F#6P#NLloyd? Why did you stop?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#3500389V#0105F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500390V#0008F#5POh, it's nothing...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3500391V#0006F#5PSorry, guys. I think my imagination\x01",
            "was playing tricks on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500392V#0100F#6P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500393V#0300F#12PI dunno what your deal is,\x01",
            "but let's skedaddle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500394V#0200F#6P#N...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0xA4, 1)
    OP_29(0x47, 0x1, 0x2)
    EventEnd(0x5)
    NewScene("t1010", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_349 end

    def Function_4_16D5(): pass

    label("Function_4_16D5")


    def lambda_16DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16DA)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 0, 400, 25800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_16D5 end

    def Function_5_1713(): pass

    label("Function_5_1713")


    def lambda_1718():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1718)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_1713 end

    def Function_6_1758(): pass

    label("Function_6_1758")


    def lambda_175D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_175D)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, -700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1758 end

    def Function_7_179D(): pass

    label("Function_7_179D")


    def lambda_17A2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17A2)
    Return()

    # Function_7_179D end

    def Function_8_17B3(): pass

    label("Function_8_17B3")


    def lambda_17B8():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17B8)
    Return()

    # Function_8_17B3 end

    def Function_9_17C9(): pass

    label("Function_9_17C9")


    def lambda_17CE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17CE)
    Return()

    # Function_9_17C9 end

    def Function_10_17DF(): pass

    label("Function_10_17DF")


    def lambda_17E4():
        OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E4)
    Return()

    # Function_10_17DF end

    def Function_11_17F5(): pass

    label("Function_11_17F5")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18AF")

    ChrTalk(
        0x101,
        (
            "#0001FI want to avoid Revache noticing us\x01",
            "at all costs.\x02\x03",
            "Despite having an invitation, actually\x01",
            "getting inside will be harder than we\x01",
            "thought. What should we do...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A22")

    ChrTalk(
        0x151,
        (
            "#5705FWeren't you all planning to go to the\x01",
            "mall's boutique?\x02\x03",
            "#5702FIf you tried to attend dressed like that,\x01",
            "I'm sure the mafia's reaction would be\x01",
            "priceless. By all means, go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI think I'll take a hard pass on that, Wazy.\x02\x03",
            "#0001FWe should go change clothes first. Then\x01",
            "we can try to fool them into letting us in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A9F")

    label("loc_1A22")


    ChrTalk(
        0x101,
        (
            "#0001FThe mafia is still standing guard outside...\x01",
            "Before heading to the auction, let's change\x01",
            "clothes at the boutique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9F")

    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    OP_68(0, 1600, -1700, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_11_17F5 end

    SaveToFile()

Try(main)
