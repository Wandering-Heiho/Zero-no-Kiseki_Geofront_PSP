from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1000.bin",                # FileName
        "t1000",                    # MapName
        "t1000",                    # Location
        0x0041,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1000",                  # 0
        "Stewardess Salsa",       # 1
        "James",                  # 2
        "Nikita",                 # 3
        "Boy",                    # 4
        "Man",                    # 5
        "Woman",                  # 6
        "Tourist",                # 7
        "Bond",                   # 8
        "Creil",                  # 9
        "Sunita",                 # 10
        "Marie",                  # 11
        "Peter",                  # 12
        "Master Fisherman Lloyd", # 13
        "Kilika",                 # 14
        "Lechter",                # 15
        "Cruise Ship",            # 16
        "Passenger",              # 17
        "Passenger",              # 18
        "Passenger",              # 19
        "Passenger",              # 20
        "Passenger",              # 21
        "Passenger",              # 22
        "Passenger",              # 23
        "Passenger",              # 24
        "SE制御",                 # 25
        "To Theme Park",          # 26
        "To Residences",          # 27
    ))

    AddCharChip((
        "chr/ch28400.itc",                   # 00
        "chr/ch20600.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch27800.itc",                   # 04
        "chr/ch26800.itc",                   # 05
        "chr/ch24400.itc",                   # 06
        "chr/ch27600.itc",                   # 07
        "chr/ch33300.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch39000.itc",                   # 0A
        "apl/ch50165.itc",                   # 0B
        "apl/ch50169.itc",                   # 0C
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

    DeclNpc(-3740,   -4000,   -47180,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(15460,   -2000,   -24889,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(15479,   -2000,   -25989,  0,    385,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9600,    -4000,   -47930,  268,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(8069,    -4000,   -48130,  86,   385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(8699,    -4000,   -49430,  45,   385,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7000,   -2000,   -26329,  270,  385,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6340,   -4000,   -47330,  135,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6869,   -4000,   -48279,  45,   389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4769,   -4000,   -47900,  270,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-3809,   -4000,   -47520,  270,  389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(20559,   -5000,   -56500,  180,  277,  0x0, 0,   11,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(18040,   -5000,   -56500,  180,  277,  0x0, 0,   12,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-24500,  -4000,   -45660,  1200,    -24490,  -6000,   -38830,  0x007C, 0,  17, 0x0000)
    DeclActor(10350,   -3990,   -46410,  1200,    10350,   -2500,   -46410,  0x007C, 0,  27, 0x0000)
    DeclActor(-30180,  -4000,   -47980,  1200,    -30180,  -4000,   -47980,  0x007C, 0,  26, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "To Theme Park")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "To Residences")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_4E0",          # 00, 0
        "Function_1_598",          # 01, 1
        "Function_2_64A",          # 02, 2
        "Function_3_7AD",          # 03, 3
        "Function_4_8A4",          # 04, 4
        "Function_5_933",          # 05, 5
        "Function_6_9DB",          # 06, 6
        "Function_7_B18",          # 07, 7
        "Function_8_C0B",          # 08, 8
        "Function_9_C73",          # 09, 9
        "Function_10_D01",         # 0A, 10
        "Function_11_ECA",         # 0B, 11
        "Function_12_F48",         # 0C, 12
        "Function_13_F82",         # 0D, 13
        "Function_14_1084",        # 0E, 14
        "Function_15_10A1",        # 0F, 15
        "Function_16_1531",        # 10, 16
        "Function_17_169B",        # 11, 17
        "Function_18_1777",        # 12, 18
        "Function_19_26F3",        # 13, 19
        "Function_20_2748",        # 14, 20
        "Function_21_2774",        # 15, 21
        "Function_22_27D0",        # 16, 22
        "Function_23_282C",        # 17, 23
        "Function_24_2888",        # 18, 24
        "Function_25_28E4",        # 19, 25
        "Function_26_2909",        # 1A, 26
        "Function_27_2ABC",        # 1B, 27
    ))


    def Function_0_4E0(): pass

    label("Function_0_4E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_520"),
        (1, "loc_52C"),
        (2, "loc_538"),
        (3, "loc_544"),
        (4, "loc_550"),
        (5, "loc_55C"),
        (6, "loc_568"),
        (SWITCH_DEFAULT, "loc_574"),
    )


    label("loc_520")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_52C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_538")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_544")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_550")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_55C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_568")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_574")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_580")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_580")

    label("loc_597")

    Return()

    # Function_0_4E0 end

    def Function_1_598(): pass

    label("Function_1_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5A7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 18)

    label("loc_5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_649")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5C3")
    Jump("loc_649")

    label("loc_5C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5D1")
    Jump("loc_649")

    label("loc_5D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5DF")
    Jump("loc_649")

    label("loc_5DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_5ED")
    Jump("loc_649")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_61E")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_649")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_640")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_649")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_649")

    label("loc_649")

    Return()

    # Function_1_598 end

    def Function_2_64A(): pass

    label("Function_2_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_690")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1000_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x1, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_6B4")

    label("loc_690")

    SetMapObjFrame(0xFF, "t1000_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x0, 0x1)

    label("loc_6B4")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -24490, -6000, -38830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)

    label("loc_73D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A6")
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -30180, -4000, -47980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_7A6")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_64A end

    def Function_3_7AD(): pass

    label("Function_3_7AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_83A")

    ChrTalk(
        0xFE,
        (
            "The ship bound for Crossbell City\x01",
            "has recently departed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The next ship will arrive shortly,\x01",
            "so please be patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_8A0")

    ChrTalk(
        0xFE,
        "Thank you for using the cruise service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please enjoy a wonderful time\x01",
            "at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0")

    TalkEnd(0xFE)
    Return()

    # Function_3_7AD end

    def Function_4_8A4(): pass

    label("Function_4_8A4")

    TalkBegin(0xFE)
    TurnDirection(0x9, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    Call(0, 6)
    Jump("loc_92F")

    label("loc_8C0")


    ChrTalk(
        0xFE,
        (
            "Hahaha... I told my wife I was just going\x01",
            "on a business trip, so there's nothing you need\x01",
            "to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92F")

    TalkEnd(0xFE)
    Return()

    # Function_4_8A4 end

    def Function_5_933(): pass

    label("Function_5_933")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94F")
    TurnDirection(0xA, 0x9, 0)
    Call(0, 6)
    Jump("loc_9D7")

    label("loc_94F")


    ChrTalk(
        0xFE,
        (
            "I've been interested in this Schwarze\x01",
            "Auction for quite a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heehee... I'm lucky that he asked me\x01",
            "to be his plus one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D7")

    TalkEnd(0xFE)
    Return()

    # Function_5_933 end

    def Function_6_9DB(): pass

    label("Function_6_9DB")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "Tonight, we party at the speaker's place!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll make sure to get you the most precious of\x01",
            "gems, no matter how much money I have to flaunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What a bad boy. What do you think your\x01",
            "wife would have to say about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha... Nikita, didn't we promise not to talk\x01",
            "about her tonight?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_9DB end

    def Function_7_B18(): pass

    label("Function_7_B18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2")

    ChrTalk(
        0xFE,
        (
            "That young man practically\x01",
            "flew off the ferry just now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was he looking forward to Mishelam that much?\x01",
            "His enthusiasm is almost contagious!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C07")

    label("loc_BC2")


    ChrTalk(
        0xFE,
        (
            "My dad's with me today, so we'll make\x01",
            "sure to have lots of fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C07")

    TalkEnd(0xFE)
    Return()

    # Function_7_B18 end

    def Function_8_C0B(): pass

    label("Function_8_C0B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Should we skip straight to the theme park?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Today, I promise to ride any ride you want.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_C0B end

    def Function_9_C73(): pass

    label("Function_9_C73")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, darling. Are you putting on your\x01",
            "brave face for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, then, we'll make sure to ride\x01",
            "the especially scary ones today.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_C73 end

    def Function_10_D01(): pass

    label("Function_10_D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37")

    ChrTalk(
        0xFE,
        (
            "I thought it'd be fun to come here after\x01",
            "enjoying the festivities in the city, but it's\x01",
            "going to get dark soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. I guess I'll just check out the\x01",
            "stores for a bit and then head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to avoid the rush of people who\x01",
            "will take the last ferry back at all costs.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_EC6")

    label("loc_E37")


    ChrTalk(
        0xFE,
        (
            "I probably won't get to do much,\x01",
            "considering I got here late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll go check out the stores for a bit\x01",
            "and then head back to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC6")

    TalkEnd(0xFE)
    Return()

    # Function_10_D01 end

    def Function_11_ECA(): pass

    label("Function_11_ECA")

    TalkBegin(0xFE)

    ChrTalk(
        0xF,
        (
            "It was a joy to spend the day here\x01",
            "with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Maybe taking a breather every now\x01",
            "and then isn't too bad.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_ECA end

    def Function_12_F48(): pass

    label("Function_12_F48")

    TalkBegin(0xFE)

    ChrTalk(
        0x10,
        (
            "The hotel was fully booked...\x01",
            "How depressing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_F48 end

    def Function_13_F82(): pass

    label("Function_13_F82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FDE")

    ChrTalk(
        0x11,
        (
            "Hopefully, Father and Mother decide to\x01",
            "take me here again sometime...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1080")

    label("loc_FDE")


    ChrTalk(
        0x11,
        (
            "Father said he still has to finish up some\x01",
            "work, so we have to go back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, Marie is very tired, too.\x01",
            "Maybe going home isn't such\x01",
            "a bad idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1080")

    TalkEnd(0xFE)
    Return()

    # Function_13_F82 end

    def Function_14_1084(): pass

    label("Function_14_1084")

    TalkBegin(0xFE)

    ChrTalk(
        0x12,
        "#1SFunyaaa...#3S\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1084 end

    def Function_15_10A1(): pass

    label("Function_15_10A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120A")

    ChrTalk(
        0xFE,
        "Oh, Lloyd! Come to fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still have to scratch that itch from the\x01",
            "fishing tournament? I can't blame you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, do you have any bait on you?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x187, 5)

    ChrTalk(
        0xFE,
        "It's not much, but I'm willing to share.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, well, I wish you the best of luck!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1205")
    SetScenarioFlags(0xD9, 1)

    label("loc_1205")

    Jump("loc_152D")

    label("loc_120A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x187, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1322")

    ChrTalk(
        0xFE,
        (
            "Did you run out of bait, Lloyd?\x01",
            "Let me see here...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x187, 2)

    ChrTalk(
        0xFE,
        "It's not much, but hopefully this helps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're a man after my own heart, Lloyd!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD9, 1)
    Jump("loc_152D")

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_13A6")

    ChrTalk(
        0xFE,
        (
            "Darn, it looks like the current's not\x01",
            "working in my favor now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess that means it's time to\x01",
            "call it a day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152D")

    label("loc_13A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_152D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(
        0xFE,
        (
            "Liberl sure is blessed to have an angler like\x01",
            "Lloyd. Even now, he knew fishing over on\x01",
            "the opposite shore was the right call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, when it comes to fishing, his\x01",
            "intuition is nothing short of miraculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The amount of fish he's managed to catch\x01",
            "today is incredible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_152D")

    label("loc_14DA")


    ChrTalk(
        0xFE,
        (
            "Haha, when it comes to fishing, his\x01",
            "intuition is nothing short of miraculous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152D")

    TalkEnd(0xFE)
    Return()

    # Function_15_10A1 end

    def Function_16_1531(): pass

    label("Function_16_1531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0xFE,
        "Hmm, I think it's time to call it a day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd say I caught an okay haul. I'm especially\x01",
            "proud of that gluttonous bass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1697")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1697")

    ChrTalk(
        0xFE,
        (
            "After the Anniversary Festival ends, I plan\x01",
            "to return home to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to check out as many fishing holes\x01",
            "and try out as many different fishing styles\x01",
            "as I can while in Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1697")

    TalkEnd(0xFE)
    Return()

    # Function_16_1531 end

    def Function_17_169B(): pass

    label("Function_17_169B")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt's time to turn Mishelam into Fishelam.\x02",
    )

    CloseMessageWindow()
    OP_68(-23140, -2400, -43580, 1500)
    MoveCamera(315, 36, 0, 1500)
    OP_6E(200, 1500)
    SetCameraDistance(50000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1772")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_1772")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_17_169B end

    def Function_18_1777(): pass

    label("Function_18_1777")

    EventBegin(0x0)
    OP_E5()
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch07300.itc", 0x1F)
    LoadChrToIndex("chr/ch20600.itc", 0x20)
    LoadChrToIndex("chr/ch20200.itc", 0x21)
    LoadChrToIndex("chr/ch20300.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadChrToIndex("chr/ch21300.itc", 0x24)
    LoadChrToIndex("chr/ch21200.itc", 0x25)
    LoadChrToIndex("chr/ch27700.itc", 0x26)
    LoadChrToIndex("chr/ch23600.itc", 0x27)
    SetChrPos(0x101, -7250, -4000, -40000, 180)
    SetChrPos(0x102, -7250, -4000, -40000, 180)
    SetChrPos(0x103, -7250, -4000, -40000, 180)
    SetChrPos(0x104, -7250, -4000, -40000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -7250, -4000, -40000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x15, -7250, -4000, -40000, 180)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -45000, -5500, -38200, 0)
    OP_D3(0x17, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x19, 0x21)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, -7250, -4000, -40000, 180)
    SetChrPos(0x19, -7250, -4000, -40000, 180)
    SetChrPos(0x1A, -7250, -4000, -40000, 180)
    SetChrPos(0x1B, -7250, -4000, -40000, 180)
    SetChrPos(0x1C, -7250, -4000, -40000, 180)
    SetChrPos(0x1D, -7250, -4000, -40000, 180)
    SetChrPos(0x1E, -7250, -4000, -40000, 180)
    SetChrPos(0x1F, -7250, -4000, -40000, 180)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    PlaceName2(340, 200, "c_plac20", 0x0, 3000)
    FadeToBright(2000, 0)
    OP_68(20240, -2400, -36530, 0)
    MoveCamera(334, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(64730, 0)
    OP_68(-1240, -2400, -36530, 15000)
    BeginChrThread(0x20, 1, 0, 25)

    def lambda_1AF5():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1AF5)
    WaitChrThread(0x17, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    Sound(478, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    OP_6F(0x1)
    EndChrThread(0x20, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(-5240, -1300, -48610, 0)
    MoveCamera(327, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(31570, 0)
    OP_0D()
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1A, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1C, 3, 0, 19)
    Sleep(1000)
    OP_63(0x16, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    BeginChrThread(0x1D, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x15, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x1F, 3, 0, 19)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 24)
    Fade(1000)
    OP_68(-530, -1300, -54200, 0)
    MoveCamera(326, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13040, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_0D()
    Sleep(500)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x1F, 0x3)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x15, 0x3)
    OP_E6()

    ChrTalk(
        0x101,
        (
            "#3500318V#0008F#5PMishelam...\x02\x03",
            "#3500319V#0006FI'm not sure if I could even dream\x01",
            "up something this beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500320V#0203F#5PThis was simply a high-class resort area\x01",
            "before the IBC began investing in its\x01",
            "commercial development.\x02\x03",
            "#3500321V#0200FThe hotel and theme park were added\x01",
            "around two years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500322V#0104F#5PAnd since then, both this place and Arc en Ciel\x01",
            "became must-see tourist attractions. With it in\x01",
            "front of me, I can see why.\x02\x03",
            "#3500323V#0100FThe hotel should be directly ahead of us,\x01",
            "with the first floor serving as a mall.\x02\x03",
            "#3500324VThere, you can find restaurants, boutiques,\x01",
            "and even jewelry shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500325V#0306F#5PYeah, but the prices are so freakin' high\x01",
            "that you can't really enjoy it unless you\x01",
            "have the dough to pay.\x02\x03",
            "#3500326V#0300FI've taken a few dates to the theme park\x01",
            "and one of the restaurants here before...\x01",
            "Good fun, but waaaay overpriced.\x02\x03",
            "#3500327VSo what's the plan, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2040():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2040)

    def lambda_204D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_204D)
    Sleep(100)

    def lambda_205D():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_205D)

    def lambda_206A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_206A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#3500328V#0003F#12PHmm...\x02\x03",
            "#3500329V#0001FLet's scout out the area surrounding\x01",
            "the auction venue, first.\x02\x03",
            "#3500330VIt's being held at Speaker Hartmann's\x01",
            "mansion, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500331V#0100F#6PCorrect. If we take a left inside of the mall,\x01",
            "we'll end up in the residential area, which\x01",
            "is lined with all sorts of mansions.\x02\x03",
            "#3500332VThe speaker's should be the furthest back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500333V#0004F#12PGood to know.\x02\x03",
            "#3500334V#0000FOnce we do that, we should take a look\x01",
            "around the other areas while we still can.\x02\x03",
            "#3500335VWe might even run into more auction\x01",
            "attendees, like that Lechter guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500336V#0202F#5PIt is likely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500337V#0106F#6PSpeaking of that man...\x02\x03",
            "#3500338V#0101FI wonder if he's really an Erebonian noble.\x01",
            "His diction and behavior doesn't quite suit\x01",
            "that picture, but I could be mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500339V#0303F#5PEh, who knows?\x02\x03",
            "#3500340V#0301FOn the other side of the coin, maybe his\x01",
            "claim about reppin' the Blood and Iron\x01",
            "Chancellor was the lie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500341V#0006F#12PNo matter his background, an oddball like\x01",
            "him was invited as a guest.\x02\x03",
            "#3500342V#0013FIt's safe to say that we can't approach the\x01",
            "Schwarze Auction with our usual mindset.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(13290, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x0, -2000, -4000, -50200, 90)
    SetScenarioFlags(0xA4, 0)
    OP_29(0x47, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2633")
    OP_29(0x18, 0x4, 0x40)
    Jump("loc_2645")

    label("loc_2633")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2645")
    OP_29(0x18, 0x4, 0x40)

    label("loc_2645")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2657")
    OP_29(0x1A, 0x4, 0x40)

    label("loc_2657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2675")
    OP_29(0x1C, 0x4, 0x40)
    Jump("loc_2687")

    label("loc_2675")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2687")
    OP_29(0x1C, 0x4, 0x40)

    label("loc_2687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2699")
    OP_29(0x1E, 0x4, 0x40)

    label("loc_2699")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AB")
    OP_29(0x21, 0x4, 0x40)

    label("loc_26AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26C9")
    OP_29(0x22, 0x4, 0x40)
    Jump("loc_26DB")

    label("loc_26C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DB")
    OP_29(0x22, 0x4, 0x40)

    label("loc_26DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x23, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26ED")
    OP_29(0x23, 0x4, 0x40)

    label("loc_26ED")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_1777 end

    def Function_19_26F3(): pass

    label("Function_19_26F3")


    def lambda_26F8():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26F8)
    Sleep(500)

    def lambda_2715():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2715)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_272E():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_272E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_26F3 end

    def Function_20_2748(): pass

    label("Function_20_2748")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2773")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)
    Jump("Function_20_2748")

    label("loc_2773")

    Return()

    # Function_20_2748 end

    def Function_21_2774(): pass

    label("Function_21_2774")


    def lambda_2779():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2779)
    Sleep(500)

    def lambda_2796():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2796)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_27AF():
        OP_95(0xFE, -2940, -4000, -50580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_2774 end

    def Function_22_27D0(): pass

    label("Function_22_27D0")


    def lambda_27D5():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27D5)
    Sleep(500)

    def lambda_27F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_280B():
        OP_95(0xFE, -4019, -4000, -51400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_280B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_27D0 end

    def Function_23_282C(): pass

    label("Function_23_282C")


    def lambda_2831():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2831)
    Sleep(500)

    def lambda_284E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_284E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2867():
        OP_95(0xFE, -4680, -4000, -49050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2867)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_23_282C end

    def Function_24_2888(): pass

    label("Function_24_2888")


    def lambda_288D():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_288D)
    Sleep(500)

    def lambda_28AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28AA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_28C3():
        OP_95(0xFE, -5640, -4000, -50180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28C3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_24_2888 end

    def Function_25_28E4(): pass

    label("Function_25_28E4")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_25_28E4 end

    def Function_26_2909(): pass

    label("Function_26_2909")

    EventBegin(0x0)
    Fade(500)
    OP_68(-28230, -2400, -50050, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34310, 0)
    SetChrPos(0x101, -28000, -4000, -48730, 270)
    SetChrPos(0x102, -28000, -4000, -47510, 225)
    SetChrPos(0x103, -26240, -4000, -49940, 270)
    SetChrPos(0x104, -26310, -4000, -48550, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_299C")
    SetChrPos(0x151, -25030, -4000, -49530, 270)

    label("loc_299C")

    StopEffect(0x0, 0x2)
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
            scpstr(SCPSTR_CODE_ITEM, 0x34C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34C, 1)

    ChrTalk(
        0x101,
        "#12P#0005FOh, is this it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FYeah, it may be the engagement\x01",
            "ring Toma told us about earlier.\x02\x03",
            "#0100FLet's bring it to his hotel room later\x01",
            "so he can confirm it.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x1)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -28000, -4000, -48730, 270)
    EventEnd(0x5)
    Return()

    # Function_26_2909 end

    def Function_27_2ABC(): pass

    label("Function_27_2ABC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Cruise Ship Schedule\x01\x01",
            " We'll be awaiting your next visit!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_2ABC end

    SaveToFile()

Try(main)
