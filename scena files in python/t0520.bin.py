from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0520.bin",                # FileName
        "t0520",                    # MapName
        "t0520",                    # Location
        0x003F,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0520",                  # 0
        "Noma",                   # 1
        "Luka",                   # 2
        "Miner Logy",             # 3
        "Felicia",                # 4
        "Letina",                 # 5
        "Estelle",                # 6
        "Joshua",                 # 7
        "Bracer Scott",           # 8
        "Bracer Wenzel",          # 9
        "Tourist Wallace",        # 10
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "apl/ch50130.itc",                   # 04
        "chr/ch33300.itc",                   # 05
        "chr/ch34500.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch27202.itc",                   # 09
        "chr/ch27302.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch24402.itc",                   # 0C
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

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(147360,  500,     4599,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(204809,  0,       560,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(203350,  0,       560,     90,   261,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7530,   -600,    -3140,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-8640,   -600,    -4380,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6199,   -600,    4199,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-9289,   -600,    3869,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-9510,   -600,    -1200,   180,  405,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_290",          # 00, 0
        "Function_1_348",          # 01, 1
        "Function_2_373",          # 02, 2
        "Function_3_573",          # 03, 3
        "Function_4_5B2",          # 04, 4
        "Function_5_5B6",          # 05, 5
        "Function_6_180A",         # 06, 6
        "Function_7_24F9",         # 07, 7
        "Function_8_2578",         # 08, 8
        "Function_9_31D9",         # 09, 9
        "Function_10_3D0F",        # 0A, 10
        "Function_11_403A",        # 0B, 11
        "Function_12_4366",        # 0C, 12
        "Function_13_4523",        # 0D, 13
        "Function_14_488E",        # 0E, 14
        "Function_15_4B7F",        # 0F, 15
        "Function_16_4D84",        # 10, 16
        "Function_17_5102",        # 11, 17
    ))


    def Function_0_290(): pass

    label("Function_0_290")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D0"),
        (1, "loc_2DC"),
        (2, "loc_2E8"),
        (3, "loc_2F4"),
        (4, "loc_300"),
        (5, "loc_30C"),
        (6, "loc_318"),
        (SWITCH_DEFAULT, "loc_324"),
    )


    label("loc_2D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_300")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_30C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_330")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_347")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_347")

    Return()

    # Function_0_290 end

    def Function_1_348(): pass

    label("Function_1_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_348")

    label("loc_372")

    Return()

    # Function_1_348 end

    def Function_2_373(): pass

    label("Function_2_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38B")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3BB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_421")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_457")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4F5")
    SetChrPos(0x9, 10680, 0, -830, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_4F5")

    Jump("loc_55F")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53A")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_55F")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_548")
    Jump("loc_55F")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_556")
    Jump("loc_55F")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55F")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    ClearChrFlags(0x11, 0x80)

    label("loc_572")

    Return()

    # Function_2_373 end

    def Function_3_573(): pass

    label("Function_3_573")

    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5B1")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_5B1")

    Return()

    # Function_3_573 end

    def Function_4_5B2(): pass

    label("Function_4_5B2")

    Call(0, 5)
    Return()

    # Function_4_5B2 end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    Call(0, 17)
    Jump("loc_1809")

    label("loc_5CC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1806")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Rest\x01",       # 2
            "Leave\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_639")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_639")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1801")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_679")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1801")

    label("loc_679")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D")
    Jump("loc_1801")

    label("loc_68D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1801")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_72A")

    ChrTalk(
        0x8,
        (
            "Even now, no one knows why the mayor\x01",
            "and Gantz haven't come back yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh* I wonder what they're up to...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7D2")

    ChrTalk(
        0x8,
        (
            "I spotted the mayor hopping on the bus;\x01",
            "he looked so depressed. I could basically\x01",
            "see the rain clouds above him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Did something happen to Gantz?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_8BB")

    ChrTalk(
        0x8,
        (
            "We had those monster attacks, and now\x01",
            "one of our miners has gone missing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hard to believe all this craziness has\x01",
            "happened in the span of a few months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hopefully, this isn't a sign of things to come...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_917")

    ChrTalk(
        0x8,
        (
            "You look exhausted! How about you book\x01",
            "a room and take a nice, long nap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_99E")

    ChrTalk(
        0x8,
        "Dang, looks like they've gotten sober...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why can't we get more customers that\x01",
            "can hold more than a few drinks?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(
        0x8,
        (
            "We're able to get the fine alcohol we\x01",
            "serve here through a trader named\x01",
            "Harold Hayworth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I assure you, his taste in drinks is just\x01",
            "as nice as his looks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The miners have been thirsty the past\x01",
            "few weeks... I'll need to ask him for\x01",
            "more alcohol next time he stops by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B45")

    label("loc_AD1")


    ChrTalk(
        0x8,
        (
            "Thanks to Harold, the inn is able to stock\x01",
            "up on some tasty drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I don't know what I'd do without him.\x02",
    )

    CloseMessageWindow()

    label("loc_B45")

    Jump("loc_1801")

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF5")

    ChrTalk(
        0x8,
        (
            "Our waitress, Luka, is as unsociable\x01",
            "as a cat in a dog park. Heck, she's\x01",
            "as rude as one, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Maybe I'll get her a little tipsy next shift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She can't hold many drinks, but trust me,\x01",
            "seeing her drunk is totally worth it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#0106FI'm not really sure about the\x01",
            "morality of this plan...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D7E")

    label("loc_CF5")


    ChrTalk(
        0x8,
        "Maybe I'll get her a little tipsy next shift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She can't hold many drinks, but, trust me,\x01",
            "seeing her drunk is totally worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7E")

    Jump("loc_1801")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(
        0x8,
        (
            "Crossbell has been around 70 years now.\x01",
            "More tourists decided to come for the festival\x01",
            "this year, so that'll be good for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Around this time of the year, the miners are\x01",
            "always going by the city, so profit is low.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1000")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F39")

    ChrTalk(
        0x8,
        "Yesterday, the mining crew threw a big party.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure, they had me busy, but it was too\x01",
            "much of a blast to complain. This inn is\x01",
            "blessed more than it deserves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FFB")

    label("loc_F39")


    ChrTalk(
        0x8,
        (
            "*sigh* Logy got wasted out of his mind.\x01",
            "I don't usually do this, but I'll let him\x01",
            "stay the night, free of charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, he may be young, but that's no\x01",
            "excuse to act this pathetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFB")

    Jump("loc_1801")

    label("loc_1000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1093")

    ChrTalk(
        0x8,
        (
            "We had two younger customers stop by\x01",
            "today. They're bracers, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What's with the gloom and doom?\x01",
            "Something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120F")

    ChrTalk(
        0x8,
        (
            "This store is like a ghost town\x01",
            "during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Okay, since I've got a bit of free time\x01",
            "on my hands, listen closely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Luka, our waitress here, is one of the\x01",
            "most unsociable people I've ever met, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...whenever she genuinely smiles, it's one of\x01",
            "the most adorable things I've ever seen. If\x01",
            "I was a guy, it'd be love at first sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12C7")

    label("loc_120F")


    ChrTalk(
        0x8,
        (
            "Luka may be unsociable, but don't let that\x01",
            "fool you. Her smile is absolutely heartwarming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a shame that she doesn't smile more often.\x01",
            "It'd do her good, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C7")

    Jump("loc_1801")

    label("loc_12CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(
        0x8,
        (
            "Now that those monster nuisances are in the\x01",
            "past, Mainz is back to the same old, same old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The only nuisance we have to worry about\x01",
            "is the mining crew complaining about how\x01",
            "they don't get off work early anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm just glad they no longer have to worry\x01",
            "about getting jumped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D5")

    label("loc_140B")


    ChrTalk(
        0x8,
        (
            "Good thing those monsters are a thing\x01",
            "of the past. Now the town doesn't have\x01",
            "to worry about stepping outside at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And it's all thanks to you four. Everyone,\x01",
            "you have my sincerest thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")

    Jump("loc_1801")

    label("loc_14DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_15CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1568")

    ChrTalk(
        0x8,
        "Oh? You folks heading out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not been the safest around here\x01",
            "lately, so try not to stay out too late.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C6")

    label("loc_1568")


    ChrTalk(
        0x8,
        (
            "Looking to warm up and sip on a\x01",
            "nice drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'll have find you folks seats, though.\x02",
    )

    CloseMessageWindow()

    label("loc_15C6")

    Jump("loc_1801")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15ED")
    SetScenarioFlags(0x66, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1723")

    ChrTalk(
        0x8,
        (
            "Huh, I haven't seen you all around before.\x01",
            "From Crossbell City, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sorry to say, you did not come at a good time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, wolf-like monsters have been\x01",
            "rampaging through our town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They even hit our food storehouse near the\x01",
            "front of town. Geez, what's their deal?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1801")

    label("loc_1723")


    ChrTalk(
        0x8,
        "That aside, you looking for anything to eat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to eat in peace and quiet,\x01",
            "now's your chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once the sun sets, pretty much every\x01",
            "seat in here will be occupied by a bunch\x01",
            "of tired, thirsty miners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1801")

    Jump("loc_5D9")

    label("loc_1806")

    TalkEnd(0x8)

    label("loc_1809")

    Return()

    # Function_5_5B6 end

    def Function_6_180A(): pass

    label("Function_6_180A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18BB")

    ChrTalk(
        0xFE,
        (
            "Gantz's disappearance has been an enigma.\x01",
            "I bet you he got into trouble and had to go\x01",
            "into hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or maybe I've read one too many\x01",
            "mystery novels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1965")

    ChrTalk(
        0xFE,
        (
            "If Gantz has been found, that means...\x01",
            "Oh, no. There's going to be another\x01",
            "party tonight, isn't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Preparing for one is always a pain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1A23")

    ChrTalk(
        0xFE,
        "Gantz must REALLY suck at gambling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever he gets wasted here, that's all he\x01",
            "ever complains about. I don't want to hear\x01",
            "about every hand he's ever lost, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AAB")

    ChrTalk(
        0xFE,
        "Hmm, that should be it for cleaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantz being here or not, cleaning isn't\x01",
            "usually very hard to take care of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5D")

    ChrTalk(
        0xFE,
        (
            "Normally, I take care of all the cleaning\x01",
            "when there aren't any customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the miners haven't been\x01",
            "throwing many parties lately.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BA8")

    label("loc_1B5D")


    ChrTalk(
        0xFE,
        (
            "Well, having no parties to clean up\x01",
            "makes my life a whole lot easier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA8")

    Jump("loc_24F5")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C65")

    ChrTalk(
        0xFE,
        "Today's the end of the festival, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead of tourists visiting, all the miners\x01",
            "who went to celebrate should be coming\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I'm swamped...\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CE0")

    ChrTalk(
        0xFE,
        (
            "I'm sort of busy, but were you\x01",
            "looking for something to drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm never in charge of the alcohol.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DAC")

    ChrTalk(
        0xFE,
        (
            "There are tourists who would come to a\x01",
            "deserted place like this at the height of\x01",
            "the Anniversary Festival? Seriously?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess I can relate. I hate\x01",
            "crowds more than anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F5")

    label("loc_1DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE3")

    ChrTalk(
        0xFE,
        "Geez, every day is as demanding as the last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't see the charm in alcohol. Probably\x01",
            "because I'm such a lightweight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI wasn't expecting to hear something like\x01",
            "that from a bar waitress...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear customer, how about you shut\x01",
            "your trap? I say whatever I want.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F7F")

    label("loc_1EE3")


    ChrTalk(
        0xFE,
        "Seriously, where's the fun in alcohol?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I drank some before, purely out of\x01",
            "curiosity, and I couldn't remember\x01",
            "a thing. What's so great about that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_24F5")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2066")

    ChrTalk(
        0xFE,
        (
            "What's your deal? Take your\x01",
            "stares and shove off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Noma takes all the orders. I just\x01",
            "carry them to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's everything. If you've got\x01",
            "what you need, would you mind\x01",
            "leaving me alone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20D5")

    label("loc_2066")


    ChrTalk(
        0xFE,
        (
            "Trying to play nice with drunk miners\x01",
            "every damn night is exhausting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can you just leave me alone?\x02",
    )

    CloseMessageWindow()

    label("loc_20D5")

    Jump("loc_24F5")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2206")

    ChrTalk(
        0xFE,
        (
            "*yawn*... Oh, dear, I just want to hop\x01",
            "back into bed. Is that so much to ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to those miners' excessive noise\x01",
            "and partying, Noma and I weren't able\x01",
            "to get much sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just how long do they plan to keep this\x01",
            "dumb 'Monsters Are Gone Party' going,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22DB")

    label("loc_2206")


    ChrTalk(
        0xFE,
        (
            "Mainz's miners throw what they like to\x01",
            "call a 'Monsters Are Gone Party' every.\x01",
            "Single. Night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I'm not mistaken, they are just looking\x01",
            "for any excuse to drink their fill. Goddess\x01",
            "preserve my sanity...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DB")

    Jump("loc_24F5")

    label("loc_22E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_22EE")
    Jump("loc_24F5")

    label("loc_22EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_23EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2394")

    ChrTalk(
        0xFE,
        (
            "*sweep* *sweep* All right.\x01",
            "It should be okay, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll take a short break, since\x01",
            "it's about to get real busy in here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23E7")

    label("loc_2394")


    ChrTalk(
        0xFE,
        (
            "I think I'll take a short break, since\x01",
            "it's about to get real busy in here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E7")

    Jump("loc_24F5")

    label("loc_23EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_24F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240E")
    SetScenarioFlags(0x66, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_240E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(
        0xFE,
        (
            "Welcome. If you want to order something,\x01",
            "do it at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What? Do you have business with me\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F5")

    label("loc_249A")


    ChrTalk(
        0xFE,
        (
            "If you want to order, could you do it at the\x01",
            "counter? I'm busy preparing for tonight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F5")

    TalkEnd(0xFE)
    Return()

    # Function_6_180A end

    def Function_7_24F9(): pass

    label("Function_7_24F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2556")

    ChrTalk(
        0xFE,
        (
            "Ugh...\x01",
            "I'm...never drinking again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "J-Just leave me alone...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2574")

    label("loc_2556")


    ChrTalk(
        0xFE,
        "J-Just leave me alone...\x02",
    )

    CloseMessageWindow()

    label("loc_2574")

    TalkEnd(0xFE)
    Return()

    # Function_7_24F9 end

    def Function_8_2578(): pass

    label("Function_8_2578")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    ChrTalk(
        0xFE,
        "Ohohoho!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At long last...I've finally achieved my\x01",
            "life's goal: negotiating and purchasing\x01",
            "septium crystals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, this is the first time I've seen\x01",
            "such a tremendous crystal of carnelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe! With this, I'll be able to return to my\x01",
            "father with pride! And it's one step closer to\x01",
            "becoming the great merchant I intend to be!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27B6")

    label("loc_26EF")


    ChrTalk(
        0xFE,
        (
            "A part of me is in disbelief that they were able\x01",
            "to excavate a carnelia crystal this large... Well,\x01",
            "Mainz IS known for their septium, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe. Just wait until you see this, Father!\x02",
    )

    CloseMessageWindow()

    label("loc_27B6")

    Jump("loc_31D5")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2866")

    ChrTalk(
        0xFE,
        (
            "Tonight, I'm visiting the mayor's house in\x01",
            "order to negotiate a septium transaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until those crystals are in my grasp...\x01",
            "I will never give up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_2866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A0")

    ChrTalk(
        0xFE,
        (
            "The mayor and I have been negotiating\x01",
            "my purchase of some of Mainz's septium\x01",
            "crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's a stubborn old man. No matter what\x01",
            "I say, he just won't budge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I'll convince you, just you wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, daughter of an illustrious Imperial\x01",
            "merchant, will emerge victorious!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A37")

    label("loc_29A0")


    ChrTalk(
        0xFE,
        (
            "That being said, I must formulate a\x01",
            "method to win him over, posthaste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First, I can try raising my offer as much\x01",
            "as I can, and then I can...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A37")

    Jump("loc_31D5")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2AF1")

    ChrTalk(
        0xFE,
        (
            "Ugh... I wasn't able to get a wink of sleep,\x01",
            "thanks to that racket coming from upstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can barely think straight...\x01",
            "Maybe I'll take today to recuperate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D5")

    label("loc_2AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C88")

    ChrTalk(
        0xFE,
        (
            "The batch of septium crystals I have my\x01",
            "sights set on here is the genuine article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the low yield on crystals lately, it\x01",
            "takes luck to even have the opportunity\x01",
            "to purchase them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Much to my dismay, I was unsuccessful\x01",
            "in negotiating for the septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter. I still have plenty of mira\x01",
            "to stay here comfortably, so I intend\x01",
            "to stick around for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D70")

    label("loc_2C88")


    ChrTalk(
        0xFE,
        (
            "I still have plenty of mira to stay here.\x01",
            "Not to mention, Letina is here to\x01",
            "keep me company and things tidy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohohoho! I fully intend to stay in this\x01",
            "town until that stubborn mayor agrees\x01",
            "to sell me those septium crystals!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D70")

    Jump("loc_31D5")

    label("loc_2D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3B")

    ChrTalk(
        0xFE,
        (
            "I'm biding my time in this town until\x01",
            "I can fulfill my goal: purchasing those\x01",
            "precious septium crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, crystals aren't something small\x01",
            "a monster would drop, like sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pure septium contain a magnificent glow\x01",
            "and are worn as jewelry by most of the\x01",
            "Erebonian nobility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were to return home accompanied with\x01",
            "a bag of septium crystals, I'm positive that\x01",
            "I could make quite the profit! Ohohoho!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_300F")

    label("loc_2F3B")


    ChrTalk(
        0xFE,
        (
            "Septium crystals aren't something small\x01",
            "a monster would drop, like sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were to return home accompanied with\x01",
            "a bag of septium crystals, I'm positive that\x01",
            "I could make quite the profit! Ohohoho!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300F")

    Jump("loc_31D5")

    label("loc_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3022")
    Jump("loc_31D5")

    label("loc_3022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")
    Call(0, 10)
    Jump("loc_3104")

    label("loc_303D")


    ChrTalk(
        0xFE,
        (
            "According to my watch, it should about time\x01",
            "for the miners to return home for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they booze and riot upstairs like they\x01",
            "did yesterday, I won't be able to eat my\x01",
            "supper in peace...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3104")

    Jump("loc_31D5")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_31D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3124")
    Call(0, 10)
    Jump("loc_31D5")

    label("loc_3124")


    ChrTalk(
        0xFE,
        (
            "Oh, hello there... By chance, did you come\x01",
            "to purchase some septium as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohoho, good luck, then! Rest assured, you\x01",
            "will not defeat my superior mercantile tactics!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D5")

    TalkEnd(0xFE)
    Return()

    # Function_8_2578 end

    def Function_9_31D9(): pass

    label("Function_9_31D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332F")

    ChrTalk(
        0xFE,
        (
            "*sigh* My lady finally obtained the septium\x01",
            "crystal she was desperately searching for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is indeed a miracle, but something tells me that\x01",
            "she does not fully comprehend that we've racked\x01",
            "up a debt of nearly four months of inn expenses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will do my sanity a favor and try\x01",
            "not to think about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33FC")

    label("loc_332F")


    ChrTalk(
        0xFE,
        (
            "In any case, we should soon be able to\x01",
            "return to Erebonia at long last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been four months since my lady and I ran\x01",
            "away from home. I'm curious to see how the\x01",
            "mansion held up in our absence...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FC")

    Jump("loc_3D0B")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_350F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348B")

    ChrTalk(
        0xFE,
        (
            "(My lady is only this serious when in the\x01",
            "middle of a business deal.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(I hope this all goes well...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_350A")

    label("loc_348B")


    ChrTalk(
        0xFE,
        (
            "(*sigh* Pondering on how tonight's business\x01",
            "deal is going to play out is going to make my\x01",
            "heart burst out of my chest...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_350A")

    Jump("loc_3D0B")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_363B")

    ChrTalk(
        0xFE,
        (
            "My lady is currently in the middle of negotiations,\x01",
            "using her usual aggressiveness and vast supply\x01",
            "of mira, but...these things are quite complex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, I'm feeling desperate, given that we\x01",
            "have come this far. The least I can do is serve\x01",
            "my lady to the best of my ability!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0B")

    label("loc_363B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370F")

    ChrTalk(
        0xFE,
        (
            "It appears that this town's miners threw a\x01",
            "drinking party, lasting long into the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It did not make my job easy. I was up late,\x01",
            "trying to get my lady into bed and asleep.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37A9")

    label("loc_370F")


    ChrTalk(
        0xFE,
        (
            "Mayor Bickson should be exhausted, too. It\x01",
            "won't be long before he yields to our demands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but wonder when I'll be\x01",
            "able to go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A9")

    Jump("loc_3D0B")

    label("loc_37AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3952")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A7")

    ChrTalk(
        0xFE,
        (
            "According to my lady, all of our travel funds\x01",
            "were pilfered from the mansion's private safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My lady assures me that we have enough\x01",
            "funds to last us a year, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...just how much did she actually take?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_394D")

    label("loc_38A7")


    ChrTalk(
        0xFE,
        (
            "She grabbed enough mira to survive a whole year\x01",
            "AND buy two train tickets here and back each?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, dear... The mansion must be in an\x01",
            "absolute uproar by now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394D")

    Jump("loc_3D0B")

    label("loc_3952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB9")

    ChrTalk(
        0xFE,
        (
            "My lady is the sole daughter of a\x01",
            "prominent Imperial merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She ventured to Crossbell with the intentions of\x01",
            "becoming a great merchant herself, dragging\x01",
            "me along with her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Since I left the mansion without saying\x01",
            "anything to my lady's father, I am positive that\x01",
            "I will get a harsh scolding when we return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B5E")

    label("loc_3AB9")


    ChrTalk(
        0xFE,
        (
            "If we do not return to the mansion quickly,\x01",
            "I'm going to be out of a job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goddess, I hope my lady will be able to\x01",
            "procure these septium crystals soon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5E")

    Jump("loc_3D0B")

    label("loc_3B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3B71")
    Jump("loc_3D0B")

    label("loc_3B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")
    Call(0, 10)
    Jump("loc_3C08")

    label("loc_3B8C")


    ChrTalk(
        0xFE,
        "Time to fetch my lady's supper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm always worried about falling down\x01",
            "the stairs. After all, I'm a major klutz...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C08")

    Jump("loc_3D0B")

    label("loc_3C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C28")
    Call(0, 10)
    Jump("loc_3D0B")

    label("loc_3C28")


    ChrTalk(
        0xFE,
        (
            "My lady and I have traveled from the\x01",
            "Empire with the intention of purchasing\x01",
            "septium crystals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, recently, monsters have been\x01",
            "sighted near the town...or so I've heard.\x01",
            "I can't help but shake thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0B")

    TalkEnd(0xFE)
    Return()

    # Function_9_31D9 end

    def Function_10_3D0F(): pass

    label("Function_10_3D0F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3E73")

    ChrTalk(
        0xB,
        (
            "Oh, would you look at the time?\x01",
            "I do believe it's time for supper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Letina, go retrieve my meal from\x01",
            "the owner and bring it back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um... There is barely anyone staying\x01",
            "at the inn, my lady. Why not eat at one\x01",
            "of the dining tables?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That requires far too much effort.\x01",
            "Shoo, now, shoo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Heehee...\x02",
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_3E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_402B")

    ChrTalk(
        0xB,
        (
            "Hohoho! This place truly deserves its\x01",
            "reputation as the leading septium mining\x01",
            "town on the entire continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "O-Of course, my lady. After all, you were\x01",
            "able to strike quite the alluring deal with\x01",
            "Mayor Bickson yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As things stand, obtaining those beautiful\x01",
            "septium crystals is only a matter of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was unsure of what to do, but no longer!\x01",
            "I'll be staying here until those crystals are\x01",
            "finally mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402B")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_10_3D0F end

    def Function_11_403A(): pass

    label("Function_11_403A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40CE")
    Jump("loc_4118")

    label("loc_40CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4118")

    label("loc_40EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_410E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4118")

    label("loc_410E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4118")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_435E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4158")
    Call(0, 16)
    Jump("loc_435E")

    label("loc_4158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42ED")

    ChrTalk(
        0xD,
        (
            "#0805FOh! H-Hey, everyone.\x02\x03",
            "#0809FAhaha... I didn't even see you walk\x01",
            "in. Here on police business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FYeah, more or less.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(Is it just me...or does it seem like\x01",
            "Estelle is forcing that smile?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F(I noticed, too. Her usual optimism\x01",
            "is kinda on the fritz.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0208F(I cannot tell whether she is simply\x01",
            "overwhelmed...or is experiencing\x01",
            "genuine sorrow...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_435E")

    label("loc_42ED")


    ChrTalk(
        0xD,
        (
            "#0809FW-Well...our break time is up!\x01",
            "We gotta get back to the highway!\x02\x03",
            "#0802FEveryone, keep your heads up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_403A end

    def Function_12_4366(): pass

    label("Function_12_4366")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43FA")
    Jump("loc_4444")

    label("loc_43FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_441A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4444")

    label("loc_441A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_443A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4444")

    label("loc_443A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4444")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_451B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4484")
    Call(0, 16)
    Jump("loc_451B")

    label("loc_4484")


    ChrTalk(
        0xE,
        (
            "#0903F(Sorry. I'd explain, but we'd be here for ages.)\x02\x03",
            "#0900F(Could you let Estelle be alone for now? It's\x01",
            "nothing against you guys, I promise.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_4366 end

    def Function_13_4523(): pass

    label("Function_13_4523")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45B7")
    Jump("loc_4601")

    label("loc_45B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45D7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4601")

    label("loc_45D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4601")

    label("loc_45F7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4601")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D0")

    ChrTalk(
        0xFE,
        (
            "Oh, nice to see you again. Good work\x01",
            "at busting those mafiosos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like you were even able to build\x01",
            "up quite the case against them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou mean Revache? Regardless of our success,\x01",
            "they were still acquitted after two days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha. That may be, but don't beat yourselves up over it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Replace the police with the bracers, and the\x01",
            "outcome wouldn't have changed, probably.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4886")

    label("loc_47D0")


    ChrTalk(
        0xFE,
        (
            "Ever since the attacks, we make sure to\x01",
            "patrol Mainz every now and then while\x01",
            "working on other jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guild might be busier than ever,\x01",
            "but it's something we have to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4886")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_4523 end

    def Function_14_488E(): pass

    label("Function_14_488E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4922")
    Jump("loc_496C")

    label("loc_4922")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4942")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_496C")

    label("loc_4942")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4962")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_496C")

    label("loc_4962")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_496C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A90")

    ChrTalk(
        0xFE,
        (
            "You all handled those monster\x01",
            "attacks pretty well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember not to get too caught up in your\x01",
            "victory, though. Always stay committed to\x01",
            "improving yourself and you'll go far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(Is he acknowledging the SSS...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4B77")

    label("loc_4A90")


    ChrTalk(
        0xFE,
        (
            "Never forget this. Success invites pride, and before\x01",
            "you know it, that very same pride could drown you.\x01",
            "If you let that happen, success becomes a pipe dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always stay committed to improving\x01",
            "yourself and you'll go far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B77")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_488E end

    def Function_15_4B7F(): pass

    label("Function_15_4B7F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C13")
    Jump("loc_4C5D")

    label("loc_4C13")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C33")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C5D")

    label("loc_4C33")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C53")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C5D")

    label("loc_4C53")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C5D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D41")

    ChrTalk(
        0xFE,
        "*glug*...*glug*...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aaaaaah! That's the stuff. Drinking\x01",
            "alone, right around noon, is one of\x01",
            "the best things life has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is just iced tea, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4D7C")

    label("loc_4D41")


    ChrTalk(
        0xFE,
        "*glug* *glug* *glug*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aaaaah, I can't get enough!\x02",
    )

    CloseMessageWindow()

    label("loc_4D7C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_4B7F end

    def Function_16_4D84(): pass

    label("Function_16_4D84")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_68(-8200, 750, -3800, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -6100, -750, -4050, 270)
    SetChrPos(0x102, -5950, -750, -5050, 270)
    SetChrPos(0x103, -5100, -750, -4050, 270)
    SetChrPos(0x104, -4950, -750, -5050, 270)
    OP_0D()

    ChrTalk(
        0xD,
        "#0808F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0906F#12PIf we've learned anything today, we know that he\x01",
            "seems like a genuinely respectable man.\x02\x03",
            "#0908FI guess it really was a misunderstanding on her\x01",
            "part. At least, that's what I want to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#0808F#11PI know... He's not a bad man,\x01",
            "that much is clear.\x02\x03",
            "And I'd never want to say that\x01",
            "it was all her fault...\x02\x03",
            "#0811FHey, Joshua... What do we do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0903F#12PEverything's okay, Estelle. This isn't\x01",
            "something we can solve just like that.\x01",
            "We knew that coming in.\x02\x03",
            "#0900FRemember? Before we came here, we\x01",
            "decided to take our time and deal with\x01",
            "the whole thing delicately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#0806F#11P...Yeah... I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F#11P(They must be having a serious conversation.\x01",
            "It'd be rude of us to interrupt...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6100, -750, -4550, 270)
    SetScenarioFlags(0x94, 4)
    EventEnd(0x5)
    Return()

    # Function_16_4D84 end

    def Function_17_5102(): pass

    label("Function_17_5102")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(3040, 1500, 1600, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x101, 2900, 0, 1900, 0)
    SetChrPos(0x102, 4100, 0, 1900, 0)
    SetChrPos(0x103, 2900, 0, 700, 0)
    SetChrPos(0x104, 4100, 0, 700, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#1200611V#1PHello again, you all.\x01",
            "Evening already, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200612V#1PLast bus leaves at eight.\x01",
            "Best hurry or you'll miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200613V#0100F#2PWe were actually thinking we would\x01",
            "spend the night in Mainz.\x02\x03",
            "#1200614VBy any chance, do you have a room\x01",
            "that would fit all of us? Preferably\x01",
            "with a table, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200615V#1PI've got the perfect room in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200616V#1PIt's always a delight to have youngsters\x01",
            "like yourselves stay with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1200617V#1PUp for some dinner, as well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200618V#0000F#2PWe'd love some.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200619V#1PThat's what I like to hear. I'll whip up\x01",
            "something great, don't you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1200620V#1PYour room is downstairs, down the hall and to\x01",
            "the left. Feel free to rest until dinner's ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200621V#0300F#4PThat's what I call hospitality. Thank ya, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200622V#0200F#4PIf you will excuse us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_5102 end

    SaveToFile()

Try(main)
