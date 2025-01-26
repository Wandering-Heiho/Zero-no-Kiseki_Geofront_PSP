from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c000b.bin",                # FileName
        "c000b",                    # MapName
        "c000b",                    # Location
        0x0002,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 3],
    )

    BuildStringList((
        "c000b",                  # 0
        "Wazy",                   # 1
        "Wald",                   # 2
        "列車",                   # 3
        "SE制御",                 # 4
        "Central Square",         # 5
        "West Street",            # 6
        "Administrative District",# 7
        "Residential District",   # 8
        "Entertainment District", # 9
        "East Street",            # 10
        "Downtown District",      # 11
        "Harbor District",        # 12
        "IBC",                    # 13
        "Station Street",         # 14
        "Back Alley",             # 15
        "Ursula Road",            # 16
        "East Crossbell Highway", # 17
        "West Crossbell Highway", # 18
        "Mainz Mountain Path",    # 19
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "Central Square")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "West Street")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "Residential District")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "East Street")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "IBC")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "Station Street")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_3EC",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_4DD",          # 02, 2
        "Function_3_4ED",          # 03, 3
        "Function_4_4FA",          # 04, 4
        "Function_5_271F",         # 05, 5
        "Function_6_274F",         # 06, 6
        "Function_7_278C",         # 07, 7
        "Function_8_27C9",         # 08, 8
        "Function_9_2806",         # 09, 9
        "Function_10_2843",        # 0A, 10
    ))


    def Function_0_3EC(): pass

    label("Function_0_3EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3EC end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DC")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_1_4A4")

    label("loc_4DC")

    Return()

    # Function_1_4A4 end

    def Function_2_4DD(): pass

    label("Function_2_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4EC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_4EC")

    Return()

    # Function_2_4DD end

    def Function_3_4ED(): pass

    label("Function_3_4ED")

    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Return()

    # Function_3_4ED end

    def Function_4_4FA(): pass

    label("Function_4_4FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    LoadChrToIndex("chr/ch02100.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    OP_68(-500, 1300, 16500, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -500, 0, 23500, 180)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -20800, -5000, 17000, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8)
    OP_90(0x101, -11600, -4800, 17000, 270)
    OP_90(0x102, -10200, -3800, 17000, 270)
    OP_90(0x103, -8800, -2800, 17000, 270)
    OP_90(0x104, -7400, -1800, 17000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xB, 0xA)
    OP_49()
    SetChrPos(0xA, -50000, -11500, 7500, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xB, 0x1000)
    OP_7D(0xB4, 0xC8, 0xDC, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetCameraDistance(15500, 3500)

    def lambda_6FE():
        OP_95(0xFE, -500, 0, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FE)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_6F(0x10)
    Sleep(300)
    OP_93(0x9, 0x10E, 0x1F4)
    Sound(1805, 255, 90, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "#0401090V'Station Street, near where the\x01",
            "construction materials are stored.'\x02\x03",
            "#0401091VAskin' me to come here alone in the\x01",
            "middle of the damn night...\x02\x03",
            "#0401092VWhat do those cops think they're\x01",
            "up to?!\x02",
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
    OP_68(-14500, -4200, 16500, 7000)
    MoveCamera(45, 16, 0, 7000)

    def lambda_887():
        OP_95(0xFE, -14500, -5000, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_887)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_6F(0x41)
    Fade(500)
    OP_68(-39500, -8000, 6500, 0)
    MoveCamera(65, 24, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(23000, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0xFA, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 1, 0, 10)
    OP_68(-21500, -8000, 6500, 5000)
    MoveCamera(45, 4, 0, 5000)
    SetCameraDistance(20000, 5000)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(-14500, -4200, 16500, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0x78, 0x0)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    ChrTalk(
        0x9,
        "#0401093V#1605FIs that...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x8,
        "Young Man's Voice",
        (
            "#0401094V#2PThe last train bound for Calvard?\x01",
            "Yes, I believe it was.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x8, 500)
    Fade(1000)
    SetChrPos(0x9, -16000, -5000, 17000, 270)
    SetChrPos(0x8, -24400, -5000, 17000, 90)
    ClearChrFlags(0x8, 0x8)
    OP_68(-18040, -4000, 17740, 0)
    MoveCamera(325, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    Sleep(1)
    OP_68(-21120, -4000, 17740, 1600)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        "#0401095V#11P#1601FWazy?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1435, 255, 90, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#0401096VGood evening, Wald.\x02\x03",
            "#0401097VWhat a beautiful night to bathe in\x01",
            "the mystic moonlight, wouldn't\x01",
            "you agree?\x02",
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

    ChrTalk(
        0x9,
        (
            "#0401098V#11P#1601FYou bastard.\x02\x03",
            "#0401099V#1604FHaha... So this is what that stupid-ass\x01",
            "invite was about.\x02\x03",
            "#0401100V#1602FSo those police punks went and set\x01",
            "me up, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-22590, -4000, 17740, 2000)

    def lambda_C76():
        OP_95(0xFE, -20400, -5000, 17000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C76)
    WaitChrThread(0x9, 1)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#0401101V#1607F#4SFine! They saved me the trouble of looking\x01",
            "for you myself!\x02\x03",
            "#0401102V#3SYou want a fight? 'Cause I'm more than\x01",
            "happy to give you one. Let's end this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401103V#0404FYou know I'm always up for a bit\x01",
            "of late-night wrestling...\x02\x03",
            "#0401104V#0400F...but alas, I am but a mere guest at this\x01",
            "rendezvous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401105V#1601FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0401106V#0402FLook. Here they come.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-16500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x9, -22000, -5000, 17500, 270)
    SetChrPos(0x8, -25000, -5000, 17000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-20500, -4000, 17000, 5500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    OP_0D()
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_F0E():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F0E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x9,
        "#0401107V#1600FYou punks again?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x101,
        (
            "#0401108VSorry to keep the two of you\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    ChrTalk(
        0x8,
        (
            "#0401109V#3P#0404FOh, no. It's a pleasure to be here.\x02\x03",
            "#0401110V#0402FSo, what's this fun anecdote you\x01",
            "promised to share with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401111V#0004F#11PI'm not sure if 'fun' is the right word,\x01",
            "but you'll at least find it interesting.\x02\x03",
            "#0401112V#0000FReady for me to start?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#0401113V#1607FH-Hold the phone!\x02\x03",
            "#0401114VAnecdotes? Fun? What the hell are\x01",
            "you two goin' on about?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0401115V#3P#0406FYou're such a simpleton.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 600)

    ChrTalk(
        0x9,
        "#0401116V#11P#1605FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401117V#3P#0404FSurely you remember the incidents that\x01",
            "occurred five nights ago?\x02\x03",
            "#0401118V#0402FThey're here to tell us who the culprit\x01",
            "was, obviously.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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
        0x9,
        "#0401119V#11P#1605FThe hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401120V#11P#0105FImpressive deduction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0401121V#11P#0200FI assume you already had your own\x01",
            "suspicions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401122V#3P#0403FWell, at first, I thought that one of\x01",
            "my members may have gone a little\x01",
            "cuckoo...\x02\x03",
            "#0401123V#0401F...but as I started to sort things out,\x01",
            "I realized that something was off\x01",
            "about the whole situation.\x02\x03",
            "#0401124VThat goes for the Vipers' side, too.\x02\x03",
            "#0401125V#0406FSadly, that's as far as my reasoning\x01",
            "could take me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401126V#0003F#11PWell, that simplifies the explanation a bit.\x02\x03",
            "#0401127V#0001FWald Wales.\x02\x03",
            "#0401128VI know there are still gaps in our theory.\x02\x03",
            "#0401129VStill, would you listen to what we've\x01",
            "found so far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401130V#11P#1603FTch.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#0401131V#1601FKeep it short.\x02\x03",
            "#0401132VWaste a minute of my time and I'll\x01",
            "bash that baby face of yours in.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-20500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    Sleep(1000)
    SetChrPos(0x9, -22000, -5000, 18000, 90)
    SetChrPos(0x8, -22200, -5000, 16500, 90)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)
    OP_64(0x9)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#0401133V#0003F#11PAnd that's what we've come to with\x01",
            "the information on hand.\x02\x03",
            "#0401134V#0001FMind giving me your thoughts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401135V#1605F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401136V#6P#0406FMy, my. How unexpected.\x02\x03",
            "#0401137VTo think that we played right into\x01",
            "the mafia's hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401138V#0000F#11PDoes that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401139V#11P#0101FYou agree with our theory?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401140V#6P#0402FBut of course.\x02\x03",
            "#0401141VAfter all, Revache sent some of their agents\x01",
            "to visit us already.\x02\x03",
            "#0401142VThey asked us to work for them, promising\x01",
            "us the moon and stars for our service.\x02\x03",
            "#0401143V#0404FNeedless to say, I immediately turned them\x01",
            "down and sent them on their merry way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401144V#0001F#11PI thought as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401145V#11P#0303FThat settles that side, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0401146V#12P#0400FWhat about you, Wald?\x02\x03",
            "#0401147VWere you also tempted into collaboration\x01",
            "with the mafia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0401148V#1603FYeah, 'bout a month ago.\x02\x03",
            "#0401149VThey were actin' all high and mighty, so\x01",
            "I decided to show 'em what real strength\x01",
            "looked like. Sent 'em packin' real fast.\x02\x03",
            "#0401150V#1602FCan't believe they actually had the balls\x01",
            "to pull a fast one on me like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(1808, 255, 90, 0)
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        (
            "#0401152V#1607F#5PWazy! I'm postponing our duel!\x02\x03",
            "#0401153VFirst, I gotta warm up by crushing\x01",
            "the smug mugs of those mobsters!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0401154V#11P#0101FW-Wait! You can't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401155V#11P#0203FSuch a short temper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401156V#0013F#11PCalm down! Acting recklessly will\x01",
            "only lead to--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0401157V#12P#0406FYou really ARE a simpleton.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#0401158V#1601F#5PSay that again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401159V#12P#0400FYou know perfectly well that you don't stand\x01",
            "a chance against the mafia on your own.\x02\x03",
            "#0401160VYou'd be waltzing into the mafia's sights like\x01",
            "a pig to slaughter. You have no chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0401161V#1607FOh, shut it already! We don't know what'll\x01",
            "happen till we try!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401162V#12P#0406FMaybe YOU could survive.\x02\x03",
            "#0401163V#0401FBut what about your poor little Vipers?\x01",
            "Can they catch bullets with their teeth?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#0401164V#1601F#5PGh...\x02\x03",
            "#0401165V#1607FWhat do you propose we do then, ya\x01",
            "bony wiseass?!\x02\x03",
            "#0401166VYou REALLY expect me to just sit here\x01",
            "and swallow the shame of havin' our\x01",
            "men hurt like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0401167V#12P#0409FHah. Of course I don't.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#0401168V#12P#0404FIt's likely just a handful of mafiosos were\x01",
            "involved in this particular scheme.\x02\x03",
            "#0401169VI say we give them a crash course on how\x01",
            "us guys in the Downtown District operate.\x02\x03",
            "#0401170V#0402FCome the final exam, they'll realize exactly\x01",
            "who they're messing with.\x02\x03",
            "#0401171V#0409FI'll require your help, though, Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401172V#1605F#5PYou what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401173V#0011F#11PH-Hold on, you two.\x02\x03",
            "#0401174V#0013FWhat are you planning? If you do\x01",
            "anything to break the law--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#0401175V#6P#0409FOh, relax. You'll be playing the teacher's\x01",
            "assistants, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401176V#0005F#11P...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1430, 255, 90, 0)
    Sleep(300)
    OP_68(-19110, -4000, 16930, 1800)

    def lambda_23BB():

        label("loc_23BB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_23BB")

    QueueWorkItem2(0x9, 2, lambda_23BB)

    def lambda_23CD():

        label("loc_23CD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_23CD")

    QueueWorkItem2(0x102, 2, lambda_23CD)

    def lambda_23DF():

        label("loc_23DF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_23DF")

    QueueWorkItem2(0x104, 2, lambda_23DF)

    def lambda_23F1():
        OP_95(0xFE, -19700, -5000, 16500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23F1)
    WaitChrThread(0x8, 1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#0401178V#6P#0404F#30WIsn't it your responsibility to resolve the\x01",
            "conflict brewing in the Downtown District?\x02\x03",
            "#0401179VI'd claim that makes it your obligation to\x01",
            "'properly educate' the mafia into leaving\x01",
            "everyone down there alone. For good.\x02\x03",
            "#0401180V#20W#0402FWouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401181V#0011F#11PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401182V#5P#0105F(What is he talking about?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401183V#11P#0202F(I do not quite understand, either.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401184V#11P#0309F(Sounds to me like he's just takin'\x01",
            "advantage of poor Lloyd.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401185V#6P#0402FRemember, it was you who bothered to call\x01",
            "us out here to share your grand theory.\x02\x03",
            "#0401186V#0409FIsn't it only natural to see this case through?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x9, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_4FA end

    def Function_5_271F(): pass

    label("Function_5_271F")

    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_2735():
        OP_96(0xFE, 0xEA60, 0xFFFFD314, 0x1D4C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2735)
    WaitChrThread(0xA, 1)
    Return()

    # Function_5_271F end

    def Function_6_274F(): pass

    label("Function_6_274F")


    def lambda_2754():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2754)
    WaitChrThread(0xFE, 1)

    def lambda_2772():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x413C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2772)
    WaitChrThread(0x101, 1)
    Return()

    # Function_6_274F end

    def Function_7_278C(): pass

    label("Function_7_278C")


    def lambda_2791():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2791)
    WaitChrThread(0xFE, 1)

    def lambda_27AF():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x4588, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27AF)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_278C end

    def Function_8_27C9(): pass

    label("Function_8_27C9")


    def lambda_27CE():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27CE)
    WaitChrThread(0xFE, 1)

    def lambda_27EC():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x4010, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27EC)
    WaitChrThread(0x103, 1)
    Return()

    # Function_8_27C9 end

    def Function_9_2806(): pass

    label("Function_9_2806")


    def lambda_280B():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_280B)
    WaitChrThread(0xFE, 1)

    def lambda_2829():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x445C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2829)
    WaitChrThread(0x104, 1)
    Return()

    # Function_9_2806 end

    def Function_10_2843(): pass

    label("Function_10_2843")

    Sound(455, 0, 100, 0)
    Return()

    # Function_10_2843 end

    SaveToFile()

Try(main)
