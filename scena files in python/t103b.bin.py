from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t103b.bin",                # FileName
        "t103b",                    # MapName
        "t103b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t103b",                  # 0
        "Clerk",                  # 1
        "Clerk",                  # 2
        "Boy",                    # 3
        "Man",                    # 4
        "Woman",                  # 5
        "Boy",                    # 6
        "Man",                    # 7
        "To Hotel Delphinia",     # 8
        "To Theme Park",          # 9
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch20600.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch24600.itc",                   # 04
        "chr/ch24200.itc",                   # 05
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-200,    4219,    -15479,  90,   257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9,      4250,    -14289,  0,    273,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(980,     4219,    -15399,  270,  257,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3829,   0,       -55380,  90,   273,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3650,   0,       -54209,  180,  257,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)

    DeclEvent(0x0000, 0, 12,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  10, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  11, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "To Hotel Delphinia")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "To Theme Park")

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_340",          # 02, 2
        "Function_3_37D",          # 03, 3
        "Function_4_415",          # 04, 4
        "Function_5_523",          # 05, 5
        "Function_6_636",          # 06, 6
        "Function_7_663",          # 07, 7
        "Function_8_7EF",          # 08, 8
        "Function_9_83A",          # 09, 9
        "Function_10_8F8",         # 0A, 10
        "Function_11_98A",         # 0B, 11
        "Function_12_AC4",         # 0C, 12
        "Function_13_D3C",         # 0D, 13
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B8"),
        (1, "loc_2C4"),
        (2, "loc_2D0"),
        (3, "loc_2DC"),
        (4, "loc_2E8"),
        (5, "loc_2F4"),
        (6, "loc_300"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_300")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_32F")

    Return()

    # Function_0_278 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_33F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_33F")

    Return()

    # Function_1_330 end

    def Function_2_340(): pass

    label("Function_2_340")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Sound(918, 1, 100, 0)
    Return()

    # Function_2_340 end

    def Function_3_37D(): pass

    label("Function_3_37D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Were you able to catch the fireworks show?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should have been able to see them anywhere\x01",
            "inside Mishelam. Those things go up, up, up!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_37D end

    def Function_4_415(): pass

    label("Function_4_415")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The nighttime parade is currently\x01",
            "underway inside the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of the park's beloved mascots are merrily\x01",
            "marching around with Mishy at the head! Oh,\x01",
            "I bet everyone is loving it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me, our guests are experiencing\x01",
            "something quite extraordinary.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_415 end

    def Function_5_523(): pass

    label("Function_5_523")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE")

    ChrTalk(
        0xFE,
        (
            "That roller coaster was out of this world!\x01",
            "If I could put it into words, it'd be like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4SWHOOOOSH!!!!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, something like that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_632")

    label("loc_5CE")


    ChrTalk(
        0xFE,
        (
            "Roller coasters are my favorite thing ever! The\x01",
            "way everything flew past me was totally crazy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632")

    TalkEnd(0xFE)
    Return()

    # Function_5_523 end

    def Function_6_636(): pass

    label("Function_6_636")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to be sick...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_636 end

    def Function_7_663(): pass

    label("Function_7_663")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D")

    ChrTalk(
        0xFE,
        (
            "What am I going to do with him...? He can\x01",
            "barely handle thrill rides, but he still forced\x01",
            "himself to get on with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we haven't had a family trip in a while,\x01",
            "so I'm really happy he was able to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to thank my husband later for\x01",
            "clearing his schedule for us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7EB")

    label("loc_79D")


    ChrTalk(
        0xFE,
        (
            "Our son had a blast as well. My husband\x01",
            "really outdid himself this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EB")

    TalkEnd(0xFE)
    Return()

    # Function_7_663 end

    def Function_8_7EF(): pass

    label("Function_8_7EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A")

    ChrTalk(
        0xFE,
        "Mmmmm... *snore*\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_836")

    label("loc_81A")


    ChrTalk(
        0xFE,
        "Zzz... Mishy... Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_836")

    TalkEnd(0xFE)
    Return()

    # Function_8_7EF end

    def Function_9_83A(): pass

    label("Function_9_83A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(
        0xFE,
        (
            "Whew. My son really drained all his\x01",
            "batteries playing at the theme park.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8F4")

    label("loc_89D")

    TurnDirection(0xFE, 0xD, 0)

    ChrTalk(
        0xFE,
        (
            "C'mon, hang in there for just a little\x01",
            "longer. The ship will be here soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_83A end

    def Function_10_8F8(): pass

    label("Function_10_8F8")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a map of Mishelam Wonderland.\x02\x03",
            "According to it, the theme park has a huge variety\x01",
            "of different rides and attractions.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_8F8 end

    def Function_11_98A(): pass

    label("Function_11_98A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "                  ~To Park Visitors~\x01\x01",
            "In Mishelam Wonderland, reckless behavior\x01",
            "and possession of weapons or other dangerous\x01",
            "objects are strictly prohibited.\x01\x01",
            "Furthermore, we ask that all children are\x01",
            "accompanied by a parent or guardian, with\x01",
            "no exceptions.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_98A end

    def Function_12_AC4(): pass

    label("Function_12_AC4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(
        0x101,
        (
            "#5003FThe theme park sure gets a lot of traffic,\x01",
            "huh? I bet the inside is bustling.\x02\x03",
            "#5000FWell, it's not like we have time to visit.\x01",
            "Once we're ready, we should head to\x01",
            "the Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBB")

    ChrTalk(
        0x103,
        "#0203FUnderstood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD2")

    label("loc_BBB")


    ChrTalk(
        0x103,
        "#5403FUnderstood.\x02",
    )

    CloseMessageWindow()

    label("loc_BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")

    ChrTalk(
        0x102,
        "#0100FWe should take care not to be late.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3F")

    label("loc_C10")


    ChrTalk(
        0x102,
        "#5300FWe should take care not to be late.\x02",
    )

    CloseMessageWindow()

    label("loc_C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C70")

    ChrTalk(
        0x104,
        "#0300FYup. Time to move out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C92")

    label("loc_C70")


    ChrTalk(
        0x104,
        "#5600FYup. Time to move out.\x02",
    )

    CloseMessageWindow()

    label("loc_C92")

    SetScenarioFlags(0x0, 4)
    Jump("loc_D25")

    label("loc_C9A")


    ChrTalk(
        0x101,
        (
            "#5000FWe don't have enough time to fit the\x01",
            "park and auction into our trip.\x02\x03",
            "Once we're ready, we should head to\x01",
            "the Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D25")

    Sleep(50)
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_12_AC4 end

    def Function_13_D3C(): pass

    label("Function_13_D3C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t105B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_D3C end

    SaveToFile()

Try(main)
