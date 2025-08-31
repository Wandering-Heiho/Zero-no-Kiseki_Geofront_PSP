from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1210.bin",                # FileName
        "c1210",                    # MapName
        "c1210",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "Cao",                    # 1
        "Heiyue Member",          # 2
        "Lau",                    # 3
        "Yin",                    # 4
        "Detective Emma",         # 5
        "Detective Dudley",       # 6
    ))

    AddCharChip((
        "chr/ch31500.itc",                   # 00
        "chr/ch06300.itc",                   # 01
        "chr/ch31400.itc",                   # 02
        "chr/ch06302.itc",                   # 03
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

    DeclNpc(6000,    0,       0,       270,  261,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-34979,  0,       1870,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-72300,  0,       1900,    2000,    -72300,  1500,    1900,    0x007C, 0,  8,  0x0000)
    DeclActor(-37230,  0,       7940,    2000,    -37230,  1500,    7940,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_334",          # 02, 2
        "Function_3_3E4",          # 03, 3
        "Function_4_453",          # 04, 4
        "Function_5_2919",         # 05, 5
        "Function_6_322D",         # 06, 6
        "Function_7_6BD9",         # 07, 7
        "Function_8_6C2A",         # 08, 8
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7")
    Event(0, 4)
    Jump("loc_311")

    label("loc_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311")
    Event(0, 6)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_320")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_333")
    ClearChrFlags(0x9, 0x80)

    label("loc_333")

    Return()

    # Function_1_2D8 end

    def Function_2_334(): pass

    label("Function_2_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4")
    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_3E3")

    label("loc_3A4")

    SetMapObjFrame(0xFF, "c122_tesri01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae", 0x0, 0x1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    ClearMapObjFlags(0x2, 0x2)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_3E3")

    Return()

    # Function_2_334 end

    def Function_3_3E4(): pass

    label("Function_3_3E4")

    TalkBegin(0xFE)

    NpcTalk(
        0xFE,
        "Man",
        "Our apologies for making you wait.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Man",
        (
            "Right this way. This is the\x01",
            "branch manager's room.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_3E4 end

    def Function_4_453(): pass

    label("Function_4_453")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(-2500, 900, 0, 0)
    MoveCamera(47, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -1900, 0, -600, 90)
    SetChrPos(0x102, -1900, 0, 500, 90)
    SetChrPos(0x103, -3000, 0, -600, 90)
    SetChrPos(0x104, -3000, 0, 500, 90)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Young Man's Voice",
        "#2100977V#6POh, how nice of you to finally visit.\x02",
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
    OP_68(4500, 900, 0, 2000)
    SetCameraDistance(23500, 2000)
    MoveCamera(47, 27, 0, 2000)
    OP_6F(0x11)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5700, 0, -1600, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_92(0x8, 0x125C, 0xFFFFF5D8, 0x1F4)

    def lambda_65C():
        OP_95(0xFE, 4700, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_65C)
    WaitChrThread(0x8, 1)

    def lambda_67A():
        OP_95(0xFE, 200, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_67A)
    Sleep(1300)
    Fade(500)
    OP_68(-530, 1000, 80, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21000, 0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x0)

    ChrTalk(
        0x101,
        (
            "#2100978V#6P#0003FHello.\x02\x03",
            "#2100979V#0000FI'm Lloyd Bannings, of the CPD's\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Eastern Man",
        "#2100980V#3204F#11PA pleasure to meet you.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Young Eastern Man")

    AnonymousTalk(
        0xFF,
        (
            "#2100981VI am Cao Lee, manager of Heiyue\x01",
            "Trading's Crossbell branch.\x02\x03",
            "#2100982VSo, you're Lloyd. And you three\x01",
            "must be... Elie, Randy, and Tio,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2100983V#6P#0011FHow'd you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100984V#0105FMay I ask how you know of our\x01",
            "names already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100985V#3204F#11POf course. Truth be told, I'm an avid reader\x01",
            "of the Crossbell Times.\x02\x03",
            "#2100986V#3200FI was mesmerized by your exploits and\x01",
            "instantly became a fan.\x02\x03",
            "#2100987V#3209FThough boorish of me, I decided to investigate\x01",
            "your backgrounds through various intermediaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100988V#6P#0003FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100989V#0306F#6P(This dude is seriously coming at us\x01",
            "guns blazin'.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100990V#3P#0201F(He is cunning and intelligent...\x01",
            "That much is obvious.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100991V#3209F#11PMake no mistake, it's an honor to meet an\x01",
            "intriguing group like yourselves.\x02\x03",
            "#2100992V#3200FWhat brings you to our office today?\x02\x03",
            "#2100993VDo you take some issue with our\x01",
            "business operations?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100994V#6P#0006FNo, not exactly.\x02\x03",
            "#2100995V#0001FWe're actually in the middle of investigating\x01",
            "an incident involving Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100996V#3205F#11PArc en Ciel, you say? Ah, but of course!\x01",
            "Crossbell's very own prided theatrical\x01",
            "troupe!\x02\x03",
            "#2100997V#3206FI've been meaning to see one of their shows\x01",
            "ever since I came to Crossbell, but work has\x01",
            "kept me oh-so busy, you know.\x02\x03",
            "#2100998V#3200FI seem to recall them having announced\x01",
            "their next production, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100999V#6P#0000FY-Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2101000V#0103FAs a matter of fact, our investigation is related\x01",
            "to an issue with their upcoming show.\x02\x03",
            "#2101001V#0100FWe'd actually like to ask you a few questions\x01",
            "about it, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101002V#3203F#11POh, dear. It sounds like quite the predicament\x01",
            "has transpired.\x02\x03",
            "#2101003V#3200FVery well. I shall comply with your request.\x01",
            "Free of charge, of course.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21300, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(270, 800, 4510, 0)
    MoveCamera(69, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrPos(0x101, -2600, 50, 4000, 90)
    SetChrPos(0x102, -2600, 50, 5000, 90)
    SetChrPos(0x103, -2600, 0, 2200, 45)
    SetChrPos(0x104, -2300, 0, 1400, 45)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 750, 50, 4500, 270)
    SetCameraDistance(20500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        "#2101004V#5P#3203FHmm... Yin, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101005V#6P#0000FWe're aware that Heiyue's main office is\x01",
            "located in the Republic's Eastern Quarter.\x02\x03",
            "#2101006VIt occurred to me that you might actually be\x01",
            "familiar with Yin due to that fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101007V#5P#3204FImpressive deduction.\x02\x03",
            "#2101008V#3200FAm I to assume that you're implying\x01",
            "that I have connections to Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101009V#6P#0003FNo, of course not.\x02\x03",
            "#2101010V#0000FWe haven't found a reliable lead...yet.\x01",
            "And no offense, but we left visiting your\x01",
            "office as a last resort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101011V#5P#3204FNone taken. So that's your game, then?\x02\x03",
            "#2101012V#3200FYou intend to seek any information you can.\x01",
            "Listen closely, then. I shall recall a Calvardian\x01",
            "legend sure to reveal deeper insight into Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101013V#6P#0001FWe're listening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101014V#5P#3200FThe name Yin holds a particularly strong\x01",
            "influence within the Eastern Quarter.\x02\x03",
            "#2101015V#3203FGarbed in a mask and shawl of ebony, no\x01",
            "one has gazed at the assassin's true face...\x02\x03",
            "#2101016VHe appears like a shadow and vanishes like a\x01",
            "phantom... His prey has never once escaped.\x02\x03",
            "#2101017V#3201FAnd though it may seem preposterous...some\x01",
            "say Yin may be immortal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2101018V#6P#0005FI-Immortal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101019V#0101F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101020V#5P#3203FWell, documents show that Yin has been operating\x01",
            "as an assassin for at least a century.\x02\x03",
            "#2101021VHis rise into legend began shortly after the\x01",
            "democratization of the Calvard Republic.\x02\x03",
            "#2101022V#3201FIf you were to examine records from that time,\x01",
            "Yin's name is frequently mentioned.\x02\x03",
            "#2101023VThe demon draped in black sent one prominent\x01",
            "figure after another to their grave during this\x01",
            "chaotic period in history.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#2101024V#6P#0003FThis story is getting more unbelievable\x01",
            "by the second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2101025V#0300F#4PIsn't it just a spooky legend to keep\x01",
            "the kiddos under control?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2101026V#5P#3209FNo, Mr. Orlando... Yin is very real.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#2101027V#6P#0013F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101028V#0301F#4PExcuse me?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20300, 60000)

    ChrTalk(
        0x8,
        (
            "#2101029V#5P#3202FYin far surpasses a mere tall tale in the\x01",
            "underworld of the Eastern Quarter.\x02\x03",
            "#2101030VThough his true identity is unknown, Zemuria's\x01",
            "greatest assassin can be employed for the\x01",
            "right price and under the right conditions.\x02\x03",
            "#2101031VA master of all assassination techniques,\x01",
            "a dark martial artist with incredible\x01",
            "dexterity and agility.\x02\x03",
            "#2101032VNo one dares deny his existence...\x02\x03",
            "#2101033V#3204FA certain organization highly values Yin\x01",
            "and entrusts many jobs to him, or so\x01",
            "the rumor goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101034V#0101F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101035V#0201F#12PThe organization you are referring to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101036V#5P#3205FAh, yes. That reminds me.\x01",
            "While we're on the topic of Yin...\x02\x03",
            "#2101037VI've heard recent claims of Yin having vanished\x01",
            "entirely from the Eastern Quarter.\x02\x03",
            "#2101038V#3204FIt has come to my attention that Yin has accepted\x01",
            "a hefty job from the aforementioned organization.\x02\x03",
            "#2101039V#3202FApparently, Yin left for a certain autonomous\x01",
            "state we're all familiar with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101040V#6P#0013FI don't like what you're implying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101041V#5P#3202FWhat's the matter?\x02\x03",
            "#2101042VI haven't given you the name of the\x01",
            "organization, have I?\x02\x03",
            "#2101043V#3209FI just can't help but wonder what state they might\x01",
            "be traveling to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101044V#6P#0010FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101045V#0103F#6PYou and Revache are one and the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101046V#5P#3204FOh, please. Refrain from comparing Heiyue\x01",
            "to that measly, local gang. Or at least, that's\x01",
            "what I'd like to say.\x02\x03",
            "#2101047VQuite frankly, I'm more than impressed with\x01",
            "how well they've managed to adapt to this\x01",
            "peculiar city.\x02\x03",
            "#2101048V#3200FThose persistent little pests have caused\x01",
            "nothing but trouble for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101049V#0301F#4PYou fessin' up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2101050V#0211F#12PHe went straight to the point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101051V#5P#3209FI am merely referring to them as our\x01",
            "fellow business competitors.\x02\x03",
            "#2101052V#3200FState law protects competition between\x01",
            "businesses and free trade, you know.\x02\x03",
            "#2101053VDo you take issue with that, officers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101054V#6P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2101055V#6P#0003FLet me ask you this one final question.\x02\x03",
            "#2101056V#0001FHas Arc en Ciel been caught in the crossfire\x01",
            "between you and Revache?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2101057V#5P#3205FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101058V#6P#0001FWe just received information about Revache's\x01",
            "proposal for Arc en Ciel to perform in the\x01",
            "Imperial capital.\x02\x03",
            "#2101059VWere you considering a similar proposal, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101060V#5P#3204FI have no problem admitting that certain\x01",
            "crowds in the Republic wish to be graced\x01",
            "by their presence.\x02\x03",
            "#2101061VHowever, our company is unconcerned with petty\x01",
            "matters such as the entertainment industry.\x02\x03",
            "#2101062V#3201FI certainly am perplexed, though.\x02\x03",
            "#2101063VWhy exactly was the threat letter signed\x01",
            "with the name of an assassin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101064V#6P#0006FThat's what I intend to find out.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2300, 0, 4000, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#2101065V#6P#0003FThank you for your time, Cao.\x01",
            "We appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24FD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24FD)
    Sleep(100)

    def lambda_250D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_250D)
    Sleep(300)

    ChrTalk(
        0x103,
        "#2101066V#0205F#11PLloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2101067V#0301F#11PYou sure you're good, man?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2101068V#0006F#5PI doubt we'd get much more out of him if\x01",
            "we stayed any longer.\x02\x03",
            "#2101069V#0000FAnd besides, Cao already seems more than\x01",
            "busy enough. So, if you'll excuse us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2101070V#0108F#5PLloyd's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101071V#5P#3204FAny time, my friend. Any time at all.\x02\x03",
            "#2101072V#3205FOne more thing before you leave, Detective Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    def lambda_26F2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_26F2)

    ChrTalk(
        0x101,
        "#2101073V#6P#0013FWhat do you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101074V#5P#3200FCome, now. Don't look so displeased.\x02\x03",
            "#2101075VDo you recall me saying that I'm a\x01",
            "big fan of the SSS? Believe me\x01",
            "when I say that was no lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101076V#6P#0011FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101077V#5P#3204FI must say... This current investigation\x01",
            "of yours absolutely fascinates me.\x02\x03",
            "#2101078VAs one of your fans, I can hardly wait\x01",
            "to see how you'll resolve this one.\x02\x03",
            "#2101079V#3202FI am most certainly looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_453 end

    def Function_5_2919(): pass

    label("Function_5_2919")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    LoadEffect(0x0, "event\\ev202_00.eff")
    OP_68(6280, 900, 1830, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21760, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 5800, 0, 3300, 180)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        "#2201803VYou've truly saved me. I appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20760, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#2201804V#11P#3206FIf the situation were to progress any further\x01",
            "down the rabbit hole, it would have gotten\x01",
            "quite messy.\x02\x03",
            "#2201805VThat was a close call... We were almost\x01",
            "suspected of attempting to assassinate\x01",
            "the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201806V\x07\x03",
            "#5P#0700FHmph... Because of your connections within\x01",
            "the Republican Faction.\x02\x03",
            "#2201807VThe leader of the Imperial Faction, Speaker\x01",
            "Hartmann, was likely the one to utter my\x01",
            "name to that secretary.\x02\x03",
            "#2201808VIt's likely that he learned of it through Revache's\x01",
            "don, Marconi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201809V\x07\x00",
            "#11P#3204FYes, I'm inclined to agree.\x02\x03",
            "#2201810VI must say, I wasn't expecting the secretary\x01",
            "to go so far as to plan an assassination.\x02\x03",
            "#2201811V#3200FEven so, there is no mistaking that his\x01",
            "objective was to harm the Republican\x01",
            "Faction's reputation through us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201812V\x07\x03",
            "#5P#0702FHmph. A truly problematic city.\x02\x03",
            "#2201813V#0700FPutting that aside...\x01",
            "Do not lump 'us' together.\x02\x03",
            "#2201814VIt's particularly irritating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201815V\x07\x00",
            "#11P#3206FOh, dear. How cold you are.\x02\x03",
            "#2201816V#3200FWell, no matter. Our ties with the members of\x01",
            "the Republican Faction can be severed at\x01",
            "a moment's notice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5630, 0, -1610, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x8, 0x2D, 0x190)
    OP_68(7110, 900, 1620, 1500)
    SetChrFlags(0x8, 0x4)

    def lambda_2EFD():
        OP_96(0xFE, 0x1C84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EFD)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x190)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#2201817V#5P#3204FAnd as we previously discussed, Heiyue's\x01",
            "counteroffensive will launch after the festival.\x02\x03",
            "#2201818V#3210FWe'll leave the operation on the festival's\x01",
            "final day in your hands, Master Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2201819V\x07\x03",
            "#0702F#5PVery well.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x190)
    Sound(1569, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#2201821V\x07\x03",
            "#0700F#5PIt's time. I'll be taking my leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0xFF, 0xB, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0xB, 0x1E, 0x12C)

    def lambda_30B2():
        OP_95(0xFE, 7300, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_30B2)

    def lambda_30CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_30CC)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(1000)
    OP_68(7300, 900, 1000, 2000)
    MoveCamera(40, 17, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2201822V\x07\x00",
            "#5P#3209FHaha... Ever the elusive phantom, are we?\x02\x03",
            "#2201823V#3210F'Time'...?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_6F(0x10)

    ChrTalk(
        0x8,
        "#2201824V#11P#3204FWhat exactly is it 'time' for, I wonder.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2919 end

    def Function_6_322D(): pass

    label("Function_6_322D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch50237.itc", 0x20)
    OP_68(1100, 1100, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -4300, 0, 0, 90)
    SetChrPos(0x102, -4300, 0, 0, 90)
    SetChrPos(0x103, -4300, 0, 0, 90)
    SetChrPos(0x104, -4300, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 2200, 0, 0, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 2800, 0, -1000, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -200, 0, 900, 90)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 300, 0, 0, 90)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xD,
        (
            "#4200076VCao.\x01",
            "My apologies for intruding on you.\x02\x03",
            "#4200077VWe wish to collaborate with you,\x01",
            "so would you be willing to share\x01",
            "details of the raid with us?\x02",
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
        0x8,
        (
            "#4200078V#3204F#11PYou'll have to forgive me. After all, it was\x01",
            "late into the night...\x02\x03",
            "#4200079V#3200FI haven't the foggiest idea of who the\x01",
            "assailants may be, or why they targeted\x01",
            "our humble company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200080V#6P#0603FEven so, it appears you were able to\x01",
            "mount an efficient defense.\x02\x03",
            "#4200081V#0600FThe first and second floors are devastated,\x01",
            "yet this room remains spotless.\x02\x03",
            "#4200082VHow in the world were you able to fend off\x01",
            "assailants armed with heavy machine guns?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200083V#3209F#11PI'll admit, it was tricky.\x02\x03",
            "#4200084V#3200FHowever, the assailants managed to\x01",
            "escape our grasp, I'm afraid.\x02\x03",
            "#4200085V#3206FMany of our men were sent to St. Ursula.\x01",
            "Dear, oh, dear. What a disaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200086V#6P#0603FYou have my condolences.\x01",
            "If you'll--\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -4800, -1000, 0, 90)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#4200087V#2PExcuse us.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    OP_68(-500, 1100, 0, 1500)
    SetCameraDistance(24000, 1500)
    SetChrPos(0x101, -4300, 0, 0, 90)

    def lambda_3882():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3882)

    def lambda_389C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_389C)

    def lambda_38AD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_38AD)
    Sleep(50)

    def lambda_38BD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_38BD)

    def lambda_38CA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_38CA)
    Sleep(50)

    def lambda_38DA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_38DA)
    Sleep(150)

    def lambda_38EA():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38EA)

    def lambda_3904():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3904)
    Sleep(400)

    def lambda_3918():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3918)

    def lambda_3932():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3932)
    Sleep(350)

    def lambda_3946():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3946)

    def lambda_3960():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3960)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#4200088V#11P#0605FYou four?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#4200089V#5PWh-What's the Special Support Section doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200090V#11P#3205FWhy, good morning, Detective Bannings.\x01",
            "I see the rest of you are in attendance, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200091V#6P#0003FPardon our interruption, Cao.\x02\x03",
            "#4200092V#0000FI know you're busy with the aftermath of the raid,\x01",
            "but could I borrow a minute of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200093V#11P#3204FAnything for you, my friend.\x02\x03",
            "#4200094V#3210FIf you'll excuse us then, Dudley.\x01",
            "I appreciate you having stopped by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4200095V#11P#0610FDamn...! We'll step aside, then.\x02",
    )

    CloseMessageWindow()

    def lambda_3BE8():

        label("loc_3BE8")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3BE8")

    QueueWorkItem2(0x101, 2, lambda_3BE8)

    def lambda_3BFA():

        label("loc_3BFA")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3BFA")

    QueueWorkItem2(0x102, 2, lambda_3BFA)

    def lambda_3C0C():

        label("loc_3C0C")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3C0C")

    QueueWorkItem2(0x103, 2, lambda_3C0C)

    def lambda_3C1E():

        label("loc_3C1E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3C1E")

    QueueWorkItem2(0x104, 2, lambda_3C1E)

    def lambda_3C30():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C30)

    def lambda_3C4A():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C4A)
    Sleep(200)

    def lambda_3C67():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3C67)

    def lambda_3C74():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C74)

    def lambda_3C8E():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C8E)
    Sleep(500)
    OP_68(-820, 1100, 110, 1000)

    def lambda_3CBC():
        OP_96(0xFE, 0xFFFFF768, 0x0, 0x0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3CBC)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#4200096V#12P#0603F(This irritates me to no end, but...\x01",
            "I'm leaving this snake to you.)\x02\x03",
            "#4200097V#0600F(Try to get what you can out of him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200098V#0005F#5P(Ah... Yes, sir!)\x02",
    )

    CloseMessageWindow()

    def lambda_3DB5():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3DB5)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 7)
    Sleep(100)

    def lambda_3DDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3DDB)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sound(104, 0, 100, 0)
    OP_68(1100, 1000, 0, 1500)
    SetCameraDistance(22500, 1500)
    OP_92(0x101, 0xFFFFFF38, 0xFFFFFDA8, 0x1F4)

    def lambda_3E49():
        OP_95(0xFE, -200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E49)
    OP_92(0x102, 0xFFFFFF38, 0x1F4, 0x1F4)

    def lambda_3E70():
        OP_95(0xFE, -200, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E70)
    OP_92(0x103, 0xFFFFFA88, 0xFFFFFDA8, 0x1F4)

    def lambda_3E97():
        OP_95(0xFE, -1400, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E97)
    OP_92(0x104, 0xFFFFFA88, 0x1F4, 0x1F4)

    def lambda_3EBE():
        OP_95(0xFE, -1400, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EBE)
    WaitChrThread(0x101, 1)

    def lambda_3EDC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EDC)
    WaitChrThread(0x102, 1)

    def lambda_3EED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3EED)
    WaitChrThread(0x103, 1)

    def lambda_3EFE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3EFE)
    WaitChrThread(0x104, 1)

    def lambda_3F0F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F0F)
    WaitChrThread(0x104, 2)
    OP_6F(0x11)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 40, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#4200099VIt has been quite some time, my friends.\x02\x03",
            "#4200100VI hear you all had quite the adventure\x01",
            "on the final day of the Anniversary\x01",
            "Festival, correct?\x02",
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
        0x101,
        (
            "#4200101V#6P#0003FI'm assuming Yin has already informed you.\x02\x03",
            "#4200102V#0001FAs you know, the Special Support Section doesn't\x01",
            "follow conventional investigative protocol.\x02\x03",
            "#4200103VAnd with that in mind, how about you go ahead\x01",
            "and tell us your true intentions?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    def lambda_41B2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_41B2)
    Sleep(50)

    def lambda_41C2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_41C2)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x8,
        "#4200104V#3210F#11POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200105V#0105F#5PL-Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200106V#5P#0006FThere's no point wasting our time with\x01",
            "his usual song and dance.\x02\x03",
            "#4200107V#0000FNot only that, but we have a lot of ground\x01",
            "to cover with Cao. I figured I'd get straight\x01",
            "to the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200108V#6P#0306FWhoa. Pretty gutsy move, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200109V#6P#0202FLloyd can be quite audacious when he\x01",
            "wants to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4200110V#3202F#11PHaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        "#4200111V#11P#3209F#4SHahahaha!\x02",
    )

    CloseMessageWindow()

    def lambda_43B4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43B4)

    def lambda_43C1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_43C1)

    def lambda_43CE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_43CE)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#4200112V#3204F#11PExactly as I had anticipated, Mr. Bannings!\x01",
            "I knew I was right to have hopes of you.\x02\x03",
            "#4200113V#3210FVery well. I'm not particularly fond of trivial\x01",
            "exchanges, anyway.\x02\x03",
            "#4200114VIf your questions are within the realm of my\x01",
            "knowledge, I will provide the answers you seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200115V#6P#0004FThank you, Cao.\x02\x03",
            "#4200116V#0001FI wanted to ask you about these three topics.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_45B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4652")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The Assailant's True Identity]\x01",      # 0
            "[Future Interactions]\x01",                # 1
            "[KeA's Identity]\x01",                     # 2
            "[No Further Questions]\x01",               # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_46BD")

    label("loc_4652")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The Assailant's True Identity]\x01",      # 0
            "[Future Interactions]\x01",                # 1
            "[KeA's Identity]\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_46BD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46DF"),
        (1, "loc_51B5"),
        (2, "loc_5ABF"),
        (3, "loc_655C"),
        (SWITCH_DEFAULT, "loc_6564"),
    )


    label("loc_46DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_503C")

    ChrTalk(
        0x101,
        (
            "#4200117V#6P#0001FIs it safe to assume Revache is\x01",
            "behind last night's raid?\x02\x03",
            "#4200118VCan you say for certain that there's any chance\x01",
            "it was carried out by a third party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200119V#3200F#11PDoubting the possibility entirely, are we?\x02\x03",
            "#4200120V#3204FIf you would elaborate for them, Lau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4200121V#11PSir.\x02",
    )

    CloseMessageWindow()

    def lambda_482E():
        OP_96(0xFE, 0x834, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_482E)
    WaitChrThread(0xA, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#4200122V#11PThe assailants may have been masked to\x01",
            "conceal their identities, but there's no\x01",
            "doubt it was Revache's men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200123V#11PTheir weapons and combat style were\x01",
            "completely identical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200124V#11PThose types of things would be difficult\x01",
            "to replicate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200125V#6P#0005FThat does make sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200126V#6P#0306FIn that case, something's still rubbin'\x01",
            "me the wrong way.\x02\x03",
            "#4200127V#0301FI hear you Heiyue dudes are all pretty damn\x01",
            "good martial artists.\x02\x03",
            "#4200128V#0300FYour main man Lau here looks like he could\x01",
            "hand out beatings left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4200129V#11PYou flatter me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200130V#6P#0303FI'm sure Revache doesn't have a shortage\x01",
            "of combat pros, but none of them could\x01",
            "match up with you guys one-on-one.\x02\x03",
            "#4200131VSo then, how'd you guys get trashed so\x01",
            "hard by a handful of their thugs?\x02\x03",
            "#4200132V#0301FWas that old Killing Bear leadin' the charge\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200133V#3204F#11PNo. I don't believe the esteemed general manager\x01",
            "of sales was present.\x02\x03",
            "#4200134V#3200FNeither were his hand-picked ex-jaeger friends.\x02\x03",
            "#4200135VWe believe Revache's regular combat personnel to\x01",
            "be behind the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200136V#6P#0013FIf that's the case, then how?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200137V#11PThough their techniques were simple, their speed\x01",
            "and power were beyond comprehension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200138V#11PThey were able to brandish those heavy machine\x01",
            "guns single-handedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#4200139V#11POur defenses were easily crushed by their\x01",
            "unnatural strength. They overtook the first\x01",
            "two floors with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200140V#6P#0301FNo foolin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200141V#6P#0201F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200142V#3200F#11PIt wasn't only limited to their power and speed,\x01",
            "either. They had inhuman endurance, as well.\x02\x03",
            "#4200143V#3204FAnd thanks to that, I had to put into practice\x01",
            "a few dangerous techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200144V#0101FD-Dangerous techniques?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200145V#6P#0001FYou seem pretty knowledgeable about combat\x01",
            "yourself, Cao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200146V#3210F#11PI am nothing but an amateur\x01",
            "compared to Master Yin.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_5018():
        OP_96(0xFE, 0xAF0, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5018)
    WaitChrThread(0xA, 1)
    Sleep(300)
    SetScenarioFlags(0x0, 0)
    Jump("loc_51B0")

    label("loc_503C")


    ChrTalk(
        0x8,
        (
            "#4200147V#3204F#11PThe assailants' identities may have been\x01",
            "concealed with their masks, but they were\x01",
            "most certainly members of Revache.\x02\x03",
            "#4200148V#3200FTheir tactics were simple, but their power\x01",
            "and speed were beyond belief. Their\x01",
            "endurance was most impressive, too.\x02\x03",
            "#4200149V#3209FI'm most curious to find out what means\x01",
            "they went through to attain such strength.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B0")

    Jump("loc_6564")

    label("loc_51B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5983")

    ChrTalk(
        0x101,
        (
            "#4200150V#6P#0003FI'll get straight to the point, Cao.\x02\x03",
            "#4200151V#0001FHow do you plan to respond to their raid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200152V#3210F#11POh...\x01",
            "What kind of question is that?\x02\x03",
            "#4200153VTake a moment to ponder on what kind of\x01",
            "organization Heiyue is. You've found your\x01",
            "answer, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200154V#6P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200155V#0103FSo, you're after revenge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200156V#3204F#11POh, please. Keep such scandalous rumors\x01",
            "to yourself.\x02\x03",
            "#4200157VI've been merely referring to crisis management.\x01",
            "At the end of the day, we only seek profits.\x02\x03",
            "#4200158V#3210FAnd in situations where our profits are threatened,\x01",
            "it is my sworn duty to crush our antagonizers\x01",
            "through the appropriate methods.\x02\x03",
            "#4200159VI fail to see what's so strange about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200160V#6P#0301FYeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200161V#6P#0211FWhat an annoyingly shrewd man.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4200162V#6P#0001FDoes requesting assistance from Heiyue's\x01",
            "main office lie among those 'proper methods'?\x02",
        )
    )

    CloseMessageWindow()
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
        0x102,
        "#4200163V#0108FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200164V#6P#0301FHe's callin' in the big guns from\x01",
            "Heiyue's main office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200165V#3209F#11PAwfully blunt, aren't we?\x02\x03",
            "#4200166V#3204FMy reputation is on the line. I have no\x01",
            "such plans at this moment.\x02\x03",
            "#4200167V#3210FFurthermore, there is no guarantee the\x01",
            "main office will respect my wishes.\x01",
            "They may intervene regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200218V#6P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200169V#3200F#11PWell, I should be able to stave off direct\x01",
            "intervention for a little while, at least.\x02\x03",
            "#4200170V#3204FEither way, we lack the proper knowledge\x01",
            "on Revache's current state, so we don't have\x01",
            "an effective countermeasure for them.\x02\x03",
            "#4200171VWe're simply investigating their movements\x01",
            "for the time being...\x02\x03",
            "#4200177V#3200F...through our most reliable and cooperative\x01",
            "employee, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200173V#6P#0205FYou requested Yin's assistance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200174V#6P#0306FHe's the best of the best for these kinda\x01",
            "undercover missions, yeah?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5ABA")

    label("loc_5983")


    ChrTalk(
        0x8,
        (
            "#4200175V#3204F#11PIt's entirely possible the main office will decide\x01",
            "to intervene. However, we plan to deal with\x01",
            "the situation ourselves for as long as we can.\x02\x03",
            "#4200176V#3200FWe're simply investigating their movements\x01",
            "for the time being.\x02\x03",
            "#4200172VBy our most reliable and cooperative\x01",
            "employee, in fact.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABA")

    Jump("loc_6564")

    label("loc_5ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6432")

    ChrTalk(
        0x101,
        (
            "#4200178V#6P#0003FThis isn't directly related to the case\x01",
            "in question...But, I figured I'd ask while I'm already here.\x02\x03",
            "#4200179V#0001FDo you really not know anything about KeA?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B86():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5B86)
    Sleep(50)

    def lambda_5B96():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5B96)
    Sleep(300)

    ChrTalk(
        0x103,
        "#4200180V#6P#0205FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200181V#0101F#5PAre you sure, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200182V#3205F#11PHmm... KeA, you said?\x02\x03",
            "#4200183V#3209FIs that a person's name?\x01",
            "Or perhaps, some kind of code?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200184V#6P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200185V#3206F#11PForgive me for speaking out of line.\x01",
            "You're more serious than I expected.\x02\x03",
            "#4200186V#3200FAll I know is that KeA is the name of that\x01",
            "little girl you took into custody after the\x01",
            "Schwarze Auction.\x02\x03",
            "#4200187VWell, and that our dear collaborator offered\x01",
            "you a small piece of advice there.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#4200188V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "The exhibits for the second half of the auction\x01",
            "are all stored in the room over there.\x02\x03",
            "#4200189VAccording to information that was sent to\x01",
            "Heiyue, there's a 'bomb,' so to speak, among\x01",
            "those items.\x02\x03",
            "#4200190VI recommend you confirm it for yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)

    def lambda_5EF7():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5EF7)

    def lambda_5F04():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5F04)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#4200191V#3203F#11P'A large, leather trunk will be exhibited in the\x01",
            "second half of the auction.'\x02\x03",
            "#4200192V'Inside the trunk is a bomb, which will only\x01",
            "serve to jeopardize Revache's position.'\x02\x03",
            "#4200193V#3201FWe were able to receive that piece of\x01",
            "information via our own networks.\x02\x03",
            "#4200194VWe've had no means of discerning who this\x01",
            "informant was, as of yet. However, in some\x01",
            "ways, that only made it more credible.\x02\x03",
            "#4200195V#3204FWe wanted to be certain, so we asked our\x01",
            "dear Master Yin to go check on it.\x02\x03",
            "#4200196V#3210FEven in my wildest dreams, I never\x01",
            "expected the true identity of the bomb\x01",
            "to appear in the form it did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200197V#6P#0301FDamn, looks like he's gonna feign\x01",
            "ignorance till the very end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200198V#0106FLet's assume you're telling the truth.\x02\x03",
            "#4200199V#0101FDo you have an inkling as to who that\x01",
            "informant might have been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200200V#3204F#11PLogically speaking, a bombshell of this\x01",
            "magnitude points to the actions of a\x01",
            "Revache defector. However...\x02\x03",
            "#4200201V...taking into account the skill required to convey\x01",
            "the information to us, they must be adept.\x02\x03",
            "#4200202V#3200FAt any rate, this is as far as our knowledge\x01",
            "regarding KeA goes.\x02\x03",
            "#4200203VI'd appreciate it if you believed me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200204V#6P#0006FUnderstood.\x01",
            "Thanks for answering us honestly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6557")

    label("loc_6432")


    ChrTalk(
        0x8,
        (
            "#4200205V#3203F#11PIt's unfortunate, but we have no information\x01",
            "regarding KeA's origins.\x02\x03",
            "#4200206V#3200FIf perchance, our network uncovers any\x01",
            "details about her, I'll be sure to promptly\x01",
            "notify you.\x02\x03",
            "#4200207V#3209FI hope that'll serve as an apology\x01",
            "for allowing this incident to occur.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6557")

    Jump("loc_6564")

    label("loc_655C")

    SetScenarioFlags(0x0, 3)
    Jump("loc_6564")

    label("loc_6564")

    Jump("loc_45B0")

    label("loc_6569")


    ChrTalk(
        0x8,
        (
            "#4200208V#3200F#11PNow, then...\x01",
            "Does this conclude your questioning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200209V#6P#0003FYes, for the moment. I appreciate\x01",
            "your cooperation.\x02\x03",
            "#4200210V#0001FDo you mind if I give the department\x01",
            "an outline of what we discussed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200211V#3204F#11PDo as you like, my friend.\x02\x03",
            "#4200212V#3200FBy the way, Detective Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200213V#6P#0005FYes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200214V#3200F#11PI'll be honest with you. This raid was far beyond\x01",
            "what I thought Revache was capable of.\x02\x03",
            "#4200215VI was under the impression that I was fully cognizant\x01",
            "of their strength, connections, and patterns.\x02\x03",
            "#4200216V#3204FYet, they were able to pull off such a brazen attack\x01",
            "on us in their weakened state.\x02\x03",
            "#4200217V#3210FThey've splendidly surpassed all my expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200168V#6P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200219V#3209F#11PI must say, I am unbelievably excited for\x01",
            "what's to come.\x02\x03",
            "#4200220VI cannot recall a moment in the last few years\x01",
            "where a situation didn't proceed in the way\x01",
            "I had planned.\x02\x03",
            "#4200221V#3202FI can finally wield my intellect to crush\x01",
            "my foes without remorse.\x02\x03",
            "#4200222VThis truly is an indescribable joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200223V#6P#0013F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200224V#6P#0310FSmug bastard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200225V#0110FYou're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200226V#6P#0206F...unbelievable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4200227V#3204F#11PDo not think for one second that I will allow\x01",
            "the police to ruin my fun.\x02\x03",
            "#4200228VAlthough... You're special, so I'll grant you\x01",
            "a unique opportunity, so to speak.\x02\x03",
            "#4200229V#3202FWill you be able to broker a resolution between\x01",
            "both groups before Heiyue begins its all-out\x01",
            "retaliation?\x02\x03",
            "#4200230VI'll be eagerly awaiting your next move.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_322D end

    def Function_7_6BD9(): pass

    label("Function_7_6BD9")


    def lambda_6BDE():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6BDE)
    WaitChrThread(0xC, 1)

    def lambda_6BFC():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6BFC)
    Sleep(900)

    def lambda_6C19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6C19)
    WaitChrThread(0xC, 1)
    Return()

    # Function_7_6BD9 end

    def Function_8_6C2A(): pass

    label("Function_8_6C2A")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is shut tight.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_6C2A end

    SaveToFile()

Try(main)
