from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "Clerk",                  # 1
        "Clerk",                  # 2
        "Mishy",                  # 3
        "Woman",                  # 4
        "Girl",                   # 5
        "Boy",                    # 6
        "Man",                    # 7
        "Tourist",                # 8
        "Bond",                   # 9
        "Creil",                  # 10
        "Sunita",                 # 11
        "Marie",                  # 12
        "SE制御",                 # 13
        "To Hotel Delphinia",     # 14
        "To Theme Park",          # 15
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch23500.itc",                   # 01
        "chr/ch23900.itc",                   # 02
        "chr/ch24600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch32200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch27600.itc",                   # 07
        "chr/ch33300.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch39000.itc",                   # 0A
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(360,     4159,    -15840,  180,  385,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9810,   4000,    -5130,   45,   385,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-8970,   4000,    -4289,   225,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3690,   4000,    -19149,  180,  385,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3690,   1639,    -23280,  0,    385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7409,   4000,    -6219,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7699,    4000,    -1519,   135,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9159,    4000,    -1759,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(7889,    4000,    -3069,   360,  405,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6949,    4000,    -3160,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 16,  0.0,                   -48.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  16.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  18, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  19, 0x0000)
    DeclActor(4180,    4250,    -9540,   1200,    4180,    4250,    -9540,   0x007C, 0,  17, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "To Hotel Delphinia")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "To Theme Park")

    ScpFunction((
        "Function_0_3D0",          # 00, 0
        "Function_1_488",          # 01, 1
        "Function_2_526",          # 02, 2
        "Function_3_647",          # 03, 3
        "Function_4_9F2",          # 04, 4
        "Function_5_F09",          # 05, 5
        "Function_6_1031",         # 06, 6
        "Function_7_10C3",         # 07, 7
        "Function_8_1103",         # 08, 8
        "Function_9_113B",         # 09, 9
        "Function_10_12A5",        # 0A, 10
        "Function_11_1324",        # 0B, 11
        "Function_12_1475",        # 0C, 12
        "Function_13_150A",        # 0D, 13
        "Function_14_15AC",        # 0E, 14
        "Function_15_15CA",        # 0F, 15
        "Function_16_1935",        # 10, 16
        "Function_17_231A",        # 11, 17
        "Function_18_24D5",        # 12, 18
        "Function_19_2567",        # 13, 19
    ))


    def Function_0_3D0(): pass

    label("Function_0_3D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_410"),
        (1, "loc_41C"),
        (2, "loc_428"),
        (3, "loc_434"),
        (4, "loc_440"),
        (5, "loc_44C"),
        (6, "loc_458"),
        (SWITCH_DEFAULT, "loc_464"),
    )


    label("loc_410")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_41C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_428")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_434")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_440")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_44C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_487")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_487")

    Return()

    # Function_0_3D0 end

    def Function_1_488(): pass

    label("Function_1_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_496")
    Jump("loc_525")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_525")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_525")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_525")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_525")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_525")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_51C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_525")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_525")

    label("loc_525")

    Return()

    # Function_1_488 end

    def Function_2_526(): pass

    label("Function_2_526")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_543")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1030_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x1, 0x1)
    Jump("loc_5A7")

    label("loc_583")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)

    label("loc_5A7")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610")
    LoadEffect(0x1, "event\\eva00_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 4180, 4250, -9540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_610")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Return()

    # Function_2_526 end

    def Function_3_647(): pass

    label("Function_3_647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_658")
    Jump("loc_9EE")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_9EE")

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_9EE")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_682")
    Jump("loc_9EE")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_690")
    Jump("loc_9EE")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_752")

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how many people like\x01",
            "to come enjoy the theme park at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The park has quite the romantic atmosphere\x01",
            "after dark. It's become a big hit with couples.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE")

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_9E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89A")

    ChrTalk(
        0xFE,
        (
            "Welcome to Mishelam's pride and joy:\x01",
            "Mishelam Wonderland!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You already have tickets?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FSorry, no. We're busy with work this time\x01",
            "around. Maybe next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I see. I feel bad for you, but we all\x01",
            "have those days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope we can make your next visit one\x01",
            "you'll never forget.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9E0")

    label("loc_89A")


    ChrTalk(
        0xFE,
        (
            "Still, it's a shame that you won't be able\x01",
            "to experience the theme park today...\x01",
            "It's quite the thrill, trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still a lot of other things Mishelam\x01",
            "has to offer, so it's not the end of the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should be able to see the fireworks\x01",
            "show from outside the park. Please try\x01",
            "and catch it if you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E0")

    Jump("loc_9EE")

    label("loc_9E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9EE")

    label("loc_9EE")

    TalkEnd(0xFE)
    Return()

    # Function_3_647 end

    def Function_4_9F2(): pass

    label("Function_4_9F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A03")
    Jump("loc_F05")

    label("loc_A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A11")
    Jump("loc_F05")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A1F")
    Jump("loc_F05")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A2D")
    Jump("loc_F05")

    label("loc_A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_F05")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(
        0xFE,
        (
            "Inside the park, you'll find various rides\x01",
            "and an assortment of Mishy-related\x01",
            "merchandise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I recommend the Mishy hairband! You'll\x01",
            "never have to ask for another one again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just imagine strolling through the park, wearing\x01",
            "your very own Mishy hairband. Isn't that exciting?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C4C")

    label("loc_B74")


    ChrTalk(
        0xFE,
        (
            "Inside the park, you'll find various rides\x01",
            "and an assortment of Mishy-related\x01",
            "merchandise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mentioned the Mishy hairband before,\x01",
            "but that's not all we have! We have straps,\x01",
            "clothes, plushies, you name it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4C")

    Jump("loc_F05")

    label("loc_C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC4")

    ChrTalk(
        0xFE,
        (
            "That tourist that just entered the park\x01",
            "was quite the character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'I'm gonna see if I can spot more\x01",
            "than one Mishy! If it can be done,\x01",
            "I'll be the one to do it!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Or so he told me. Quite enthusiastically, at that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(It's funny how you can tell it was\x01",
            "Lechter by one statement...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(What's he playing at...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF7")

    label("loc_DC4")


    ChrTalk(
        0xFE,
        (
            "Haha, I know what you're thinking, but there's no\x01",
            "need to worry. We have made it impossible for\x01",
            "more than one Mishy to be public at a given time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm, must mean that they're really\x01",
            "careful when putting together shifts...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F(Please do not speak such heresy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F(S-Sorry.)\x02",
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_F05")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F05")

    label("loc_F05")

    TalkEnd(0xFE)
    Return()

    # Function_4_9F2 end

    def Function_5_F09(): pass

    label("Function_5_F09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hiya! Welcome to Mishelam Wonderland!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Meeheehee! Have fun!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201FMishy...! Fur and all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FT-Tio? You okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FAhem... Nothing. You did not\x01",
            "hear anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_102D")

    label("loc_FE0")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hiya! Welcome to Mishelam Wonderland!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Meeheehee! Have fun!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102D")

    TalkEnd(0xFE)
    Return()

    # Function_5_F09 end

    def Function_6_1031(): pass

    label("Function_6_1031")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wow... This is that theme park\x01",
            "I'm always hearing about, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sure is big. I bet this place could\x01",
            "keep us entertained for weeks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1031 end

    def Function_7_10C3(): pass

    label("Function_7_10C3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Woohoo! I've been wanting\x01",
            "to come here for forever!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_10C3 end

    def Function_8_1103(): pass

    label("Function_8_1103")

    TalkBegin(0xFE)
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "C'mon, Dad! Let's go inside already!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1103 end

    def Function_9_113B(): pass

    label("Function_9_113B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D6")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xD,
        (
            "Dad! What's the holdup?\x01",
            "Let's go on inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear you, I hear you. Just give me\x01",
            "one minute and I'll be right there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12A1")

    label("loc_11D6")


    ChrTalk(
        0xFE,
        (
            "Geez, these kind of places really get kids\x01",
            "going. It's already evening, yet he shows\x01",
            "no signs of slowing down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I left him alone, he'd probably keep\x01",
            "playing until he dropped from exhaustion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A1")

    TalkEnd(0xFE)
    Return()

    # Function_9_113B end

    def Function_10_12A5(): pass

    label("Function_10_12A5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I know the night is still young and all, but\x01",
            "I'd rather get back to the hotel before the\x01",
            "nighttime crowd comes in.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_12A5 end

    def Function_11_1324(): pass

    label("Function_11_1324")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13B3")

    ChrTalk(
        0x10,
        "Between you and me, I still have a lot of work to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The stress limits how much I enjoy myself,\x01",
            "but that's okay...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_13B3")


    ChrTalk(
        0x10,
        (
            "I thought it would be a good idea to spend some\x01",
            "quality time with my family every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Those two look like they're having a ball,\x01",
            "so I guess that makes this trip worth it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1471")

    TalkEnd(0xFE)
    Return()

    # Function_11_1324 end

    def Function_12_1475(): pass

    label("Function_12_1475")

    TalkBegin(0xFE)

    ChrTalk(
        0x11,
        (
            "Today, my husband was able to join\x01",
            "Sunita and I on our trip to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I do love visiting the theme\x01",
            "park. Especially as a family.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1475 end

    def Function_13_150A(): pass

    label("Function_13_150A")

    TalkBegin(0xFE)

    ChrTalk(
        0x12,
        (
            "Father, I really want to ride the\x01",
            "ferris wheel. Is that all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "And it's not just me. Marie, too! We want\x01",
            "to go to the tippy-top of Mishelam!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_150A end

    def Function_14_15AC(): pass

    label("Function_14_15AC")

    TalkBegin(0xFE)

    ChrTalk(
        0x13,
        "#1SNya-o... ♪#3S\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_15AC end

    def Function_15_15CA(): pass

    label("Function_15_15CA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_15DA")
    Jump("loc_1921")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_15E8")
    Jump("loc_1921")

    label("loc_15E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_15F6")
    Jump("loc_1921")

    label("loc_15F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1604")
    Jump("loc_1921")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1612")
    Jump("loc_1921")

    label("loc_1612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AD")

    ChrTalk(
        0x151,
        (
            "#5705FWere you were wanting to visit the theme\x01",
            "park, Lloyd?\x02\x03",
            "#5702FMaybe we could get our hands on a Mishy\x01",
            "costume and sneak into the auction using\x01",
            "that. I'm sure that'd be entertaining to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FThere's no way that'd work, and you know it.\x01",
            "Besides, that'd just be plain awkward...\x02\x03",
            "#0000FA-Anyway, let's check out the boutique\x01",
            "and see if we can get some new clothes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_182E")

    label("loc_17AD")


    ChrTalk(
        0x101,
        (
            "#0000FThere's no benefit in visiting the theme park.\x01",
            "For now, let's try to find some classy clothes\x01",
            "at the mall's boutique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182E")

    Jump("loc_1921")

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(
        0x101,
        (
            "#0003FOur objective is the Schwarze Auction.\x01",
            "Going to the theme park isn't going to\x01",
            "help us. I'm sorry, Tio.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1913")

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F(W-Wow, she looks crushed. Maybe\x01",
            "I was a little too harsh...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1913")

    Jump("loc_1921")

    label("loc_1918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1921")

    label("loc_1921")

    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x5)
    Return()

    # Function_15_15CA end

    def Function_16_1935(): pass

    label("Function_16_1935")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadEffect(0x0, "event\\ev309_00.eff")
    FadeToBright(1000, 0)
    OP_68(0, 2200, -47400, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22940, 0)
    SetCameraDistance(21940, 2500)
    SetChrPos(0x101, 600, 0, -49200, 0)
    SetChrPos(0x102, -600, 0, -49200, 0)
    SetChrPos(0x103, 1200, 0, -50700, 0)
    SetChrPos(0x104, -1200, 0, -50700, 0)

    def lambda_19E2():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19E2)

    def lambda_19F7():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19F7)

    def lambda_1A0C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A0C)

    def lambda_1A21():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A21)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#3500395V#0205F#11PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500396V#0005F#5PThis must be the theme park.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 0)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(-2830, 2200, -34120, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27290, 0)
    SetCameraDistance(25290, 3000)
    OP_90(0x101, -3930, 4000, -37980, 0)
    OP_90(0x102, -4800, 4000, -38790, 0)
    OP_90(0x103, -2750, 4000, -39310, 0)
    OP_90(0x104, -3800, 4000, -40070, 0)

    def lambda_1C3F():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C3F)
    Sleep(50)

    def lambda_1C57():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C57)
    Sleep(50)

    def lambda_1C6F():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C6F)
    Sleep(50)

    def lambda_1C87():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C87)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        "#3500397V#0205F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500398V#0012F#5PEr, it looks like it'd be a pretty interesting\x01",
            "place. Don't you guys think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500399V#0302F#6POh, yeah. Place is damn big.\x02\x03",
            "#3500400V#0304FYou got your ferris wheel, roller coaster...\x02\x03",
            "#3500401VHell, they've even got a haunted house\x01",
            "and merry-go-round.\x02\x03",
            "#3500402V#0300FThey're apparently building a castle inspired\x01",
            "by the Middle Ages, too. The thing is gonna\x01",
            "look like it's ripped right out of a fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500403V#0011FTh-That's pretty impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500404V#0104F#5PYou have to remember that this place\x01",
            "is run by the IBC. Their goal is to attract\x01",
            "tourists, so they put in quite the effort.\x02\x03",
            "#3500405V#0102FI came here before with Bell, but I never had\x01",
            "the chance to see everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500406V#0205F#6P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    def lambda_1FDB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FDB)

    def lambda_1FE8():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FE8)

    ChrTalk(
        0x101,
        (
            "#3500407V#0012F#5PUh...well...\x02\x03",
            "#3500408V#0000FWe may not have much time left, but\x01",
            "do you want to take a peek inside, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500409V#0208F#6PNo, that is all right...\x02\x03",
            "#3500410V#0206FWe are technically here on police business,\x01",
            "so we do not need to go this time.\x02\x03",
            "#3500411VBesides, a ticket is very expensive. We\x01",
            "would not have enough mira for all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500412V#0303F#6PYeah, those things don't come cheap.\x02\x03",
            "#3500413V#0300FOnce we set foot in that place, I doubt\x01",
            "they'd let us ask for a refund.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500414V#0109F#5PHow about we come here next time we\x01",
            "have a vacation?\x02\x03",
            "#3500415V#0102FThen, we can come and experience\x01",
            "everything Mishelam has to offer us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        "#3500416V#0202F#12PI'd like that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -3890, 0, -32460, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 2)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_16_1935 end

    def Function_17_231A(): pass

    label("Function_17_231A")

    EventBegin(0x0)
    Fade(500)
    OP_68(8380, 7250, -13860, 0)
    MoveCamera(313, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20350, 0)
    SetChrPos(0x101, 4970, 4250, -11650, 0)
    SetChrPos(0x102, 4400, 4250, -13060, 0)
    SetChrPos(0x103, 6270, 4000, -12400, 315)
    SetChrPos(0x104, 7200, 4000, -11960, 315)
    StopEffect(0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_23B0")
    SetChrPos(0x151, 5580, 4000, -13450, 0)

    label("loc_23B0")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34D, 1)

    ChrTalk(
        0x101,
        "#5P#0005FHmm, take a look at this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FCould this be the engagement ring\x01",
            "that Toma guy was talkin' about?\x02\x03",
            "#0306FMight as well bring it to him while\x01",
            "we have the time, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x3)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 4970, 4250, -11650, 0)
    EventEnd(0x5)
    Return()

    # Function_17_231A end

    def Function_18_24D5(): pass

    label("Function_18_24D5")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a map of Mishelam Wonderland.\x02\x03",
            "According to it, the theme park has a wide variety\x01",
            "of different rides and attractions.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_18_24D5 end

    def Function_19_2567(): pass

    label("Function_19_2567")

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
            "objects is strictly prohibited.\x01\x01",
            "Furthermore, we ask that all children are\x01",
            "accompanied by a parent or guardian.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_2567 end

    SaveToFile()

Try(main)
